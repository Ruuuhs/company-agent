# /content — コンテンツ制作部ルーター

## このコマンドの役割

コンテンツ制作部への指示をルーティングする。

**キーワード**: YouTube、動画、台本、コンテンツ、企画、サムネイル、教材、カリキュラム、編集、ネタ

## エージェント一覧

| エージェント | ファイル | 専門 |
|------------|--------|------|
| Eito | `agents/03-コンテンツ制作部/eito.md` | YouTube企画・ネタ出し |
| Shiori | `agents/03-コンテンツ制作部/shiori.md` | 台本・スクリプト |
| Hikaru | `agents/03-コンテンツ制作部/hikaru.md` | サムネイル指示書 |
| Itsuki | `agents/03-コンテンツ制作部/itsuki.md` | 教材・カリキュラム |
| Hayato | `agents/03-コンテンツ制作部/hayato.md` | 動画編集指示書 |

## ルーティングロジック

```
「YouTube企画・ネタ」系 → Eito
「台本・スクリプト」系 → Shiori（Eitoの企画書を受け取り）
「サムネイル」系 → Hikaru
「教材・カリキュラム」系 → Itsuki
「編集指示」系 → Hayato（Shioriの台本を受け取り）
「動画を1本完成させたい」→ Eito→Shiori→Hikaru→Hayato（順次）
```

## 典型的な指示例と対応

| 指示 | 起動エージェント |
|------|---------------|
| 「YouTube のネタを出して」 | Eito |
| 「この企画の台本を作って」 | Shiori |
| 「サムネイルの指示書を作って」 | Hikaru |
| 「新しい教材のカリキュラムを設計して」 | Itsuki |
| 「編集指示書を作って」 | Hayato |
| 「来週のYouTube、全部準備して」 | Eito + Shiori + Hikaru + Hayato（順次） |
