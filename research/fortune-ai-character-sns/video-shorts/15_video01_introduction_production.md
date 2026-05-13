# 第1本目動画 制作実行パッケージ｜ルナ初登場・自己紹介（30秒）

**作成日**: 2026-05-13
**用途**: TikTok / YouTube Shorts / Instagram Reels（縦9:16）
**ベース台本**: `13_short_video_scripts.md` パターン3
**ベースプロンプト**: `14_short_video_ai_prompts.md`
**ステータス**: 生成実行用・即着手可

---

## 0. 全体設計サマリ

| 項目 | 内容 |
|------|------|
| キャラ | ルナ（タロット占い師シーズー犬） |
| 尺 | 30秒 |
| シーン数 | 5カット（各3〜10秒） |
| 推奨ツール | Veo3（メイン動画） / Midjourney v7（基準画像） / ElevenLabs v3（音声） / Suno AI（BGM） / CapCut（編集） |
| 縦横比 | 9:16（1080×1920px） |
| フレームレート | 60fps |
| 想定制作時間 | 初回PoC 6〜8時間（基準画像確定含む） |
| 想定コスト | 月額ツール費 約14,400〜17,300円のうち1本制作分 |

---

## 1. 制作フロー（実行順）

```
STEP 1: キャラクター基準画像生成（Midjourney v7）       … 60〜90分
STEP 2: 各シーンの動画クリップ生成（Veo3）              … 30〜60分/シーン × 5
STEP 3: ナレーション音声生成（ElevenLabs v3）           … 30分
STEP 4: BGM・SE調達（Suno AI / Freesound.org）         … 30分
STEP 5: 編集・テロップ・AIラベル付与（CapCut）          … 60〜90分
STEP 6: 投稿前チェック（法務・AIラベル・字幕）          … 15分
```

---

## 2. STEP 1: キャラクター基準画像生成（Midjourney v7）

### 2-1. 正面構図プロンプト（マスター画像用）

**英語（コピペ用）**:
```
Cute anthropomorphized Shih Tzu dog fortune teller, chibi anime style, standing front view, large round black sparkling eyes, soft shy smile, brown and white long fluffy fur, wearing purple starry cloak with scattered gold star embroidery, purple beret hat with pink ribbon slightly tilted, small purple amethyst gemstone necklace, holding three tarot cards with purple and gold geometric pattern back design, watercolor illustration style, soft pastel lighting, magical fantasy atmosphere, purple and gold color palette, white background for reference sheet, full body character design --ar 2:3 --stylize 750 --v 7
```

**実行手順**:
1. Discord または Midjourney Web で上記を投稿
2. 4枚生成 → 最良の1枚を Upscale
3. 右クリック → "Copy Image Address" で **基準画像URL** を取得・保存
4. 右クリック → "Copy Job ID" で **seed番号** を取得・保存

**保存先**: `research/fortune-ai-character-sns/video-shorts/character-bible/luna_master_front.png`

### 2-2. ネガティブプロンプト（Stable Diffusion使用時のみ）

```
realistic photography, 3D render, ugly, deformed, extra fingers, malformed hands, blurry, low quality, nsfw, scary expression, sharp angular features, western cartoon style, human face without fur, no costume, plain clothing, different colored eyes, asymmetrical ears, inconsistent fur pattern, text artifacts, watermarks
```

### 2-3. キャラ崩れ回避の必須設定

| 項目 | 設定 |
|------|------|
| `--cref` | 基準画像URL（2回目以降の生成すべてに必須） |
| `--cw` | `100`（Character Weightを最大化） |
| `--seed` | 初回生成のJob IDから固定 |
| `--stylize` | `750` を維持 |
| `--v` | `7`（cref対応バージョン） |

---

## 3. STEP 2: シーン別動画生成プロンプト（Veo3）

### 共通パラメータ

| 項目 | 設定 |
|------|------|
| Reference Image | STEP 1で確定した基準画像をアップロード |
| Aspect Ratio | 9:16（縦） |
| Motion Intensity | Low（キャラ崩れ防止） |
| 言語 | プロンプトは英語推奨 |
| 1クリップ最大尺 | 8秒（仮説・要確認） |

---

### シーン1（0:00〜0:02・2秒）：ドラマチック登場

**台本セリフ**: 「あ…はじめまして。」（ルナ・少し恥ずかしそうに）
**演出意図**: 視聴者の手を止める一瞬のフック。キャラの第一印象を決定づける

**Veo3プロンプト（英語・コピペ用）**:
```
A cute chibi anime-style anthropomorphized Shih Tzu dog character pops into frame from a dark purple background, her purple beret with pink ribbon slightly tilted to one side. She has large round sparkling black eyes, brown and white fluffy fur, wearing a purple starry cloak with gold star patterns. Her expression is shy and slightly embarrassed, her cheeks faintly blushing. Small golden sparkles burst around her as she appears. Background: deep purple gradient with soft floating purple light orbs. Camera: static medium-close shot, slight zoom-in pop. Style: soft watercolor anime, pastel tones, magical kawaii atmosphere. Duration: 2 seconds. Motion intensity: Low.
```

**期待される出力**:
- 暗い紫背景からルナがふわっと飛び出す
- ベレー帽がわずかに傾いている（ギャップの可愛さ演出）
- 頬が少し赤らんだ恥ずかしそうな表情
- 周囲に金色のきらめきパーティクル

---

### シーン2（0:02〜0:08・6秒）：自己紹介＋カードを掲げる

**台本セリフ**: 「わたし、ルナといいます。タロット占い師をしているシーズー犬です。（ワン）」
**演出意図**: キャラ名・職業の明確化。ベレー帽を直す仕草で愛着形成

**Veo3プロンプト（英語・コピペ用）**:
```
Cute chibi anime-style anthropomorphized Shih Tzu dog character facing camera in medium shot. She gently adjusts her tilted purple beret with pink ribbon using one paw, then holds up three tarot cards (purple and gold geometric back design) fanned out in her other paw at chest height. Her large black eyes look directly at camera with a warm gentle smile. Brown and white long fluffy fur sways softly. Tail wags slowly behind her. Background: cozy mystical fortune teller's room with soft purple bokeh candlelight and floating golden dust particles. Camera: static medium shot, very subtle push-in. Style: soft watercolor anime, warm candlelight plus purple ambient. Duration: 6 seconds. Motion intensity: Low.
```

**期待される出力**:
- ベレー帽を片足でちょこんと直す
- もう片足でタロット3枚を扇形に掲げる
- カメラ目線で穏やかに微笑む
- 背景は神秘的な占い部屋

---

### シーン3（0:08〜0:18・10秒）：カードを広げようとして手元がもたつく ★最重要カット

**台本セリフ**: 「毎日1枚、カードを引いて、今日のあなたにちょっとしたヒントをお届けしたいなと思っています。あくまでエンタメとして、気軽に楽しんでもらえたら嬉しいです。」
**演出意図**: シーズー犬らしい不器用さで「ギャップの可愛さ」を最大化。**キャラへの親しみの核**

**Veo3プロンプト（英語・コピペ用）**:
```
Close-up to medium shot of cute chibi anime-style anthropomorphized Shih Tzu dog character at a round table covered with dark purple velvet. She tries to fan out tarot cards on the table with both small paws but the cards slip and slide awkwardly, scattering slightly. She tilts her head with an embarrassed sheepish smile, one ear flopping down. Her cheeks blush faintly. She then carefully gathers the cards back together with both paws, glancing up at camera with an apologetic warm smile. Background: cozy fortune teller's room with three lit candles casting warm amber glow, blurred bookshelves. Camera: medium shot, very subtle handheld feel, slight push-in during the gather-back motion. Style: soft watercolor anime, warm candlelight, kawaii moe expression. Duration: 8 seconds. Motion intensity: Low-Medium.
```

**注意**: Veo3は8秒上限のため、このシーン10秒は2クリップに分割
- クリップ3a（4秒）: カードを広げようとしてもたつく
- クリップ3b（4秒）: カードを集め直して照れ笑い

**期待される出力**:
- カードを扇形に広げようとして失敗する不器用な動き
- 片耳がぺたっと垂れる照れ表情
- 頬がほんのり赤らむ
- カードを集め直してカメラに申し訳なさそうな笑顔

---

### シーン4（0:18〜0:25・7秒）：1枚引いて裏向きで掲げる＋「クゥン」

**台本セリフ**: 「もう1枚、引いてみました。（クゥン）これ…なかなかいいカードです。次の動画で開けますね。」
**演出意図**: 続編への期待感を生む。「クゥン」で感情の動きを表現

**Veo3プロンプト（英語・コピペ用）**:
```
Medium close-up of cute chibi anime-style anthropomorphized Shih Tzu dog character. She gracefully picks up one tarot card from the table with both paws and holds it face-down toward the camera at chest height. Her expression shifts to one of pleasant surprise—eyes widen slightly with sparkles, both ears perk up, small soft smile. She tilts her head slightly to the right in a curious adorable manner. The card has a purple and gold geometric back design that subtly glows. Background: warm candlelit fortune teller's room with purple bokeh. Camera: static medium close-up centered on character and card. Style: soft watercolor anime, warm magical glow on card edges. Duration: 7 seconds. Motion intensity: Low.
```

**期待される出力**:
- カードを優雅に取り上げる
- 視聴者にカードを掲げる
- 目を見開いて両耳ピンと立つ「驚き喜び」表情
- 首を右に傾けるあざとかわいい仕草

---

### シーン5（0:25〜0:30・5秒）：お辞儀＋しっぽふり

**台本セリフ**: 「フォローして、待っていてもらえますか？よろしくお願いします。」
**演出意図**: フォロー誘導の最大化。礼儀正しく可愛い締めくくり

**Veo3プロンプト（英語・コピペ用）**:
```
Medium-wide shot of cute chibi anime-style anthropomorphized Shih Tzu dog character standing at her table. She places three tarot cards face-down in a neat pile, looks up at camera with a bright wide-eyed smile, tail wagging energetically behind her, then performs a polite Japanese-style bow (ojigi) with her head and shoulders dipping forward. A gentle shower of golden stars and small sparkles falls from above around her. Background: warm candlelit room with subtle purple magical runes briefly appearing and fading. Camera: starts medium-wide, slowly zooms in to medium shot during the bow. Style: warm and inviting watercolor anime, slightly brighter lighting than other scenes. Duration: 5 seconds. Motion intensity: Low-Medium.
```

**期待される出力**:
- カードをきれいに重ねる
- カメラに笑顔で見上げる
- しっぽを元気よく振る
- 礼儀正しいお辞儀
- 上から金の星が降る

---

## 4. STEP 3: ナレーション音声生成（ElevenLabs v3）

### 4-1. ボイス設計プロンプト

```
Voice description: Young female voice, approximately 18-22 years old, soft and gentle tone with a slightly dreamy quality, speaks Japanese with warmth and quiet mystery, never loud or excited, always calm and reassuring, slight hint of shyness and playfulness without being childish, clear enunciation with natural Japanese pacing, occasional gentle rising inflections at sentence ends suggesting wonder. Suitable for a cute fortune-telling anime character (Shih Tzu dog persona).
```

### 4-2. セリフ別生成テキスト（コピペ用）

**シーン1**（少し恥ずかしそうに）:
```
あ……はじめまして。
```
- 設定: rate 0.85x, pitch +12%, 「あ」と「はじめまして」の間に0.4秒のbreak

**シーン2**:
```
わたし、ルナといいます。タロット占い師をしているシーズー犬です。
```
- 設定: rate 0.88x, pitch +10%, 「ルナ」を軽く強調
- 文末に犬の鳴き声「ワン」を別ファイルで合成（後述）

**シーン3**（少し早口で照れ気味）:
```
毎日1枚、カードを引いて、今日のあなたにちょっとしたヒントをお届けしたいなと思っています。あくまでエンタメとして、気軽に楽しんでもらえたら嬉しいです。
```
- 設定: rate 0.90x, pitch +10%, 「ヒント」「エンタメ」を軽く強調
- **法務上の最重要セリフ**：「あくまでエンタメ」を確実に発音

**シーン4**:
```
もう1枚、引いてみました。これ……なかなかいいカードです。次の動画で開けますね。
```
- 設定: rate 0.85x, pitch +10%, 「これ」の後に0.5秒のbreak、「クゥン」を別ファイルで合成

**シーン5**:
```
フォローして、待っていてもらえますか？よろしくお願いします。
```
- 設定: rate 0.88x, pitch +12%, 「フォロー」を軽く強調、「？」の語尾を上げる

### 4-3. 犬の鳴き声「ワン」「クゥン」の調達

**選択肢A（推奨・無料）**: Freesound.org または Pixabay Audio
- 検索キーワード: "cute dog whimper kwoon", "puppy yelp small soft", "shih tzu bark gentle"
- CC0ライセンスのみ採用

**選択肢B**: ElevenLabs Sound Effects
```
プロンプト: "single soft cute small dog whimper, gentle high-pitched puppy kwoon sound, 0.6 seconds, warm and adorable"
プロンプト: "single small dog soft bark, friendly puppy wan sound, 0.4 seconds, cheerful"
```

---

## 5. STEP 4: BGM・SE調達

### 5-1. BGM（Suno AIで生成）

**Suno AIプロンプト（英語・コピペ用）**:
```
Instrumental background music, healing fantasy ambient, soft piano melody with gentle harp arpeggios, light celesta and string ensemble, occasional soft wind chimes, tempo 70 BPM, cute mysterious fortune teller aesthetic, Japanese kawaii anime inspired, warm candlelight feeling, no lyrics, loopable, 35 seconds total length, gentle fade in at start and gentle fade out at end
```

**音量バランス**:
- 0:00〜0:08（自己紹介前半）: 30%
- 0:08〜0:18（メッセージ部分）: 20%（セリフを聞かせる）
- 0:18〜0:30（後半・締め）: 35%

### 5-2. SE（効果音）

| タイミング | 効果音 | 音量 | 調達先 |
|-----------|------|------|--------|
| 0:00 | ポップな登場音（「ぽん！」） | 75% | Freesound.org "cute pop sound" |
| 0:02 | 鈴の音1回（高音） | 60% | Freesound.org "single bell chime" |
| 0:08〜0:18 | カードを擦る音（軽く） | 40% | Freesound.org "card shuffle gentle" |
| 0:18 | カードを取る「すっ」 | 55% | Freesound.org "card pickup soft" |
| 0:25 | 小さなチャイム2連 | 65% | Freesound.org "magical sparkle chime" |
| 0:28 | 星が降る「キラキラ」 | 55% | Freesound.org "star sparkle fall" |

---

## 6. STEP 5: 編集・テロップ（CapCut）

### 6-1. プロジェクト設定

| 項目 | 値 |
|------|---|
| 解像度 | 1080×1920px（縦9:16） |
| フレームレート | 60fps |
| エクスポート形式 | MP4 / H.264 / 最大ビットレート |

### 6-2. テロップ仕様

**フォント**: Noto Sans JP Bold
**カラー**: 白（#FFFFFF）+ 黒ドロップシャドウ（オフセット2px・ぼかし4px）
**強調キーワード**: 金色（#F59E0B）

### 6-3. テロップ配置タイムライン

| タイミング | テロップ | スタイル | 表示時間 |
|----------|--------|--------|--------|
| 0:00〜0:02 | はじめまして🌙 | 大・中央・弾むアニメ | 2秒 |
| 0:02〜0:08 | タロット占い師の **ルナ** です | 中・下部・「ルナ」金色 | 6秒 |
| 0:08〜0:18 | 毎日1枚カードを引きます／*あくまでエンタメです* | 中・下部・2行 | 10秒 |
| 0:18〜0:25 | 次の動画でカードを開けます | 大・下部 | 7秒 |
| 0:25〜0:30 | フォローして待っててね🐾 | 大・下部・「フォロー」金色 | 5秒 |
| 全編 | AI制作コンテンツ | 小・右下・半透明70% | 常時 |

### 6-4. AI生成ラベル（必須）

**画面内表示**（全編表示）:
- 位置：右下
- フォント：Noto Sans JP Regular 24px
- カラー：白70%透明
- テキスト：「AI制作コンテンツ」

**エンドカード追記**（最終1秒）:
```
※本動画は生成AIツール（Veo3 / Midjourney / ElevenLabs / Suno AI）を使用して制作したコンテンツです。
※占いの結果はエンターテインメント目的であり、断定的な判断を提供するものではありません。
```

---

## 7. STEP 6: 投稿前チェックリスト

```
[ ] AI生成ラベルを画面内に常時表示しているか
[ ] エンドカードに免責表記（占い＝エンタメ）を入れているか
[ ] 「絶対」「必ず」「運命」「確定」「霊感」を使っていないか
[ ] キャラの一貫性が崩れていないか（毛色・衣装色・目）
[ ] 音声と口の動きが大きくズレていないか
[ ] 全シーンが繋がって自然に流れるか
[ ] ハッシュタグを設定したか
[ ] TikTok投稿時：「AIコンテンツ」トグルをONにしたか
[ ] YouTube Shorts投稿時：「変更または合成されたコンテンツ」をONにしたか
[ ] Instagram Reels投稿時：「AIで作成」ラベルを付与したか
```

---

## 8. プラットフォーム別投稿設定

### TikTok

**タイトル/キャプション**:
```
はじめまして！タロット占い師のルナです🌙
毎日1枚、あなたにヒントをお届けします
※AIで作ったキャラです・占いはエンタメとしてお楽しみください
```

**ハッシュタグ**:
```
#タロット #初投稿 #タロット占い師 #ルナのタロット #シーズー #AIキャラ #占いTikTok #タロット好きな人と繋がりたい #フォローして #はじめまして
```

**設定**:
- AIコンテンツトグル: ON
- コメント: ON
- デュエット/リミックス: ON（拡散促進）

### YouTube Shorts

**タイトル**: 「はじめまして🌙タロット占い師のルナです【AIキャラ初登場】」

**説明欄**:
```
はじめまして、タロット占い師のルナです🌙
わたしはAIで作られたシーズー犬のキャラクターで、毎日1枚タロットカードを引いて、あなたにちょっとしたヒントをお届けします。

※本動画は生成AIツールで制作しています
※占いの結果はエンターテインメント目的であり、断定的な判断を提供するものではありません

#タロット #タロット占い #AIキャラ #シーズー犬
```

**設定**:
- 「変更または合成されたコンテンツ」: ON
- 視聴者層: すべての視聴者向け（子ども向けではない）
- 言語: 日本語

### Instagram Reels

**キャプション**:
```
はじめまして🌙
タロット占い師のルナです

毎日1枚、あなたにそっとヒントをお届けします
あくまでエンタメとして気軽に楽しんでね

🐾 AIで作ったキャラクターです
🔮 占い結果はエンタメ目的です

#タロット #タロット占い #AIアート #シーズー犬 #占い好きと繋がりたい
```

---

## 9. PoC評価指標（投稿後24〜72時間）

| 指標 | 目標値（仮説） | 測定方法 |
|------|------------|---------|
| 完視聴率 | 50%以上 | TikTok Analytics |
| 平均視聴時間 | 18秒以上（30秒中の60%） | TikTok / YouTube Analytics |
| エンゲージメント率 | 3%以上 | (いいね＋コメント＋シェア) ÷ 再生数 |
| フォロワー獲得 | 投稿後72h以内に50人以上 | 各PFの増加数 |
| キャラ一貫性の崩れ | コメント0件 | コメント定性チェック |
| 法務指摘 | コメント0件 | 「断定」「霊感」等の指摘がないか |

---

## 10. 失敗時のフォールバック

| 失敗パターン | 対処 |
|-----------|------|
| Veo3でキャラの毛色が崩れる | Reference Image を高解像度版に差し替え、`anthropomorphized Shih Tzu dog` を冒頭強調 |
| 音声と口の動きがズレる | Hedra または D-IDでリップシンク再生成（仮説・要検証） |
| シーン3のもたつき演出が伝わらない | Kling v1.6 で再生成（顔表情の安定性が高い・仮説） |
| 完視聴率が30%未満 | テロップを増やす、冒頭2秒のフック強化 |
| 「キャラ崩壊」コメント多数 | キャラクターバイブルを強化、Midjourney `--cw 100` 確認 |

---

## 付記：制作コスト概算（本動画1本あたり）

| 費目 | コスト | 備考 |
|------|------|------|
| Midjourney v7 | 約100〜200円分 | 基準画像生成（Fast時間消費） |
| Veo3 | 約500〜800円分 | 5〜8クリップ生成 |
| ElevenLabs | 約100〜200円分 | 音声合成5本 |
| Suno AI | 約50〜100円分 | BGM 1曲 |
| CapCut | 0円 | 無料プラン |
| **合計** | **約750〜1,300円/本** | 月30本投稿で約23,000〜39,000円 |

---

*本パッケージは台本（13）・AI動画プロンプト集（14）から第1本目「ルナ初登場・自己紹介型30秒」に絞って統合・実行用にカスタマイズしたものである。Veo3・Midjourney・ElevenLabsの仕様変更が頻繁なため、生成実行前に各公式サイトで最新仕様を確認すること。*
