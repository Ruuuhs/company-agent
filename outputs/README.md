# outputs/

このフォルダはすべてのエージェントが生成したドキュメントを一元管理する場所です。

---

## フォルダ構造と保存期間

| フォルダ | 用途 | 保存期間 |
|---------|------|---------|
| `meeting-logs/` | 議事録 | 3年 |
| `documents/contracts/` | 契約書・NDA | 5年 |
| `documents/proposals/` | 提案書・見積書 | 5年 |
| `finance/reports/` | 財務レポート・KPIレポート | 7年 |
| `finance/budgets/` | 予算管理ファイル | 7年 |
| `reports/strategy/` | 戦略・競合レポート・事業企画書 | 1年 |
| `reports/operations/` | 月次振り返り・事業レポート | 1年 |
| `reports/marketing/` | マーケティング・コンテンツ企画 | 1年 |
| `reports/research/` | 市場調査・トレンドレポート | 1年 |
| `content/scripts/` | YouTube台本・教材 | 1年 |
| `content/visuals/` | サムネイル指示書・編集指示書 | 1年 |
| `tmp/` | 一時作業ファイル | **30日で削除** |

---

## 命名規則

```
YYYY-MM-DD_[種別]_[内容].md
```

例:
- `2026-04-14_戦略レポート_AI案件参入戦略.md`
- `2026-04-14_競合分析_AI受託開発市場.md`
- `2026-04-08_議事録_Q2戦略会議.md`
- `2026-04-10_契約書_業務委託_A社.md`

---

## ルール

- 保存期間を超えたファイルは定期的にアーカイブまたは削除する
- `tmp/` のファイルは30日経過後に削除する（作業が完了次第、適切なフォルダに移動すること）
- 命名規則に従わないファイルは受け付けない
- 詳細は [`guidelines/security-policy.md`](../guidelines/security-policy.md) および [`guidelines/output-standards.md`](../guidelines/output-standards.md) を参照
