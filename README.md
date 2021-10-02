# 2021pycon-production

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FTheStarkor%2F2021pycon-production&count_bg=%23FFE873&title_bg=%23646464&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://www.notion.so/thestar/e6f6b641bd8f493085e5f044182dcae3)

`PyCon 2021 - 매일이 새로운 초기 스타트업 파이썬과 함께라면?`의 레포지토리입니다. 짧은 강연의 보조자료로 필요한 환경 설정 및 시간이 부족하여 강연에서 다루지 못한 부분이 많아 추가 예제를 포함하고 있습니다.

## 환경 설정

### Requirements
- python ([download](https://www.python.org/downloads/))
- Docker ([설명](https://thestar.notion.site/Docker-bf23af854d354a918c6739f9251e9f39), [docker desktop download](https://www.docker.com/products/docker-desktop))
- Node ([download](https://nodejs.org/ko/download/))
- AWS 계정 ([AWS console](https://console.aws.amazon.com/console/home))

### Infra 설정
- [EC2](https://thestar.notion.site/EC2-7fde9b510fdb49d6917bdb27ec1babd7)
- [CodeStar](https://thestar.notion.site/CodeStar-739b28470daf4b569e68c7157faca49b)
- Serverless framework
  - `$ npm install -g serverless`

## 예제

서비스에서 주로 많이 사용하는 image upload 서버, 크롤링 그리고 Gateway를 예제로 작성하였습니다. 라이브러리 설치, aws 연결 및 환경 설정들에 대한 예시를 포함하고 있습니다.

### Image Upload with S3

- [Flask(EC2 or CodeStar)](https://github.com/TheStarkor/2021pycon-production/tree/main/upload-flask)

### 데이터 크롤링

- [Serverless](https://github.com/TheStarkor/2021pycon-production/tree/main/crawling)

### API Gateway

- [Serverless](https://github.com/TheStarkor/2021pycon-production/tree/main/gateway)

