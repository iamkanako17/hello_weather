# アプリ名

hello_weather

## 概要

旅行者が旅先で現在地の天気と観光地情報を見れるサイト。

## 設定

- OpenWeatherMapAPI にアクセスし、API_Key を取得して、環境変数に設定する。
- MacOS Catalina 以降の場合

```terminal
% vim ~/.zshrc
WEATHER_KEY='*******'
% source ~/.zshrc
```

- Flask に"os"をインポートして、設定した環境変数を呼び出す。

```Python3: main.py
import os
api_key = os.environ.get('****')
```

## 実装予定の内容

- 共有機能で、旅行前にサイトの情報を共有できる機能。
- 現在地周辺の観光地情報を提供。
- 星空指数の提供。

### version

- Flask 1.1.2
- Python 3.8.5
- BootsStrap 4.5.0
