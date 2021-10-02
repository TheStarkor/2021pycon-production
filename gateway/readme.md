# Gateway

서비스를 운영하면서 다양한 micro-services를 제작하고 사용하거나 webhooks를 사용할 일이 있습니다. 이 경우 각 기능별 url을 정리하여 호출해도 되지만, proxy 혹은 gateway를 사용하여 통합하여 사용할 필요가 있습니다. 이렇게 하면 하나의 domain으로 통합해서 관리 할 수 있고 api 호출을 확인 할 수 있는 등의 장점이 있습니다. 또한, 내부 도메인을 보호할 수도 있습니다.

예제에서는 `requests` 라이브러리를 이용하여 pycon 홈페이지로 요청을 보내는 api를 제작하였습니다. 이렇게 외부 라이브러리를 사용할 경우 강연에서 언급한 `serverless-python-requirements` 플러그인을 설치하고 `docker`를 실행한 환경에서 deploy를 해 주어야 docker 환경에서 해당 라이브러리를 설치해서 서버에 배포가 진행됩니다. 
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
service: gateway

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
  gateway:
    handler: handler.main
    events:
      - http:
          path: pycon
          method: GET
```