# fxtradeapp

<pre>
<repository-root>/
│
├── .github/                     # GitHub Actionsや設定ファイル
│   └── workflows/
│       └── deploy.yaml          # CI/CD用のワークフロー
│
├── MyFunctionApp/               # Functionアプリケーションのルートディレクトリ
│   ├── __init__.py              # 必須: Functionのエントリポイント
│   ├── function.json            # 必須: Functionの設定ファイル
│   ├── host.json                # Function App全体の構成
│   ├── local.settings.json      # ローカル開発用設定ファイル
│   ├── requirements.txt         # 必須: Python依存関係
│   ├── main.py                  # Functionロジックを記述 (例)
│   └── proxies.json             # (任意) プロキシ設定ファイル
│
├── tests/                       # テストコードディレクトリ
│   └── test_my_function.py      # pytestなどを使ったテストコード
│
├── .gitignore                   # Git管理しないファイルを指定
├── README.md                    # リポジトリの説明
└── requirements.txt             # Python依存関係 (root level, optional)
</repository-root>
</pre>
