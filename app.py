import os
import traceback
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="LuminoSage — Research Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600;700;900&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body { margin: 0; padding: 0; }

.stApp {
    background: #0a0a0a !important;
    background-image:
        radial-gradient(ellipse 70% 50% at 0% 0%,   rgba(124,58,237,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 50% 40% at 100% 100%, rgba(16,185,129,0.07) 0%, transparent 55%) !important;
    font-family: 'Outfit', sans-serif;
    min-height: 100vh;
}

/* ── Strip ALL Streamlit chrome ── */
#MainMenu,
footer,
header,
div[data-testid="stToolbar"],
div[data-testid="stDecoration"],
div[data-testid="stStatusWidget"],
div[data-testid="collapsedControl"],
section[data-testid="stSidebar"] { display: none !important; visibility: hidden !important; }

.block-container,
div[data-testid="stMainBlockContainer"],
div[data-testid="stAppViewBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 3px; height: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #1e1e1e; border-radius: 99px; }
* { scrollbar-width: thin; scrollbar-color: #1e1e1e transparent; }

/* ══ PAGE SHELL ══ */
.ls-page {
    max-width: 880px;
    margin: 0 auto;
    padding: 52px 28px 120px;
}

/* ══ NAV ══ */
.ls-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 68px;
    flex-wrap: wrap;
    gap: 12px;
}
.ls-brand {
    display: flex;
    align-items: center;
    gap: 10px;
}
.ls-brand-mark {
    width: 34px; height: 34px;
    border-radius: 9px;
    background: linear-gradient(140deg, #7c3aed 0%, #10b981 100%);
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 4px 20px rgba(124,58,237,0.25);
}
.ls-brand-name {
    font-family: 'Outfit', sans-serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: -0.035em;
}
.ls-brand-name .w { color: #f5f5f5; }
.ls-brand-name .v { color: #a78bfa; }
.ls-nav-r { display: flex; align-items: center; gap: 7px; flex-wrap: wrap; }

.ls-pill {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.04em;
    color: #3a3a3a;
    border: 1px solid #1d1d1d;
    border-radius: 99px;
    padding: 4px 12px;
    line-height: 1.4;
    white-space: nowrap;
}
.ls-pill-green {
    color: #10b981 !important;
    border-color: rgba(16,185,129,0.22) !important;
    background: rgba(16,185,129,0.05) !important;
    display: inline-flex; align-items: center; gap: 6px;
}
.ls-dot-pulse {
    width: 5px; height: 5px; border-radius: 50%;
    background: #10b981; flex-shrink: 0;
    animation: dp 1.8s ease-in-out infinite;
}
@keyframes dp { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.2;transform:scale(.7)} }

/* ══ HERO ══ */
.ls-hero { margin-bottom: 56px; }
.ls-kicker {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #7c3aed;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex; align-items: center; gap: 12px;
    opacity: 0.8;
}
.ls-kicker::before {
    content: '';
    width: 24px; height: 1px;
    background: currentColor;
    opacity: 0.6;
    flex-shrink: 0;
}
.ls-h1-block { line-height: 1; margin-bottom: 6px; }
.ls-h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(44px, 8vw, 80px);
    font-weight: 900;
    line-height: 0.88;
    letter-spacing: -0.048em;
    color: #f0f0f0;
    display: block;
}
.ls-h1-accent {
    font-family: 'Instrument Serif', serif;
    font-style: italic;
    font-weight: 400;
    font-size: clamp(46px, 8.5vw, 84px);
    line-height: 0.95;
    letter-spacing: -0.02em;
    display: block;
    background: linear-gradient(118deg, #a78bfa 15%, #34d399 85%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 28px;
}
.ls-hero-sub {
    font-family: 'Outfit', sans-serif;
    font-size: 15px;
    font-weight: 300;
    color: #404040;
    max-width: 460px;
    line-height: 1.78;
}
.ls-hero-sub strong { color: #666; font-weight: 500; }

/* ══ PIPELINE ══ */
.ls-flow {
    display: flex;
    align-items: stretch;
    overflow-x: auto;
    scrollbar-width: none;
    margin-bottom: 40px;
    gap: 0;
    padding-bottom: 2px;
}
.ls-flow::-webkit-scrollbar { display: none; }

.ls-node {
    display: flex; align-items: center; gap: 11px;
    background: #0f0f0f;
    border: 1px solid #191919;
    border-radius: 12px;
    padding: 13px 17px;
    flex-shrink: 0;
    cursor: default;
    transition: border-color .2s, background .2s;
}
.ls-node:hover { border-color: #2c2c2c; background: #141414; }

.ls-ico {
    width: 34px; height: 34px;
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.ico-v  { background: rgba(124,58,237,0.13); }
.ico-a  { background: rgba(245,158,11,0.1); }
.ico-w  { background: rgba(16,185,129,0.1); }
.ico-rp { background: rgba(249,115,22,0.1); }

.ls-node-lbl {
    font-family: 'DM Mono', monospace;
    font-size: 9px; color: #2c2c2c;
    text-transform: uppercase; letter-spacing: .1em;
    margin-bottom: 3px;
}
.ls-node-name {
    font-family: 'Outfit', sans-serif;
    font-size: 12px; font-weight: 600;
    color: #aaa; white-space: nowrap; letter-spacing: -.01em;
}
.ls-arrow {
    font-family: 'DM Mono', monospace;
    font-size: 16px; color: #1d1d1d;
    padding: 0 5px; flex-shrink: 0;
    display: flex; align-items: center;
    user-select: none;
}

/* ══ FILE STRIP ══ */
.ls-filestrip {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 7px;
    padding: 14px 18px;
    background: rgba(255,255,255,0.015);
    border: 1px solid #171717;
    border-radius: 13px;
    margin-bottom: 44px;
}
.ls-filestrip-lbl {
    font-family: 'DM Mono', monospace;
    font-size: 9px; color: #282828;
    text-transform: uppercase; letter-spacing: .12em;
    margin-right: 6px; flex-shrink: 0;
}
.ls-fbadge {
    display: inline-flex; align-items: center; gap: 5px;
    font-family: 'DM Mono', monospace; font-size: 10px;
    border-radius: 7px; padding: 4px 10px;
    border: 1px solid #1d1d1d; background: #0d0d0d;
    white-space: nowrap;
}
.fb-agent { color: #8b5cf6; border-color: rgba(139,92,246,.2); }
.fb-task  { color: #34d399; border-color: rgba(52,211,153,.18); }
.fb-core  { color: #fbbf24; border-color: rgba(251,191,36,.18); }
.fb-sep {
    font-family: 'DM Mono', monospace;
    font-size: 9px; color: #1d1d1d;
    padding: 0 4px; user-select: none;
}

/* ══ INPUT CARD ══ */
.ls-icard {
    background: #0e0e0e;
    border: 1px solid #1a1a1a;
    border-radius: 18px;
    padding: 24px 24px 18px;
    margin-bottom: 14px;
}
.ls-icard-top {
    display: flex; align-items: center;
    justify-content: space-between;
    margin-bottom: 14px; flex-wrap: wrap; gap: 8px;
}
.ls-icard-lbl {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: #2e2e2e;
    text-transform: uppercase; letter-spacing: .14em;
    display: flex; align-items: center; gap: 7px;
}
.ls-vdot {
    width: 5px; height: 5px; border-radius: 50%;
    background: #a78bfa; flex-shrink: 0;
}
.ls-icard-hint {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: #1e1e1e;
}

/* textarea */
div[data-testid="stTextArea"] label { display: none !important; }
div[data-testid="stTextArea"] > div { background: transparent !important; border: none !important; }
div[data-testid="stTextArea"] textarea {
    background: #080808 !important;
    border: 1px solid #1e1e1e !important;
    border-radius: 11px !important;
    color: #ddd !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 15px !important; font-weight: 300 !important;
    line-height: 1.75 !important;
    padding: 16px 18px !important;
    resize: none !important;
    caret-color: #a78bfa !important;
    transition: border-color .2s, box-shadow .2s !important;
    box-shadow: none !important;
}
div[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(167,139,250,.3) !important;
    box-shadow: 0 0 0 3px rgba(167,139,250,.06) !important;
    outline: none !important;
}
div[data-testid="stTextArea"] textarea::placeholder {
    color: #202020 !important; font-style: italic !important;
}

/* chips */
.ls-chips { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 14px; }
.ls-chip {
    font-family: 'DM Mono', monospace; font-size: 10px;
    color: #2e2e2e; border: 1px solid #191919;
    border-radius: 99px; padding: 5px 12px;
    white-space: nowrap; cursor: default;
    transition: all .18s;
}
.ls-chip:hover { color: #a78bfa; border-color: rgba(167,139,250,.22); background: rgba(167,139,250,.04); }

/* ══ RUN BUTTON ══ */
div[data-testid="stButton"] > button {
    background: #f0f0f0 !important;
    color: #080808 !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important; font-weight: 700 !important;
    letter-spacing: -.015em !important;
    padding: 15px 40px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all .2s ease !important;
}
div[data-testid="stButton"] > button:hover {
    background: #ebe5ff !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 14px 36px rgba(124,58,237,.2) !important;
}
div[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
    box-shadow: none !important;
}

/* ══ STATUS WIDGET ══ */
div[data-testid="stStatus"] {
    background: #0d0d0d !important;
    border: 1px solid #1a1a1a !important;
    border-radius: 12px !important;
    margin-top: 16px !important;
}
div[data-testid="stStatus"] p,
div[data-testid="stStatus"] span,
div[data-testid="stStatus"] div {
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important; color: #3a3a3a !important;
}

/* ══ REPORT HEADER ══ */
.ls-report-hdr {
    display: flex; align-items: center; gap: 12px;
    margin: 48px 0 22px;
    padding-bottom: 16px;
    border-bottom: 1px solid #141414;
    flex-wrap: wrap;
}
.ls-report-badge {
    font-family: 'DM Mono', monospace; font-size: 9px;
    color: #10b981;
    background: rgba(16,185,129,.07);
    border: 1px solid rgba(16,185,129,.15);
    border-radius: 99px; padding: 4px 13px;
    letter-spacing: .12em; text-transform: uppercase;
}
.ls-report-title {
    font-family: 'Outfit', sans-serif;
    font-size: 11px; font-weight: 600;
    color: #252525; letter-spacing: -.01em;
}

/* ══ MARKDOWN CONTENT ══ */
div[data-testid="stMarkdown"] h1 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 22px !important; font-weight: 800 !important;
    color: #eeeeee !important; letter-spacing: -.03em !important;
    margin: 30px 0 12px !important; line-height: 1.2 !important;
    border: none !important;
}
div[data-testid="stMarkdown"] h2 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 16px !important; font-weight: 700 !important;
    color: #ccc !important; letter-spacing: -.02em !important;
    margin: 26px 0 10px !important;
    padding-bottom: 8px !important;
    border-bottom: 1px solid #161616 !important;
}
div[data-testid="stMarkdown"] h3 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 13px !important; font-weight: 600 !important;
    color: #a78bfa !important;
    margin: 20px 0 8px !important; letter-spacing: .01em !important;
}
div[data-testid="stMarkdown"] p {
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important; font-weight: 300 !important;
    color: #585858 !important; line-height: 1.85 !important;
    margin-bottom: 12px !important;
}
div[data-testid="stMarkdown"] ul,
div[data-testid="stMarkdown"] ol { padding-left: 20px !important; }
div[data-testid="stMarkdown"] li {
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important; font-weight: 300 !important;
    color: #585858 !important; line-height: 1.8 !important;
    margin-bottom: 5px !important;
}
div[data-testid="stMarkdown"] strong { color: #d8d8d8 !important; font-weight: 600 !important; }
div[data-testid="stMarkdown"] em    { color: #777 !important; font-style: italic !important; }
div[data-testid="stMarkdown"] a     { color: #a78bfa !important; text-decoration: underline !important; text-decoration-color: rgba(167,139,250,.3) !important; }
div[data-testid="stMarkdown"] code {
    font-family: 'DM Mono', monospace !important;
    background: rgba(167,139,250,.08) !important;
    color: #a78bfa !important;
    padding: 2px 7px !important; border-radius: 5px !important; font-size: 12px !important;
}
div[data-testid="stMarkdown"] pre code {
    display: block !important; padding: 16px !important;
    border-radius: 10px !important; font-size: 12px !important;
    border: 1px solid #1a1a1a !important;
}
div[data-testid="stMarkdown"] blockquote {
    border-left: 2px solid #a78bfa !important;
    padding-left: 16px !important; margin: 16px 0 !important;
    color: #484848 !important; font-style: italic !important;
}
div[data-testid="stMarkdown"] hr {
    border: none !important;
    border-top: 1px solid #141414 !important;
    margin: 28px 0 !important;
}
div[data-testid="stMarkdown"] table {
    width: 100% !important; border-collapse: collapse !important;
    font-family: 'DM Mono', monospace !important; font-size: 12px !important;
}
div[data-testid="stMarkdown"] th {
    background: #0f0f0f !important; color: #555 !important;
    border-bottom: 1px solid #1d1d1d !important;
    padding: 8px 12px !important; text-align: left !important;
}
div[data-testid="stMarkdown"] td {
    border-bottom: 1px solid #141414 !important;
    padding: 8px 12px !important; color: #484848 !important;
}

/* ══ DOWNLOAD ROW ══ */
.ls-dl-row {
    display: flex; align-items: center;
    gap: 12px; flex-wrap: wrap;
    padding: 18px 0 0;
    border-top: 1px solid #141414;
    margin-top: 36px;
}
.ls-dl-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: #252525; letter-spacing: .06em;
    flex-grow: 1;
}

div[data-testid="stDownloadButton"] > button {
    background: transparent !important;
    color: #383838 !important;
    border: 1px solid #1c1c1c !important;
    border-radius: 10px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important; letter-spacing: .07em !important;
    padding: 9px 18px !important;
    width: auto !important;
    transform: none !important; box-shadow: none !important;
    transition: all .18s !important;
}
div[data-testid="stDownloadButton"] > button:hover {
    color: #a78bfa !important;
    border-color: rgba(167,139,250,.25) !important;
    background: rgba(167,139,250,.05) !important;
    transform: none !important; box-shadow: none !important;
}

/* ══ ALERTS ══ */
div[data-testid="stAlert"] {
    border-radius: 11px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important;
}

/* ══ EXPANDER ══ */
details[data-testid="stExpander"] {
    background: #0d0d0d !important;
    border: 1px solid #1a1a1a !important;
    border-radius: 10px !important;
}
details[data-testid="stExpander"] summary {
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important; color: #333 !important;
}

/* ══ FOOTER ══ */
.ls-footer {
    margin-top: 88px; padding-top: 22px;
    border-top: 1px solid #131313;
    display: flex; align-items: center;
    justify-content: space-between; flex-wrap: wrap; gap: 10px;
}
.ls-footer-l {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: #1f1f1f;
}
.ls-footer-r {
    font-family: 'DM Mono', monospace;
    font-size: 10px; color: #1f1f1f;
    display: flex; align-items: center; gap: 0;
}
.ls-fsep { color: #181818; margin: 0 9px; }

/* ══ RESPONSIVE ══ */
@media (max-width: 700px) {
    .ls-page { padding: 36px 16px 80px; }
    .ls-nav { margin-bottom: 48px; }
    .ls-h1 { font-size: 38px; }
    .ls-h1-accent { font-size: 40px; }
    .ls-hero-sub { font-size: 14px; max-width: 100%; }
    .ls-nav-r { gap: 5px; }
    .ls-pill { font-size: 9px; padding: 3px 9px; }
    .ls-node { padding: 10px 12px; min-width: 0; }
    .ls-node-name { font-size: 11px; }
    .ls-ico { width: 28px; height: 28px; }
    .ls-icard { padding: 18px 14px 14px; }
    .ls-chip { font-size: 9px; padding: 5px 10px; }
    .ls-filestrip { padding: 11px 14px; }
    .ls-fbadge { font-size: 9px; padding: 3px 8px; }
}
@media (max-width: 440px) {
    .ls-h1 { font-size: 30px; }
    .ls-h1-accent { font-size: 32px; }
    .ls-nav-r .ls-pill:not(.ls-pill-green) { display: none; }
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
#  API KEY CHECKS
# ══════════════════════════════════════════════════════════════════════════
def check_keys():
    missing = []
    if not os.getenv("MISTRAL_API_KEY") or os.getenv("MISTRAL_API_KEY") == "your_mistral_api_key_here":
        missing.append(("MISTRAL_API_KEY", "https://console.mistral.ai"))
    if not os.getenv("SERPER_API_KEY") or os.getenv("SERPER_API_KEY") == "your_serper_api_key_here":
        missing.append(("SERPER_API_KEY", "https://serper.dev"))
    return missing

missing_keys = check_keys()
if missing_keys:
    for key, url in missing_keys:
        st.error(f"**{key}** missing — get it free at {url}")
    st.stop()

# Lazy import after key check
try:
    from crew import run_research_crew
except ImportError as e:
    st.error(f"Could not import from crew.py: {e}")
    st.stop()

# Session state
if "result" not in st.session_state:
    st.session_state.result = None
if "last_query" not in st.session_state:
    st.session_state.last_query = ""

# ══════════════════════════════════════════════════════════════════════════
#  PAGE START
# ══════════════════════════════════════════════════════════════════════════
st.markdown('<div class="ls-page">', unsafe_allow_html=True)

# ── NAV ───────────────────────────────────────────────────────────────────
st.markdown("""
<nav class="ls-nav">
  <div class="ls-brand">
    <div class="ls-brand-mark">
      <svg viewBox="0 0 24 24" fill="none" stroke="#fff"
           stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"
           width="16" height="16">
        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14
                         18.18 21.02 12 17.77 5.82 21.02
                         7 14.14 2 9.27 8.91 8.26 12 2"/>
      </svg>
    </div>
    <div class="ls-brand-name">
      <span class="w">Lumino</span><span class="v">Sage</span>
    </div>
  </div>
  <div class="ls-nav-r">
    <span class="ls-pill">CrewAI</span>
    <span class="ls-pill">Mistral AI</span>
    <span class="ls-pill ls-pill-green">
      <span class="ls-dot-pulse"></span>live
    </span>
  </div>
</nav>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ls-hero">
  <div class="ls-kicker">Multi-Agent Research Intelligence</div>
  <div class="ls-h1-block">
    <span class="ls-h1">Research,</span>
    <span class="ls-h1-accent">Reimagined.</span>
  </div>
  <p class="ls-hero-sub">
    Three specialized agents — <strong>researcher</strong>,
    <strong>analyst</strong>, <strong>writer</strong> — collaborate
    in sequence to turn any question into a structured,
    publication-ready report you can download and keep.
  </p>
</div>
""", unsafe_allow_html=True)

# ── PIPELINE ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="ls-flow">

  <div class="ls-node">
    <div class="ls-ico ico-v">
      <svg viewBox="0 0 24 24" fill="none" stroke="#a78bfa"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
           width="15" height="15">
        <circle cx="11" cy="11" r="8"/>
        <line x1="21" y1="21" x2="16.65" y2="16.65"/>
      </svg>
    </div>
    <div>
      <div class="ls-node-lbl">Agent 01</div>
      <div class="ls-node-name">Researcher</div>
    </div>
  </div>

  <div class="ls-arrow">›</div>

  <div class="ls-node">
    <div class="ls-ico ico-a">
      <svg viewBox="0 0 24 24" fill="none" stroke="#f59e0b"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
           width="15" height="15">
        <line x1="9" y1="21" x2="15" y2="21"/>
        <line x1="12" y1="17" x2="12" y2="21"/>
        <path d="M12 2a7 7 0 0 1 7 7c0 2.62-1.4 4.9-3.5 6.2V17H8.5v-1.8A7 7 0 0 1 5 9a7 7 0 0 1 7-7z"/>
      </svg>
    </div>
    <div>
      <div class="ls-node-lbl">Agent 02</div>
      <div class="ls-node-name">Analyst</div>
    </div>
  </div>

  <div class="ls-arrow">›</div>

  <div class="ls-node">
    <div class="ls-ico ico-w">
      <svg viewBox="0 0 24 24" fill="none" stroke="#10b981"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
           width="15" height="15">
        <path d="M12 20h9"/>
        <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
      </svg>
    </div>
    <div>
      <div class="ls-node-lbl">Agent 03</div>
      <div class="ls-node-name">Writer</div>
    </div>
  </div>

  <div class="ls-arrow">›</div>

  <div class="ls-node">
    <div class="ls-ico ico-rp">
      <svg viewBox="0 0 24 24" fill="none" stroke="#f97316"
           stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
           width="15" height="15">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <line x1="10" y1="9" x2="8" y2="9"/>
      </svg>
    </div>
    <div>
      <div class="ls-node-lbl">Output</div>
      <div class="ls-node-name">Report</div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── FILE STRUCTURE STRIP ───────────────────────────────────────────────────
st.markdown("""
<div class="ls-filestrip">
  <span class="ls-filestrip-lbl">Project files</span>

  <span class="ls-fbadge fb-agent">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
      <circle cx="9" cy="7" r="4"/>
      <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
      <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
    </svg>
    app.py
  </span>

  <span class="ls-fbadge fb-agent">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <line x1="18" y1="20" x2="18" y2="10"/>
      <line x1="12" y1="20" x2="12" y2="4"/>
      <line x1="6"  y1="20" x2="6"  y2="14"/>
    </svg>
    agents.py
  </span>

  <span class="ls-fbadge fb-agent">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <path d="M12 20h9"/>
      <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
    </svg>
    crew.py
  </span>

  <span class="ls-fbadge" style="color:#1d1d1d; border-color:#141414;">·</span>

  <span class="ls-fbadge fb-task">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <circle cx="11" cy="11" r="8"/>
      <line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    agents.py
  </span>

  <span class="ls-fbadge fb-task">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <polyline points="9 11 12 14 22 4"/>
      <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
    </svg>
    
  </span>

  <span class="ls-fbadge fb-task">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <path d="M12 20h9"/>
      <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
    </svg>
    
  </span>

  <span class="ls-fbadge" style="color:#1d1d1d; border-color:#141414;">·</span>

  <span class="ls-fbadge fb-core">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <circle cx="12" cy="12" r="3"/>
      <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
      <path d="M4.93 4.93a10 10 0 0 0 0 14.14"/>
    </svg>
    crew.py
  </span>

  <span class="ls-fbadge fb-core">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" width="10" height="10">
      <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
      <line x1="8" y1="21" x2="16" y2="21"/>
      <line x1="12" y1="17" x2="12" y2="21"/>
    </svg>
    app.py
  </span>
</div>
""", unsafe_allow_html=True)

# ── INPUT CARD ────────────────────────────────────────────────────────────
st.markdown("""
<div class="ls-icard">
  <div class="ls-icard-top">
    <div class="ls-icard-lbl">
      <span class="ls-vdot"></span>Research Query
    </div>
    <span class="ls-icard-hint">be specific → better results</span>
  </div>
""", unsafe_allow_html=True)

query = st.text_area(
    label="q",
    label_visibility="collapsed",
    height=112,
    placeholder="What do you want to know? e.g. How is AI changing drug discovery in 2025?",
)

st.markdown("""
  <div class="ls-chips">
    <span class="ls-chip">↳ AI impact on software jobs 2025</span>
    <span class="ls-chip">↳ Fusion energy breakthroughs</span>
    <span class="ls-chip">↳ CRISPR latest applications</span>
    <span class="ls-chip">↳ Quantum computing progress</span>
    <span class="ls-chip">↳ Multi-agent AI systems</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── RUN BUTTON ────────────────────────────────────────────────────────────
st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
run = st.button("Run Research Pipeline  →", use_container_width=True)

# ── EXECUTION ─────────────────────────────────────────────────────────────
if run:
    if not query or not query.strip():
        st.warning("Type a research query above first.")
    else:
        st.session_state.result    = None
        st.session_state.last_query = query.strip()
        err_msg   = None
        err_trace = None

        with st.status("Running pipeline — agents working...", expanded=True) as status:
            st.write("› **Researcher** scanning and gathering sources...")
            st.write("› **Analyst** processing and evaluating findings...")
            st.write("› **Writer** drafting the final report...")
            try:
                result = run_research_crew(query.strip())
                st.session_state.result = str(result)
                status.update(
                    label="Pipeline complete — report ready ✦",
                    state="complete",
                    expanded=False
                )
            except Exception as e:
                err_msg   = str(e)
                err_trace = traceback.format_exc()
                status.update(label="Pipeline failed", state="error")

        if err_msg:
            st.error(f"**Error:** {err_msg}")
            with st.expander("Full traceback"):
                st.code(err_trace)

# ── REPORT DISPLAY ────────────────────────────────────────────────────────
if st.session_state.result:
    result_str = st.session_state.result
    safe_name  = st.session_state.last_query[:42].replace(" ", "_").replace("/", "-")

    st.markdown("""
    <div class="ls-report-hdr">
      <span class="ls-report-badge">✦ Generated</span>
      <span class="ls-report-title">LuminoSage Research Report</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(result_str)

    # ── Download row ──────────────────────────────────────────────────────
    st.markdown("""
    <div class="ls-dl-row">
      <span class="ls-dl-label">↓ Save this report to use it later</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 1, 1])
    with col2:
        st.download_button(
            label="↓  Markdown  .md",
            data=result_str,
            file_name=f"luminosage_{safe_name}.md",
            mime="text/markdown",
            key="dl_md",
        )
    with col3:
        st.download_button(
            label="↓  Plain text  .txt",
            data=result_str,
            file_name=f"luminosage_{safe_name}.txt",
            mime="text/plain",
            key="dl_txt",
        )

# ── FOOTER ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="ls-footer">
  <span class="ls-footer-l">LuminoSage AI — built by Krish Jain</span>
  <div class="ls-footer-r">
    <span>CrewAI</span><span class="ls-fsep">/</span>
    <span>Mistral AI</span><span class="ls-fsep">/</span>
    <span>SerperDev</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)