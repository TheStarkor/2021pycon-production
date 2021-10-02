# Crawling

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