"""
Langfuse + OpenAI GPT CLIチャットアプリ

Langfuseの@observeデコレータを使って、OpenAI APIへのリクエストを
自動的にトレーシングするデモアプリケーションです。

使い方:
  1. .env.example を .env にコピーしてAPIキーを設定
  2. pip install -r requirements.txt
  3. python main.py
"""

import os
import sys
import threading
import itertools
import time
import uuid
from datetime import datetime

from dotenv import load_dotenv

# .envファイルから環境変数を読み込む（ルート .env を優先）
_root_env = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
load_dotenv(dotenv_path=_root_env, override=True)

from openai import OpenAI
import langfuse
from langfuse import observe, get_client


# --------------------------------------------------------------------------
# スピナー（思考中の表示）
# --------------------------------------------------------------------------
# Braille spinner + パルスドット
_SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
_PULSE_DOTS = ["   ", ".  ", ".. ", "...", " ..", "  .", "   "]


class Spinner:
    """API応答待ちの間に表示するアニメーションスピナー。"""

    def __init__(self, message: str = "Thinking"):
        self._message = message
        self._stop = threading.Event()
        self._thread = None
        self._elapsed = 0.0

    def start(self):
        self._stop.clear()
        self._elapsed = 0.0
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join()
        # スピナー行をクリア
        print(f"\r{' ' * 50}\r", end="", flush=True)

    def _spin(self):
        interval = 0.08
        frame_idx = 0
        dot_idx = 0
        dot_tick = 0
        while not self._stop.is_set():
            spinner_char = _SPINNER_FRAMES[frame_idx % len(_SPINNER_FRAMES)]
            dots = _PULSE_DOTS[dot_idx % len(_PULSE_DOTS)]
            sec = f"{self._elapsed:.1f}s"
            line = f"\r  \033[36m{spinner_char}\033[0m {self._message} \033[2m{dots} {sec}\033[0m"
            print(line, end="", flush=True)
            time.sleep(interval)
            self._elapsed += interval
            frame_idx += 1
            dot_tick += 1
            if dot_tick % 3 == 0:
                dot_idx += 1

# --------------------------------------------------------------------------
# 環境変数バリデーション
# --------------------------------------------------------------------------
REQUIRED_ENV_VARS = [
    "OPENAI_API_KEY",
    "LANGFUSE_PUBLIC_KEY",
    "LANGFUSE_SECRET_KEY",
    "LANGFUSE_HOST",
]


def _validate_env() -> None:
    """必要な環境変数が設定されているか確認する。"""
    missing = [v for v in REQUIRED_ENV_VARS if not os.environ.get(v)]
    if missing:
        print(f"[ERROR] 以下の環境変数が未設定です: {', '.join(missing)}")
        print("  .env.example を .env にコピーして値を設定してください。")
        sys.exit(1)


# --------------------------------------------------------------------------
# Langfuse 認証チェック
# --------------------------------------------------------------------------
def _check_langfuse_connection() -> None:
    """Langfuseへの接続を確認する。"""
    try:
        client = get_client()
        if client.auth_check():
            print("[OK] Langfuse接続確認完了")
        else:
            print("[WARN] Langfuse認証に失敗しました。トレースは記録されない可能性があります。")
    except Exception as e:
        print(f"[WARN] Langfuse接続チェック中にエラー: {e}")
        print("  Langfuseサーバーが起動しているか確認してください。")


# --------------------------------------------------------------------------
# LLM呼び出し (トレーシング対象)
# --------------------------------------------------------------------------
@observe(name="gpt-chat", as_type="generation")
def call_gpt(messages: list[dict], model: str = "gpt-4o-mini") -> str:
    """
    OpenAI GPT APIを呼び出す。

    @observeデコレータにより、この関数の入出力・実行時間・トークン使用量が
    Langfuseに自動的に記録されます。
    """
    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        max_tokens=1024,
        messages=messages,
    )

    result = response.choices[0].message.content
    return result


# --------------------------------------------------------------------------
# チャットパイプライン (トレーシング対象)
# --------------------------------------------------------------------------
def chat_pipeline(user_input: str, history: list[dict], session_id: str, turn: int) -> str:
    """
    ユーザー入力を受け取り、GPTに送信し、回答を返す。

    propagate_attributes で session_id を設定し、
    同一セッション内の全ターンをLangfuse UIの Sessions 画面でまとめて確認できます。
    """
    with langfuse.propagate_attributes(
        session_id=session_id,
        metadata={"turn": str(turn)},
    ):
        # @observe をコンテキスト内で呼ぶために内部関数で実行
        return _run_pipeline(user_input, history)


@observe(name="chat-pipeline")
def _run_pipeline(user_input: str, history: list[dict]) -> str:
    # ユーザーメッセージを履歴に追加
    history.append({"role": "user", "content": user_input})

    # GPT APIを呼び出し
    response_text = call_gpt(messages=history)

    # アシスタントの応答を履歴に追加
    history.append({"role": "assistant", "content": response_text})

    return response_text


# --------------------------------------------------------------------------
# メインループ
# --------------------------------------------------------------------------
def main() -> None:
    """CLIチャットアプリのメインループ。"""
    _validate_env()

    langfuse_host = os.environ.get("LANGFUSE_HOST", "http://localhost:3000")

    print()
    print("  \033[1m\033[36m>>> Langfuse + GPT CLI Chat <<<\033[0m")
    print()

    # 起動チェック
    sys.stdout.write("  Langfuse  ")
    sys.stdout.flush()
    langfuse_ok = False
    try:
        client = get_client()
        if client.auth_check():
            print("\033[32m● connected\033[0m")
            langfuse_ok = True
        else:
            print("\033[31m● auth failed\033[0m")
    except Exception:
        print("\033[31m● offline\033[0m")

    if langfuse_ok:
        print(f"  Traces   \033[2m{langfuse_host}\033[0m")
    else:
        print("  \033[2m※ Traces will not be recorded. Check .env\033[0m")

    # セッションID生成（同一チャットセッションの全ターンを紐づける）
    session_id = f"chat-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"

    print(f"  Session  \033[2m{session_id}\033[0m")
    print()
    print("  \033[2mquit / exit / q で終了\033[0m")
    print("  ─────────────────────────────────")

    history: list[dict] = []
    turn = 0

    while True:
        try:
            print()
            user_input = input("  \033[32mYou\033[0m > ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            break

        turn += 1
        spinner = Spinner("Thinking")
        spinner.start()
        try:
            response = chat_pipeline(user_input, history, session_id, turn)
            spinner.stop()
            print(f"  \033[33mGPT\033[0m > {response}")
        except Exception as e:
            spinner.stop()
            print(f"  \033[31mERROR\033[0m > {e}")

    # Langfuseのバッファをフラッシュして全トレースを送信
    print()
    print("  ─────────────────────────────────")
    try:
        langfuse_client = get_client()
        langfuse_client.flush()
        if langfuse_ok and turn > 0:
            print(f"  \033[32m✓\033[0m {turn} traces flushed")
            print(f"  \033[2m{langfuse_host}\033[0m")
    except Exception:
        pass
    print("  \033[2mBye!\033[0m")
    print()


if __name__ == "__main__":
    main()
