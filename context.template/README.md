# context.template/ — 個人コンテキストのひな形

このフォルダは `context/` フォルダの**初期テンプレート**です。

---

## セットアップ手順

リポジトリをcloneしたら、以下を実行してください：

```bash
./setup.sh
```

これで `context.template/` をもとに `context/` が自動生成されます。

---

## context/ とは

`context/` フォルダはAIが**セッションをまたいで記憶を継続する**ための「あなた専用のファイル群」です。

| ファイル | 役割 |
|---------|------|
| `company-state.md` | 会社の現在状態・KPI・保留中の意思決定 |
| `activeContext.md` | 今日のフォーカス・優先タスク・ブロッカー |
| `decisions-log.md` | 意思決定の「なぜ」を追跡するログ（追記のみ） |
| `ongoing-projects.md` | 進行中プロジェクトの状態・マイルストーン |
| `session-log.md` | 3行サマリー（追記のみ） |

---

## 重要なルール

- `context/` はgit管理対象外（`.gitignore`）です。**リモートにpushされません**
- `context/` の内容はあなたのローカルにのみ存在します
- セッション終了時に `context/` を更新すること（AIが次回引き継げる）
- バックアップはご自身でクラウドストレージ等に保管してください

---

## テンプレートの更新について

`context.template/` がリポジトリ側で更新された場合、`context/` との差分を手動でマージしてください：

```bash
# テンプレートの差分を確認
diff -r context.template/ context/
```
