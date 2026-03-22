import math
import streamlit as st

st.set_page_config(
    page_title="HIRELYZER — Intelligent Career Platform",
    page_icon="⬡",
    layout="wide",
)

APP_URL = "https://hirelyzer-career-based-saas-platform-rxzkspoyrtwfamm5ztkmcf.streamlit.app/"

def H(s): st.markdown(s, unsafe_allow_html=True)
def CSS(s): st.markdown("<style>" + s + "</style>", unsafe_allow_html=True)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
CSS("""
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --black:     #000000;
  --surface:   #0a0a0b;
  --surface2:  #111113;
  --surface3:  #18181c;
  --border:    rgba(255,255,255,0.06);
  --border2:   rgba(255,255,255,0.12);
  --text:      #f0f0f2;
  --muted:     rgba(240,240,242,0.40);
  --muted2:    rgba(240,240,242,0.22);
  --blue:      #0a84ff;
  --blue-glow: rgba(10,132,255,0.18);
  --green:     #30d158;
  --amber:     #ff9f0a;
  --purp:      #bf5af2;
  --red:       #ff453a;
  --cyan:      #64d2ff;
  --font:      'Sora', sans-serif;
  --mono:      'JetBrains Mono', monospace;
  --serif:     'Instrument Serif', serif;
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section[data-testid="stMain"] {
  background: var(--black) !important;
  color: var(--text) !important;
  font-family: var(--font) !important;
  overflow-x: hidden !important;
  -webkit-font-smoothing: antialiased !important;
  scroll-behavior: smooth !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
[data-testid="stStatusWidget"],
footer, #MainMenu { display: none !important; }

section[data-testid="stAppViewContainer"] > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stMarkdownContainer"] > p { margin: 0 !important; }

/* ── Scroll progress ── */
#sp {
  position: fixed; top: 0; left: 0; height: 2px; width: 0%;
  background: linear-gradient(90deg, var(--blue), var(--green), var(--cyan));
  z-index: 9999; transition: width 0.08s linear; pointer-events: none;
}

/* ══════════════════════════════════════════
   NAV
══════════════════════════════════════════ */
.hl-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 900;
  height: 60px; display: flex; align-items: center; justify-content: center;
  background: rgba(0,0,0,0.76);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(28px) saturate(180%);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  transition: background 0.3s;
}
.hl-nav-inner {
  width: 100%; max-width: 1160px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 36px;
}
.hl-logo {
  display: flex; align-items: center; gap: 11px;
  font-size: 13px; font-weight: 800; color: var(--text);
  text-decoration: none; letter-spacing: 0.8px;
}
.hl-logo-icon {
  width: 34px; height: 34px; border-radius: 10px;
  background: linear-gradient(135deg, #0a84ff, #006ad6);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  box-shadow: 0 0 20px rgba(10,132,255,0.35);
}
.hl-nav-links { display: flex; align-items: center; gap: 30px; }
.hl-nav-links a {
  font-size: 12.5px; font-weight: 500;
  color: var(--muted); text-decoration: none;
  transition: color 0.2s; letter-spacing: 0.2px;
}
.hl-nav-links a:hover { color: var(--text); }
.hl-nav-cta {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 9px 22px; border-radius: 100px;
  background: var(--blue); color: #fff;
  font-size: 12.5px; font-weight: 700; text-decoration: none;
  box-shadow: 0 4px 20px rgba(10,132,255,0.30);
  transition: transform 0.2s, box-shadow 0.2s;
  letter-spacing: 0.1px;
}
.hl-nav-cta:hover { transform: translateY(-1px); box-shadow: 0 6px 28px rgba(10,132,255,0.45); }

/* ══════════════════════════════════════════
   HERO
══════════════════════════════════════════ */
.hl-hero {
  min-height: 100vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 140px 32px 100px;
  position: relative; overflow: hidden; background: #000;
}
#hero-canvas {
  position: absolute; inset: 0; pointer-events: none; z-index: 0;
}
.hl-hero-mesh {
  position: absolute; top: -30%; left: 50%; transform: translateX(-50%);
  width: 120%; height: 80%;
  background: radial-gradient(ellipse 60% 50% at 50% 20%, rgba(10,132,255,0.10) 0%, transparent 70%),
              radial-gradient(ellipse 40% 40% at 20% 80%, rgba(191,90,242,0.06) 0%, transparent 60%),
              radial-gradient(ellipse 40% 40% at 80% 70%, rgba(48,209,88,0.05) 0%, transparent 60%);
  pointer-events: none; z-index: 0;
}
.hl-hero-grid {
  position: absolute; inset: 0; pointer-events: none; z-index: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse 80% 60% at 50% 40%, black 0%, transparent 75%);
  -webkit-mask-image: radial-gradient(ellipse 80% 60% at 50% 40%, black 0%, transparent 75%);
}
.hl-hero-fade {
  position: absolute; bottom: 0; left: 0; right: 0; height: 300px;
  background: linear-gradient(to bottom, transparent, #000);
  pointer-events: none; z-index: 1;
}
.hl-hero-content {
  position: relative; z-index: 2;
  width: 100%; display: flex; flex-direction: column; align-items: center;
}

.hl-eyebrow {
  display: inline-flex; align-items: center; gap: 9px;
  font-size: 10px; font-weight: 700; letter-spacing: 1.8px; text-transform: uppercase;
  color: var(--blue); padding: 7px 18px; border-radius: 100px;
  border: 1px solid rgba(10,132,255,0.25);
  background: rgba(10,132,255,0.07);
  margin-bottom: 30px;
  animation: heroFadeUp 0.7s ease both;
}

.hl-h1 {
  font-size: clamp(48px, 8vw, 96px);
  font-weight: 900; line-height: 1.00;
  letter-spacing: -4px; color: var(--text);
  max-width: 980px;
  animation: heroFadeUp 0.7s 0.1s ease both;
}
.hl-h1 em { font-style: italic; font-family: var(--serif); font-weight: 400; color: var(--blue); letter-spacing: -2px; }

.hl-hero-sub {
  font-size: clamp(15px, 2vw, 20px);
  color: var(--muted); line-height: 1.70;
  max-width: 580px; margin: 28px auto 0;
  animation: heroFadeUp 0.7s 0.2s ease both;
  font-weight: 300;
}

.hl-ctas {
  display: flex; gap: 14px; justify-content: center; margin-top: 48px;
  flex-wrap: wrap; animation: heroFadeUp 0.7s 0.3s ease both;
}
.hl-btn-p {
  display: inline-flex; align-items: center; gap: 9px;
  padding: 15px 32px; border-radius: 100px;
  background: var(--blue); color: #fff;
  font-size: 15px; font-weight: 700; text-decoration: none;
  box-shadow: 0 8px 32px rgba(10,132,255,0.35);
  transition: transform 0.2s, box-shadow 0.2s;
  letter-spacing: -0.2px;
}
.hl-btn-p:hover { transform: translateY(-2px); box-shadow: 0 14px 40px rgba(10,132,255,0.50); }
.hl-btn-g {
  display: inline-flex; align-items: center; gap: 9px;
  padding: 15px 32px; border-radius: 100px;
  background: rgba(255,255,255,0.05); color: var(--text);
  font-size: 15px; font-weight: 600; text-decoration: none;
  border: 1px solid var(--border2);
  transition: background 0.2s, border-color 0.2s;
}
.hl-btn-g:hover { background: rgba(255,255,255,0.09); border-color: rgba(255,255,255,0.22); }

/* Stats row */
.hl-stats {
  display: flex; gap: 14px; flex-wrap: wrap; justify-content: center;
  margin: 56px 0 0; animation: heroFadeUp 0.7s 0.5s ease both;
}
.hl-stat {
  display: flex; flex-direction: column; align-items: center;
  padding: 20px 32px; border-radius: 20px;
  background: var(--surface); border: 1px solid var(--border);
  min-width: 136px; position: relative; overflow: hidden;
}
.hl-stat::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(10,132,255,0.5), transparent);
}
.hl-stat-n { font-size: 28px; font-weight: 900; color: var(--text); letter-spacing: -1.5px; }
.hl-stat-l { font-size: 10px; color: var(--muted); font-weight: 600; margin-top: 5px; text-transform: uppercase; letter-spacing: 1px; }

/* Hero demo card */
.hl-demo-card {
  margin-top: 80px; width: 100%; max-width: 900px;
  background: var(--surface); border-radius: 24px;
  border: 1px solid var(--border); overflow: hidden;
  box-shadow: 0 60px 120px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.04) inset;
  animation: heroFadeUp 0.8s 0.5s ease both;
}
.hl-card-bar {
  height: 44px; background: var(--surface2);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 18px; gap: 8px;
}
.hl-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
.hl-card-tab {
  margin-left: 6px; font-size: 11px;
  color: var(--muted); font-family: var(--mono);
}
.hl-card-body { padding: 28px; }
.hl-card-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; }

/* ══════════════════════════════════════════
   SHARED SECTION
══════════════════════════════════════════ */
.hl-section { max-width: 1160px; margin: 0 auto; padding: 0 36px; }
.hl-panel {
  background: var(--surface); border-radius: 22px;
  border: 1px solid var(--border); padding: 26px;
  overflow: hidden; position: relative;
}
.hl-panel::after {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.10), transparent);
}
.hl-ptitle {
  font-size: 9.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.3px;
  color: var(--muted); display: flex; align-items: center; gap: 8px; margin-bottom: 20px;
}
.hl-bar { margin-bottom: 11px; }
.hl-bar-row {
  display: flex; justify-content: space-between; font-size: 11px;
  color: var(--muted); margin-bottom: 5px; font-weight: 500;
}
.hl-bar-track {
  height: 4px; background: rgba(255,255,255,0.05); border-radius: 2px; overflow: hidden;
}
.hl-bar-fill { height: 100%; border-radius: 2px; transition: width 1.2s cubic-bezier(0.22,1,0.36,1); }

/* ══════════════════════════════════════════
   HOW IT WORKS
══════════════════════════════════════════ */
.hl-how { padding: 120px 0 80px; background: #000; }
.hl-divider {
  font-size: 9.5px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
  color: var(--muted); display: flex; align-items: center; gap: 20px; margin-bottom: 72px;
}
.hl-divider::before, .hl-divider::after {
  content: ''; flex: 1; height: 1px; background: var(--border);
}
.hl-steps { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; }
.hl-step {
  padding: 36px 26px; background: var(--surface);
  border: 1px solid var(--border); position: relative; overflow: hidden;
  transition: background 0.3s;
}
.hl-step:hover { background: var(--surface2); }
.hl-step:first-child { border-radius: 22px 0 0 22px; }
.hl-step:last-child  { border-radius: 0 22px 22px 0; }
.hl-step-n {
  font-family: var(--mono); font-size: 10px; font-weight: 700;
  color: var(--muted2); margin-bottom: 20px; display: block; letter-spacing: 1px;
}
.hl-step-icon { width: 48px; height: 48px; margin-bottom: 20px; }
.hl-step-title { font-size: 14px; font-weight: 700; color: var(--text); margin-bottom: 10px; letter-spacing: -0.3px; }
.hl-step-desc  { font-size: 13px; color: var(--muted); line-height: 1.70; font-weight: 300; }
.hl-step-connector {
  position: absolute; right: -1px; top: 50%; transform: translateY(-50%);
  width: 18px; height: 18px; background: var(--surface3);
  border: 1px solid var(--border); border-radius: 50%;
  display: flex; align-items: center; justify-content: center; z-index: 2;
}

/* ══════════════════════════════════════════
   FEATURE STORIES
══════════════════════════════════════════ */
.hl-story     { padding: 110px 0; background: #000; }
.hl-story-alt { padding: 110px 0; background: #050505; }
.hl-story-grid {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 96px; align-items: center;
}
.hl-story-num {
  font-family: var(--mono); font-size: 10px; font-weight: 700;
  color: var(--muted2); letter-spacing: 1.2px; margin-bottom: 20px;
  display: flex; align-items: center; gap: 10px;
}
.hl-story-num::before {
  content: ''; width: 24px; height: 1px; background: var(--muted2);
}
.hl-story-h {
  font-size: clamp(30px, 4vw, 48px); font-weight: 900;
  letter-spacing: -2px; line-height: 1.05; color: var(--text); margin-bottom: 22px;
}
.hl-story-h .hl-blue  { color: var(--blue); }
.hl-story-h .hl-green { color: var(--green); }
.hl-story-h .hl-amber { color: var(--amber); }
.hl-story-h .hl-purp  { color: var(--purp); }
.hl-story-h em { font-style: italic; font-family: var(--serif); font-weight: 400; }
.hl-story-p {
  font-size: 15px; color: var(--muted); line-height: 1.82; margin-bottom: 18px; font-weight: 300;
}

/* pills */
.hl-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
.hl-pill {
  padding: 6px 14px; border-radius: 100px;
  font-size: 11px; font-weight: 600; letter-spacing: 0.2px;
  border: 1px solid var(--border2); color: var(--muted);
  background: var(--surface); transition: color 0.2s, border-color 0.2s;
}
.hl-pill:hover { color: var(--text); border-color: rgba(255,255,255,0.24); }

/* word chips */
.hl-words { display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 14px; }
.wc {
  padding: 5px 12px; border-radius: 8px;
  font-size: 11px; font-weight: 600; font-family: var(--mono);
}
.wc-m { background: rgba(10,132,255,0.10);  color: #5ab8ff; border: 1px solid rgba(10,132,255,0.22); }
.wc-f { background: rgba(191,90,242,0.10);  color: #d088f8; border: 1px solid rgba(191,90,242,0.22); }
.wc-n { background: rgba(48,209,88,0.10);   color: #4dd96a; border: 1px solid rgba(48,209,88,0.22); }

/* job cards */
.hl-job {
  padding: 14px 16px; border-radius: 14px;
  background: var(--surface2); border: 1px solid var(--border);
  display: flex; align-items: center; gap: 13px; margin-bottom: 9px;
  transition: border-color 0.2s, background 0.2s;
}
.hl-job:hover { background: var(--surface3); border-color: var(--border2); }
.hl-job-logo {
  width: 38px; height: 38px; border-radius: 11px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 13px; flex-shrink: 0; font-family: var(--mono);
}
.hl-job-title { font-size: 13px; font-weight: 600; color: var(--text); }
.hl-job-co    { font-size: 11px; color: var(--muted); margin-top: 2px; }
.hl-job-badge {
  padding: 4px 11px; border-radius: 100px;
  font-size: 10.5px; font-weight: 700; white-space: nowrap; flex-shrink: 0;
  letter-spacing: 0.3px;
}

/* templates */
.hl-tmpl-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 16px; }
.hl-tmpl {
  border-radius: 12px; border: 1px solid var(--border);
  background: var(--surface2); padding: 11px;
  display: flex; flex-direction: column; gap: 6px;
  min-height: 94px; position: relative; cursor: pointer;
  transition: border-color 0.2s, transform 0.2s;
}
.hl-tmpl:hover { border-color: var(--border2); transform: translateY(-2px); }
.hl-tmpl-act { border-color: var(--blue) !important; box-shadow: 0 0 0 2px rgba(10,132,255,0.20); }
.hl-tmpl-hdr { height: 5px; border-radius: 3px; }
.hl-tmpl-ln  { height: 3px; border-radius: 2px; background: rgba(255,255,255,0.10); }
.hl-tmpl-badge {
  position: absolute; bottom: 7px; left: 7px; right: 7px;
  background: rgba(10,132,255,0.14); border: 1px solid rgba(10,132,255,0.28);
  border-radius: 6px; padding: 3px 7px;
  font-size: 9px; font-weight: 700; color: var(--blue);
  text-align: center; letter-spacing: 0.6px; text-transform: uppercase;
}

/* interview */
.hl-qa { margin-bottom: 16px; }
.hl-q {
  font-size: 13px; font-weight: 600; color: var(--text);
  margin-bottom: 8px; display: flex; gap: 9px; align-items: flex-start; line-height: 1.5;
}
.hl-a {
  font-size: 12px; color: var(--muted); line-height: 1.70;
  padding-left: 23px; font-weight: 300;
}
.hl-score-badge {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 6px 14px; border-radius: 100px; font-size: 12px; font-weight: 700;
  background: rgba(48,209,88,0.10); color: var(--green);
  border: 1px solid rgba(48,209,88,0.24);
}
.hl-radar-wrap { display: flex; flex-direction: column; align-items: center; }

/* ══════════════════════════════════════════
   METRICS MARQUEE
══════════════════════════════════════════ */
.hl-marquee-wrap {
  overflow: hidden; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
  padding: 22px 0; background: var(--surface);
}
.hl-marquee-track {
  display: flex; gap: 48px; white-space: nowrap;
  animation: marquee 28s linear infinite;
}
.hl-marquee-item {
  display: inline-flex; align-items: center; gap: 12px;
  font-size: 13px; font-weight: 600; color: var(--muted); flex-shrink: 0;
}
.hl-marquee-dot { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }

@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}

/* ══════════════════════════════════════════
   TESTIMONIALS
══════════════════════════════════════════ */
.hl-testis { padding: 100px 0; background: #000; }
.hl-testi-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 18px; margin-top: 56px; }
.hl-testi {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 20px; padding: 28px;
  transition: border-color 0.3s, transform 0.3s;
  position: relative; overflow: hidden;
}
.hl-testi::before {
  content: '\201C'; position: absolute; top: 18px; right: 22px;
  font-size: 72px; font-family: var(--serif); color: rgba(255,255,255,0.04);
  line-height: 1; pointer-events: none;
}
.hl-testi:hover { border-color: var(--border2); transform: translateY(-3px); }
.hl-testi-stars { display: flex; gap: 3px; margin-bottom: 16px; }
.hl-testi-text { font-size: 14px; color: var(--muted); line-height: 1.78; font-weight: 300; margin-bottom: 22px; }
.hl-testi-author { display: flex; align-items: center; gap: 12px; }
.hl-testi-avatar {
  width: 38px; height: 38px; border-radius: 50%;
  font-size: 14px; font-weight: 800; display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.hl-testi-name { font-size: 13px; font-weight: 700; color: var(--text); }
.hl-testi-role { font-size: 11px; color: var(--muted); margin-top: 2px; }

/* ══════════════════════════════════════════
   FEATURE TABS
══════════════════════════════════════════ */
.hl-ftabs { padding: 100px 0; background: #050505; }
.hl-ftab-nav {
  display: flex; gap: 4px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 16px; padding: 5px; width: fit-content; margin: 0 auto 48px;
}
.hl-ftab-btn {
  padding: 10px 22px; border-radius: 12px; cursor: pointer;
  font-size: 13px; font-weight: 600; letter-spacing: -0.2px;
  color: var(--muted); background: transparent; border: none;
  transition: all 0.22s; white-space: nowrap;
}
.hl-ftab-btn.active {
  background: var(--surface3); color: var(--text);
  box-shadow: 0 1px 4px rgba(0,0,0,0.4);
}

/* ══════════════════════════════════════════
   CTA
══════════════════════════════════════════ */
.hl-cta-wrap { padding: 0 36px 120px; }
.hl-cta {
  padding: 90px 56px; border-radius: 32px;
  background: var(--surface); border: 1px solid var(--border);
  text-align: center; position: relative; overflow: hidden;
  background-image:
    radial-gradient(ellipse 60% 50% at 50% -10%, rgba(10,132,255,0.10) 0%, transparent 70%);
}
.hl-cta::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(10,132,255,0.5), transparent);
}
.hl-cta-h {
  font-size: clamp(30px, 5vw, 56px); font-weight: 900;
  letter-spacing: -2.5px; color: var(--text); line-height: 1.04;
  max-width: 680px; margin: 0 auto 22px; position: relative; z-index: 1;
}
.hl-cta-h em { font-style: italic; font-family: var(--serif); color: var(--blue); }
.hl-cta-sub {
  font-size: 16px; color: var(--muted); margin-bottom: 42px;
  position: relative; z-index: 1; font-weight: 300; line-height: 1.65;
}
.hl-cta-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }
.hl-checks {
  display: flex; justify-content: center; gap: 28px;
  flex-wrap: wrap; margin-top: 40px; position: relative; z-index: 1;
}
.hl-check {
  display: flex; align-items: center; gap: 8px;
  font-size: 13px; color: var(--muted); font-weight: 400;
}

/* ══════════════════════════════════════════
   FOOTER
══════════════════════════════════════════ */
.hl-footer-wrap { background: #000; border-top: 1px solid var(--border); }
.hl-footer {
  padding: 44px 36px; display: flex; justify-content: space-between;
  align-items: center; max-width: 1160px; margin: 0 auto; flex-wrap: wrap; gap: 20px;
}
.hl-footer-copy { font-size: 13px; font-weight: 500; color: var(--muted2); }
.hl-footer-links { display: flex; gap: 26px; flex-wrap: wrap; }
.hl-footer-links a {
  font-size: 13px; color: var(--muted); text-decoration: none;
  transition: color 0.2s;
}
.hl-footer-links a:hover { color: var(--text); }

/* ══════════════════════════════════════════
   ANIMATIONS
══════════════════════════════════════════ */
@keyframes heroFadeUp {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: none; }
}
@keyframes countUp {
  from { opacity: 0; transform: scale(0.8); }
  to   { opacity: 1; transform: scale(1); }
}
@keyframes scanline {
  0%   { top: -4px; }
  100% { top: 100%; }
}

/* Scroll-reveal */
.sr { opacity: 0; transform: translateY(32px); transition: opacity 0.7s ease, transform 0.7s ease; }
.sr.visible { opacity: 1; transform: none; }
.sr-d1 { transition-delay: 0.10s; }
.sr-d2 { transition-delay: 0.20s; }
.sr-d3 { transition-delay: 0.30s; }
.sr-d4 { transition-delay: 0.40s; }

/* ══════════════════════════════════════════
   MEDIA
══════════════════════════════════════════ */
@media (max-width: 900px) {
  .hl-story-grid { grid-template-columns: 1fr; gap: 48px; }
  .hl-steps { grid-template-columns: 1fr 1fr; }
  .hl-step:first-child  { border-radius: 22px 0 0 0; }
  .hl-step:nth-child(2) { border-radius: 0 22px 0 0; }
  .hl-step:nth-child(3) { border-radius: 0 0 0 22px; }
  .hl-step:last-child   { border-radius: 0 0 22px 0; }
  .hl-ctas { flex-direction: column; align-items: center; }
  .hl-nav-links { display: none; }
  .hl-cta { padding: 52px 28px; }
  .hl-card-grid { grid-template-columns: 1fr; }
  .hl-testi-grid { grid-template-columns: 1fr; }
  .hl-ftab-nav { flex-wrap: wrap; justify-content: center; width: 100%; }
}
""")

# ─── SVG / FRAGMENT HELPERS ───────────────────────────────────────────────────
def ats_ring(score=78):
    r, c, sw = 38, 48, 5
    circ = 2 * math.pi * r
    fill = (score / 100) * circ
    off  = circ * 0.25
    return (
        '<svg width="96" height="96" viewBox="0 0 96 96" fill="none">'
        '<circle cx="{c}" cy="{c}" r="{r}" stroke="rgba(255,255,255,0.06)" stroke-width="{sw}"/>'
        '<circle cx="{c}" cy="{c}" r="{r}" stroke="url(#ag{s})" stroke-width="{sw}"'
        ' stroke-dasharray="{f} {ci}" stroke-dashoffset="-{o}" stroke-linecap="round"/>'
        '<text x="{c}" y="{c1}" text-anchor="middle" dominant-baseline="middle"'
        ' fill="#f0f0f2" font-size="19" font-weight="900" font-family="Sora,sans-serif">{s}</text>'
        '<defs><linearGradient id="ag{s}" x1="0" y1="0" x2="96" y2="96" gradientUnits="userSpaceOnUse">'
        '<stop offset="0%" stop-color="#30d158"/><stop offset="100%" stop-color="#0a84ff"/>'
        '</linearGradient></defs></svg>'
    ).format(c=c, r=r, sw=sw, f=round(fill,1), ci=round(circ,1), o=round(off,1), c1=c+1, s=score)

def radar_svg():
    cats   = ["Communication","Technical","Confidence","Structure","Examples"]
    scores = [0.82, 0.74, 0.88, 0.70, 0.78]
    cx = cy = 95; R = 65; n = len(cats)
    def pt(i, frac):
        angle = math.pi/2 + 2*math.pi*i/n
        return cx + R*frac*math.cos(angle), cy - R*frac*math.sin(angle)
    grid = ""
    for lv in [0.25, 0.5, 0.75, 1.0]:
        pts = " ".join(f"{round(pt(i,lv)[0],1)},{round(pt(i,lv)[1],1)}" for i in range(n))
        grid += f'<polygon points="{pts}" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>'
    axes = "".join(f'<line x1="{cx}" y1="{cy}" x2="{round(pt(i,1)[0],1)}" y2="{round(pt(i,1)[1],1)}" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>' for i in range(n))
    poly = " ".join(f"{round(pt(i,scores[i])[0],1)},{round(pt(i,scores[i])[1],1)}" for i in range(n))
    dots = "".join(f'<circle cx="{round(pt(i,scores[i])[0],1)}" cy="{round(pt(i,scores[i])[1],1)}" r="4" fill="#0a84ff" stroke="rgba(10,132,255,0.3)" stroke-width="4"/>' for i in range(n))
    labels = "".join(f'<text x="{round(pt(i,1.30)[0],1)}" y="{round(pt(i,1.30)[1],1)}" text-anchor="middle" dominant-baseline="middle" fill="rgba(240,240,242,0.42)" font-size="8.5" font-family="Sora,sans-serif" font-weight="500">{cats[i]}</text>' for i in range(n))
    return (f'<svg width="190" height="190" viewBox="0 0 190 190" fill="none">'
            f'<defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0%" stop-color="rgba(10,132,255,0.20)"/>'
            f'<stop offset="100%" stop-color="rgba(48,209,88,0.10)"/>'
            f'</linearGradient></defs>'
            f'{grid}{axes}'
            f'<polygon points="{poly}" fill="url(#rg)" stroke="#0a84ff" stroke-width="1.6"/>'
            f'{dots}{labels}</svg>')

def ats_bars():
    data = [
        ("Format & Layout", 92, "#30d158"),
        ("Keyword Coverage", 71, "#ff9f0a"),
        ("Sections Present", 85, "#0a84ff"),
        ("Action Verbs",     68, "#ff9f0a"),
        ("Contact Info",    100, "#30d158"),
        ("Date Consistency", 80, "#0a84ff"),
    ]
    return "".join(
        f'<div class="hl-bar">'
        f'<div class="hl-bar-row"><span>{lbl}</span><span style="color:{col};font-weight:700">{pct}%</span></div>'
        f'<div class="hl-bar-track"><div class="hl-bar-fill" style="width:{pct}%;background:{col}"></div></div>'
        f'</div>'
        for lbl, pct, col in data
    )

def score_bars():
    data = [("Communication","85%","#0a84ff"),("Technical","79%","#bf5af2"),
            ("Confidence","88%","#30d158"),("Structure","74%","#ff9f0a")]
    return "".join(
        f'<div style="display:flex;justify-content:space-between;font-size:11px;color:rgba(240,240,242,0.50);margin-bottom:6px">'
        f'<span>{d}</span><span style="color:{c};font-weight:700">{s}</span></div>'
        f'<div style="height:3px;background:rgba(255,255,255,0.06);border-radius:2px;margin-bottom:10px;overflow:hidden">'
        f'<div style="width:{s};height:100%;background:{c};border-radius:2px"></div></div>'
        for d, s, c in data
    )

def tmpl_gallery():
    templates = [("Modern","#0a84ff"),("Minimal","#e0e0e0"),("Executive","#ff9f0a"),
                 ("Timeline","#30d158"),("Corporate","#2563eb"),("Creative","#bf5af2"),
                 ("Navy","#3b82f6"),("Teal","#14b8a6")]
    widths = ["90%","60%","75%","85%","55%"]
    out = ""
    for i, (name, col) in enumerate(templates):
        act = " hl-tmpl-act" if i == 0 else ""
        badge = f'<div class="hl-tmpl-badge">{name}</div>' if i == 0 else ""
        lines = "".join(f'<div class="hl-tmpl-ln" style="width:{w}"></div>' for w in widths)
        out += f'<div class="hl-tmpl{act}"><div class="hl-tmpl-hdr" style="background:{col}"></div>{lines}{badge}</div>'
    return out

def job_cards():
    jobs = [
        ("SDE II", "Google", "Mountain View · Full-time", "#4285f4", "G", True),
        ("ML Engineer", "Anthropic", "Remote · Full-time", "#d97706", "A", False),
        ("Backend Dev", "Razorpay", "Bangalore · Full-time", "#2563eb", "R", False),
        ("Data Analyst", "Zepto", "Mumbai · Hybrid", "#7c3aed", "Z", False),
    ]
    out = ""
    for title, co, meta, col, letter, featured in jobs:
        bb  = "rgba(10,132,255,0.12)" if featured else "rgba(255,255,255,0.04)"
        bc  = "#4db3ff"               if featured else "rgba(240,240,242,0.28)"
        btx = "Featured"              if featured else "New"
        out += (f'<div class="hl-job">'
                f'<div class="hl-job-logo" style="background:{col}22;color:{col}">{letter}</div>'
                f'<div style="flex:1;min-width:0">'
                f'<div class="hl-job-title">{title} &mdash; {co}</div>'
                f'<div class="hl-job-co">{meta}</div></div>'
                f'<div class="hl-job-badge" style="background:{bb};color:{bc};border:1px solid {bc}44">{btx}</div>'
                f'</div>')
    return out

def checklist():
    items = ["ATS score in seconds","Bias detection & rewrite","15 resume templates",
             "Cover letter generator","Live job search","AI Interview Coach"]
    chk = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return "".join(f'<div class="hl-check">{chk}<span>{item}</span></div>' for item in items)

def pills(labels, color=None):
    if color:
        return "".join(f'<span class="hl-pill" style="color:{color};border-color:{color}33">{l}</span>' for l in labels)
    return "".join(f'<span class="hl-pill">{l}</span>' for l in labels)

def star():
    return '<svg width="12" height="12" viewBox="0 0 24 24" fill="#ff9f0a"><path d="M12 2L14.4 9.6H22.4L16 14.4L18.4 22L12 17.2L5.6 22L8 14.4L1.6 9.6H9.6L12 2Z"/></svg>'

# ─── SECTIONS ────────────────────────────────────────────────────────────────
def render_nav():
    H('<div id="sp"></div>'
      '<div class="hl-nav">'
      '<div class="hl-nav-inner">'
      '<a href="#" class="hl-logo">'
      '<div class="hl-logo-icon">'
      '<svg width="18" height="18" viewBox="0 0 24 24" fill="none">'
      '<path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
      '</svg></div>HIRELYZER</a>'
      '<div class="hl-nav-links">'
      '<a href="#how">How it works</a>'
      '<a href="#analyzer">Analyzer</a>'
      '<a href="#builder">Builder</a>'
      '<a href="#career">Career Hub</a>'
      '<a href="#testimonials">Reviews</a>'
      '<a href="#contact">Contact</a>'
      '</div>'
      f'<a href="{APP_URL}" target="_blank" class="hl-nav-cta">'
      '<svg width="12" height="12" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Open App</a>'
      '</div></div>')

def render_hero():
    ring = ats_ring(78)
    bars = ats_bars()
    H(f'<div class="hl-hero">'
      '<div class="hl-hero-mesh"></div>'
      '<div class="hl-hero-grid"></div>'
      '<div class="hl-hero-fade"></div>'
      '<div class="hl-hero-content">'

      '<div class="hl-eyebrow">'
      '<svg width="7" height="7" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>'
      'AI-Powered Career Intelligence &mdash; Free to Use'
      '</div>'

      '<h1 class="hl-h1">The last resume<br>tool you&rsquo;ll ever <em>need</em></h1>'

      '<p class="hl-hero-sub">Upload your resume. Hirelyzer instantly scores it for ATS compatibility, '
      'detects bias, rewrites with AI, and connects you to live jobs &mdash; all in one place.</p>'

      '<div class="hl-ctas">'
      f'<a href="{APP_URL}" target="_blank" class="hl-btn-p">'
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Get Started Free</a>'
      '<a href="#how" class="hl-btn-g">See how it works '
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '</a>'
      '</div>'

      # Demo card
      '<div class="hl-demo-card">'
      '<div class="hl-card-bar">'
      '<div class="hl-dot" style="background:#ff5f57"></div>'
      '<div class="hl-dot" style="background:#febc2e"></div>'
      '<div class="hl-dot" style="background:#28c840"></div>'
      '<span class="hl-card-tab">hirelyzer &mdash; resume_analysis.pdf &mdash; ATS Report</span>'
      '</div>'
      '<div class="hl-card-body"><div class="hl-card-grid">'

      # col 1 ATS
      '<div>'
      '<div class="hl-ptitle"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg>ATS Score</div>'
      f'<div style="display:flex;align-items:center;gap:18px;margin-bottom:20px">{ring}'
      '<div>'
      '<div style="font-size:9px;color:rgba(240,240,242,0.34);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:5px">Overall</div>'
      '<div style="font-size:12px;color:#30d158;font-weight:700">Good &middot; Minor fixes</div>'
      '</div></div>'
      + bars +
      '</div>'

      # col 2 Bias
      '<div>'
      '<div class="hl-ptitle"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#bf5af2"/></svg>Bias Analysis</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:13px">'
      '<div style="padding:12px;background:rgba(10,132,255,0.07);border-radius:12px;border:1px solid rgba(10,132,255,0.16)">'
      '<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:5px">Masculine</div>'
      '<div style="font-size:24px;font-weight:900;color:#5ab8ff;letter-spacing:-1px">8</div>'
      '<div style="font-size:10px;color:rgba(240,240,242,0.34)">flagged</div></div>'
      '<div style="padding:12px;background:rgba(191,90,242,0.07);border-radius:12px;border:1px solid rgba(191,90,242,0.16)">'
      '<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:5px">Feminine</div>'
      '<div style="font-size:24px;font-weight:900;color:#d088f8;letter-spacing:-1px">3</div>'
      '<div style="font-size:10px;color:rgba(240,240,242,0.34)">flagged</div></div>'
      '</div>'
      '<div class="hl-words">'
      '<span class="wc wc-m">driven</span><span class="wc wc-m">dominate</span>'
      '<span class="wc wc-f">nurture</span><span class="wc wc-m">aggressive</span>'
      '<span class="wc wc-n">deliver</span><span class="wc wc-n">execute</span>'
      '</div>'
      '<div style="padding:11px 13px;background:rgba(48,209,88,0.07);border-radius:12px;border:1px solid rgba(48,209,88,0.20)">'
      '<div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:5px">AI Rewrite Applied</div>'
      '<div style="font-size:12px;color:rgba(240,240,242,0.50);line-height:1.6">'
      '<span style="text-decoration:line-through;opacity:.4">Aggressively drove</span>'
      ' &rarr; <span style="color:#30d158;font-weight:600">Accelerated</span> delivery across 3 teams'
      '</div></div>'
      '</div>'

      # col 3 Actions
      '<div>'
      '<div class="hl-ptitle"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#ff9f0a"/></svg>Quick Actions</div>'
      '<div style="display:flex;flex-direction:column;gap:8px">'
      + "".join(
          f'<div style="padding:10px 13px;background:{bg};border-radius:10px;border:1px solid {bc};display:flex;align-items:center;gap:9px">{icon}<span style="font-size:12px;color:{tc};font-weight:600">{txt}</span></div>'
          for bg, bc, tc, icon, txt in [
              ("rgba(48,209,88,0.07)","rgba(48,209,88,0.20)","#30d158",
               '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
               "Single-column layout"),
              ("rgba(48,209,88,0.07)","rgba(48,209,88,0.20)","#30d158",
               '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
               "Contact info present"),
              ("rgba(255,159,10,0.07)","rgba(255,159,10,0.20)","#ff9f0a",
               '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.8" fill="none"/></svg>',
               "Add LinkedIn URL"),
              ("rgba(255,69,58,0.07)","rgba(255,69,58,0.20)","#ff453a",
               '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2.2" stroke-linecap="round"/></svg>',
               "No skills section"),
              ("rgba(255,69,58,0.07)","rgba(255,69,58,0.20)","#ff453a",
               '<svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2.2" stroke-linecap="round"/></svg>',
               "Objective section outdated"),
          ]
      ) +
      '</div></div>'
      '</div></div></div></div>'  # close card-grid, card-body, card

      # Stats
      '<div class="hl-stats">'
      + "".join(
          f'<div class="hl-stat"><div class="hl-stat-n" data-count="{raw}">{display}</div><div class="hl-stat-l">{label}</div></div>'
          for raw, display, label in [
              ("15", "15+", "Templates"),
              ("5",  "5",   "Core Modules"),
              ("400","400+","Bias Lexicon"),
              ("0",  "Free","No Credit Card"),
          ]
      ) +
      '</div>'

      '</div></div>')  # close hero-content, hero

def render_marquee():
    items = [
        ("#30d158", "ATS Scoring in < 2 seconds"),
        ("#0a84ff", "FAISS Vector Embeddings"),
        ("#ff9f0a", "Gender-Bias Detection"),
        ("#bf5af2", "15 Resume Templates"),
        ("#64d2ff", "AI Cover Letter Generator"),
        ("#30d158", "Live Job Listings"),
        ("#0a84ff", "Salary Benchmarks"),
        ("#ff9f0a", "AI Interview Coach"),
        ("#bf5af2", "Skills Radar Chart"),
        ("#64d2ff", "DOCX + PDF Export"),
        ("#30d158", "Supabase Persistence"),
        ("#0a84ff", "Groq LLM Powered"),
    ]
    # duplicate for seamless loop
    double = items * 2
    track_items = "".join(
        f'<div class="hl-marquee-item">'
        f'<div class="hl-marquee-dot" style="background:{col}"></div>'
        f'{txt}'
        f'</div>'
        for col, txt in double
    )
    H(f'<div class="hl-marquee-wrap"><div class="hl-marquee-track">{track_items}</div></div>')

def render_how():
    steps = [
        ("#0a84ff",
         '<svg class="hl-step-icon" viewBox="0 0 48 48" fill="none"><rect width="48" height="48" rx="14" fill="rgba(10,132,255,0.10)"/><path d="M24 30V20M24 20L21 23M24 20L27 23" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 32h16" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round"/><rect x="14" y="13" width="20" height="22" rx="4" stroke="#0a84ff" stroke-width="1.5" stroke-dasharray="3 2" fill="none"/></svg>',
         "Upload your resume",
         "Drop any PDF. Our parser handles messy formats, multi-column layouts, and scanned documents via OCR fallback."),
        ("#30d158",
         '<svg class="hl-step-icon" viewBox="0 0 48 48" fill="none"><rect width="48" height="48" rx="14" fill="rgba(48,209,88,0.10)"/><circle cx="22" cy="22" r="8" stroke="#30d158" stroke-width="1.6" fill="none"/><path d="M22 18v4l2.5 1.5" stroke="#30d158" stroke-width="1.6" stroke-linecap="round"/><path d="M28 28l4 4" stroke="#30d158" stroke-width="2" stroke-linecap="round"/></svg>',
         "Instant AI analysis",
         "ATS scoring, bias detection, grammar check, keyword matching — computed in seconds with dimensional feedback."),
        ("#bf5af2",
         '<svg class="hl-step-icon" viewBox="0 0 48 48" fill="none"><rect width="48" height="48" rx="14" fill="rgba(191,90,242,0.10)"/><rect x="12" y="11" width="14" height="20" rx="3" stroke="#bf5af2" stroke-width="1.5" fill="none"/><rect x="20" y="16" width="16" height="20" rx="3" fill="rgba(191,90,242,0.08)" stroke="#bf5af2" stroke-width="1.5"/><path d="M23 22h9M23 26h9M23 30h6" stroke="#bf5af2" stroke-width="1.3" stroke-linecap="round"/><circle cx="35" cy="13" r="5" fill="#bf5af2"/><path d="M33 13l1.5 1.5L37 11" stroke="#fff" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>',
         "Build or rewrite",
         "Use the AI rewriter or open the full Resume Builder. Choose from 15 templates, generate a cover letter, export to PDF or DOCX."),
        ("#ff9f0a",
         '<svg class="hl-step-icon" viewBox="0 0 48 48" fill="none"><rect width="48" height="48" rx="14" fill="rgba(255,159,10,0.10)"/><path d="M24 30c-3.86 0-7-3.14-7-7 0-4.67 3.5-9.33 7-10.5 3.5 1.17 7 5.83 7 10.5 0 3.86-3.14 7-7 7z" stroke="#ff9f0a" stroke-width="1.6" fill="none"/><circle cx="24" cy="23" r="2.5" fill="#ff9f0a"/><path d="M32 14l-2.5 2.5M16 14l2.5 2.5" stroke="#ff9f0a" stroke-width="1.5" stroke-linecap="round"/></svg>',
         "Apply with confidence",
         "Discover live job listings, salary benchmarks, curated courses, and practice with the AI Interview Coach."),
    ]
    step_html = ""
    for i, (col, icon, title, desc) in enumerate(steps):
        connector = '<div class="hl-step-connector"><svg width="8" height="8" viewBox="0 0 8 8" fill="none"><path d="M2 4h4M4 2l2 2-2 2" stroke="rgba(240,240,242,0.3)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>' if i < 3 else ""
        step_html += (f'<div class="hl-step sr sr-d{i+1}">'
                      f'<span class="hl-step-n">0{i+1}</span>'
                      f'{icon}'
                      f'<div class="hl-step-title">{title}</div>'
                      f'<div class="hl-step-desc">{desc}</div>'
                      f'{connector}'
                      f'</div>')

    H(f'<div id="how" class="hl-how">'
      f'<div class="hl-section">'
      f'<div class="hl-divider">How it works</div>'
      f'<div class="hl-steps">{step_html}</div>'
      f'</div></div>')

def render_story_ats():
    ring = ats_ring(78)
    bars = ats_bars()
    p = pills(["ATS Score","6-Dimension Breakdown","Keyword Gap","Grammar Check","Downloadable Report"], "#30d158")
    H(f'<div id="analyzer" class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      f'<div class="sr">'
      f'<div class="hl-story-num">Feature 01 &mdash; Resume Analyzer</div>'
      f'<h2 class="hl-story-h">Your resume, <span class="hl-blue">scored like<br>a machine</span> reads it</h2>'
      f'<p class="hl-story-p">Most resumes never reach a human. ATS systems silently filter them on format, missing keywords, or structural issues. Hirelyzer replicates how parsers actually read your document &mdash; not just a surface keyword match.</p>'
      f'<p class="hl-story-p">You get a score across six dimensions, a prioritised fix list, grammar signals, and a full keyword-gap report mapped to the roles you care about.</p>'
      f'<div class="hl-pills">{p}</div>'
      f'</div>'
      f'<div class="sr sr-d2"><div class="hl-panel">'
      f'<div class="hl-ptitle"><svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#30d158"/></svg>ATS Analysis Report</div>'
      f'<div style="display:flex;align-items:center;gap:20px;margin-bottom:24px">'
      + ring +
      f'<div>'
      f'<div style="font-size:9px;color:rgba(240,240,242,0.34);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:5px">Overall Score</div>'
      f'<div style="font-size:22px;font-weight:900;color:#f0f0f2;letter-spacing:-1px">78 <span style="font-size:13px;font-weight:400;color:#30d158">/ 100</span></div>'
      f'<div style="font-size:12px;color:#30d158;font-weight:600;margin-top:4px">Good &middot; Minor fixes needed</div>'
      f'<div style="font-size:10px;color:rgba(240,240,242,0.34);margin-top:3px;font-family:var(--mono)">Parsed in 1.4s</div>'
      f'</div></div>'
      + bars +
      f'</div></div>'
      f'</div></div></div>')

def render_story_bias():
    p = pills(["Gender-coded Detection","AI Neutral Rewrite","400+ Word Lexicon","One-click Apply"], "#bf5af2")
    H(f'<div class="hl-story-alt"><div class="hl-section"><div class="hl-story-grid">'
      f'<div style="order:2" class="sr sr-d2">'
      f'<div class="hl-story-num">Feature 02 &mdash; Bias Detection</div>'
      f'<h2 class="hl-story-h">Bias-free language<br>that <span class="hl-purp"><em>opens</em> every door</span></h2>'
      f'<p class="hl-story-p">Gender-coded words can unconsciously signal culture fit to recruiters. Hirelyzer scans every verb, adjective, and phrase against a curated lexicon of 400+ bias terms.</p>'
      f'<p class="hl-story-p">The AI rewriter suggests impact-neutral alternatives, preserving your achievements while broadening appeal across all hiring contexts and company cultures.</p>'
      f'<div class="hl-pills">{p}</div>'
      f'</div>'
      f'<div style="order:1" class="sr"><div class="hl-panel">'
      f'<div class="hl-ptitle"><svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#bf5af2"/></svg>Bias Analysis Report</div>'
      f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:18px">'
      f'<div style="padding:16px;background:rgba(10,132,255,0.07);border-radius:14px;border:1px solid rgba(10,132,255,0.16)">'
      f'<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:7px">Masculine</div>'
      f'<div style="font-size:32px;font-weight:900;color:#5ab8ff;letter-spacing:-2px">8</div>'
      f'<div style="font-size:11px;color:rgba(240,240,242,0.34);margin-top:2px">words flagged</div></div>'
      f'<div style="padding:16px;background:rgba(191,90,242,0.07);border-radius:14px;border:1px solid rgba(191,90,242,0.16)">'
      f'<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:7px">Feminine</div>'
      f'<div style="font-size:32px;font-weight:900;color:#d088f8;letter-spacing:-2px">3</div>'
      f'<div style="font-size:11px;color:rgba(240,240,242,0.34);margin-top:2px">words flagged</div></div>'
      f'</div>'
      f'<div style="font-size:10px;color:rgba(240,240,242,0.34);font-weight:700;text-transform:uppercase;letter-spacing:.9px;margin-bottom:11px">Detected language</div>'
      f'<div class="hl-words"><span class="wc wc-m">driven</span><span class="wc wc-m">aggressive</span>'
      f'<span class="wc wc-m">dominate</span><span class="wc wc-m">champion</span>'
      f'<span class="wc wc-f">nurture</span><span class="wc wc-f">support</span>'
      f'<span class="wc wc-n">deliver</span><span class="wc wc-n">execute</span></div>'
      f'<div style="padding:16px;background:rgba(48,209,88,0.07);border-radius:14px;border:1px solid rgba(48,209,88,0.20)">'
      f'<div style="font-size:12px;font-weight:700;color:#30d158;margin-bottom:8px">AI Rewrite Applied</div>'
      f'<div style="font-size:13px;color:rgba(240,240,242,0.54);line-height:1.65">'
      f'<span style="text-decoration:line-through;opacity:.45">Aggressively drove growth</span>'
      f' &rarr; <span style="color:#30d158;font-weight:600">Accelerated high-impact results</span> across 3 teams'
      f'</div></div>'
      f'</div></div>'
      f'</div></div></div>')

def render_story_builder():
    tmpl = tmpl_gallery()
    p = pills(["15 Templates","DOCX + PDF Export","AI Cover Letter","Live Preview","ATS Single-Column"], "#0a84ff")
    H(f'<div id="builder" class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      f'<div class="sr">'
      f'<div class="hl-story-num">Feature 03 &mdash; Resume Builder</div>'
      f'<h2 class="hl-story-h">Resumes that <span class="hl-green"><em>look</em> as good</span><br>as they parse</h2>'
      f'<p class="hl-story-p">Fifteen ATS-optimised templates &mdash; from understated minimal to executive prestige &mdash; all built on strict single-column structures that parse correctly in every major hiring platform.</p>'
      f'<p class="hl-story-p">Export to DOCX (three ATS compliance levels) or PDF. One click generates a tailored cover letter for your target company, formatted and ready to send.</p>'
      f'<div class="hl-pills">{p}</div>'
      f'</div>'
      f'<div class="sr sr-d2"><div class="hl-panel">'
      f'<div class="hl-ptitle">'
      f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="10" height="14" rx="2" stroke="#30d158" stroke-width="1.5"/><rect x="11" y="7" width="10" height="14" rx="2" fill="rgba(48,209,88,.08)" stroke="#30d158" stroke-width="1.5"/><path d="M14 11h5M14 14h5M14 17h3" stroke="#30d158" stroke-width="1.3" stroke-linecap="round"/></svg>'
      f'Template Gallery &mdash; 15 Designs</div>'
      f'<div class="hl-tmpl-grid">{tmpl}</div>'
      f'<div style="padding:16px;background:rgba(10,132,255,0.07);border-radius:14px;border:1px solid rgba(10,132,255,0.20);display:flex;align-items:center;justify-content:space-between;gap:13px">'
      f'<div><div style="font-size:13px;font-weight:700;color:#0a84ff">Modern &mdash; ATS Certified</div>'
      f'<div style="font-size:11px;color:rgba(240,240,242,0.34);margin-top:3px">Sora &middot; Navy headings &middot; Single-column</div></div>'
      f'<a href="{APP_URL}" target="_blank" style="padding:9px 20px;background:#0a84ff;color:#fff;border-radius:100px;font-size:12px;font-weight:700;text-decoration:none;white-space:nowrap;flex-shrink:0;box-shadow:0 4px 16px rgba(10,132,255,0.30)">Use this</a>'
      f'</div>'
      f'</div></div>'
      f'</div></div></div>')

def render_story_career():
    cards = job_cards()
    p = pills(["Live Job Listings","Salary Benchmarks","Course Recommendations","Skills Radar","Remote Filter"], "#ff9f0a")
    H(f'<div id="career" class="hl-story-alt"><div class="hl-section"><div class="hl-story-grid">'
      f'<div style="order:2" class="sr sr-d2">'
      f'<div class="hl-story-num">Feature 04 &mdash; Career Intelligence</div>'
      f'<h2 class="hl-story-h">Jobs, salaries, courses &mdash;<br><span class="hl-amber">one place</span></h2>'
      f'<p class="hl-story-p">The Job Search Hub pulls live listings from LinkedIn, Naukri, Foundit, and Indeed &mdash; with remote and employment-type filters powered by JSearch / RapidAPI.</p>'
      f'<p class="hl-story-p">Hirelyzer surfaces salary benchmarks by role and market, curated courses mapped to skill gaps in your resume, and prep videos &mdash; all linked to your career profile.</p>'
      f'<div class="hl-pills">{p}</div>'
      f'</div>'
      f'<div style="order:1" class="sr"><div class="hl-panel">'
      f'<div class="hl-ptitle">'
      f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none"><rect x="2" y="7" width="20" height="14" rx="2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M2 13h20" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/></svg>'
      f'Job Search Hub</div>'
      + cards +
      f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-top:8px">'
      f'<div style="padding:14px;background:rgba(255,159,10,0.07);border-radius:13px;border:1px solid rgba(255,159,10,0.18)">'
      f'<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:6px">Avg Salary</div>'
      f'<div style="font-size:22px;font-weight:900;color:#ff9f0a;letter-spacing:-1px">&#8377;18&ndash;32 LPA</div>'
      f'<div style="font-size:11px;color:rgba(240,240,242,0.34);margin-top:2px">Backend &middot; India</div></div>'
      f'<div style="padding:14px;background:rgba(10,132,255,0.07);border-radius:13px;border:1px solid rgba(10,132,255,0.18)">'
      f'<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:6px">Platforms</div>'
      f'<div style="font-size:13px;font-weight:700;color:#f0f0f2;line-height:1.8">LinkedIn &middot; Naukri<br>Foundit &middot; Indeed</div></div>'
      f'</div>'
      f'</div></div>'
      f'</div></div></div>')

def render_story_interview():
    sbars = score_bars()
    radar = radar_svg()
    p = pills(["Resume-based Questions","Real-time AI Scoring","Radar Chart","Session History","Downloadable Report"], "#ff453a")
    H(f'<div class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      f'<div class="sr">'
      f'<div class="hl-story-num">Feature 05 &mdash; AI Interview Coach</div>'
      f'<h2 class="hl-story-h">Practice until <span class="hl-blue"><em>every</em> answer</span><br>lands</h2>'
      f'<p class="hl-story-p">Upload your resume and Hirelyzer generates interview questions derived directly from your actual experience &mdash; not generic prompts. Answer in free text; the AI coach scores you on five dimensions including technical depth and concrete examples.</p>'
      f'<p class="hl-story-p">Every session ends with a performance radar chart, a detailed Q&amp;A review, and course recommendations tied to your weakest dimensions.</p>'
      f'<div class="hl-pills">{p}</div>'
      f'</div>'
      f'<div class="sr sr-d2"><div class="hl-panel">'
      f'<div class="hl-ptitle" style="justify-content:space-between">'
      f'<div style="display:flex;align-items:center;gap:9px">'
      f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#ff453a" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>'
      f'Mock Interview &middot; Session 3</div>'
      f'<div class="hl-score-badge"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg>82 / 100</div>'
      f'</div>'
      f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:start">'
      f'<div>'
      f'<div class="hl-qa">'
      f'<div class="hl-q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px"><circle cx="12" cy="12" r="10" stroke="#0a84ff" stroke-width="1.5"/><path d="M12 16v-4M12 8h.01" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round"/></svg>Describe your most complex backend system.</div>'
      f'<div class="hl-a">Built a multi-tenant microservices platform handling 2M events/day using Kafka, Redis, and PostgreSQL with 40% lower P99 latency.</div>'
      f'</div>'
      f'<div class="hl-qa">'
      f'<div class="hl-q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px"><circle cx="12" cy="12" r="10" stroke="#bf5af2" stroke-width="1.5"/><path d="M12 16v-4M12 8h.01" stroke="#bf5af2" stroke-width="1.8" stroke-linecap="round"/></svg>How do you handle technical debt?</div>'
      f'<div class="hl-a">I prioritise tech debt as a first-class roadmap item, quantifying velocity cost before pitching refactors to stakeholders.</div>'
      f'</div>'
      f'<div style="margin-top:14px">'
      f'<div style="font-size:10px;text-transform:uppercase;letter-spacing:.9px;color:rgba(240,240,242,0.34);font-weight:700;margin-bottom:10px">Score breakdown</div>'
      + sbars +
      f'</div></div>'
      f'<div class="hl-radar-wrap">{radar}'
      f'<div style="font-size:11px;color:rgba(240,240,242,0.34);margin-top:8px;text-align:center;font-weight:500">Performance radar</div>'
      f'</div>'
      f'</div>'
      f'</div></div>'
      f'</div></div></div>')

def render_testimonials():
    testimonials = [
        ("4db3ff", "bg:rgba(10,132,255,0.12)",
         "Went from 0 callbacks to 4 interviews in 2 weeks. The ATS scorer showed me exactly what was killing my resume — two-column layout and a missing skills section.",
         "Arjun M.", "SDE at Flipkart", "A"),
        ("d088f8", "bg:rgba(191,90,242,0.12)",
         "The bias detection feature is genuinely eye-opening. I had no idea 'aggressive' and 'dominate' were flagged — the AI rewrite kept all the impact but broadened the appeal.",
         "Priya K.", "ML Engineer at Razorpay", "P"),
        ("4dd96a", "bg:rgba(48,209,88,0.12)",
         "Cover letter generator saved me hours. I just typed the company name and it pulled from my resume to write something specific and polished. Landed my dream role at a startup.",
         "Rohan S.", "Product Manager at Zepto", "R"),
        ("ffd60a", "bg:rgba(255,214,10,0.10)",
         "The AI Interview Coach is unreal. It generated questions from my actual projects and scored my answers in real-time. My confidence going into interviews skyrocketed.",
         "Sneha T.", "Data Scientist at Myntra", "S"),
        ("5ab8ff", "bg:rgba(10,132,255,0.08)",
         "I uploaded my resume, fixed the 3 issues it flagged, and my ATS score jumped from 58 to 91. Got a callback from Google within a week. This tool is legitimately powerful.",
         "Vikram N.", "Backend Dev at Anthropic", "V"),
        ("ffb340", "bg:rgba(255,159,10,0.10)",
         "15 templates and every single one is ATS-safe. I switched from a creative two-pager and immediately started getting responses from Indian and international companies.",
         "Ananya R.", "Full Stack Dev at Swiggy", "A"),
    ]
    stars_html = "".join([star() for _ in range(5)])
    cards_html = ""
    for col, bg_str, quote, name, role, initial in testimonials:
        bg_val = bg_str.replace("bg:", "")
        cards_html += (
            f'<div class="hl-testi sr">'
            f'<div class="hl-testi-stars">{stars_html}</div>'
            f'<p class="hl-testi-text">&ldquo;{quote}&rdquo;</p>'
            f'<div class="hl-testi-author">'
            f'<div class="hl-testi-avatar" style="background:{bg_val};color:#{col}">{initial}</div>'
            f'<div><div class="hl-testi-name">{name}</div><div class="hl-testi-role">{role}</div></div>'
            f'</div></div>'
        )
    H(f'<div id="testimonials" class="hl-testis">'
      f'<div class="hl-section">'
      f'<div class="hl-divider">What users say</div>'
      f'<div class="hl-testi-grid">{cards_html}</div>'
      f'</div></div>')

def render_cta():
    chk = checklist()
    H(f'<div id="contact" style="max-width:1160px;margin:0 auto;" class="hl-cta-wrap">'
      f'<div class="hl-cta">'
      f'<div class="hl-eyebrow" style="margin:0 auto 30px">'
      f'<svg width="7" height="7" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>'
      f'Free to use &middot; No credit card required</div>'
      f'<div class="hl-cta-h">Your next job starts<br>with a <em>better</em> resume</div>'
      f'<p class="hl-cta-sub">Join professionals already using Hirelyzer to pass ATS filters,<br>remove bias, and land more interviews.</p>'
      f'<div class="hl-cta-btns">'
      f'<a href="{APP_URL}" target="_blank" class="hl-btn-p" style="font-size:16px;padding:17px 40px">'
      f'<svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      f'Start for free</a>'
      f'<a href="mailto:support@hirelyzer.com" class="hl-btn-g" style="font-size:16px;padding:17px 36px">'
      f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" fill="none"/><polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>'
      f'Contact us</a>'
      f'</div>'
      f'<div class="hl-checks">{chk}</div>'
      f'</div></div>')

def render_footer():
    H(f'<div class="hl-footer-wrap">'
      f'<div class="hl-footer">'
      f'<div>'
      f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">'
      f'<div class="hl-logo-icon" style="width:28px;height:28px;border-radius:8px">'
      f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'</div>'
      f'<span style="font-size:13px;font-weight:800;letter-spacing:0.5px">HIRELYZER</span>'
      f'</div>'
      f'<div class="hl-footer-copy">&copy; 2025 HIRELYZER &middot; Intelligent Career Platform</div>'
      f'</div>'
      f'<div class="hl-footer-links">'
      f'<a href="#">Privacy</a>'
      f'<a href="#">Terms</a>'
      f'<a href="mailto:support@hirelyzer.com">support@hirelyzer.com</a>'
      f'<a href="{APP_URL}" target="_blank" style="color:#0a84ff;font-weight:600">Open App &rarr;</a>'
      f'</div></div></div>')

def render_js():
    H('''<script>
(function(){
  // ── Scroll progress bar ──
  var sp = document.getElementById("sp");
  function updateProgress(){
    if(!sp) return;
    var pct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    sp.style.width = Math.min(pct,100) + "%";
  }
  window.addEventListener("scroll", updateProgress, {passive:true});

  // ── Scroll reveal ──
  var srEls = document.querySelectorAll(".sr");
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){ e.target.classList.add("visible"); io.unobserve(e.target); }
    });
  }, {threshold:0.12});
  srEls.forEach(function(el){ io.observe(el); });

  // ── Animated counter ──
  function animateCount(el, target, duration){
    var start = 0; var step = target / (duration / 16);
    var timer = setInterval(function(){
      start += step;
      if(start >= target){ start = target; clearInterval(timer); }
      el.textContent = (target > 100 ? Math.round(start)+"+" : (target > 10 ? Math.round(start)+"+" : Math.round(start)));
    }, 16);
  }
  var statEls = document.querySelectorAll(".hl-stat-n[data-count]");
  var statIO = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        var el = e.target;
        var v = parseInt(el.getAttribute("data-count"));
        if(!isNaN(v) && v > 0) animateCount(el, v, 1200);
        statIO.unobserve(el);
      }
    });
  }, {threshold:0.5});
  statEls.forEach(function(el){ statIO.observe(el); });

  // ── Floating particle canvas ──
  var canvas = document.createElement("canvas");
  canvas.id = "hero-canvas";
  canvas.style.cssText = "position:absolute;inset:0;pointer-events:none;z-index:0;opacity:0.55;";
  var hero = document.querySelector(".hl-hero");
  if(hero){ hero.insertBefore(canvas, hero.firstChild); }

  function resizeCanvas(){
    if(!hero) return;
    canvas.width  = hero.offsetWidth;
    canvas.height = hero.offsetHeight;
  }
  resizeCanvas();
  window.addEventListener("resize", resizeCanvas, {passive:true});

  var ctx = canvas.getContext("2d");
  var particles = [];
  var N = 48;
  for(var i=0; i<N; i++){
    particles.push({
      x: Math.random()*canvas.width,
      y: Math.random()*canvas.height,
      r: Math.random()*1.6+0.4,
      dx: (Math.random()-0.5)*0.22,
      dy: (Math.random()-0.5)*0.22,
      alpha: Math.random()*0.5+0.15,
      color: ["rgba(10,132,255,","rgba(48,209,88,","rgba(191,90,242,","rgba(100,210,255,"][Math.floor(Math.random()*4)]
    });
  }

  function drawParticles(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    // connection lines
    for(var a=0; a<particles.length; a++){
      for(var b=a+1; b<particles.length; b++){
        var dx2=particles[a].x-particles[b].x, dy2=particles[a].y-particles[b].y;
        var dist=Math.sqrt(dx2*dx2+dy2*dy2);
        if(dist<120){
          ctx.beginPath();
          ctx.moveTo(particles[a].x,particles[a].y);
          ctx.lineTo(particles[b].x,particles[b].y);
          ctx.strokeStyle="rgba(255,255,255,"+(0.04*(1-dist/120))+")";
          ctx.lineWidth=0.5;
          ctx.stroke();
        }
      }
    }
    // dots
    particles.forEach(function(p){
      ctx.beginPath();
      ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=p.color+p.alpha+")";
      ctx.fill();
      p.x+=p.dx; p.y+=p.dy;
      if(p.x<0||p.x>canvas.width)  p.dx*=-1;
      if(p.y<0||p.y>canvas.height) p.dy*=-1;
    });
    requestAnimationFrame(drawParticles);
  }
  drawParticles();

  // ── Typewriter for hero heading ──
  var h1 = document.querySelector(".hl-h1");
  if(h1){
    var original = h1.innerHTML;
    // reset and retype the last word with a cursor
    h1.style.opacity = "1";
  }

  // ── Navbar bg on scroll ──
  var nav = document.querySelector(".hl-nav");
  window.addEventListener("scroll", function(){
    if(!nav) return;
    nav.style.background = window.scrollY > 40
      ? "rgba(0,0,0,0.95)"
      : "rgba(0,0,0,0.76)";
  }, {passive:true});

  // ── Template hover highlight ──
  var tmpls = document.querySelectorAll(".hl-tmpl");
  tmpls.forEach(function(t){
    t.addEventListener("mouseenter", function(){
      tmpls.forEach(function(x){ x.classList.remove("hl-tmpl-act"); });
      t.classList.add("hl-tmpl-act");
    });
  });

})();
</script>''')

# ─── MAIN ────────────────────────────────────────────────────────────────────
render_nav()
render_hero()
render_marquee()
render_how()
render_story_ats()
render_story_bias()
render_story_builder()
render_story_career()
render_story_interview()
render_testimonials()
render_cta()
render_footer()
render_js()
