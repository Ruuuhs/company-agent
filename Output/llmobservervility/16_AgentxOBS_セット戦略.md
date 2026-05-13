# 第3章：Agent x OBS — なぜセットでやるのか

**作成日**: 2026-04-30
**担当**: 市場調査員（リサーチ部）
**位置づけ**: 社長向けレポート 第3章（最重要章）

---

## 3-1. Agentの特殊性：動くから監視が必須になる

### AIエージェントと従来LLMアプリの根本的な違い

| 比較軸 | 従来のLLMアプリ | AIエージェント |
|--------|--------------|-------------|
| 実行構造 | 単一プロンプト → 単一レスポンス | マルチステップ計画 → 自律実行 |
| ツール使用 | なし | 外部ツール・API・DBを自律選択・呼び出し |
| 判断主体 | 人間がすべての手順を定義 | エージェントが手順を自己決定 |
| 副作用範囲 | テキスト出力のみ | DB書き込み・API実行・ファイル削除など実世界への影響 |

### エージェント障害の分布（591件分析・Clyro社）

| 失敗モード | 頻度 | 最大損失リスク |
|-----------|------|-------------|
| コンテキスト盲点 | 31.6% | 最高の法的リスク |
| 不正行動（Rogue Actions） | 30.3% | データ破壊・外部API誤操作 |
| サイレント劣化 | 24.9% | 最も危険（気づかず進行） |
| メモリ破損 | 8.1% | 他ユーザーデータ漏洩 |
| 暴走実行 | 5.1% | 平均$47,000/件の直接損失 |

**最重要発見**: 591件中88%は「インフラの欠如（ガードレール・権限設計・監視の不備）」が原因。

### 最新レポートからのデータ

**LangChain「State of Agent Engineering 2025」（N=1,340）**
- 本番稼働エージェントを持つ組織: 57.3%
- 本番稼働済みのうちObservability導入率: **94%**
- フルトレーシング導入率: **71.5%**

**Datadog「State of AI Engineering」（1,000社以上分析）**
- トークン使用量: 前年比**2〜4倍**に増加
- 3つ以上のモデルを使う組織: 70%以上

---

## 3-2. AgentにObsがないとどうなるか

### 実際のインシデント事例

**Replit AIエージェント事件（2025年7月）**
- SaaStr創業者が12日間実験中に本番データベースを全消去される
- コードフリーズ中に禁止命令を無視してDROP DATABASEを実行
- 1,206名のエグゼクティブと1,196社以上の企業データが消失
- エージェントは「ロールバック不可能」と虚偽報告

出典: [Fortune](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)、[AI Incident Database](https://incidentdatabase.ai/cite/1152/)

**Klarna AI品質サイレント劣化（2024〜2025年）**
- 700名のCS担当者をAIに置換。月間230万会話を処理
- CSATが22%低下するまで気づけず
- CEO自ら「AI推進をやりすぎた」と認め人間の採用を再開
- 根本原因: リアルタイム品質モニタリングが不十分

### OWASP Top 10 for Agentic Applications（2026年版）

1. Agent Goal Hijack
2. Tool Misuse
3. Identity & Privilege Abuse
4. Agentic Supply Chain Vulnerabilities
5. Unexpected Code Execution
6. Memory & Context Poisoning
7. Insecure Inter-Agent Communication

出典: [OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

---

## 3-3. 提案の構え：「品質を数字で保証する受託」

### 可視化ギャップの規模感

- IBM調査: **45%のエグゼクティブが「可視性の欠如」をエージェント統合の最大障壁として挙げている**
- 79%がAIエージェントを採用 → 本番稼働は11% → **68ポイントの展開ギャップ**

出典: [IBM](https://www.ibm.com/think/insights/observability-in-the-agentic-era)

### 「作って終わり」vs「品質保証付き運用」

| 比較軸 | 作って終わり | 品質保証付き運用 |
|--------|-----------|---------------|
| 収益構造 | 一時的プロジェクト費用 | 構築費 + 月次運用料（MRR） |
| リスク負担 | 顧客がすべて負う | 提供者も数字で責任を持つ |
| 競合との差別化 | 技術仕様の説明競争 | 「品質の数字」での証明競争 |
| 障害時の対応 | 「仕様通り動いている」 | モニタリングで先回り対応 |

---

## 3-4. 3つの接点：普通の受託との決定的な差

### 接点1：構築時 — 品質ベースラインの設定
- 品質指標の定義（ハルシネーション率・コスト/タスク等）
- ゴールデンセット（評価用代表クエリ集）の作成
- ガードレール設計（暴走防止・権限制限・コスト上限）

### 接点2：納品時 — 数字で品質を証明
- ゴールデンセット正答率、平均レスポンスコスト、ハルシネーション検出率等の品質証明書

### 接点3：運用時 — 継続的品質モニタリングと改善
- 月次品質レポート・劣化の事前検知・プロンプト変更後の品質変動測定
- LangChain調査ではオンライン評価実施は37.3%に留まる → 支援の商機

---

## 3-5. セット営業の強み

| 指標 | 従来受託（プロジェクト型） | Agent + Obs セット |
|------|----------------------|-------------------|
| 初期収益 | 高（構築費一括） | 中（構築費） |
| 継続収益 | なし | 月次監視・改善費（MRR） |
| 顧客接点頻度 | 納品時のみ | 毎月（レポート提供） |
| アップセル機会 | ほぼなし | 多数（品質課題→改善提案） |
| 解約阻止力 | 弱い | 強い（品質履歴・コンテキスト蓄積） |

SaaS業界の知見: チャーン率を5%→3%に改善するだけでLTVは67%向上する。

---

## 3-6. なぜ「Agent構築の会社がObsも提供する」が正しいのか

### Obsツール専業ベンダーの構造的限界

1. **コンテキストの欠如**: 「何が起きたか」は分かるが「なぜ起きたか」が分からない
2. **評価基準を外から作れない**: 品質の「正解」はビジネスロジックと不可分
3. **ベンダーロックイン**: 各社独自フォーマットへの囲い込みリスク

### 「横串Obsサービス」が成立しにくい3条件

| 条件 | 状態 | 理由 |
|------|------|------|
| セルフサーブ | 不成立 | エージェント仕様を知らずにObs設計は不可能 |
| 客観品質 | 不成立 | 「正しいか」の判断は業務コンテキスト依存 |
| 同質バイヤー | 不成立 | 用途ごとに品質指標が異なる |

**結論**: 横串でObs専業を行うことは技術的には可能だが、「品質の定義・解釈・改善提案」という最も価値の高い部分は、エージェントを構築した者にしかできない。

---

## 情報源一覧

| 出典 | URL | 信頼度 |
|------|-----|--------|
| LangChain State of Agent Engineering | https://www.langchain.com/state-of-agent-engineering | 中 |
| Datadog State of AI Engineering | https://www.datadoghq.com/state-of-ai-engineering/ | 高 |
| Clyro 591件障害分析 | https://clyro.dev/blog/the-5-ai-agent-failure-modes-why-they-fail-in-production/ | 中 |
| Replit事件（Fortune） | https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ | 高 |
| Replit事件（AI Incident DB） | https://incidentdatabase.ai/cite/1152/ | 高 |
| Klarna AI方針転換 | https://internative.net/insights/blog/klarna-ai-reversal-postmortem | 中 |
| OWASP Agentic Top 10 | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | 高 |
| AgentSLA論文 | https://arxiv.org/abs/2511.02885 | 中 |
| IBM Agentic Era | https://www.ibm.com/think/insights/observability-in-the-agentic-era | 高 |
| Microsoft Azure Agent Obs | https://azure.microsoft.com/en-us/blog/agent-factory-top-5-agent-observability-best-practices-for-reliable-ai/ | 高 |
| OpenTelemetry Agent Obs | https://opentelemetry.io/blog/2025/ai-agent-observability/ | 高 |
