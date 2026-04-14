# context/ — AIセッション間の記憶を繋ぐフォルダ

このフォルダはAIが**セッションをまたいで記憶を継続する**ための「生きたファイル群」です。

---

## ファイル一覧と役割

| ファイル | 更新頻度 | 役割 |
|---------|---------|------|
| `company-state.md` | 変化があるたびに（最低週1回） | 会社の現在状態・KPI・保留中の意思決定 |
| `activeContext.md` | 毎セッション開始時 | 今日のフォーカス・優先タスク・ブロッカー |
| `decisions-log.md` | 意思決定のたびに | 意思決定の「なぜ」を追跡するログ（追記のみ） |
| `ongoing-projects.md` | 週次 | 進行中プロジェクトの状態・マイルストーン |
| `session-log.md` | セッション終了時 | 3行サマリー（追記のみ） |

---

## このフォルダの位置づけ（3層ドキュメントモデル）

```
【永続】 context/ + guidelines/
          ↑ 常に最新状態を維持する「生きたファイル」
          
【中期】 outputs/（1〜7年保存）
          ↑ 完成したレポート・契約書・議事録
          
【短期】 outputs/tmp/（30日で削除）
          ↑ 一時作業ファイル
```

---

## ルール

- **削除禁止**: decisions-log.md と session-log.md は追記のみ。削除・編集は不可
- **最新性維持**: company-state.md は古い情報が残らないよう週次でレビュー
- **Gitコミット必須**: セッション終了後は context/ の変更を必ずコミットすること

---

## AIへの指示（CLAUDE.mdより）

セッション開始時: `company-state.md` → `activeContext.md` → `session-log.md`（直近3件）を読む
セッション終了時: `decisions-log.md` → `session-log.md` → `ongoing-projects.md` を更新してコミット
