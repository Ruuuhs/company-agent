# company-agent

Claude Code を活用した仮想チーム（10部門・24エージェント）の統合システムです。代表（ユーザー）が指示を出すと、チーフ（司令塔）が自動的に担当エージェントを起動し、結果を統合して報告します。

---

## ディレクトリ構造

```
company-agent/
├── CLAUDE.md                    # 司令塔・ルーティング規則（エントリーポイント）
├── agents/                      # エージェント定義（部門別・24名）
│   ├── 01-経営企画部/
│   ├── 02-事業開発部/
│   ├── 03-コンテンツ制作部/
│   ├── 04-マーケティング部/
│   ├── 05-人事部/
│   ├── 06-経営管理部/
│   ├── 07-リサーチ部/
│   ├── 08-データ分析部/
│   ├── 09-営業部/
│   └── 10-M&A評価部/
├── guidelines/                  # 社内マニュアル・ガイドライン（全エージェント共通）
├── templates/                   # アウトプットテンプレート（部門別）
├── outputs/                     # 生成されたドキュメント群 ★コアフロー
│   ├── meeting-logs/            # 議事録（保存期間: 3年）
│   ├── documents/
│   │   ├── contracts/           # 契約書・NDA（保存期間: 5年）
│   │   └── proposals/           # 提案書・見積書（保存期間: 5年）
│   ├── finance/
│   │   ├── reports/             # 財務・KPIレポート（保存期間: 7年）
│   │   └── budgets/             # 予算管理（保存期間: 7年）
│   ├── reports/
│   │   ├── strategy/            # 戦略・競合レポート（保存期間: 1年）
│   │   ├── operations/          # 月次振り返り・事業レポート（保存期間: 1年）
│   │   ├── marketing/           # マーケティング・コンテンツ企画（保存期間: 1年）
│   │   └── research/            # 市場調査・トレンドレポート（保存期間: 1年）
│   ├── content/
│   │   ├── scripts/             # YouTube台本・教材（保存期間: 1年）
│   │   └── visuals/             # サムネイル・編集指示書（保存期間: 1年）
│   └── tmp/                     # 一時作業ファイル（30日で削除）
└── docs/                        # 設計ドキュメント
    └── virtual-team-guide.md
```

---

## 使い方

1. **指示を出す** — チャットで自然言語で指示するだけ
2. **チーフが自動ルーティング** — CLAUDE.md のルーティングテーブルに従い担当部門を起動
3. **並列処理** — 複数部門にまたがるタスクは同時並列で処理
4. **統合レポート** — チーフが各エージェントの結果を1つのレポートに統合して報告
5. **outputs/に保存** — 生成されたドキュメントは outputs/ に自動保存

---

## 部門一覧

| 部門 | スラッシュコマンド | 担当領域 |
|------|-----------------|---------|
| 経営企画部 | `/strategy` | 戦略・ロードマップ・競合分析 |
| 事業開発部 | `/business-dev` | 新規事業・収益モデル・価格設計 |
| コンテンツ制作部 | `/content` | YouTube・動画・台本・教材 |
| マーケティング部 | `/marketing` | SNS・PR・LP・コピー・メルマガ |
| 人事部 | `/hr` | 採用・組織・オンボーディング |
| 経営管理部 | `/management` | 経費・予算・契約・法務 |
| リサーチ部 | `/research` | 市場調査・競合・トレンド・助成金 |
| データ分析部 | `/data` | KPI・分析・ABテスト・可視化 |
| 営業部 | `/sales` | 提案書・見積・商談・契約書 |
| M&A評価部 | `/ma` | M&A・バリュエーション・PMI |

---

## outputs/フォルダについて

すべてのエージェントが生成したドキュメントは `outputs/` フォルダに一元管理されます。

### 命名規則

```
YYYY-MM-DD_[種別]_[内容].md
例: 2026-04-14_戦略レポート_AI案件参入戦略.md
    2026-04-14_競合分析_AI受託開発市場.md
    2026-04-08_議事録_Q2戦略会議.md
```

### 部門別の保存先早見表

詳細は [`guidelines/output-standards.md`](guidelines/output-standards.md) を参照。

| 担当部門 | 保存先 |
|---------|--------|
| 議事録 | `outputs/meeting-logs/` |
| 戦略・競合・事業企画 | `outputs/reports/strategy/` |
| マーケティング・PR | `outputs/reports/marketing/` |
| 市場調査・リサーチ | `outputs/reports/research/` |
| 財務・KPI | `outputs/finance/reports/` |
| 契約書・NDA | `outputs/documents/contracts/` |
| 提案書・見積書 | `outputs/documents/proposals/` |
| YouTube台本・教材 | `outputs/content/scripts/` |
| 一時作業ファイル | `outputs/tmp/`（30日で削除） |

---

## 主要なガイドライン

| ファイル | 目的 |
|---------|------|
| [`guidelines/output-standards.md`](guidelines/output-standards.md) | アウトプットの品質基準・ファイル命名規則・outputs/構造 |
| [`guidelines/security-policy.md`](guidelines/security-policy.md) | データ保管ルール・保存期間・セキュリティ基準 |
| [`guidelines/collaboration-protocol.md`](guidelines/collaboration-protocol.md) | エージェント間の連携ルール・引き継ぎフォーマット |
| [`guidelines/escalation-rules.md`](guidelines/escalation-rules.md) | 代表確認が必要なケースの判定基準 |
| [`guidelines/tools-manual.md`](guidelines/tools-manual.md) | ツール使用・ファイル操作のルール |

---

## システム詳細設計

[`docs/virtual-team-guide.md`](docs/virtual-team-guide.md) を参照してください。
