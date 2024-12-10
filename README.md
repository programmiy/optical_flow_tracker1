
---

# **optical_flow_tracker**

### **Description**
FlowFinder는 실시간 비디오에서 특정 객체를 선택하고, 배경과 분리하여 객체의 움직임을 추적하는 도구입니다.  
군나르 파너백 알고리즘(Gunnar Farnebäck Optical Flow)을 활용하여, 사용자가 선택한 관심 영역(Region of Interest, ROI)의 움직임을 분석하고 추출합니다.

---

## **Features**
- 마우스를 사용한 실시간 객체 선택
- 객체의 광류 계산 및 이동 시각화
- 배경과 객체의 동적 분리
- 간단하고 직관적인 사용자 인터페이스

---

## **Installation**

### **Prerequisites**
- Python 3.8 이상
- OpenCV 라이브러리

### **Setup**
1. 이 저장소를 클론합니다:
   ```bash
   git clone https://github.com/programmiy/optical_flow_tracker1.git
   cd FlowFinder
   ```
2. 필요한 Python 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**
1. 프로젝트 디렉토리에서 스크립트를 실행합니다:
   ```bash
   python farneback_tracker.py
   ```
2. 프로그램 실행 후:
   - 마우스를 사용하여 관심 영역(ROI)을 드래그하여 선택합니다.
   - 선택된 객체의 움직임이 추적, 추출됩니다.
3. ESC 키를 눌러 프로그램을 종료합니다.

---

## **Demo**
실행 화면 예시:
- ROI 선택 및 객체 이동 추적이 화면에 시각화됩니다.
  
(데모 이미지를 삽입하거나 동영상 링크 추가)
아직 없음
---

## **Technologies Used**
- **Python**
- **OpenCV**
- **Gunnar Farnebäck Optical Flow Algorithm**

---

## **Contributing**
기여를 환영합니다!  
버그 리포트, 피드백, 또는 기능 제안은 [Issues](https://github.com/programmiy/optical_flow_tracker1/issues)에 남겨주세요.

---

## **License**
이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.

---

## **Acknowledgements**
- 군나르 파너백(Gunnar Farnebäck) 알고리즘을 기반으로 한 Optical Flow 구현.
- big thx to opencv

---


