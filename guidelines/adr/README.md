# guidelines/adr/ — Architecture Decision Records

このフォルダは**重要な意思決定の「なぜ」を追跡する**ためのADR（Architecture Decision Records）を管理します。

---

## ADRとは

ADR（Architecture Decision Records）は、もともとソフトウェアアーキテクチャの意思決定を記録する手法です。このリポジトリでは、以下のような経営・組織・システム設計の意思決定にも適用します：

- システム設計・フォルダ構造の変更
- 事業戦略・方針の決定
- ガイドライン・プロセスの変更
- ツール・技術スタックの採用・変更

---

## ファイル命名規則

```
ADR-NNNN_[kebab-case-title].md
例: ADR-0001_outputs-folder-structure.md
    ADR-0002_document-management-3layer-model.md
```

NNNNは4桁の連番（0001, 0002, ...）。

---

## ADR一覧

| 番号 | タイトル | ステータス | 作成日 |
|------|---------|---------|--------|
| [ADR-0000](ADR-0000_template.md) | テンプレート | - | 2026-04-14 |
| [ADR-0001](ADR-0001_outputs-folder-structure.md) | outputs/フォルダ構造の設計 | 承認済み | 2026-04-14 |
| [ADR-0002](ADR-0002_document-management-3layer-model.md) | ドキュメント管理3層モデルの採用 | 承認済み | 2026-04-14 |

---

## ステータスの定義

| ステータス | 意味 |
|---------|------|
| 提案中 | 検討中・まだ承認されていない |
| 承認済み | 採用・現在有効 |
| 却下 | 検討したが採用しなかった |
| 非推奨 | かつては有効だったが現在は推奨しない |
| 置換 | 別のADRに置き換えられた |

---

## 新しいADRを作成するとき

1. `ADR-0000_template.md` をコピー
2. 連番を割り振る（現在の最大番号 + 1）
3. 上の「ADR一覧」テーブルに追記
4. `context/decisions-log.md` にも1行追記

---

## いつADRを書くか

- 「なぜこうしたのか」が1ヶ月後にわからなくなりそうな決定
- 複数の選択肢を比較検討した決定
- 影響範囲が2ファイル以上に及ぶ変更
- 事業・戦略の方針転換
