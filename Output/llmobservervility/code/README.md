# LLM Observability デモ — Langfuse + Claude

Langfuse v3（セルフホスト版）と、Anthropic Claude APIをトレーシングするCLIチャットアプリのデモ環境です。

## 構成

```
code/
├── docker-compose.yml      # Langfuse v3 インフラ一式
├── .env.example            # Docker Compose用 環境変数テンプレート
├── app/
│   ├── main.py             # CLIチャットアプリ（Langfuseトレーシング付き）
│   ├── requirements.txt    # Python依存パッケージ
│   └── .env.example        # アプリ用 環境変数テンプレート
└── README.md               # このファイル
```

### Langfuse v3 アーキテクチャ

| コンテナ | 役割 | ポート |
|---------|------|-------|
| langfuse-web | UI + API サーバー | 3000 |
| langfuse-worker | バックグラウンドジョブ処理 | 3030 (内部) |
| postgres | メタデータ・ユーザー管理 | 5432 (内部) |
| clickhouse | トレース・スコアの高速分析 | 8123, 9000 (内部) |
| redis | キュー・キャッシュ | 6379 (内部) |
| minio | S3互換オブジェクトストレージ | 9090 |

## 前提条件

- Docker / Docker Compose
- Python 3.10+
- Anthropic APIキー

## セットアップ手順

### 1. 初回セットアップ（ワンコマンド）

```bash
cd code/
make setup
```

これだけで以下が自動実行されます:

- `.env` ファイル生成（シークレットは自動生成）
- Python仮想環境の作成・依存パッケージインストール
- Langfuse全コンテナの起動

### 2. Langfuse でAPIキーを取得

1. http://localhost:3000 でアカウントを作成
2. プロジェクトを作成
3. Settings > API Keys から Public Key と Secret Key を取得

### 3. アプリの環境変数を設定

`app/.env` を編集して以下を記入:

```
ANTHROPIC_API_KEY=sk-ant-xxxxx       ← Anthropicコンソールから取得
LANGFUSE_PUBLIC_KEY=pk-lf-xxxxx      ← Langfuse UIから取得
LANGFUSE_SECRET_KEY=sk-lf-xxxxx      ← Langfuse UIから取得
```

### 4. チャット開始

```bash
make chat
```

チャットを開始すると、各メッセージのやり取りがLangfuseにトレースとして記録されます。
Langfuse UI (http://localhost:3000) の「Traces」タブで確認できます。

## Makeコマンド一覧

| コマンド | 用途 |
|---------|------|
| `make setup` | 初回セットアップ（env生成→venv→Langfuse起動） |
| `make up` | Langfuseを起動 |
| `make down` | Langfuseを停止 |
| `make restart` | Langfuseを再起動 |
| `make chat` | CLIチャットアプリを起動 |
| `make status` | コンテナの状態確認 |
| `make logs` | Langfuseのログ表示 |
| `make pip-install` | Pythonパッケージを再インストール |
| `make clean` | 仮想環境を削除 |
| `make reset` | 全データ削除して初期状態に戻す（確認あり） |

## 動作確認のポイント

- Langfuse UIの Traces 画面で `chat-pipeline` トレースが表示される
- 各トレース内に `claude-chat` (generation) が子スパンとして表示される
- 入力・出力・レイテンシが記録されている

## トラブルシューティング

### Langfuseが起動しない

```bash
# ログを確認
docker compose logs langfuse-web
docker compose logs langfuse-worker

# 全コンテナを再起動
docker compose down && docker compose up -d
```

### Langfuse認証エラー

- `.env` の `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` が正しいか確認
- `LANGFUSE_HOST` が `http://localhost:3000` になっているか確認

### データの永続化

Docker Composeの named volumes により、`docker compose down` してもデータは保持されます。
完全にリセットする場合:

```bash
docker compose down -v  # ボリュームも含めて削除
```

## 参考リンク

- [Langfuse 公式ドキュメント](https://langfuse.com/docs)
- [Langfuse セルフホスティング (Docker Compose)](https://langfuse.com/self-hosting/deployment/docker-compose)
- [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/decorators)
- [Langfuse + Anthropic 連携](https://langfuse.com/integrations/model-providers/anthropic)
- [Anthropic Claude API](https://docs.anthropic.com/)
