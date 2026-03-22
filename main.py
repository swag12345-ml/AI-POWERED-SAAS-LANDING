"""
HIRELYZER — Intelligent Career Platform
Landing Page · Streamlit · Rebuilt from scratch
─────────────────────────────────────────────────
Architecture
  • All CSS in one inject_css() call — no style leakage
  • All JS in one inject_js() call — no script leakage
  • HTML rendered only via h() helper, never via st.write / st.markdown directly
  • SVG helpers return pure strings — composed, never evaluated inside f-strings
  • Every section is its own function — zero global side-effects
"""

import math
import streamlit as st

# ──────────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="HIRELYZER — Intelligent Career Platform",
    page_icon="⬡",
    layout="wide",
)

APP_URL = "https://hirelyzer-career-based-saas-platform-rxzkspoyrtwfamm5ztkmcf.streamlit.app/"

# ──────────────────────────────────────────────────────────────
# PRIMITIVES
# ──────────────────────────────────────────────────────────────
def h(markup: str) -> None:
    """Render raw HTML — only ever called from section functions."""
    st.markdown(markup, unsafe_allow_html=True)


def style(css: str) -> None:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# SVG FACTORIES  (pure string, no side-effects)
# ──────────────────────────────────────────────────────────────
def svg_ats_ring(score: int = 78) -> str:
    r, cx, cy, sw = 38, 48, 48, 5
    circ = 2 * math.pi * r
    fill = (score / 100) * circ
    offset = circ * 0.25
    return (
        '<svg width="96" height="96" viewBox="0 0 96 96" fill="none">'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="rgba(255,255,255,0.06)" stroke-width="{sw}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="url(#atsGrad)" stroke-width="{sw}"'
        f' stroke-dasharray="{fill:.1f} {circ:.1f}" stroke-dashoffset="-{offset:.1f}"'
        f' stroke-linecap="round" style="transition:stroke-dasharray 1.4s cubic-bezier(.4,0,.2,1)"/>'
        '<defs><linearGradient id="atsGrad" x1="0" y1="0" x2="96" y2="96" gradientUnits="userSpaceOnUse">'
        '<stop offset="0%" stop-color="#30d158"/>'
        '<stop offset="100%" stop-color="#0a84ff"/>'
        '</linearGradient></defs>'
        f'<text x="{cx}" y="{cy+1}" text-anchor="middle" dominant-baseline="middle"'
        f' fill="#f5f5f7" font-size="18" font-weight="800" font-family="Sora,sans-serif">{score}</text>'
        '</svg>'
    )


def svg_radar(
    cats: list[str] | None = None,
    scores: list[float] | None = None,
    size: int = 190,
) -> str:
    if cats is None:
        cats = ["Communication", "Technical", "Confidence", "Structure", "Examples"]
    if scores is None:
        scores = [0.82, 0.74, 0.88, 0.70, 0.78]
    cx = cy = size // 2
    R = cx - 28
    n = len(cats)

    def pt(i: int, frac: float) -> tuple[float, float]:
        angle = math.pi / 2 + 2 * math.pi * i / n
        return cx + R * frac * math.cos(angle), cy - R * frac * math.sin(angle)

    grid_lines = "".join(
        '<polygon points="'
        + " ".join(f"{pt(i, lv)[0]:.1f},{pt(i, lv)[1]:.1f}" for i in range(n))
        + '" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
        for lv in [0.25, 0.5, 0.75, 1.0]
    )
    axes = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{pt(i,1)[0]:.1f}" y2="{pt(i,1)[1]:.1f}"'
        ' stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
        for i in range(n)
    )
    poly = " ".join(f"{pt(i, scores[i])[0]:.1f},{pt(i, scores[i])[1]:.1f}" for i in range(n))
    dots = "".join(
        f'<circle cx="{pt(i, scores[i])[0]:.1f}" cy="{pt(i, scores[i])[1]:.1f}"'
        ' r="3.5" fill="#0a84ff"/>'
        for i in range(n)
    )
    labels = "".join(
        f'<text x="{pt(i,1.28)[0]:.1f}" y="{pt(i,1.28)[1]:.1f}"'
        ' text-anchor="middle" dominant-baseline="middle"'
        ' fill="rgba(245,245,247,0.45)" font-size="8.5"'
        f' font-family="Sora,sans-serif" font-weight="500">{cats[i]}</text>'
        for i in range(n)
    )
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" fill="none">'
        f'{grid_lines}{axes}'
        f'<polygon points="{poly}" fill="rgba(10,132,255,0.14)" stroke="#0a84ff" stroke-width="1.5"/>'
        f'{dots}{labels}'
        "</svg>"
    )


def svg_check() -> str:
    return (
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none">'
        '<path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2"'
        ' stroke-linecap="round" stroke-linejoin="round"/>'
        "</svg>"
    )


# ──────────────────────────────────────────────────────────────
# HTML FRAGMENT BUILDERS  (return str, no side-effects)
# ──────────────────────────────────────────────────────────────
def build_ats_bars() -> str:
    bars = [
        ("Format & Layout",   92, "#30d158"),
        ("Keyword Coverage",  71, "#ff9f0a"),
        ("Sections Present",  85, "#0a84ff"),
        ("Action Verbs",      68, "#ff9f0a"),
        ("Contact Info",     100, "#30d158"),
        ("Date Consistency",  80, "#0a84ff"),
    ]
    parts = []
    for label, pct, col in bars:
        parts.append(
            f'<div class="bar-item">'
            f'<div class="bar-label"><span>{label}</span>'
            f'<span style="color:{col};font-weight:600">{pct}%</span></div>'
            f'<div class="bar-track">'
            f'<div class="bar-fill" style="width:{pct}%;background:{col}"></div>'
            f"</div></div>"
        )
    return "".join(parts)


def build_score_bars() -> str:
    dims = [
        ("Communication", "85%", "#0a84ff"),
        ("Technical",     "79%", "#bf5af2"),
        ("Confidence",    "88%", "#30d158"),
        ("Structure",     "74%", "#ff9f0a"),
    ]
    parts = []
    for dim, sc, col in dims:
        parts.append(
            f'<div style="display:flex;justify-content:space-between;'
            f'font-size:11px;color:var(--m);margin-bottom:5px">'
            f"<span>{dim}</span>"
            f'<span style="color:{col};font-weight:600">{sc}</span></div>'
            f'<div style="height:3px;background:rgba(255,255,255,0.07);'
            f'border-radius:2px;margin-bottom:9px;overflow:hidden">'
            f'<div style="width:{sc};height:100%;background:{col};border-radius:2px"></div>'
            f"</div>"
        )
    return "".join(parts)


def build_template_gallery() -> str:
    templates = [
        ("Modern",     "#0a84ff"),
        ("Minimal",    "#f5f5f7"),
        ("Executive",  "#ff9f0a"),
        ("Timeline",   "#30d158"),
        ("Corporate",  "#1d4ed8"),
        ("Creative",   "#bf5af2"),
        ("Navy",       "#172554"),
        ("Teal",       "#0d9488"),
    ]
    parts = []
    for i, (name, col) in enumerate(templates):
        active_cls = "tmpl-active" if i == 0 else ""
        badge = (
            f'<div class="tmpl-badge">{name}</div>' if i == 0 else ""
        )
        parts.append(
            f'<div class="tmpl-thumb {active_cls}">'
            f'<div class="tmpl-hdr" style="background:{col};opacity:.9"></div>'
            f'<div class="tmpl-ln w90"></div>'
            f'<div class="tmpl-ln w60"></div>'
            f'<div class="tmpl-ln w75"></div>'
            f'<div class="tmpl-ln w85"></div>'
            f'<div class="tmpl-ln w55"></div>'
            f"{badge}"
            f"</div>"
        )
    return "".join(parts)


def build_job_cards() -> str:
    jobs = [
        ("SDE II",       "Google",   "Mountain View · Full-time", "#4285f4", "G", True),
        ("ML Engineer",  "Anthropic","Remote · Full-time",        "#d97706", "A", False),
        ("Backend Dev",  "Razorpay", "Bangalore · Full-time",     "#2563eb", "R", False),
        ("Data Analyst", "Zepto",    "Mumbai · Hybrid",           "#7c3aed", "Z", False),
    ]
    parts = []
    for title, co, meta, col, letter, featured in jobs:
        bb  = "rgba(10,132,255,0.12)"      if featured else "rgba(255,255,255,0.05)"
        bc  = "#4db3ff"                     if featured else "rgba(245,245,247,0.3)"
        btx = "Featured"                    if featured else "New"
        parts.append(
            f'<div class="job-card">'
            f'<div class="job-logo" style="background:{col}22;color:{col}">{letter}</div>'
            f'<div class="job-meta">'
            f'<div class="job-title">{title} — {co}</div>'
            f'<div class="job-co">{meta}</div>'
            f"</div>"
            f'<div class="job-badge" style="background:{bb};color:{bc};border:1px solid {bc}40">{btx}</div>'
            f"</div>"
        )
    return "".join(parts)


def build_checklist() -> str:
    items = [
        "ATS score in seconds",
        "Bias detection & rewrite",
        "15 resume templates",
        "Cover letter generator",
        "Live job search",
        "AI Interview Coach",
    ]
    chk = svg_check()
    return "".join(
        f'<div class="check-item">{chk}<span>{item}</span></div>'
        for item in items
    )


def build_pills(labels: list[str]) -> str:
    return "".join(f'<span class="pill">{lbl}</span>' for lbl in labels)


# ──────────────────────────────────────────────────────────────
# CSS  (injected once, at the top)
# ──────────────────────────────────────────────────────────────
def inject_css() -> None:
    style("""
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ── TOKENS ─────────────────────────────────────── */
:root {
  --bg:    #000;
  --bg1:   #080808;
  --bg2:   #0f0f10;
  --bg3:   #141416;
  --surf:  #1a1a1e;
  --b:     rgba(255,255,255,0.07);
  --b2:    rgba(255,255,255,0.13);
  --t:     #f5f5f7;
  --m:     rgba(245,245,247,0.54);
  --m2:    rgba(245,245,247,0.34);
  --a:     #0a84ff;
  --ag:    #30d158;
  --aw:    #ff9f0a;
  --ap:    #bf5af2;
  --ar:    #ff453a;
  --font:  'Sora', -apple-system, 'SF Pro Display', sans-serif;
  --mono:  'JetBrains Mono', monospace;
  --r:     20px;
  --r-sm:  12px;
  --ease:  cubic-bezier(.4,0,.2,1);
}

/* ── RESET ───────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[class*="css"] {
  background: var(--bg) !important;
  color: var(--t);
  font-family: var(--font);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* hide ALL streamlit chrome */
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
[data-testid="stStatusWidget"],
footer,
#MainMenu { display: none !important; }

[data-testid="stAppViewContainer"] > section { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── SCROLL PROGRESS ─────────────────────────────── */
#sp {
  position: fixed; top: 0; left: 0; height: 2px; width: 0;
  background: linear-gradient(90deg, var(--a), var(--ag));
  z-index: 9999; transition: width .06s linear;
}

/* ── NAV ─────────────────────────────────────────── */
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 900;
  height: 58px; display: flex; align-items: center; justify-content: center;
  backdrop-filter: saturate(200%) blur(28px);
  -webkit-backdrop-filter: saturate(200%) blur(28px);
  background: rgba(0,0,0,0.76);
  border-bottom: 1px solid var(--b);
}
.nav-inner {
  width: 100%; max-width: 1120px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 36px;
}
.nav-logo {
  display: flex; align-items: center; gap: 10px;
  font-size: 14px; font-weight: 800; color: var(--t);
  text-decoration: none; letter-spacing: .6px;
}
.nav-mark {
  width: 32px; height: 32px;
  background: var(--a); border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
}
.nav-links { display: flex; align-items: center; gap: 30px; }
.nav-links a {
  font-size: 13px; font-weight: 500; color: var(--m);
  text-decoration: none; transition: color .2s var(--ease);
  letter-spacing: -.1px;
}
.nav-links a:hover { color: var(--t); }
.nav-cta {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 8px 20px; border-radius: 980px;
  background: var(--a); color: #fff;
  font-size: 13px; font-weight: 600; text-decoration: none;
  transition: opacity .2s, transform .15s var(--ease);
  letter-spacing: -.1px;
}
.nav-cta:hover { opacity: .84; transform: scale(.97); }

/* ── HERO ─────────────────────────────────────────── */
.hero {
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center;
  padding: 130px 36px 90px;
  position: relative; overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute; top: -180px; left: 50%;
  transform: translateX(-50%);
  width: 900px; height: 700px;
  background: radial-gradient(ellipse, rgba(10,132,255,.11) 0%, transparent 68%);
  pointer-events: none;
}
.hero::after {
  content: '';
  position: absolute; bottom: 0; left: 0; right: 0; height: 220px;
  background: linear-gradient(to bottom, transparent, #000);
  pointer-events: none;
}

/* ── EYEBROW ─────────────────────────────────────── */
.eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 10.5px; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase; color: var(--a);
  padding: 6px 16px; border-radius: 980px;
  border: 1px solid rgba(10,132,255,.28);
  background: rgba(10,132,255,.06);
  margin-bottom: 30px;
  animation: fadeUp .65s var(--ease) both;
}

/* ── H1 ──────────────────────────────────────────── */
.h1 {
  font-size: clamp(44px, 7.5vw, 88px);
  font-weight: 800; line-height: 1.02; letter-spacing: -3.5px;
  color: var(--t); max-width: 940px;
  animation: fadeUp .65s .1s var(--ease) both;
}
.h1 em { font-style: normal; color: var(--a); }
.h1 .hl-g { color: var(--ag); }

/* ── HERO SUB ────────────────────────────────────── */
.hero-sub {
  font-size: clamp(15px, 1.9vw, 19px);
  color: var(--m); line-height: 1.65; letter-spacing: -.2px;
  max-width: 560px; margin: 26px auto 0;
  animation: fadeUp .65s .2s var(--ease) both;
}

/* ── CTA BUTTONS ─────────────────────────────────── */
.ctas {
  display: flex; gap: 14px; justify-content: center;
  margin-top: 46px; flex-wrap: wrap;
  animation: fadeUp .65s .3s var(--ease) both;
}
.btn-p {
  display: inline-flex; align-items: center; gap: 9px;
  padding: 14px 30px; border-radius: 980px;
  background: var(--a); color: #fff;
  font-size: 15px; font-weight: 600; text-decoration: none;
  letter-spacing: -.2px;
  transition: opacity .2s, transform .15s var(--ease), box-shadow .2s;
  box-shadow: 0 0 0 0 rgba(10,132,255,.4);
}
.btn-p:hover {
  opacity: .88; transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(10,132,255,.35);
}
.btn-g {
  display: inline-flex; align-items: center; gap: 9px;
  padding: 14px 30px; border-radius: 980px;
  background: var(--surf); color: var(--t);
  font-size: 15px; font-weight: 600; text-decoration: none;
  letter-spacing: -.2px; border: 1px solid var(--b2);
  transition: background .2s, transform .15s var(--ease);
}
.btn-g:hover { background: #242428; transform: translateY(-2px); }

/* ── HERO DASHBOARD CARD ─────────────────────────── */
.hero-card {
  margin-top: 74px; width: 100%; max-width: 860px;
  background: var(--bg2); border-radius: 24px;
  border: 1px solid var(--b); overflow: hidden;
  box-shadow: 0 50px 120px rgba(0,0,0,.7);
  position: relative; z-index: 1;
  animation: fadeUp .65s .44s var(--ease) both;
}
.card-bar {
  height: 40px; background: var(--bg3);
  border-bottom: 1px solid var(--b);
  display: flex; align-items: center; padding: 0 18px; gap: 8px;
}
.dot { width: 12px; height: 12px; border-radius: 50%; }
.card-tab {
  margin-left: 8px; font-size: 11px; color: var(--m2);
  font-family: var(--mono);
}
.card-body { padding: 28px; }

/* ── STAT ROW ────────────────────────────────────── */
.stat-row {
  display: flex; gap: 12px; flex-wrap: wrap; justify-content: center;
  margin: 30px 0 0;
  animation: fadeUp .65s .55s var(--ease) both;
}
.stat {
  display: flex; flex-direction: column; align-items: center;
  padding: 18px 30px; border-radius: 18px;
  background: var(--bg2); border: 1px solid var(--b); min-width: 130px;
  transition: border-color .2s, transform .2s var(--ease);
}
.stat:hover { border-color: var(--b2); transform: translateY(-2px); }
.stat-n {
  font-size: 26px; font-weight: 800; color: var(--t);
  letter-spacing: -1px;
}
.stat-l {
  font-size: 10.5px; color: var(--m2); font-weight: 600;
  margin-top: 4px; text-transform: uppercase; letter-spacing: .9px;
}

/* ── SECTION WRAPPER ─────────────────────────────── */
.section { max-width: 1120px; margin: 0 auto; padding: 0 36px; }

/* ── SECTION DIVIDER ─────────────────────────────── */
.sec-div {
  font-size: 10.5px; font-weight: 700; letter-spacing: 1.5px;
  text-transform: uppercase; color: var(--m2);
  display: flex; align-items: center; gap: 18px;
  margin-bottom: 72px;
}
.sec-div::before, .sec-div::after {
  content: ''; flex: 1; height: 1px; background: var(--b);
}

/* ── HOW IT WORKS STEPS ──────────────────────────── */
.steps {
  display: grid; grid-template-columns: repeat(4,1fr); gap: 2px;
}
.step {
  padding: 34px 26px; background: var(--bg2);
  border: 1px solid var(--b); position: relative; overflow: hidden;
  transition: background .2s;
}
.step:hover { background: var(--bg3); }
.step:first-child  { border-radius: 22px 0 0 22px; }
.step:last-child   { border-radius: 0 22px 22px 0; }
.step-n {
  font-family: var(--mono); font-size: 10.5px; font-weight: 600;
  color: var(--m2); margin-bottom: 18px; display: block; letter-spacing: .5px;
}
.step-icon { width: 46px; height: 46px; margin-bottom: 18px; }
.step-title {
  font-size: 14.5px; font-weight: 700; color: var(--t);
  margin-bottom: 10px; letter-spacing: -.3px;
}
.step-desc { font-size: 13px; color: var(--m); line-height: 1.68; }
.step-glow {
  position: absolute; bottom: -40px; right: -40px;
  width: 120px; height: 120px; border-radius: 50%;
  opacity: .06; filter: blur(30px);
}

/* ── STORY SECTIONS ──────────────────────────────── */
.story { padding: 100px 0; }
.story-alt { padding: 100px 0; background: var(--bg1); }
.story-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 84px; align-items: center;
}
.story-num {
  font-family: var(--mono); font-size: 10.5px; font-weight: 600;
  color: var(--m2); letter-spacing: 1px; margin-bottom: 20px;
}
.story-h {
  font-size: clamp(28px, 3.8vw, 46px); font-weight: 800;
  letter-spacing: -1.8px; line-height: 1.08; color: var(--t);
  margin-bottom: 22px;
}
.story-h span { color: var(--a); }
.story-h .g   { color: var(--ag); }
.story-h .w   { color: var(--aw); }
.story-h .p   { color: var(--ap); }
.story-p {
  font-size: 15.5px; color: var(--m); line-height: 1.78;
  font-weight: 400; margin-bottom: 18px;
}
.pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
.pill {
  padding: 6px 14px; border-radius: 980px; font-size: 11.5px; font-weight: 600;
  border: 1px solid var(--b2); color: var(--m); background: var(--bg2);
  transition: border-color .2s, color .2s;
}
.pill:hover { border-color: var(--a); color: var(--a); }

/* ── PANEL ───────────────────────────────────────── */
.panel {
  background: var(--bg2); border-radius: 22px;
  border: 1px solid var(--b); padding: 26px; overflow: hidden; position: relative;
}
.panel::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse at 80% 0%, rgba(10,132,255,.04) 0%, transparent 60%);
  pointer-events: none;
}
.panel-title {
  font-size: 10.5px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1.1px; color: var(--m2);
  display: flex; align-items: center; gap: 8px;
  margin-bottom: 20px;
}

/* ── ATS BARS ────────────────────────────────────── */
.bar-item { margin-bottom: 11px; }
.bar-label {
  display: flex; justify-content: space-between;
  font-size: 11.5px; color: var(--m); margin-bottom: 5px; font-weight: 500;
}
.bar-track {
  height: 4px; background: rgba(255,255,255,0.06);
  border-radius: 2px; overflow: hidden;
}
.bar-fill {
  height: 100%; border-radius: 2px;
  transition: width 1.4s cubic-bezier(.4,0,.2,1);
}

/* ── WORD CHIPS ──────────────────────────────────── */
.word-row { display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 14px; }
.wc {
  padding: 5px 12px; border-radius: 8px;
  font-size: 11.5px; font-weight: 600; font-family: var(--mono);
}
.wc-m { background: rgba(10,132,255,.11);  color: #4db3ff; border: 1px solid rgba(10,132,255,.2); }
.wc-f { background: rgba(191,90,242,.11);  color: #d07ef7; border: 1px solid rgba(191,90,242,.2); }
.wc-n { background: rgba(48,209,88,.11);   color: #4cd964; border: 1px solid rgba(48,209,88,.2); }

/* ── TEMPLATE GALLERY ───────────────────────────── */
.tmpl-grid {
  display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 16px;
}
.tmpl-thumb {
  border-radius: 10px; border: 1px solid var(--b); overflow: hidden;
  background: var(--bg3); padding: 10px;
  display: flex; flex-direction: column; gap: 5px; min-height: 92px;
  position: relative; transition: border-color .2s;
}
.tmpl-thumb:hover { border-color: var(--b2); }
.tmpl-active { border-color: var(--a) !important; box-shadow: 0 0 0 2px rgba(10,132,255,.2); }
.tmpl-hdr { height: 5px; border-radius: 2px; }
.tmpl-ln { height: 3px; border-radius: 1.5px; background: var(--b2); }
.w90 { width: 90%; }  .w85 { width: 85%; }  .w75 { width: 75%; }
.w60 { width: 60%; }  .w55 { width: 55%; }
.tmpl-badge {
  position: absolute; bottom: 6px; left: 6px; right: 6px;
  background: rgba(10,132,255,.15); border: 1px solid rgba(10,132,255,.25);
  border-radius: 5px; padding: 3px 6px;
  font-size: 9px; font-weight: 700; color: var(--a);
  text-align: center; letter-spacing: .6px; text-transform: uppercase;
}

/* ── JOB CARDS ───────────────────────────────────── */
.job-card {
  padding: 13px 16px; border-radius: 14px;
  background: var(--bg3); border: 1px solid var(--b);
  display: flex; align-items: center; gap: 12px; margin-bottom: 8px;
  transition: border-color .2s, transform .2s var(--ease);
}
.job-card:hover { border-color: var(--b2); transform: translateX(3px); }
.job-logo {
  width: 36px; height: 36px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 13px; flex-shrink: 0; font-family: var(--mono);
}
.job-meta { flex: 1; min-width: 0; }
.job-title {
  font-size: 13px; font-weight: 600; color: var(--t);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.job-co { font-size: 11px; color: var(--m2); margin-top: 2px; }
.job-badge {
  padding: 3px 10px; border-radius: 980px;
  font-size: 11px; font-weight: 600; white-space: nowrap;
}

/* ── RADAR WRAPPER ───────────────────────────────── */
.radar-wrap {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
}

/* ── Q&A ─────────────────────────────────────────── */
.qa { margin-bottom: 16px; }
.q {
  font-size: 13px; font-weight: 600; color: var(--t);
  margin-bottom: 8px; display: flex; gap: 9px; align-items: flex-start;
}
.a { font-size: 12px; color: var(--m); line-height: 1.65; padding-left: 24px; }
.score-badge {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 5px 13px; border-radius: 980px; font-size: 12px; font-weight: 700;
  background: rgba(48,209,88,.12); color: var(--ag);
  border: 1px solid rgba(48,209,88,.22);
}

/* ── CTA BLOCK ───────────────────────────────────── */
.cta-block {
  margin: 0 0 120px;
  padding: 90px 52px; border-radius: 30px;
  background: var(--bg2); border: 1px solid var(--b);
  text-align: center; position: relative; overflow: hidden;
}
.cta-block::before {
  content: ''; position: absolute; top: -320px; left: 50%;
  transform: translateX(-50%); width: 700px; height: 700px;
  background: radial-gradient(ellipse, rgba(10,132,255,.09) 0%, transparent 68%);
  pointer-events: none;
}
.cta-block::after {
  content: ''; position: absolute; bottom: -200px; right: -100px;
  width: 400px; height: 400px;
  background: radial-gradient(ellipse, rgba(48,209,88,.05) 0%, transparent 70%);
  pointer-events: none;
}
.cta-h {
  font-size: clamp(30px, 4.8vw, 56px); font-weight: 800;
  letter-spacing: -2.5px; color: var(--t); line-height: 1.06;
  max-width: 680px; margin: 0 auto 22px; position: relative; z-index: 1;
}
.cta-sub {
  font-size: 17px; color: var(--m);
  margin-bottom: 42px; position: relative; z-index: 1;
}
.check-row {
  display: flex; justify-content: center;
  gap: 30px; flex-wrap: wrap; margin-top: 38px;
}
.check-item {
  display: flex; align-items: center;
  gap: 8px; font-size: 13px; color: var(--m2);
}

/* ── FOOTER ──────────────────────────────────────── */
.footer-inner {
  border-top: 1px solid var(--b); padding: 42px 36px;
  display: flex; justify-content: space-between; align-items: center;
  max-width: 1120px; margin: 0 auto; flex-wrap: wrap; gap: 20px;
}
.footer-copy { font-size: 13px; font-weight: 600; color: var(--m2); }
.footer-links { display: flex; gap: 26px; }
.footer-links a {
  font-size: 13px; color: var(--m2); text-decoration: none;
  transition: color .2s var(--ease);
}
.footer-links a:hover { color: var(--t); }

/* ── SCROLL REVEAL ───────────────────────────────── */
.reveal {
  opacity: 0; transform: translateY(28px);
  transition: opacity .7s var(--ease), transform .7s var(--ease);
}
.reveal.visible { opacity: 1; transform: none; }

/* ── ANIMATIONS ──────────────────────────────────── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(26px); }
  to   { opacity: 1; transform: none; }
}
@keyframes pulse {
  0%,100% { opacity: 1; }
  50%      { opacity: .5; }
}

/* ── RESPONSIVE ──────────────────────────────────── */
@media (max-width: 860px) {
  .story-grid { grid-template-columns: 1fr; gap: 44px; }
  .steps { grid-template-columns: 1fr 1fr; }
  .step:first-child  { border-radius: 22px 0 0 0; }
  .step:nth-child(2) { border-radius: 0 22px 0 0; }
  .step:nth-child(3) { border-radius: 0 0 0 22px; }
  .step:last-child   { border-radius: 0 0 22px 0; }
  .ctas { flex-direction: column; align-items: center; }
  .nav-links { display: none; }
  .cta-block { padding: 52px 28px; }
  .hero-card .card-body { padding: 18px; }
}
""")


# ──────────────────────────────────────────────────────────────
# JS  (injected once)
# ──────────────────────────────────────────────────────────────
def inject_js() -> None:
    h("""
<script>
(function () {
  /* ── scroll progress bar ── */
  var sp = document.getElementById('sp');
  function updateSP() {
    if (!sp) return;
    var pct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    sp.style.width = Math.min(pct, 100) + '%';
  }
  window.addEventListener('scroll', updateSP, { passive: true });

  /* ── scroll reveal ── */
  var revealEls = [];
  function collectReveal() { revealEls = Array.from(document.querySelectorAll('.reveal')); }
  function checkReveal() {
    var vh = window.innerHeight;
    revealEls.forEach(function (el) {
      if (el.getBoundingClientRect().top < vh * 0.92) el.classList.add('visible');
    });
  }
  function init() { collectReveal(); checkReveal(); }

  /* ── retry because Streamlit injects DOM asynchronously ── */
  var attempts = 0;
  var timer = setInterval(function () {
    init();
    attempts++;
    if (attempts > 20) clearInterval(timer);
  }, 300);

  window.addEventListener('scroll', checkReveal, { passive: true });
})();
</script>
""")


# ──────────────────────────────────────────────────────────────
# SECTION RENDERERS
# ──────────────────────────────────────────────────────────────
def render_nav() -> None:
    h(f"""
<div id="sp"></div>
<div class="nav">
  <div class="nav-inner">
    <a href="#" class="nav-logo">
      <div class="nav-mark">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
          <path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5"
            stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      HIRELYZER
    </a>
    <div class="nav-links">
      <a href="#how">How it works</a>
      <a href="#analyzer">Analyzer</a>
      <a href="#builder">Builder</a>
      <a href="#career">Career Hub</a>
      <a href="#contact">Contact</a>
    </div>
    <a href="{APP_URL}" target="_blank" class="nav-cta">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="#fff">
        <path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/>
      </svg>
      Open App
    </a>
  </div>
</div>
""")


def render_hero() -> None:
    ring = svg_ats_ring(78)
    ats_bars = build_ats_bars()
    h(f"""
<div class="hero">
  <div class="eyebrow">
    <svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>
    AI-Powered Career Intelligence
  </div>

  <h1 class="h1">The last resume tool<br>you&rsquo;ll ever <em>need</em></h1>

  <p class="hero-sub">
    Upload your resume. Hirelyzer instantly scores it for ATS compatibility,
    detects bias, rewrites with AI, and connects you to jobs &mdash; all in one place.
  </p>

  <div class="ctas">
    <a href="{APP_URL}" target="_blank" class="btn-p">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff">
        <path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/>
      </svg>
      Get Started Free
    </a>
    <a href="#how" class="btn-g">
      See how it works
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
        <path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8"
          stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </a>
  </div>

  <!-- ── DASHBOARD CARD ── -->
  <div class="hero-card">
    <div class="card-bar">
      <div class="dot" style="background:#ff5f57"></div>
      <div class="dot" style="background:#febc2e"></div>
      <div class="dot" style="background:#28c840"></div>
      <span class="card-tab">hirelyzer &mdash; resume_analysis.pdf</span>
    </div>
    <div class="card-body">
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px">

        <!-- ATS SCORE -->
        <div>
          <div class="panel-title">
            <svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#30d158"/></svg>
            ATS Score
          </div>
          <div style="display:flex;align-items:center;gap:16px;margin-bottom:20px">
            {ring}
            <div>
              <div style="font-size:9.5px;color:var(--m2);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:4px">Overall</div>
              <div style="font-size:11px;color:#30d158;font-weight:600;margin-top:2px">Good &middot; Minor fixes</div>
            </div>
          </div>
          {ats_bars}
        </div>

        <!-- BIAS ANALYSIS -->
        <div>
          <div class="panel-title">
            <svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#bf5af2"/></svg>
            Bias Analysis
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:14px">
            <div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:4px">Masculine</div>
              <div style="font-size:22px;font-weight:800;color:#4db3ff">8</div>
              <div style="font-size:10px;color:var(--m2)">flagged</div>
            </div>
            <div style="padding:12px;background:rgba(191,90,242,0.06);border-radius:10px;border:1px solid rgba(191,90,242,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:4px">Feminine</div>
              <div style="font-size:22px;font-weight:800;color:#d07ef7">3</div>
              <div style="font-size:10px;color:var(--m2)">flagged</div>
            </div>
          </div>
          <div class="word-row">
            <span class="wc wc-m">driven</span>
            <span class="wc wc-m">dominate</span>
            <span class="wc wc-f">nurture</span>
            <span class="wc wc-m">aggressive</span>
            <span class="wc wc-n">deliver</span>
            <span class="wc wc-n">execute</span>
          </div>
          <div style="padding:10px 12px;background:rgba(48,209,88,0.06);border-radius:10px;border:1px solid rgba(48,209,88,0.18)">
            <div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:4px">AI Rewrite Applied</div>
            <div style="font-size:11px;color:var(--m);line-height:1.6">
              <span style="text-decoration:line-through;opacity:.4">Aggressively drove</span>
              &rarr; <span style="color:#30d158">Accelerated</span> delivery across 3 teams
            </div>
          </div>
        </div>

        <!-- QUICK ACTIONS -->
        <div>
          <div class="panel-title">
            <svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#ff9f0a"/></svg>
            Quick Actions
          </div>
          <div style="display:flex;flex-direction:column;gap:8px">
            <div style="padding:9px 12px;background:rgba(48,209,88,0.07);border-radius:9px;border:1px solid rgba(48,209,88,0.18);display:flex;align-items:center;gap:8px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span style="font-size:12px;color:#30d158;font-weight:600">Single-column layout</span>
            </div>
            <div style="padding:9px 12px;background:rgba(48,209,88,0.07);border-radius:9px;border:1px solid rgba(48,209,88,0.18);display:flex;align-items:center;gap:8px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span style="font-size:12px;color:#30d158;font-weight:600">Contact info present</span>
            </div>
            <div style="padding:9px 12px;background:rgba(255,159,10,0.07);border-radius:9px;border:1px solid rgba(255,159,10,0.18);display:flex;align-items:center;gap:8px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>
              <span style="font-size:12px;color:#ff9f0a;font-weight:600">Add LinkedIn URL</span>
            </div>
            <div style="padding:9px 12px;background:rgba(255,69,58,0.07);border-radius:9px;border:1px solid rgba(255,69,58,0.18);display:flex;align-items:center;gap:8px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2" stroke-linecap="round"/></svg>
              <span style="font-size:12px;color:#ff453a;font-weight:600">No skills section</span>
            </div>
            <div style="padding:9px 12px;background:rgba(255,69,58,0.07);border-radius:9px;border:1px solid rgba(255,69,58,0.18);display:flex;align-items:center;gap:8px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2" stroke-linecap="round"/></svg>
              <span style="font-size:12px;color:#ff453a;font-weight:600">Objective section outdated</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- STATS -->
  <div class="stat-row">
    <div class="stat"><div class="stat-n">15+</div><div class="stat-l">Templates</div></div>
    <div class="stat"><div class="stat-n">5</div><div class="stat-l">Core Modules</div></div>
    <div class="stat"><div class="stat-n">AI</div><div class="stat-l">LLM Powered</div></div>
    <div class="stat"><div class="stat-n">Free</div><div class="stat-l">No Credit Card</div></div>
  </div>
</div>
""")


def render_how_it_works() -> None:
    h("""
<div id="how" style="padding:100px 0 60px">
  <div class="section reveal">
    <div class="sec-div">How it works</div>
    <div class="steps">

      <div class="step">
        <div class="step-glow" style="background:#0a84ff"></div>
        <span class="step-n">01</span>
        <svg class="step-icon" viewBox="0 0 46 46" fill="none">
          <rect width="46" height="46" rx="13" fill="rgba(10,132,255,0.1)"/>
          <path d="M23 29V21M23 21L20 24M23 21L26 24" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M16 31h14" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round"/>
          <rect x="15" y="13" width="16" height="20" rx="3" stroke="#0a84ff" stroke-width="1.4" stroke-dasharray="3 2" fill="none"/>
        </svg>
        <div class="step-title">Upload your resume</div>
        <div class="step-desc">Drop any PDF. Our parser handles messy formats, multi-column layouts, and scanned documents via OCR fallback.</div>
      </div>

      <div class="step">
        <div class="step-glow" style="background:#30d158"></div>
        <span class="step-n">02</span>
        <svg class="step-icon" viewBox="0 0 46 46" fill="none">
          <rect width="46" height="46" rx="13" fill="rgba(48,209,88,0.1)"/>
          <circle cx="21" cy="21" r="7" stroke="#30d158" stroke-width="1.5" fill="none"/>
          <path d="M21 18v3l2 1.5" stroke="#30d158" stroke-width="1.5" stroke-linecap="round"/>
          <path d="M26.2 26.2l3.5 3.5" stroke="#30d158" stroke-width="1.7" stroke-linecap="round"/>
        </svg>
        <div class="step-title">Instant AI analysis</div>
        <div class="step-desc">ATS scoring, bias detection, grammar check, keyword matching — all computed in seconds with detailed feedback.</div>
      </div>

      <div class="step">
        <div class="step-glow" style="background:#bf5af2"></div>
        <span class="step-n">03</span>
        <svg class="step-icon" viewBox="0 0 46 46" fill="none">
          <rect width="46" height="46" rx="13" fill="rgba(191,90,242,0.1)"/>
          <rect x="12" y="11" width="13" height="18" rx="2.5" stroke="#bf5af2" stroke-width="1.5" fill="none"/>
          <rect x="20" y="16" width="14" height="18" rx="2.5" fill="rgba(191,90,242,0.08)" stroke="#bf5af2" stroke-width="1.5"/>
          <path d="M23 21h8M23 24.5h8M23 28h5" stroke="#bf5af2" stroke-width="1.3" stroke-linecap="round"/>
          <circle cx="33" cy="13" r="4" fill="#bf5af2"/>
          <path d="M31.5 13l1 1 2-2" stroke="#fff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div class="step-title">Build or rewrite</div>
        <div class="step-desc">Use the AI rewriter or open the full Resume Builder. Choose from 15 templates, generate a cover letter, export to PDF or DOCX.</div>
      </div>

      <div class="step">
        <div class="step-glow" style="background:#ff9f0a"></div>
        <span class="step-n">04</span>
        <svg class="step-icon" viewBox="0 0 46 46" fill="none">
          <rect width="46" height="46" rx="13" fill="rgba(255,159,10,0.1)"/>
          <path d="M23 29c-3.31 0-6-2.69-6-6 0-4 3-8 6-9 3 1 6 5 6 9 0 3.31-2.69 6-6 6z" stroke="#ff9f0a" stroke-width="1.5" fill="none"/>
          <circle cx="23" cy="23" r="2" fill="#ff9f0a"/>
          <path d="M30 14l-2 2M16 14l2 2" stroke="#ff9f0a" stroke-width="1.4" stroke-linecap="round"/>
        </svg>
        <div class="step-title">Apply with confidence</div>
        <div class="step-desc">Discover live job listings, salary benchmarks, curated courses, and practice with the AI Interview Coach before applying.</div>
      </div>

    </div>
  </div>
</div>
""")


def render_story_ats_analyzer() -> None:
    ats_bars = build_ats_bars()
    ring = svg_ats_ring(78)
    h(f"""
<div id="analyzer" class="story">
  <div class="section">
    <div class="story-grid">
      <div class="reveal">
        <div class="story-num">Feature 01 &mdash; Resume Analyzer</div>
        <h2 class="story-h">Your resume, <span>scored like a machine</span> reads it</h2>
        <p class="story-p">
          Most resumes never reach a human. Applicant Tracking Systems silently filter them
          on format, missing keywords, or structural issues. Hirelyzer&rsquo;s analyzer
          replicates how ATS parsers actually read your document &mdash; not just a surface
          keyword match.
        </p>
        <p class="story-p">
          You get a score across six dimensions, a prioritised fix list, grammar and
          readability signals, and a full keyword-gap report mapped to the roles you care about.
        </p>
        <div class="pills">
          {build_pills(["ATS Score", "6-Dimension Breakdown", "Keyword Gap", "Grammar Check", "Downloadable Report"])}
        </div>
      </div>
      <div class="reveal">
        <div class="panel">
          <div class="panel-title">
            <svg width="12" height="12" viewBox="0 0 12 12"><circle cx="6" cy="6" r="6" fill="#30d158"/></svg>
            ATS Analysis Report
          </div>
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:24px">
            {ring}
            <div>
              <div style="font-size:9.5px;color:var(--m2);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:4px">Overall Score</div>
              <div style="font-size:11px;color:#30d158;font-weight:600">Good &middot; Minor fixes needed</div>
              <div style="font-size:10px;color:var(--m2);margin-top:4px">Parsed in 1.4 s</div>
            </div>
          </div>
          {ats_bars}
        </div>
      </div>
    </div>
  </div>
</div>
""")


def render_story_bias() -> None:
    h("""
<div class="story-alt">
  <div class="section">
    <div class="story-grid">
      <div class="reveal" style="order:2">
        <div class="story-num">Feature 02 &mdash; Bias Detection</div>
        <h2 class="story-h">Bias-free language that <span class="p">opens every door</span></h2>
        <p class="story-p">
          Gender-coded words can unconsciously signal culture fit to recruiters &mdash;
          research shows resumes with neutral language receive significantly more callbacks.
          Hirelyzer scans every verb, adjective, and phrase against a curated bias lexicon.
        </p>
        <p class="story-p">
          The AI rewriter suggests impact-neutral alternatives, preserving your
          achievements while broadening appeal across hiring contexts.
        </p>
        <div class="pills">
          <span class="pill">Gender-coded Detection</span>
          <span class="pill">AI Neutral Rewrite</span>
          <span class="pill">Lexicon of 400+ Words</span>
          <span class="pill">One-click Apply</span>
        </div>
      </div>
      <div class="reveal" style="order:1">
        <div class="panel">
          <div class="panel-title">
            <svg width="12" height="12" viewBox="0 0 12 12"><circle cx="6" cy="6" r="6" fill="#bf5af2"/></svg>
            Bias Analysis Report
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:18px">
            <div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:6px">Masculine</div>
              <div style="font-size:26px;font-weight:800;color:#4db3ff">8</div>
              <div style="font-size:11px;color:var(--m2)">words flagged</div>
            </div>
            <div style="padding:14px;background:rgba(191,90,242,0.06);border-radius:12px;border:1px solid rgba(191,90,242,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:6px">Feminine</div>
              <div style="font-size:26px;font-weight:800;color:#d07ef7">3</div>
              <div style="font-size:11px;color:var(--m2)">words flagged</div>
            </div>
          </div>
          <div style="font-size:10px;color:var(--m2);font-weight:700;text-transform:uppercase;letter-spacing:.9px;margin-bottom:10px">Detected language</div>
          <div class="word-row">
            <span class="wc wc-m">driven</span>
            <span class="wc wc-m">aggressive</span>
            <span class="wc wc-m">dominate</span>
            <span class="wc wc-m">champion</span>
            <span class="wc wc-m">spearhead</span>
            <span class="wc wc-f">nurture</span>
            <span class="wc wc-f">support</span>
            <span class="wc wc-f">help</span>
            <span class="wc wc-n">deliver</span>
            <span class="wc wc-n">execute</span>
          </div>
          <div style="padding:14px;background:rgba(48,209,88,0.06);border-radius:12px;border:1px solid rgba(48,209,88,0.18)">
            <div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:6px">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" style="vertical-align:middle;margin-right:4px">
                <path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              AI Rewrite Applied
            </div>
            <div style="font-size:12px;color:var(--m);line-height:1.65">
              <span style="text-decoration:line-through;opacity:.45">Aggressively drove growth</span>
              &rarr; <span style="color:#30d158">Accelerated high-impact results</span> across 3 teams
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")


def render_story_builder() -> None:
    tmpl = build_template_gallery()
    h(f"""
<div id="builder" class="story">
  <div class="section">
    <div class="story-grid">
      <div class="reveal">
        <div class="story-num">Feature 03 &mdash; Resume Builder</div>
        <h2 class="story-h">Build resumes that <span class="g">look as good</span> as they parse</h2>
        <p class="story-p">
          Fifteen ATS-optimised templates &mdash; from understated minimal to executive prestige &mdash;
          all built on strict single-column structures that parse correctly in every major
          hiring platform. Choose a style, fill your details, and our AI enhances every
          section with no-repetition language rules enforced across the entire document.
        </p>
        <p class="story-p">
          Export to DOCX (three ATS compliance levels) or PDF. Need a cover letter?
          One click generates a tailored letter for your target company, formatted and ready to send.
        </p>
        <div class="pills">
          {build_pills(["15 Templates", "DOCX + PDF Export", "AI Cover Letter", "Live Preview", "ATS Single-Column"])}
        </div>
      </div>
      <div class="reveal">
        <div class="panel">
          <div class="panel-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
              <rect x="3" y="3" width="10" height="14" rx="2" stroke="#30d158" stroke-width="1.5"/>
              <rect x="11" y="7" width="10" height="14" rx="2" fill="rgba(48,209,88,.08)" stroke="#30d158" stroke-width="1.5"/>
              <path d="M14 11h5M14 14h5M14 17h3" stroke="#30d158" stroke-width="1.3" stroke-linecap="round"/>
            </svg>
            Template Gallery &mdash; 15 Designs
          </div>
          <div class="tmpl-grid">
            {tmpl}
          </div>
          <div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.18);display:flex;align-items:center;justify-content:space-between">
            <div>
              <div style="font-size:12px;font-weight:700;color:var(--a)">Modern &mdash; ATS Certified</div>
              <div style="font-size:11px;color:var(--m2);margin-top:2px">Sora &middot; Navy headings &middot; Single-column</div>
            </div>
            <a href="{APP_URL}" target="_blank" style="padding:8px 18px;background:var(--a);color:#fff;border-radius:980px;font-size:12px;font-weight:600;text-decoration:none;white-space:nowrap;flex-shrink:0">Use this</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")


def render_story_career() -> None:
    cards = build_job_cards()
    h(f"""
<div id="career" class="story-alt">
  <div class="section">
    <div class="story-grid">
      <div class="reveal" style="order:2">
        <div class="story-num">Feature 04 &mdash; Career Intelligence</div>
        <h2 class="story-h">Jobs, salaries, courses &mdash; <span class="w">one place</span></h2>
        <p class="story-p">
          The Job Search Hub pulls live listings from LinkedIn, Naukri, Foundit, and Indeed &mdash;
          or uses the JSearch/RapidAPI engine for direct listings with remote and employment-type
          filters. Every search is role-aware and location-smart.
        </p>
        <p class="story-p">
          Alongside jobs, Hirelyzer surfaces salary benchmarks by role and market,
          curated course recommendations mapped to real skill gaps in your resume,
          and interview preparation videos &mdash; all linked to your career profile.
        </p>
        <div class="pills">
          {build_pills(["Live Job Listings", "Salary Benchmarks", "Course Recommendations", "Skills Radar", "Remote Filter"])}
        </div>
      </div>
      <div class="reveal" style="order:1">
        <div class="panel">
          <div class="panel-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
              <rect x="2" y="7" width="20" height="14" rx="2" stroke="#ff9f0a" stroke-width="1.5"/>
              <path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="#ff9f0a" stroke-width="1.5"/>
              <path d="M2 13h20" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/>
            </svg>
            Job Search Hub
          </div>
          {cards}
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px">
            <div style="padding:12px;background:rgba(255,159,10,0.06);border-radius:10px;border:1px solid rgba(255,159,10,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:5px">Avg Salary</div>
              <div style="font-size:20px;font-weight:800;color:#ff9f0a">&#8377;18&ndash;32 LPA</div>
              <div style="font-size:11px;color:var(--m2)">Backend &middot; India</div>
            </div>
            <div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:5px">Platforms</div>
              <div style="font-size:13px;font-weight:700;color:var(--t);line-height:1.7">LinkedIn &middot; Naukri<br>Foundit &middot; Indeed</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")


def render_story_interview() -> None:
    score_bars = build_score_bars()
    radar = svg_radar()
    h(f"""
<div class="story">
  <div class="section">
    <div class="story-grid">
      <div class="reveal">
        <div class="story-num">Feature 05 &mdash; AI Interview Coach</div>
        <h2 class="story-h">Practice until <span>every answer</span> lands</h2>
        <p class="story-p">
          Upload your resume and Hirelyzer generates interview questions derived directly
          from your actual experience &mdash; not generic prompts. Answer in free text;
          the AI coach scores you on communication, technical depth, confidence signals,
          structure, and use of concrete examples.
        </p>
        <p class="story-p">
          Every session ends with a performance radar chart, a detailed Q&amp;A review,
          and course recommendations tied to your weakest dimensions. Your progress
          is tracked across sessions in the My Progress dashboard.
        </p>
        <div class="pills">
          {build_pills(["Resume-based Questions", "Real-time AI Scoring", "Radar Chart", "Session History", "Downloadable Report"])}
        </div>
      </div>
      <div class="reveal">
        <div class="panel">
          <div class="panel-title" style="justify-content:space-between">
            <div style="display:flex;align-items:center;gap:8px">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
                <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"
                  stroke="#ff453a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
              </svg>
              Mock Interview &middot; Session 3
            </div>
            <div class="score-badge">
              <svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg>
              82 / 100
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
            <div>
              <div class="qa">
                <div class="q">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px">
                    <circle cx="12" cy="12" r="10" stroke="#0a84ff" stroke-width="1.5"/>
                    <path d="M12 16v-4M12 8h.01" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round"/>
                  </svg>
                  Describe your most complex backend system.
                </div>
                <div class="a">Built a multi-tenant microservices platform handling 2M events/day using Kafka, Redis, and PostgreSQL with 40% lower P99 latency.</div>
              </div>
              <div class="qa">
                <div class="q">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px">
                    <circle cx="12" cy="12" r="10" stroke="#bf5af2" stroke-width="1.5"/>
                    <path d="M12 16v-4M12 8h.01" stroke="#bf5af2" stroke-width="1.8" stroke-linecap="round"/>
                  </svg>
                  How do you handle technical debt?
                </div>
                <div class="a">I prioritise tech debt as a first-class roadmap item, quantifying velocity cost before pitching refactors to stakeholders.</div>
              </div>
              <div style="margin-top:14px">
                <div style="font-size:10px;text-transform:uppercase;letter-spacing:.9px;color:var(--m2);font-weight:700;margin-bottom:10px">Score breakdown</div>
                {score_bars}
              </div>
            </div>
            <div class="radar-wrap">
              {radar}
              <div style="font-size:11px;color:var(--m2);margin-top:8px;text-align:center;letter-spacing:.3px">Performance radar</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")


def render_cta() -> None:
    checklist = build_checklist()
    h(f"""
<div class="section">
  <div id="contact" class="cta-block reveal">
    <div class="eyebrow" style="margin:0 auto 30px">
      <svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>
      Free to use &middot; No credit card required
    </div>
    <div class="cta-h">Your next job starts with a better resume</div>
    <p class="cta-sub">
      Join professionals already using Hirelyzer to pass ATS filters,
      remove bias, and land more interviews.
    </p>
    <div style="display:flex;gap:14px;justify-content:center;position:relative;z-index:1;flex-wrap:wrap">
      <a href="{APP_URL}" target="_blank" class="btn-p" style="font-size:16px;padding:16px 38px">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff">
          <path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/>
        </svg>
        Start for free
      </a>
      <a href="mailto:support@hirelyzer.com" class="btn-g" style="font-size:16px;padding:16px 34px">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
            stroke="currentColor" stroke-width="1.5" fill="none"/>
          <polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" fill="none"/>
        </svg>
        Contact us
      </a>
    </div>
    <div class="check-row">
      {checklist}
    </div>
  </div>
</div>
""")


def render_footer() -> None:
    h(f"""
<footer>
  <div class="footer-inner">
    <div class="footer-copy">&copy; 2025 HIRELYZER &middot; Intelligent Career Platform</div>
    <div class="footer-links">
      <a href="#">Privacy</a>
      <a href="#">Terms</a>
      <a href="mailto:support@hirelyzer.com">support@hirelyzer.com</a>
      <a href="{APP_URL}" target="_blank">Open App &rarr;</a>
    </div>
  </div>
</footer>
""")


# ──────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────
def main() -> None:
    inject_css()

    render_nav()
    render_hero()
    render_how_it_works()
    render_story_ats_analyzer()
    render_story_bias()
    render_story_builder()
    render_story_career()
    render_story_interview()
    render_cta()
    render_footer()

    inject_js()   # always last — DOM must exist before querying


if __name__ == "__main__":
    main()
