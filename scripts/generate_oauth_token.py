#!/usr/bin/env python3
"""
Google OAuth Refresh Token を取得するスクリプト

使用方法:
    python scripts/generate_oauth_token.py
"""

import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow

def main():
    # GitHub Secrets から取得する値（または環境変数から）
    CLIENT_ID = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')

    if not CLIENT_ID or not CLIENT_SECRET:
        print("❌ エラー: 環境変数が設定されていません")
        print("\n以下の環境変数を設定してください:")
        print("  GOOGLE_OAUTH_CLIENT_ID")
        print("  GOOGLE_OAUTH_CLIENT_SECRET")
        print("\nまたは .env ファイルを作成してください:")
        print("  GOOGLE_OAUTH_CLIENT_ID=your_client_id")
        print("  GOOGLE_OAUTH_CLIENT_SECRET=your_client_secret")
        sys.exit(1)

    SCOPES = ['https://www.googleapis.com/auth/drive']

    # OAuth 2.0 credentials 設定
    client_config = {
        "installed": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"]
        }
    }

    print("\n" + "="*80)
    print("🔐 Google OAuth Refresh Token 取得")
    print("="*80 + "\n")

    try:
        flow = InstalledAppFlow.from_client_config(client_config, SCOPES)

        # ブラウザで認証（ローカルサーバーを起動）
        print("ブラウザが自動で開きます...\n")
        creds = flow.run_local_server(port=8080, open_browser=True)

        if creds.refresh_token:
            print("\n" + "="*80)
            print("✅ 取得成功！")
            print("="*80)
            print(f"\n📋 新しい Refresh Token:\n{creds.refresh_token}\n")
            print("="*80)
            print("\n📝 次のステップ:")
            print("1. 上記の Refresh Token をコピー")
            print("2. GitHub リポジトリの Settings → Secrets and variables → Actions")
            print("3. GOOGLE_OAUTH_REFRESH_TOKEN を編集")
            print("4. 新しい Token を貼り付けて保存")
            print("="*80 + "\n")

            return 0
        else:
            print("❌ Refresh Token を取得できませんでした")
            return 1

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
