# TechBot 🤖

AI chatbot specialized in recommending apps, software, and cloud services.
Automatically adapts responses to each user's technical level.

## Project structure

```
techbot/
├── app.py                  # Entry point — streamlit run app.py
├── requirements.txt
│
├── config/
│   └── prompts.py          # All prompt strings & level definitions
│
├── core/
│   ├── level_detector.py   # Classifies user text → beginner/intermediate/advanced
│   └── chat_engine.py      # Builds system prompt & streams Claude responses
│
├── state/
│   └── session.py          # Streamlit session-state init & helpers
│
└── ui/
    ├── page.py             # st.set_page_config()
    ├── styles.py           # Global dark-theme CSS
    ├── sidebar.py          # Settings panel & stats
    ├── header.py           # Title block & level badge
    └── chat.py             # Welcome message & conversation history
```

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Get your FREE Cloudflare credentials (no credit card needed):
#    - Account ID: dash.cloudflare.com → sidebar inferior derecho
#    - API Token:  dash.cloudflare.com/profile/api-tokens → Create Token
#                  usa la plantilla "Workers AI (Read)"
export CLOUDFLARE_ACCOUNT_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export CLOUDFLARE_API_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Windows CMD
set CLOUDFLARE_ACCOUNT_ID=xxxx...
set CLOUDFLARE_API_TOKEN=xxxx...

# 3. Run
streamlit run app.py
```

## Free tier (Cloudflare Workers AI)
- **10,000 Neurons gratis por día**, sin tarjeta de crédito.
- Modelo usado: `@cf/meta/llama-3.1-8b-instruct`
- Cada conversación consume ~100–500 Neurons según el largo.

## How level detection works

- On **auto** mode, the first message triggers a lightweight Claude call that
  returns a single word: `beginner`, `intermediate`, or `advanced`.
- Detection re-runs every 5 messages so TechBot adapts if the conversation shifts.
- Users can override the level at any time from the sidebar.