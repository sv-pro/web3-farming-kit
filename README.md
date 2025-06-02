# Web3 Farming Kit

🧰 A modular toolkit for onchain activity tracking, retrodrop farming, and bot-based automation.

## 🚀 Quickstart

### 1. Install dependencies
```bash
poetry install
```

### 2. Create .env file
```bash
cp .env.example .env
# Then edit the values
```

### 3. Run CLI
```bash
poetry run python main.py 0xYourWalletAddress
```

### 4. Run Telegram bot
```bash
poetry run python bot/bot.py
```

## 📁 Structure
```
core/   - core business logic
cli/    - command-line interface (Click)
bot/    - Telegram bot
ui/     - Streamlit interface
db/     - MongoDB integration
utils/  - loggers and helpers
```

## 🔐 Access & Secrets Management

- Keep all sensitive access data in `meta/vault.md`
- Store `.env` in Bitwarden or encrypted (`.env.gpg`)
- Never commit `.env` to Git
