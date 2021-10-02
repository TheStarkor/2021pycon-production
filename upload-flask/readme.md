# Image Upload with S3

### 실행

1. `.flaskenv`파일 생성
  ```
  ACCESS_KEY=<ACCESS_KEY>
  SECRET_KEY=<SECRET_KEY>
  BUCKET_NAME=<BUCKET_NAME>
  ```

2. docker 실행
  ```
  $ docker build -t image-upload
  $ docker run -d -p 80:5000 image-upload
  ```

### 설명

form에 img를 키로 서버에 POST 요청을 보내면 s3에 이미지를 저장하고 s3에 저장된 uri를 response로 주는 API 서버입니다.

`boto3` 라이브러리를 사용하여 AWS와 연결하는데 이 때, 접근 권한을 위해 `ACCESS_KEY`, `SECREET_KEY`가 필요하고 이미지를 저장할 `BUCKET_NAME`이 필요합니다. 이 값들은 공개되면 안되는 경우가 있기 때문에 github과 같은 퍼블릭 레포에 해당 값을 제외하고 업로드 할 필요가 있습니다. 이를 위해 `.env`를 많이 사용하고 flask의 경우 `.flaskenv`를 사용하면 됩니다.

위 세팅을 하고 나면 S3에 접근이 가능하게 됩니다. 연결 이후 `upload_file()` 함수를 통해 이미지를 업로드 하면 되는데, 서비스에 사용할 이미지의 경우 권한 상관없이 이미지를 확인 할 수 있는 경우가 많아 `public-read` 권한을 추가하였습니다. 이를 제거할 경우 단순 url을 통한 접근이 금지됩니다.

해당 세팅을 하고 서버로 form에 이미지를 넣어 POST 요청을 보내면 아래 사진과 같이 성공적으로 파일을 업로드 하고 return을 하게 됩니다. 

![example](https://user-images.githubusercontent.com/45455072/135729994-d58e6001-02f6-4e4e-b1d8-e351b26eb90b.png)