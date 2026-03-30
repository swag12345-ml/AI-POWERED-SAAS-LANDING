import streamlit as st

st.set_page_config(
    page_title="HIRELYZER — GAMING EDITION",
    page_icon="⚡",
    layout="wide",
)

APP_URL = "https://hirelyzer-supabase-implemented-kf4y7bocccdsmiswtabveh.streamlit.app/"
SUPPORT_EMAIL = "swagato_bmca2024@msit.edu.in"

def H(s):
    st.markdown(s, unsafe_allow_html=True)

def CSS(s):
    st.markdown("<style>" + s + "</style>", unsafe_allow_html=True)

CSS("""
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&display=swap');

:root {
  --cyan:    #00f5ff;
  --magenta: #ff00ff;
  --yellow:  #ffff00;
  --orange:  #ff6600;
  --green:   #00ff41;
  --red:     #ff0033;
  --white:   #ffffff;
  --dim:     rgba(255,255,255,0.55);
  --dimmer:  rgba(255,255,255,0.22);
  --bg:      #000008;
  --bg2:     #04040f;
  --panel:   rgba(0,245,255,0.04);
  --border:  rgba(0,245,255,0.18);
  --border2: rgba(255,0,255,0.18);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
  background-color: var(--bg) !important;
  color: var(--white) !important;
  font-family: 'Rajdhani', sans-serif !important;
  overflow-x: hidden !important;
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

/* ═══════════════════════════════════════════════════
   SCANLINES OVERLAY
═══════════════════════════════════════════════════ */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(0,0,0,0.08) 2px,
    rgba(0,0,0,0.08) 4px
  );
  pointer-events: none;
  z-index: 9999;
  animation: scanMove 8s linear infinite;
}
@keyframes scanMove {
  0%   { background-position: 0 0; }
  100% { background-position: 0 100px; }
}

/* ═══════════════════════════════════════════════════
   SCROLL PROGRESS
═══════════════════════════════════════════════════ */
#sp {
  position: fixed; top: 0; left: 0; height: 3px; width: 0%;
  background: linear-gradient(90deg, var(--cyan), var(--magenta), var(--cyan));
  background-size: 200%;
  z-index: 9998;
  animation: gradShift 2s linear infinite;
  box-shadow: 0 0 12px var(--cyan), 0 0 24px rgba(0,245,255,0.5);
  pointer-events: none;
  transition: width 0.05s linear;
}

/* ═══════════════════════════════════════════════════
   GLOBAL ANIMATIONS
═══════════════════════════════════════════════════ */
@keyframes gradShift {
  0% { background-position: 0% 0%; }
  100% { background-position: 200% 0%; }
}
@keyframes glitch {
  0%,100% { clip-path: none; transform: none; }
  7%  { clip-path: polygon(0 15%, 100% 15%, 100% 22%, 0 22%); transform: translate(-3px, 0); }
  10% { clip-path: none; transform: none; }
  27% { clip-path: polygon(0 65%, 100% 65%, 100% 72%, 0 72%); transform: translate(3px, 0); color: var(--magenta); }
  30% { clip-path: none; transform: none; color: inherit; }
  55% { clip-path: polygon(0 40%, 100% 40%, 100% 48%, 0 48%); transform: translate(-2px, 0); }
  58% { clip-path: none; transform: none; }
}
@keyframes scanline-flash {
  0%,100% { opacity: 0; }
  50%      { opacity: 1; }
}
@keyframes float-hex {
  0%,100% { transform: translateY(0) rotate(0deg); opacity: 0.3; }
  50%     { transform: translateY(-30px) rotate(180deg); opacity: 0.7; }
}
@keyframes pulse-ring {
  0%   { transform: scale(1); opacity: 1; }
  100% { transform: scale(2.5); opacity: 0; }
}
@keyframes cyber-border {
  0%   { border-color: var(--cyan); box-shadow: 0 0 10px var(--cyan), inset 0 0 10px rgba(0,245,255,0.05); }
  33%  { border-color: var(--magenta); box-shadow: 0 0 10px var(--magenta), inset 0 0 10px rgba(255,0,255,0.05); }
  66%  { border-color: var(--cyan); box-shadow: 0 0 10px var(--cyan), inset 0 0 10px rgba(0,245,255,0.05); }
  100% { border-color: var(--cyan); box-shadow: 0 0 10px var(--cyan), inset 0 0 10px rgba(0,245,255,0.05); }
}
@keyframes hud-in {
  from { opacity: 0; transform: translateX(-20px); }
  to   { opacity: 1; transform: none; }
}
@keyframes blink-cursor {
  0%,100% { opacity: 1; }
  50%     { opacity: 0; }
}
@keyframes matrix-fall {
  0%   { transform: translateY(-100%); opacity: 0; }
  10%  { opacity: 1; }
  100% { transform: translateY(100vh); opacity: 0; }
}
@keyframes power-up {
  0%   { transform: scaleX(0); }
  100% { transform: scaleX(1); }
}
@keyframes neon-flicker {
  0%,19%,21%,23%,25%,54%,56%,100% {
    text-shadow: 0 0 7px var(--cyan), 0 0 10px var(--cyan), 0 0 21px var(--cyan), 0 0 42px var(--cyan);
  }
  20%,24%,55% {
    text-shadow: none;
  }
}
@keyframes orbit {
  from { transform: rotate(0deg) translateX(120px) rotate(0deg); }
  to   { transform: rotate(360deg) translateX(120px) rotate(-360deg); }
}
@keyframes slideUp {
  from { opacity:0; transform: translateY(40px) skewX(-2deg); }
  to   { opacity:1; transform: none; }
}
@keyframes grid-pulse {
  0%,100% { opacity: 0.04; }
  50%     { opacity: 0.09; }
}
@keyframes ticker {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ═══════════════════════════════════════════════════
   MATRIX RAIN BACKGROUND
═══════════════════════════════════════════════════ */
#matrix-canvas {
  position: fixed; top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none; z-index: 0;
  opacity: 0.07;
}

/* ═══════════════════════════════════════════════════
   PERSPECTIVE GRID
═══════════════════════════════════════════════════ */
.cyber-grid {
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background-image:
    linear-gradient(rgba(0,245,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,245,255,0.06) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: grid-pulse 4s ease-in-out infinite;
  mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 30%, transparent 100%);
}

/* ═══════════════════════════════════════════════════
   NAV
═══════════════════════════════════════════════════ */
.g-nav {
  position: sticky; top: 0; z-index: 900;
  height: 64px;
  background: rgba(0,0,8,0.9);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(24px);
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 40px rgba(0,245,255,0.08);
}
.g-nav-inner {
  width: 100%; max-width: 1200px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 32px;
}
.g-logo {
  display: flex; align-items: center; gap: 12px;
  font-family: 'Orbitron', monospace;
  font-size: 15px; font-weight: 900;
  color: var(--cyan);
  text-decoration: none;
  letter-spacing: 3px;
  text-shadow: 0 0 20px var(--cyan);
}
.g-logo-hex {
  width: 38px; height: 38px;
  background: linear-gradient(135deg, rgba(0,245,255,0.15), rgba(0,245,255,0.05));
  border: 1px solid var(--cyan);
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  display: flex; align-items: center; justify-content: center;
  font-size: 14px;
  box-shadow: 0 0 15px rgba(0,245,255,0.4);
  animation: cyber-border 3s infinite;
}
.g-nav-links {
  display: flex; align-items: center; gap: 32px;
}
.g-nav-links a {
  font-family: 'Rajdhani', sans-serif;
  font-size: 13px; font-weight: 600;
  color: var(--dim); text-decoration: none;
  letter-spacing: 2px; text-transform: uppercase;
  transition: color 0.2s, text-shadow 0.2s;
  position: relative;
}
.g-nav-links a::after {
  content: '';
  position: absolute; bottom: -4px; left: 0; right: 0; height: 1px;
  background: var(--cyan);
  transform: scaleX(0); transition: transform 0.2s;
  box-shadow: 0 0 6px var(--cyan);
}
.g-nav-links a:hover { color: var(--cyan); text-shadow: 0 0 10px var(--cyan); }
.g-nav-links a:hover::after { transform: scaleX(1); }

.g-nav-cta {
  font-family: 'Orbitron', monospace;
  font-size: 11px; font-weight: 700;
  padding: 10px 24px; letter-spacing: 2px; text-transform: uppercase;
  border: 1px solid var(--cyan);
  color: var(--cyan); text-decoration: none;
  background: rgba(0,245,255,0.05);
  clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
  transition: background 0.2s, box-shadow 0.2s, color 0.2s;
  position: relative; overflow: hidden;
}
.g-nav-cta::before {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(0,245,255,0.2), transparent);
  transform: translateX(-100%);
  transition: transform 0.3s;
}
.g-nav-cta:hover {
  background: rgba(0,245,255,0.12);
  box-shadow: 0 0 20px rgba(0,245,255,0.3);
  color: var(--white);
}
.g-nav-cta:hover::before { transform: translateX(0); }

/* ═══════════════════════════════════════════════════
   ANNOUNCEMENT BANNER
═══════════════════════════════════════════════════ */
.g-banner {
  background: linear-gradient(90deg, transparent, rgba(0,245,255,0.06), rgba(255,0,255,0.04), transparent);
  border-bottom: 1px solid rgba(0,245,255,0.12);
  padding: 9px 32px; text-align: center;
  font-family: 'Share Tech Mono', monospace;
  font-size: 12px; color: var(--dim);
  display: flex; align-items: center; justify-content: center; gap: 12px;
  position: relative; z-index: 901;
}
.g-banner-badge {
  font-family: 'Orbitron', monospace;
  font-size: 9px; font-weight: 700; letter-spacing: 2px;
  padding: 3px 10px;
  border: 1px solid var(--green);
  color: var(--green);
  text-shadow: 0 0 8px var(--green);
  animation: neon-flicker 4s infinite;
}
.g-banner a {
  color: var(--cyan); font-weight: 700; text-decoration: none;
  text-shadow: 0 0 6px var(--cyan);
}

/* ═══════════════════════════════════════════════════
   HERO
═══════════════════════════════════════════════════ */
.g-hero {
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center;
  padding: 80px 32px;
  position: relative; overflow: hidden;
  background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,245,255,0.06) 0%, transparent 60%),
              radial-gradient(ellipse 60% 50% at 80% 80%, rgba(255,0,255,0.04) 0%, transparent 60%),
              var(--bg);
}

/* Corner HUD brackets */
.g-hero::before {
  content: '';
  position: absolute;
  top: 40px; left: 40px;
  width: 60px; height: 60px;
  border-top: 2px solid var(--cyan);
  border-left: 2px solid var(--cyan);
  box-shadow: 0 0 10px var(--cyan);
  pointer-events: none;
}
.g-hero::after {
  content: '';
  position: absolute;
  bottom: 80px; right: 40px;
  width: 60px; height: 60px;
  border-bottom: 2px solid var(--magenta);
  border-right: 2px solid var(--magenta);
  box-shadow: 0 0 10px var(--magenta);
  pointer-events: none;
}

/* Orbiting elements */
.g-hero-orbit {
  position: absolute;
  top: 50%; left: 50%;
  width: 1px; height: 1px;
  pointer-events: none; z-index: 0;
}
.g-orbit-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(0,245,255,0.08);
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
}

.g-hero-content { position: relative; z-index: 1; }

.g-status-bar {
  display: inline-flex; align-items: center; gap: 8px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 11px; color: var(--green);
  padding: 6px 18px;
  border: 1px solid rgba(0,255,65,0.3);
  background: rgba(0,255,65,0.04);
  margin-bottom: 32px;
  letter-spacing: 2px;
  text-transform: uppercase;
  animation: slideUp 0.5s ease both;
}
.g-status-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 8px var(--green);
  animation: blink-cursor 1s step-end infinite;
}

.g-h1 {
  font-family: 'Orbitron', monospace;
  font-size: clamp(40px, 8vw, 100px);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -2px;
  color: var(--white);
  max-width: 1000px;
  margin: 0 auto;
  animation: slideUp 0.5s 0.1s ease both;
}
.g-h1-glitch {
  display: block;
  color: var(--cyan);
  text-shadow: 0 0 30px var(--cyan), 0 0 60px rgba(0,245,255,0.3);
  animation: glitch 8s infinite, slideUp 0.5s 0.15s ease both;
  position: relative;
}
.g-h1-glitch::before {
  content: attr(data-text);
  position: absolute; inset: 0;
  color: var(--magenta);
  clip-path: polygon(0 30%, 100% 30%, 100% 40%, 0 40%);
  transform: translateX(-3px);
  animation: glitch 8s 0.5s infinite;
  opacity: 0.6;
}
.g-h1-sub {
  display: block; font-size: 0.55em;
  color: var(--dim);
  letter-spacing: 8px;
  font-weight: 400;
  margin-top: 8px;
}

/* Typewriter */
.g-typewriter-wrap {
  display: inline-block;
  color: var(--magenta);
  text-shadow: 0 0 20px var(--magenta);
}
.g-cursor {
  display: inline-block;
  width: 4px; height: 0.75em;
  background: var(--cyan);
  margin-left: 4px; vertical-align: middle;
  animation: blink-cursor 0.8s step-end infinite;
  box-shadow: 0 0 8px var(--cyan);
}

.g-hero-desc {
  font-size: clamp(15px, 2vw, 19px);
  color: var(--dim); line-height: 1.8;
  max-width: 560px; margin: 32px auto 0;
  font-weight: 400; letter-spacing: 0.5px;
  animation: slideUp 0.5s 0.2s ease both;
}

/* HUD stats row */
.g-hud-row {
  display: flex; align-items: center; justify-content: center; gap: 40px;
  margin-top: 52px;
  animation: slideUp 0.5s 0.25s ease both;
}
.g-hud-stat {
  display: flex; flex-direction: column; align-items: center; gap: 4px;
  position: relative; padding: 0 20px;
}
.g-hud-stat::after {
  content: '';
  position: absolute; right: 0; top: 10%; bottom: 10%;
  width: 1px;
  background: linear-gradient(180deg, transparent, var(--border), transparent);
}
.g-hud-stat:last-child::after { display: none; }
.g-hud-num {
  font-family: 'Orbitron', monospace;
  font-size: 28px; font-weight: 900;
  color: var(--cyan);
  text-shadow: 0 0 20px var(--cyan);
}
.g-hud-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 10px; color: var(--dimmer);
  letter-spacing: 2px; text-transform: uppercase;
}

/* CTA buttons */
.g-ctas {
  display: flex; gap: 16px; justify-content: center; margin-top: 48px; flex-wrap: wrap;
  animation: slideUp 0.5s 0.3s ease both;
}
.g-btn-primary {
  font-family: 'Orbitron', monospace;
  font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
  padding: 16px 40px;
  background: linear-gradient(135deg, rgba(0,245,255,0.15), rgba(0,245,255,0.05));
  border: 1px solid var(--cyan);
  color: var(--cyan); text-decoration: none;
  clip-path: polygon(12px 0%, 100% 0%, calc(100% - 12px) 100%, 0% 100%);
  position: relative; overflow: hidden;
  transition: all 0.2s;
  box-shadow: 0 0 20px rgba(0,245,255,0.2), inset 0 0 20px rgba(0,245,255,0.03);
}
.g-btn-primary::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(0,245,255,0.3), rgba(0,245,255,0.1));
  transform: translateX(-100%); transition: transform 0.3s;
}
.g-btn-primary:hover {
  color: var(--white);
  box-shadow: 0 0 40px rgba(0,245,255,0.4), inset 0 0 30px rgba(0,245,255,0.1);
  transform: translateY(-2px);
}
.g-btn-primary:hover::before { transform: translateX(0); }

.g-btn-secondary {
  font-family: 'Orbitron', monospace;
  font-size: 12px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
  padding: 16px 40px;
  background: transparent;
  border: 1px solid rgba(255,255,255,0.15);
  color: var(--dim); text-decoration: none;
  clip-path: polygon(12px 0%, 100% 0%, calc(100% - 12px) 100%, 0% 100%);
  transition: all 0.2s;
}
.g-btn-secondary:hover {
  border-color: var(--magenta);
  color: var(--magenta);
  box-shadow: 0 0 20px rgba(255,0,255,0.2);
}

/* Scroll indicator */
.g-scroll-hint {
  margin-top: 60px;
  display: flex; flex-direction: column; align-items: center; gap: 8px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 10px; color: var(--dimmer); letter-spacing: 3px;
  animation: slideUp 0.5s 0.4s ease both;
}
.g-scroll-line {
  width: 1px; height: 40px;
  background: linear-gradient(180deg, var(--cyan), transparent);
  animation: power-up 2s ease-in-out infinite;
  box-shadow: 0 0 6px var(--cyan);
}

/* ═══════════════════════════════════════════════════
   SECTION WRAPPER
═══════════════════════════════════════════════════ */
.g-section {
  padding: 100px 32px; position: relative; max-width: 1200px; margin: 0 auto;
}
.g-section-full {
  padding: 100px 0; position: relative;
}
.g-section-header {
  text-align: center; margin-bottom: 64px;
}
.g-section-eyebrow {
  font-family: 'Share Tech Mono', monospace;
  font-size: 11px; letter-spacing: 4px; text-transform: uppercase;
  color: var(--cyan); margin-bottom: 16px;
  display: flex; align-items: center; justify-content: center; gap: 12px;
}
.g-section-eyebrow::before,
.g-section-eyebrow::after {
  content: '';
  display: block; width: 40px; height: 1px;
  background: linear-gradient(90deg, transparent, var(--cyan));
}
.g-section-eyebrow::after { transform: scaleX(-1); }
.g-section-h2 {
  font-family: 'Orbitron', monospace;
  font-size: clamp(24px, 4vw, 44px);
  font-weight: 800; color: var(--white);
  letter-spacing: -1px; line-height: 1.1;
}
.g-section-h2 .accent { color: var(--cyan); text-shadow: 0 0 20px var(--cyan); }
.g-section-h2 .accent-m { color: var(--magenta); text-shadow: 0 0 20px var(--magenta); }
.g-section-sub {
  font-size: 16px; color: var(--dim); margin-top: 14px; line-height: 1.7; letter-spacing: 0.3px;
}

/* ═══════════════════════════════════════════════════
   HOW IT WORKS — MISSION STEPS
═══════════════════════════════════════════════════ */
.g-steps {
  display: grid; grid-template-columns: repeat(4,1fr); gap: 0;
  margin-top: 56px;
  border: 1px solid var(--border); border-radius: 4px;
  overflow: hidden;
}
.g-step {
  padding: 36px 28px;
  border-right: 1px solid var(--border);
  position: relative; overflow: hidden;
  background: rgba(0,0,8,0.9);
  transition: background 0.3s;
}
.g-step:last-child { border-right: none; }
.g-step::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cyan), var(--magenta));
  transform: scaleX(0); transition: transform 0.4s;
}
.g-step:hover { background: rgba(0,245,255,0.03); }
.g-step:hover::before { transform: scaleX(1); }
.g-step-num {
  font-family: 'Orbitron', monospace;
  font-size: 10px; font-weight: 700; letter-spacing: 3px;
  color: var(--dimmer); margin-bottom: 16px;
  display: flex; align-items: center; gap: 8px;
}
.g-step-num::after {
  content: '';
  flex: 1; height: 1px;
  background: linear-gradient(90deg, var(--border), transparent);
}
.g-step-icon {
  font-size: 28px; margin-bottom: 16px;
  filter: drop-shadow(0 0 8px var(--cyan));
}
.g-step-title {
  font-family: 'Orbitron', monospace;
  font-size: 13px; font-weight: 700;
  color: var(--white); margin-bottom: 10px;
  letter-spacing: 0.5px;
}
.g-step-desc {
  font-size: 13px; color: var(--dim); line-height: 1.7;
}

/* ═══════════════════════════════════════════════════
   FEATURE PANELS — STORY SECTIONS
═══════════════════════════════════════════════════ */
.g-story {
  padding: 80px 32px; position: relative;
  border-top: 1px solid rgba(255,255,255,0.04);
}
.g-story-inner {
  max-width: 1200px; margin: 0 auto;
  display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;
}
.g-story-inner.rev { direction: rtl; }
.g-story-inner.rev > * { direction: ltr; }

.g-story-label {
  font-family: 'Share Tech Mono', monospace;
  font-size: 10px; letter-spacing: 4px; text-transform: uppercase;
  color: var(--cyan); margin-bottom: 20px;
  display: flex; align-items: center; gap: 8px;
}
.g-story-label-dot {
  width: 5px; height: 5px; border-radius: 50%;
  background: var(--cyan); box-shadow: 0 0 8px var(--cyan);
}
.g-story-h {
  font-family: 'Orbitron', monospace;
  font-size: clamp(20px, 3vw, 32px);
  font-weight: 800; color: var(--white);
  line-height: 1.15; letter-spacing: -0.5px; margin-bottom: 18px;
}
.g-story-p {
  font-size: 15px; color: var(--dim); line-height: 1.85;
  margin-bottom: 20px; letter-spacing: 0.2px;
}

/* Cyber panel card */
.g-panel {
  background: rgba(0,0,12,0.95);
  border: 1px solid var(--border);
  border-radius: 4px; padding: 28px;
  position: relative; overflow: hidden;
  box-shadow: 0 0 40px rgba(0,245,255,0.05);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.g-panel::before {
  content: '';
  position: absolute; top: 0; left: 0;
  width: 100%; height: 2px;
  background: linear-gradient(90deg, var(--cyan), var(--magenta), transparent);
}
.g-panel::after {
  content: '';
  position: absolute; top: 4px; right: 4px;
  width: 8px; height: 8px;
  border-top: 1px solid var(--cyan);
  border-right: 1px solid var(--cyan);
}
.g-panel:hover {
  border-color: rgba(0,245,255,0.35);
  box-shadow: 0 0 60px rgba(0,245,255,0.08), 0 20px 40px rgba(0,0,0,0.5);
  transform: translateY(-3px);
}

/* ── Pills ── */
.g-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 16px; }
.g-pill {
  font-family: 'Share Tech Mono', monospace;
  font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase;
  padding: 5px 12px;
  border: 1px solid rgba(0,245,255,0.2);
  color: rgba(0,245,255,0.7);
  background: rgba(0,245,255,0.04);
  clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.g-pill:hover {
  border-color: var(--cyan);
  color: var(--cyan);
  background: rgba(0,245,255,0.08);
  box-shadow: 0 0 10px rgba(0,245,255,0.15);
}

/* ── ATS Score visualization ── */
.g-ats-meter {
  margin-bottom: 20px;
}
.g-meter-label {
  display: flex; justify-content: space-between; align-items: center;
  font-family: 'Share Tech Mono', monospace;
  font-size: 11px; color: var(--dim); margin-bottom: 6px;
}
.g-meter-value {
  font-size: 13px; font-weight: 700; color: var(--cyan);
  text-shadow: 0 0 8px var(--cyan);
}
.g-meter-bar {
  height: 4px; background: rgba(255,255,255,0.06);
  border-radius: 0; overflow: hidden; position: relative;
}
.g-meter-fill {
  height: 100%; border-radius: 0;
  animation: power-up 1.2s cubic-bezier(0.16,1,0.3,1) both;
  position: relative;
}
.g-meter-fill::after {
  content: '';
  position: absolute; right: 0; top: -2px; bottom: -2px; width: 3px;
  background: inherit;
  box-shadow: 0 0 8px currentColor;
  filter: brightness(2);
}

/* ── Mini resume templates ── */
.g-tmpl-grid {
  display: grid; grid-template-columns: repeat(4,1fr); gap: 8px; margin-bottom: 16px;
}
.g-tmpl {
  border-radius: 4px; border: 1px solid rgba(0,245,255,0.1);
  background: rgba(0,0,12,0.9); overflow: hidden;
  display: flex; flex-direction: column; min-height: 100px;
  position: relative; cursor: pointer;
  transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
}
.g-tmpl:hover { border-color: var(--cyan); transform: translateY(-3px); box-shadow: 0 0 15px rgba(0,245,255,0.15); }
.g-tmpl-act { border-color: var(--cyan) !important; box-shadow: 0 0 15px rgba(0,245,255,0.2) !important; }
.g-tmpl-hdr { height: 4px; }
.g-tmpl-ln { height: 2px; border-radius: 1px; background: rgba(255,255,255,0.1); margin: 2px 4px; }
.g-tmpl-badge {
  position: absolute; bottom: 4px; left: 4px; right: 4px;
  background: rgba(0,245,255,0.1); border: 1px solid rgba(0,245,255,0.25);
  border-radius: 2px; padding: 2px 4px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 7px; color: var(--cyan); text-align: center; letter-spacing: 0.5px;
}

/* ── Job cards ── */
.g-job {
  padding: 12px 16px;
  border: 1px solid rgba(255,255,255,0.06);
  background: rgba(0,0,12,0.9);
  display: flex; align-items: center; gap: 12px; margin-bottom: 8px;
  transition: border-color 0.2s, transform 0.2s;
  position: relative;
}
.g-job::before {
  content: '';
  position: absolute; left: 0; top: 0; bottom: 0; width: 2px;
  background: var(--cyan);
  transform: scaleY(0); transition: transform 0.2s;
}
.g-job:hover { border-color: rgba(0,245,255,0.2); transform: translateX(4px); }
.g-job:hover::before { transform: scaleY(1); }
.g-job-logo {
  width: 34px; height: 34px; border-radius: 2px;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 12px; flex-shrink: 0;
  font-family: 'Orbitron', monospace;
}
.g-job-title { font-size: 13px; font-weight: 600; color: var(--white); font-family: 'Rajdhani', sans-serif; letter-spacing: 0.5px; }
.g-job-co { font-size: 11px; color: var(--dimmer); margin-top: 1px; font-family: 'Share Tech Mono', monospace; }
.g-job-badge {
  padding: 3px 10px; font-size: 9px; font-weight: 700; white-space: nowrap;
  flex-shrink: 0; font-family: 'Orbitron', monospace; letter-spacing: 1px;
  clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
}

/* ═══════════════════════════════════════════════════
   TESTIMONIALS TICKER
═══════════════════════════════════════════════════ */
.g-ticker-wrap {
  overflow: hidden; padding: 48px 0;
  border-top: 1px solid rgba(0,245,255,0.06);
  border-bottom: 1px solid rgba(0,245,255,0.06);
  background: linear-gradient(180deg, transparent, rgba(0,245,255,0.015), transparent);
  mask-image: linear-gradient(90deg, transparent, black 6%, black 94%, transparent);
}
.g-ticker-track {
  display: flex; gap: 20px; width: max-content;
  animation: ticker 40s linear infinite;
}
.g-ticker-track:hover { animation-play-state: paused; }
.g-ticker-item {
  border: 1px solid rgba(0,245,255,0.1);
  background: rgba(0,0,12,0.9);
  padding: 20px 24px; min-width: 300px; max-width: 340px;
  flex-shrink: 0;
  clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
  transition: border-color 0.2s;
  position: relative;
}
.g-ticker-item::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, var(--cyan), transparent);
}
.g-ticker-item:hover { border-color: rgba(0,245,255,0.3); }
.g-ticker-stars { color: var(--cyan); font-size: 10px; margin-bottom: 8px; letter-spacing: 2px; text-shadow: 0 0 8px var(--cyan); }
.g-ticker-quote { font-size: 13px; color: var(--dim); line-height: 1.7; margin-bottom: 14px; font-style: italic; }
.g-ticker-author { display: flex; align-items: center; gap: 10px; }
.g-ticker-avatar {
  width: 32px; height: 32px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 700; flex-shrink: 0;
  font-family: 'Orbitron', monospace;
  border: 1px solid var(--border);
}
.g-ticker-name {
  font-size: 12px; font-weight: 700; color: var(--white);
  font-family: 'Orbitron', monospace; font-size: 10px; letter-spacing: 1px;
}
.g-ticker-role { font-size: 11px; color: var(--dimmer); font-family: 'Share Tech Mono', monospace; }

/* ═══════════════════════════════════════════════════
   COMPARISON TABLE
═══════════════════════════════════════════════════ */
.g-compare-wrap {
  margin-top: 52px;
  border: 1px solid var(--border); overflow: hidden;
}
.g-compare-head, .g-compare-row {
  display: grid; grid-template-columns: 1.8fr 1fr 1fr 1fr;
}
.g-compare-head {
  background: rgba(0,0,12,0.98);
  border-bottom: 1px solid var(--border);
}
.g-compare-row {
  border-bottom: 1px solid rgba(255,255,255,0.03);
  transition: background 0.15s;
}
.g-compare-row:last-child { border-bottom: none; }
.g-compare-row:hover { background: rgba(255,255,255,0.01); }
.g-ch {
  padding: 14px 20px;
  font-family: 'Orbitron', monospace;
  font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;
  color: var(--dimmer);
}
.g-ch-hl {
  background: rgba(0,245,255,0.05);
  border-left: 1px solid rgba(0,245,255,0.15);
  border-right: 1px solid rgba(0,245,255,0.15);
  color: var(--cyan); display: flex; align-items: center; gap: 6px; justify-content: center;
}
.g-cc { padding: 14px 20px; font-size: 13px; color: var(--dim); display: flex; align-items: center; }
.g-cc-feat { font-weight: 600; color: var(--white); font-size: 13px; font-family: 'Rajdhani', sans-serif; letter-spacing: 0.3px; }
.g-cc-feat small { display: block; font-size: 11px; color: var(--dimmer); font-weight: 400; margin-top: 1px; font-family: 'Share Tech Mono', monospace; }
.g-cc-hl {
  background: rgba(0,245,255,0.03);
  border-left: 1px solid rgba(0,245,255,0.08);
  border-right: 1px solid rgba(0,245,255,0.08);
  justify-content: center; font-weight: 700; color: var(--white);
}
.g-cc-center { justify-content: center; }
.g-chk-y { color: var(--cyan); font-size: 14px; text-shadow: 0 0 8px var(--cyan); }
.g-chk-n { color: rgba(255,255,255,0.12); font-size: 16px; }
.g-chk-p { color: var(--orange); font-size: 10px; font-weight: 700; font-family: 'Share Tech Mono', monospace; }

/* ═══════════════════════════════════════════════════
   FEATURE GRID
═══════════════════════════════════════════════════ */
.g-feat-grid {
  display: grid; grid-template-columns: repeat(3,1fr); gap: 1px;
  margin-top: 56px;
  background: rgba(0,245,255,0.06);
  border: 1px solid var(--border);
}
.g-feat {
  padding: 36px 30px;
  background: var(--bg2);
  position: relative; overflow: hidden;
  transition: background 0.3s;
}
.g-feat:hover { background: rgba(0,245,255,0.02); }
.g-feat::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,245,255,0.12), transparent);
}
.g-feat::after {
  content: '';
  position: absolute; bottom: 0; left: 0; width: 0;
  height: 1px; background: var(--cyan);
  transition: width 0.4s;
}
.g-feat:hover::after { width: 100%; }
.g-feat-icon {
  width: 44px; height: 44px;
  border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 20px; font-size: 18px;
  clip-path: polygon(6px 0%, 100% 0%, calc(100% - 6px) 100%, 0% 100%);
  background: rgba(0,245,255,0.04);
}
.g-feat-title {
  font-family: 'Orbitron', monospace;
  font-size: 12px; font-weight: 700; color: var(--white);
  margin-bottom: 10px; letter-spacing: 0.5px;
}
.g-feat-desc { font-size: 13px; color: var(--dim); line-height: 1.7; }

/* ═══════════════════════════════════════════════════
   FAQ
═══════════════════════════════════════════════════ */
.g-faq-list { max-width: 760px; margin: 56px auto 0; }
.g-faq-item {
  border: 1px solid rgba(0,245,255,0.08);
  background: rgba(0,0,12,0.9);
  margin-bottom: 4px; overflow: hidden;
  transition: border-color 0.2s;
}
.g-faq-item:hover { border-color: rgba(0,245,255,0.2); }
.g-faq-q {
  padding: 18px 24px;
  font-size: 14px; font-weight: 600; color: var(--white);
  display: flex; justify-content: space-between; align-items: center;
  cursor: pointer; gap: 12px;
  font-family: 'Rajdhani', sans-serif; letter-spacing: 0.3px;
}
.g-faq-q-icon {
  width: 24px; height: 24px; flex-shrink: 0;
  border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; color: var(--cyan);
  clip-path: polygon(4px 0%, 100% 0%, calc(100% - 4px) 100%, 0% 100%);
  background: rgba(0,245,255,0.05);
}
.g-faq-a { padding: 0 24px 18px; font-size: 14px; color: var(--dim); line-height: 1.8; }

/* ═══════════════════════════════════════════════════
   CTA SECTION
═══════════════════════════════════════════════════ */
.g-cta-section {
  margin: 0 32px 100px;
  padding: 80px 60px; text-align: center;
  border: 1px solid var(--border); position: relative; overflow: hidden;
  background: rgba(0,0,12,0.95);
  clip-path: polygon(20px 0%, 100% 0%, calc(100% - 20px) 100%, 0% 100%);
}
.g-cta-section::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 70% 50% at 50% -10%, rgba(0,245,255,0.08) 0%, transparent 60%),
              radial-gradient(ellipse 40% 40% at 80% 80%, rgba(255,0,255,0.04) 0%, transparent 60%);
  pointer-events: none;
}
.g-cta-corner-tl, .g-cta-corner-br {
  position: absolute; width: 30px; height: 30px;
}
.g-cta-corner-tl {
  top: 12px; left: 30px;
  border-top: 2px solid var(--cyan); border-left: 2px solid var(--cyan);
}
.g-cta-corner-br {
  bottom: 12px; right: 30px;
  border-bottom: 2px solid var(--magenta); border-right: 2px solid var(--magenta);
}
.g-cta-h {
  font-family: 'Orbitron', monospace;
  font-size: clamp(24px, 4vw, 48px); font-weight: 900;
  letter-spacing: -1px; color: var(--white); line-height: 1.05;
  max-width: 700px; margin: 0 auto 20px; position: relative; z-index: 1;
}
.g-cta-sub {
  font-size: 16px; color: var(--dim);
  margin: 0 auto 40px; max-width: 500px; line-height: 1.7;
  position: relative; z-index: 1;
}
.g-cta-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }

/* ═══════════════════════════════════════════════════
   CONTACT
═══════════════════════════════════════════════════ */
.g-contact-card {
  border: 1px solid var(--border);
  background: rgba(0,0,12,0.95);
  padding: 44px; max-width: 560px; margin: 0 auto 80px;
  text-align: center; position: relative;
  clip-path: polygon(16px 0%, 100% 0%, calc(100% - 16px) 100%, 0% 100%);
}
.g-contact-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cyan), var(--magenta), var(--cyan));
}
.g-contact-card h3 {
  font-family: 'Orbitron', monospace;
  font-size: 18px; font-weight: 800; color: var(--white);
  letter-spacing: 0px; margin-bottom: 10px;
}
.g-contact-card p { font-size: 14px; color: var(--dim); line-height: 1.7; margin-bottom: 28px; }
.g-contact-email {
  display: inline-flex; align-items: center; gap: 10px;
  padding: 14px 28px;
  border: 1px solid rgba(0,245,255,0.25);
  color: var(--cyan); font-size: 13px; font-weight: 600; text-decoration: none;
  font-family: 'Share Tech Mono', monospace;
  clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
  background: rgba(0,245,255,0.05);
  transition: background 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.g-contact-email:hover {
  background: rgba(0,245,255,0.1);
  border-color: var(--cyan);
  box-shadow: 0 0 20px rgba(0,245,255,0.2);
}

/* ═══════════════════════════════════════════════════
   FOOTER
═══════════════════════════════════════════════════ */
.g-footer {
  border-top: 1px solid rgba(0,245,255,0.08);
  padding: 40px 32px;
  display: flex; align-items: center; justify-content: space-between;
  max-width: 1200px; margin: 0 auto; gap: 20px;
  flex-wrap: wrap;
}
.g-footer-copy {
  font-family: 'Share Tech Mono', monospace;
  font-size: 11px; color: var(--dimmer); letter-spacing: 1px;
}
.g-footer-links { display: flex; gap: 24px; }
.g-footer-links a {
  font-family: 'Share Tech Mono', monospace;
  font-size: 11px; color: var(--dimmer); text-decoration: none;
  letter-spacing: 1px; transition: color 0.2s;
}
.g-footer-links a:hover { color: var(--cyan); text-shadow: 0 0 6px var(--cyan); }

/* ═══════════════════════════════════════════════════
   STICKY CTA BAR
═══════════════════════════════════════════════════ */
#g-sticky {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 890;
  background: rgba(0,0,8,0.96);
  border-top: 1px solid var(--border);
  backdrop-filter: blur(24px);
  padding: 12px 32px;
  display: flex; align-items: center; justify-content: space-between;
  transform: translateY(100%); transition: transform 0.4s cubic-bezier(0.16,1,0.3,1);
  box-shadow: 0 -4px 30px rgba(0,245,255,0.08);
}
#g-sticky.visible { transform: translateY(0); }
.g-sticky-inner { max-width: 1200px; width: 100%; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.g-sticky-text {
  font-family: 'Share Tech Mono', monospace;
  font-size: 12px; color: var(--dim); letter-spacing: 1px;
}
.g-sticky-text strong { color: var(--cyan); }
.g-sticky-btns { display: flex; gap: 10px; align-items: center; }
#g-sticky-dismiss {
  background: none; border: none; color: var(--dimmer);
  font-size: 20px; cursor: pointer; padding: 4px 8px; line-height: 1;
  transition: color 0.2s;
}
#g-sticky-dismiss:hover { color: var(--white); }

/* ═══════════════════════════════════════════════════
   SECTION DOT NAV
═══════════════════════════════════════════════════ */
#g-dots {
  position: fixed; right: 20px; top: 50%; transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 10px; z-index: 800;
}
.g-dot-nav {
  width: 6px; height: 6px;
  background: rgba(0,245,255,0.15);
  cursor: pointer; transition: all 0.3s;
  border: none; padding: 0;
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
}
.g-dot-nav.active {
  background: var(--cyan);
  transform: scale(1.6);
  box-shadow: 0 0 10px var(--cyan);
}
.g-dot-nav:hover { background: rgba(0,245,255,0.5); }

/* ═══════════════════════════════════════════════════
   TOAST
═══════════════════════════════════════════════════ */
#g-toast {
  position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%) translateY(20px);
  background: rgba(0,0,12,0.97);
  border: 1px solid var(--cyan);
  padding: 10px 20px;
  font-family: 'Share Tech Mono', monospace;
  font-size: 12px; color: var(--white);
  display: flex; align-items: center; gap: 8px; z-index: 9998;
  opacity: 0; transition: opacity 0.3s, transform 0.3s; pointer-events: none;
  box-shadow: 0 0 20px rgba(0,245,255,0.2);
  clip-path: polygon(8px 0%, 100% 0%, calc(100% - 8px) 100%, 0% 100%);
  letter-spacing: 1px;
}
#g-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
#g-toast-dot { width: 6px; height: 6px; background: var(--green); box-shadow: 0 0 8px var(--green); flex-shrink: 0; }

/* ═══════════════════════════════════════════════════
   RADAR
═══════════════════════════════════════════════════ */
.g-radar-polygon {
  stroke-dasharray: 1000; stroke-dashoffset: 1000;
  transition: stroke-dashoffset 1.8s cubic-bezier(0.4,0,0.2,1);
}
.g-radar-polygon.drawn { stroke-dashoffset: 0; }
.g-radar-dot {
  opacity: 0; transform: scale(0);
  transition: opacity 0.4s ease, transform 0.4s ease;
}
.g-radar-dot.drawn { opacity: 1; transform: scale(1); }

/* ═══════════════════════════════════════════════════
   RESPONSIVE
═══════════════════════════════════════════════════ */
@media (max-width: 900px) {
  .g-story-inner { grid-template-columns: 1fr; gap: 40px; }
  .g-story-inner.rev { direction: ltr; }
  .g-steps { grid-template-columns: 1fr 1fr; }
  .g-step { border-right: none; border-bottom: 1px solid var(--border); }
  .g-feat-grid { grid-template-columns: 1fr; }
  .g-nav-links { display: none; }
  .g-cta-section { margin: 0 16px 60px; padding: 60px 28px; }
  .g-hud-row { gap: 20px; }
  .g-tmpl-grid { grid-template-columns: repeat(2,1fr); }
  #g-dots { display: none; }
}
@media (max-width: 600px) {
  .g-steps { grid-template-columns: 1fr; }
  .g-compare-wrap { overflow-x: auto; }
}
""")

# ─────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────

def chk_y(): return '<span class="g-chk-y">⬡</span>'
def chk_n(): return '<span class="g-chk-n">—</span>'
def chk_p(t): return f'<span class="g-chk-p">{t}</span>'

def g_pill(labels):
    return "".join(f'<span class="g-pill">{l}</span>' for l in labels)

def g_job_cards():
    jobs = [
        ("SDE II","Google","MTN VIEW · FULL-TIME","#00b4f5","G",True),
        ("ML Engineer","Anthropic","REMOTE · FULL-TIME","#ff9f0a","A",False),
        ("Backend Dev","Razorpay","BANGALORE · FULL-TIME","#7c3aed","R",False),
        ("Data Analyst","Zepto","MUMBAI · HYBRID","#00ff41","Z",False),
    ]
    out = ""
    for title,co,meta,col,letter,featured in jobs:
        if featured:
            bb="rgba(0,245,255,0.1)"; bc="var(--cyan)"; btx="FEATURED"
            shadow=";box-shadow:0 0 10px rgba(0,245,255,0.2)"
        else:
            bb="rgba(255,255,255,0.03)"; bc="rgba(255,255,255,0.3)"; btx="NEW"; shadow=""
        out += (f'<div class="g-job">'
                f'<div class="g-job-logo" style="background:{col}22;color:{col}">{letter}</div>'
                f'<div style="flex:1;min-width:0">'
                f'<div class="g-job-title">{title} — {co}</div>'
                f'<div class="g-job-co">{meta}</div></div>'
                f'<div class="g-job-badge" style="background:{bb};color:{bc};border:1px solid {bc}44{shadow}">{btx}</div>'
                f'</div>')
    return out

def ats_meter(label, pct, color="var(--cyan)"):
    return (f'<div class="g-ats-meter">'
            f'<div class="g-meter-label"><span>{label}</span>'
            f'<span class="g-meter-value" style="color:{color};text-shadow:0 0 8px {color}">{pct}%</span></div>'
            f'<div class="g-meter-bar">'
            f'<div class="g-meter-fill" style="width:{pct}%;background:{color}"></div>'
            f'</div></div>')

def mini_template(name, color, active=False):
    act = ' g-tmpl-act' if active else ''
    return (f'<div class="g-tmpl{act}">'
            f'<div class="g-tmpl-hdr" style="background:{color}"></div>'
            f'<div style="padding:4px">'
            f'<div class="g-tmpl-ln" style="width:70%"></div>'
            f'<div class="g-tmpl-ln" style="width:50%"></div>'
            f'<div class="g-tmpl-ln" style="width:80%"></div>'
            f'<div class="g-tmpl-ln" style="width:60%"></div>'
            f'</div>'
            f'<div class="g-tmpl-badge">{name}</div>'
            f'</div>')

def radar_chart(skills, scores, color="00f5ff"):
    import math
    n = len(skills)
    cx, cy, r = 130, 130, 100
    grid_html = ""
    for ring in [0.25, 0.5, 0.75, 1.0]:
        pts = " ".join(f"{cx + r*ring*math.cos(math.pi/2 - 2*math.pi*i/n):.1f},{cy - r*ring*math.sin(math.pi/2 - 2*math.pi*i/n):.1f}" for i in range(n))
        grid_html += f'<polygon points="{pts}" fill="none" stroke="#{color}" stroke-width="0.5" opacity="0.2"/>'
    for i in range(n):
        x2 = cx + r*math.cos(math.pi/2 - 2*math.pi*i/n)
        y2 = cy - r*math.sin(math.pi/2 - 2*math.pi*i/n)
        grid_html += f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#{color}" stroke-width="0.5" opacity="0.2"/>'
    pts_main = " ".join(f"{cx + r*(s/100)*math.cos(math.pi/2 - 2*math.pi*i/n):.1f},{cy - r*(s/100)*math.sin(math.pi/2 - 2*math.pi*i/n):.1f}" for i,(s) in enumerate(scores))
    dot_html = ""
    for i, s in enumerate(scores):
        dx = cx + r*(s/100)*math.cos(math.pi/2 - 2*math.pi*i/n)
        dy = cy - r*(s/100)*math.sin(math.pi/2 - 2*math.pi*i/n)
        dot_html += f'<circle class="g-radar-dot" cx="{dx:.1f}" cy="{dy:.1f}" r="4" fill="#{color}" stroke="#{color}" stroke-width="1"/>'
    label_html = ""
    for i, sk in enumerate(skills):
        lx = cx + (r+18)*math.cos(math.pi/2 - 2*math.pi*i/n)
        ly = cy - (r+18)*math.sin(math.pi/2 - 2*math.pi*i/n)
        anchor = "middle" if abs(lx-cx)<5 else ("start" if lx>cx else "end")
        label_html += f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" fill="rgba(255,255,255,0.5)" font-size="8" font-family="Share Tech Mono,monospace">{sk}</text>'
    return (f'<svg id="g-radar-svg" viewBox="0 0 260 260" xmlns="http://www.w3.org/2000/svg" width="100%">'
            f'{grid_html}'
            f'<polygon id="g-radar-poly" class="g-radar-polygon" points="{pts_main}" fill="rgba(0,245,255,0.1)" stroke="#{color}" stroke-width="2"/>'
            f'{dot_html}{label_html}'
            f'</svg>')

# ─────────────────────────────────────────────────────────────────
# SECTIONS
# ─────────────────────────────────────────────────────────────────

def render_banner():
    H(f'<div class="g-banner">'
      f'<span class="g-banner-badge">// LIVE</span>'
      f'AI Interview Coach deployed — practice with resume-based missions &amp; get instant scoring. '
      f'<a href="{APP_URL}" target="_blank">BOOT UP &rarr;</a>'
      f'</div>')

def render_nav():
    H('<div id="sp"></div>'
      '<canvas id="matrix-canvas"></canvas>'
      '<div class="cyber-grid"></div>'

      # Toast
      '<div id="g-toast"><div id="g-toast-dot"></div><span id="g-toast-msg"></span></div>'

      # Sticky CTA
      '<div id="g-sticky">'
      '<div class="g-sticky-inner">'
      '<span class="g-sticky-text">// SYSTEM READY — <strong>HIRELYZER</strong> — YOUR CAREER PLATFORM</span>'
      '<div class="g-sticky-btns">'
      f'<a href="{APP_URL}" target="_blank" class="g-btn-primary" style="padding:10px 24px;font-size:10px">LAUNCH APP</a>'
      '<button id="g-sticky-dismiss" onclick="window.dismissSticky()">×</button>'
      '</div></div></div>'

      # Section dots
      '<div id="g-dots">'
      '<button class="g-dot-nav active" data-section="g-hero-anchor" title="Hero"></button>'
      '<button class="g-dot-nav" data-section="how" title="How"></button>'
      '<button class="g-dot-nav" data-section="analyzer" title="Analyzer"></button>'
      '<button class="g-dot-nav" data-section="builder" title="Builder"></button>'
      '<button class="g-dot-nav" data-section="career" title="Career"></button>'
      '<button class="g-dot-nav" data-section="compare" title="Compare"></button>'
      '<button class="g-dot-nav" data-section="contact" title="Contact"></button>'
      '</div>'

      # Nav
      '<nav class="g-nav" id="g-nav">'
      '<div class="g-nav-inner">'
      '<a href="#g-hero-anchor" class="g-logo">'
      '<div class="g-logo-hex">⬡</div>'
      'HIRELYZER'
      '</a>'
      '<div class="g-nav-links">'
      '<a href="#how" data-nav="how">HOW IT WORKS</a>'
      '<a href="#analyzer" data-nav="analyzer">ANALYZER</a>'
      '<a href="#builder" data-nav="builder">BUILDER</a>'
      '<a href="#career" data-nav="career">CAREER HUB</a>'
      '<a href="#compare" data-nav="compare">COMPARE</a>'
      '</div>'
      f'<a href="{APP_URL}" target="_blank" class="g-nav-cta">LAUNCH APP ▶</a>'
      '</div></nav>')

def render_hero():
    H('<div id="g-hero-anchor"></div>'
      '<section class="g-hero">'

      # Orbit rings
      '<div class="g-orbit-ring" style="width:400px;height:400px"></div>'
      '<div class="g-orbit-ring" style="width:600px;height:600px"></div>'
      '<div class="g-orbit-ring" style="width:800px;height:800px"></div>'

      '<div class="g-hero-content">'

      '<div class="g-status-bar">'
      '<div class="g-status-dot"></div>'
      '// SYSTEM STATUS: ONLINE &nbsp;·&nbsp; v2.4.1 &nbsp;·&nbsp; ALL SYSTEMS GO'
      '</div>'

      '<h1 class="g-h1">'
      'YOUR CAREER<br>'
      f'<span class="g-h1-glitch" data-text="DESERVES">DESERVES</span><br>'
      '<span style="color:var(--magenta);text-shadow:0 0 30px var(--magenta)">'
      '<span id="g-typewriter">everyone</span><span class="g-cursor"></span>'
      '</span>'
      '<span class="g-h1-sub">// INTELLIGENT CAREER PLATFORM</span>'
      '</h1>'

      '<p class="g-hero-desc">'
      'Beat ATS systems. Eliminate bias. Land interviews at top companies. '
      'HIRELYZER gives you the unfair advantage — powered by AI that actually works.'
      '</p>'

      '<div class="g-hud-row">'
      '<div class="g-hud-stat">'
      '<div class="g-hud-num" data-count="12000" data-suffix="+">0+</div>'
      '<div class="g-hud-label">USERS DEPLOYED</div>'
      '</div>'
      '<div class="g-hud-stat">'
      '<div class="g-hud-num" data-count="94" data-suffix="%">0%</div>'
      '<div class="g-hud-label">ATS PASS RATE</div>'
      '</div>'
      '<div class="g-hud-stat">'
      '<div class="g-hud-num" data-count="15">0</div>'
      '<div class="g-hud-label">RESUME TEMPLATES</div>'
      '</div>'
      '<div class="g-hud-stat">'
      '<div class="g-hud-num" data-count="3" data-suffix="s">0s</div>'
      '<div class="g-hud-label">ATS SCAN TIME</div>'
      '</div>'
      '</div>'

      '<div class="g-ctas">'
      f'<a href="{APP_URL}" target="_blank" class="g-btn-primary">▶ INITIALIZE FREE</a>'
      '<a href="#how" class="g-btn-secondary">VIEW INTEL ↓</a>'
      '</div>'

      '<div class="g-scroll-hint">'
      '<span>SCROLL DOWN</span>'
      '<div class="g-scroll-line"></div>'
      '</div>'

      '</div>'
      '</section>')

def render_how():
    H('<div id="how"></div>'
      '<div style="background:var(--bg2);border-top:1px solid rgba(0,245,255,0.06);border-bottom:1px solid rgba(0,245,255,0.06)">'
      '<div class="g-section">'
      '<div class="g-section-header">'
      '<div class="g-section-eyebrow">MISSION BRIEFING</div>'
      '<h2 class="g-section-h2">HOW THE <span class="accent">SYSTEM</span> WORKS</h2>'
      '<p class="g-section-sub">Four-phase protocol to career domination. Execute in sequence.</p>'
      '</div>'

      '<div class="g-steps">'
      '<div class="g-step">'
      '<div class="g-step-num">PHASE <span style="color:var(--cyan)">01</span></div>'
      '<div class="g-step-icon">📄</div>'
      '<div class="g-step-title">UPLOAD RESUME</div>'
      '<div class="g-step-desc">Drop your resume. Our scanner ingests every keyword, gap, and formatting issue in under 3 seconds.</div>'
      '</div>'
      '<div class="g-step">'
      '<div class="g-step-num">PHASE <span style="color:var(--cyan)">02</span></div>'
      '<div class="g-step-icon">⚡</div>'
      '<div class="g-step-title">AI ANALYSIS</div>'
      '<div class="g-step-desc">Multi-layer AI cross-references your resume against ATS algorithms and live job requirements.</div>'
      '</div>'
      '<div class="g-step">'
      '<div class="g-step-num">PHASE <span style="color:var(--cyan)">03</span></div>'
      '<div class="g-step-icon">🎯</div>'
      '<div class="g-step-title">OPTIMIZE & BUILD</div>'
      '<div class="g-step-desc">Rewrite. Rebuild. Choose from 15 ATS-optimized templates. Generate cover letters instantly.</div>'
      '</div>'
      '<div class="g-step">'
      '<div class="g-step-num">PHASE <span style="color:var(--cyan)">04</span></div>'
      '<div class="g-step-icon">🚀</div>'
      '<div class="g-step-title">DEPLOY & WIN</div>'
      '<div class="g-step-desc">Live job matching. AI interview coaching. Real-time feedback loops. You\'re ready to launch.</div>'
      '</div>'
      '</div>'

      '</div>'
      '</div>')

def render_story_ats():
    skills  = ["KEYWORDS","FORMAT","SKILLS","LENGTH","IMPACT","CLARITY"]
    scores  = [88, 74, 92, 68, 85, 78]
    radar   = radar_chart(skills, scores)

    H('<div id="analyzer"></div>'
      '<section class="g-story">'
      '<div class="g-story-inner">'

      '<div>'
      '<div class="g-story-label"><div class="g-story-label-dot"></div>ATS ANALYSIS ENGINE</div>'
      '<h2 class="g-story-h">INSTANT <span style="color:var(--cyan)">ATS SCORE</span><br>IN UNDER 3 SECONDS</h2>'
      '<p class="g-story-p">Most resumes get filtered before a human ever sees them. Our engine simulates 50+ enterprise ATS systems — exposing exactly why you\'re being rejected and how to fix it.</p>'
      '<div class="g-pills">'
      + g_pill(["ATS SIMULATION","KEYWORD DENSITY","FORMAT AUDIT","BIAS SCAN","SCORE BOOST"]) +
      '</div>'
      '</div>'

      '<div class="g-panel">'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--cyan);letter-spacing:2px;margin-bottom:16px">// ATS ANALYSIS REPORT</div>'
      + ats_meter("KEYWORD MATCH", 88, "var(--cyan)")
      + ats_meter("FORMAT SCORE", 74, "var(--magenta)")
      + ats_meter("SKILL ALIGNMENT", 92, "var(--green)")
      + ats_meter("IMPACT METRICS", 85, "var(--orange)") +
      '<div style="height:1px;background:var(--border);margin:16px 0"></div>'
      + radar +
      '</div>'

      '</div>'
      '</section>')

def render_story_bias():
    H('<section class="g-story" style="background:rgba(255,0,255,0.01)">'
      '<div class="g-story-inner rev">'

      '<div class="g-panel">'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--magenta);letter-spacing:2px;margin-bottom:16px">// BIAS DETECTION ACTIVE</div>'
      '<div style="margin-bottom:16px">'
      '<div style="display:flex;justify-content:space-between;margin-bottom:8px;font-size:12px;font-family:\'Share Tech Mono\',monospace">'
      '<span style="color:var(--dim)">GENDER BIAS DETECTED</span>'
      '<span style="color:var(--red)">HIGH RISK</span>'
      '</div>'
      '<div style="background:rgba(255,0,51,0.08);border:1px solid rgba(255,0,51,0.2);padding:10px 14px;font-size:12px;color:var(--dim);font-family:\'Share Tech Mono\',monospace">'
      '<span style="color:var(--red)">⚠</span> "aggressive go-getter" → flagged as male-coded'
      '</div>'
      '</div>'
      '<div style="margin-bottom:16px">'
      '<div style="display:flex;justify-content:space-between;margin-bottom:8px;font-size:12px;font-family:\'Share Tech Mono\',monospace">'
      '<span style="color:var(--dim)">AI REWRITE READY</span>'
      '<span style="color:var(--green)">APPLYING FIX</span>'
      '</div>'
      '<div style="background:rgba(0,255,65,0.05);border:1px solid rgba(0,255,65,0.2);padding:10px 14px;font-size:12px;color:var(--dim);font-family:\'Share Tech Mono\',monospace">'
      '<span style="color:var(--green)">✓</span> "results-driven professional" → neutral &amp; inclusive'
      '</div>'
      '</div>'
      '<div style="background:rgba(0,245,255,0.04);border:1px solid var(--border);padding:14px;text-align:center">'
      '<div style="font-family:\'Orbitron\',monospace;font-size:22px;font-weight:900;color:var(--cyan);text-shadow:0 0 20px var(--cyan)">93%</div>'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--dimmer);letter-spacing:2px;margin-top:4px">BIAS ELIMINATION RATE</div>'
      '</div>'
      '</div>'

      '<div>'
      '<div class="g-story-label" style="color:var(--magenta)"><div class="g-story-label-dot" style="background:var(--magenta);box-shadow:0 0 8px var(--magenta)"></div>BIAS NEUTRALIZER</div>'
      '<h2 class="g-story-h">ELIMINATE BIAS.<br><span style="color:var(--magenta)">LEVEL THE</span><br>PLAYING FIELD.</h2>'
      '<p class="g-story-p">Hidden language patterns are silently sabotaging your applications. Our AI scans for gender, age, cultural, and socioeconomic bias — then rewrites for maximum inclusivity.</p>'
      '<div class="g-pills" style="--pill-border:rgba(255,0,255,0.2);--pill-color:rgba(255,0,255,0.7)">'
      + g_pill(["GENDER BIAS","AGE BIAS","CULTURAL BIAS","TONE AUDIT","AI REWRITE"]) +
      '</div>'
      '</div>'

      '</div>'
      '</section>')

def render_story_builder():
    tmpls = [
        ("CYBER","#00f5ff",True), ("ELITE","#ff00ff",False),
        ("EXEC","#ff9f0a",False), ("GHOST","#00ff41",False),
        ("NEO","#7c3aed",False), ("SLATE","#64748b",False),
        ("NOVA","#fb7185",False), ("VOID","#a78bfa",False),
    ]
    tmpl_html = '<div class="g-tmpl-grid">'
    for name, color, active in tmpls:
        tmpl_html += mini_template(name, color, active)
    tmpl_html += '</div>'

    H('<div id="builder"></div>'
      '<section class="g-story" style="background:rgba(255,150,0,0.01)">'
      '<div class="g-story-inner">'

      '<div>'
      '<div class="g-story-label" style="color:var(--orange)"><div class="g-story-label-dot" style="background:var(--orange);box-shadow:0 0 8px var(--orange)"></div>RESUME FORGE</div>'
      '<h2 class="g-story-h"><span style="color:var(--orange)">15 BATTLE-TESTED</span><br>RESUME TEMPLATES</h2>'
      '<p class="g-story-p">Every template engineered for ATS compatibility. Pick your loadout, customize your colors, and generate a cover letter in one click. No design skills required.</p>'
      '<div class="g-pills">'
      + g_pill(["15 TEMPLATES","ATS-OPTIMIZED","COVER LETTER AI","PDF EXPORT","1-CLICK APPLY"]) +
      '</div>'
      '</div>'

      '<div class="g-panel">'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--orange);letter-spacing:2px;margin-bottom:16px">// TEMPLATE LOADOUT</div>'
      + tmpl_html +
      '<div style="height:1px;background:var(--border);margin:12px 0"></div>'
      '<div style="display:flex;gap:10px">'
      '<div class="g-btn-primary" style="flex:1;text-align:center;padding:10px;font-size:9px;cursor:pointer;clip-path:polygon(6px 0%,100% 0%,calc(100% - 6px) 100%,0% 100%)">GENERATE COVER LETTER</div>'
      '<div style="flex:1;text-align:center;padding:10px;border:1px solid var(--border);font-family:\'Orbitron\',monospace;font-size:9px;color:var(--dim);cursor:pointer;clip-path:polygon(6px 0%,100% 0%,calc(100% - 6px) 100%,0% 100%)">EXPORT PDF</div>'
      '</div>'
      '</div>'

      '</div>'
      '</section>')

def render_story_career():
    H('<div id="career"></div>'
      '<section class="g-story" style="background:rgba(0,255,65,0.01)">'
      '<div class="g-story-inner rev">'

      '<div class="g-panel">'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--green);letter-spacing:2px;margin-bottom:16px">// LIVE JOB FEED</div>'
      + g_job_cards() +
      '<div style="height:1px;background:var(--border);margin:12px 0"></div>'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--dimmer);text-align:center;letter-spacing:2px">SHOWING 4 OF 2,400+ LIVE POSITIONS</div>'
      '</div>'

      '<div>'
      '<div class="g-story-label" style="color:var(--green)"><div class="g-story-label-dot" style="background:var(--green);box-shadow:0 0 8px var(--green)"></div>CAREER INTEL HUB</div>'
      '<h2 class="g-story-h"><span style="color:var(--green)">REAL-TIME</span><br>JOB MATCHING<br>ENGINE</h2>'
      '<p class="g-story-p">Stop scrolling job boards. Our engine continuously monitors 50+ platforms and surfaces roles that match your exact profile — with compatibility scores and salary intel.</p>'
      '<div class="g-pills">'
      + g_pill(["LIVE MATCHING","SALARY DATA","SKILL GAPS","APPLY TRACKING","COMPANY INTEL"]) +
      '</div>'
      '</div>'

      '</div>'
      '</section>')

def render_story_interview():
    H('<section class="g-story" style="background:rgba(124,58,237,0.01)">'
      '<div class="g-story-inner">'

      '<div>'
      '<div class="g-story-label" style="color:#a78bfa"><div class="g-story-label-dot" style="background:#a78bfa;box-shadow:0 0 8px #a78bfa"></div>INTERVIEW SIMULATOR</div>'
      '<h2 class="g-story-h"><span style="color:#a78bfa">AI-POWERED</span><br>INTERVIEW<br>TRAINING</h2>'
      '<p class="g-story-p">Face questions generated from your actual resume. Get instant scoring on clarity, confidence, and content. Train until you\'re ready to dominate any interview.</p>'
      '<div class="g-pills">'
      + g_pill(["RESUME-BASED Q&A","INSTANT SCORING","WEAKNESS DETECTION","MOCK INTERVIEWS","FEEDBACK LOOPS"]) +
      '</div>'
      '</div>'

      '<div class="g-panel">'
      '<div style="font-family:\'Share Tech Mono\',monospace;font-size:10px;color:#a78bfa;letter-spacing:2px;margin-bottom:16px">// INTERVIEW SIM — ROUND 01</div>'
      '<div style="margin-bottom:16px">'
      '<div style="font-size:12px;font-weight:600;color:var(--white);margin-bottom:8px;display:flex;gap:8px;align-items:flex-start;font-family:\'Rajdhani\',sans-serif">'
      '<span style="color:#a78bfa;font-family:\'Share Tech Mono\',monospace;font-size:10px">Q:</span>'
      'Describe a time you led a complex technical project end-to-end.'
      '</div>'
      '<div style="font-size:12px;color:var(--dim);line-height:1.7;padding-left:20px;font-family:\'Rajdhani\',sans-serif">'
      'At Anthropic, I architected a distributed pipeline handling 2M+ daily API requests — reducing latency by 40% through async processing and Redis caching...'
      '</div>'
      '</div>'
      '<div style="display:flex;gap:8px;align-items:center;padding:10px 14px;background:rgba(167,139,250,0.06);border:1px solid rgba(167,139,250,0.2)">'
      '<span style="color:var(--green);font-family:\'Share Tech Mono\',monospace;font-size:10px">SCORE:</span>'
      '<span style="font-family:\'Orbitron\',monospace;font-size:18px;font-weight:900;color:var(--green);text-shadow:0 0 15px var(--green)">92/100</span>'
      '<span style="font-size:11px;color:var(--dim);font-family:\'Share Tech Mono\',monospace;margin-left:auto">EXCELLENT RESPONSE</span>'
      '</div>'
      '</div>'

      '</div>'
      '</section>')

def render_testimonials():
    quotes = [
        ("Got a Google offer after 3 weeks of using this. The ATS score feature alone is worth everything.", "R. SHARMA", "SWE @ GOOGLE", "#00f5ff", "R"),
        ("The bias detection rewrote my summary — suddenly getting 5x more callbacks.", "P. CHEN", "PM @ MICROSOFT", "#ff00ff", "P"),
        ("Built my resume in 10 minutes. Had an interview the next day. Landed the role.", "A. PATEL", "ML ENGINEER", "#00ff41", "A"),
        ("Interview coach trained me on my own resume. I went in confident and got an offer.", "S. KIM", "DATA SCIENTIST", "#ff9f0a", "S"),
        ("Moved from 2% to 78% ATS pass rate. This is insane technology.", "M. OKAFOR", "BACKEND DEV", "#7c3aed", "M"),
        ("Cover letter generator saved me 3 hours per application. No more writer's block.", "L. TORRES", "PRODUCT DESIGNER", "#fb7185", "L"),
    ]
    items = ""
    for q, name, role, color, letter in quotes:
        stars = '<div class="g-ticker-stars">★ ★ ★ ★ ★</div>'
        items += (f'<div class="g-ticker-item">'
                  f'{stars}'
                  f'<div class="g-ticker-quote">"{q}"</div>'
                  f'<div class="g-ticker-author">'
                  f'<div class="g-ticker-avatar" style="background:{color}22;color:{color}">{letter}</div>'
                  f'<div><div class="g-ticker-name">{name}</div><div class="g-ticker-role">{role}</div></div>'
                  f'</div></div>')
    full = items * 2
    H(f'<div class="g-ticker-wrap"><div class="g-ticker-track">{full}</div></div>')

def render_compare():
    H('<div id="compare"></div>'
      '<div style="background:var(--bg2);border-top:1px solid rgba(0,245,255,0.06)">'
      '<div class="g-section">'
      '<div class="g-section-header">'
      '<div class="g-section-eyebrow">COMPETITIVE ANALYSIS</div>'
      '<h2 class="g-section-h2">HIRELYZER <span class="accent">VS</span> THE REST</h2>'
      '<p class="g-section-sub">We didn\'t build another resume tool. We built a career weapon.</p>'
      '</div>'

      '<div class="g-compare-wrap">'
      '<div class="g-compare-head">'
      '<div class="g-ch">CAPABILITY</div>'
      '<div class="g-ch g-ch-hl">⬡ HIRELYZER</div>'
      '<div class="g-ch" style="text-align:center">RESUME.IO</div>'
      '<div class="g-ch" style="text-align:center">JOBSCAN</div>'
      '</div>'
      + ''.join([
          f'<div class="g-compare-row">'
          f'<div class="g-cc"><div class="g-cc-feat">{feat}<small>{sub}</small></div></div>'
          f'<div class="g-cc g-cc-hl g-cc-center">{ours}</div>'
          f'<div class="g-cc g-cc-center">{r}</div>'
          f'<div class="g-cc g-cc-center">{j}</div>'
          f'</div>'
          for feat, sub, ours, r, j in [
              ("ATS Score Analysis", "Multi-system simulation", chk_y(), chk_y(), chk_y()),
              ("Bias Detection & Rewrite", "Gender, age, cultural", chk_y(), chk_n(), chk_n()),
              ("15 Resume Templates", "ATS-optimized designs", chk_y(), chk_y(), chk_n()),
              ("AI Cover Letter", "Role-specific generation", chk_y(), chk_p("PAID"), chk_n()),
              ("Live Job Matching", "Real-time 50+ platforms", chk_y(), chk_n(), chk_p("LIMITED")),
              ("AI Interview Coach", "Resume-based questions", chk_y(), chk_n(), chk_n()),
              ("Salary Intelligence", "Market rate data", chk_y(), chk_n(), chk_p("BASIC")),
              ("100% Free Tier", "No credit card required", chk_y(), chk_n(), chk_n()),
          ]
      ]) +
      '</div>'

      '</div>'
      '</div>')

def render_features():
    feats = [
        ("⚡", "ATS SCANNER", "Simulate 50+ enterprise ATS systems in real-time. Know exactly why you're being filtered."),
        ("🔍", "BIAS DETECTOR", "AI-powered language analysis catches invisible bias patterns and rewrites for inclusivity."),
        ("📋", "TEMPLATE FORGE", "15 battle-tested templates. Every design is ATS-safe and recruiter-approved."),
        ("✉️", "COVER LETTER AI", "Generate compelling, role-specific cover letters in one click from your resume data."),
        ("🎯", "JOB MATCHER", "Real-time job matching across 50+ platforms with compatibility scoring and alerts."),
        ("🎤", "INTERVIEW SIM", "Practice with AI-generated questions based on your actual resume. Score and improve."),
    ]
    H('<div style="background:var(--bg)">'
      '<div class="g-section">'
      '<div class="g-section-header">'
      '<div class="g-section-eyebrow">ARSENAL</div>'
      '<h2 class="g-section-h2">YOUR <span class="accent">WEAPONS</span> LOADOUT</h2>'
      '</div>'
      '<div class="g-feat-grid">'
      + "".join(f'<div class="g-feat"><div class="g-feat-icon">{icon}</div><div class="g-feat-title">{title}</div><div class="g-feat-desc">{desc}</div></div>' for icon, title, desc in feats) +
      '</div></div></div>')

def render_faq():
    faqs = [
        ("Is HIRELYZER actually free?", "Yes. Core features — ATS scanning, bias detection, resume builder, and job matching — are all free. No credit card. No tricks."),
        ("How accurate is the ATS simulation?", "Our engine simulates 50+ enterprise ATS systems with 90%+ accuracy based on real applicant tracking data and recruiter feedback loops."),
        ("How does the bias detection work?", "We use a fine-tuned NLP model trained on 10,000+ professional documents to identify language patterns correlated with demographic signals — then suggest neutral alternatives."),
        ("Can the AI really write my cover letter?", "Yes. Our model reads your resume, the job description, and generates a tailored cover letter that matches the company's tone. Edit before sending."),
        ("What makes the Interview Coach different?", "Unlike generic question banks, our coach generates questions directly from your resume. So you practice the exact conversations recruiters will have about your actual experience."),
        ("Is my data secure?", "We use end-to-end encryption. Your resume data is never sold or used to train external models. You control your data."),
    ]
    H('<div id="g-faq" style="background:var(--bg2);border-top:1px solid rgba(0,245,255,0.06)">'
      '<div class="g-section">'
      '<div class="g-section-header">'
      '<div class="g-section-eyebrow">INTEL DATABASE</div>'
      '<h2 class="g-section-h2">FREQUENTLY ASKED <span class="accent">QUESTIONS</span></h2>'
      '</div>'
      '<div class="g-faq-list">'
      + "".join(f'<div class="g-faq-item"><div class="g-faq-q" onclick="this.parentElement.classList.toggle(\'open\')">{q}<div class="g-faq-q-icon">+</div></div><div class="g-faq-a" style="display:none">{a}</div></div>' for q,a in faqs) +
      '</div></div></div>')

def render_cta():
    H(f'<div style="background:var(--bg)">'
      f'<div style="max-width:1200px;margin:0 auto;padding:80px 32px 0">'
      f'<div class="g-cta-section">'
      f'<div class="g-cta-corner-tl"></div>'
      f'<div class="g-cta-corner-br"></div>'
      f'<h2 class="g-cta-h">READY TO <span style="color:var(--cyan)">DOMINATE</span><br>YOUR JOB SEARCH?</h2>'
      f'<p class="g-cta-sub">Join 12,000+ professionals who gave themselves the unfair advantage. Free forever. No excuses.</p>'
      f'<div class="g-cta-btns">'
      f'<a href="{APP_URL}" target="_blank" class="g-btn-primary" style="font-size:13px;padding:18px 48px">⬡ INITIALIZE FREE — NO CREDIT CARD</a>'
      f'</div>'
      f'<div style="display:flex;justify-content:center;gap:32px;flex-wrap:wrap;margin-top:36px">'
      f'<span style="font-family:\'Share Tech Mono\',monospace;font-size:11px;color:var(--dimmer);display:flex;align-items:center;gap:6px"><span style="color:var(--green)">✓</span> FREE FOREVER TIER</span>'
      f'<span style="font-family:\'Share Tech Mono\',monospace;font-size:11px;color:var(--dimmer);display:flex;align-items:center;gap:6px"><span style="color:var(--green)">✓</span> NO CREDIT CARD</span>'
      f'<span style="font-family:\'Share Tech Mono\',monospace;font-size:11px;color:var(--dimmer);display:flex;align-items:center;gap:6px"><span style="color:var(--green)">✓</span> 2 MIN SETUP</span>'
      f'<span style="font-family:\'Share Tech Mono\',monospace;font-size:11px;color:var(--dimmer);display:flex;align-items:center;gap:6px"><span style="color:var(--green)">✓</span> FULL ATS SCAN</span>'
      f'</div>'
      f'</div></div></div>')

def render_contact():
    H(f'<div id="contact" style="background:var(--bg)">'
      f'<div class="g-section">'
      f'<div class="g-section-header">'
      f'<div class="g-section-eyebrow">COMMS CHANNEL</div>'
      f'<h2 class="g-section-h2">ESTABLISH <span class="accent">CONTACT</span></h2>'
      f'</div>'
      f'<div class="g-contact-card">'
      f'<h3>SUPPORT COMMAND</h3>'
      f'<p>Questions? Bugs? Feature requests? Open a direct line to the team.</p>'
      f'<a href="mailto:{SUPPORT_EMAIL}" class="g-contact-email">📡 {SUPPORT_EMAIL}</a>'
      f'<div style="margin-top:20px;font-family:\'Share Tech Mono\',monospace;font-size:10px;color:var(--dimmer);letter-spacing:1px">RESPONSE TIME: &lt; 24 HOURS // MON–FRI</div>'
      f'</div></div></div>')

def render_footer():
    H('<footer style="background:var(--bg);border-top:1px solid rgba(0,245,255,0.06)">'
      '<div class="g-footer">'
      '<div>'
      '<div style="font-family:\'Orbitron\',monospace;font-size:13px;font-weight:900;color:var(--cyan);letter-spacing:3px;text-shadow:0 0 15px var(--cyan);margin-bottom:6px">⬡ HIRELYZER</div>'
      '<div class="g-footer-copy">© 2025 HIRELYZER. ALL SYSTEMS OPERATIONAL.</div>'
      '</div>'
      '<div class="g-footer-links">'
      f'<a href="{APP_URL}" target="_blank">LAUNCH APP</a>'
      f'<a href="mailto:{SUPPORT_EMAIL}">SUPPORT</a>'
      '<a href="#">PRIVACY</a>'
      '</div>'
      '</div>'
      '</footer>')

def render_js():
    H('<script>'
      '(function(){'

      # Matrix rain
      'var canvas=document.getElementById("matrix-canvas");'
      'var ctx=canvas.getContext("2d");'
      'var cols,drops;'
      'function initMatrix(){'
      'canvas.width=window.innerWidth;canvas.height=window.innerHeight;'
      'cols=Math.floor(canvas.width/16);'
      'drops=new Array(cols).fill(0).map(function(){return Math.random()*-50;});'
      '}'
      'initMatrix();'
      'var chars="01アイウエオカキクケコサシスセソタチツテトHIRELYZER".split("");'
      'function drawMatrix(){'
      'ctx.fillStyle="rgba(0,0,8,0.05)";ctx.fillRect(0,0,canvas.width,canvas.height);'
      'ctx.fillStyle="#00f5ff";ctx.font="12px Share Tech Mono,monospace";'
      'drops.forEach(function(y,i){'
      'var c=chars[Math.floor(Math.random()*chars.length)];'
      'ctx.fillStyle=Math.random()>0.98?"#ffffff":"#00f5ff";'
      'ctx.fillText(c,i*16,y*16);'
      'if(y*16>canvas.height&&Math.random()>0.975)drops[i]=0;'
      'drops[i]+=0.5;'
      '});'
      '}'
      'setInterval(drawMatrix,50);'
      'window.addEventListener("resize",initMatrix,{passive:true});'

      # Scroll progress
      'var sp=document.getElementById("sp");'
      'function updateScroll(){'
      'var pct=window.scrollY/(document.documentElement.scrollHeight-window.innerHeight)*100;'
      'if(sp)sp.style.width=pct+"%";'
      '}'
      'window.addEventListener("scroll",updateScroll,{passive:true});'

      # Sticky CTA
      'var sticky=document.getElementById("g-sticky");'
      'var stickyDismissed=false;'
      'function checkSticky(){'
      'if(stickyDismissed||!sticky)return;'
      'var pct=window.scrollY/(document.documentElement.scrollHeight-window.innerHeight);'
      'sticky.classList.toggle("visible",pct>0.3);'
      '}'
      'window.addEventListener("scroll",checkSticky,{passive:true});'
      'window.dismissSticky=function(){stickyDismissed=true;if(sticky)sticky.classList.remove("visible");};'

      # Toast
      'var toastTimer;'
      'window.showToast=function(msg,color){'
      'var t=document.getElementById("g-toast");var m=document.getElementById("g-toast-msg");var d=document.getElementById("g-toast-dot");'
      'if(!t||!m)return;m.textContent=msg;if(d&&color){d.style.background=color;d.style.boxShadow="0 0 8px "+color;}'
      't.classList.add("show");clearTimeout(toastTimer);toastTimer=setTimeout(function(){t.classList.remove("show");},3000);'
      '};'

      # Stat counters
      'function animCount(el,target,suffix){'
      'var dur=2000,startT=null;'
      'function step(ts){if(!startT)startT=ts;var p=Math.min((ts-startT)/dur,1);var e=1-Math.pow(1-p,3);'
      'el.textContent=Math.round(e*target)+(suffix||"");if(p<1)requestAnimationFrame(step);}'
      'requestAnimationFrame(step);}'
      'var statObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){if(e.isIntersecting){'
      'var el=e.target;var c=parseInt(el.getAttribute("data-count"));var s=el.getAttribute("data-suffix")||"";'
      'if(c){animCount(el,c,s);}statObs.unobserve(el);}});},{threshold:0.5});'
      'document.querySelectorAll("[data-count]").forEach(function(el){statObs.observe(el);});'

      # Radar
      'var radarObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var poly=document.getElementById("g-radar-poly");if(poly)poly.classList.add("drawn");'
      'document.querySelectorAll(".g-radar-dot").forEach(function(d){d.classList.add("drawn");});'
      'radarObs.unobserve(e.target);}});},{threshold:0.3});'
      'var rv=document.getElementById("g-radar-svg");if(rv)radarObs.observe(rv);'

      # Nav dots
      'var sectionIds=["g-hero-anchor","how","analyzer","builder","career","compare","contact"];'
      'var dotObs=new IntersectionObserver(function(entries){'
      'entries.forEach(function(e){'
      'if(e.isIntersecting){'
      'var id=e.target.id;'
      'document.querySelectorAll(".g-dot-nav").forEach(function(d){d.classList.toggle("active",d.getAttribute("data-section")===id);});'
      '}});},{threshold:0.4});'
      'sectionIds.forEach(function(id){var el=document.getElementById(id);if(el)dotObs.observe(el);});'
      'document.querySelectorAll(".g-dot-nav").forEach(function(btn){'
      'btn.addEventListener("click",function(){'
      'var el=document.getElementById(this.getAttribute("data-section"));'
      'if(el)el.scrollIntoView({behavior:"smooth",block:"start"});'
      '});});'

      # Typewriter
      'var words=["everyone","engineers","designers","devs","job seekers","you"];'
      'var tw=document.getElementById("g-typewriter");'
      'var twIdx=0,twDel=false,twCur="everyone",twTimer;'
      'function typeStep(){'
      'if(!tw)return;var target=words[twIdx];'
      'if(!twDel){twCur=target.slice(0,twCur.length+1);tw.textContent=twCur;'
      'if(twCur===target){twDel=true;twTimer=setTimeout(typeStep,2000);return;}'
      'twTimer=setTimeout(typeStep,90);}'
      'else{twCur=twCur.slice(0,-1);tw.textContent=twCur;'
      'if(twCur.length===0){twDel=false;twIdx=(twIdx+1)%words.length;twTimer=setTimeout(typeStep,300);return;}'
      'twTimer=setTimeout(typeStep,55);}'
      '}'
      'setTimeout(function(){twDel=true;typeStep();},2500);'

      # FAQ
      'document.querySelectorAll(".g-faq-q").forEach(function(q){'
      'q.addEventListener("click",function(){'
      'var item=this.parentElement;'
      'var ans=item.querySelector(".g-faq-a");'
      'var icon=this.querySelector(".g-faq-q-icon");'
      'var isOpen=item.classList.contains("open");'
      'document.querySelectorAll(".g-faq-item").forEach(function(i){'
      'i.classList.remove("open");'
      'var a=i.querySelector(".g-faq-a");var ic=i.querySelector(".g-faq-q-icon");'
      'if(a)a.style.display="none";if(ic)ic.textContent="+";'
      '});'
      'if(!isOpen){'
      'item.classList.add("open");'
      'if(ans)ans.style.display="block";if(icon)icon.textContent="×";'
      '}'
      '});});'

      '})();'
      '</script>')

# ─── MAIN ─────────────────────────────────────────────────────────────────────
render_banner()
render_nav()
render_hero()
render_how()
render_story_ats()
render_story_bias()
render_story_builder()
render_story_career()
render_story_interview()
render_testimonials()
render_compare()
render_features()
render_faq()
render_cta()
render_contact()
render_footer()
render_js()
