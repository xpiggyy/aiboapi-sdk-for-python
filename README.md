# aiboapi: Unofficial API for AIBO - Python

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

aiboapi は、AIBO API にリクエストを送信するための Python 3 ライブラリです。 認証にaiboの access_token を使用して aibo web api クライアントのリクエストをエミュレートします。

# Install package
```sh
$ pip install git+https://github.com/xpiggyy/aiboabi-sdk-for-python
```


# Usage

```py
from aibo import Aibo

token = 'xxxxxxx'
aibo = Aibo(token)
aibo.aibo_control(API_NAME: str, arguments: Dict)
```

# API_NAME List
### action_api 
action_apiは arguments が必要です。<br>
すべての arguments およびレスポンスパラメータの詳細については、[API Documentation](https://developer.aibo.com/jp/docs#action-api)を確認してください。<br>

|   API_NAME  |    arguments Required    |   Description   |  
|---|---|---|
|   approach_object   | Yes  |  指定されたものに近づきます。 |
|   approach_person |   Yes    |   人に指定された距離まで近づきます。  |
|   change_posture    | Yes |   指定された姿勢をとります。すでにその姿勢のときは、何もせずに終了します。    |





