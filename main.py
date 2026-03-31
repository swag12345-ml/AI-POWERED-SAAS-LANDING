import math
import streamlit as st

st.set_page_config(
    page_title="Swagato Bhattacharya — Python Developer & AI Engineer",
    page_icon="⬡",
    layout="wide",
)

# ─── helpers ──────────────────────────────────────────────────────────────────
def H(s):
    st.markdown(s, unsafe_allow_html=True)

def CSS(s):
    st.markdown("<style>" + s + "</style>", unsafe_allow_html=True)

# ─── CSS ──────────────────────────────────────────────────────────────────────
CSS("""
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --blue:    #0a84ff;
  --green:   #30d158;
  --purple:  #bf5af2;
  --amber:   #ff9f0a;
  --red:     #ff453a;
  --sky:     #4db3ff;
  --fg:      #f5f5f7;
  --fg2:     rgba(245,245,247,0.55);
  --fg3:     rgba(245,245,247,0.28);
  --border:  rgba(255,255,255,0.08);
  --surface: #0a0a0c;
  --surface2:#111115;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
  background-color: #000 !important;
  color: var(--fg) !important;
  font-family: 'Sora', sans-serif !important;
  overflow-x: hidden !important;
  -webkit-font-smoothing: antialiased !important;
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

/* ── Scroll progress bar ── */
#sp {
  position: fixed; top: 0; left: 0; right: 0; height: 2px; width: 0%;
  background: linear-gradient(90deg, #0a84ff, #30d158, #bf5af2, #0a84ff);
  background-size: 200% 100%; z-index: 9999;
  transition: width 0.05s linear; pointer-events: none;
  animation: gradientShift 3s linear infinite;
}

/* ── Noise overlay ── */
.sb-noise {
  position: fixed; inset: 0; z-index: 1; pointer-events: none; opacity: 0.025;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-size: 128px 128px;
}

/* ── Section dot nav ── */
#sb-dots {
  position: fixed; right: 24px; top: 50%; transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 10px; z-index: 800;
}
.sb-dot-nav {
  width: 7px; height: 7px; border-radius: 50%;
  background: rgba(255,255,255,0.2); cursor: pointer;
  transition: background 0.3s, transform 0.3s, box-shadow 0.3s; border: none; padding: 0;
}
.sb-dot-nav.active { background: var(--blue); transform: scale(1.5); box-shadow: 0 0 8px var(--blue); }
.sb-dot-nav:hover { background: rgba(255,255,255,0.5); }
@media (max-width: 900px) { #sb-dots { display: none; } }

/* ── Mobile hamburger ── */
.sb-hamburger {
  display: none; flex-direction: column; gap: 5px; cursor: pointer;
  background: none; border: none; padding: 6px;
}
.sb-hamburger span {
  display: block; width: 22px; height: 2px; background: var(--fg2);
  border-radius: 2px; transition: transform 0.3s ease, opacity 0.3s ease;
}
.sb-hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.sb-hamburger.open span:nth-child(2) { opacity: 0; }
.sb-hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

/* ── Mobile drawer ── */
#sb-drawer {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: 850;
  background: rgba(0,0,0,0.98); display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 32px;
  transform: translateY(-100%); transition: transform 0.4s cubic-bezier(0.16,1,0.3,1);
  pointer-events: none;
}
#sb-drawer.open { transform: translateY(0); pointer-events: all; }
#sb-drawer a {
  font-size: 28px; font-weight: 700; color: var(--fg2);
  text-decoration: none; letter-spacing: -1px; transition: color 0.2s;
}
#sb-drawer a:hover { color: var(--fg); }
#sb-drawer-close {
  position: absolute; top: 24px; right: 24px;
  background: none; border: none; color: var(--fg3); font-size: 28px; cursor: pointer; line-height: 1;
}

/* ── Announcement banner ── */
.sb-banner {
  background: linear-gradient(90deg, rgba(10,132,255,0.1), rgba(48,209,88,0.06), rgba(191,90,242,0.08), rgba(10,132,255,0.1));
  background-size: 300% 100%;
  border-bottom: 1px solid rgba(10,132,255,0.18);
  padding: 10px 32px; text-align: center; position: relative; z-index: 901;
  font-size: 12.5px; color: var(--fg2); font-weight: 500;
  display: flex; align-items: center; justify-content: center; gap: 10px;
  animation: shimmerBg 5s linear infinite;
}
.sb-banner-badge {
  padding: 2px 10px; border-radius: 100px;
  background: linear-gradient(135deg, rgba(10,132,255,0.25), rgba(48,209,88,0.15));
  border: 1px solid rgba(10,132,255,0.4); color: var(--blue);
  font-size: 10px; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase;
  box-shadow: 0 0 12px rgba(10,132,255,0.2);
}
.sb-banner a { color: var(--blue); font-weight: 600; text-decoration: none; transition: color 0.2s; }
.sb-banner a:hover { color: var(--sky); }

/* ── Nav ── */
.sb-nav {
  position: sticky; top: 0; left: 0; right: 0; z-index: 900;
  height: 62px; display: flex; align-items: center; justify-content: center;
  background: rgba(0,0,0,0.82); border-bottom: 1px solid rgba(255,255,255,0.06);
  backdrop-filter: blur(32px); -webkit-backdrop-filter: blur(32px);
  transition: box-shadow 0.4s ease, border-color 0.4s ease;
}
.sb-nav.scrolled { box-shadow: 0 8px 48px rgba(0,0,0,0.7); border-color: rgba(255,255,255,0.09); }
.sb-nav-inner {
  width: 100%; max-width: 1140px;
  display: flex; align-items: center; justify-content: space-between; padding: 0 32px;
}
.sb-logo {
  display: flex; align-items: center; gap: 10px; font-size: 13.5px;
  font-weight: 800; color: var(--fg); text-decoration: none; letter-spacing: 0.8px;
}
.sb-logo-icon {
  width: 34px; height: 34px; border-radius: 10px;
  background: linear-gradient(135deg, #1a6fff, #0044bb);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  box-shadow: 0 4px 20px rgba(10,132,255,0.45), 0 0 0 1px rgba(10,132,255,0.2);
  font-size: 16px;
}
.sb-nav-links { display: flex; align-items: center; gap: 30px; }
.sb-nav-links a {
  font-size: 13px; font-weight: 500; color: var(--fg3); text-decoration: none;
  transition: color 0.2s; position: relative; padding-bottom: 4px;
}
.sb-nav-links a::after {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, var(--blue), var(--green));
  transform: scaleX(0); transition: transform 0.25s ease; transform-origin: left;
}
.sb-nav-links a:hover { color: var(--fg); }
.sb-nav-links a:hover::after { transform: scaleX(1); }
.sb-nav-links a.sb-nav-active { color: var(--fg); }
.sb-nav-links a.sb-nav-active::after { transform: scaleX(1); }
.sb-nav-right { display: flex; align-items: center; gap: 12px; }
.sb-nav-cta {
  display: inline-flex; align-items: center; gap: 7px; padding: 8px 20px;
  border-radius: 100px; background: linear-gradient(135deg, #1a6fff, #0055d4);
  color: #fff; font-size: 13px; font-weight: 600; text-decoration: none;
  box-shadow: 0 4px 20px rgba(10,132,255,0.35);
  transition: transform 0.15s, box-shadow 0.2s; position: relative; overflow: hidden;
}
.sb-nav-cta::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.12), transparent); border-radius: inherit;
}
.sb-nav-cta:hover { transform: translateY(-1px); box-shadow: 0 6px 28px rgba(10,132,255,0.5); }
@media (max-width: 900px) { .sb-nav-links { display: none; } .sb-hamburger { display: flex !important; } }

/* ── Hero ── */
.sb-hero {
  min-height: 100vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 80px 32px 80px;
  position: relative; overflow: hidden; background: #000;
}
.sb-aurora { position: absolute; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
.sb-aurora-1 {
  position: absolute; width: 800px; height: 800px; border-radius: 50%;
  background: radial-gradient(circle, rgba(10,132,255,0.12) 0%, transparent 65%);
  top: -200px; left: 10%; animation: auroraFloat1 12s ease-in-out infinite;
}
.sb-aurora-2 {
  position: absolute; width: 700px; height: 700px; border-radius: 50%;
  background: radial-gradient(circle, rgba(48,209,88,0.07) 0%, transparent 60%);
  top: 0; right: 5%; animation: auroraFloat2 15s ease-in-out infinite;
}
.sb-aurora-3 {
  position: absolute; width: 600px; height: 600px; border-radius: 50%;
  background: radial-gradient(circle, rgba(191,90,242,0.07) 0%, transparent 60%);
  bottom: -100px; left: 30%; animation: auroraFloat3 18s ease-in-out infinite;
}
#sb-particles { position: absolute; inset: 0; pointer-events: none; z-index: 0; }
.sb-hero-grid {
  position: absolute; inset: 0; pointer-events: none; z-index: 0;
  background-image: linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 56px 56px;
  mask-image: radial-gradient(ellipse 70% 50% at 50% 0%, black 40%, transparent 100%);
}
.sb-hero-fade {
  position: absolute; bottom: 0; left: 0; right: 0; height: 280px;
  background: linear-gradient(to bottom, transparent, #000); pointer-events: none; z-index: 0;
}
#sb-spotlight {
  position: absolute; pointer-events: none; z-index: 0;
  width: 700px; height: 700px; border-radius: 50%;
  background: radial-gradient(circle, rgba(10,132,255,0.07) 0%, transparent 60%);
  transform: translate(-50%, -50%); transition: left 0.1s ease, top 0.1s ease;
  left: 50%; top: 50%;
}
.sb-hero-content { position: relative; z-index: 1; width: 100%; display: flex; flex-direction: column; align-items: center; }

.sb-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 10.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--blue); padding: 6px 16px; border-radius: 100px;
  border: 1px solid rgba(10,132,255,0.3); background: rgba(10,132,255,0.08); margin-bottom: 28px;
  animation: fadeUp 0.6s ease both; box-shadow: 0 0 20px rgba(10,132,255,0.1);
}
.sb-eyebrow-dot {
  width: 6px; height: 6px; border-radius: 50%; background: var(--green);
  box-shadow: 0 0 8px var(--green); animation: pulse 2s ease infinite;
}

.sb-h1 {
  font-size: clamp(44px, 7.5vw, 96px); font-weight: 800; line-height: 1.0;
  letter-spacing: -4px; color: var(--fg); max-width: 1020px;
  animation: fadeUp 0.6s 0.1s ease both;
  background: linear-gradient(135deg, #f5f5f7 50%, rgba(245,245,247,0.55));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}

.sb-hero-sub {
  font-size: clamp(15px, 1.9vw, 19px); color: var(--fg2); line-height: 1.75;
  max-width: 580px; margin: 28px auto 0; animation: fadeUp 0.6s 0.2s ease both;
}

.sb-ctas {
  display: flex; gap: 14px; justify-content: center; margin-top: 48px; flex-wrap: wrap;
  animation: fadeUp 0.6s 0.3s ease both;
}

.sb-btn-p {
  display: inline-flex; align-items: center; gap: 8px; padding: 15px 34px; border-radius: 100px;
  background: linear-gradient(135deg, #1a6fff, #0055d4);
  color: #fff; font-size: 15px; font-weight: 600; text-decoration: none; letter-spacing: -0.2px;
  box-shadow: 0 4px 28px rgba(10,132,255,0.45), 0 0 0 1px rgba(10,132,255,0.15);
  transition: transform 0.15s, box-shadow 0.2s; position: relative; overflow: hidden;
}
.sb-btn-p::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.14), transparent); border-radius: inherit;
}
.sb-btn-p:hover { transform: translateY(-2px); box-shadow: 0 8px 36px rgba(10,132,255,0.55); }

.sb-btn-g {
  display: inline-flex; align-items: center; gap: 8px; padding: 14px 30px; border-radius: 100px;
  background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
  color: var(--fg2); font-size: 15px; font-weight: 600; text-decoration: none;
  backdrop-filter: blur(12px); transition: border-color 0.2s, color 0.2s, transform 0.2s;
}
.sb-btn-g:hover { border-color: rgba(255,255,255,0.25); color: var(--fg); transform: translateY(-2px); }

.sb-hero-features {
  display: flex; align-items: center; gap: 0; margin-top: 40px; flex-wrap: wrap;
  justify-content: center; animation: fadeUp 0.6s 0.4s ease both;
  background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
  border-radius: 100px; padding: 10px 24px;
}
.sb-hf-item {
  display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600;
  color: var(--fg3); padding: 0 16px; white-space: nowrap;
}
.sb-hf-sep { width: 1px; height: 14px; background: rgba(255,255,255,0.1); flex-shrink: 0; }

/* ── Stats row ── */
.sb-stats {
  display: flex; gap: 0; justify-content: center; margin-top: 56px; flex-wrap: wrap;
  animation: fadeUp 0.6s 0.5s ease both;
}
.sb-stat {
  padding: 20px 36px; text-align: center; border-right: 1px solid rgba(255,255,255,0.07);
}
.sb-stat:last-child { border-right: none; }
.sb-stat-n {
  font-size: 28px; font-weight: 800; letter-spacing: -1.5px; color: var(--fg);
  font-family: 'JetBrains Mono', monospace;
}
.sb-stat-l { font-size: 11px; font-weight: 600; color: var(--fg3); margin-top: 4px; text-transform: uppercase; letter-spacing: 0.8px; }

/* ── Section base ── */
.sb-section { padding: 100px 0; }
.sb-section-inner { max-width: 1140px; margin: 0 auto; padding: 0 32px; }
.sb-divider {
  font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
  color: var(--blue); margin-bottom: 20px; display: flex; align-items: center; gap: 12px;
}
.sb-divider::before { content: ''; width: 24px; height: 1px; background: var(--blue); }
.sb-section-h {
  font-size: clamp(32px, 4.5vw, 52px); font-weight: 800; letter-spacing: -2.5px;
  color: var(--fg); line-height: 1.06; margin-bottom: 16px;
}
.sb-section-p { font-size: 16px; color: var(--fg2); line-height: 1.75; max-width: 560px; margin-bottom: 8px; }
.sb-blue  { color: var(--blue); }
.sb-green { color: var(--green); }
.sb-amber { color: var(--amber); }
.sb-purple{ color: var(--purple); }

/* ── Reveal ── */
.sb-reveal { opacity: 0; transform: translateY(32px); transition: opacity 0.7s ease, transform 0.7s ease; }
.sb-reveal.visible { opacity: 1; transform: none; }
.sb-reveal-delay-1 { transition-delay: 0.1s; }
.sb-reveal-delay-2 { transition-delay: 0.2s; }
.sb-reveal-delay-3 { transition-delay: 0.3s; }

/* ── Panel (mock UI card) ── */
.sb-panel {
  background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.09);
  border-radius: 20px; padding: 22px;
  box-shadow: 0 24px 64px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,255,255,0.03);
}
.sb-ptitle {
  display: flex; align-items: center; gap: 8px;
  font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;
  color: var(--fg3); margin-bottom: 16px; padding-bottom: 12px;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

/* ── Story grid ── */
.sb-story-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;
}
@media (max-width: 900px) { .sb-story-grid { grid-template-columns: 1fr; gap: 44px; } }
.sb-story-num { font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--fg3); margin-bottom: 16px; }
.sb-story-h { font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; letter-spacing: -1.5px; line-height: 1.1; color: var(--fg); margin-bottom: 18px; }
.sb-story-p { font-size: 15px; color: var(--fg2); line-height: 1.78; margin-bottom: 12px; }

/* ── Pills ── */
.sb-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 24px; }
.sb-pill {
  padding: 6px 14px; border-radius: 100px; font-size: 12px; font-weight: 600;
  background: rgba(10,132,255,0.07); border: 1px solid rgba(10,132,255,0.18);
  color: var(--sky); transition: background 0.2s, border-color 0.2s;
}
.sb-pill:hover { background: rgba(10,132,255,0.14); border-color: rgba(10,132,255,0.35); }

/* ── Steps (skills) ── */
.sb-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2px; margin-top: 48px; }
@media (max-width: 900px) { .sb-steps { grid-template-columns: 1fr 1fr; } }
.sb-step {
  background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.06);
  padding: 30px 26px; position: relative; overflow: hidden;
  transition: background 0.25s, border-color 0.25s, transform 0.25s;
}
.sb-step:first-child { border-radius: 20px 0 0 0; }
.sb-step:nth-child(4) { border-radius: 0 20px 0 0; }
.sb-step:nth-child(5) { border-radius: 0 0 0 20px; }
.sb-step:last-child   { border-radius: 0 0 20px 0; }
.sb-step:hover { background: rgba(14,14,18,0.98); border-color: rgba(255,255,255,0.11); transform: translateY(-3px); }
.sb-step::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
}
.sb-step-n { font-size: 11px; font-weight: 700; color: var(--fg3); margin-bottom: 16px; letter-spacing: 1px; text-transform: uppercase; }
.sb-step-icon { width: 44px; height: 44px; margin-bottom: 18px; }
.sb-step-title { font-size: 15px; font-weight: 700; color: var(--fg); margin-bottom: 9px; letter-spacing: -0.3px; }
.sb-step-desc { font-size: 13px; color: var(--fg2); line-height: 1.74; }

/* ── Skill pills grid ── */
.sb-skill-groups { display: grid; grid-template-columns: repeat(2,1fr); gap: 2px; margin-top: 48px; }
@media (max-width: 700px) { .sb-skill-groups { grid-template-columns: 1fr; } }
.sb-skill-group {
  background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.06);
  padding: 28px; transition: border-color 0.25s;
}
.sb-skill-group:first-child { border-radius: 20px 0 0 0; }
.sb-skill-group:nth-child(2) { border-radius: 0 20px 0 0; }
.sb-skill-group:nth-child(3) { border-radius: 0 0 0 20px; }
.sb-skill-group:last-child { border-radius: 0 0 20px 0; }
.sb-skill-group:hover { border-color: rgba(255,255,255,0.13); }
.sb-skill-group-title {
  font-size: 11px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase;
  color: var(--fg3); margin-bottom: 18px; display: flex; align-items: center; gap: 8px;
}
.sb-skill-pill-wrap { display: flex; flex-wrap: wrap; gap: 7px; }
.sb-spill {
  padding: 6px 14px; border-radius: 100px; font-size: 12px; font-weight: 600;
  background: rgba(255,255,255,0.04); border: 1px solid var(--border); color: var(--fg2);
  transition: all 0.2s; cursor: default;
}
.sb-spill:hover { background: rgba(10,132,255,0.12); border-color: rgba(10,132,255,0.3); color: var(--blue); }

/* ── Experience cards ── */
.sb-exp-list { display: flex; flex-direction: column; gap: 2px; margin-top: 48px; }
.sb-exp-card {
  background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.07);
  border-radius: 20px; padding: 36px;
  transition: border-color 0.3s, background 0.3s, transform 0.3s; cursor: default;
}
.sb-exp-card:hover { border-color: rgba(10,132,255,0.25); background: rgba(14,14,18,0.98); transform: translateX(4px); }
.sb-exp-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; flex-wrap: wrap; margin-bottom: 20px; }
.sb-exp-role { font-size: 19px; font-weight: 700; letter-spacing: -0.5px; }
.sb-exp-company { font-size: 13px; color: var(--blue); font-weight: 600; margin-top: 4px; font-family: 'JetBrains Mono', monospace; }
.sb-exp-date {
  font-size: 12px; font-weight: 600; color: var(--fg3); padding: 5px 14px;
  border-radius: 100px; border: 1px solid var(--border); background: var(--surface);
  white-space: nowrap;
}
.sb-exp-points { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.sb-exp-points li { font-size: 14.5px; color: var(--fg2); line-height: 1.6; padding-left: 20px; position: relative; }
.sb-exp-points li::before { content: ''; position: absolute; left: 0; top: 10px; width: 6px; height: 6px; border-radius: 50%; background: var(--blue); }

/* ── Project cards ── */
.sb-card-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 20px; margin-top: 48px; }
@media (max-width: 700px) { .sb-card-grid { grid-template-columns: 1fr; } }
.sb-card {
  background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px; padding: 36px; position: relative; overflow: hidden;
  transition: border-color 0.4s, transform 0.4s, box-shadow 0.4s;
}
.sb-card:hover { border-color: rgba(10,132,255,0.25); transform: translateY(-4px); box-shadow: 0 24px 64px rgba(0,0,0,0.5); }
.sb-card-icon {
  width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center;
  justify-content: center; font-size: 24px; margin-bottom: 24px;
  background: rgba(10,132,255,0.1); border: 1px solid rgba(10,132,255,0.2);
}
.sb-card-name { font-size: 22px; font-weight: 800; letter-spacing: -0.8px; margin-bottom: 6px; }
.sb-card-tagline { font-size: 13px; color: var(--blue); font-weight: 600; font-family: 'JetBrains Mono', monospace; margin-bottom: 16px; }
.sb-card-desc { font-size: 14.5px; color: var(--fg2); line-height: 1.65; margin-bottom: 22px; }
.sb-card-stack { display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 24px; }
.sb-stack-tag {
  font-size: 11px; font-weight: 600; padding: 4px 12px; border-radius: 100px;
  background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: var(--fg3);
  transition: color 0.2s, border-color 0.2s;
}
.sb-stack-tag:hover { color: var(--fg2); border-color: rgba(255,255,255,0.15); }
.sb-card-badge {
  display: inline-flex; align-items: center; gap: 6px; padding: 5px 13px; border-radius: 100px;
  font-size: 11.5px; font-weight: 700; letter-spacing: 0.5px;
  background: rgba(48,209,88,0.1); border: 1px solid rgba(48,209,88,0.25); color: var(--green);
}
.sb-card-link {
  display: inline-flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 700;
  color: var(--blue); text-decoration: none; padding: 10px 20px;
  border-radius: 100px; border: 1px solid rgba(10,132,255,0.3);
  background: rgba(10,132,255,0.08); margin-top: 16px;
  transition: background 0.2s, border-color 0.2s;
}
.sb-card-link:hover { background: rgba(10,132,255,0.18); border-color: rgba(10,132,255,0.5); }

/* ── Cert / Education cards ── */
.sb-cert-list { display: flex; flex-direction: column; gap: 14px; margin-top: 48px; }
.sb-cert-card {
  background: rgba(8,8,12,0.95); border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px; padding: 24px 28px; display: flex; align-items: center; gap: 20px;
  transition: border-color 0.3s, background 0.3s;
}
.sb-cert-card:hover { border-color: rgba(191,90,242,0.3); background: rgba(14,14,18,0.98); }
.sb-cert-icon {
  width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center; font-size: 22px;
  background: rgba(191,90,242,0.08); border: 1px solid rgba(191,90,242,0.2);
}
.sb-cert-name { font-size: 15px; font-weight: 700; }
.sb-cert-sub { font-size: 12.5px; color: var(--fg3); margin-top: 3px; font-family: 'JetBrains Mono', monospace; }

/* ── Testimonial ticker ── */
.sb-ticker-wrap {
  overflow: hidden; padding: 48px 0; background: #000;
  border-top: 1px solid rgba(255,255,255,0.05);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  mask-image: linear-gradient(90deg, transparent, black 8%, black 92%, transparent);
}
.sb-ticker-track { display: flex; gap: 24px; width: max-content; animation: tickerScroll 42s linear infinite; }
.sb-ticker-track:hover { animation-play-state: paused; }
.sb-ticker-item {
  background: rgba(10,10,14,0.9); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px; padding: 22px 26px; min-width: 300px; max-width: 340px;
  flex-shrink: 0; backdrop-filter: blur(8px);
  transition: border-color 0.2s, transform 0.2s;
}
.sb-ticker-item:hover { border-color: rgba(255,255,255,0.16); transform: translateY(-3px); }
.sb-ticker-stars { color: #ff9f0a; font-size: 10px; margin-bottom: 8px; letter-spacing: 1px; }
.sb-ticker-quote { font-size: 13px; color: var(--fg2); line-height: 1.74; margin-bottom: 14px; font-style: italic; }
.sb-ticker-author { display: flex; align-items: center; gap: 10px; }
.sb-ticker-avatar { width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; flex-shrink: 0; }
.sb-ticker-name { font-size: 12px; font-weight: 700; color: var(--fg); }
.sb-ticker-role { font-size: 11px; color: var(--fg3); margin-top: 1px; }

/* ── CTA section ── */
.sb-cta-section {
  margin: 0 32px 120px; padding: 96px 60px; border-radius: 32px;
  background: rgba(6,6,10,0.95); border: 1px solid rgba(255,255,255,0.08);
  text-align: center; position: relative; overflow: hidden;
  box-shadow: 0 40px 80px rgba(0,0,0,0.5);
}
.sb-cta-glow {
  position: absolute; top: -300px; left: 50%; transform: translateX(-50%);
  width: 800px; height: 800px;
  background: radial-gradient(ellipse at center, rgba(10,132,255,0.12) 0%, rgba(48,209,88,0.05) 45%, transparent 68%);
  pointer-events: none; animation: auroraFloat1 10s ease-in-out infinite;
}
.sb-cta-h { font-size: clamp(28px, 4.5vw, 56px); font-weight: 800; letter-spacing: -2.5px; color: var(--fg); line-height: 1.04; max-width: 680px; margin: 0 auto 22px; position: relative; z-index: 1; }
.sb-cta-sub { font-size: 16px; color: var(--fg2); margin: 0 auto 40px; position: relative; z-index: 1; max-width: 520px; line-height: 1.72; }
.sb-cta-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }
@media (max-width: 640px) { .sb-cta-section { padding: 56px 28px; margin: 0 16px 80px; } }

/* ── Contact card ── */
.sb-contact-card {
  background: rgba(8,8,12,0.9); border-radius: 24px; border: 1px solid rgba(255,255,255,0.07);
  padding: 44px; max-width: 560px; margin: 0 auto 100px;
  text-align: center; backdrop-filter: blur(12px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.4);
}
.sb-contact-card h3 { font-size: 22px; font-weight: 800; color: var(--fg); letter-spacing: -0.8px; margin-bottom: 10px; }
.sb-contact-card p { font-size: 14px; color: var(--fg3); line-height: 1.7; margin-bottom: 28px; }
.sb-contact-links { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }
.sb-contact-link {
  display: inline-flex; align-items: center; gap: 9px; padding: 11px 22px; border-radius: 14px;
  background: rgba(10,132,255,0.07); border: 1px solid rgba(10,132,255,0.22);
  color: var(--sky); font-size: 13px; font-weight: 600; text-decoration: none;
  font-family: 'JetBrains Mono', monospace;
  transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.sb-contact-link:hover { background: rgba(10,132,255,0.13); border-color: rgba(10,132,255,0.4); box-shadow: 0 0 24px rgba(10,132,255,0.15); }

/* ── Footer ── */
.sb-footer {
  border-top: 1px solid rgba(255,255,255,0.06); padding: 44px 32px;
  display: grid; grid-template-columns: 1fr auto; align-items: center;
  max-width: 1140px; margin: 0 auto; gap: 20px;
}
.sb-footer-copy { font-size: 13px; font-weight: 600; color: var(--fg3); }
.sb-footer-tagline { font-size: 12px; color: rgba(245,245,247,0.18); margin-top: 5px; }
.sb-footer-links { display: flex; gap: 24px; }
.sb-footer-links a { font-size: 13px; color: rgba(245,245,247,0.28); text-decoration: none; transition: color 0.2s; }
.sb-footer-links a:hover { color: var(--fg2); }
@media (max-width: 640px) { .sb-footer { grid-template-columns: 1fr; } }

/* ── Keyframes ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(32px); }
  to   { opacity: 1; transform: none; }
}
@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes shimmerBg {
  0%   { background-position: 200% center; }
  100% { background-position: -200% center; }
}
@keyframes pulse {
  0%, 100% { opacity: 1; box-shadow: 0 0 8px var(--green); }
  50%       { opacity: 0.5; box-shadow: 0 0 4px var(--green); }
}
@keyframes tickerScroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
@keyframes auroraFloat1 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33%       { transform: translate(60px, 40px) scale(1.05); }
  66%       { transform: translate(-40px, 80px) scale(0.96); }
}
@keyframes auroraFloat2 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  40%       { transform: translate(-80px, 60px) scale(1.08); }
  70%       { transform: translate(40px, -40px) scale(0.94); }
}
@keyframes auroraFloat3 {
  0%, 100% { transform: translate(0, 0) scale(1); }
  30%       { transform: translate(50px, -60px) scale(1.06); }
  60%       { transform: translate(-60px, 20px) scale(1.02); }
}
""")


# ─── helpers ──────────────────────────────────────────────────────────────────
LINKEDIN  = "https://www.linkedin.com/in/swagato-bhattacharya-8a52aa373/"
GITHUB    = "https://github.com/swag12345-ml"
HIRELYZER = "https://hirelyzer-supabase-implemented-kf4y7bocccdsmiswtabveh.streamlit.app/"
EMAIL     = "swagato_bmca2024@msit.edu.in"
PHONE     = "+91 70442 75077"

def pills(labels, color="blue"):
    clr_map = {"blue": (var_blue := "rgba(10,132,255,0.07)", "rgba(10,132,255,0.18)", "#4db3ff"),
               "green": ("rgba(48,209,88,0.07)", "rgba(48,209,88,0.18)", "#30d158"),
               "purple": ("rgba(191,90,242,0.07)", "rgba(191,90,242,0.18)", "#bf5af2")}
    bg, _, fg = clr_map.get(color, clr_map["blue"])
    return "".join(
        f'<span class="sb-pill">{l}</span>' for l in labels
    )

def chk_y():
    return '<span style="color:#30d158;font-size:16px;filter:drop-shadow(0 0 4px rgba(48,209,88,0.4))">✓</span>'

def chk_n():
    return '<span style="color:rgba(245,245,247,0.18);font-size:18px">&mdash;</span>'

def checks(items):
    chk = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return "".join(f'<div style="display:flex;align-items:center;gap:8px;font-size:13px;color:rgba(245,245,247,0.5);margin-bottom:8px">{chk}<span>{i}</span></div>' for i in items)


# ─── SECTIONS ─────────────────────────────────────────────────────────────────
def render_banner():
    H('<div class="sb-banner">'
      '<span class="sb-banner-badge">Open to Work</span>'
      'Python Developer &amp; AI Engineer &mdash; Available for full-time roles, freelance &amp; collaborations. '
      '<a href="mailto:' + EMAIL + '">Get in touch &rarr;</a>'
      '</div>')


def render_nav():
    H('<div id="sp"></div>'
      '<div class="sb-noise"></div>'

      # Mobile drawer
      '<div id="sb-drawer">'
      '<button id="sb-drawer-close" onclick="closeDrawer()">&times;</button>'
      '<a href="#sb-hero-anchor" onclick="closeDrawer()">Home</a>'
      '<a href="#about" onclick="closeDrawer()">About</a>'
      '<a href="#experience" onclick="closeDrawer()">Experience</a>'
      '<a href="#projects" onclick="closeDrawer()">Projects</a>'
      '<a href="#skills" onclick="closeDrawer()">Skills</a>'
      '<a href="#contact" onclick="closeDrawer()">Contact</a>'
      '</div>'

      # Section dots
      '<div id="sb-dots">'
      '<button class="sb-dot-nav" data-section="sb-hero-anchor" title="Home"></button>'
      '<button class="sb-dot-nav" data-section="about" title="About"></button>'
      '<button class="sb-dot-nav" data-section="experience" title="Experience"></button>'
      '<button class="sb-dot-nav" data-section="projects" title="Projects"></button>'
      '<button class="sb-dot-nav" data-section="skills" title="Skills"></button>'
      '<button class="sb-dot-nav" data-section="contact" title="Contact"></button>'
      '</div>'

      # Nav
      '<nav class="sb-nav" id="sb-nav">'
      '<div class="sb-nav-inner">'
      '<a href="#sb-hero-anchor" class="sb-logo">'
      '<div class="sb-logo-icon">⬡</div>'
      'SWAGATO'
      '</a>'
      '<div class="sb-nav-links">'
      '<a href="#about" data-nav="about">About</a>'
      '<a href="#experience" data-nav="experience">Experience</a>'
      '<a href="#projects" data-nav="projects">Projects</a>'
      '<a href="#skills" data-nav="skills">Skills</a>'
      '<a href="#contact" data-nav="contact">Contact</a>'
      '</div>'
      '<div class="sb-nav-right">'
      '<button class="sb-hamburger" id="sb-hamburger" onclick="openDrawer()" style="display:none" aria-label="Menu">'
      '<span></span><span></span><span></span>'
      '</button>'
      '<a href="mailto:' + EMAIL + '" class="sb-nav-cta">'
      '✦ Hire Me'
      '</a>'
      '</div>'
      '</div></nav>')


def render_hero():
    H('<div class="sb-hero">'
      '<div id="sb-hero-anchor" style="position:absolute;top:0;pointer-events:none"></div>'

      '<div class="sb-aurora">'
      '<div class="sb-aurora-1"></div>'
      '<div class="sb-aurora-2"></div>'
      '<div class="sb-aurora-3"></div>'
      '</div>'

      '<canvas id="sb-particles"></canvas>'
      '<div class="sb-hero-grid"></div>'
      '<div id="sb-spotlight"></div>'
      '<div class="sb-hero-fade"></div>'

      '<div class="sb-hero-content">'
      '<div class="sb-eyebrow">'
      '<div class="sb-eyebrow-dot"></div>'
      'Python Developer &amp; Generative AI Engineer &mdash; Kolkata, India'
      '</div>'

      '<h1 class="sb-h1">Swagato<br/>Bhattacharya</h1>'

      '<p class="sb-hero-sub">Building intelligent systems at the intersection of backend engineering and Generative AI &mdash; from LangChain-powered RAG pipelines to full-stack platforms that actually ship.</p>'

      '<div class="sb-ctas">'
      '<a href="#projects" class="sb-btn-p">'
      '⬡ View Projects'
      '</a>'
      '<a href="' + LINKEDIN + '" target="_blank" class="sb-btn-g">'
      '↗ LinkedIn'
      '</a>'
      '</div>'

      '<div class="sb-hero-features">'
      '<div class="sb-hf-item">'
      '<svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>'
      'Python & LangChain</div>'
      '<div class="sb-hf-sep"></div>'
      '<div class="sb-hf-item">'
      '<svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>'
      'Generative AI & LLMs</div>'
      '<div class="sb-hf-sep"></div>'
      '<div class="sb-hf-item">'
      '<svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>'
      'RESTful APIs</div>'
      '<div class="sb-hf-sep"></div>'
      '<div class="sb-hf-item">'
      '<svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>'
      'RAG Pipelines</div>'
      '<div class="sb-hf-sep"></div>'
      '<div class="sb-hf-item">'
      '<svg width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round"/></svg>'
      'Streamlit Apps</div>'
      '</div>'

      '<div class="sb-stats">'
      '<div class="sb-stat"><div class="sb-stat-n" style="color:#0a84ff" data-count="9" data-suffix="mo">9mo</div><div class="sb-stat-l">Internship</div></div>'
      '<div class="sb-stat"><div class="sb-stat-n" style="color:#30d158" data-count="2" data-suffix="+">2+</div><div class="sb-stat-l">AI Projects</div></div>'
      '<div class="sb-stat"><div class="sb-stat-n" style="color:#bf5af2">SIH</div><div class="sb-stat-l">State Qualifier</div></div>'
      '<div class="sb-stat"><div class="sb-stat-n" style="color:#ff9f0a" data-count="10" data-suffix="+">10+</div><div class="sb-stat-l">Technologies</div></div>'
      '<div class="sb-stat"><div class="sb-stat-n" style="color:#4db3ff">B.Sc.</div><div class="sb-stat-l">CS Hons</div></div>'
      '</div>'

      '</div>'  # hero-content
      '</div>')  # hero


def render_about():
    H('<div id="about" class="sb-section" style="background:#000">'
      '<div class="sb-section-inner">'
      '<div class="sb-story-grid">'

      '<div class="sb-reveal">'
      '<div class="sb-divider">About Me</div>'
      '<h2 class="sb-section-h">Building at the<br><span class="sb-blue">edge of AI</span></h2>'
      '<p class="sb-section-p">I\'m an entry-level Python Developer with hands-on experience in backend development and Generative AI. I excel at building RESTful APIs and managing advanced AI models using frameworks like LangChain.</p>'
      '<p class="sb-section-p">My analytical mindset enables me to write efficient, scalable, and maintainable code while continuously improving user experiences through innovative, real-world projects.</p>'
      '<div class="sb-pills">' + pills(["Analytical Mindset","Logical Problem-Solving","Team Collaboration","Adaptability","Time Management"]) + '</div>'
      '</div>'

      '<div class="sb-reveal sb-reveal-delay-2">'
      '<div class="sb-panel">'
      '<div class="sb-ptitle">'
      '<svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>'
      'At a glance'
      '</div>'

      '<div style="display:flex;flex-direction:column;gap:14px">'

      '<div style="display:flex;justify-content:space-between;align-items:center;padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.14)">'
      '<div style="font-size:12px;color:rgba(245,245,247,0.4);font-weight:600;text-transform:uppercase;letter-spacing:.8px">Status</div>'
      '<div style="font-size:13px;font-weight:700;color:#30d158;display:flex;align-items:center;gap:6px">'
      '<span style="width:6px;height:6px;background:#30d158;border-radius:50%;box-shadow:0 0 6px #30d158;display:inline-block"></span>'
      'Open to Opportunities'
      '</div></div>'

      '<div style="display:flex;justify-content:space-between;align-items:center;padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;border:1px solid rgba(255,255,255,0.07)">'
      '<div style="font-size:12px;color:rgba(245,245,247,0.4);font-weight:600;text-transform:uppercase;letter-spacing:.8px">Location</div>'
      '<div style="font-size:13px;font-weight:700;color:#f5f5f7">Kolkata, India</div></div>'

      '<div style="display:flex;justify-content:space-between;align-items:center;padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;border:1px solid rgba(255,255,255,0.07)">'
      '<div style="font-size:12px;color:rgba(245,245,247,0.4);font-weight:600;text-transform:uppercase;letter-spacing:.8px">Focus</div>'
      '<div style="font-size:13px;font-weight:700;color:#f5f5f7">Backend + Gen AI</div></div>'

      '<div style="display:flex;justify-content:space-between;align-items:center;padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;border:1px solid rgba(255,255,255,0.07)">'
      '<div style="font-size:12px;color:rgba(245,245,247,0.4);font-weight:600;text-transform:uppercase;letter-spacing:.8px">Languages</div>'
      '<div style="font-size:13px;font-weight:700;color:#f5f5f7">English · Bengali · Hindi</div></div>'

      '<div style="display:flex;justify-content:space-between;align-items:center;padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;border:1px solid rgba(255,255,255,0.07)">'
      '<div style="font-size:12px;color:rgba(245,245,247,0.4);font-weight:600;text-transform:uppercase;letter-spacing:.8px">Interests</div>'
      '<div style="font-size:13px;font-weight:700;color:#f5f5f7">AI · LLMs · Data Analytics</div></div>'

      '</div>'  # flex col
      '</div>'  # panel
      '</div>'  # right col

      '</div>'  # story-grid
      '</div>'  # section-inner
      '</div>')  # section


def render_experience():
    H('<div id="experience" class="sb-section" style="background:#030305">'
      '<div class="sb-section-inner">'
      '<div class="sb-divider sb-reveal">Experience</div>'
      '<h2 class="sb-section-h sb-reveal">Where I\'ve<br>been <span class="sb-blue">building</span></h2>'

      '<div class="sb-exp-list">'

      # Card 1: A.Technologies
      '<div class="sb-exp-card sb-reveal">'
      '<div class="sb-exp-top">'
      '<div>'
      '<div class="sb-exp-role">Full Stack Developer — Intern</div>'
      '<div class="sb-exp-company">A.Technologies</div>'
      '</div>'
      '<div class="sb-exp-date">Sep 2023 — Jun 2024</div>'
      '</div>'
      '<ul class="sb-exp-points">'
      '<li>Constructed the CITY-FIXERS platform using JavaScript, HTML/CSS and SQL — connecting frontend elements with server-side logic end-to-end.</li>'
      '<li>Optimised the responsive interface, enhancing mobile interaction metrics by <strong style="color:#30d158">30%</strong> and improving navigation clarity across all devices.</li>'
      '<li>Authored test scripts, performed debugging and executed unit evaluations — raising system reliability and reducing downtime by <strong style="color:#30d158">40%</strong>.</li>'
      '<li>Documented technical processes and workflows, providing analytical insights to support project delivery and completion.</li>'
      '</ul>'
      '</div>'

      '</div>'  # exp-list

      # Education inline
      '<div style="margin-top:48px">'
      '<div class="sb-divider sb-reveal">Education</div>'
      '<div class="sb-cert-list">'

      '<div class="sb-cert-card sb-reveal">'
      '<div class="sb-cert-icon">🎓</div>'
      '<div>'
      '<div class="sb-cert-name">B.Sc. (Hons) Computer Science</div>'
      '<div class="sb-cert-sub">Behala College &nbsp;·&nbsp; Sep 2021 – Jul 2024 &nbsp;·&nbsp; MERN Specialisation</div>'
      '</div></div>'

      '<div class="sb-cert-card sb-reveal sb-reveal-delay-1">'
      '<div class="sb-cert-icon">📜</div>'
      '<div>'
      '<div class="sb-cert-name">ESC — MERN Training</div>'
      '<div class="sb-cert-sub">Jul 2025 – Oct 2025 &nbsp;·&nbsp; LLaMA 3.3 · LangChain · Groq API · Plotly · Streamlit</div>'
      '</div></div>'

      '</div>'  # cert-list
      '</div>'  # education wrapper

      '</div>'  # section-inner
      '</div>')  # section


def render_projects():
    H('<div id="projects" class="sb-section" style="background:#000">'
      '<div class="sb-section-inner">'
      '<div class="sb-divider sb-reveal">Projects</div>'
      '<h2 class="sb-section-h sb-reveal">Things I\'ve<br><span class="sb-green">shipped</span></h2>'

      '<div class="sb-card-grid">'

      # ── HIRELYZER ──
      '<div class="sb-card sb-reveal">'
      '<div class="sb-card-icon">⬡</div>'
      '<div class="sb-card-name">HIRELYZER</div>'
      '<div class="sb-card-tagline">AI-Driven Career Intelligence Platform</div>'
      '<p class="sb-card-desc">End-to-end AI career platform integrating resume analysis with ATS scoring, grammar validation, bias detection, skill-gap insights, job search with domain filtering, live interview coaching, and a scalable admin analytics dashboard.</p>'
      '<div class="sb-card-stack">'
      '<span class="sb-stack-tag">Python</span>'
      '<span class="sb-stack-tag">LangChain</span>'
      '<span class="sb-stack-tag">LLaMA</span>'
      '<span class="sb-stack-tag">Streamlit</span>'
      '<span class="sb-stack-tag">SQLite3</span>'
      '<span class="sb-stack-tag">NumPy</span>'
      '<span class="sb-stack-tag">Pandas</span>'
      '<span class="sb-stack-tag">Matplotlib</span>'
      '<span class="sb-stack-tag">HTML/CSS/JS</span>'
      '</div>'
      '<div style="margin-bottom:12px"><span class="sb-card-badge">🏆 SIH 2025 State Qualifier &mdash; PS ID: 25140</span></div>'
      '<div style="font-size:12.5px;color:rgba(245,245,247,0.3);margin-bottom:4px;font-family:\'JetBrains Mono\',monospace">Mar 2025 – Aug 2025</div>'
      '<a href="' + HIRELYZER + '" target="_blank" class="sb-card-link">↗ Live Demo</a>'
      '</div>'

      # ── TRANZIFY ──
      '<div class="sb-card sb-reveal sb-reveal-delay-1" style="--card-accent:rgba(48,209,88,0.1)">'
      '<div class="sb-card-icon" style="background:rgba(48,209,88,0.1);border-color:rgba(48,209,88,0.2)">📈</div>'
      '<div class="sb-card-name">TRANZIFY</div>'
      '<div class="sb-card-tagline" style="color:#30d158">AI Financial Advisor Platform</div>'
      '<p class="sb-card-desc">AI-powered platform delivering automated guidance on budgeting, investment planning, debt reduction and retirement strategies — powered by LLaMA 3.3 and Groq API for real-time personalised scoring and actionable insights.</p>'
      '<div class="sb-card-stack">'
      '<span class="sb-stack-tag">Python</span>'
      '<span class="sb-stack-tag">LLaMA 3.3</span>'
      '<span class="sb-stack-tag">LangChain</span>'
      '<span class="sb-stack-tag">Groq API</span>'
      '<span class="sb-stack-tag">Streamlit</span>'
      '<span class="sb-stack-tag">Plotly</span>'
      '<span class="sb-stack-tag">NumPy</span>'
      '<span class="sb-stack-tag">Pandas</span>'
      '</div>'
      '<div style="font-size:13px;color:rgba(245,245,247,0.35);line-height:1.65;margin-bottom:8px">'
      'Dynamic Plotly dashboards &middot; Deterministic fallback mechanisms &middot; Real-time financial computation'
      '</div>'
      '<div style="font-size:12.5px;color:rgba(245,245,247,0.3);font-family:\'JetBrains Mono\',monospace">Aug 2025 – Sep 2025</div>'
      '</div>'

      '</div>'  # card-grid
      '</div>'  # section-inner
      '</div>')  # section


def render_skills():
    skill_sections = [
        ("🤖", "AI & Machine Learning",
         ["Generative AI", "LLMs", "Retrieval-Augmented Generation (RAG)", "LangChain", "FAISS", "Vector Databases"]),
        ("🐍", "Languages & Core",
         ["Python", "JavaScript", "HTML", "SQL"]),
        ("⚙️", "Backend & APIs",
         ["RESTful API Development", "Backend Development", "SQLite3", "Git", "Streamlit"]),
        ("📊", "Data & Visualisation",
         ["NumPy", "Pandas", "Matplotlib", "Plotly", "Data Analytics"]),
    ]

    groups_html = ""
    for icon, title, skills in skill_sections:
        pills_html = "".join(f'<span class="sb-spill">{s}</span>' for s in skills)
        groups_html += (
            f'<div class="sb-skill-group sb-reveal">'
            f'<div class="sb-skill-group-title"><span>{icon}</span>{title}</div>'
            f'<div class="sb-skill-pill-wrap">{pills_html}</div>'
            f'</div>'
        )

    H('<div id="skills" class="sb-section" style="background:#030305">'
      '<div class="sb-section-inner">'
      '<div class="sb-divider sb-reveal">Skills</div>'
      '<h2 class="sb-section-h sb-reveal">My technical<br><span class="sb-purple">toolkit</span></h2>'
      '<div class="sb-skill-groups">' + groups_html + '</div>'
      '</div>'
      '</div>')


def render_testimonials():
    testimonials = [
        ("&ldquo;Built an AI platform and qualified for SIH 2025 state level &mdash; the architecture and engineering quality stood out.&rdquo;", "Hackathon Jury", "Smart India Hackathon 2025", "#0a84ff"),
        ("&ldquo;Swagato&rsquo;s internship work on CITY-FIXERS improved mobile engagement by 30%. Solid frontend and backend instincts.&rdquo;", "Team Lead", "A.Technologies", "#30d158"),
        ("&ldquo;The HIRELYZER platform is impressively polished &mdash; ATS scoring, bias detection, and interview coaching all in one.&rdquo;", "Peer Review", "Portfolio Showcase", "#bf5af2"),
        ("&ldquo;TRANZIFY uses Groq + LLaMA 3.3 to deliver real-time financial insights. The Plotly dashboards are clean and interactive.&rdquo;", "Code Review", "ESC MERN Training", "#ff9f0a"),
        ("&ldquo;Reduced system downtime by 40% through disciplined test scripting and debugging during his internship tenure.&rdquo;", "Senior Dev", "A.Technologies", "#4db3ff"),
        ("&ldquo;Strong grasp of RAG pipelines and vector databases for an entry-level developer. The LangChain integration is production-ready.&rdquo;", "Mentor", "AI Workshop", "#ff453a"),
    ]

    def card(quote, name, role, color):
        init = name[0]
        return (
            '<div class="sb-ticker-item">'
            '<div class="sb-ticker-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
            '<div class="sb-ticker-quote">' + quote + '</div>'
            '<div class="sb-ticker-author">'
            '<div class="sb-ticker-avatar" style="background:' + color + '22;color:' + color + ';box-shadow:0 0 12px ' + color + '22">' + init + '</div>'
            '<div><div class="sb-ticker-name">' + name + '</div><div class="sb-ticker-role">' + role + '</div></div>'
            '</div></div>'
        )

    cards_html = "".join(card(*t) for t in testimonials)
    H('<div class="sb-ticker-wrap">'
      '<div class="sb-ticker-track">'
      + cards_html + cards_html +
      '</div></div>')


def render_cta():
    H('<div class="sb-cta-section sb-reveal">'
      '<div class="sb-cta-glow"></div>'
      '<h2 class="sb-cta-h">Let&rsquo;s build something<br>remarkable together</h2>'
      '<p class="sb-cta-sub">Open to full-time roles, freelance projects, and collaborations. I respond fast &mdash; drop me a message.</p>'
      '<div class="sb-cta-btns">'
      '<a href="mailto:' + EMAIL + '" class="sb-btn-p" style="font-size:15px;padding:16px 36px">'
      '✦ Get in Touch'
      '</a>'
      '<a href="' + GITHUB + '" target="_blank" class="sb-btn-g" style="font-size:15px;padding:16px 32px">'
      '↗ View GitHub'
      '</a>'
      '</div>'
      '<div style="margin-top:36px">'
      + checks(["Available for full-time roles", "Open to freelance & contract work", "Quick to respond & onboard"])
      + '</div>'
      '</div>')


def render_contact():
    H('<div id="contact">'
      '<div class="sb-contact-card sb-reveal">'
      '<h3>Reach out directly</h3>'
      '<p>Whether you have a role, a project idea, or just want to connect &mdash; I&rsquo;m always happy to chat.</p>'
      '<div class="sb-contact-links">'
      '<a href="mailto:' + EMAIL + '" class="sb-contact-link">✉ ' + EMAIL + '</a>'
      '<a href="tel:+917044275077" class="sb-contact-link">✆ ' + PHONE + '</a>'
      '<a href="' + LINKEDIN + '" target="_blank" class="sb-contact-link">in LinkedIn</a>'
      '<a href="' + GITHUB + '" target="_blank" class="sb-contact-link">⌥ GitHub</a>'
      '</div>'
      '</div>'
      '</div>')


def render_footer():
    H('<div class="sb-footer">'
      '<div class="sb-footer-left">'
      '<div class="sb-footer-copy">Swagato Bhattacharya &copy; 2026</div>'
      '<div class="sb-footer-tagline">Python Developer &amp; Generative AI Engineer &mdash; Kolkata, India</div>'
      '</div>'
      '<div class="sb-footer-links">'
      '<a href="mailto:' + EMAIL + '">Email</a>'
      '<a href="' + LINKEDIN + '" target="_blank">LinkedIn</a>'
      '<a href="' + GITHUB + '" target="_blank">GitHub</a>'
      '</div>'
      '</div>')


def render_js():
    H('<script>'
      '(function(){'

      # Scroll progress
      'var sp=document.getElementById("sp");'
      'function updateSP(){'
      'var sc=window.scrollY;var h=document.documentElement.scrollHeight-window.innerHeight;'
      'if(sp)sp.style.width=(h>0?(sc/h*100):0)+"%";'
      '}'
      'window.addEventListener("scroll",updateSP,{passive:true});'

      # Nav scrolled state
      'var nav=document.getElementById("sb-nav");'
      'window.addEventListener("scroll",function(){if(nav)nav.classList.toggle("scrolled",window.scrollY>40);},{passive:true});'

      # Mobile hamburger show/hide
      'var hb=document.getElementById("sb-hamburger");'
      'if(hb){'
      'function checkHB(){hb.style.display=window.innerWidth<=900?"flex":"none";}'
      'checkHB();window.addEventListener("resize",checkHB);'
      '}'

      # Mobile drawer
      'window.openDrawer=function(){'
      'document.getElementById("sb-drawer").classList.add("open");'
      'document.getElementById("sb-hamburger").classList.add("open");'
      'document.body.style.overflow="hidden";'
      '};'
      'window.closeDrawer=function(){'
      'document.getElementById("sb-drawer").classList.remove("open");'
      'document.getElementById("sb-hamburger").classList.remove("open");'
      'document.body.style.overflow="";'
      '};'
      'var dc=document.getElementById("sb-drawer-close");'
      'if(dc)dc.addEventListener("click",closeDrawer);'

      # Section dot nav
      'var dots=document.querySelectorAll(".sb-dot-nav");'
      'dots.forEach(function(d){'
      'd.addEventListener("click",function(){'
      'var t=document.getElementById(this.getAttribute("data-section"));'
      'if(t)t.scrollIntoView({behavior:"smooth",block:"start"});'
      '});});'

      'var sectionIds=["sb-hero-anchor","about","experience","projects","skills","contact"];'
      'var dotObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var id=e.target.id;'
      'dots.forEach(function(d){d.classList.toggle("active",d.getAttribute("data-section")===id);});'
      'var navLinks=document.querySelectorAll("[data-nav]");'
      'navLinks.forEach(function(a){a.classList.toggle("sb-nav-active",a.getAttribute("data-nav")===id);});'
      '}'
      '});},{threshold:0.4});'
      'sectionIds.forEach(function(id){var el=document.getElementById(id);if(el)dotObs.observe(el);});'

      # Reveal on scroll
      'var reveals=document.querySelectorAll(".sb-reveal");'
      'var revObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add("visible");revObs.unobserve(e.target);}});'
      '},{threshold:0.12});'
      'reveals.forEach(function(el){revObs.observe(el);});'

      # Animated stat counters
      'function animateCount(el,target,suffix){'
      'var start=0;var dur=1800;var startTime=null;'
      'function step(ts){'
      'if(!startTime)startTime=ts;'
      'var p=Math.min((ts-startTime)/dur,1);var ease=1-Math.pow(1-p,3);'
      'el.textContent=Math.round(ease*target)+(suffix||"");'
      'if(p<1)requestAnimationFrame(step);'
      '}'
      'requestAnimationFrame(step);'
      '}'
      'var statObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var el=e.target,count=parseInt(el.getAttribute("data-count")),suf=el.getAttribute("data-suffix")||"";'
      'if(count)animateCount(el,count,suf);statObs.unobserve(el);'
      '}'
      '});},{threshold:0.5});'
      'document.querySelectorAll("[data-count]").forEach(function(el){statObs.observe(el);});'

      # Cursor spotlight
      'var heroEl=document.querySelector(".sb-hero");'
      'var spotlight=document.getElementById("sb-spotlight");'
      'if(heroEl&&spotlight){'
      'heroEl.addEventListener("mousemove",function(e){'
      'var rect=heroEl.getBoundingClientRect();'
      'spotlight.style.left=(e.clientX-rect.left)+"px";'
      'spotlight.style.top=(e.clientY-rect.top)+"px";'
      '},{passive:true});'
      'heroEl.addEventListener("mouseleave",function(){spotlight.style.left="50%";spotlight.style.top="50%";});'
      '}'

      # Particle canvas
      '(function(){'
      'var canvas=document.getElementById("sb-particles");'
      'if(!canvas)return;'
      'var ctx=canvas.getContext("2d");'
      'var particles=[];var W,H;'
      'function resize(){'
      'var hero=document.querySelector(".sb-hero");'
      'if(!hero)return;var r=hero.getBoundingClientRect();'
      'W=canvas.width=r.width;H=canvas.height=r.height;'
      'canvas.style.width=r.width+"px";canvas.style.height=r.height+"px";'
      '}'
      'function Particle(){'
      'this.x=Math.random()*W;this.y=Math.random()*H;'
      'this.vx=(Math.random()-0.5)*0.3;this.vy=(Math.random()-0.5)*0.3;'
      'this.r=Math.random()*1.5+0.5;this.a=Math.random()*0.4+0.05;'
      'this.color=["rgba(10,132,255,","rgba(48,209,88,","rgba(191,90,242,"][Math.floor(Math.random()*3)];'
      '}'
      'Particle.prototype.update=function(){'
      'this.x+=this.vx;this.y+=this.vy;'
      'if(this.x<0)this.x=W;if(this.x>W)this.x=0;'
      'if(this.y<0)this.y=H;if(this.y>H)this.y=0;'
      '};'
      'Particle.prototype.draw=function(){'
      'ctx.beginPath();ctx.arc(this.x,this.y,this.r,0,Math.PI*2);'
      'ctx.fillStyle=this.color+this.a+")";ctx.fill();'
      '};'
      'resize();'
      'for(var i=0;i<80;i++){particles.push(new Particle());}'
      'function loop(){'
      'ctx.clearRect(0,0,W,H);'
      'particles.forEach(function(p){p.update();p.draw();});'
      'requestAnimationFrame(loop);'
      '}'
      'loop();'
      'window.addEventListener("resize",resize,{passive:true});'
      '})();'

      '})();'
      '</script>')


# ─── MAIN ─────────────────────────────────────────────────────────────────────
render_banner()
render_nav()
render_hero()
render_about()
render_experience()
render_projects()
render_skills()
render_testimonials()
render_cta()
render_contact()
render_footer()
render_js()
