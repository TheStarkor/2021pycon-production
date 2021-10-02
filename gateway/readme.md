# Gateway

### `Serverless.yml`

```
service: gateway

frameworkVersion: '2'

provider:
  name: aws
  runtime: python3.8
  region: ap-northeast-2
  lambdaHashingVersion: 20201221

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: non-linux
    
functions:
  gateway:
    handler: handler.main
    events:
      - http:
          path: pycon
          method: GET
```

### 설명