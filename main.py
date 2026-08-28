"""
ローカル環境で一覧ページ生成を実行するためのエントリポイント
（GitHub Actionsを使わずに動作確認したいときに使う）。

事前に GOOGLE_OAUTH_CLIENT_ID / GOOGLE_OAUTH_CLIENT_SECRET /
GOOGLE_OAUTH_REFRESH_TOKEN を .env または環境変数に設定しておくこと。
実行すると scripts/generate_pages_list.py と同じ処理で
public/index.html を生成する。
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts"))

from dotenv import load_dotenv

load_dotenv()

import generate_pages_list

if __name__ == "__main__":
    generate_pages_list.main()
