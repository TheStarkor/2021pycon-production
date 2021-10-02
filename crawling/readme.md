# Crawling

### 실행
1. profile 변경
  `serverless.yml` 내부 `provider.profile
2. `serverless-python-requirements`플러그인 설치 후 deploy (docker 실행중인 환경)
```
$ npm i
$ sls deploy
```

### `Serverless.yml`

```
service: crawling

frameworkVersion: '2'

provider:
  name: aws
  runtime: python3.8
  region: ap-northeast-2
  profile: pycon2021-demo
  lambdaHashingVersion: 20201221

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: non-linux

functions:
  main:
    handler: handler.main
    events:
      - schedule: rate(2 hours)
```

### 설명

간단하게 `requests`와 `bs4`를 사용하여 pycon2021 홈페이지(https://2021.pycon.kr)에 접속하여 img 태그들을 찾은 후 img의 src를 출력하는 서비스를 만들어 보았습니다. 그리고 크롤링의 경우 특정 시간 간격으로 진행되는 경우가 많으므로 `.yml`에 `schedule` 이벤트를 추가하여 2시간마다 해당 함수가 실행될 수 있도록 하였습니다. 이를 활용하여 특정 시간마다 함수를 실행하고 원하는 파일 형식으로 저장하거나 알림을 보내주는 기능을 제작 할 수 있습니다.

크롤링의 경우 `requests`, `bs4` 혹은 `selenium`과 같은 라이브러리를 사용합니다. 본 예제에서는 `requests`와 `bs4`를 사용하였습니다. 이렇게 외부 라이브러리를 사용할 경우 강연에서 언급한 `serverless-python-requirements` 플러그인을 설치하고 `docker`를 실행한 환경에서 deploy를 해 주어야 docker 환경에서 해당 라이브러리를 설치해서 서버에 배포가 진행됩니다.