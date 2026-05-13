# AI動画生成プロンプト集：タロット占い師シーズー犬キャラ（ショート動画用）

**作成日**: 2026-05-13
**担当**: ビジュアルデザイナー（コンテンツ制作部）
**参照レポート**: research/fortune-ai-character-sns/10_final_report.md
**用途**: TikTok / YouTube Shorts 縦型動画（9:16）、30〜60秒
**技術スタック**: Veo3（メイン）/ Midjourney v7（キャラ画像）/ ElevenLabs v3（音声）
**ステータス**: 初版。PoC実施後に数値・パラメータを要更新

---

## 重要前提事項

- 本プロンプト集はキャラクターIP「ほしよみ（Hoshiyomi）」のTarot担当キャラ（仮称: Luna）の第1弾動画制作用である
- Veo3の1クリップ最大尺は **8秒** が現時点の仕様上限（仮説・要検証。2026年5月時点のGoogle AI Pro情報に基づく）
- 30〜60秒の完成動画はVeo3クリップ（各5〜8秒）を4〜8本つなぎ合わせてCapCut等で編集する構成を前提とする
- AI生成コンテンツのラベル表示は全SNSで義務化済み。本プロンプト集のすべての成果物に表示義務が発生する（詳細はセクション7参照）
- 占い結果を「断定的判断」として表現することは消費者契約法改正（2023年）により取消可能。プロンプト内および動画内テキストで「絶対」「必ず」等の断定表現は使用禁止

---

## セクション1：キャラクター設計プロンプト（基準画像生成用）

### 1-1. キャラクター共通設定（全プロンプトに埋め込む核心情報）

```
キャラクター核心仕様:
- 種族: 擬人化シーズー犬（Shih Tzu dog, anthropomorphized）
- 毛色: 茶色と白のツートーン（brown and white two-tone long fur）
- 体型: 小柄・丸みのあるかわいい体型（small, round, chibi-proportioned）
- 顔: 大きな黒いつぶらな瞳（large round black eyes）、丸顔、わずかに微笑む口元
- 衣装: 紫色の星柄マント（purple starry cloak with gold star patterns）
- 帽子: 紫のベレー帽にピンクのリボン（purple beret with pink ribbon）
- 首元: 小さな紫の宝石装飾（small purple gemstone necklace）
- 持ち物: タロットカード3枚（裏面は紫と金の幾何学模様）
- アートスタイル: 日本アニメ・かわいい系、watercolor風タッチ、彩色ソフトな仕上がり
- カラーパレット: 紫（#7C3AED）、金（#F59E0B）、白（#FFFFFF）、茶色（#92400E）
```

### 1-2. Midjourney v7 正面構図プロンプト

**英語（実際に使用するプロンプト）**

```
Cute anthropomorphized Shih Tzu dog fortune teller, chibi anime style, standing front view, 
large round black sparkling eyes, soft smile, brown and white long fluffy fur, 
wearing purple starry cloak with scattered gold star embroidery, 
purple beret hat with pink ribbon, small purple amethyst gemstone necklace, 
holding three tarot cards with purple and gold geometric pattern back design, 
watercolor illustration style, soft pastel lighting, magical fantasy atmosphere, 
purple and gold color palette, white background for reference sheet, 
full body character design, --ar 2:3 --stylize 750 --v 7
```

**日本語訳**

かわいい擬人化シーズー犬の占い師キャラ、ちびアニメスタイル、正面立ちポーズ、大きな丸い黒いキラキラした瞳、やさしい微笑み、茶色と白の長いふわふわの毛、金の星模様の刺繍が散りばめられた紫色の星柄マント、ピンクのリボンが付いた紫のベレー帽、小さな紫のアメジスト宝石ネックレス、紫と金の幾何学模様の裏面デザインのタロットカード3枚を持っている、水彩イラストスタイル、やわらかいパステルライティング、魔法のファンタジー雰囲気、紫と金のカラーパレット、参照用ホワイト背景、全身キャラクターデザイン

**推奨パラメータ**

| パラメータ | 値 | 理由 |
|-----------|-----|------|
| `--ar` | `2:3` | キャラクター参照シート用の縦長比率 |
| `--stylize` | `750` | アニメ・かわいい寄りのスタイル強調（150〜1000の中間上寄り） |
| `--v` | `7` | cref機能対応バージョン（v7以降） |
| `--seed` | 初回生成後に固定 | 2本目以降のキャラ一貫性維持に必須 |

### 1-3. Midjourney v7 横向き・斜め向きプロンプト

**横向き（Left Side View）英語**

```
Cute anthropomorphized Shih Tzu dog fortune teller, chibi anime style, 
left side profile view, same character as reference (cref), 
brown and white long fluffy fur, purple starry cloak with gold stars, 
purple beret with pink ribbon, holding tarot cards in both hands slightly raised, 
gentle closed-eye smile as if focusing, watercolor illustration style, 
soft purple ambient glow, magical sparkles around character, 
--ar 2:3 --stylize 750 --v 7 --cref [基準画像URL]
```

**斜め正面（3/4 View）英語**

```
Cute anthropomorphized Shih Tzu dog fortune teller, chibi anime style, 
3/4 angle front-left view, same character as reference (cref), 
slightly tilting head to the right with curious expression, 
one ear perked up, brown and white long fluffy fur flowing, 
purple starry cloak slightly open showing inner lining, 
holding one tarot card face-down toward viewer, 
watercolor illustration, magical bokeh background, soft candlelight glow, 
--ar 2:3 --stylize 750 --v 7 --cref [基準画像URL]
```

### 1-4. キャラクター一貫性維持の設定方法

```
cref（Character Reference）使用手順:
1. 正面構図で最も満足のいく1枚を「基準画像（master reference）」として確定
2. Midjourney v7でその画像URLを取得
3. 以降すべてのプロンプトに --cref [URL] --cw 100 を追加
   （--cw 100 でキャラクターの外見要素を最大限維持）
4. seedも --seed [番号] で固定すること（初回生成Jobの右クリック → Copy job ID）

Stable Diffusion XL / Forge 使用時の一貫性:
- ControlNet IPAdapter（ip_adapter_plus_face_sd15等）でキャラ顔を固定
- 基準画像をreference imageとして設定
- DWPose controlnetで体型・ポーズのブレを抑制（仮説・要検証）
```

### 1-5. ネガティブプロンプト（避けるべき要素）

**Midjourney / Stable Diffusion 共通**

```
[英語]
realistic photography, 3D render, ugly, deformed, extra fingers, 
malformed hands, blurry, low quality, nsfw, adult content, 
scary expression, sharp angular features, western cartoon style, 
human face without fur, no costume, plain clothing, 
different colored eyes, asymmetrical ears, inconsistent fur pattern, 
text artifacts, watermarks

[日本語訳]
リアルな写真、3Dレンダリング、醜い、変形、余分な指、
形の悪い手、ぼやけ、低品質、成人向けコンテンツ、
怖い表情、鋭い角張った特徴、西洋漫画スタイル、
毛のない人間顔、衣装なし、シンプルな服装、
色の違う瞳、非対称な耳、統一性のない毛模様、
テキストアーティファクト、透かし
```

---

## セクション2：シーン別動画生成プロンプト（Veo3優先）

### Veo3利用時の共通注意事項

- 1クリップ最大8秒（2026年5月時点。要定期確認）
- Google AI Pro（月額約2,900円）で利用可能
- 参照画像（Reference Image）をアップロードしてキャラ一貫性を確保する
- プロンプトは英語が推奨（日本語は精度が下がる場合あり。要検証）
- Motion Intensity設定: Low〜Medium推奨（Highはキャラ崩れリスクあり）

### シーン1：オープニングフック（0〜5秒）

**用途**: 冒頭のつかみ。視聴者の手を止める

**Veo3プロンプト（英語）**

```
A cute chibi anime-style anthropomorphized Shih Tzu dog in a purple starry cloak and purple beret 
with pink ribbon sits at a round table covered with dark purple velvet cloth. 
The character has large round black eyes and brown-and-white fluffy fur. 
She slowly fans three tarot cards face-down on the table with her small paws, 
looking directly at the camera with a soft mysterious smile. 
Golden sparkles drift from the cards. Candlelight from the left side creates warm amber shadows. 
Background is a cozy dark room with bookshelves and floating orbs of purple light. 
Camera: slow zoom in from medium shot to close-up of face.
Style: soft watercolor animation, pastel tones, magical atmosphere. 
Duration: 5 seconds. Motion intensity: Low.
```

**日本語訳**

紫色の星柄マントと、ピンクのリボンが付いた紫のベレー帽をかぶった、かわいいちびアニメスタイルの擬人化シーズー犬が、濃い紫色のベルベットの布がかかった丸テーブルに座っている。このキャラクターは大きな丸い黒い目と茶色と白のふわふわの毛を持つ。彼女は小さな前足で3枚のタロットカードを伏せた状態でテーブルにゆっくりとファンに広げ、やわらかな神秘的な微笑みでカメラを直視している。金色のきらめきがカードから漂う。左側からのろうそくの光が暖かいアンバーの影を作る。背景は本棚と紫色の光の浮かぶ球体が漂う居心地のよい暗い部屋。カメラ: ミディアムショットからアップへのゆっくりとしたズームイン。スタイル: やわらかい水彩アニメーション、パステルトーン、魔法の雰囲気。尺: 5秒。モーション強度: 低。

**推奨ツール**: Veo3（最優先）、次点Kling v1.6（参照画像機能対応）
**カメラワーク**: Slow zoom in（medium → close-up）
**BGM**: このシーンは無音 or 鈴の音1回のみが効果的

---

### シーン2：カードめくり演出（5〜12秒）

**用途**: 「今日の運勢を引くよ」の見せ場

**Veo3プロンプト（英語）**

```
Close-up shot of the Shih Tzu fortune teller character's paws. 
She slowly picks up one tarot card from the table with both paws and 
gradually turns it face-up to reveal a glowing golden sun symbol on a purple background. 
Her large black eyes widen with a gentle excited expression as she tilts her head slightly to the right. 
One fluffy ear perks up. Golden light rays burst from the revealed card, 
illuminating her face and purple cloak with warm light. 
Tiny stars and sparkles scatter in the air around the card. 
Camera: stays on tight close-up of hands and card, then slowly pulls back to include face.
Style: watercolor anime, magical glow effect, warm amber and purple palette.
Duration: 6 seconds. Motion intensity: Low-Medium.
```

**日本語訳**

シーズー占い師キャラの前足のクローズアップショット。彼女は両前足でテーブルから1枚のタロットカードをゆっくりと手に取り、紫色の背景に輝く金色の太陽シンボルが描かれた表面を徐々に見せる。大きな黒い瞳が広がり、頭をわずかに右に傾けてやさしく興奮した表情を見せる。ふわふわした耳が1枚立ち上がる。明かされたカードから金色の光が放射状に広がり、顔と紫のマントを暖かい光で照らす。小さな星ときらめきがカードの周りの空中に散らばる。カメラ: 手とカードのタイトなクローズアップを維持し、その後ゆっくりと後退して顔も含める。スタイル: 水彩アニメ、魔法の輝きエフェクト、暖かいアンバーと紫のパレット。尺: 6秒。モーション強度: 低〜中。

**推奨ツール**: Veo3（手の動きの繊細さが必要）
**カメラワーク**: Close-up → 緩やかなpull back

---

### シーン3：メッセージデリバリー（13〜30秒）

**用途**: 占い結果・アドバイスをキャラが語るシーン（ElevenLabs音声に合わせて口の動きを合成）

**Veo3プロンプト（英語）**

```
Medium shot of the cute Shih Tzu fortune teller character facing slightly toward camera (3/4 angle). 
She holds a tarot card face-up in one paw raised slightly at chest height. 
Her mouth moves gently as if speaking, eyes bright and warm, 
occasionally blinking slowly (one slow blink cycle). 
Free paw gestures softly in an explanatory motion. 
Tail wags slowly behind her. 
Background: cozy mystical room with soft bokeh purple candlelight and floating golden dust particles. 
Soft rim light on her cloak edges creates a magical silhouette effect. 
Camera: static medium shot with very subtle push-in (barely perceptible).
Style: watercolor anime, soft depth of field, warm candlelight plus cool purple ambient.
Duration: 8 seconds. Motion intensity: Low. (Loop this clip 2-3 times with variation)
```

**日本語訳**

かわいいシーズー占い師キャラクターのミディアムショット、やや斜め（3/4アングル）でカメラに向いている。胸の高さでわずかに持ち上げた一方の前足にタロットカードの表面を持つ。まるで話しているかのように口がやさしく動き、瞳は明るく温かく、時々ゆっくりとまばたきをする（1回のスロービンクサイクル）。空いている前足が説明するような動作でやさしく動く。しっぽが後ろでゆっくり揺れる。背景: やわらかなボケた紫のろうそくの光と漂う金色のほこり粒子のある居心地のよい神秘的な部屋。マントの端のやわらかなリムライトが魔法のシルエット効果を作る。カメラ: ほとんど気づかないほどわずかなプッシュインのある静的なミディアムショット。スタイル: 水彩アニメ、やわらかい被写界深度、暖かいろうそくの光とクールな紫のアンビエント。尺: 8秒。モーション強度: 低。（バリエーションをつけてこのクリップを2〜3回ループさせる）

**推奨ツール**: Veo3（メイン）またはHedra（口の動き合成に特化。仮説・要検証）
**カメラワーク**: 静的ミディアムショット + 極微のpush-in

---

### シーン4：リアクション・感情表現（31〜45秒）

**用途**: キャラが「クゥン」と首を傾げたり、耳を動かすかわいい演技で感情移入を促す

**Veo3プロンプト（英語）**

```
Close-up of the Shih Tzu fortune teller character's face. 
She tilts her head to the left with a quizzical but adorable expression, 
one eyebrow-like tuft of fur raised. Both ears perk up and wiggle gently. 
Her large round black eyes shimmer with curiosity. 
She then slowly shakes her head left-right in a light "no-no" gesture, 
followed by a warm closed-eye smile and a gentle single nod. 
Small sparkle effects appear near her eyes when she smiles. 
Background blurred to shallow depth showing purple bokeh candlelight. 
Camera: tight close-up, static, centered on face.
Style: extremely cute, maximum moe expression, soft watercolor anime.
Duration: 6 seconds. Motion intensity: Low.
```

**日本語訳**

シーズー占い師キャラクターの顔のクローズアップ。不思議そうだがかわいらしい表情で頭を左に傾け、眉毛のような毛の房が1本上がっている。両耳が立ち上がってやさしく揺れる。大きな丸い黒い瞳が好奇心でキラキラと輝く。その後、軽い「ノーノー」のしぐさで頭をゆっくりと左右に振り、続いて暖かい閉じ目の笑顔とやさしい1回のうなずき。微笑むときに目の近くに小さなきらめきエフェクトが現れる。背景は紫のボケたろうそくの光を見せる浅い被写界深度でぼかされる。カメラ: 顔を中央にした静的なタイトクローズアップ。スタイル: 極めてかわいい、最大限のもえ表現、やわらかな水彩アニメ。尺: 6秒。モーション強度: 低。

**推奨ツール**: Veo3（最優先）、Kling v1.6（顔アニメが比較的安定。仮説）
**カメラワーク**: Tight close-up、static

---

### シーン5：エンディング・CTA（45〜60秒）

**用途**: フォロー・保存・LINE登録を促す締めシーン

**Veo3プロンプト（英語）**

```
Medium-wide shot of the Shih Tzu fortune teller character standing at her table. 
She gathers the three tarot cards neatly with both paws, taps them on the table edge to align them, 
then places them face-down in a neat pile. 
She looks up at the camera, waves one paw in a small friendly wave, 
and gives a bright wide-eyed smile with her tail wagging energetically. 
She then bows slightly in a polite Japanese-style bow (ojigin). 
A shower of golden stars and small sparkles falls from above around her. 
Purple magical runes briefly appear and fade in the background. 
Camera: starts medium-wide, slowly zooms in to medium as she bows.
Style: warm and inviting, bright lighting slightly stronger than other scenes, watercolor anime.
Duration: 7 seconds. Motion intensity: Low-Medium.
```

**日本語訳**

シーズー占い師キャラクターがテーブルに立っているミディアムワイドショット。両前足でタロットカード3枚をきれいに集め、テーブルの端で揃えるようにトントンとたたき、その後ふせた状態できれいな山に重ねる。カメラを見上げ、一方の前足で小さく友好的に手を振り、しっぽを元気よく振りながら明るい大きな目の笑顔を見せる。その後、礼儀正しい日本式のお辞儀（お辞儀）でわずかに頭を下げる。金色の星と小さなきらめきのシャワーが上から彼女の周りに降り注ぐ。紫の魔法のルーン文字が背景に一瞬現れてフェードアウトする。カメラ: ミディアムワイドから始まり、彼女がお辞儀する際にミディアムへとゆっくりズームイン。スタイル: 暖かく親しみやすい、他のシーンよりやや強い明るいライティング、水彩アニメ。尺: 7秒。モーション強度: 低〜中。

**推奨ツール**: Veo3（メイン）
**カメラワーク**: Medium-wide → slow zoom in to medium

---

### ツール別特性比較と使い分け

| ツール | 強み | 弱み | 最適シーン | 月額目安 |
|--------|------|------|-----------|---------|
| **Veo3** | 動作の滑らかさ・光の表現・参照画像対応 | 1クリップ8秒上限（仮説・要検証）・キャラ顔の細かい一貫性は不安定なことあり | シーン1・2・5 | 約2,900円（Google AI Pro） |
| **Runway Gen-3 Alpha** | 長めのクリップ（最大16秒）・スタイル維持が比較的安定 | 日本アニメ風の表現はVeo3より弱い傾向（仮説） | シーン3（長めのスピーチシーン） | 約1,500〜3,000円 |
| **Kling v1.6** | 顔アニメーションの安定性・コスト | 光表現やパーティクルは他ツールより弱い（仮説） | シーン4（表情フォーカス） | 約2,000〜4,000円 |
| **Sora（OpenAI）** | 高品質な動き・長尺（最大20秒）（仮説・要検証） | 商用利用条件・料金体系が変動中（要確認） | シーン3の代替 | 要確認 |

---

## セクション3：小道具・背景プロンプト

### 3-1. タロットカード裏面（統一デザイン用）

**Midjourney v7プロンプト（英語）**

```
Tarot card back design, ornate geometric pattern, 
deep purple background (#4C1D95), intricate gold mandala border, 
small scattered golden five-pointed stars and crescent moons, 
central diamond grid pattern in thin gold lines, 
art nouveau style borders, mystical and elegant, 
no text, symmetrical design, high detail, 
suitable for a cute fortune teller aesthetic, 
--ar 2:3 --stylize 600 --v 7
```

**日本語訳**

タロットカードの裏面デザイン、装飾的な幾何学模様、濃い紫色の背景（#4C1D95）、複雑な金色のマンダラボーダー、小さく散りばめられた金色の五芒星と三日月、細い金色の線によるダイヤモンドグリッドパターン、アールヌーボースタイルのボーダー、神秘的でエレガント、テキストなし、対称的なデザイン、高精細、かわいい占い師のエステティックに適合

### 3-2. タロットカード表面（各種シンボル用）

**「太陽」カード（陽の運勢）英語**

```
Tarot card, The Sun card design, cute kawaii anime style, 
bright golden sun with radiant rays, small cute sunflower field below, 
purple card border matching character's costume, gold lettering "THE SUN", 
watercolor texture, magical and cheerful, positive energy, 
--ar 2:3 --stylize 500 --v 7
```

**「月」カード（神秘・直感）英語**

```
Tarot card, The Moon card design, cute kawaii anime style, 
large crescent moon with gentle glow, two tiny cute dog silhouettes howling below, 
reflecting pool with purple shimmer, mysterious night atmosphere, 
purple and silver color palette, gold lettering "THE MOON", 
watercolor texture, --ar 2:3 --stylize 500 --v 7
```

### 3-3. 背景セット一覧

**背景A: 神秘の占い部屋（メインセット）英語**

```
Cozy mystical fortune teller's room interior, dark purple walls, 
wooden bookshelves filled with old books and crystal bottles, 
round table with dark purple velvet tablecloth, 
three lit candles in ornate brass holders casting warm amber glow, 
floating orbs of soft purple light, 
crystal ball on wooden stand glowing faintly blue-purple, 
window showing starry night sky, 
star charts and tarot-related posters on walls, 
warm candlelight mixed with cool magical purple ambient light, 
depth of field with foreground slightly blurred, 
watercolor anime style background, --ar 9:16 --stylize 400 --v 7
```

**日本語訳**

居心地のよい神秘的な占い師の部屋のインテリア、濃い紫色の壁、古い本や水晶の瓶がいっぱいの木製の本棚、濃い紫色のベルベットのテーブルクロスがかかった丸いテーブル、暖かいアンバーの光を放つ装飾的な真鍮のホルダーに収まった3本の点灯したキャンドル、やわらかな紫色の光の浮かぶ球体、かすかに青紫色に輝く木製スタンドの水晶玉、星空を見せる窓、壁に貼られた星図とタロット関連のポスター、クールな魔法的な紫のアンビエント光と混ざり合う暖かいろうそくの光、前景がわずかにぼかされた被写界深度、水彩アニメスタイルの背景

**背景B: 星空フィールド（バリエーション）英語**

```
Magical outdoor night scene, endless starry sky with milky way visible, 
soft glowing constellation lines in purple and gold, 
floating tarot cards drifting in the air, 
silver crescent moon large and luminous, 
gently rolling hills silhouette below, 
soft ground fog with purple and gold particles, 
dreamy fantasy atmosphere, 
watercolor anime background style, --ar 9:16 --stylize 500 --v 7
```

**背景C: ロウソクテーブル接写（シーン2専用）英語**

```
Extreme close-up of dark purple velvet table surface, 
single candle flame in soft focus background creating warm bokeh, 
scattered golden star confetti on velvet, 
three tarot cards face-down with purple and gold geometric back design, 
soft magical purple rim light from unknown source, 
particle dust floating in amber and purple light, 
watercolor texture overlay, cinematic depth of field, 
--ar 9:16 --stylize 350 --v 7
```

---

## セクション4：音声合成プロンプト（ElevenLabs v3）

### 4-1. キャラクターボイス設計

**キャラクターボイス仕様**

| 項目 | 設定値 | 理由 |
|------|--------|------|
| 性別 | 女性 | ターゲット（30〜50代女性・Z世代女性）への親和性 |
| 年齢感 | 10代後半〜20代前半（10_final_reportのLunaキャラ設定に準拠） | 若くかわいい印象を保つ |
| 口調 | やさしく穏やか、やや不思議ちゃん系、語尾に少し丸みがある | キャラのビジュアルとの一致 |
| 話速 | やや遅め（0.85〜0.90×）| 30〜60秒の短尺でも聞き取りやすさ優先 |
| ピッチ | 標準より+10〜15%高め | かわいさと聞き取りやすさのバランス |
| 感情表現 | 温かみ・神秘感・不思議さを混在させる | 占いコンテンツの雰囲気に合致 |

**ElevenLabs v3 Voice Design プロンプト（英語）**

```
Voice description: Young female voice, approximately 18-22 years old, 
soft and gentle tone with a slightly dreamy quality, 
speaks with warmth and quiet mystery, 
never loud or excited, always calm and reassuring, 
slight hint of playfulness without being childish, 
clear enunciation with natural Japanese-style pacing, 
occasional gentle rising inflections at sentence ends suggesting wonder, 
suitable for a cute fortune-telling anime character.
```

**日本語訳**

ボイスの説明: 若い女性の声、約18〜22歳、やわらかくやさしいトーン、わずかに夢見がちな質感、温かみと静かな神秘感を持って話す、大きな声や興奮は一切なく、常に落ち着いて安心感がある、子供っぽくない程度のわずかな遊び心、クリアな発音と自然な日本語ペーシング、不思議さを示す文末の時折やさしく上がる語調、かわいい占いアニメキャラクターに適した声。

### 4-2. セリフ別音声調整設定

**ElevenLabs SSML（仮説・サポート状況要確認）**

```xml
<!-- オープニング（神秘感を高める） -->
<speak>
  <prosody rate="slow" pitch="+10%">
    今日のカード、一緒に引いてみようか？
  </prosody>
  <break time="500ms"/>
  <prosody rate="x-slow" pitch="+5%">
    ...どんな答えが出るかな
  </prosody>
</speak>

<!-- カードめくり（ドラマチックに） -->
<speak>
  <break time="300ms"/>
  <prosody rate="slow" pitch="+12%">
    出たよ...
  </prosody>
  <break time="800ms"/>
  <emphasis level="moderate">太陽のカード！</emphasis>
</speak>

<!-- アドバイス部分（温かく丁寧に） -->
<speak>
  <prosody rate="0.88" pitch="+8%">
    今日はね、新しいことへの一歩を大切にしてみて。
    小さな変化が、大きな流れにつながっていくから。
  </prosody>
</speak>
```

### 4-3. 犬の鳴き声・感嘆符の挿入方法

犬の鳴き声（「クゥン」「ワン」）はElevenLabsでの自然な生成が困難なため、以下の2段階方式を推奨する。

**推奨手順**

```
Step 1: ElevenLabsで通常セリフ部分の音声を生成
Step 2: 鳴き声を別途調達（以下の3つの選択肢から選ぶ）

選択肢A（推奨）: Freesound.org / Pixabay Audio の著作権フリー犬の鳴き声素材を使用
  - 検索キーワード: "cute dog whimper", "puppy yelp", "small dog bark" 等
  - CC0ライセンスのものを選択し、クレジット表記不要を確認

選択肢B: ElevenLabsのSound Effects生成機能を使用
  プロンプト: "soft cute small dog whimper, single quiet kwoon sound, 
               high-pitched gentle puppy cry, 0.5 seconds"

選択肢C（仮説・要検証）: Adobe Auditionまたはizotopeのサウンドデザインで合成
  - 基音: 正弦波 800〜1200Hz、ピッチエンベロープで下降
  - リバーブを軽く付加して温かみを出す

Step 3: CapCutまたはAudacityでセリフ音声と鳴き声を合成
  - 鳴き声はセリフの間（ポーズ部分）または文末直後に挿入
  - 音量バランス: セリフ 100% / 鳴き声 60〜70%
```

### 4-4. Voice Cloning（将来的な使用。現状は設計のみ）

```
ElevenLabs v3 Voice Cloning 設定方針:
- 利用条件: Professional Voiceフィーチャー（Creatorプラン以上・要確認）
- サンプル音声: 最低30秒〜1分のクリーンな収録音声が必要
- 現時点ではキャラクターに対応する実際の声優/VAがいないため、
  Voice Designプロンプトによる生成を先行して採用し、
  IPが確立された後にVoice Cloningへ移行する方針とする（仮説）
- 注意: Voice Cloningで生成した声をSNS公開コンテンツに使用する際、
  元の声のサンプル提供者の同意書が必要（法務チェッカーへ確認が必須）
```

---

## セクション5：編集・合成指示

### 5-1. 全体的な編集フロー（CapCut対応）

```
推奨ソフト: CapCut（ショート動画向け・縦型9:16対応・無料プランあり）
代替: DaVinci Resolve（高品質だが習熟コストが高い）

基本フロー:
① Veo3でクリップ生成 → 各シーン別にダウンロード
② CapCutで新規プロジェクト作成（9:16、60fps、1080×1920px）
③ クリップを時系列に並べる（シーン1→2→3→4→5の順）
④ BGMを最下層トラックに配置（音量設定はセクション5-4参照）
⑤ SE（効果音）を各タイミングに配置
⑥ テロップを追加
⑦ AI生成ラベルをエンドカードまたは冒頭に追加
⑧ エクスポート: MP4、H.264、60fps、最大ビットレート設定
```

### 5-2. テロップ設計

**テロップ基本スタイル**

| 項目 | 設定 | 根拠 |
|------|------|------|
| フォント | Noto Sans JP Bold（ブランドガイドライン準拠） | 視認性・日本語対応 |
| サイズ | タイトルテロップ: 64〜72px相当 / 通常テロップ: 48px相当 | スマホ小画面での読みやすさ |
| カラー | 白（#FFFFFF）+ 黒いドロップシャドウ（オフセット2px、ぼかし4px） | 背景色に依存しない視認性 |
| 強調キーワード | 金色（#F59E0B）または紫（#7C3AED） | ブランドカラー準拠 |
| 位置 | 画面下部20〜30%エリア（人物の顔と重ならない位置） | キャラクターのビジュアルを損なわない |
| 最大行数 | 1画面あたり2行まで | 可読性確保 |
| アニメーション | フェードイン（0.3秒）、表示後0.3秒でフェードアウト | 自然な読みやすさ |

**テロップ内容設計例（第1弾動画）**

| タイミング | テロップテキスト | スタイル | 表示秒数 |
|-----------|---------------|---------|---------|
| 0〜2秒 | 今日の運勢を引くよ✨ | 強調（金色キーワード: 運勢） | 3秒 |
| 5〜8秒 | カードを選んでね | 通常 | 3秒 |
| 13〜17秒 | 【太陽のカード】 | 見出し（金色・大きめ） | 4秒 |
| 17〜28秒 | 新しい一歩を大切に/小さな変化が大きな流れへ | 通常・2行 | 8秒 |
| 45〜55秒 | 毎日占い更新中！/フォローしてね | 強調（紫キーワード: フォロー） | 5秒 |
| 55〜60秒 | AI生成コンテンツ | 小字・半透明（詳細はセクション7） | 5秒 |

### 5-3. 効果音（SE）挿入タイミング

| タイミング | 効果音 | 音量 | 素材源（推奨） |
|-----------|--------|------|--------------|
| オープニング最初の1秒 | 鈴の音（シングルトーン・高音） | 70% | Freesound.org（CC0） |
| カードを置く瞬間 | カードを置く柔らかい音（「ぺたん」） | 60% | Freesound.org（CC0） |
| カードをめくる瞬間 | カードめくり音（「さらっ」） | 65% | Freesound.org（CC0） |
| カードが光るエフェクト瞬間 | 魔法の輝き音（グリッターチャイム系） | 75% | Freesound.org（CC0） |
| 犬のリアクションシーン | クゥン（小型犬ウィンプ） | 65% | セクション4-3の手順に従う |
| エンディング手振り | 小さなチャイム音2連打 | 70% | Freesound.org（CC0） |

### 5-4. BGM選定指針

**BGM基本方針**

```
ジャンル: ヒーリング系 / 神秘的 / アンビエント
テンポ: 60〜80BPM（ゆったりとした印象）
楽器構成: ピアノ + ハープ + ストリングス + 軽いパーカッション
避けるべき: 歌詞付き、激しいビート、過度に西洋クラシック的な荘厳さ
目指すトーン: 「ファンタジー × かわいい × 少し神秘的」
音量バランス: 導入部50% → セリフ部分25〜30% → エンディング45%
```

**BGM調達オプション（著作権フリー優先）**

| オプション | 具体的な選択肢 | コスト | 確認事項 |
|-----------|------------|-------|---------|
| **推奨A** | Suno AI（AIミュージック生成）でオリジナル制作 | 月額約10ドル〜 | 商用利用条件を利用規約で確認すること（仮説・要確認） |
| **推奨B** | YouTube Audio Library「Healing」「Ambient」カテゴリ | 無料 | 一部はYouTube外での使用制限あり。利用規約確認必須 |
| 選択肢C | Artlist（年額約25,000円〜） | 有料 | SNS・商用利用可。ライセンス最も明確 |
| 選択肢D | Pixabay Music（CC0） | 無料 | CC0確認済みのもののみ使用 |

**Suno AIプロンプト例（テーマ曲生成用）**

```
[英語]
Instrumental background music, healing ambient, fantasy magical atmosphere, 
soft piano melody with gentle harp arpeggios, light string ensemble, 
occasional soft wind chimes, tempo 68 BPM, 
cute mysterious fortune teller aesthetic, Japanese anime inspired, 
no lyrics, loopable, 60 seconds, gentle fade in and fade out

[日本語訳]
インストゥルメンタルのバックグラウンドミュージック、ヒーリングアンビエント、ファンタジー魔法の雰囲気、ジェントルなハープのアルペジオを伴うやわらかいピアノのメロディ、軽いストリングアンサンブル、時折やわらかなウィンドチャイム、テンポ68BPM、かわいい神秘的な占い師のエステティック、日本のアニメにインスパイア、歌詞なし、ループ可能、60秒、やさしいフェードインとフェードアウト
```

---

## セクション6：キャラ一貫性維持のワークフロー

### 6-1. 第2本目以降の制作手順

```
【必須：キャラクターバイブル（Character Bible）の作成】

1本目の動画完成後、以下のファイルを作成してフォルダに保存すること:

キャラクターバイブル保存内容:
- 基準画像（正面・横・斜め）の高解像度PNG × 3枚
- Midjourney seed番号（Job IDから取得）
- 使用したプロンプト全文（このドキュメントを保存）
- Veo3参照画像として使用した画像のURL or ローカルパス
- 確定したカラーコード一覧（#7C3AED等）
- ElevenLabs Voice IDまたはSettings JSON

保存場所: research/fortune-ai-character-sns/video-shorts/character-bible/
```

**第2本目以降の制作チェックリスト**

```
[ ] キャラクターバイブルを参照して基準画像を確認した
[ ] Midjourney --cref に基準画像URLを設定した
[ ] Midjourney --seed に確定seed番号を設定した
[ ] Veo3のReference Image に基準画像を設定した
[ ] ElevenLabsのVoice IDを前回と同一に設定した
[ ] 衣装の色（紫 #7C3AED）・帽子のリボン（ピンク）・宝石（紫）の一致を生成後に目視確認した
[ ] 背景スタイルが既存動画と統一されているか確認した
```

### 6-2. 失敗例（崩れやすいポイント）と回避策

| 崩れるポイント | 発生原因 | 回避策 |
|--------------|---------|--------|
| 毛の色が変わる（全白・全茶になる） | cref未使用またはプロンプトの毛色記述不足 | 「brown and white two-tone」を必ずプロンプトに明記。crefを必ず使用 |
| 衣装の星模様が消える | stylize値が高すぎると細部が省略される | stylize 600〜750に保つ。ネガティブプロンプトに「plain clothing」を追加 |
| 目の大きさが変わる | アングル変更時にcref効果が弱まる | --cw 100 を明示（Character Weightを最大に）。プロンプトに「large round black eyes」を常に含める |
| Veo3でキャラが途中で人間になる | 参照画像の解像度不足またはプロンプトでのキャラ属性の明記不足 | Reference Imageを必ず設定。プロンプト冒頭に「anthropomorphized Shih Tzu dog character」を必ず書く |
| 口の動きが音声とズレる | ElevenLabsとVeo3の単純組み合わせ限界 | HedraまたはD-IDを使用して音声に合わせたリップシンクを生成（仮説・要検証） |
| しっぽが不自然な動きをする | 短毛犬プロンプトが混入している可能性 | 「long fluffy tail」「Shih Tzu long fur」を明記 |

### 6-3. シリーズ展開（占星術猫等）への横展開時の注意点

```
「ほしよみ」世界観には将来的にAria（占星術担当）・Kotone（数秘術担当）の
追加キャラが計画されている（10_final_report Part2参照）。
横展開時の統一ルール:

1. 世界観の統一
   - 背景（占い部屋・星空）は共通アセットを使用する
   - カラーパレット（紫・金・白）は全キャラ共通
   - BGMは同じシリーズの楽曲を使用（テーマ違いのバリエーション）

2. キャラ固有の識別要素を明確に分ける
   - Lunaシーズー犬: 紫マント・タロットカード
   - Aria（占星術猫・未設計）: 別の衣装色（青系推奨）+ 星座盤アイコン
   - Kotone（数秘術・未設計）: 別の衣装色（緑系推奨）+ 数字のカード
   ※ AriaとKotoneの詳細設計は別途ビジュアルデザイナーが担当

3. Midjourney cref の管理
   - 各キャラクターのseed・crefURLは必ずキャラクターバイブルに別ファイルとして保存
   - キャラ間でcrefを混在させないこと（崩れの原因）

4. 商標・著作権への注意
   - キャラクターIPの商標登録・意匠登録は早期に法務チェッカーへ確認を依頼すること
   - Midjourneyの商用利用規約（年収1億円超でProプラン必要・10_final_report参照）の確認を怠らないこと
```

---

## セクション7：AI生成表示義務対応

### 7-1. 各SNSのAI生成ラベル設定方法

**TikTok**

```
設定手順:
1. 投稿画面で「AIコンテンツ」トグルをONにする
2. 「AI生成の音声、映像、または画像が含まれています」を選択
3. これを設定しないと運営側が検出した場合にBAN・収益停止のリスクがある
   （AI量産コンテンツへの規制が2025〜2026年で強化中）
```

**YouTube / YouTube Shorts**

```
設定手順:
1. アップロード後の詳細設定画面で「変更または合成されたコンテンツ」をONにする
2. 「AI生成コンテンツが含まれます」にチェック
3. AI量産動画収益化除外ポリシー（2025年7月施行済み）の適用を避けるため、
   オリジナルIPキャラクターとしての編集上の工夫（セリフのオリジナリティ・占いコンテンツの独自性）を加えること
   （仮説・YouTubeポリシーの詳細は公式ヘルプを随時確認）
```

**Instagram**

```
設定手順:
1. 投稿後に「詳細設定」から「AIで作成」ラベルを追加
2. Reelsの場合は投稿フロー内でAIラベルを設定できる（仕様変更の可能性あり・要確認）
```

### 7-2. 動画内表示の推奨表記

**テロップとして動画内に常時表示する内容**

```
推奨表記（日本語）:
「このコンテンツはAIを使用して制作されています」

略称表記（画面スペースが少ない場合）:
「AI制作コンテンツ」

英語表記（海外向け投稿時）:
"This content is AI-generated"
```

**表示仕様**

| 項目 | 設定値 |
|------|--------|
| 配置 | 動画の右下または左下（キャラクターとテロップに被らない位置） |
| フォントサイズ | 24〜28px相当（小さすぎず・邪魔にならない） |
| カラー | 白（#FFFFFF）・透明度70%（半透明） |
| 表示タイミング | 動画全編を通して常時表示（または最初の5秒と最後の5秒） |
| アニメーション | なし（静的テキスト） |

**エンドカードへの追記（推奨）**

```
エンドカード最下部に以下を追記:
「※本動画は生成AIツール（Veo3 / Midjourney / ElevenLabs）を使用して制作したコンテンツです。
   占いの結果はエンターテインメント目的であり、断定的な判断を提供するものではありません。」

この免責表記は消費者契約法改正（2023年）への対応として必須（10_final_report Part1-1参照）。
```

---

## 付記：制作コスト概算（月次）

| 費目 | 月額目安 | 備考 |
|------|---------|------|
| Midjourney v7 Proプラン | 約3,000〜4,400円 | 商用利用・Fast時間60分 |
| Google AI Pro（Veo3込み） | 約2,900円 | Veo3生成クリップ数の上限あり（要確認） |
| ElevenLabs Creatorプラン | 約3,000〜4,500円 | 月10万文字相当（仮説） |
| Suno AI Proプラン | 約1,500円 | BGM生成用 |
| CapCut（ビジネスプラン） | 約4,000円（仮説） | 商用テンプレート利用時 |
| **合計** | **約14,400〜17,300円/月** | 5〜8万円/月の予算内に十分収まる |

---

## 次のステップ

1. キャラクター基準画像（正面・横・斜め）をMidjourney v7で生成し、最良の1枚をキャラクターバイブルに登録する
2. Veo3でシーン1〜5のテストクリップを各1本ずつ生成し、キャラ一貫性を目視確認する
3. ElevenLabsでボイスサンプルを3パターン生成し、関係者でレビューする
4. 上記3点が完了した時点で10_final_reportのアクションプラン「#6 AI動画生成技術の内部PoC」（期日: 2026-06-07）の完了報告を行う

---

*本プロンプト集は2026-05-13時点の各ツールの仕様・料金に基づく。Veo3・Midjourney・ElevenLabsは仕様変更が頻繁なため、PoC実施前に各公式サイトで最新情報を確認すること。仮説・未検証箇所は「（仮説）」「（要検証）」と明記している。*
