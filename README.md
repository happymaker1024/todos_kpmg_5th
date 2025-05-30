# fastapi app 구현하기 kpmg_5th
- todo앱
- face recognition
- 실습 날짜 : 2025. 05. 30

## 실습환경
```
- 윈도우10
- conda 가상환경
- python 버전 3.12
```

## 설치라이브리
```
pip install fastapi
pip install "uvicorn[standard]"
- html 템플릿
pip install jinja2 python-multipart
- ORM 
pip install sqlalchemy 
```
## face_recognition
```
- face_recognition 라이브러리 설치를 위해 필요함
conda install -c conda-forge dlib -y
conda install -c conda-forge mkl -y
 
- 얼굴 인식 라이브러리
conda install -c conda-forge face_recognition -y

- 이미지 처리 라이브러리 (cv2)
pip install opencv-python 
``` 

# 실행방법
```
python app_start.py
```
