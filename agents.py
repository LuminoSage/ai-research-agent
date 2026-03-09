import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

load_dotenv()

# ── LLM setup ─────────────────────────────────────────────────────────────
def get_llm():
    return LLM(
        model="mistral/mistral-small-latest",
        api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0.5,
    )

# ── Tool setup ─────────────────────────────────────────────────────────────
search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

# ── Agents ─────────────────────────────────────────────────────────────────

def research_specialist():
    return Agent(
        role="Research Specialist",
        goal=(
            "Search the web thoroughly and gather comprehensive, accurate, "
            "and up-to-date information about the given research topic."
        ),
        backstory=(
            "You are an expert research analyst with years of experience "
            "finding credible sources and extracting the most relevant facts. "
            "You leave no stone unturned and always verify information from "
            "multiple sources before passing it on."
        ),
        tools=[search_tool],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )


def content_analyst():
    return Agent(
        role="Content Analyst",
        goal=(
            "Critically analyze the raw research gathered and identify the key "
            "themes, insights, patterns, and gaps. Structure the findings logically."
        ),
        backstory=(
            "You are a sharp analytical thinker who specializes in making sense "
            "of large amounts of information. You are great at spotting what "
            "matters, what's missing, and how pieces of information connect. "
            "You always produce clear, structured analysis."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )


def content_writer():
    return Agent(
        role="Content Writer",
        goal=(
            "Transform the structured analysis into a polished, engaging, and "
            "well-formatted research report that anyone can understand."
        ),
        backstory=(
            "You are a professional writer who turns complex research into clear, "
            "compelling reports. You write in a crisp, informative style with "
            "proper headings, bullet points where needed, and a strong summary. "
            "Your reports are always publication-ready."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
    )