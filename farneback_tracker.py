import cv2
import numpy as np

# 전역 변수 설정
roi = None  # 선택된 관심 영역
tracking = False  # 객체 추적 활성화 여부
roi_hist = None  # 관심 영역의 히스토그램

# 마우스 콜백 함수
def select_roi(event, x, y, flags, param):
    global roi, tracking
    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 클릭 시
        roi = (x, y, x, y)  # ROI 시작점
        tracking = False
    elif event == cv2.EVENT_MOUSEMOVE and roi is not None:  # 드래그로 영역 선택
        roi = (roi[0], roi[1], x, y)  # ROI 업데이트
    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 버튼 떼기
        roi = (roi[0], roi[1], x, y)  # ROI 최종 설정
        tracking = True  # 추적 활성화

# 초기화
cap = cv2.VideoCapture(0)  # 실시간 비디오 스트림
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", select_roi)

# 광류 설정
prev_gray = None  # 이전 프레임 저장용
mask = None  # 광류 시각화 마스크

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 현재 프레임 복사 및 그레이스케일 변환
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if roi and tracking:
        x0, y0, x1, y1 = roi
        x0, y0, x1, y1 = max(x0, 0), max(y0, 0), min(x1, frame.shape[1]), min(y1, frame.shape[0])
        roi_frame = frame_gray[y0:y1, x0:x1]

        # 첫 프레임에서는 광류 초기화
        if prev_gray is None:
            prev_gray = frame_gray
            mask = np.zeros_like(frame)
            mask[..., 1] = 255  # 색상(녹색) 채널 설정

        # 군나르 파너백 광류 계산
        flow = cv2.calcOpticalFlowFarneback(prev_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # 관심 영역에서의 이동 벡터 추출
        roi_flow = flow[y0:y1, x0:x1]
        dx, dy = roi_flow[..., 0], roi_flow[..., 1]

        # 관심 영역 중심 이동량 시각화
        avg_dx = int(np.mean(dx))
        avg_dy = int(np.mean(dy))
        cv2.arrowedLine(frame, (x0 + (x1 - x0) // 2, y0 + (y1 - y0) // 2),
                        (x0 + (x1 - x0) // 2 + avg_dx, y0 + (y1 - y0) // 2 + avg_dy),
                        (0, 0, 255), 2)

        # 이전 프레임 업데이트
        prev_gray = frame_gray

    # 선택된 ROI 시각화
    if roi:
        x0, y0, x1, y1 = roi
        cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)

    cv2.imshow("Video", frame)

    # ESC 키로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()