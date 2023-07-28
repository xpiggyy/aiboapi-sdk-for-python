# aiboapi: Unofficial API for AIBO - Python


aiboapi は、AIBO API にリクエストを送信するための Python 3 ライブラリです。 認証に aibo の access_token を使用して aibo web api クライアントのリクエストをエミュレートします。<br>
※eventid による api リクエストも必要であれば実装します

# Install package

```sh
$ pip install git+https://github.com/xpiggyy/aiboapi-sdk-for-python
```

# Usage

```py
from aiboapi import Aibo

token = 'token is here!!'
a = Aibo(token)

a.get_devices()
a.get_nickname()

a.ask_action(API_NAME: str, arguments: str)
```

# Methods
| Method            |   Parameters |   Description | 
| ------------------- | ------------------ | ------------------ |
|   get_devices    |    None    |    deviceIdを取得します。 |
|   ask_action  |   API_NAME: str, arguments: str = None  |   aiboに行動を指示します。|

# API_NAME List

### Action API

Action API は arguments が必要です。<br>
すべての arguments およびレスポンスパラメータの詳細については、[API Documentation](https://developer.aibo.com/jp/docs#action-api)を確認してください。<br>

| API_NAME            | arguments Required | Description                                                                                                    |
| ------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------- |
| set_mode     | Yes                | aibo が指示待ち中になるかどうかを指定します。                                                                                   |
| approach_object     | Yes                | 指定されたものに近づきます。                                                                                   |
| approach_person     | Yes                | 人に指定された距離まで近づきます。                                                                             |
| change_posture      | Yes                | 指定された姿勢をとります。すでにその姿勢のときは、何もせずに終了します。                                       |
| chase_object        | Yes                | 指定されたものを見続けます。                                                                                 |
| chase_person        | Yes                | 人を見続けます。                                                                                               |
| explore             | Yes                | 指定された時間歩き回ります。                                                                                   |
| find_object         | Yes                | 指定されたものを探します。                                                                                     |
| find_person         | Yes                | 人を探します。                                                                                                 |
| get_close_to_object | Yes                | 近くにある指定されたものに対して、かなりそばまで近づきます。ApproachObject で近づいたあとに使用してください。  |
| kick_object         | Yes                | 指定されたものを蹴ったりヘディングしたりします。                                                               |
| move_along_circle   | Yes                | 円弧を描きながら歩きます。                                                                                     |
| move_direction      | Yes                | 指定された方向へ指定された距離を歩きます。                                                                     |
| move_forward        | Yes                | 指定された距離を前後に歩きます。                                                                               |
| move_head           | Yes                | 指定された向きへ、指定された速さで首と顔を動かします。                                                         |
| move_sideways       | Yes                | 指定された距離を左右に横歩きします。                                                                           |
| move_to_position    | Yes                | 指定された場所へ向かいます。そのとき認識している地図に指定された場所が存在している場合、その場所へ向かいます。 |
| play_bone           | Yes                | 専用アクセサリーのアイボーンを使って遊びます。ApproarchObject で近づいた後に使用してください。                 |
| play_dice           | Yes                | 専用アクセサリーのサイコロを使い、指定された遊びを行います。ApproarchObject で近づいた後に使用してください。   |
| play_motion         | Yes                | 指定された動作を行います。                                                                                     |
| play_trick          | Yes                | 指定されたふるまい（ひと続きの動作）を行います。                                                               |
| release_object      | Yes                | くわえているものを離します。                                                                                   |
| stay                | Yes                | 指定された時間、待機します。                                                                                   |
| turn_around         | Yes                | 指定された角度だけその場で回ります。                                                                           |

---

### Cognition API

Cognition API は arguments が不必要です。<br>
すべての arguments およびレスポンスパラメータの詳細については、[API Documentation](https://developer.aibo.com/jp/docs#action-api)を確認してください。<br>

| API_NAME             | arguments Required | Description                                                                                          |
| -------------------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| approach_object      | No                 | 指定されたものに近づきます。                                                                         |
| biting_status        | No                 | ものをくわえているかどうかを取得します。                                                             |
| body_touched_status  | No                 | 体のどの部分を触られているのかを取得します。                                                         |
| found_objects_status | No                 | 認識している人やものについて取得します。                                                             |
| hungry_status        | No                 | バッテリー残量を取得します。                                                                         |
| name_called_status   | No                 | 自分の名前を呼ばれたかどうかを取得します。名前を呼ばれていた場合、呼ばれた方向も合わせて取得します。 |
| paw_pads_status      | No                 | 肉球が押されているかどうかを取得します。                                                             |
| posture_status       | No                 | とっている姿勢を取得します。                                                                         |
| sleepy_status        | No                 | 眠さを取得します。                                                                                   |
| voice_command_status | No                 | 反応した言葉を取得します。                                                                           |
