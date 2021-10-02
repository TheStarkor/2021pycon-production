# Image Upload with S3

## 실행

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