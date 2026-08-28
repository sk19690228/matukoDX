# マツコ・デラックス思考パターン返信文作成アプリ

Google Drive に保存された対象ポスト一覧（Markdown）を読み込み、各ポストへの
Xリプライ文をマツコ・デラックスの思考パターンで3パターン自動作成し、
GitHub Pages のレビューページで確認・手動投稿できるようにするアプリです。

自動投稿は行いません。投稿はリポジトリのオーナーが一覧ページを見て、
気に入ったバリアントをコピーし、手動で実行する運用です。

## ドキュメント

- [docs/REPLY_BOT_SETUP.md](./docs/REPLY_BOT_SETUP.md): 認証情報（Google Drive / X API）のセットアップ手順
- [docs/MOBILE_POSTING.md](./docs/MOBILE_POSTING.md): スマホからの一覧確認・投稿手順
- [docs/HOUSE_STYLE.md](./docs/HOUSE_STYLE.md): リプライ文生成ルール（マツコ・デラックス思考パターン）

## 構成

```
.
├── main.py                          # ローカル実行用のエントリポイント
├── requirements.txt
├── docs/
├── scripts/
│   ├── drive_reply_common.py        # Drive連携・パース・共通ユーティリティ
│   ├── dump_markdown.py             # 当日分Markdownを取得しActionsログに出力
│   ├── generate_pages_list.py       # レビュー用 public/index.html を生成
│   ├── manual_post.py               # 指定tweet_idへ手動投稿を実行
│   └── get_google_refresh_token.py  # OAuthリフレッシュトークン取得（ローカル1回のみ）
├── results/
│   ├── replies_YYYYMMDD.json        # {tweet_id: [variant1, variant2, variant3]}
│   └── manual_reply_status_YYYYMMDD.json  # 投稿済み/失敗の状態記録
├── public/                          # generate_pages_list.py が生成する静的ページ（gitignore対象）
└── .github/workflows/
    ├── dump_markdown.yml            # Driveの当日分MarkdownをActionsログに出力（手動実行）
    ├── publish_list.yml             # レビューページを生成しGitHub Pagesへデプロイ（定期＋手動）
    └── manual_post.yml              # 指定ポストへ手動投稿（手動実行）
```

セットアップ手順は [docs/REPLY_BOT_SETUP.md](./docs/REPLY_BOT_SETUP.md) を参照してください。
