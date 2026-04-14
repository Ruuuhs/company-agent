#!/bin/bash
# company-agent ローカル環境セットアップスクリプト
# リポジトリをcloneした後に一度だけ実行してください

set -e

echo "=== company-agent セットアップ ==="
echo ""

# context/ フォルダの初期化
if [ -d "context" ]; then
  echo "[SKIP] context/ は既に存在します。スキップします。"
  echo "       （既存のコンテキストはそのまま保持されます）"
else
  echo "[INIT] context.template/ から context/ を生成します..."
  cp -r context.template/ context/
  echo "[OK]   context/ を作成しました。"
fi

echo ""
echo "=== セットアップ完了 ==="
echo ""
echo "次のステップ:"
echo "  1. context/company-state.md を開いて会社情報を入力してください"
echo "  2. context/activeContext.md を今日のフォーカスで更新してください"
echo "  3. 'claude' コマンドを実行してClaude Codeを起動してください"
echo ""
echo "  ※ context/ はgit管理対象外です。リモートにpushされません（個人専用）"
echo "  ※ バックアップはご自身でクラウドストレージ等に保管してください"
