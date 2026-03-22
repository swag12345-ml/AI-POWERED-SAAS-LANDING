mport streamlit as st
import base64
from textwrap import dedent

st.set_page_config(page_title="HIRELYZER — Cinematic Landing", page_icon="🚀", layout="wide")
st.set_page_config(page_title="HIRELYZER — Intelligent Career Platform", page_icon="⬡", layout="wide")

# ---------------------- Helpful utilities ----------------------
def local_css(css: str):
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def img_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ---------------------- Advanced Cinematic CSS ----------------------
css = dedent("""
:root{
  --bg1: #050816;
  --bg2: #0e0b1a;
  --accent: linear-gradient(135deg,#ff6a88 0%,#ff8a50 25%,#5f2c82 50%,#2b5876 75%,#1e3c72 100%);
  --accent-hover: linear-gradient(135deg,#ff7a98 0%,#ff9a60 25%,#6f3c92 50%,#3b6886 75%,#2e4c82 100%);
  --glass: rgba(255,255,255,0.06);
  --glass-strong: rgba(255,255,255,0.08);
  --card-shadow: 0 20px 60px rgba(2,6,23,0.8), 0 8px 32px rgba(79,70,229,0.15);
  --glow: 0 0 40px rgba(79,70,229,0.3);
  --text-glow: 0 0 20px rgba(255,255,255,0.1);
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg:       #000000;
  --bg1:      #0a0a0a;
  --bg2:      #111111;
  --bg3:      #161616;
  --surface:  #1c1c1e;
  --border:   rgba(255,255,255,0.08);
  --border2:  rgba(255,255,255,0.14);
  --text:     #f5f5f7;
  --muted:    rgba(245,245,247,0.56);
  --muted2:   rgba(245,245,247,0.36);
  --accent:   #0a84ff;
  --accent2:  #30d158;
  --accent3:  #ff9f0a;
  --accent4:  #bf5af2;
  --mono:     'JetBrains Mono', monospace;
  --sans:     'Sora', -apple-system, 'SF Pro Display', sans-serif;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-10px) rotate(1deg); }
  66% { transform: translateY(5px) rotate(-1deg); }
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

@keyframes pulse-glow {
  0%, 100% { box-shadow: var(--card-shadow), var(--glow); }
  50% { box-shadow: var(--card-shadow), 0 0 60px rgba(79,70,229,0.4); }
html, body, [data-testid="stAppViewContainer"], [class*="css"] {
  background: var(--bg) !important;
  color: var(--text);
  font-family: var(--sans);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
footer { display: none !important; }

[data-testid="stAppViewContainer"] > section { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ─── SCROLL PROGRESS ─── */
#sp { position:fixed;top:0;left:0;height:2px;width:0%;background:var(--accent);z-index:9999;transition:width .08s linear; }

/* ─── NAV ─── */
.hl-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 900;
  backdrop-filter: saturate(180%) blur(24px);
  -webkit-backdrop-filter: saturate(180%) blur(24px);
  background: rgba(0,0,0,0.72);
  border-bottom: 1px solid var(--border);
  height: 56px;
  display: flex; align-items: center; justify-content: center;
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
.hl-nav-inner {
  width: 100%; max-width: 1100px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
}

@keyframes scale-in {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
.hl-logo {
  display: flex; align-items: center; gap: 10px;
  font-size: 15px; font-weight: 700; letter-spacing: -.2px;
  color: var(--text); text-decoration: none;
}

html, body, [class*="css"]{
  background: 
    radial-gradient(1400px 800px at 15% 15%, rgba(79, 70, 229, 0.15), transparent),
    radial-gradient(1200px 700px at 85% 85%, rgba(59,130,246,0.08), transparent),
    radial-gradient(800px 600px at 50% 0%, rgba(139, 92, 246, 0.05), transparent),
    linear-gradient(180deg,var(--bg1),var(--bg2));
  color: rgba(255,255,255,0.95);
  font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  overflow-x: hidden;
.hl-logo-mark {
  width: 30px; height: 30px; display: flex; align-items: center; justify-content: center;
  background: var(--accent); border-radius: 8px;
}
.hl-nav-links {
  display: flex; align-items: center; gap: 28px;
}
.hl-nav-links a {
  font-size: 13px; font-weight: 500; color: var(--muted);
  text-decoration: none; transition: color .2s;
  letter-spacing: -.1px;
}
.hl-nav-links a:hover { color: var(--text); }
.hl-nav-cta {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 18px; border-radius: 980px;
  background: var(--accent); color: #fff;
  font-size: 13px; font-weight: 600; text-decoration: none;
  transition: opacity .2s, transform .15s;
  letter-spacing: -.1px;
}
.hl-nav-cta:hover { opacity: .86; transform: scale(.98); }

.hero{
  display:flex;
  gap:32px;
  align-items:center;
  padding:60px 32px;
  border-radius:24px;
  background:linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.05);
  box-shadow:var(--card-shadow);
  animation: slide-up 0.8s ease-out, pulse-glow 4s ease-in-out infinite;
  position: relative;
  overflow: hidden;
/* ─── SECTIONS ─── */
.hl-section {
  max-width: 1100px; margin: 0 auto; padding: 0 32px;
}

.hero::before {
/* ─── HERO ─── */
.hl-hero {
  min-height: 100vh;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  text-align: center; padding: 120px 32px 80px;
  position: relative; overflow: hidden;
}
.hl-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
  animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
  0% { left: -100%; }
  100% { left: 100%; }
}

.hero-left{
  flex:1;
  z-index: 2;
}

.hero-right{
  width:450px;
  min-width:350px;
  z-index: 2;
  animation: float 6s ease-in-out infinite;
}

.h-eyebrow{
  letter-spacing:3px;
  color:rgba(255,255,255,0.6);
  font-weight:700;
  font-size:13px;
  text-transform: uppercase;
  text-shadow: var(--text-glow);
  animation: slide-up 0.8s ease-out 0.2s both;
}

.h-title{
  font-size:56px;
  font-weight:900;
  line-height:1.05;
  margin:12px 0;
  background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 50%, #cbd5e1 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 30px rgba(255,255,255,0.1);
  animation: slide-up 0.8s ease-out 0.4s both;
}

.h-sub{
  color:rgba(255,255,255,0.75);
  font-size:20px;
  margin-bottom:24px;
  line-height: 1.6;
  animation: slide-up 0.8s ease-out 0.6s both;
}

.cta-row{
  display:flex;
  gap:16px;
  animation: slide-up 0.8s ease-out 0.8s both;
}

.btn{
  background:var(--accent);
  background-size: 200% 200%;
  padding:16px 28px;
  border-radius:16px;
  font-weight:800;
  border:none;
  cursor:pointer;
  box-shadow:0 12px 24px rgba(79,70,229,0.25), 0 4px 12px rgba(0,0,0,0.1);
  color:white;
  font-size:16px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  text-decoration: none;
  display: inline-block;
  animation: gradient-shift 3s ease infinite;
  position: absolute; top: -200px; left: 50%; transform: translateX(-50%);
  width: 800px; height: 600px;
  background: radial-gradient(ellipse, rgba(10,132,255,.12) 0%, transparent 70%);
  pointer-events: none;
}

.btn:hover{
  background:var(--accent-hover);
  transform: translateY(-2px) scale(1.02);
  box-shadow:0 16px 32px rgba(79,70,229,0.35), 0 8px 16px rgba(0,0,0,0.2);
.hl-hero::after {
  content: '';
  position: absolute; bottom: 0; left: 0; right: 0; height: 200px;
  background: linear-gradient(to bottom, transparent, var(--bg));
  pointer-events: none;
}

.btn:active{
  transform: translateY(0) scale(0.98);
.hl-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 11px; font-weight: 600; letter-spacing: 1.4px; text-transform: uppercase;
  color: var(--accent); margin-bottom: 28px;
  padding: 6px 14px; border-radius: 980px;
  border: 1px solid rgba(10,132,255,.3);
  background: rgba(10,132,255,.07);
  animation: fadeUp .7s ease both;
}

.btn.secondary{
  background:transparent;
  border:2px solid rgba(255,255,255,0.1);
  color:white;
  backdrop-filter: blur(10px);
.hl-h1 {
  font-size: clamp(42px, 7vw, 86px);
  font-weight: 800; line-height: 1.03; letter-spacing: -3px;
  color: var(--text);
  animation: fadeUp .7s .12s ease both;
  max-width: 920px;
}

.btn.secondary:hover{
  background:rgba(255,255,255,0.05);
  border-color: rgba(255,255,255,0.2);
  transform: translateY(-2px) scale(1.02);
.hl-h1 em { font-style: normal; color: var(--accent); }
.hl-hero-sub {
  font-size: clamp(16px, 2vw, 20px); color: var(--muted);
  font-weight: 400; line-height: 1.6; letter-spacing: -.2px;
  max-width: 580px; margin: 24px auto 0;
  animation: fadeUp .7s .22s ease both;
}

.features{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:24px;
  margin-top:32px;
.hl-hero-ctas {
  display: flex; gap: 14px; justify-content: center; margin-top: 44px;
  animation: fadeUp .7s .32s ease both;
}
.hl-btn-primary {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 14px 28px; border-radius: 980px;
  background: var(--accent); color: #fff;
  font-size: 15px; font-weight: 600; text-decoration: none;
  letter-spacing: -.2px;
  transition: opacity .2s, transform .15s;
  box-shadow: 0 0 0 0 rgba(10,132,255,0);
}
.hl-btn-primary:hover { opacity: .86; transform: translateY(-1px); }
.hl-btn-ghost {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 14px 28px; border-radius: 980px;
  background: var(--surface); color: var(--text);
  font-size: 15px; font-weight: 600; text-decoration: none;
  letter-spacing: -.2px; border: 1px solid var(--border2);
  transition: background .2s, transform .15s;
}
.hl-btn-ghost:hover { background: #2c2c2e; transform: translateY(-1px); }

.feature-card{
  padding:28px;
  border-radius:20px;
  background:linear-gradient(135deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
  backdrop-filter: blur(20px);
  border:1px solid rgba(255,255,255,0.06);
  box-shadow: 0 8px 32px rgba(0,0,0,0.3);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
/* ─── HERO CARD ─── */
.hl-hero-card {
  margin-top: 72px; width: 100%; max-width: 780px;
  background: var(--bg2); border-radius: 22px;
  border: 1px solid var(--border);
  overflow: hidden;
  animation: scale-in 0.6s ease-out;
  animation: fadeUp .7s .45s ease both;
  box-shadow: 0 40px 100px rgba(0,0,0,.6);
  position: relative; z-index: 1;
}

.feature-card:hover{
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 60px rgba(0,0,0,0.4), 0 0 40px rgba(79,70,229,0.2);
  border-color: rgba(255,255,255,0.12);
.hl-card-bar {
  height: 38px; background: var(--bg3);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 16px; gap: 8px;
}
.hl-dot { width: 12px; height: 12px; border-radius: 50%; }
.hl-card-body { padding: 28px; }

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transition: transform 0.4s ease;
/* ─── STAT ROW ─── */
.hl-stat-row {
  display: flex; gap: 12px; flex-wrap: wrap; justify-content: center;
  margin: 28px 0 0; animation: fadeUp .7s .55s ease both;
}

.feature-card:hover::before {
  transform: scaleX(1);
.hl-stat {
  display: flex; flex-direction: column; align-items: center;
  padding: 18px 28px; border-radius: 16px;
  background: var(--bg2); border: 1px solid var(--border);
  min-width: 130px;
}
.hl-stat-n { font-size: 26px; font-weight: 800; color: var(--text); letter-spacing: -1px; }
.hl-stat-l { font-size: 11px; color: var(--muted2); font-weight: 500; margin-top: 4px; text-transform: uppercase; letter-spacing: .8px; }

.feature-title{
  font-weight:800;
  margin-top:12px;
  font-size:18px;
  color: rgba(255,255,255,0.95);
/* ─── DIVIDER LABEL ─── */
.hl-section-label {
  font-size: 11px; font-weight: 600; letter-spacing: 1.4px; text-transform: uppercase;
  color: var(--muted2); display: flex; align-items: center; gap: 16px; margin-bottom: 72px;
}

.feature-desc{
  color:rgba(255,255,255,0.7);
  font-size:15px;
  margin-top:8px;
  line-height: 1.6;
.hl-section-label::before, .hl-section-label::after {
  content: ''; flex: 1; height: 1px; background: var(--border);
}

.footer{
  padding:32px 16px;
  margin-top:32px;
  color:rgba(255,255,255,0.6);
  text-align: center;
  border-top: 1px solid rgba(255,255,255,0.05);
/* ─── STORY SECTIONS ─── */
.hl-story { padding: 100px 0; }
.hl-story-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;
}

.nav-container {
  backdrop-filter: blur(20px);
  background: rgba(5,8,22,0.8);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  position: sticky;
  top: 0;
  z-index: 100;
  animation: slide-up 0.6s ease-out;
.hl-story-grid.reverse { direction: rtl; }
.hl-story-grid.reverse > * { direction: ltr; }
.hl-story-number {
  font-family: var(--mono); font-size: 11px; font-weight: 500;
  color: var(--muted2); letter-spacing: 1px; margin-bottom: 20px;
}

.nav-link {
  transition: all 0.3s ease;
  position: relative;
.hl-story-heading {
  font-size: clamp(28px, 4vw, 44px);
  font-weight: 800; letter-spacing: -1.5px; line-height: 1.1;
  color: var(--text); margin-bottom: 20px;
}

.nav-link:hover {
  color: rgba(255,255,255,0.95) !important;
  transform: translateY(-1px);
.hl-story-heading span { color: var(--accent); }
.hl-story-body {
  font-size: 16px; color: var(--muted); line-height: 1.75; font-weight: 400;
  margin-bottom: 28px;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--accent);
  transition: width 0.3s ease;
.hl-story-pills { display: flex; flex-wrap: wrap; gap: 8px; }
.hl-pill {
  padding: 6px 14px; border-radius: 980px;
  font-size: 12px; font-weight: 600; letter-spacing: -.1px;
  border: 1px solid var(--border); color: var(--muted);
  background: var(--bg2);
}

.nav-link:hover::after {
  width: 100%;
/* ─── VISUAL PANELS ─── */
.hl-panel {
  background: var(--bg2); border-radius: 20px; border: 1px solid var(--border);
  padding: 28px; overflow: hidden; position: relative;
}

.logo-container {
  transition: all 0.3s ease;
.hl-panel-title {
  font-size: 11px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 1px; color: var(--muted2); margin-bottom: 20px;
  display: flex; align-items: center; gap: 8px;
}

.logo-container:hover {
  transform: scale(1.05);
.hl-score-ring-wrap { display: flex; align-items: center; gap: 24px; margin-bottom: 24px; }
.hl-score-val { font-size: 42px; font-weight: 800; color: var(--text); letter-spacing: -2px; }
.hl-score-sub { font-size: 12px; color: var(--muted2); margin-top: 2px; font-weight: 500; }
.hl-bar-row { display: flex; flex-direction: column; gap: 10px; }
.hl-bar-item { }
.hl-bar-label { display: flex; justify-content: space-between; font-size: 12px; color: var(--muted); margin-bottom: 5px; font-weight: 500; }
.hl-bar-track { height: 4px; background: var(--border); border-radius: 2px; overflow: hidden; }
.hl-bar-fill { height: 100%; border-radius: 2px; transition: width 1.2s cubic-bezier(.4,0,.2,1); }

/* word chips */
.hl-word-row { display: flex; flex-wrap: wrap; gap: 7px; }
.hl-word-chip {
  padding: 5px 11px; border-radius: 8px; font-size: 12px; font-weight: 600;
  font-family: var(--mono);
}

.ats-preview {
  border-radius:18px;
  padding:24px;
  background:linear-gradient(135deg, rgba(255,255,255,0.04), rgba(0,0,0,0.3));
  backdrop-filter: blur(20px);
  box-shadow:0 25px 80px rgba(0,0,0,0.7), 0 0 40px rgba(79,70,229,0.1);
  border:1px solid rgba(255,255,255,0.06);
  transition: all 0.4s ease;
  animation: float 8s ease-in-out infinite;
.hl-chip-m { background: rgba(10,132,255,.12); color: #4db3ff; border: 1px solid rgba(10,132,255,.2); }
.hl-chip-f { background: rgba(191,90,242,.12); color: #d07ef7; border: 1px solid rgba(191,90,242,.2); }
.hl-chip-n { background: rgba(48,209,88,.12); color: #4cd964; border: 1px solid rgba(48,209,88,.2); }

/* template preview */
.hl-template-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.hl-template-thumb {
  border-radius: 10px; border: 1px solid var(--border); overflow: hidden;
  aspect-ratio: 3/4; background: var(--bg3); position: relative;
  display: flex; flex-direction: column; padding: 10px; gap: 4px;
}

.ats-preview:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow:0 30px 100px rgba(0,0,0,0.8), 0 0 60px rgba(79,70,229,0.2);
.hl-template-thumb .tl { height: 5px; border-radius: 2px; background: var(--border2); width: 70%; }
.hl-template-thumb .ts { height: 3px; border-radius: 1.5px; background: var(--border); }
.hl-thumb-active { border-color: var(--accent) !important; box-shadow: 0 0 0 2px rgba(10,132,255,.2); }
.hl-thumb-badge {
  position: absolute; bottom: 8px; left: 8px; right: 8px;
  background: rgba(10,132,255,.15); border: 1px solid rgba(10,132,255,.2);
  border-radius: 6px; padding: 4px 8px;
  font-size: 10px; font-weight: 600; color: var(--accent); text-align: center;
  letter-spacing: .5px; text-transform: uppercase;
}

.skill-tag {
  transition: all 0.3s ease;
/* job card */
.hl-job-card {
  padding: 14px 16px; border-radius: 12px; background: var(--bg3);
  border: 1px solid var(--border); display: flex; align-items: center; gap: 12px;
  transition: border-color .2s;
}

.skill-tag:hover {
  background: rgba(79,70,229,0.3) !important;
  transform: scale(1.05);
.hl-job-card:hover { border-color: var(--border2); }
.hl-job-logo {
  width: 36px; height: 36px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 13px; flex-shrink: 0;
}

.section-title {
  background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: slide-up 0.8s ease-out;
.hl-job-meta { flex: 1; min-width: 0; }
.hl-job-title { font-size: 13px; font-weight: 600; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.hl-job-co { font-size: 11px; color: var(--muted2); margin-top: 2px; }
.hl-job-badge { padding: 3px 10px; border-radius: 980px; font-size: 11px; font-weight: 600; }

/* interview coach */
.hl-qa { margin-bottom: 16px; }
.hl-q { font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 8px; display: flex; gap: 8px; }
.hl-a { font-size: 12px; color: var(--muted); line-height: 1.6; padding-left: 22px; }
.hl-score-badge {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 5px 12px; border-radius: 980px; font-size: 12px; font-weight: 700;
  background: rgba(48,209,88,.12); color: var(--accent2);
  border: 1px solid rgba(48,209,88,.2);
}

.pricing-card-featured {
  position: relative;
  overflow: hidden;
/* ─── HOW IT WORKS ─── */
.hl-steps { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; }
.hl-step {
  padding: 32px 24px;
  background: var(--bg2); border: 1px solid var(--border);
  position: relative; overflow: hidden;
}

.pricing-card-featured::before {
  content: 'MOST POPULAR';
  position: absolute;
  top: -10px;
  right: -30px;
  background: var(--accent);
  color: white;
  padding: 8px 40px;
  font-size: 12px;
  font-weight: 800;
  transform: rotate(45deg);
  letter-spacing: 1px;
.hl-step:first-child { border-radius: 20px 0 0 20px; }
.hl-step:last-child { border-radius: 0 20px 20px 0; }
.hl-step-n {
  font-family: var(--mono); font-size: 11px; font-weight: 500; color: var(--muted2);
  margin-bottom: 16px; display: block;
}

@media (max-width: 900px){
  .hero{flex-direction:column; padding: 40px 20px;}
  .hero-right{width: 100%; min-width: auto;}
  .features{grid-template-columns:repeat(1,1fr)}
  .h-title{font-size:40px}
  .cta-row{flex-direction: column; align-items: center;}
  .btn{width: 100%; text-align: center;}
.hl-step-icon { width: 40px; height: 40px; margin-bottom: 16px; }
.hl-step-title { font-size: 15px; font-weight: 700; color: var(--text); margin-bottom: 8px; letter-spacing: -.3px; }
.hl-step-desc { font-size: 13px; color: var(--muted); line-height: 1.65; }
.hl-step-connector {
  position: absolute; top: 44px; right: -18px;
  width: 36px; z-index: 2;
}

@media (max-width: 600px){
  .h-title{font-size:32px}
  .hero{padding: 30px 16px;}
  .feature-card{padding: 20px;}
/* ─── FINAL CTA ─── */
.hl-cta-block {
  margin: 0 0 120px; padding: 80px 48px;
  border-radius: 28px; background: var(--bg2);
  border: 1px solid var(--border); text-align: center;
  position: relative; overflow: hidden;
}

.typewriter{
  display:inline-block;
  overflow:hidden;
  white-space:nowrap;
.hl-cta-block::before {
  content: ''; position: absolute; top: -300px; left: 50%; transform: translateX(-50%);
  width: 600px; height: 600px;
  background: radial-gradient(ellipse, rgba(10,132,255,.1) 0%, transparent 70%);
  pointer-events: none;
}

.typewriter-text{
  border-right:3px solid rgba(255,255,255,0.7);
  padding-right:8px;
  animation: blink 1s infinite;
.hl-cta-heading {
  font-size: clamp(30px, 5vw, 52px);
  font-weight: 800; letter-spacing: -2px; color: var(--text); line-height: 1.07;
  max-width: 640px; margin: 0 auto 20px; position: relative; z-index: 1;
}

@keyframes blink {
  0%, 50% { border-color: rgba(255,255,255,0.7); }
  51%, 100% { border-color: transparent; }
.hl-cta-sub {
  font-size: 17px; color: var(--muted); margin-bottom: 40px;
  position: relative; z-index: 1;
}

.scroll-indicator {
  position: fixed;
  top: 0;
  left: 0;
  width: 0%;
  height: 3px;
  background: var(--accent);
  z-index: 1000;
  transition: width 0.1s ease;
/* ─── FOOTER ─── */
.hl-footer {
  border-top: 1px solid var(--border);
  padding: 40px 32px;
  display: flex; justify-content: space-between; align-items: center;
  max-width: 1100px; margin: 0 auto;
  flex-wrap: wrap; gap: 20px;
}

.parallax-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
.hl-footer-logo { font-size: 14px; font-weight: 700; color: var(--muted); letter-spacing: -.2px; }
.hl-footer-links { display: flex; gap: 24px; }
.hl-footer-links a { font-size: 13px; color: var(--muted2); text-decoration: none; transition: color .2s; }
.hl-footer-links a:hover { color: var(--text); }

/* ─── KEYFRAMES ─── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}

.floating-element {
  position: absolute;
  opacity: 0.1;
  animation: float 10s ease-in-out infinite;
@keyframes spin360 {
  to { transform: rotate(360deg); }
}
@keyframes scanline {
  from { top: 0; } to { top: 100%; }
}
@keyframes pulse2 {
  0%,100% { opacity:1; } 50% { opacity:.5; }
}
@keyframes barGrow {
  from { width: 0; } to { width: var(--w); }
}

.floating-element:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
.floating-element:nth-child(2) { top: 20%; right: 10%; animation-delay: 2s; }
.floating-element:nth-child(3) { bottom: 30%; left: 20%; animation-delay: 4s; }
.floating-element:nth-child(4) { bottom: 10%; right: 20%; animation-delay: 6s; }
/* ─── RESPONSIVE ─── */
@media (max-width:860px) {
  .hl-story-grid { grid-template-columns:1fr; gap:40px; }
  .hl-story-grid.reverse { direction:ltr; }
  .hl-steps { grid-template-columns:1fr 1fr; }
  .hl-step:first-child { border-radius:20px 0 0 0; }
  .hl-step:last-child  { border-radius:0 0 20px 0; }
  .hl-step:nth-child(2) { border-radius:0 20px 0 0; }
  .hl-step:nth-child(3) { border-radius:0 0 0 20px; }
  .hl-hero-ctas { flex-direction:column; align-items:center; }
  .hl-nav-links { display:none; }
  .hl-cta-block { padding:48px 24px; }
  .hl-template-grid { grid-template-columns:1fr 1fr 1fr 1fr; }
  .hl-template-thumb { aspect-ratio: auto; height:60px; }
}
""")
local_css(css)

# ---------------------- Scroll Progress Indicator ----------------------
st.markdown("""
<div class="scroll-indicator" id="scrollIndicator"></div>
<div class="parallax-bg">
  <div class="floating-element">🚀</div>
  <div class="floating-element">⭐</div>
  <div class="floating-element">💼</div>
  <div class="floating-element">📊</div>
APP_URL = "https://hirelyzer-6ebkwzigpyt6rnvsb39bjo.streamlit.app/"

# ──────────────────────────────────────────────
# INLINE SVG ICONS
# ──────────────────────────────────────────────
def icon_resume():
    return """<svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="3" y="2" width="14" height="18" rx="2.5" stroke="#0a84ff" stroke-width="1.5"/>
<rect x="21" y="2" width="0" height="0"/>
<path d="M7 7h7M7 11h7M7 15h4" stroke="#0a84ff" stroke-width="1.5" stroke-linecap="round"/>
</svg>"""

def icon_sparkle():
    return """<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z" fill="#0a84ff"/>
<path d="M19 15L19.9 17.1L22 18L19.9 18.9L19 21L18.1 18.9L16 18L18.1 17.1L19 15Z" fill="#0a84ff" opacity=".6"/>
</svg>"""

def icon_arrow():
    return """<svg width="16" height="16" viewBox="0 0 24 24" fill="none">
<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

def icon_check():
    return """<svg width="14" height="14" viewBox="0 0 24 24" fill="none">
<path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# Step icons
def svg_upload():
    return """<svg class="hl-step-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="40" height="40" rx="12" fill="rgba(10,132,255,0.1)"/>
<path d="M20 26V18M20 18L17 21M20 18L23 21" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M14 28h12" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round"/>
<rect x="12" y="12" width="16" height="18" rx="3" stroke="#0a84ff" stroke-width="1.4" stroke-dasharray="3 2"/>
</svg>"""

def svg_analyze():
    return """<svg class="hl-step-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="40" height="40" rx="12" fill="rgba(48,209,88,0.1)"/>
<circle cx="20" cy="20" r="8" stroke="#30d158" stroke-width="1.5"/>
<path d="M20 16v4l3 2" stroke="#30d158" stroke-width="1.5" stroke-linecap="round"/>
<path d="M25.66 25.66l3 3" stroke="#30d158" stroke-width="1.6" stroke-linecap="round"/>
</svg>"""

def svg_build():
    return """<svg class="hl-step-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="40" height="40" rx="12" fill="rgba(191,90,242,0.1)"/>
<rect x="12" y="12" width="16" height="18" rx="3" stroke="#bf5af2" stroke-width="1.5"/>
<path d="M16 17h8M16 20.5h8M16 24h5" stroke="#bf5af2" stroke-width="1.4" stroke-linecap="round"/>
<circle cx="28" cy="13" r="4" fill="#bf5af2"/>
<path d="M26.5 13l1 1 2-2" stroke="#fff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

def svg_launch():
    return """<svg class="hl-step-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="40" height="40" rx="12" fill="rgba(255,159,10,0.1)"/>
<path d="M20 26c-3.31 0-6-2.69-6-6 0-4 3-8 6-9 3 1 6 5 6 9 0 3.31-2.69 6-6 6z" stroke="#ff9f0a" stroke-width="1.5"/>
<circle cx="20" cy="20" r="2" fill="#ff9f0a"/>
<path d="M28 12l-2 2M12 12l2 2M28 28l-2-2M12 28l2-2" stroke="#ff9f0a" stroke-width="1.4" stroke-linecap="round"/>
</svg>"""

# Feature story icons
def svg_ats_icon():
    return """<svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="48" height="48" rx="14" fill="rgba(10,132,255,0.1)"/>
<path d="M16 14h16v20H16z" stroke="#0a84ff" stroke-width="1.5" rx="3" ry="3"/>
<path d="M20 19h8M20 22.5h8M20 26h5" stroke="#0a84ff" stroke-width="1.3" stroke-linecap="round"/>
<path d="M30 30l5 5" stroke="#30d158" stroke-width="1.8" stroke-linecap="round"/>
<circle cx="30" cy="29" r="4" stroke="#30d158" stroke-width="1.5"/>
</svg>"""

def svg_bias_icon():
    return """<svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="48" height="48" rx="14" fill="rgba(191,90,242,0.1)"/>
<circle cx="24" cy="24" r="9" stroke="#bf5af2" stroke-width="1.5"/>
<path d="M24 15v18M15 24h18" stroke="#bf5af2" stroke-width="1.3" stroke-linecap="round" opacity=".4"/>
<path d="M21 21h2.5a1.5 1.5 0 010 3H21m0-3v6m0-6h3m0 6h-3" stroke="#bf5af2" stroke-width="1.4" stroke-linecap="round"/>
</svg>"""

def svg_builder_icon():
    return """<svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="48" height="48" rx="14" fill="rgba(48,209,88,0.1)"/>
<rect x="14" y="13" width="13" height="17" rx="2.5" stroke="#30d158" stroke-width="1.5"/>
<rect x="20" y="18" width="14" height="17" rx="2.5" fill="rgba(48,209,88,.12)" stroke="#30d158" stroke-width="1.5"/>
<path d="M23 22h8M23 25.5h8M23 29h5" stroke="#30d158" stroke-width="1.3" stroke-linecap="round"/>
</svg>"""

def svg_job_icon():
    return """<svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="48" height="48" rx="14" fill="rgba(255,159,10,0.1)"/>
<rect x="13" y="20" width="22" height="15" rx="3" stroke="#ff9f0a" stroke-width="1.5"/>
<path d="M20 20v-3a1 1 0 011-1h6a1 1 0 011 1v3" stroke="#ff9f0a" stroke-width="1.5"/>
<path d="M13 26h22" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/>
<path d="M20 26v2h8v-2" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/>
</svg>"""

def svg_interview_icon():
    return """<svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="48" height="48" rx="14" fill="rgba(255,69,58,0.08)"/>
<path d="M14 17h14a2 2 0 012 2v8a2 2 0 01-2 2h-2l-3 4-3-4h-4a2 2 0 01-2-2v-8a2 2 0 012-2z" stroke="#ff453a" stroke-width="1.5"/>
<path d="M18 22h6M18 25h4" stroke="#ff453a" stroke-width="1.3" stroke-linecap="round"/>
<circle cx="32" cy="29" r="5" fill="rgba(48,209,88,0.15)" stroke="#30d158" stroke-width="1.4"/>
<path d="M30 29l1.5 1.5 2.5-3" stroke="#30d158" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# ATS ring SVG
def svg_ats_ring(score=78):
    r = 38; cx = cy = 48; stroke_w = 5
    circ = 2 * 3.14159 * r
    fill = (score/100) * circ
    return f"""<svg width="96" height="96" viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="{cx}" cy="{cy}" r="{r}" stroke="rgba(255,255,255,0.06)" stroke-width="{stroke_w}"/>
<circle cx="{cx}" cy="{cy}" r="{r}" stroke="url(#atsGrad)" stroke-width="{stroke_w}"
  stroke-dasharray="{fill:.1f} {circ:.1f}" stroke-dashoffset="{circ*0.25:.1f}"
  stroke-linecap="round"/>
<defs>
<linearGradient id="atsGrad" x1="0" y1="0" x2="96" y2="96" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#30d158"/>
<stop offset="100%" stop-color="#0a84ff"/>
</linearGradient>
</defs>
</svg>"""

# Radar SVG for interview
def svg_radar():
    import math
    categories = ["Communication","Technical","Confidence","Structure","Examples"]
    scores     = [0.82, 0.74, 0.88, 0.70, 0.78]
    cx, cy, R  = 100, 100, 70
    n = len(categories)
    def pt(i, frac):
        angle = math.pi/2 + 2*math.pi*i/n
        x = cx + R*frac*math.cos(angle)
        y = cy - R*frac*math.sin(angle)
        return x, y
    # grid rings
    grid = ""
    for level in [0.25,0.5,0.75,1.0]:
        pts = " ".join(f"{pt(i,level)[0]:.1f},{pt(i,level)[1]:.1f}" for i in range(n))
        grid += f'<polygon points="{pts}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
    # axes
    axes = ""
    for i in range(n):
        x,y = pt(i,1)
        axes += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
    # data polygon
    data_pts = " ".join(f"{pt(i,scores[i])[0]:.1f},{pt(i,scores[i])[1]:.1f}" for i in range(n))
    # labels
    labels = ""
    for i,cat in enumerate(categories):
        x,y = pt(i,1.22)
        labels += f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="middle" fill="rgba(245,245,247,0.45)" font-size="8" font-family="Sora,sans-serif" font-weight="500">{cat}</text>'
    # dots
    dots = ""
    for i in range(n):
        x,y = pt(i,scores[i])
        dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#0a84ff"/>'

    return f"""<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
{grid}{axes}
<polygon points="{data_pts}" fill="rgba(10,132,255,0.15)" stroke="#0a84ff" stroke-width="1.5"/>
{dots}{labels}
</svg>"""

# ──────────────────────────────────────────────
# RENDER
# ──────────────────────────────────────────────

st.markdown('<div id="sp"></div>', unsafe_allow_html=True)

# ── NAV ──
st.markdown(f"""
<div class="hl-nav">
  <div class="hl-nav-inner">
    <a href="#" class="hl-logo">
      <div class="hl-logo-mark">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"
            stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      HIRELYZER
    </a>
    <div class="hl-nav-links">
      <a href="#how">How it works</a>
      <a href="#analyzer">Analyzer</a>
      <a href="#builder">Builder</a>
      <a href="#career">Career Hub</a>
      <a href="#contact">Contact</a>
    </div>
    <a href="{APP_URL}" target="_blank" class="hl-nav-cta">
      {icon_sparkle()} Open App
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------- Enhanced Top Nav ----------------------
st.markdown("""
<div class='nav-container'>
<div style='display:flex;justify-content:space-between;align-items:center;padding:16px 24px;max-width:1200px;margin:0 auto;'>
  <div style='display:flex;align-items:center;gap:16px' class='logo-container'>
    <div style='width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,#ff6a88,#5f2c82);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:20px;box-shadow:0 8px 20px rgba(79,70,229,0.3)'>HL</div>
    <div style='font-weight:800;font-size:18px'>HIRELYZER</div>
# ── HERO ──
st.markdown(f"""
<div class="hl-hero">
  <div class="hl-eyebrow">
    <svg width="12" height="12" viewBox="0 0 12 12" fill="#0a84ff"><circle cx="6" cy="6" r="6"/></svg>
    AI-Powered Career Intelligence
  </div>
  <div style='display:flex;gap:32px;align-items:center'>
    <a href='#features' class='nav-link' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600;font-size:15px'>Features</a>
    <a href='#pricing' class='nav-link' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600;font-size:15px'>Pricing</a>
    <a href='#contact' class='nav-link' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600;font-size:15px'>Contact</a>
    <a href="https://hirelyzer-6ebkwzigpyt6rnvsb39bjo.streamlit.app/" target="_blank" class='btn' style='text-decoration:none'>
      🚀 Open App
  <h1 class="hl-h1">The last resume tool<br>you'll ever <em>need</em></h1>
  <p class="hl-hero-sub">
    Upload your resume. Hirelyzer instantly scores it for ATS compatibility,
    detects bias, rewrites it with AI, and connects you to jobs — all in one place.
  </p>
  <div class="hl-hero-ctas">
    <a href="{APP_URL}" target="_blank" class="hl-btn-primary">
      {icon_sparkle()} Get Started Free
    </a>
    <a href="#how" class="hl-btn-ghost">
      See how it works {icon_arrow()}
    </a>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

# ---------------------- Enhanced Hero Section ----------------------
hero_html = """
<div style='max-width:1200px;margin:40px auto;padding:0 20px'>
<div class='hero'>
  <div class='hero-left'>
    <div class='h-eyebrow'>🤖 AI-Powered Career Tools · ⚡ Instant · 🎯 Insightful</div>
    <div class='h-title'>Make Resumes that Pass — and People who Hire.</div>
    <div class='h-sub'><span class='typewriter'><span id='typewriter' class='typewriter-text'></span></span></div>
    <div class='cta-row'>
      <a href="https://hirelyzer-6ebkwzigpyt6rnvsb39bjo.streamlit.app/" target="_blank" class='btn'>
        ✨ Launch App
      </a>
      <a href='#pricing' class='btn secondary'>
        💎 View Plans
      </a>
  <div class="hl-hero-card">
    <div class="hl-card-bar">
      <div class="hl-dot" style="background:#ff5f57"></div>
      <div class="hl-dot" style="background:#febc2e"></div>
      <div class="hl-dot" style="background:#28c840"></div>
      <span style="margin-left:8px;font-size:11px;color:var(--muted2);font-family:var(--mono)">hirelyzer — resume_analysis.pdf</span>
    </div>
  </div>
  <div class='hero-right'>
    <div class='ats-preview'>
      <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:20px'>
        <div style='font-weight:800;font-size:16px;color:rgba(255,255,255,0.95)'>🎯 Live ATS Preview</div>
        <div style='font-size:12px;color:rgba(255,255,255,0.6);background:rgba(0,255,0,0.1);padding:4px 8px;border-radius:12px;border:1px solid rgba(0,255,0,0.2)'>● LIVE</div>
      </div>
      <div style='background:rgba(255,255,255,0.03);padding:20px;border-radius:14px;border:1px solid rgba(255,255,255,0.05)'>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin-bottom:12px'>📄 Resume: <b style='color:rgba(255,255,255,0.95)'>John Doe — Backend Engineer</b></div>
        <div style='display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px'>
          <div class='skill-tag' style='padding:8px 12px;border-radius:20px;background:rgba(79,70,229,0.2);font-size:12px;font-weight:600;border:1px solid rgba(79,70,229,0.3)'>Python</div>
          <div class='skill-tag' style='padding:8px 12px;border-radius:20px;background:rgba(34,197,94,0.2);font-size:12px;font-weight:600;border:1px solid rgba(34,197,94,0.3)'>Django</div>
          <div class='skill-tag' style='padding:8px 12px;border-radius:20px;background:rgba(59,130,246,0.2);font-size:12px;font-weight:600;border:1px solid rgba(59,130,246,0.3)'>PostgreSQL</div>
    <div class="hl-card-body">
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">
        <div>
          <div class="hl-panel-title">
            <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#30d158"/></svg>
            ATS Score
          </div>
          <div class="hl-score-ring-wrap">
            {svg_ats_ring(78)}
            <div>
              <div class="hl-score-val">78</div>
              <div class="hl-score-sub">out of 100</div>
            </div>
          </div>
          <div class="hl-bar-row">
            <div class="hl-bar-item">
              <div class="hl-bar-label"><span>Format</span><span style="color:var(--accent2)">92%</span></div>
              <div class="hl-bar-track"><div class="hl-bar-fill" style="width:92%;background:#30d158"></div></div>
            </div>
            <div class="hl-bar-item">
              <div class="hl-bar-label"><span>Keywords</span><span style="color:#ff9f0a">71%</span></div>
              <div class="hl-bar-track"><div class="hl-bar-fill" style="width:71%;background:#ff9f0a"></div></div>
            </div>
            <div class="hl-bar-item">
              <div class="hl-bar-label"><span>Sections</span><span style="color:var(--accent)">85%</span></div>
              <div class="hl-bar-track"><div class="hl-bar-fill" style="width:85%;background:#0a84ff"></div></div>
            </div>
          </div>
        </div>
        <div style='display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-top:1px solid rgba(255,255,255,0.05)'>
          <div style='font-size:13px;color:rgba(255,255,255,0.7)'>🎯 ATS Score</div>
          <div style='font-weight:900;font-size:24px;background:linear-gradient(135deg,#10b981,#3b82f6);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent'>78%</div>
        <div>
          <div class="hl-panel-title">
            <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#bf5af2"/></svg>
            Bias Analysis
          </div>
          <div style="margin-bottom:12px">
            <div style="font-size:11px;color:var(--muted2);margin-bottom:8px;font-weight:500">FLAGGED WORDS</div>
            <div class="hl-word-row">
              <span class="hl-word-chip hl-chip-m">driven</span>
              <span class="hl-word-chip hl-chip-m">dominate</span>
              <span class="hl-word-chip hl-chip-f">nurture</span>
              <span class="hl-word-chip hl-chip-m">aggressive</span>
              <span class="hl-word-chip hl-chip-n">deliver</span>
              <span class="hl-word-chip hl-chip-n">execute</span>
            </div>
          </div>
          <div style="padding:10px 12px;background:rgba(191,90,242,0.08);border-radius:10px;border:1px solid rgba(191,90,242,0.18)">
            <div style="font-size:11px;font-weight:600;color:#d07ef7;margin-bottom:4px">AI Suggestion</div>
            <div style="font-size:11px;color:var(--muted);line-height:1.6">Replace "aggressive growth" with "high-impact results" to reduce masculine bias signal.</div>
          </div>
        </div>
        <div style='width:100%;height:6px;background:rgba(255,255,255,0.1);border-radius:3px;margin-top:8px;overflow:hidden'>
          <div style='width:78%;height:100%;background:linear-gradient(90deg,#10b981,#3b82f6);border-radius:3px;animation:pulse 2s ease-in-out infinite'></div>
        <div>
          <div class="hl-panel-title">
            <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#ff9f0a"/></svg>
            Quick Actions
          </div>
          <div style="display:flex;flex-direction:column;gap:8px">
            <div style="padding:10px 12px;background:rgba(48,209,88,0.08);border-radius:10px;border:1px solid rgba(48,209,88,0.18);display:flex;align-items:center;gap:8px">
              {icon_check()}<span style="font-size:12px;color:var(--accent2);font-weight:600">Single-column layout</span>
            </div>
            <div style="padding:10px 12px;background:rgba(48,209,88,0.08);border-radius:10px;border:1px solid rgba(48,209,88,0.18);display:flex;align-items:center;gap:8px">
              {icon_check()}<span style="font-size:12px;color:var(--accent2);font-weight:600">Contact info present</span>
            </div>
            <div style="padding:10px 12px;background:rgba(255,159,10,0.08);border-radius:10px;border:1px solid rgba(255,159,10,0.18);display:flex;align-items:center;gap:8px">
              <svg width="14" height="14" viewBox="0 0 24 24"><path d="M12 8v4m0 4h.01M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>
              <span style="font-size:12px;color:#ff9f0a;font-weight:600">Add LinkedIn URL</span>
            </div>
            <div style="padding:10px 12px;background:rgba(255,69,58,0.08);border-radius:10px;border:1px solid rgba(255,69,58,0.18);display:flex;align-items:center;gap:8px">
              <svg width="14" height="14" viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg>
              <span style="font-size:12px;color:#ff453a;font-weight:600">No skills section</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="hl-stat-row">
    <div class="hl-stat"><div class="hl-stat-n">15+</div><div class="hl-stat-l">Resume Templates</div></div>
    <div class="hl-stat"><div class="hl-stat-n">4</div><div class="hl-stat-l">Core Modules</div></div>
    <div class="hl-stat"><div class="hl-stat-n">AI</div><div class="hl-stat-l">Powered by LLM</div></div>
    <div class="hl-stat"><div class="hl-stat-n">Free</div><div class="hl-stat-l">No credit card</div></div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

<script>
const phrases = [
  '🚀 Upload your resume — get ATS-ready feedback in seconds.',
  '✍️ Rewrite bullets for impact. Fix grammar & bias automatically.',
  '🔍 Discover jobs, recommended courses, and salary insights.'
];
let idx=0;const el=document.getElementById('typewriter');
function show(){
  const txt = phrases[idx];
  let i=0;el.innerText='';
  const t = setInterval(()=>{
    el.innerText += txt[i++];
    if(i>txt.length-1){
      clearInterval(t);
      setTimeout(()=>{ idx=(idx+1)%phrases.length; show(); },3000);
    }
  },30);
}
if(el) show();

// Scroll progress indicator
window.addEventListener('scroll', () => {
  const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
  document.getElementById('scrollIndicator').style.width = scrolled + '%';
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
</script>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ---------------------- Enhanced Features Section ----------------------
features_html = """
<div id='features' style='padding:80px 20px;max-width:1200px;margin:0 auto'>
  <h2 class='section-title' style='font-size:48px;font-weight:900;margin-bottom:16px;text-align:center'>🚀 Powerful Features</h2>
  <p style='text-align:center;color:rgba(255,255,255,0.7);font-size:18px;margin-bottom:48px;max-width:600px;margin-left:auto;margin-right:auto'>Everything you need to create winning resumes and land your dream job</p>
  <div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:28px'>
    <div class='feature-card'>
      <div style='font-size:32px;margin-bottom:8px'>📄</div>
      <div class='feature-title'>AI Resume Analyzer</div>
      <div class='feature-desc'>Upload your resume and instantly receive comprehensive ATS scoring with AI-powered feedback for keywords, grammar, formatting, and bias detection to maximize your chances.</div>
      <div style='margin-top:16px;padding:12px;background:rgba(79,70,229,0.1);border-radius:8px;border-left:3px solid #4f46e5'>
        <div style='font-size:12px;color:rgba(255,255,255,0.8);font-weight:600'>✨ AI-Powered Analysis</div>
# ── HOW IT WORKS ──
st.markdown(f"""
<div id="how" style="padding:100px 0 60px">
  <div class="hl-section">
    <div class="hl-section-label">How it works</div>
    <div class="hl-steps">
      <div class="hl-step">
        <span class="hl-step-n">01</span>
        {svg_upload()}
        <div class="hl-step-title">Upload your resume</div>
        <div class="hl-step-desc">Drop any PDF. Our parser handles messy formats, multi-column layouts, and scanned documents via OCR fallback.</div>
      </div>
    </div>
    <div class='feature-card'>
      <div style='font-size:32px;margin-bottom:8px'>📝</div>
      <div class='feature-title'>Smart Resume Builder</div>
      <div class='feature-desc'>Create professional resumes and cover letters using modern, ATS-friendly templates. Generate tailored content with AI assistance and export in multiple formats (PDF, DOCX).</div>
      <div style='margin-top:16px;padding:12px;background:rgba(34,197,94,0.1);border-radius:8px;border-left:3px solid #22c55e'>
        <div style='font-size:12px;color:rgba(255,255,255,0.8);font-weight:600'>🎨 Professional Templates</div>
      <div class="hl-step">
        <span class="hl-step-n">02</span>
        {svg_analyze()}
        <div class="hl-step-title">Instant AI analysis</div>
        <div class="hl-step-desc">ATS scoring, bias detection, grammar check, keyword matching — all computed in seconds with detailed per-section feedback.</div>
      </div>
      <div class="hl-step">
        <span class="hl-step-n">03</span>
        {svg_build()}
        <div class="hl-step-title">Build or rewrite</div>
        <div class="hl-step-desc">Use the AI rewriter or open the full Resume Builder. Choose from 15 templates, generate a cover letter, export to PDF or DOCX.</div>
      </div>
      <div class="hl-step">
        <span class="hl-step-n">04</span>
        {svg_launch()}
        <div class="hl-step-title">Apply with confidence</div>
        <div class="hl-step-desc">Discover live job listings, salary benchmarks, curated courses, and practice with the AI Interview Coach before submitting.</div>
      </div>
    </div>
    <div class='feature-card'>
      <div style='font-size:32px;margin-bottom:8px'>🔍</div>
      <div class='feature-title'>Career Intelligence Hub</div>
      <div class='feature-desc'>Explore curated job opportunities, access real-time salary benchmarks, and discover personalized course recommendations perfectly aligned with your career goals and aspirations.</div>
      <div style='margin-top:16px;padding:12px;background:rgba(59,130,246,0.1);border-radius:8px;border-left:3px solid #3b82f6'>
        <div style='font-size:12px;color:rgba(255,255,255,0.8);font-weight:600'>📊 Market Insights</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STORY 1: ATS ANALYZER ──
st.markdown(f"""
<div id="analyzer" class="hl-story">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div>
        <div class="hl-story-number">Feature 01 — Resume Analyzer</div>
        <h2 class="hl-story-heading">Your resume, <span>scored like a machine</span> reads it</h2>
        <p class="hl-story-body">
          Most resumes never reach a human. Applicant Tracking Systems silently filter them out
          on format, missing keywords, or structural issues. Hirelyzer's analyzer replicates
          exactly how ATS parsers — Workday, Greenhouse, Lever — evaluate your document.
        </p>
        <p class="hl-story-body">
          Every section, every bullet, every date format is weighed against real hiring criteria.
          You see a precise score, a list of passes and failures, and an AI-written action plan
          to close the gap.
        </p>
        <div class="hl-story-pills">
          <span class="hl-pill">ATS Scoring</span>
          <span class="hl-pill">Section Detection</span>
          <span class="hl-pill">Action Verb Check</span>
          <span class="hl-pill">Format Audit</span>
          <span class="hl-pill">Multi-resume Compare</span>
        </div>
      </div>
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title">
            {svg_ats_icon()}
            <span style="margin-left:8px">Live ATS Breakdown</span>
          </div>
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:24px">
            {svg_ats_ring(78)}
            <div>
              <div style="font-size:11px;color:var(--muted2);font-weight:500;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px">Overall</div>
              <div style="font-size:38px;font-weight:800;color:var(--text);letter-spacing:-2px;line-height:1">78</div>
              <div style="font-size:12px;color:var(--accent2);font-weight:600;margin-top:4px">Good · Minor fixes needed</div>
            </div>
          </div>
          <div class="hl-bar-row" style="gap:12px">
            {"".join(f'''
            <div class="hl-bar-item">
              <div class="hl-bar-label"><span>{cat}</span><span style="color:{col}">{pct}%</span></div>
              <div class="hl-bar-track"><div class="hl-bar-fill" style="width:{pct}%;background:{col}"></div></div>
            </div>''' for cat,pct,col in [
              ("Format & Layout",92,"#30d158"),
              ("Keyword Coverage",71,"#ff9f0a"),
              ("Sections Present",85,"#0a84ff"),
              ("Action Verbs",68,"#ff9f0a"),
              ("Contact Info",100,"#30d158"),
              ("Date Consistency",80,"#0a84ff"),
            ])}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""
st.markdown(features_html, unsafe_allow_html=True)

# ---------------------- Enhanced Pricing Section ----------------------
pricing_html = """
<div id='pricing' style='padding:80px 20px;background:linear-gradient(135deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));backdrop-filter:blur(20px);border-radius:24px;margin:40px 20px;border:1px solid rgba(255,255,255,0.05);max-width:1200px;margin-left:auto;margin-right:auto'>
  <h2 class='section-title' style='font-size:48px;font-weight:900;margin-bottom:16px;text-align:center'>💎 Choose Your Plan</h2>
  <p style='text-align:center;color:rgba(255,255,255,0.7);font-size:18px;margin-bottom:48px'>Start free, upgrade when you're ready to accelerate your career</p>
  <div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;max-width:1000px;margin:0 auto'>
    <div class='feature-card' style='text-align:center;padding:32px'>
      <div style='font-size:24px;font-weight:800;margin-bottom:8px'>🆓 Free</div>
      <div style='font-size:15px;color:rgba(255,255,255,0.7);margin-bottom:20px;line-height:1.5'>Perfect for getting started with basic ATS scoring and resume analysis</div>
      <div style='font-size:36px;font-weight:900;margin:20px 0;background:linear-gradient(135deg,#10b981,#3b82f6);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent'>$0</div>
      <div style='font-size:14px;color:rgba(255,255,255,0.6);margin-bottom:24px'>Forever free</div>
      <button class='btn secondary' style='width:100%'>🚀 Get Started</button>
      <div style='margin-top:20px;text-align:left'>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Basic ATS scoring</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Grammar check</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ 3 resume uploads/month</div>
""", unsafe_allow_html=True)

# ── STORY 2: BIAS DETECTION ──
st.markdown(f"""
<div class="hl-story" style="background:var(--bg1)">
  <div class="hl-section">
    <div class="hl-story-grid reverse">
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title">
            {svg_bias_icon()}
            <span style="margin-left:8px">Bias Detection Report</span>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px">
            <div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.14)">
              <div style="font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted2);font-weight:600;margin-bottom:6px">Masculine</div>
              <div style="font-size:24px;font-weight:800;color:#4db3ff">8</div>
              <div style="font-size:11px;color:var(--muted2)">words flagged</div>
            </div>
            <div style="padding:14px;background:rgba(191,90,242,0.06);border-radius:12px;border:1px solid rgba(191,90,242,0.14)">
              <div style="font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted2);font-weight:600;margin-bottom:6px">Feminine</div>
              <div style="font-size:24px;font-weight:800;color:#d07ef7">3</div>
              <div style="font-size:11px;color:var(--muted2)">words flagged</div>
            </div>
          </div>
          <div style="margin-bottom:16px">
            <div style="font-size:11px;color:var(--muted2);font-weight:500;margin-bottom:10px;text-transform:uppercase;letter-spacing:.8px">Detected language</div>
            <div class="hl-word-row">
              {"".join(f'<span class="hl-word-chip hl-chip-m">{w}</span>' for w in ["driven","aggressive","dominate","champion","spearhead","force"])}
              {"".join(f'<span class="hl-word-chip hl-chip-f">{w}</span>' for w in ["nurture","support","help"])}
              {"".join(f'<span class="hl-word-chip hl-chip-n">{w}</span>' for w in ["deliver","execute","build"])}
            </div>
          </div>
          <div style="padding:14px;background:rgba(48,209,88,0.06);border-radius:12px;border:1px solid rgba(48,209,88,0.14)">
            <div style="font-size:11px;font-weight:700;color:var(--accent2);margin-bottom:6px">
              {icon_check()} AI Rewrite Applied
            </div>
            <div style="font-size:12px;color:var(--muted);line-height:1.65">
              <span style="text-decoration:line-through;opacity:.5">Aggressively drove</span>
              → <span style="color:var(--accent2)">Accelerated</span> product delivery across 3 teams
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="hl-story-number">Feature 02 — Bias Detection</div>
        <h2 class="hl-story-heading">Language that <span>closes doors</span> — detected and replaced</h2>
        <p class="hl-story-body">
          Decades of research show that gendered language in resumes affects hiring outcomes.
          Words coded as "masculine" or "feminine" unconsciously signal culture fit to
          recruiters — and the wrong signals filter you out before the first call.
        </p>
        <p class="hl-story-body">
          Hirelyzer identifies every biased word, scores your overall language balance,
          and rewrites your resume with neutral, high-impact alternatives using a curated
          replacement lexicon built from real hiring data.
        </p>
        <div class="hl-story-pills">
          <span class="hl-pill">Gender-coded word detection</span>
          <span class="hl-pill">Bias score 0–100</span>
          <span class="hl-pill">LLM rewrite</span>
          <span class="hl-pill">Highlighted diff</span>
          <span class="hl-pill">Side-by-side compare</span>
        </div>
      </div>
    </div>
    <div class='feature-card pricing-card-featured' style='text-align:center;padding:32px;border:2px solid rgba(79,70,229,0.3);transform:scale(1.05)'>
      <div style='font-size:24px;font-weight:800;margin-bottom:8px'>⭐ Pro</div>
      <div style='font-size:15px;color:rgba(255,255,255,0.7);margin-bottom:20px;line-height:1.5'>Complete resume builder with AI rewrites, advanced analytics, and job insights</div>
      <div style='font-size:36px;font-weight:900;margin:20px 0;background:linear-gradient(135deg,#ff6a88,#5f2c82);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent'>$9</div>
      <div style='font-size:14px;color:rgba(255,255,255,0.6);margin-bottom:24px'>per month</div>
      <button class='btn' style='width:100%'>🎯 Choose Pro</button>
      <div style='margin-top:20px;text-align:left'>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Everything in Free</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ AI-powered rewrites</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Premium templates</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Job market insights</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Unlimited uploads</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STORY 3: RESUME BUILDER ──
templates = [
    ("Modern",True), ("Minimal",False), ("Executive",False), ("Timeline",False),
    ("Corporate",False), ("Creative",False), ("Navy",False), ("Teal",False),
]
template_cards = ""
for name, active in templates:
    cls = "hl-template-thumb" + (" hl-thumb-active" if active else "")
    badge = f'<div class="hl-thumb-badge">{name}</div>' if active else ""
    lines = "".join(f'<div class="ts" style="height:3px;background:var(--border);border-radius:1.5px;width:{w}%"></div>' for w in [70,55,90,40,75,60])
    template_cards += f"""
<div class="{cls}">
  <div class="tl"></div>
  <div style="height:4px;border-radius:2px;background:{"var(--accent)" if active else "var(--border2)"};width:50%;margin-bottom:4px"></div>
  {lines}
  {badge}
</div>"""

st.markdown(f"""
<div id="builder" class="hl-story">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div>
        <div class="hl-story-number">Feature 03 — Resume Builder</div>
        <h2 class="hl-story-heading">Build resumes that <span>look as good</span> as they parse</h2>
        <p class="hl-story-body">
          Fifteen ATS-optimised templates — from understated minimal to executive prestige —
          all built on strict single-column structures that parse correctly in every major
          hiring platform. Choose a style, fill your details, and our AI enhances every
          section with no-repetition language rules enforced across the entire document.
        </p>
        <p class="hl-story-body">
          Export to DOCX (three ATS compliance levels) or PDF. Need a cover letter?
          One click generates a tailored letter for your target company, formatted and
          ready to send.
        </p>
        <div class="hl-story-pills">
          <span class="hl-pill">15 templates</span>
          <span class="hl-pill">DOCX + PDF export</span>
          <span class="hl-pill">AI cover letter</span>
          <span class="hl-pill">Live preview</span>
          <span class="hl-pill">ATS single-column</span>
        </div>
      </div>
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title">
            {svg_builder_icon()}
            <span style="margin-left:8px">Template Gallery — 15 Designs</span>
          </div>
          <div class="hl-template-grid">{template_cards}</div>
          <div style="margin-top:16px;padding:14px;background:rgba(48,209,88,0.06);border-radius:12px;border:1px solid rgba(48,209,88,0.14);display:flex;align-items:center;justify-content:space-between">
            <div>
              <div style="font-size:12px;font-weight:700;color:var(--accent2)">Modern — ATS Certified</div>
              <div style="font-size:11px;color:var(--muted2);margin-top:2px">Calibri · Navy headings · Single-column</div>
            </div>
            <a href="{APP_URL}" target="_blank" style="padding:8px 16px;background:var(--accent);color:#fff;border-radius:980px;font-size:12px;font-weight:600;text-decoration:none">Use this</a>
          </div>
        </div>
      </div>
    </div>
    <div class='feature-card' style='text-align:center;padding:32px'>
      <div style='font-size:24px;font-weight:800;margin-bottom:8px'>🏢 Enterprise</div>
      <div style='font-size:15px;color:rgba(255,255,255,0.7);margin-bottom:20px;line-height:1.5'>Advanced tools for recruiters and teams with bulk hiring and analytics</div>
      <div style='font-size:36px;font-weight:900;margin:20px 0;background:linear-gradient(135deg,#f59e0b,#ef4444);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent'>Custom</div>
      <div style='font-size:14px;color:rgba(255,255,255,0.6);margin-bottom:24px'>Contact for pricing</div>
      <button class='btn secondary' style='width:100%'>📞 Contact Sales</button>
      <div style='margin-top:20px;text-align:left'>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Everything in Pro</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Team management</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Bulk processing</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Custom integrations</div>
        <div style='font-size:13px;color:rgba(255,255,255,0.7);margin:8px 0'>✅ Priority support</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STORY 4: JOB SEARCH ──
jobs = [
    ("SDE","Google","Mountain View · Full-time","#4285f4","G",True),
    ("ML Engineer","Anthropic","Remote · Full-time","#d97706","A",False),
    ("Backend Dev","Razorpay","Bangalore · Full-time","#2563eb","R",False),
    ("Data Analyst","Zepto","Mumbai · Hybrid","#7c3aed","Z",False),
]

job_cards = ""
for title, co, meta, color, letter, featured in jobs:
    badge_bg = "rgba(10,132,255,0.12)" if featured else "rgba(255,255,255,0.05)"
    badge_col = "#4db3ff" if featured else "var(--muted2)"
    badge_txt = "Featured" if featured else "New"
    job_cards += f"""
<div class="hl-job-card">
  <div class="hl-job-logo" style="background:{color}20;color:{color}">{letter}</div>
  <div class="hl-job-meta">
    <div class="hl-job-title">{title} — {co}</div>
    <div class="hl-job-co">{meta}</div>
  </div>
  <div class="hl-job-badge" style="background:{badge_bg};color:{badge_col};border:1px solid {badge_col}40">{badge_txt}</div>
</div>"""

st.markdown(f"""
<div id="career" class="hl-story" style="background:var(--bg1)">
  <div class="hl-section">
    <div class="hl-story-grid reverse">
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title">
            {svg_job_icon()}
            <span style="margin-left:8px">Job Search Hub</span>
          </div>
          <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:20px">
            {job_cards}
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
            <div style="padding:12px;background:rgba(255,159,10,0.06);border-radius:10px;border:1px solid rgba(255,159,10,0.14)">
              <div style="font-size:10px;color:var(--muted2);text-transform:uppercase;letter-spacing:.8px;font-weight:600;margin-bottom:4px">Avg Salary</div>
              <div style="font-size:20px;font-weight:800;color:#ff9f0a">₹18–32 LPA</div>
              <div style="font-size:11px;color:var(--muted2)">Backend Engineering · India</div>
            </div>
            <div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.14)">
              <div style="font-size:10px;color:var(--muted2);text-transform:uppercase;letter-spacing:.8px;font-weight:600;margin-bottom:4px">Platform</div>
              <div style="font-size:14px;font-weight:700;color:var(--text);margin-top:4px;line-height:1.5">LinkedIn · Naukri<br>Foundit · Indeed</div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="hl-story-number">Feature 04 — Career Intelligence</div>
        <h2 class="hl-story-heading">Jobs, salaries, courses — <span>one place</span></h2>
        <p class="hl-story-body">
          The Job Search Hub pulls live listings from LinkedIn, Naukri, Foundit, Indeed,
          and Glassdoor — or uses the JSearch/RapidAPI engine for direct listings with
          remote and employment-type filters. Every search is role-aware and
          location-smart.
        </p>
        <p class="hl-story-body">
          Alongside jobs, Hirelyzer surfaces salary benchmarks by role and market,
          curated course recommendations mapped to real skill gaps in your resume,
          and resume/interview preparation videos — all linked to your career profile.
        </p>
        <div class="hl-story-pills">
          <span class="hl-pill">Live job listings</span>
          <span class="hl-pill">Salary benchmarks</span>
          <span class="hl-pill">Course recommendations</span>
          <span class="hl-pill">Skills radar</span>
          <span class="hl-pill">Remote filter</span>
        </div>
      </div>
    </div>
  </div>
</div>
"""
st.markdown(pricing_html, unsafe_allow_html=True)

# ---------------------- Enhanced Contact Section ----------------------
contact_html = """
<div id='contact' style='padding:80px 20px;margin-top:40px;max-width:1200px;margin-left:auto;margin-right:auto'>
  <h2 class='section-title' style='font-size:48px;font-weight:900;margin-bottom:16px;text-align:center'>💬 Get In Touch</h2>
  <div style='max-width:700px;margin:0 auto;text-align:center'>
    <p style='color:rgba(255,255,255,0.7);font-size:18px;margin-bottom:40px;line-height:1.6'>Have questions or need support? Our team is here to help you succeed in your career journey.</p>
    <div style='display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;margin-bottom:40px'>
      <div class='feature-card' style='text-align:center;padding:24px'>
        <div style='font-size:32px;margin-bottom:12px'>📧</div>
        <div style='font-weight:700;margin-bottom:8px'>Email Support</div>
        <a href='mailto:support@hirelyzer.com' style='color:#8ab4f8;text-decoration:none;font-weight:600'>support@hirelyzer.com</a>
""", unsafe_allow_html=True)

# ── STORY 5: AI INTERVIEW COACH ──
st.markdown(f"""
<div class="hl-story">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div>
        <div class="hl-story-number">Feature 05 — AI Interview Coach</div>
        <h2 class="hl-story-heading">Practice until <span>every answer</span> lands</h2>
        <p class="hl-story-body">
          Upload your resume and Hirelyzer generates interview questions derived directly
          from your actual experience — not generic prompts. Answer in free text;
          the AI coach scores you on communication, technical depth, confidence signals,
          structure, and use of concrete examples.
        </p>
        <p class="hl-story-body">
          Every session ends with a performance radar chart, a detailed Q&A review,
          and course recommendations tied to your weakest dimensions. Your progress
          is tracked across sessions with trend charts visible in My Progress.
        </p>
        <div class="hl-story-pills">
          <span class="hl-pill">Resume-based questions</span>
          <span class="hl-pill">Real-time AI scoring</span>
          <span class="hl-pill">Radar performance chart</span>
          <span class="hl-pill">Session history</span>
          <span class="hl-pill">Downloadable report</span>
        </div>
      </div>
      <div class='feature-card' style='text-align:center;padding:24px'>
        <div style='font-size:32px;margin-bottom:12px'>🌐</div>
        <div style='font-weight:700;margin-bottom:8px'>Visit Website</div>
        <a href='https://hirelyzer-6ebkwzigpyt6rnvsb39bjo.streamlit.app/' target='_blank' style='color:#8ab4f8;text-decoration:none;font-weight:600'>https://hirelyzer-ijkfwqydjqz3wqyvjkhegw.streamlit.app/</a>
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title">
            {svg_interview_icon()}
            <span style="margin-left:8px">Mock Interview · Session 3</span>
            <div class="hl-score-badge" style="margin-left:auto">
              <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#30d158"/></svg>
              82 / 100
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
            <div>
              <div class="hl-qa">
                <div class="hl-q">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#0a84ff" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>
                  Describe your most complex backend system.
                </div>
                <div class="hl-a">Built a multi-tenant microservices platform handling 2M events/day using Kafka, Redis, and PostgreSQL. Reduced P99 latency by 40%.</div>
              </div>
              <div class="hl-qa">
                <div class="hl-q">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#bf5af2" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>
                  How do you handle technical debt?
                </div>
                <div class="hl-a">I prioritise tech debt as a first-class roadmap item, quantifying its cost in sprint velocity before pitching refactors to stakeholders.</div>
              </div>
              <div style="margin-top:12px">
                <div style="font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted2);font-weight:600;margin-bottom:8px">Score breakdown</div>
                {"".join(f'''<div style="display:flex;justify-content:space-between;font-size:11px;color:var(--muted);margin-bottom:6px">
                  <span>{dim}</span><span style="color:{col};font-weight:600">{sc}</span></div>
                  <div style="height:3px;background:var(--border);border-radius:2px;margin-bottom:8px;overflow:hidden">
                  <div style="width:{sc};height:100%;background:{col};border-radius:2px"></div></div>'''
                for dim,sc,col in [("Communication","85%","#0a84ff"),("Technical","79%","#bf5af2"),("Confidence","88%","#30d158"),("Structure","74%","#ff9f0a")])}
              </div>
            </div>
            <div style="display:flex;flex-direction:column;align-items:center;justify-content:center">
              {svg_radar()}
              <div style="font-size:11px;color:var(--muted2);text-align:center;margin-top:4px">Performance radar</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div style='padding:32px;background:linear-gradient(135deg,rgba(79,70,229,0.1),rgba(59,130,246,0.05));border-radius:16px;border:1px solid rgba(79,70,229,0.2)'>
      <div style='font-size:18px;font-weight:700;margin-bottom:12px;color:rgba(255,255,255,0.95)'>🚀 Ready to Transform Your Career?</div>
      <p style='color:rgba(255,255,255,0.8);margin-bottom:20px'>Join thousands of professionals who have already upgraded their resumes with HIRELYZER</p>
      <a href="https://hirelyzer-6ebkwzigpyt6rnvsb39bjo.streamlit.app/" target="_blank" class='btn' style='text-decoration:none'>
        ✨ Start Your Journey Now
  </div>
</div>
""", unsafe_allow_html=True)

# ── FINAL CTA ──
st.markdown(f"""
<div class="hl-section">
  <div id="contact" class="hl-cta-block">
    <div class="hl-eyebrow" style="margin:0 auto 28px">
      <svg width="12" height="12" viewBox="0 0 12 12" fill="#0a84ff"><circle cx="6" cy="6" r="6"/></svg>
      Free to use · No credit card required
    </div>
    <div class="hl-cta-heading">Your next job starts with a better resume</div>
    <div class="hl-cta-sub">Join professionals already using Hirelyzer to pass ATS filters, remove bias, and land more interviews.</div>
    <div style="display:flex;gap:14px;justify-content:center;position:relative;z-index:1;flex-wrap:wrap">
      <a href="{APP_URL}" target="_blank" class="hl-btn-primary" style="font-size:16px;padding:16px 36px">
        {icon_sparkle()} Start for free
      </a>
      <a href="mailto:support@hirelyzer.com" class="hl-btn-ghost" style="font-size:16px;padding:16px 32px">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5"/><polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5"/></svg>
        Contact us
      </a>
    </div>
    <div style="margin-top:40px;display:flex;justify-content:center;gap:32px;flex-wrap:wrap">
      {"".join(f'''<div style="display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted2)">
        {icon_check()}<span>{item}</span></div>''' for item in [
        "ATS score in seconds","Bias detection & rewrite","15 resume templates",
        "Cover letter generator","Live job search","AI interview coach"])}
    </div>
  </div>
</div>
<div class='footer'>
  <div style='max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px'>
    <div>© 2025 HIRELYZER. All rights reserved.</div>
    <div style='display:flex;gap:24px'>
      <a href='#' style='color:rgba(255,255,255,0.6);text-decoration:none;font-size:14px'>Privacy Policy</a>
      <a href='#' style='color:rgba(255,255,255,0.6);text-decoration:none;font-size:14px'>Terms of Service</a>
      <a href='#' style='color:rgba(255,255,255,0.6);text-decoration:none;font-size:14px'>Cookie Policy</a>
""", unsafe_allow_html=True)

# ── FOOTER ──
st.markdown(f"""
<footer>
  <div class="hl-footer">
    <div class="hl-footer-logo">
      © 2025 HIRELYZER · Intelligent Career Platform
    </div>
    <div class="hl-footer-links">
      <a href="#">Privacy</a>
      <a href="#">Terms</a>
      <a href="mailto:support@hirelyzer.com">support@hirelyzer.com</a>
      <a href="{APP_URL}" target="_blank">Open App</a>
    </div>
  </div>
</div>
"""
st.markdown(contact_html, unsafe_allow_html=True)
</footer>
""", unsafe_allow_html=True)

# ── JS ──
st.markdown("""
<script>
(function(){
  const sp = document.getElementById('sp');
  if(sp){
    window.addEventListener('scroll', () => {
      const pct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
      sp.style.width = pct + '%';
    }, {passive:true});
  }
  // IntersectionObserver for bar animations
  const bars = document.querySelectorAll('.hl-bar-fill');
  const io = new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.style.transition='width 1.2s cubic-bezier(.4,0,.2,1)';
        io.unobserve(e.target);
      }
    });
  },{threshold:.1});
  bars.forEach(b=>io.observe(b));
})();
</script>
""", unsafe_allow_html=True)
