SHELL := /bin/bash
ENV_FILE := products/web3-farming-kit/.env

setup:
	@echo "🔧 Checking Poetry..."
	@which poetry || (echo "❌ Poetry not found. Please install it." && exit 1)
	@echo "✅ Poetry found"
	@echo "📦 Installing dependencies..."
	@cd products/web3-farming-kit && poetry install
	@if [ ! -f $(ENV_FILE) ]; then \
	  echo "⚠️ .env not found. Create it from .env.example"; \
	else \
	  echo "✅ .env file exists"; \
	fi

run-cli:
	@poetry run python products/web3-farming-kit/main.py 0x1234567890abcdef1234567890abcdef12345678

run-bot:
	@poetry run python products/web3-farming-kit/bot/bot.py

run-ui:
	@poetry run streamlit run products/web3-farming-kit/ui/app.py

notifier:
	@poetry run python products/web3-farming-kit/bot/service.py

test:
	@poetry run pytest products/web3-farming-kit/tests/

deploy-render:
	@echo "🌐 To deploy to Render:"
	@echo "1. Push your code to GitHub"
	@echo "2. Connect repo in Render dashboard"
	@echo "3. It will pick up render.yaml automatically"

deploy-cloudrun:
	@echo "☁️ To deploy to Google Cloud Run:"
	@echo "Run:"
	@echo "  ./cloud-run-deploy.sh"
