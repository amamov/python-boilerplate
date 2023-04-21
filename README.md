# 2023 Python Boilerplate

## Getting Started

1. `python3 -m venv ./venv`

2. `source venv/bin/activate`

3. `pip3 install -r requirements.txt`

4. `python3 run.py`

## gspread_user_key 인증키 발급

1. [Google Cloud Console](https://console.cloud.google.com/apis/api/drive.googleapis.com/)에서 프로젝트 생성 후, 사용자 인증 정보 만들기에서 서비스 계정을 클릭한다.

2. 서비스 계정을 만들고 라이브러리에서 구글 드라이브와 구글 스프레드 시트 사용을 클릭한다.

3. 만든 서비스 계정의 이메일 (`__@__.iam.gserviceaccount.com`)을 복사해서 스프레드 시트 share에 추가한다.

4. 서비스 계정에서 Action(작업)에서 Manage Keys(키 관리)에 들어가서 JSON 파일의 비공개 키(`gspread_user_key.json`)를 다운 받는다.
