# LuminoSage AI ✦

A multi-agent research system that does your Googling, thinking, and writing for you.
Not because you're lazy. Because you're *efficient*.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)
![CrewAI](https://img.shields.io/badge/CrewAI-1.9.3-purple?style=flat-square)
![Mistral](https://img.shields.io/badge/LLM-Mistral_AI-orange?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square)

---

## What it does

You type a question. Three AI agents argue about it (professionally), then hand you a clean research report. You take the credit. Everyone wins.

```
Your question  →  Researcher  →  Analyst  →  Writer  →  Your report
```

**The agents:**

- **Researcher** — scours the web so you don't have to open 14 tabs
- **Analyst** — figures out what actually matters in all that noise  
- **Writer** — turns it into something readable (unlike my commit messages)

---

## Project structure

```
ai-research-agent/
├── agents/
│   ├── research_specialist.py
│   ├── data_analyst.py
│   └── content_writer.py
├── tasks/
│   ├── research_task.py
│   ├── analysis_task.py
│   └── writing_task.py
├── crew.py          ← where the agents actually meet
├── app.py           ← the pretty face
├── requirements.txt
└── .env.example
```

---

## Setup (5 minutes, I timed it)

**1. Clone it**
```bash
git clone https://github.com/LuminoSage/ai-research-agent.git
cd ai-research-agent
```

**2. Create a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
pip install litellm
```

**4. Get your API keys** (both free, no credit card)

| Key | Where |
|-----|-------|
| `MISTRAL_API_KEY` | https://console.mistral.ai |
| `SERPER_API_KEY` | https://serper.dev |

**5. Add them to `.env`**
```bash
cp .env.example .env
# open .env and paste your keys
```

**6. Run**
```bash
streamlit run app.py
```

Open `http://localhost:8501` and ask it something.

---

## Queries that work well

- *"Latest breakthroughs in fusion energy 2025"*
- *"How is AI changing drug discovery?"*
- *"Explain quantum computing like I have a CS degree but forgot everything"*

---

## Tech stack

- **[CrewAI](https://crewai.com)** — the multi-agent framework doing the heavy lifting
- **[Mistral AI](https://mistral.ai)** — the LLM powering the agents (free tier)
- **[SerperDev](https://serper.dev)** — real-time web search (2500 free searches/month)
- **[Streamlit](https://streamlit.io)** — the UI that makes it look like I know design

---

## Common issues

**`signal only works in main thread`** — harmless warning from CrewAI telemetry. Add `CREWAI_TELEMETRY_OPT_OUT=true` to your `.env` to silence it.

**`Invalid API Key`** — you probably copy-pasted with a space. Check your `.env`.

**Agents seem stuck** — they're not. Mistral is thinking. Give it 30–60 seconds. Research takes time, even for AI.

---

## Notes

- Python 3.12 recommended. 3.14 breaks half the AI libraries (they're not ready for the future yet)
- The `.env` file is gitignored on purpose. Don't commit your API keys. Please.
- If an agent fails mid-run, check your Mistral/Serper quotas first before debugging for an hour

---

Built by [Krish Jain](https://github.com/YOUR_USERNAME) · CS 
