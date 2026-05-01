# =============================================================================
# LLM Observability デモ — Langfuse + Claude
# =============================================================================
#
#   初回: make setup
#   毎回: make up  /  make chat  /  make down
#   確認: make status  /  make logs
#
# =============================================================================

.PHONY: help setup setup-env setup-venv up down restart status logs chat clean reset

SHELL := /bin/bash
COMPOSE := docker compose
APP_DIR := app
VENV := $(APP_DIR)/.venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# デフォルトターゲット
help: ## コマンド一覧を表示
	@echo ""
	@echo "  LLM Observability デモ"
	@echo "  ======================"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'
	@echo ""

# ---------------------------------------------------------------------------
# 初回セットアップ
# ---------------------------------------------------------------------------
setup: setup-env setup-venv up ## 初回セットアップ（env作成→venv→Langfuse起動）
	@echo ""
	@echo "============================================"
	@echo "  セットアップ完了!"
	@echo "============================================"
	@echo ""
	@echo "  1. Langfuse UI を開いてください:"
	@echo "     http://localhost:3000"
	@echo ""
	@echo "  2. アカウント作成 → プロジェクト作成 → APIキー取得"
	@echo ""
	@echo "  3. app/.env を編集してキーを設定:"
	@echo "     ANTHROPIC_API_KEY=sk-ant-xxxxx"
	@echo "     LANGFUSE_PUBLIC_KEY=pk-lf-xxxxx"
	@echo "     LANGFUSE_SECRET_KEY=sk-lf-xxxxx"
	@echo ""
	@echo "  4. チャット開始:"
	@echo "     make chat"
	@echo ""

setup-env: ## .envファイルを生成（シークレット自動生成）
	@if [ ! -f .env ]; then \
		echo "[setup] .env を生成しています..."; \
		NEXTAUTH_SECRET=$$(openssl rand -hex 32); \
		SALT=$$(openssl rand -hex 32); \
		ENCRYPTION_KEY=$$(openssl rand -hex 32); \
		PG_PASS=$$(openssl rand -hex 16); \
		CH_PASS=$$(openssl rand -hex 16); \
		REDIS_PASS=$$(openssl rand -hex 16); \
		MINIO_PASS=$$(openssl rand -hex 16); \
		sed \
			-e "s|changeme-generate-with-openssl-rand-hex-32|$$NEXTAUTH_SECRET|1" \
			-e "s|changeme-generate-with-openssl-rand-hex-32|$$SALT|1" \
			-e "s|changeme-generate-with-openssl-rand-hex-32|$$ENCRYPTION_KEY|1" \
			-e "s|changeme-postgres-password|$$PG_PASS|g" \
			-e "s|changeme-clickhouse-password|$$CH_PASS|g" \
			-e "s|changeme-redis-password|$$REDIS_PASS|g" \
			-e "s|changeme-minio-password|$$MINIO_PASS|g" \
			.env.example > .env; \
		echo "[OK] .env 生成完了（シークレット自動生成済み）"; \
	else \
		echo "[skip] .env は既に存在します"; \
	fi
	@if [ ! -f $(APP_DIR)/.env ]; then \
		cp $(APP_DIR)/.env.example $(APP_DIR)/.env; \
		echo "[OK] app/.env 生成完了（APIキーを手動で設定してください）"; \
	else \
		echo "[skip] app/.env は既に存在します"; \
	fi

setup-venv: ## Python仮想環境を作成して依存パッケージをインストール
	@if [ ! -d $(VENV) ]; then \
		echo "[setup] Python仮想環境を作成しています..."; \
		python3 -m venv $(VENV); \
		$(PIP) install --upgrade pip -q; \
		$(PIP) install -r $(APP_DIR)/requirements.txt -q; \
		echo "[OK] 仮想環境セットアップ完了"; \
	else \
		echo "[skip] 仮想環境は既に存在します（更新: make pip-install）"; \
	fi

pip-install: ## 依存パッケージを再インストール
	$(PIP) install --upgrade pip -q
	$(PIP) install -r $(APP_DIR)/requirements.txt
	@echo "[OK] パッケージインストール完了"

# ---------------------------------------------------------------------------
# Langfuse 操作
# ---------------------------------------------------------------------------
up: ## Langfuseを起動
	$(COMPOSE) up -d
	@echo ""
	@echo "[OK] Langfuse起動中..."
	@echo "     UI: http://localhost:3000"
	@echo "     状態確認: make status"

down: ## Langfuseを停止
	$(COMPOSE) down
	@echo "[OK] Langfuse停止"

restart: ## Langfuseを再起動
	$(COMPOSE) down
	$(COMPOSE) up -d
	@echo "[OK] Langfuse再起動完了"

status: ## 全コンテナの状態を表示
	@$(COMPOSE) ps

logs: ## Langfuseのログを表示（Ctrl+Cで終了）
	$(COMPOSE) logs -f langfuse-web langfuse-worker

logs-all: ## 全コンテナのログを表示
	$(COMPOSE) logs -f

# ---------------------------------------------------------------------------
# アプリ実行
# ---------------------------------------------------------------------------
chat: ## CLIチャットアプリを起動
	@if [ ! -d $(VENV) ]; then \
		echo "[ERROR] 仮想環境がありません。先に make setup を実行してください。"; \
		exit 1; \
	fi
	cd $(APP_DIR) && ../$(PYTHON) main.py

# ---------------------------------------------------------------------------
# クリーンアップ
# ---------------------------------------------------------------------------
clean: ## 仮想環境を削除
	rm -rf $(VENV)
	@echo "[OK] 仮想環境を削除しました"

reset: ## 全データを削除して初期状態に戻す（要確認）
	@echo "Langfuseの全データ（DB・ボリューム）を削除します。"
	@read -p "本当に実行しますか？ [y/N]: " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		$(COMPOSE) down -v; \
		rm -rf $(VENV); \
		rm -f .env $(APP_DIR)/.env; \
		echo "[OK] 全データを削除しました。make setup で再構築できます。"; \
	else \
		echo "キャンセルしました"; \
	fi
