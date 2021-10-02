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
