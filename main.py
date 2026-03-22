import math
import streamlit as st

st.set_page_config(
    page_title="HIRELYZER — Intelligent Career Platform",
    page_icon="⬡",
    layout="wide",
)

APP_URL = "https://hirelyzer-career-based-saas-platform-rxzkspoyrtwfamm5ztkmcf.streamlit.app/"

# ─── helpers ──────────────────────────────────────────────────────────────────
def H(s):
    st.markdown(s, unsafe_allow_html=True)

def CSS(s):
    st.markdown("<style>" + s + "</style>", unsafe_allow_html=True)

# ─── CSS ──────────────────────────────────────────────────────────────────────
CSS("""
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
  background-color: #000000 !important;
  color: #f5f5f7 !important;
  font-family: 'Sora', sans-serif !important;
  overflow-x: hidden !important;
  -webkit-font-smoothing: antialiased !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stSidebar"],
[data-testid="stStatusWidget"],
footer,
#MainMenu { display: none !important; }

section[data-testid="stAppViewContainer"] > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stMarkdownContainer"] > p { margin: 0 !important; }

#sp {
  position: fixed; top: 0; left: 0; right: 0; height: 2px; width: 0%;
  background: linear-gradient(90deg, #0a84ff, #30d158);
  z-index: 9999; transition: width 0.05s linear; pointer-events: none;
}

.hl-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 900;
  height: 58px; display: flex; align-items: center; justify-content: center;
  background: rgba(0,0,0,0.82);
  border-bottom: 1px solid rgba(255,255,255,0.07);
  backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
}
.hl-nav-inner {
  width: 100%; max-width: 1100px;
  display: flex; align-items: center; justify-content: space-between; padding: 0 32px;
}
.hl-logo {
  display: flex; align-items: center; gap: 10px;
  font-size: 14px; font-weight: 800; color: #f5f5f7; text-decoration: none; letter-spacing: 0.5px;
}
.hl-logo-icon {
  width: 32px; height: 32px; border-radius: 9px; background: #0a84ff;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.hl-nav-links { display: flex; align-items: center; gap: 28px; }
.hl-nav-links a { font-size: 13px; font-weight: 500; color: rgba(245,245,247,0.54); text-decoration: none; }
.hl-nav-cta {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 8px 20px; border-radius: 100px; background: #0a84ff;
  color: #fff; font-size: 13px; font-weight: 600; text-decoration: none;
}

.hl-hero {
  min-height: 100vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 130px 32px 80px;
  position: relative; overflow: hidden; background: #000;
}
.hl-hero-glow {
  position: absolute; top: -200px; left: 50%; transform: translateX(-50%);
  width: 900px; height: 700px;
  background: radial-gradient(ellipse at center, rgba(10,132,255,0.11) 0%, transparent 68%);
  pointer-events: none; z-index: 0;
}
.hl-hero-fade {
  position: absolute; bottom: 0; left: 0; right: 0; height: 200px;
  background: linear-gradient(to bottom, transparent, #000);
  pointer-events: none; z-index: 0;
}
.hl-hero-content {
  position: relative; z-index: 1; width: 100%; display: flex; flex-direction: column; align-items: center;
}

.hl-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 10.5px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;
  color: #0a84ff; padding: 6px 16px; border-radius: 100px;
  border: 1px solid rgba(10,132,255,0.28); background: rgba(10,132,255,0.07); margin-bottom: 28px;
  animation: fadeUp 0.6s ease both;
}

.hl-h1 {
  font-size: clamp(42px, 7vw, 84px); font-weight: 800; line-height: 1.03;
  letter-spacing: -3px; color: #f5f5f7; max-width: 920px;
  animation: fadeUp 0.6s 0.1s ease both;
}
.hl-h1-blue { color: #0a84ff; font-style: normal; }

.hl-hero-sub {
  font-size: clamp(15px, 1.9vw, 19px); color: rgba(245,245,247,0.54); line-height: 1.65;
  max-width: 560px; margin: 24px auto 0; animation: fadeUp 0.6s 0.2s ease both;
}

.hl-ctas {
  display: flex; gap: 14px; justify-content: center; margin-top: 44px; flex-wrap: wrap;
  animation: fadeUp 0.6s 0.3s ease both;
}
.hl-btn-p {
  display: inline-flex; align-items: center; gap: 8px; padding: 14px 30px;
  border-radius: 100px; background: #0a84ff; color: #fff;
  font-size: 15px; font-weight: 600; text-decoration: none; letter-spacing: -0.2px;
}
.hl-btn-g {
  display: inline-flex; align-items: center; gap: 8px; padding: 14px 30px;
  border-radius: 100px; background: #1a1a1e; color: #f5f5f7;
  font-size: 15px; font-weight: 600; text-decoration: none; letter-spacing: -0.2px;
  border: 1px solid rgba(255,255,255,0.13);
}

.hl-card {
  margin-top: 72px; width: 100%; max-width: 840px; background: #0f0f10;
  border-radius: 22px; border: 1px solid rgba(255,255,255,0.07); overflow: hidden;
  box-shadow: 0 40px 100px rgba(0,0,0,0.7); animation: fadeUp 0.6s 0.44s ease both;
}
.hl-card-bar {
  height: 40px; background: #141416; border-bottom: 1px solid rgba(255,255,255,0.07);
  display: flex; align-items: center; padding: 0 16px; gap: 8px;
}
.hl-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
.hl-card-tab { margin-left: 6px; font-size: 11px; color: rgba(245,245,247,0.34); font-family: 'JetBrains Mono', monospace; }
.hl-card-body { padding: 24px; }
.hl-card-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }

.hl-ptitle {
  font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.1px;
  color: rgba(245,245,247,0.34); display: flex; align-items: center; gap: 7px; margin-bottom: 18px;
}

.hl-bar { margin-bottom: 10px; }
.hl-bar-row {
  display: flex; justify-content: space-between; font-size: 11px;
  color: rgba(245,245,247,0.54); margin-bottom: 4px; font-weight: 500;
}
.hl-bar-track { height: 4px; background: rgba(255,255,255,0.06); border-radius: 2px; overflow: hidden; }
.hl-bar-fill  { height: 100%; border-radius: 2px; }

.hl-words { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.wc { padding: 4px 11px; border-radius: 7px; font-size: 11px; font-weight: 600; font-family: 'JetBrains Mono', monospace; }
.wc-m { background: rgba(10,132,255,0.11);  color: #4db3ff; border: 1px solid rgba(10,132,255,0.2); }
.wc-f { background: rgba(191,90,242,0.11);  color: #d07ef7; border: 1px solid rgba(191,90,242,0.2); }
.wc-n { background: rgba(48,209,88,0.11);   color: #4cd964; border: 1px solid rgba(48,209,88,0.2); }

.hl-stats {
  display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; margin: 28px 0 0;
  animation: fadeUp 0.6s 0.55s ease both;
}
.hl-stat {
  display: flex; flex-direction: column; align-items: center; padding: 18px 28px;
  border-radius: 18px; background: #0f0f10; border: 1px solid rgba(255,255,255,0.07); min-width: 128px;
}
.hl-stat-n { font-size: 26px; font-weight: 800; color: #f5f5f7; letter-spacing: -1px; }
.hl-stat-l { font-size: 10px; color: rgba(245,245,247,0.34); font-weight: 600; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.9px; }

.hl-section { max-width: 1100px; margin: 0 auto; padding: 0 32px; }

.hl-divider {
  font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;
  color: rgba(245,245,247,0.34); display: flex; align-items: center; gap: 18px; margin-bottom: 64px;
}
.hl-divider::before,
.hl-divider::after { content: ''; flex: 1; height: 1px; background: rgba(255,255,255,0.07); }

.hl-steps { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; }
.hl-step {
  padding: 32px 24px; background: #0f0f10;
  border: 1px solid rgba(255,255,255,0.07); position: relative; overflow: hidden;
}
.hl-step:first-child { border-radius: 20px 0 0 20px; }
.hl-step:last-child  { border-radius: 0 20px 20px 0; }
.hl-step-n { font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 600; color: rgba(245,245,247,0.34); margin-bottom: 16px; display: block; }
.hl-step-icon { width: 44px; height: 44px; margin-bottom: 16px; }
.hl-step-title { font-size: 14px; font-weight: 700; color: #f5f5f7; margin-bottom: 8px; letter-spacing: -0.3px; }
.hl-step-desc  { font-size: 13px; color: rgba(245,245,247,0.54); line-height: 1.65; }

.hl-story     { padding: 100px 0; background: #000; }
.hl-story-alt { padding: 100px 0; background: #080808; }
.hl-story-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }

.hl-story-num { font-family: 'JetBrains Mono', monospace; font-size: 10.5px; font-weight: 600; color: rgba(245,245,247,0.34); letter-spacing: 1px; margin-bottom: 18px; }
.hl-story-h { font-size: clamp(28px, 3.8vw, 44px); font-weight: 800; letter-spacing: -1.8px; line-height: 1.08; color: #f5f5f7; margin-bottom: 20px; }
.hl-story-h .hl-blue  { color: #0a84ff; }
.hl-story-h .hl-green { color: #30d158; }
.hl-story-h .hl-amber { color: #ff9f0a; }
.hl-story-h .hl-purp  { color: #bf5af2; }
.hl-story-p { font-size: 15px; color: rgba(245,245,247,0.54); line-height: 1.78; margin-bottom: 16px; }

.hl-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
.hl-pill { padding: 6px 14px; border-radius: 100px; font-size: 11.5px; font-weight: 600; border: 1px solid rgba(255,255,255,0.13); color: rgba(245,245,247,0.54); background: #0f0f10; }

.hl-panel { background: #0f0f10; border-radius: 20px; border: 1px solid rgba(255,255,255,0.07); padding: 24px; overflow: hidden; position: relative; }

.hl-tmpl-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 14px; }
.hl-tmpl { border-radius: 8px; border: 1px solid rgba(255,255,255,0.07); background: #141416; overflow: hidden; display: flex; flex-direction: column; min-height: 110px; position: relative; cursor: pointer; }
.hl-tmpl:hover { border-color: rgba(255,255,255,0.2) !important; }
.hl-tmpl-act { border-color: #0a84ff !important; box-shadow: 0 0 0 2px rgba(10,132,255,0.2); }
.hl-tmpl-hdr { height: 5px; border-radius: 2px; }
.hl-tmpl-ln  { height: 3px; border-radius: 1.5px; background: rgba(255,255,255,0.13); }
.hl-tmpl-badge { position: absolute; bottom: 6px; left: 6px; right: 6px; background: rgba(10,132,255,0.15); border: 1px solid rgba(10,132,255,0.25); border-radius: 5px; padding: 3px 6px; font-size: 9px; font-weight: 700; color: #0a84ff; text-align: center; letter-spacing: 0.5px; text-transform: uppercase; }

.hl-job { padding: 13px 15px; border-radius: 12px; background: #141416; border: 1px solid rgba(255,255,255,0.07); display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
.hl-job-logo { width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13px; flex-shrink: 0; font-family: 'JetBrains Mono', monospace; }
.hl-job-title { font-size: 13px; font-weight: 600; color: #f5f5f7; }
.hl-job-co    { font-size: 11px; color: rgba(245,245,247,0.34); margin-top: 2px; }
.hl-job-badge { padding: 3px 10px; border-radius: 100px; font-size: 11px; font-weight: 600; white-space: nowrap; flex-shrink: 0; }

.hl-radar-wrap { display: flex; flex-direction: column; align-items: center; }

.hl-qa { margin-bottom: 14px; }
.hl-q { font-size: 13px; font-weight: 600; color: #f5f5f7; margin-bottom: 7px; display: flex; gap: 8px; align-items: flex-start; }
.hl-a { font-size: 12px; color: rgba(245,245,247,0.54); line-height: 1.65; padding-left: 22px; }
.hl-score-badge { display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; border-radius: 100px; font-size: 12px; font-weight: 700; background: rgba(48,209,88,0.12); color: #30d158; border: 1px solid rgba(48,209,88,0.22); }

.hl-cta { margin: 0 0 120px; padding: 80px 48px; border-radius: 28px; background: #0f0f10; border: 1px solid rgba(255,255,255,0.07); text-align: center; position: relative; overflow: hidden; }
.hl-cta-glow { position: absolute; top: -300px; left: 50%; transform: translateX(-50%); width: 600px; height: 600px; background: radial-gradient(ellipse at center, rgba(10,132,255,0.09) 0%, transparent 68%); pointer-events: none; }
.hl-cta-h { font-size: clamp(28px, 4.5vw, 52px); font-weight: 800; letter-spacing: -2px; color: #f5f5f7; line-height: 1.06; max-width: 640px; margin: 0 auto 20px; position: relative; z-index: 1; }
.hl-cta-sub { font-size: 16px; color: rgba(245,245,247,0.54); margin-bottom: 38px; position: relative; z-index: 1; }
.hl-cta-btns { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; position: relative; z-index: 1; }

.hl-checks { display: flex; justify-content: center; gap: 26px; flex-wrap: wrap; margin-top: 36px; }
.hl-check  { display: flex; align-items: center; gap: 7px; font-size: 13px; color: rgba(245,245,247,0.34); }

.hl-footer { border-top: 1px solid rgba(255,255,255,0.07); padding: 40px 32px; display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; flex-wrap: wrap; gap: 18px; }
.hl-footer-copy { font-size: 13px; font-weight: 600; color: rgba(245,245,247,0.34); }
.hl-footer-links { display: flex; gap: 24px; }
.hl-footer-links a { font-size: 13px; color: rgba(245,245,247,0.34); text-decoration: none; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: none; }
}

@media (max-width: 860px) {
  .hl-story-grid { grid-template-columns: 1fr; gap: 40px; }
  .hl-steps { grid-template-columns: 1fr 1fr; }
  .hl-step:first-child  { border-radius: 20px 0 0 0; }
  .hl-step:nth-child(2) { border-radius: 0 20px 0 0; }
  .hl-step:nth-child(3) { border-radius: 0 0 0 20px; }
  .hl-step:last-child   { border-radius: 0 0 20px 0; }
  .hl-ctas { flex-direction: column; align-items: center; }
  .hl-nav-links { display: none; }
  .hl-cta { padding: 48px 24px; }
  .hl-card-grid { grid-template-columns: 1fr; }
}
""")

# ─── SVG helpers ──────────────────────────────────────────────────────────────
def ats_ring(score=78):
    r, c, sw = 38, 48, 5
    circ = 2 * math.pi * r
    fill = (score / 100) * circ
    off  = circ * 0.25
    return (
        '<svg width="96" height="96" viewBox="0 0 96 96" fill="none">'
        '<circle cx="' + str(c) + '" cy="' + str(c) + '" r="' + str(r) + '" stroke="rgba(255,255,255,0.06)" stroke-width="' + str(sw) + '"/>'
        '<circle cx="' + str(c) + '" cy="' + str(c) + '" r="' + str(r) + '" stroke="url(#ag)" stroke-width="' + str(sw) + '"'
        ' stroke-dasharray="' + str(round(fill,1)) + ' ' + str(round(circ,1)) + '"'
        ' stroke-dashoffset="-' + str(round(off,1)) + '" stroke-linecap="round"/>'
        '<text x="' + str(c) + '" y="' + str(c+1) + '" text-anchor="middle" dominant-baseline="middle"'
        ' fill="#f5f5f7" font-size="18" font-weight="800" font-family="Sora,sans-serif">' + str(score) + '</text>'
        '<defs><linearGradient id="ag" x1="0" y1="0" x2="96" y2="96" gradientUnits="userSpaceOnUse">'
        '<stop offset="0%" stop-color="#30d158"/><stop offset="100%" stop-color="#0a84ff"/>'
        '</linearGradient></defs></svg>'
    )

def radar_svg():
    cats   = ["Communication","Technical","Confidence","Structure","Examples"]
    scores = [0.82, 0.74, 0.88, 0.70, 0.78]
    cx = cy = 95; R = 65; n = len(cats)
    def pt(i, frac):
        angle = math.pi/2 + 2*math.pi*i/n
        return cx + R*frac*math.cos(angle), cy - R*frac*math.sin(angle)
    grid = ""
    for lv in [0.25, 0.5, 0.75, 1.0]:
        pts = " ".join(str(round(pt(i,lv)[0],1))+","+str(round(pt(i,lv)[1],1)) for i in range(n))
        grid += '<polygon points="'+pts+'" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>'
    axes = "".join('<line x1="'+str(cx)+'" y1="'+str(cy)+'" x2="'+str(round(pt(i,1)[0],1))+'" y2="'+str(round(pt(i,1)[1],1))+'" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>' for i in range(n))
    poly = " ".join(str(round(pt(i,scores[i])[0],1))+","+str(round(pt(i,scores[i])[1],1)) for i in range(n))
    dots = "".join('<circle cx="'+str(round(pt(i,scores[i])[0],1))+'" cy="'+str(round(pt(i,scores[i])[1],1))+'" r="3.5" fill="#0a84ff"/>' for i in range(n))
    labels = "".join('<text x="'+str(round(pt(i,1.27)[0],1))+'" y="'+str(round(pt(i,1.27)[1],1))+'" text-anchor="middle" dominant-baseline="middle" fill="rgba(245,245,247,0.4)" font-size="8.5" font-family="Sora,sans-serif" font-weight="500">'+cats[i]+'</text>' for i in range(n))
    return ('<svg width="190" height="190" viewBox="0 0 190 190" fill="none">'+grid+axes+'<polygon points="'+poly+'" fill="rgba(10,132,255,0.14)" stroke="#0a84ff" stroke-width="1.5"/>'+dots+labels+'</svg>')

# ─── fragment builders ────────────────────────────────────────────────────────
def ats_bars():
    data = [("Format & Layout",92,"#30d158"),("Keyword Coverage",71,"#ff9f0a"),("Sections Present",85,"#0a84ff"),("Action Verbs",68,"#ff9f0a"),("Contact Info",100,"#30d158"),("Date Consistency",80,"#0a84ff")]
    return "".join('<div class="hl-bar"><div class="hl-bar-row"><span>'+lbl+'</span><span style="color:'+col+';font-weight:600">'+str(pct)+'%</span></div><div class="hl-bar-track"><div class="hl-bar-fill" style="width:'+str(pct)+'%;background:'+col+'"></div></div></div>' for lbl,pct,col in data)

def score_bars():
    data = [("Communication","85%","#0a84ff"),("Technical","79%","#bf5af2"),("Confidence","88%","#30d158"),("Structure","74%","#ff9f0a")]
    return "".join('<div style="display:flex;justify-content:space-between;font-size:11px;color:rgba(245,245,247,0.54);margin-bottom:5px"><span>'+dim+'</span><span style="color:'+col+';font-weight:600">'+sc+'</span></div><div style="height:3px;background:rgba(255,255,255,0.07);border-radius:2px;margin-bottom:8px;overflow:hidden"><div style="width:'+sc+';height:100%;background:'+col+';border-radius:2px"></div></div>' for dim,sc,col in data)

def tmpl_gallery():
    """
    Renders the full interactive template gallery with:
    - 15 faithful mini-resume thumbnails (all templates shown, 8 visible + scroll)
    - Hover tooltip with larger preview + template details
    - Click-to-select with animated info bar update
    - Filter tabs: All / Single-col / Two-col
    - ATS badge overlay on thumbnails
    - Animated selection ring
    """

    # ── per-template data ────────────────────────────────────────────────────
    # fields: id, name, accent, layout, sidebar_bg, header_bg, ats_level, tags, font_hint
    TEMPLATES = [
        ("modern",      "Modern Minimal",       "#0a84ff", "single",  None,      None,      "★★★", ["Single-col","Blue","Minimal"], "Sora"),
        ("classic",     "Classic Clean",        "#e5e5e5", "single",  None,      None,      "★★★", ["Single-col","B&W","ATS Top"], "Georgia"),
        ("executive",   "Executive",            "#ff9f0a", "single",  None,      "#ff9f0a", "★★★", ["Single-col","Amber","Prestige"], "Playfair"),
        ("timeline",    "Timeline",             "#30d158", "timeline",None,      None,      "★★☆", ["Single-col","Green","Visual"], "Sora"),
        ("slate",       "Slate Gray",           "#6b7280", "single",  None,      None,      "★★★", ["Single-col","Gray","Minimal"], "DM Sans"),
        ("burgundy",    "Burgundy Classic",     "#9b2335", "single",  None,      "#9b2335", "★★★", ["Single-col","Red","Classic"], "Merriweather"),
        ("forest",      "Forest Green",         "#2d6a4f", "single",  None,      None,      "★★★", ["Single-col","Green","Elegant"], "Lato"),
        ("corporate",   "Corporate Blue",       "#3b82f6", "sidebar", "#1a2744", None,      "★★☆", ["Two-col","Blue","Corporate"], "Segoe UI"),
        ("creative",    "Creative Green",       "#22c55e", "sidebar", "#0f2018", None,      "★★☆", ["Two-col","Green","Creative"], "Nunito"),
        ("terracotta",  "Warm Terracotta",      "#c2714f", "sidebar", "#2a1a14", None,      "★★☆", ["Two-col","Warm","Premium"], "Cormorant"),
        ("navy",        "Navy Prestige",        "#e2b96a", "sidebar", "#0d1833", None,      "★★☆", ["Two-col","Gold","Prestige"], "Libre Baskerville"),
        ("teal",        "Teal Impact",          "#0d9488", "sidebar", "#0d2420", None,      "★★☆", ["Two-col","Teal","Modern"], "Work Sans"),
        ("indigo",      "Indigo Tech",          "#818cf8", "sidebar", "#1e1b4b", None,      "★★☆", ["Two-col","Indigo","Tech"], "Inter"),
        ("default",     "Default Professional", "#9ca3af", "sidebar", "#374151", None,      "★★☆", ["Two-col","Gray","Professional"], "Segoe UI"),
        ("sidebar_el",  "Elegant Sidebar",      "#38bdf8", "sidebar", "#0f172a", None,      "★★☆", ["Two-col","Sky","Elegant"], "Raleway"),
    ]

    # ── micro HTML builders ──────────────────────────────────────────────────
    def ln(w, col="rgba(255,255,255,0.14)", h="2px", mt="3px"):
        return f'<div style="height:{h};width:{w};background:{col};border-radius:1px;margin-top:{mt}"></div>'

    def sl(col, w="38%"):  # section label
        return f'<div style="height:1.5px;width:{w};background:{col};opacity:.8;border-radius:1px;margin-top:5px;margin-bottom:2px"></div>'

    def avatar(col):
        return f'<div style="width:14px;height:14px;border-radius:50%;background:{col};opacity:.75;margin:0 auto 3px;flex-shrink:0"></div>'

    def pill_row(col):
        return (f'<div style="display:flex;gap:2px;margin-top:3px">'
                f'<div style="height:4px;width:22%;background:{col};opacity:.5;border-radius:3px"></div>'
                f'<div style="height:4px;width:18%;background:{col};opacity:.35;border-radius:3px"></div>'
                f'<div style="height:4px;width:24%;background:{col};opacity:.4;border-radius:3px"></div>'
                f'</div>')

    def skill_dots(col):
        filled = f'<div style="width:4px;height:4px;border-radius:50%;background:{col};opacity:.8"></div>'
        empty  = f'<div style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.15)"></div>'
        return (f'<div style="display:flex;gap:2px;margin-top:3px">' + filled*4 + empty + f'</div>')

    def exp_entry(col, w1="80%", w2="65%"):
        return (f'<div style="display:flex;align-items:flex-start;gap:2px;margin-top:3px">'
                f'<div style="width:2px;height:12px;background:{col};opacity:.6;flex-shrink:0;border-radius:1px;margin-top:1px"></div>'
                f'<div style="flex:1">{ln(w1)}{ln(w2)}</div></div>')

    def timeline_entry(col):
        return (f'<div style="display:flex;align-items:flex-start;gap:2px;margin-top:3px">'
                f'<div style="display:flex;flex-direction:column;align-items:center;gap:0;flex-shrink:0">'
                f'<div style="width:5px;height:5px;border-radius:50%;background:{col};margin-top:1px"></div>'
                f'<div style="width:1px;height:10px;background:{col};opacity:.25"></div></div>'
                f'<div style="flex:1;margin-top:1px">{ln("85%")}{ln("68%")}</div></div>')

    # ── render each thumbnail inner HTML ─────────────────────────────────────
    def render_thumb(tid, accent, layout, sidebar_bg, header_bg):
        body_content = ""
        header = ""

        if layout == "sidebar":
            sb = sidebar_bg or "#1e293b"
            # avatar + name block
            sb_inner = (
                avatar(accent)
                + f'<div style="height:3px;width:75%;background:rgba(255,255,255,0.65);border-radius:1px;margin:0 auto 1px"></div>'
                + f'<div style="height:2px;width:50%;background:{accent};opacity:.6;border-radius:1px;margin:0 auto 2px"></div>'
                + f'<div style="height:1px;width:80%;background:rgba(255,255,255,0.12);border-radius:1px;margin:0 auto 2px"></div>'
                + sl(accent, "70%")
                + pill_row(accent)
                + sl(accent, "60%")
                + skill_dots(accent)
            )
            body_content = (
                f'<div style="display:flex;flex:1;min-height:0">'
                f'<div style="width:34%;background:{sb};padding:4px 3px;display:flex;flex-direction:column;">'
                + sb_inner +
                f'</div>'
                f'<div style="flex:1;padding:4px 4px;display:flex;flex-direction:column;">'
                + sl(accent) + exp_entry(accent) + exp_entry(accent, "75%", "55%")
                + sl(accent) + ln("90%") + ln("72%") + ln("82%")
                + f'</div>'
                f'</div>'
            )

        elif layout == "timeline":
            hb = header_bg or accent
            header = (
                f'<div style="height:4px;background:{hb};border-radius:3px 3px 0 0"></div>'
                f'<div style="padding:3px 5px 2px">'
                f'<div style="height:3px;width:50%;background:rgba(255,255,255,0.7);border-radius:1px;margin-bottom:2px"></div>'
                f'<div style="height:2px;width:30%;background:{accent};opacity:.6;border-radius:1px"></div>'
                f'</div>'
            )
            body_content = (
                f'<div style="flex:1;padding:2px 5px;display:flex;flex-direction:column;">'
                + sl(accent) + timeline_entry(accent) + timeline_entry(accent)
                + sl(accent) + ln("88%") + ln("70%")
                + f'</div>'
            )

        elif header_bg:  # band header (Executive, Burgundy)
            header = (
                f'<div style="background:{header_bg};padding:5px 5px;border-radius:3px 3px 0 0">'
                f'<div style="height:3px;width:50%;background:rgba(255,255,255,0.9);border-radius:1px;margin-bottom:2px"></div>'
                f'<div style="height:2px;width:32%;background:rgba(255,255,255,0.55);border-radius:1px"></div>'
                f'<div style="display:flex;gap:3px;margin-top:2px">'
                f'<div style="height:1.5px;width:15%;background:rgba(255,255,255,0.3);border-radius:1px"></div>'
                f'<div style="height:1.5px;width:15%;background:rgba(255,255,255,0.3);border-radius:1px"></div>'
                f'</div></div>'
            )
            body_content = (
                f'<div style="flex:1;padding:3px 5px;display:flex;flex-direction:column;">'
                + sl(accent) + exp_entry(accent) + exp_entry(accent, "70%", "55%")
                + sl(accent) + ln("88%") + ln("72%") + ln("80%")
                + f'</div>'
            )

        elif tid in ("modern",):  # centred header
            header = (
                f'<div style="text-align:center;padding:5px 4px 3px;border-bottom:1.5px solid {accent}">'
                f'<div style="height:3px;width:46%;background:rgba(255,255,255,0.75);border-radius:1px;margin:0 auto 2px"></div>'
                f'<div style="height:2px;width:28%;background:{accent};border-radius:1px;margin:0 auto 2px"></div>'
                f'<div style="display:flex;justify-content:center;gap:3px">'
                f'<div style="height:1.5px;width:13%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
                f'<div style="height:1.5px;width:13%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
                f'<div style="height:1.5px;width:13%;background:rgba(255,255,255,0.2);border-radius:1px"></div>'
                f'</div></div>'
            )
            body_content = (
                f'<div style="flex:1;padding:3px 5px;display:flex;flex-direction:column;">'
                + sl(accent) + ln("90%","rgba(255,255,255,0.16)") + ln("80%","rgba(255,255,255,0.12)") + ln("70%","rgba(255,255,255,0.10)")
                + sl(accent) + exp_entry(accent) + exp_entry(accent, "75%", "58%")
                + sl(accent) + pill_row(accent)
                + f'</div>'
            )

        else:  # standard single-col with top bar
            lc = accent if accent != "#e5e5e5" else "rgba(255,255,255,0.55)"
            header = (
                f'<div style="height:4px;background:{accent};border-radius:3px 3px 0 0"></div>'
                f'<div style="padding:3px 5px 2px;border-bottom:1px solid rgba(255,255,255,0.06)">'
                f'<div style="height:3px;width:52%;background:rgba(255,255,255,0.7);border-radius:1px;margin-bottom:2px"></div>'
                f'<div style="height:2px;width:30%;background:{lc};opacity:.7;border-radius:1px"></div>'
                f'<div style="display:flex;gap:3px;margin-top:2px">'
                f'<div style="height:1.5px;width:15%;background:rgba(255,255,255,0.18);border-radius:1px"></div>'
                f'<div style="height:1.5px;width:15%;background:rgba(255,255,255,0.18);border-radius:1px"></div>'
                f'</div></div>'
            )
            body_content = (
                f'<div style="flex:1;padding:3px 5px;display:flex;flex-direction:column;">'
                + sl(lc) + exp_entry(accent if accent != "#e5e5e5" else "rgba(255,255,255,0.4)") + exp_entry(accent if accent != "#e5e5e5" else "rgba(255,255,255,0.4)", "70%", "55%")
                + sl(lc) + ln("90%") + ln("74%") + ln("82%")
                + sl(lc) + pill_row(accent if accent != "#e5e5e5" else "rgba(255,255,255,0.4)")
                + f'</div>'
            )

        return header + body_content

    # ── build the gallery HTML block with embedded JS ────────────────────────
    # Build JSON-like data for each template (used by the JS)
    import json as _json

    tmpl_data = []
    for tid, name, accent, layout, sidebar_bg, header_bg, ats, tags, font in TEMPLATES:
        col_type = "Two-column" if layout == "sidebar" else "Single-column"
        tmpl_data.append({
            "id": tid, "name": name, "accent": accent,
            "ats": ats, "tags": tags, "font": font,
            "colType": col_type
        })
    tmpl_json = _json.dumps(tmpl_data)

    # Build thumbnail HTML for each template
    thumbs_html = ""
    for i, (tid, name, accent, layout, sidebar_bg, header_bg, ats, tags, font) in enumerate(TEMPLATES):
        inner = render_thumb(tid, accent, layout, sidebar_bg, header_bg)
        act_style = f'border-color:{accent};box-shadow:0 0 0 2px {accent}33;' if i == 0 else ''
        thumbs_html += (
            f'<div class="hl-tmpl" id="tmpl-{tid}" data-idx="{i}" '
            f'style="display:flex;flex-direction:column;padding:0;overflow:hidden;cursor:pointer;'
            f'transition:border-color .18s,box-shadow .18s,transform .15s;{act_style}">'
            + inner +
            f'<div class="hl-tmpl-ats" style="position:absolute;top:4px;right:4px;'
            f'background:rgba(0,0,0,0.55);backdrop-filter:blur(4px);border-radius:3px;'
            f'padding:1px 4px;font-size:7px;font-weight:700;letter-spacing:.4px;color:#30d158;'
            f'opacity:0;transition:opacity .2s;">ATS</div>'
            + f'</div>'
        )

    # Build the tooltip HTML
    tooltip_html = (
        '<div id="hl-tmpl-tooltip" style="display:none;position:fixed;z-index:9999;'
        'background:#1a1a1e;border:1px solid rgba(255,255,255,0.12);border-radius:14px;'
        'padding:14px;width:200px;pointer-events:none;'
        'box-shadow:0 24px 60px rgba(0,0,0,0.8);transition:opacity .15s;">'
        '<div id="tt-preview" style="width:100%;height:130px;background:#141416;border-radius:8px;'
        'overflow:hidden;margin-bottom:10px;border:1px solid rgba(255,255,255,0.07)"></div>'
        '<div id="tt-name" style="font-size:12px;font-weight:700;color:#f5f5f7;margin-bottom:4px"></div>'
        '<div id="tt-meta" style="font-size:10px;color:rgba(245,245,247,0.4);margin-bottom:6px"></div>'
        '<div id="tt-tags" style="display:flex;flex-wrap:wrap;gap:4px"></div>'
        '</div>'
    )

    # Build the JS that wires everything together
    js = f"""
<script>
(function(){{
  var DATA = {tmpl_json};
  var active = 0;
  var APP = '{APP_URL}';

  // tooltip
  var tip = document.getElementById('hl-tmpl-tooltip');
  var ttPreview = document.getElementById('tt-preview');
  var ttName = document.getElementById('tt-name');
  var ttMeta = document.getElementById('tt-meta');
  var ttTags = document.getElementById('tt-tags');
  var infoName = document.getElementById('hl-info-name');
  var infoMeta = document.getElementById('hl-info-meta');
  var infoAts  = document.getElementById('hl-info-ats');
  var infoFont = document.getElementById('hl-info-font');
  var infoDot  = document.getElementById('hl-info-dot');
  var filterBtns = document.querySelectorAll('.hl-filter-btn');
  var allCards = document.querySelectorAll('.hl-tmpl[data-idx]');

  function setActive(idx) {{
    active = idx;
    var d = DATA[idx];
    allCards.forEach(function(c){{
      var ci = parseInt(c.getAttribute('data-idx'));
      if(ci === idx) {{
        c.style.borderColor = d.accent;
        c.style.boxShadow = '0 0 0 2px '+d.accent+'33';
        c.style.transform = 'scale(1.04)';
      }} else {{
        c.style.borderColor = 'rgba(255,255,255,0.07)';
        c.style.boxShadow = 'none';
        c.style.transform = 'scale(1)';
      }}
    }});
    if(infoName) {{
      infoName.textContent = d.name + ' — ATS ' + (d.ats.length > 3 ? 'Certified' : 'Optimised');
      infoName.style.color = d.accent;
    }}
    if(infoMeta) infoMeta.textContent = d.font + ' · ' + d.colType;
    if(infoAts)  infoAts.textContent  = d.ats;
    if(infoFont) infoFont.textContent = d.font;
    if(infoDot)  infoDot.style.background = d.accent;
  }}

  function showTooltip(card, idx) {{
    var d = DATA[idx];
    ttName.textContent = d.name;
    ttMeta.textContent = d.font + ' · ' + d.colType;
    ttTags.innerHTML = d.tags.map(function(t){{
      return '<span style="padding:2px 7px;border-radius:3px;font-size:9px;font-weight:700;'
        + 'background:'+d.accent+'22;color:'+d.accent+';border:1px solid '+d.accent+'44">'+t+'</span>';
    }}).join('');
    // copy the card inner HTML into the tooltip preview
    ttPreview.innerHTML = card.innerHTML;
    ttPreview.style.transform = 'scale(1)';

    var rect = card.getBoundingClientRect();
    var tipW = 200, tipH = 220;
    var left = rect.right + 8;
    var top  = rect.top + (rect.height/2) - (tipH/2);
    if(left + tipW > window.innerWidth - 8) left = rect.left - tipW - 8;
    if(top < 8) top = 8;
    if(top + tipH > window.innerHeight - 8) top = window.innerHeight - tipH - 8;
    tip.style.left  = left + 'px';
    tip.style.top   = top  + 'px';
    tip.style.display = 'block';
    tip.style.opacity = '1';
  }}

  function hideTooltip() {{
    tip.style.opacity = '0';
    setTimeout(function(){{ tip.style.display='none'; }}, 150);
  }}

  allCards.forEach(function(card) {{
    var idx = parseInt(card.getAttribute('data-idx'));
    var atsLabel = card.querySelector('.hl-tmpl-ats');

    card.addEventListener('click', function() {{ setActive(idx); }});

    card.addEventListener('mouseenter', function() {{
      showTooltip(card, idx);
      if(atsLabel) atsLabel.style.opacity = '1';
    }});
    card.addEventListener('mouseleave', function() {{
      hideTooltip();
      if(atsLabel) atsLabel.style.opacity = '0';
    }});
  }});

  // filter tabs
  filterBtns.forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var f = btn.getAttribute('data-filter');
      filterBtns.forEach(function(b){{ b.classList.remove('active'); }});
      btn.classList.add('active');
      allCards.forEach(function(c) {{
        var idx = parseInt(c.getAttribute('data-idx'));
        var d = DATA[idx];
        var show = f === 'all'
          || (f === 'single' && d.colType === 'Single-column')
          || (f === 'two'    && d.colType === 'Two-column');
        c.style.display = show ? 'flex' : 'none';
      }});
    }});
  }});

  // scroll row hint
  var grid = document.getElementById('hl-tmpl-grid-inner');
  if(grid) {{
    grid.addEventListener('scroll', function() {{
      var fade = document.getElementById('hl-grid-fade');
      if(fade) fade.style.opacity = grid.scrollLeft > 20 ? '0' : '1';
    }});
  }}

  setActive(0);
}})();
</script>"""

    # ── assemble the full widget ─────────────────────────────────────────────
    filter_tabs = (
        '<div style="display:flex;gap:6px;margin-bottom:12px;align-items:center">'
        '<span style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1px;'
        'color:rgba(245,245,247,0.28);margin-right:4px">Filter</span>'
        '<button class="hl-filter-btn active" data-filter="all" '
        'style="padding:3px 10px;border-radius:6px;border:1px solid rgba(255,255,255,0.13);'
        'background:rgba(255,255,255,0.08);color:rgba(245,245,247,0.7);font-size:10px;'
        'font-weight:600;cursor:pointer;transition:all .15s;letter-spacing:.3px">All 15</button>'
        '<button class="hl-filter-btn" data-filter="single" '
        'style="padding:3px 10px;border-radius:6px;border:1px solid rgba(255,255,255,0.07);'
        'background:transparent;color:rgba(245,245,247,0.4);font-size:10px;'
        'font-weight:600;cursor:pointer;transition:all .15s;letter-spacing:.3px">Single-col</button>'
        '<button class="hl-filter-btn" data-filter="two" '
        'style="padding:3px 10px;border-radius:6px;border:1px solid rgba(255,255,255,0.07);'
        'background:transparent;color:rgba(245,245,247,0.4);font-size:10px;'
        'font-weight:600;cursor:pointer;transition:all .15s;letter-spacing:.3px">Two-col</button>'
        '</div>'
    )

    grid_wrap = (
        '<div style="position:relative">'
        '<div id="hl-tmpl-grid-inner" '
        'style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;'
        'max-height:284px;overflow-y:auto;overflow-x:hidden;padding-right:4px;'
        'scrollbar-width:thin;scrollbar-color:rgba(255,255,255,0.1) transparent;">'
        + thumbs_html +
        '</div>'
        '<div id="hl-grid-fade" style="position:absolute;bottom:0;left:0;right:0;height:36px;'
        'background:linear-gradient(to bottom,transparent,#0f0f10);pointer-events:none;'
        'border-radius:0 0 10px 10px;transition:opacity .3s"></div>'
        '</div>'
    )

    info_bar = (
        '<div style="margin-top:12px;padding:12px 14px;background:rgba(10,132,255,0.06);'
        'border-radius:12px;border:1px solid rgba(10,132,255,0.18);'
        'display:flex;align-items:center;justify-content:space-between;gap:12px">'
        '<div style="display:flex;align-items:center;gap:8px;min-width:0;">'
        '<div id="hl-info-dot" style="width:7px;height:7px;border-radius:50%;background:#0a84ff;flex-shrink:0"></div>'
        '<div style="min-width:0">'
        '<div id="hl-info-name" style="font-size:12px;font-weight:700;color:#0a84ff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">Modern — ATS Certified</div>'
        '<div style="display:flex;align-items:center;gap:8px;margin-top:2px">'
        '<div id="hl-info-meta" style="font-size:10px;color:rgba(245,245,247,0.34)">Sora · Single-column</div>'
        '<div id="hl-info-ats" style="font-size:10px;color:#30d158;letter-spacing:1px">★★★</div>'
        '</div>'
        '</div></div>'
        '<a href="' + APP_URL + '" target="_blank" '
        'style="padding:8px 18px;background:#0a84ff;color:#fff;border-radius:100px;'
        'font-size:12px;font-weight:600;text-decoration:none;white-space:nowrap;flex-shrink:0">'
        'Use this</a>'
        '</div>'
    )

    return (
        '<style>'
        '.hl-filter-btn.active{background:rgba(255,255,255,0.1)!important;'
        'border-color:rgba(255,255,255,0.25)!important;color:rgba(245,245,247,0.9)!important}'
        '.hl-filter-btn:hover{background:rgba(255,255,255,0.06)!important;'
        'color:rgba(245,245,247,0.6)!important}'
        '#hl-tmpl-grid-inner::-webkit-scrollbar{width:3px}'
        '#hl-tmpl-grid-inner::-webkit-scrollbar-track{background:transparent}'
        '#hl-tmpl-grid-inner::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.1);border-radius:2px}'
        '</style>'
        + tooltip_html
        + filter_tabs
        + grid_wrap
        + info_bar
        + js
    )

def job_cards():
    jobs = [("SDE II","Google","Mountain View · Full-time","#4285f4","G",True),("ML Engineer","Anthropic","Remote · Full-time","#d97706","A",False),("Backend Dev","Razorpay","Bangalore · Full-time","#2563eb","R",False),("Data Analyst","Zepto","Mumbai · Hybrid","#7c3aed","Z",False)]
    out = ""
    for title,co,meta,col,letter,featured in jobs:
        bb  = "rgba(10,132,255,0.12)" if featured else "rgba(255,255,255,0.05)"
        bc  = "#4db3ff"               if featured else "rgba(245,245,247,0.3)"
        btx = "Featured"              if featured else "New"
        out += '<div class="hl-job"><div class="hl-job-logo" style="background:'+col+'22;color:'+col+'">'+letter+'</div><div style="flex:1;min-width:0"><div class="hl-job-title">'+title+' \u2014 '+co+'</div><div class="hl-job-co">'+meta+'</div></div><div class="hl-job-badge" style="background:'+bb+';color:'+bc+';border:1px solid '+bc+'40">'+btx+'</div></div>'
    return out

def checklist():
    items = ["ATS score in seconds","Bias detection & rewrite","15 resume templates","Cover letter generator","Live job search","AI Interview Coach"]
    chk = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return "".join('<div class="hl-check">'+chk+'<span>'+item+'</span></div>' for item in items)

def pills(labels):
    return "".join('<span class="hl-pill">'+l+'</span>' for l in labels)

# ─── SECTIONS ─────────────────────────────────────────────────────────────────
def render_nav():
    H('<div id="sp"></div>'
      '<div class="hl-nav"><div class="hl-nav-inner">'
      '<a href="#" class="hl-logo"><div class="hl-logo-icon">'
      '<svg width="18" height="18" viewBox="0 0 24 24" fill="none">'
      '<path d="M12 2L2 7l10 5 10-5-10-5z M2 17l10 5 10-5 M2 12l10 5 10-5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
      '</svg></div>HIRELYZER</a>'
      '<div class="hl-nav-links">'
      '<a href="#how">How it works</a>'
      '<a href="#analyzer">Analyzer</a>'
      '<a href="#builder">Builder</a>'
      '<a href="#career">Career Hub</a>'
      '<a href="#contact">Contact</a>'
      '</div>'
      '<a href="' + APP_URL + '" target="_blank" class="hl-nav-cta">'
      '<svg width="12" height="12" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Open App</a>'
      '</div></div>')

def render_hero():
    ring = ats_ring(78)
    bars = ats_bars()
    H('<div class="hl-hero">'
      '<div class="hl-hero-glow"></div>'
      '<div class="hl-hero-fade"></div>'
      '<div class="hl-hero-content">'
      '<div class="hl-eyebrow">'
      '<svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>'
      'AI-Powered Career Intelligence'
      '</div>'
      '<h1 class="hl-h1">The last resume tool<br>you&rsquo;ll ever <em class="hl-h1-blue">need</em></h1>'
      '<p class="hl-hero-sub">Upload your resume. Hirelyzer instantly scores it for ATS compatibility, detects bias, rewrites with AI, and connects you to jobs &mdash; all in one place.</p>'
      '<div class="hl-ctas">'
      '<a href="' + APP_URL + '" target="_blank" class="hl-btn-p">'
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>'
      'Get Started Free</a>'
      '<a href="#how" class="hl-btn-g">See how it works'
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '</a></div>'

      '<div class="hl-card">'
      '<div class="hl-card-bar">'
      '<div class="hl-dot" style="background:#ff5f57"></div>'
      '<div class="hl-dot" style="background:#febc2e"></div>'
      '<div class="hl-dot" style="background:#28c840"></div>'
      '<span class="hl-card-tab">hirelyzer &mdash; resume_analysis.pdf</span>'
      '</div>'
      '<div class="hl-card-body"><div class="hl-card-grid">'

      # col 1 - ATS
      '<div>'
      '<div class="hl-ptitle"><svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#30d158"/></svg>ATS Score</div>'
      '<div style="display:flex;align-items:center;gap:16px;margin-bottom:18px">'
      + ring +
      '<div>'
      '<div style="font-size:9px;color:rgba(245,245,247,0.34);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:4px">Overall</div>'
      '<div style="font-size:11px;color:#30d158;font-weight:600;margin-top:2px">Good &middot; Minor fixes</div>'
      '</div></div>'
      + bars +
      '</div>'

      # col 2 - Bias
      '<div>'
      '<div class="hl-ptitle"><svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#bf5af2"/></svg>Bias Analysis</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">'
      '<div style="padding:11px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)">'
      '<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:4px">Masculine</div>'
      '<div style="font-size:22px;font-weight:800;color:#4db3ff">8</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.34)">flagged</div></div>'
      '<div style="padding:11px;background:rgba(191,90,242,0.06);border-radius:10px;border:1px solid rgba(191,90,242,0.15)">'
      '<div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:4px">Feminine</div>'
      '<div style="font-size:22px;font-weight:800;color:#d07ef7">3</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.34)">flagged</div></div>'
      '</div>'
      '<div class="hl-words">'
      '<span class="wc wc-m">driven</span>'
      '<span class="wc wc-m">dominate</span>'
      '<span class="wc wc-f">nurture</span>'
      '<span class="wc wc-m">aggressive</span>'
      '<span class="wc wc-n">deliver</span>'
      '<span class="wc wc-n">execute</span>'
      '</div>'
      '<div style="padding:10px 12px;background:rgba(48,209,88,0.06);border-radius:10px;border:1px solid rgba(48,209,88,0.18)">'
      '<div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:4px">AI Rewrite Applied</div>'
      '<div style="font-size:11px;color:rgba(245,245,247,0.54);line-height:1.6">'
      '<span style="text-decoration:line-through;opacity:.4">Aggressively drove</span>'
      ' &rarr; <span style="color:#30d158">Accelerated</span> delivery across 3 teams'
      '</div></div>'
      '</div>'

      # col 3 - Quick Actions
      '<div>'
      '<div class="hl-ptitle"><svg width="9" height="9" viewBox="0 0 9 9"><circle cx="4.5" cy="4.5" r="4.5" fill="#ff9f0a"/></svg>Quick Actions</div>'
      '<div style="display:flex;flex-direction:column;gap:8px">'
      '<div style="padding:9px 12px;background:rgba(48,209,88,0.07);border-radius:9px;border:1px solid rgba(48,209,88,0.18);display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-size:12px;color:#30d158;font-weight:600">Single-column layout</span></div>'
      '<div style="padding:9px 12px;background:rgba(48,209,88,0.07);border-radius:9px;border:1px solid rgba(48,209,88,0.18);display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-size:12px;color:#30d158;font-weight:600">Contact info present</span></div>'
      '<div style="padding:9px 12px;background:rgba(255,159,10,0.07);border-radius:9px;border:1px solid rgba(255,159,10,0.18);display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg><span style="font-size:12px;color:#ff9f0a;font-weight:600">Add LinkedIn URL</span></div>'
      '<div style="padding:9px 12px;background:rgba(255,69,58,0.07);border-radius:9px;border:1px solid rgba(255,69,58,0.18);display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2" stroke-linecap="round"/></svg><span style="font-size:12px;color:#ff453a;font-weight:600">No skills section</span></div>'
      '<div style="padding:9px 12px;background:rgba(255,69,58,0.07);border-radius:9px;border:1px solid rgba(255,69,58,0.18);display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#ff453a" stroke-width="2" stroke-linecap="round"/></svg><span style="font-size:12px;color:#ff453a;font-weight:600">Objective section outdated</span></div>'
      '</div></div>'

      '</div></div></div>'  # close grid, card-body, card

      '<div class="hl-stats">'
      '<div class="hl-stat"><div class="hl-stat-n">15+</div><div class="hl-stat-l">Templates</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n">5</div><div class="hl-stat-l">Core Modules</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n">AI</div><div class="hl-stat-l">LLM Powered</div></div>'
      '<div class="hl-stat"><div class="hl-stat-n">Free</div><div class="hl-stat-l">No Credit Card</div></div>'
      '</div>'
      '</div></div>')  # close hero-content, hero

def render_how():
    H('<div id="how" style="padding:100px 0 60px;background:#000">'
      '<div class="hl-section">'
      '<div class="hl-divider">How it works</div>'
      '<div class="hl-steps">'

      '<div class="hl-step"><span class="hl-step-n">01</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(10,132,255,0.1)"/><path d="M22 28V20M22 20L19 23M22 20L25 23" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 30h14" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round"/><rect x="14" y="13" width="16" height="19" rx="3" stroke="#0a84ff" stroke-width="1.4" stroke-dasharray="3 2" fill="none"/></svg>'
      '<div class="hl-step-title">Upload your resume</div>'
      '<div class="hl-step-desc">Drop any PDF. Our parser handles messy formats, multi-column layouts, and scanned documents via OCR fallback.</div></div>'

      '<div class="hl-step"><span class="hl-step-n">02</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(48,209,88,0.1)"/><circle cx="20" cy="20" r="7" stroke="#30d158" stroke-width="1.5" fill="none"/><path d="M20 17v3l2 1.5" stroke="#30d158" stroke-width="1.5" stroke-linecap="round"/><path d="M25.2 25.2l3.5 3.5" stroke="#30d158" stroke-width="1.7" stroke-linecap="round"/></svg>'
      '<div class="hl-step-title">Instant AI analysis</div>'
      '<div class="hl-step-desc">ATS scoring, bias detection, grammar check, keyword matching &mdash; all computed in seconds with detailed feedback.</div></div>'

      '<div class="hl-step"><span class="hl-step-n">03</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(191,90,242,0.1)"/><rect x="12" y="11" width="13" height="18" rx="2.5" stroke="#bf5af2" stroke-width="1.5" fill="none"/><rect x="19" y="16" width="14" height="18" rx="2.5" fill="rgba(191,90,242,0.08)" stroke="#bf5af2" stroke-width="1.5"/><path d="M22 21h8M22 24.5h8M22 28h5" stroke="#bf5af2" stroke-width="1.3" stroke-linecap="round"/><circle cx="32" cy="13" r="4" fill="#bf5af2"/><path d="M30.5 13l1 1 2-2" stroke="#fff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '<div class="hl-step-title">Build or rewrite</div>'
      '<div class="hl-step-desc">Use the AI rewriter or open the full Resume Builder. Choose from 15 templates, generate a cover letter, export to PDF or DOCX.</div></div>'

      '<div class="hl-step"><span class="hl-step-n">04</span>'
      '<svg class="hl-step-icon" viewBox="0 0 44 44" fill="none"><rect width="44" height="44" rx="12" fill="rgba(255,159,10,0.1)"/><path d="M22 28c-3.31 0-6-2.69-6-6 0-4 3-8 6-9 3 1 6 5 6 9 0 3.31-2.69 6-6 6z" stroke="#ff9f0a" stroke-width="1.5" fill="none"/><circle cx="22" cy="22" r="2" fill="#ff9f0a"/><path d="M29 13l-2 2M15 13l2 2" stroke="#ff9f0a" stroke-width="1.4" stroke-linecap="round"/></svg>'
      '<div class="hl-step-title">Apply with confidence</div>'
      '<div class="hl-step-desc">Discover live job listings, salary benchmarks, curated courses, and practice with the AI Interview Coach before applying.</div></div>'

      '</div></div></div>')

def render_story_ats():
    ring = ats_ring(78)
    bars = ats_bars()
    p = pills(["ATS Score","6-Dimension Breakdown","Keyword Gap","Grammar Check","Downloadable Report"])
    H('<div id="analyzer" class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      '<div>'
      '<div class="hl-story-num">Feature 01 &mdash; Resume Analyzer</div>'
      '<h2 class="hl-story-h">Your resume, <span class="hl-blue">scored like a machine</span> reads it</h2>'
      '<p class="hl-story-p">Most resumes never reach a human. Applicant Tracking Systems silently filter them on format, missing keywords, or structural issues. Hirelyzer&rsquo;s analyzer replicates how ATS parsers actually read your document &mdash; not just a surface keyword match.</p>'
      '<p class="hl-story-p">You get a score across six dimensions, a prioritised fix list, grammar and readability signals, and a full keyword-gap report mapped to the roles you care about.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="11" height="11" viewBox="0 0 11 11"><circle cx="5.5" cy="5.5" r="5.5" fill="#30d158"/></svg>ATS Analysis Report</div>'
      '<div style="display:flex;align-items:center;gap:18px;margin-bottom:22px">'
      + ring +
      '<div>'
      '<div style="font-size:9px;color:rgba(245,245,247,0.34);text-transform:uppercase;letter-spacing:.9px;font-weight:700;margin-bottom:4px">Overall Score</div>'
      '<div style="font-size:11px;color:#30d158;font-weight:600">Good &middot; Minor fixes needed</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.34);margin-top:4px">Parsed in 1.4s</div>'
      '</div></div>'
      + bars +
      '</div></div>'
      '</div></div></div>')

def render_story_bias():
    p = pills(["Gender-coded Detection","AI Neutral Rewrite","Lexicon of 400+ Words","One-click Apply"])
    H('<div class="hl-story-alt"><div class="hl-section"><div class="hl-story-grid">'
      '<div style="order:2">'
      '<div class="hl-story-num">Feature 02 &mdash; Bias Detection</div>'
      '<h2 class="hl-story-h">Bias-free language that <span class="hl-purp">opens every door</span></h2>'
      '<p class="hl-story-p">Gender-coded words can unconsciously signal culture fit to recruiters. Hirelyzer scans every verb, adjective, and phrase against a curated bias lexicon of 400+ terms.</p>'
      '<p class="hl-story-p">The AI rewriter suggests impact-neutral alternatives, preserving your achievements while broadening appeal across hiring contexts.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div style="order:1"><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="11" height="11" viewBox="0 0 11 11"><circle cx="5.5" cy="5.5" r="5.5" fill="#bf5af2"/></svg>Bias Analysis Report</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px">'
      '<div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:6px">Masculine</div><div style="font-size:26px;font-weight:800;color:#4db3ff">8</div><div style="font-size:11px;color:rgba(245,245,247,0.34)">words flagged</div></div>'
      '<div style="padding:14px;background:rgba(191,90,242,0.06);border-radius:12px;border:1px solid rgba(191,90,242,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:6px">Feminine</div><div style="font-size:26px;font-weight:800;color:#d07ef7">3</div><div style="font-size:11px;color:rgba(245,245,247,0.34)">words flagged</div></div>'
      '</div>'
      '<div style="font-size:10px;color:rgba(245,245,247,0.34);font-weight:700;text-transform:uppercase;letter-spacing:.9px;margin-bottom:10px">Detected language</div>'
      '<div class="hl-words"><span class="wc wc-m">driven</span><span class="wc wc-m">aggressive</span><span class="wc wc-m">dominate</span><span class="wc wc-m">champion</span><span class="wc wc-f">nurture</span><span class="wc wc-f">support</span><span class="wc wc-n">deliver</span><span class="wc wc-n">execute</span></div>'
      '<div style="padding:14px;background:rgba(48,209,88,0.06);border-radius:12px;border:1px solid rgba(48,209,88,0.18)">'
      '<div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:6px">AI Rewrite Applied</div>'
      '<div style="font-size:12px;color:rgba(245,245,247,0.54);line-height:1.65"><span style="text-decoration:line-through;opacity:.45">Aggressively drove growth</span> &rarr; <span style="color:#30d158">Accelerated high-impact results</span> across 3 teams</div>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_story_builder():
    tmpl = tmpl_gallery()
    p = pills(["15 Templates","DOCX + PDF Export","AI Cover Letter","Live Preview","ATS Single-Column"])
    H('<div id="builder" class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      '<div>'
      '<div class="hl-story-num">Feature 03 &mdash; Resume Builder</div>'
      '<h2 class="hl-story-h">Build resumes that <span class="hl-green">look as good</span> as they parse</h2>'
      '<p class="hl-story-p">Fifteen ATS-optimised templates &mdash; from understated minimal to executive prestige &mdash; all built on strict single-column structures that parse correctly in every major hiring platform.</p>'
      '<p class="hl-story-p">Export to DOCX (three ATS compliance levels) or PDF. One click generates a tailored cover letter for your target company, formatted and ready to send.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="10" height="14" rx="2" stroke="#30d158" stroke-width="1.5"/><rect x="11" y="7" width="10" height="14" rx="2" fill="rgba(48,209,88,.08)" stroke="#30d158" stroke-width="1.5"/><path d="M14 11h5M14 14h5M14 17h3" stroke="#30d158" stroke-width="1.3" stroke-linecap="round"/></svg>Template Gallery &mdash; 15 Designs</div>'
      '<div class="hl-tmpl-grid">' + tmpl + '</div>'
      '<div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.18);display:flex;align-items:center;justify-content:space-between;gap:12px">'
      '<div><div style="font-size:12px;font-weight:700;color:#0a84ff">Modern &mdash; ATS Certified</div><div style="font-size:11px;color:rgba(245,245,247,0.34);margin-top:2px">Sora &middot; Navy headings &middot; Single-column</div></div>'
      '<a href="' + APP_URL + '" target="_blank" style="padding:8px 18px;background:#0a84ff;color:#fff;border-radius:100px;font-size:12px;font-weight:600;text-decoration:none;white-space:nowrap;flex-shrink:0">Use this</a>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_story_career():
    cards = job_cards()
    p = pills(["Live Job Listings","Salary Benchmarks","Course Recommendations","Skills Radar","Remote Filter"])
    H('<div id="career" class="hl-story-alt"><div class="hl-section"><div class="hl-story-grid">'
      '<div style="order:2">'
      '<div class="hl-story-num">Feature 04 &mdash; Career Intelligence</div>'
      '<h2 class="hl-story-h">Jobs, salaries, courses &mdash; <span class="hl-amber">one place</span></h2>'
      '<p class="hl-story-p">The Job Search Hub pulls live listings from LinkedIn, Naukri, Foundit, and Indeed &mdash; or uses the JSearch/RapidAPI engine with remote and employment-type filters.</p>'
      '<p class="hl-story-p">Hirelyzer surfaces salary benchmarks by role and market, curated courses mapped to skill gaps in your resume, and prep videos &mdash; all linked to your career profile.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div style="order:1"><div class="hl-panel">'
      '<div class="hl-ptitle"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><rect x="2" y="7" width="20" height="14" rx="2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="#ff9f0a" stroke-width="1.5"/><path d="M2 13h20" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/></svg>Job Search Hub</div>'
      + cards +
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px">'
      '<div style="padding:12px;background:rgba(255,159,10,0.06);border-radius:10px;border:1px solid rgba(255,159,10,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:5px">Avg Salary</div><div style="font-size:20px;font-weight:800;color:#ff9f0a">&#8377;18&ndash;32 LPA</div><div style="font-size:11px;color:rgba(245,245,247,0.34)">Backend &middot; India</div></div>'
      '<div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)"><div style="font-size:9px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:5px">Platforms</div><div style="font-size:13px;font-weight:700;color:#f5f5f7;line-height:1.7">LinkedIn &middot; Naukri<br>Foundit &middot; Indeed</div></div>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_story_interview():
    sbars = score_bars()
    radar = radar_svg()
    p = pills(["Resume-based Questions","Real-time AI Scoring","Radar Chart","Session History","Downloadable Report"])
    H('<div class="hl-story"><div class="hl-section"><div class="hl-story-grid">'
      '<div>'
      '<div class="hl-story-num">Feature 05 &mdash; AI Interview Coach</div>'
      '<h2 class="hl-story-h">Practice until <span class="hl-blue">every answer</span> lands</h2>'
      '<p class="hl-story-p">Upload your resume and Hirelyzer generates interview questions derived directly from your actual experience &mdash; not generic prompts. Answer in free text; the AI coach scores you on communication, technical depth, confidence, structure, and use of concrete examples.</p>'
      '<p class="hl-story-p">Every session ends with a performance radar chart, a detailed Q&amp;A review, and course recommendations tied to your weakest dimensions.</p>'
      '<div class="hl-pills">' + p + '</div>'
      '</div>'
      '<div><div class="hl-panel">'
      '<div class="hl-ptitle" style="justify-content:space-between">'
      '<div style="display:flex;align-items:center;gap:8px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#ff453a" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>Mock Interview &middot; Session 3</div>'
      '<div class="hl-score-badge"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg>82 / 100</div>'
      '</div>'
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">'
      '<div>'
      '<div class="hl-qa"><div class="hl-q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px"><circle cx="12" cy="12" r="10" stroke="#0a84ff" stroke-width="1.5"/><path d="M12 16v-4M12 8h.01" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round"/></svg>Describe your most complex backend system.</div><div class="hl-a">Built a multi-tenant microservices platform handling 2M events/day using Kafka, Redis, and PostgreSQL with 40% lower P99 latency.</div></div>'
      '<div class="hl-qa"><div class="hl-q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px"><circle cx="12" cy="12" r="10" stroke="#bf5af2" stroke-width="1.5"/><path d="M12 16v-4M12 8h.01" stroke="#bf5af2" stroke-width="1.8" stroke-linecap="round"/></svg>How do you handle technical debt?</div><div class="hl-a">I prioritise tech debt as a first-class roadmap item, quantifying velocity cost before pitching refactors to stakeholders.</div></div>'
      '<div style="margin-top:12px"><div style="font-size:10px;text-transform:uppercase;letter-spacing:.9px;color:rgba(245,245,247,0.34);font-weight:700;margin-bottom:8px">Score breakdown</div>'
      + sbars +
      '</div></div>'
      '<div class="hl-radar-wrap">' + radar + '<div style="font-size:11px;color:rgba(245,245,247,0.34);margin-top:6px;text-align:center">Performance radar</div></div>'
      '</div>'
      '</div></div>'
      '</div></div></div>')

def render_cta():
    chk = checklist()
    H('<div class="hl-section">'
      '<div id="contact" class="hl-cta"><div class="hl-cta-glow"></div>'
      '<div class="hl-eyebrow" style="margin:0 auto 28px"><svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>Free to use &middot; No credit card required</div>'
      '<div class="hl-cta-h">Your next job starts with a better resume</div>'
      '<p class="hl-cta-sub">Join professionals already using Hirelyzer to pass ATS filters, remove bias, and land more interviews.</p>'
      '<div class="hl-cta-btns">'
      '<a href="' + APP_URL + '" target="_blank" class="hl-btn-p" style="font-size:16px;padding:16px 36px"><svg width="14" height="14" viewBox="0 0 24 24" fill="#fff"><path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/></svg>Start for free</a>'
      '<a href="mailto:support@hirelyzer.com" class="hl-btn-g" style="font-size:16px;padding:16px 32px"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" fill="none"/><polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>Contact us</a>'
      '</div>'
      '<div class="hl-checks">' + chk + '</div>'
      '</div></div>')

def render_footer():
    H('<footer style="background:#000">'
      '<div class="hl-footer">'
      '<div class="hl-footer-copy">&copy; 2025 HIRELYZER &middot; Intelligent Career Platform</div>'
      '<div class="hl-footer-links">'
      '<a href="#">Privacy</a>'
      '<a href="#">Terms</a>'
      '<a href="mailto:support@hirelyzer.com">support@hirelyzer.com</a>'
      '<a href="' + APP_URL + '" target="_blank">Open App &rarr;</a>'
      '</div></div></footer>')

def render_js():
    H('<script>'
      '(function(){'
      'var sp=document.getElementById("sp");'
      'function u(){if(!sp)return;var p=(window.scrollY/(document.documentElement.scrollHeight-window.innerHeight))*100;sp.style.width=Math.min(p,100)+"%";}'
      'window.addEventListener("scroll",u,{passive:true});'
      '})();'
      '</script>')

# ─── MAIN ─────────────────────────────────────────────────────────────────────
render_nav()
render_hero()
render_how()
render_story_ats()
render_story_bias()
render_story_builder()
render_story_career()
render_story_interview()
render_cta()
render_footer()
render_js()
