import streamlit as st
import math

st.set_page_config(
    page_title="HIRELYZER — Intelligent Career Platform",
    page_icon="⬡",
    layout="wide"
)

APP_URL = "https://hirelyzer-career-based-saas-platform-rxzkspoyrtwfamm5ztkmcf.streamlit.app/"

# ─────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────
def css(s): st.markdown(f"<style>{s}</style>", unsafe_allow_html=True)
def html(s): st.markdown(s, unsafe_allow_html=True)

# ─────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────
css("""
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root{
  --bg:#000;--bg1:#0a0a0a;--bg2:#111;--bg3:#161616;--surface:#1c1c1e;
  --b:rgba(255,255,255,0.08);--b2:rgba(255,255,255,0.14);
  --t:#f5f5f7;--m:rgba(245,245,247,0.56);--m2:rgba(245,245,247,0.36);
  --a:#0a84ff;--a2:#30d158;--a3:#ff9f0a;--a4:#bf5af2;
  --font:'Sora',-apple-system,'SF Pro Display',sans-serif;
  --mono:'JetBrains Mono',monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

html,body,[data-testid="stAppViewContainer"],[class*="css"]{
  background:var(--bg)!important;color:var(--t);
  font-family:var(--font);overflow-x:hidden;-webkit-font-smoothing:antialiased;
}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stSidebar"],footer{display:none!important}
[data-testid="stAppViewContainer"]>section{padding:0!important}
.block-container{padding:0!important;max-width:100%!important}

/* scroll bar */
#sp{position:fixed;top:0;left:0;height:2px;width:0%;background:var(--a);z-index:9999;transition:width .08s linear}

/* NAV */
.hl-nav{position:fixed;top:0;left:0;right:0;z-index:900;
  backdrop-filter:saturate(180%) blur(24px);-webkit-backdrop-filter:saturate(180%) blur(24px);
  background:rgba(0,0,0,0.78);border-bottom:1px solid var(--b);height:56px;
  display:flex;align-items:center;justify-content:center}
.hl-nav-inner{width:100%;max-width:1100px;display:flex;align-items:center;
  justify-content:space-between;padding:0 32px}
.hl-logo{display:flex;align-items:center;gap:10px;font-size:15px;font-weight:700;
  color:var(--t);text-decoration:none;letter-spacing:-.2px}
.hl-logo-mark{width:30px;height:30px;display:flex;align-items:center;justify-content:center;
  background:var(--a);border-radius:8px}
.hl-nav-links{display:flex;align-items:center;gap:28px}
.hl-nav-links a{font-size:13px;font-weight:500;color:var(--m);text-decoration:none;
  transition:color .2s;letter-spacing:-.1px}
.hl-nav-links a:hover{color:var(--t)}
.hl-nav-cta{display:flex;align-items:center;gap:8px;padding:8px 18px;border-radius:980px;
  background:var(--a);color:#fff;font-size:13px;font-weight:600;text-decoration:none;
  transition:opacity .2s,transform .15s}
.hl-nav-cta:hover{opacity:.86;transform:scale(.98)}

/* HERO */
.hl-hero{min-height:100vh;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;padding:120px 32px 80px;position:relative;overflow:hidden}
.hl-hero::before{content:'';position:absolute;top:-200px;left:50%;transform:translateX(-50%);
  width:800px;height:600px;
  background:radial-gradient(ellipse,rgba(10,132,255,.12) 0%,transparent 70%);pointer-events:none}
.hl-hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:200px;
  background:linear-gradient(to bottom,transparent,#000);pointer-events:none}
.hl-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:600;
  letter-spacing:1.4px;text-transform:uppercase;color:var(--a);margin-bottom:28px;
  padding:6px 14px;border-radius:980px;border:1px solid rgba(10,132,255,.3);
  background:rgba(10,132,255,.07);animation:fadeUp .7s ease both}
.hl-h1{font-size:clamp(42px,7vw,84px);font-weight:800;line-height:1.03;letter-spacing:-3px;
  color:var(--t);animation:fadeUp .7s .12s ease both;max-width:920px}
.hl-h1 em{font-style:normal;color:var(--a)}
.hl-hero-sub{font-size:clamp(16px,2vw,20px);color:var(--m);font-weight:400;line-height:1.6;
  letter-spacing:-.2px;max-width:580px;margin:24px auto 0;animation:fadeUp .7s .22s ease both}
.hl-hero-ctas{display:flex;gap:14px;justify-content:center;margin-top:44px;
  animation:fadeUp .7s .32s ease both;flex-wrap:wrap}
.hl-btn-p{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;border-radius:980px;
  background:var(--a);color:#fff;font-size:15px;font-weight:600;text-decoration:none;
  letter-spacing:-.2px;transition:opacity .2s,transform .15s}
.hl-btn-p:hover{opacity:.86;transform:translateY(-1px)}
.hl-btn-g{display:inline-flex;align-items:center;gap:8px;padding:14px 28px;border-radius:980px;
  background:var(--surface);color:var(--t);font-size:15px;font-weight:600;text-decoration:none;
  letter-spacing:-.2px;border:1px solid var(--b2);transition:background .2s,transform .15s}
.hl-btn-g:hover{background:#2c2c2e;transform:translateY(-1px)}

/* HERO CARD */
.hl-hero-card{margin-top:72px;width:100%;max-width:820px;background:var(--bg2);border-radius:22px;
  border:1px solid var(--b);overflow:hidden;animation:fadeUp .7s .45s ease both;
  box-shadow:0 40px 100px rgba(0,0,0,.6);position:relative;z-index:1}
.hl-card-bar{height:38px;background:var(--bg3);border-bottom:1px solid var(--b);
  display:flex;align-items:center;padding:0 16px;gap:8px}
.dot{width:12px;height:12px;border-radius:50%}
.hl-card-body{padding:28px}

/* STAT ROW */
.hl-stat-row{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;
  margin:28px 0 0;animation:fadeUp .7s .55s ease both}
.hl-stat{display:flex;flex-direction:column;align-items:center;padding:18px 28px;
  border-radius:16px;background:var(--bg2);border:1px solid var(--b);min-width:130px}
.hl-stat-n{font-size:26px;font-weight:800;color:var(--t);letter-spacing:-1px}
.hl-stat-l{font-size:11px;color:var(--m2);font-weight:500;margin-top:4px;
  text-transform:uppercase;letter-spacing:.8px}

/* SECTION LABEL */
.hl-section-label{font-size:11px;font-weight:600;letter-spacing:1.4px;text-transform:uppercase;
  color:var(--m2);display:flex;align-items:center;gap:16px;margin-bottom:72px}
.hl-section-label::before,.hl-section-label::after{content:'';flex:1;height:1px;background:var(--b)}

/* HOW IT WORKS */
.hl-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:2px}
.hl-step{padding:32px 24px;background:var(--bg2);border:1px solid var(--b);position:relative;overflow:hidden}
.hl-step:first-child{border-radius:20px 0 0 20px}
.hl-step:last-child{border-radius:0 20px 20px 0}
.hl-step-n{font-family:var(--mono);font-size:11px;font-weight:500;color:var(--m2);
  margin-bottom:16px;display:block}
.hl-step-icon{width:44px;height:44px;margin-bottom:16px}
.hl-step-title{font-size:15px;font-weight:700;color:var(--t);margin-bottom:8px;letter-spacing:-.3px}
.hl-step-desc{font-size:13px;color:var(--m);line-height:1.65}

/* STORY SECTIONS */
.hl-section{max-width:1100px;margin:0 auto;padding:0 32px}
.hl-story{padding:100px 0}
.hl-story-grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.hl-story-number{font-family:var(--mono);font-size:11px;font-weight:500;color:var(--m2);
  letter-spacing:1px;margin-bottom:20px}
.hl-story-heading{font-size:clamp(28px,4vw,44px);font-weight:800;letter-spacing:-1.5px;
  line-height:1.1;color:var(--t);margin-bottom:20px}
.hl-story-heading span{color:var(--a)}
.hl-story-body{font-size:16px;color:var(--m);line-height:1.75;font-weight:400;margin-bottom:20px}
.hl-pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.hl-pill{padding:6px 14px;border-radius:980px;font-size:12px;font-weight:600;
  border:1px solid var(--b);color:var(--m);background:var(--bg2)}

/* PANEL */
.hl-panel{background:var(--bg2);border-radius:20px;border:1px solid var(--b);
  padding:28px;overflow:hidden;position:relative}
.hl-panel-title{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:1px;
  color:var(--m2);margin-bottom:20px;display:flex;align-items:center;gap:8px}

/* BARS */
.hl-bar-item{margin-bottom:12px}
.hl-bar-label{display:flex;justify-content:space-between;font-size:12px;color:var(--m);
  margin-bottom:5px;font-weight:500}
.hl-bar-track{height:4px;background:rgba(255,255,255,0.07);border-radius:2px;overflow:hidden}
.hl-bar-fill{height:100%;border-radius:2px;transition:width 1.2s cubic-bezier(.4,0,.2,1)}

/* WORD CHIPS */
.hl-word-row{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:14px}
.wc{padding:5px 11px;border-radius:8px;font-size:12px;font-weight:600;font-family:var(--mono)}
.wc-m{background:rgba(10,132,255,.12);color:#4db3ff;border:1px solid rgba(10,132,255,.2)}
.wc-f{background:rgba(191,90,242,.12);color:#d07ef7;border:1px solid rgba(191,90,242,.2)}
.wc-n{background:rgba(48,209,88,.12);color:#4cd964;border:1px solid rgba(48,209,88,.2)}

/* TEMPLATE GALLERY */
.hl-tmpl-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px}
.hl-tmpl-thumb{border-radius:10px;border:1px solid var(--b);overflow:hidden;
  background:var(--bg3);position:relative;padding:10px;
  display:flex;flex-direction:column;gap:4px;min-height:90px}
.hl-tmpl-thumb.active{border-color:var(--a);box-shadow:0 0 0 2px rgba(10,132,255,.2)}
.tmpl-line-h{height:5px;border-radius:2px;background:var(--b2);width:70%}
.tmpl-line-s{height:3px;border-radius:1.5px;background:var(--b);width:90%}
.tmpl-line-s2{height:3px;border-radius:1.5px;background:var(--b);width:60%}
.tmpl-line-s3{height:3px;border-radius:1.5px;background:var(--b);width:75%}
.hl-tmpl-badge{position:absolute;bottom:6px;left:6px;right:6px;
  background:rgba(10,132,255,.15);border:1px solid rgba(10,132,255,.2);
  border-radius:5px;padding:3px 6px;font-size:9px;font-weight:700;
  color:var(--a);text-align:center;letter-spacing:.5px;text-transform:uppercase}

/* JOB CARDS */
.hl-job-card{padding:14px 16px;border-radius:12px;background:var(--bg3);
  border:1px solid var(--b);display:flex;align-items:center;gap:12px;
  margin-bottom:8px;transition:border-color .2s}
.hl-job-logo{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;
  justify-content:center;font-weight:800;font-size:13px;flex-shrink:0;font-family:var(--mono)}
.hl-job-meta{flex:1;min-width:0}
.hl-job-title{font-size:13px;font-weight:600;color:var(--t);white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.hl-job-co{font-size:11px;color:var(--m2);margin-top:2px}
.hl-job-badge{padding:3px 10px;border-radius:980px;font-size:11px;font-weight:600;white-space:nowrap}

/* RADAR */
.hl-radar-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center}

/* Q&A */
.hl-qa{margin-bottom:16px}
.hl-q{font-size:13px;font-weight:600;color:var(--t);margin-bottom:8px;display:flex;gap:8px;align-items:flex-start}
.hl-a{font-size:12px;color:var(--m);line-height:1.65;padding-left:24px}
.hl-score-badge{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;
  border-radius:980px;font-size:12px;font-weight:700;background:rgba(48,209,88,.12);
  color:var(--a2);border:1px solid rgba(48,209,88,.2)}

/* CTA BLOCK */
.hl-cta-block{margin:0 0 120px;padding:80px 48px;border-radius:28px;background:var(--bg2);
  border:1px solid var(--b);text-align:center;position:relative;overflow:hidden}
.hl-cta-block::before{content:'';position:absolute;top:-300px;left:50%;
  transform:translateX(-50%);width:600px;height:600px;
  background:radial-gradient(ellipse,rgba(10,132,255,.1) 0%,transparent 70%);pointer-events:none}
.hl-cta-heading{font-size:clamp(30px,5vw,52px);font-weight:800;letter-spacing:-2px;
  color:var(--t);line-height:1.07;max-width:640px;margin:0 auto 20px;position:relative;z-index:1}
.hl-cta-sub{font-size:17px;color:var(--m);margin-bottom:40px;position:relative;z-index:1}
.hl-check-row{display:flex;justify-content:center;gap:28px;flex-wrap:wrap;margin-top:36px}
.hl-check-item{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--m2)}

/* FOOTER */
.hl-footer{border-top:1px solid var(--b);padding:40px 32px;display:flex;
  justify-content:space-between;align-items:center;max-width:1100px;margin:0 auto;
  flex-wrap:wrap;gap:20px}
.hl-footer-links{display:flex;gap:24px}
.hl-footer-links a{font-size:13px;color:var(--m2);text-decoration:none;transition:color .2s}
.hl-footer-links a:hover{color:var(--t)}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

@media(max-width:860px){
  .hl-story-grid{grid-template-columns:1fr;gap:40px}
  .hl-steps{grid-template-columns:1fr 1fr}
  .hl-step:first-child{border-radius:20px 0 0 0}
  .hl-step:last-child{border-radius:0 0 20px 0}
  .hl-step:nth-child(2){border-radius:0 20px 0 0}
  .hl-step:nth-child(3){border-radius:0 0 0 20px}
  .hl-hero-ctas{flex-direction:column;align-items:center}
  .hl-nav-links{display:none}
  .hl-cta-block{padding:48px 24px}
  .hl-tmpl-grid{grid-template-columns:repeat(4,1fr)}
}
""")

# ─────────────────────────────────────────
# SVG HELPERS  (no f-string nesting issues)
# ─────────────────────────────────────────
def ats_ring(score=78):
    r = 38; c = 48; sw = 5
    circ = 2 * math.pi * r
    fill = (score / 100) * circ
    offset = circ * 0.25
    return (
        f'<svg width="96" height="96" viewBox="0 0 96 96" fill="none">'
        f'<circle cx="{c}" cy="{c}" r="{r}" stroke="rgba(255,255,255,0.06)" stroke-width="{sw}"/>'
        f'<circle cx="{c}" cy="{c}" r="{r}" stroke="url(#ag)" stroke-width="{sw}"'
        f' stroke-dasharray="{fill:.1f} {circ:.1f}" stroke-dashoffset="{offset:.1f}"'
        f' stroke-linecap="round"/>'
        f'<defs><linearGradient id="ag" x1="0" y1="0" x2="96" y2="96" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0%" stop-color="#30d158"/><stop offset="100%" stop-color="#0a84ff"/>'
        f'</linearGradient></defs></svg>'
    )

def radar_svg():
    cats   = ["Communication","Technical","Confidence","Structure","Examples"]
    scores = [0.82, 0.74, 0.88, 0.70, 0.78]
    cx = cy = 95; R = 65; n = len(cats)
    def pt(i, frac):
        angle = math.pi/2 + 2*math.pi*i/n
        return cx + R*frac*math.cos(angle), cy - R*frac*math.sin(angle)
    grid = "".join(
        '<polygon points="' +
        " ".join(f"{pt(i,lv)[0]:.1f},{pt(i,lv)[1]:.1f}" for i in range(n)) +
        '" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>'
        for lv in [0.25,0.5,0.75,1.0]
    )
    axes = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{pt(i,1)[0]:.1f}" y2="{pt(i,1)[1]:.1f}" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>'
        for i in range(n)
    )
    poly = " ".join(f"{pt(i,scores[i])[0]:.1f},{pt(i,scores[i])[1]:.1f}" for i in range(n))
    dots = "".join(
        f'<circle cx="{pt(i,scores[i])[0]:.1f}" cy="{pt(i,scores[i])[1]:.1f}" r="3" fill="#0a84ff"/>'
        for i in range(n)
    )
    labels = "".join(
        f'<text x="{pt(i,1.26)[0]:.1f}" y="{pt(i,1.26)[1]:.1f}" text-anchor="middle"'
        f' dominant-baseline="middle" fill="rgba(245,245,247,0.4)" font-size="8"'
        f' font-family="Sora,sans-serif" font-weight="500">{cats[i]}</text>'
        for i in range(n)
    )
    return (
        f'<svg width="190" height="190" viewBox="0 0 190 190" fill="none">'
        f'{grid}{axes}'
        f'<polygon points="{poly}" fill="rgba(10,132,255,0.15)" stroke="#0a84ff" stroke-width="1.5"/>'
        f'{dots}{labels}</svg>'
    )

# ─────────────────────────────────────────
# PRE-BUILD HTML FRAGMENTS
# ─────────────────────────────────────────

# ── ATS bars ──
bars_data = [
    ("Format & Layout",    92, "#30d158"),
    ("Keyword Coverage",   71, "#ff9f0a"),
    ("Sections Present",   85, "#0a84ff"),
    ("Action Verbs",       68, "#ff9f0a"),
    ("Contact Info",      100, "#30d158"),
    ("Date Consistency",   80, "#0a84ff"),
]
ats_bars = ""
for label, pct, col in bars_data:
    ats_bars += (
        f'<div class="hl-bar-item">'
        f'<div class="hl-bar-label"><span>{label}</span>'
        f'<span style="color:{col}">{pct}%</span></div>'
        f'<div class="hl-bar-track">'
        f'<div class="hl-bar-fill" style="width:{pct}%;background:{col}"></div>'
        f'</div></div>'
    )

# ── interview score breakdown ──
score_dims = [
    ("Communication", "85%", "#0a84ff"),
    ("Technical",     "79%", "#bf5af2"),
    ("Confidence",    "88%", "#30d158"),
    ("Structure",     "74%", "#ff9f0a"),
]
score_bars = ""
for dim, sc, col in score_dims:
    score_bars += (
        f'<div style="display:flex;justify-content:space-between;font-size:11px;'
        f'color:var(--m);margin-bottom:5px">'
        f'<span>{dim}</span><span style="color:{col};font-weight:600">{sc}</span></div>'
        f'<div style="height:3px;background:rgba(255,255,255,0.07);border-radius:2px;'
        f'margin-bottom:8px;overflow:hidden">'
        f'<div style="width:{sc};height:100%;background:{col};border-radius:2px"></div></div>'
    )

# ── template gallery ──
template_names = [
    "Modern","Minimal","Executive","Timeline",
    "Corporate","Creative","Navy","Teal",
]
accent_bars = ["#0a84ff","#f5f5f7","#ff9f0a","#30d158","#1d4ed8","#bf5af2","#172554","#0d9488"]
tmpl_html = ""
for i, (name, bar_col) in enumerate(zip(template_names, accent_bars)):
    active = "active" if i == 0 else ""
    badge  = f'<div class="hl-tmpl-badge">{name}</div>' if i == 0 else ""
    tmpl_html += (
        f'<div class="hl-tmpl-thumb {active}">'
        f'<div class="tmpl-line-h" style="background:{bar_col};opacity:0.9"></div>'
        f'<div class="tmpl-line-s"></div>'
        f'<div class="tmpl-line-s2"></div>'
        f'<div class="tmpl-line-s3"></div>'
        f'<div class="tmpl-line-s"></div>'
        f'<div class="tmpl-line-s2"></div>'
        f'{badge}</div>'
    )

# ── job cards ──
jobs = [
    ("SDE II",        "Google",   "Mountain View · Full-time", "#4285f4", "G", True),
    ("ML Engineer",   "Anthropic","Remote · Full-time",        "#d97706", "A", False),
    ("Backend Dev",   "Razorpay", "Bangalore · Full-time",     "#2563eb", "R", False),
    ("Data Analyst",  "Zepto",    "Mumbai · Hybrid",           "#7c3aed", "Z", False),
]
job_cards_html = ""
for title, co, meta, col, letter, featured in jobs:
    bb  = "rgba(10,132,255,0.12)" if featured else "rgba(255,255,255,0.05)"
    bc  = "#4db3ff"  if featured else "rgba(245,245,247,0.3)"
    btx = "Featured" if featured else "New"
    job_cards_html += (
        f'<div class="hl-job-card">'
        f'<div class="hl-job-logo" style="background:{col}22;color:{col}">{letter}</div>'
        f'<div class="hl-job-meta">'
        f'<div class="hl-job-title">{title} — {co}</div>'
        f'<div class="hl-job-co">{meta}</div>'
        f'</div>'
        f'<div class="hl-job-badge" style="background:{bb};color:{bc};border:1px solid {bc}40">{btx}</div>'
        f'</div>'
    )

# ── check list items ──
check_items = [
    "ATS score in seconds","Bias detection & rewrite","15 resume templates",
    "Cover letter generator","Live job search","AI Interview Coach",
]
check_icon = (
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none">'
    '<path d="M5 12l5 5L19 7" stroke="#30d158" stroke-width="2.2" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)
check_row_html = "".join(
    f'<div class="hl-check-item">{check_icon}<span>{item}</span></div>'
    for item in check_items
)

# ─────────────────────────────────────────
# NAV
# ─────────────────────────────────────────
html(f"""
<div id="sp"></div>
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
      <svg width="13" height="13" viewBox="0 0 24 24" fill="#fff">
        <path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/>
      </svg>
      Open App
    </a>
  </div>
</div>
""")

# ─────────────────────────────────────────
# HERO
# ─────────────────────────────────────────
html(f"""
<div class="hl-hero">
  <div class="hl-eyebrow">
    <svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>
    AI-Powered Career Intelligence
  </div>
  <h1 class="hl-h1">The last resume tool<br>you&rsquo;ll ever <em>need</em></h1>
  <p class="hl-hero-sub">
    Upload your resume. Hirelyzer instantly scores it for ATS compatibility,
    detects bias, rewrites it with AI, and connects you to jobs — all in one place.
  </p>
  <div class="hl-hero-ctas">
    <a href="{APP_URL}" target="_blank" class="hl-btn-p">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="#fff">
        <path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/>
      </svg>
      Get Started Free
    </a>
    <a href="#how" class="hl-btn-g">
      See how it works
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none">
        <path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="1.8"
          stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </a>
  </div>

  <!-- HERO CARD -->
  <div class="hl-hero-card">
    <div class="hl-card-bar">
      <div class="dot" style="background:#ff5f57"></div>
      <div class="dot" style="background:#febc2e"></div>
      <div class="dot" style="background:#28c840"></div>
      <span style="margin-left:8px;font-size:11px;color:var(--m2);font-family:var(--mono)">
        hirelyzer — resume_analysis.pdf
      </span>
    </div>
    <div class="hl-card-body">
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px">

        <!-- col 1: ATS -->
        <div>
          <div class="hl-panel-title">
            <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#30d158"/></svg>
            ATS Score
          </div>
          <div style="display:flex;align-items:center;gap:16px;margin-bottom:20px">
            {ats_ring(78)}
            <div>
              <div style="font-size:10px;color:var(--m2);text-transform:uppercase;letter-spacing:.8px;font-weight:600;margin-bottom:4px">Overall</div>
              <div style="font-size:36px;font-weight:800;color:var(--t);letter-spacing:-2px;line-height:1">78</div>
              <div style="font-size:11px;color:#30d158;font-weight:600;margin-top:4px">Good · Minor fixes</div>
            </div>
          </div>
          {ats_bars}
        </div>

        <!-- col 2: bias -->
        <div>
          <div class="hl-panel-title">
            <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#bf5af2"/></svg>
            Bias Analysis
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:14px">
            <div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:4px">Masculine</div>
              <div style="font-size:22px;font-weight:800;color:#4db3ff">8</div>
              <div style="font-size:10px;color:var(--m2)">flagged</div>
            </div>
            <div style="padding:12px;background:rgba(191,90,242,0.06);border-radius:10px;border:1px solid rgba(191,90,242,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:4px">Feminine</div>
              <div style="font-size:22px;font-weight:800;color:#d07ef7">3</div>
              <div style="font-size:10px;color:var(--m2)">flagged</div>
            </div>
          </div>
          <div class="hl-word-row">
            <span class="wc wc-m">driven</span>
            <span class="wc wc-m">dominate</span>
            <span class="wc wc-f">nurture</span>
            <span class="wc wc-m">aggressive</span>
            <span class="wc wc-n">deliver</span>
            <span class="wc wc-n">execute</span>
          </div>
          <div style="padding:10px 12px;background:rgba(48,209,88,0.06);border-radius:10px;border:1px solid rgba(48,209,88,0.16)">
            <div style="font-size:11px;font-weight:700;color:#30d158;margin-bottom:4px">AI Rewrite Applied</div>
            <div style="font-size:11px;color:var(--m);line-height:1.6">
              <span style="text-decoration:line-through;opacity:.45">Aggressively drove</span>
              &rarr; <span style="color:#30d158">Accelerated</span> delivery across 3 teams
            </div>
          </div>
        </div>

        <!-- col 3: quick actions -->
        <div>
          <div class="hl-panel-title">
            <svg width="10" height="10" viewBox="0 0 10 10"><circle cx="5" cy="5" r="5" fill="#ff9f0a"/></svg>
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
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="#ff9f0a" stroke-width="1.8" stroke-linecap="round" fill="none"/></svg>
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
  <div class="hl-stat-row">
    <div class="hl-stat"><div class="hl-stat-n">15+</div><div class="hl-stat-l">Templates</div></div>
    <div class="hl-stat"><div class="hl-stat-n">5</div><div class="hl-stat-l">Core Modules</div></div>
    <div class="hl-stat"><div class="hl-stat-n">AI</div><div class="hl-stat-l">LLM Powered</div></div>
    <div class="hl-stat"><div class="hl-stat-n">Free</div><div class="hl-stat-l">No Credit Card</div></div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# HOW IT WORKS
# ─────────────────────────────────────────
html(f"""
<div id="how" style="padding:100px 0 60px">
  <div class="hl-section">
    <div class="hl-section-label">How it works</div>
    <div class="hl-steps">

      <div class="hl-step">
        <span class="hl-step-n">01</span>
        <svg class="hl-step-icon" viewBox="0 0 44 44" fill="none">
          <rect width="44" height="44" rx="12" fill="rgba(10,132,255,0.1)"/>
          <path d="M22 28V20M22 20L19 23M22 20L25 23" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M15 30h14" stroke="#0a84ff" stroke-width="1.6" stroke-linecap="round"/>
          <rect x="14" y="13" width="16" height="19" rx="3" stroke="#0a84ff" stroke-width="1.4" stroke-dasharray="3 2" fill="none"/>
        </svg>
        <div class="hl-step-title">Upload your resume</div>
        <div class="hl-step-desc">Drop any PDF. Our parser handles messy formats, multi-column layouts, and scanned documents via OCR fallback.</div>
      </div>

      <div class="hl-step">
        <span class="hl-step-n">02</span>
        <svg class="hl-step-icon" viewBox="0 0 44 44" fill="none">
          <rect width="44" height="44" rx="12" fill="rgba(48,209,88,0.1)"/>
          <circle cx="20" cy="20" r="7" stroke="#30d158" stroke-width="1.5" fill="none"/>
          <path d="M20 17v3l2 1.5" stroke="#30d158" stroke-width="1.5" stroke-linecap="round"/>
          <path d="M25.2 25.2l3.5 3.5" stroke="#30d158" stroke-width="1.7" stroke-linecap="round"/>
        </svg>
        <div class="hl-step-title">Instant AI analysis</div>
        <div class="hl-step-desc">ATS scoring, bias detection, grammar check, keyword matching — all computed in seconds with detailed feedback.</div>
      </div>

      <div class="hl-step">
        <span class="hl-step-n">03</span>
        <svg class="hl-step-icon" viewBox="0 0 44 44" fill="none">
          <rect width="44" height="44" rx="12" fill="rgba(191,90,242,0.1)"/>
          <rect x="12" y="11" width="13" height="18" rx="2.5" stroke="#bf5af2" stroke-width="1.5" fill="none"/>
          <rect x="19" y="16" width="14" height="18" rx="2.5" fill="rgba(191,90,242,0.1)" stroke="#bf5af2" stroke-width="1.5"/>
          <path d="M22 21h8M22 24.5h8M22 28h5" stroke="#bf5af2" stroke-width="1.3" stroke-linecap="round"/>
          <circle cx="32" cy="13" r="4" fill="#bf5af2"/>
          <path d="M30.5 13l1 1 2-2" stroke="#fff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <div class="hl-step-title">Build or rewrite</div>
        <div class="hl-step-desc">Use the AI rewriter or open the full Resume Builder. Choose from 15 templates, generate a cover letter, export to PDF or DOCX.</div>
      </div>

      <div class="hl-step">
        <span class="hl-step-n">04</span>
        <svg class="hl-step-icon" viewBox="0 0 44 44" fill="none">
          <rect width="44" height="44" rx="12" fill="rgba(255,159,10,0.1)"/>
          <path d="M22 28c-3.31 0-6-2.69-6-6 0-4 3-8 6-9 3 1 6 5 6 9 0 3.31-2.69 6-6 6z" stroke="#ff9f0a" stroke-width="1.5" fill="none"/>
          <circle cx="22" cy="22" r="2" fill="#ff9f0a"/>
          <path d="M29 13l-2 2M15 13l2 2" stroke="#ff9f0a" stroke-width="1.4" stroke-linecap="round"/>
        </svg>
        <div class="hl-step-title">Apply with confidence</div>
        <div class="hl-step-desc">Discover live job listings, salary benchmarks, curated courses, and practice with the AI Interview Coach before applying.</div>
      </div>

    </div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# STORY 1 — ATS ANALYZER
# ─────────────────────────────────────────
html(f"""
<div id="analyzer" class="hl-story">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div>
        <div class="hl-story-number">Feature 01 &mdash; Resume Analyzer</div>
        <h2 class="hl-story-heading">Your resume, <span>scored like a machine</span> reads it</h2>
        <p class="hl-story-body">
          Most resumes never reach a human. Applicant Tracking Systems silently filter them out on
          format, missing keywords, or structural issues. Hirelyzer&rsquo;s analyzer replicates
          exactly how ATS parsers &mdash; Workday, Greenhouse, Lever &mdash; evaluate your document.
        </p>
        <p class="hl-story-body">
          Every section, every bullet, every date format is weighed against real hiring criteria.
          You see a precise score, a list of passes and failures, and an AI-written action plan
          to close the gap.
        </p>
        <div class="hl-pills">
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
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
              <rect x="3" y="2" width="14" height="18" rx="2.5" stroke="#0a84ff" stroke-width="1.5"/>
              <path d="M7 7h7M7 11h7M7 15h4" stroke="#0a84ff" stroke-width="1.5" stroke-linecap="round"/>
              <circle cx="17" cy="17" r="4" fill="none" stroke="#30d158" stroke-width="1.4"/>
              <path d="M20 20l2.5 2.5" stroke="#30d158" stroke-width="1.6" stroke-linecap="round"/>
            </svg>
            Live ATS Breakdown
          </div>
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:24px">
            {ats_ring(78)}
            <div>
              <div style="font-size:10px;color:var(--m2);text-transform:uppercase;letter-spacing:.8px;font-weight:600;margin-bottom:4px">Overall</div>
              <div style="font-size:38px;font-weight:800;color:var(--t);letter-spacing:-2px;line-height:1">78</div>
              <div style="font-size:12px;color:#30d158;font-weight:600;margin-top:4px">Good &middot; Minor fixes needed</div>
            </div>
          </div>
          {ats_bars}
        </div>
      </div>
    </div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# STORY 2 — BIAS DETECTION
# ─────────────────────────────────────────
html(f"""
<div class="hl-story" style="background:var(--bg1)">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div style="order:2">
        <div class="hl-story-number">Feature 02 &mdash; Bias Detection</div>
        <h2 class="hl-story-heading">Language that <span>closes doors</span> &mdash; detected and replaced</h2>
        <p class="hl-story-body">
          Decades of research show that gendered language in resumes affects hiring outcomes.
          Words coded as &ldquo;masculine&rdquo; or &ldquo;feminine&rdquo; unconsciously signal
          culture fit to recruiters &mdash; and the wrong signals filter you out before the first call.
        </p>
        <p class="hl-story-body">
          Hirelyzer identifies every biased word, scores your overall language balance,
          and rewrites your resume with neutral, high-impact alternatives using a curated
          replacement lexicon built from real hiring data.
        </p>
        <div class="hl-pills">
          <span class="hl-pill">Gender-coded word detection</span>
          <span class="hl-pill">Bias score 0&ndash;100</span>
          <span class="hl-pill">LLM rewrite</span>
          <span class="hl-pill">Highlighted diff</span>
          <span class="hl-pill">Side-by-side compare</span>
        </div>
      </div>
      <div style="order:1">
        <div class="hl-panel">
          <div class="hl-panel-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="9" stroke="#bf5af2" stroke-width="1.5"/>
              <path d="M9 9h2.5a1.5 1.5 0 010 3H9m0-3v6m0-6h3" stroke="#bf5af2" stroke-width="1.4" stroke-linecap="round"/>
            </svg>
            Bias Detection Report
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:18px">
            <div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:5px">Masculine</div>
              <div style="font-size:26px;font-weight:800;color:#4db3ff">8</div>
              <div style="font-size:11px;color:var(--m2)">words flagged</div>
            </div>
            <div style="padding:14px;background:rgba(191,90,242,0.06);border-radius:12px;border:1px solid rgba(191,90,242,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:5px">Feminine</div>
              <div style="font-size:26px;font-weight:800;color:#d07ef7">3</div>
              <div style="font-size:11px;color:var(--m2)">words flagged</div>
            </div>
          </div>
          <div style="font-size:10px;color:var(--m2);font-weight:600;text-transform:uppercase;letter-spacing:.8px;margin-bottom:10px">Detected language</div>
          <div class="hl-word-row">
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
          <div style="padding:14px;background:rgba(48,209,88,0.06);border-radius:12px;border:1px solid rgba(48,209,88,0.16)">
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

# ─────────────────────────────────────────
# STORY 3 — RESUME BUILDER
# ─────────────────────────────────────────
html(f"""
<div id="builder" class="hl-story">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div>
        <div class="hl-story-number">Feature 03 &mdash; Resume Builder</div>
        <h2 class="hl-story-heading">Build resumes that <span>look as good</span> as they parse</h2>
        <p class="hl-story-body">
          Fifteen ATS-optimised templates &mdash; from understated minimal to executive prestige &mdash;
          all built on strict single-column structures that parse correctly in every major
          hiring platform. Choose a style, fill your details, and our AI enhances every
          section with no-repetition language rules enforced across the entire document.
        </p>
        <p class="hl-story-body">
          Export to DOCX (three ATS compliance levels) or PDF. Need a cover letter?
          One click generates a tailored letter for your target company, formatted and
          ready to send.
        </p>
        <div class="hl-pills">
          <span class="hl-pill">15 Templates</span>
          <span class="hl-pill">DOCX + PDF Export</span>
          <span class="hl-pill">AI Cover Letter</span>
          <span class="hl-pill">Live Preview</span>
          <span class="hl-pill">ATS Single-Column</span>
        </div>
      </div>
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
              <rect x="3" y="3" width="10" height="14" rx="2" stroke="#30d158" stroke-width="1.5"/>
              <rect x="11" y="7" width="10" height="14" rx="2" fill="rgba(48,209,88,.1)" stroke="#30d158" stroke-width="1.5"/>
              <path d="M14 11h5M14 14h5M14 17h3" stroke="#30d158" stroke-width="1.3" stroke-linecap="round"/>
            </svg>
            Template Gallery &mdash; 15 Designs
          </div>
          <div class="hl-tmpl-grid">
            {tmpl_html}
          </div>
          <div style="padding:14px;background:rgba(10,132,255,0.06);border-radius:12px;border:1px solid rgba(10,132,255,0.16);display:flex;align-items:center;justify-content:space-between">
            <div>
              <div style="font-size:12px;font-weight:700;color:var(--a)">Modern &mdash; ATS Certified</div>
              <div style="font-size:11px;color:var(--m2);margin-top:2px">Sora &middot; Navy headings &middot; Single-column</div>
            </div>
            <a href="{APP_URL}" target="_blank" style="padding:8px 16px;background:var(--a);color:#fff;border-radius:980px;font-size:12px;font-weight:600;text-decoration:none;white-space:nowrap">Use this</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# STORY 4 — JOB SEARCH
# ─────────────────────────────────────────
html(f"""
<div id="career" class="hl-story" style="background:var(--bg1)">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div style="order:2">
        <div class="hl-story-number">Feature 04 &mdash; Career Intelligence</div>
        <h2 class="hl-story-heading">Jobs, salaries, courses &mdash; <span>one place</span></h2>
        <p class="hl-story-body">
          The Job Search Hub pulls live listings from LinkedIn, Naukri, Foundit, Indeed,
          and Glassdoor &mdash; or uses the JSearch/RapidAPI engine for direct listings with
          remote and employment-type filters. Every search is role-aware and location-smart.
        </p>
        <p class="hl-story-body">
          Alongside jobs, Hirelyzer surfaces salary benchmarks by role and market,
          curated course recommendations mapped to real skill gaps in your resume,
          and resume &amp; interview preparation videos &mdash; all linked to your career profile.
        </p>
        <div class="hl-pills">
          <span class="hl-pill">Live Job Listings</span>
          <span class="hl-pill">Salary Benchmarks</span>
          <span class="hl-pill">Course Recommendations</span>
          <span class="hl-pill">Skills Radar</span>
          <span class="hl-pill">Remote Filter</span>
        </div>
      </div>
      <div style="order:1">
        <div class="hl-panel">
          <div class="hl-panel-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
              <rect x="2" y="7" width="20" height="14" rx="2" stroke="#ff9f0a" stroke-width="1.5"/>
              <path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2" stroke="#ff9f0a" stroke-width="1.5"/>
              <path d="M2 13h20" stroke="#ff9f0a" stroke-width="1.3" stroke-linecap="round"/>
            </svg>
            Job Search Hub
          </div>
          {job_cards_html}
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:4px">
            <div style="padding:12px;background:rgba(255,159,10,0.06);border-radius:10px;border:1px solid rgba(255,159,10,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:5px">Avg Salary</div>
              <div style="font-size:20px;font-weight:800;color:#ff9f0a">&#8377;18&ndash;32 LPA</div>
              <div style="font-size:11px;color:var(--m2)">Backend &middot; India</div>
            </div>
            <div style="padding:12px;background:rgba(10,132,255,0.06);border-radius:10px;border:1px solid rgba(10,132,255,0.15)">
              <div style="font-size:9px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:5px">Platforms</div>
              <div style="font-size:13px;font-weight:700;color:var(--t);line-height:1.7">LinkedIn &middot; Naukri<br>Foundit &middot; Indeed</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# STORY 5 — AI INTERVIEW COACH
# ─────────────────────────────────────────
html(f"""
<div class="hl-story">
  <div class="hl-section">
    <div class="hl-story-grid">
      <div>
        <div class="hl-story-number">Feature 05 &mdash; AI Interview Coach</div>
        <h2 class="hl-story-heading">Practice until <span>every answer</span> lands</h2>
        <p class="hl-story-body">
          Upload your resume and Hirelyzer generates interview questions derived directly
          from your actual experience &mdash; not generic prompts. Answer in free text;
          the AI coach scores you on communication, technical depth, confidence signals,
          structure, and use of concrete examples.
        </p>
        <p class="hl-story-body">
          Every session ends with a performance radar chart, a detailed Q&amp;A review,
          and course recommendations tied to your weakest dimensions. Your progress
          is tracked across sessions in My Progress dashboard.
        </p>
        <div class="hl-pills">
          <span class="hl-pill">Resume-based Questions</span>
          <span class="hl-pill">Real-time AI Scoring</span>
          <span class="hl-pill">Radar Chart</span>
          <span class="hl-pill">Session History</span>
          <span class="hl-pill">Downloadable Report</span>
        </div>
      </div>
      <div>
        <div class="hl-panel">
          <div class="hl-panel-title" style="justify-content:space-between">
            <div style="display:flex;align-items:center;gap:8px">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="#ff453a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
              </svg>
              Mock Interview &middot; Session 3
            </div>
            <div class="hl-score-badge">
              <svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#30d158"/></svg>
              82 / 100
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start">
            <div>
              <div class="hl-qa">
                <div class="hl-q">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px">
                    <circle cx="12" cy="12" r="10" stroke="#0a84ff" stroke-width="1.5"/>
                    <path d="M12 16v-4M12 8h.01" stroke="#0a84ff" stroke-width="1.8" stroke-linecap="round"/>
                  </svg>
                  Describe your most complex backend system.
                </div>
                <div class="hl-a">Built a multi-tenant microservices platform handling 2M events/day using Kafka, Redis, and PostgreSQL with 40% lower P99 latency.</div>
              </div>
              <div class="hl-qa">
                <div class="hl-q">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="flex-shrink:0;margin-top:1px">
                    <circle cx="12" cy="12" r="10" stroke="#bf5af2" stroke-width="1.5"/>
                    <path d="M12 16v-4M12 8h.01" stroke="#bf5af2" stroke-width="1.8" stroke-linecap="round"/>
                  </svg>
                  How do you handle technical debt?
                </div>
                <div class="hl-a">I prioritise tech debt as a first-class roadmap item, quantifying velocity cost before pitching refactors to stakeholders.</div>
              </div>
              <div style="margin-top:14px">
                <div style="font-size:10px;text-transform:uppercase;letter-spacing:.8px;color:var(--m2);font-weight:600;margin-bottom:8px">Score breakdown</div>
                {score_bars}
              </div>
            </div>
            <div class="hl-radar-wrap">
              {radar_svg()}
              <div style="font-size:11px;color:var(--m2);margin-top:6px;text-align:center">Performance radar</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# FINAL CTA
# ─────────────────────────────────────────
html(f"""
<div class="hl-section">
  <div id="contact" class="hl-cta-block">
    <div class="hl-eyebrow" style="margin:0 auto 28px">
      <svg width="8" height="8" viewBox="0 0 8 8"><circle cx="4" cy="4" r="4" fill="#0a84ff"/></svg>
      Free to use &middot; No credit card required
    </div>
    <div class="hl-cta-heading">Your next job starts with a better resume</div>
    <p class="hl-cta-sub">Join professionals already using Hirelyzer to pass ATS filters, remove bias, and land more interviews.</p>
    <div style="display:flex;gap:14px;justify-content:center;position:relative;z-index:1;flex-wrap:wrap">
      <a href="{APP_URL}" target="_blank" class="hl-btn-p" style="font-size:16px;padding:16px 36px">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="#fff">
          <path d="M12 2L13.8 8.2L20 10L13.8 11.8L12 18L10.2 11.8L4 10L10.2 8.2L12 2Z"/>
        </svg>
        Start for free
      </a>
      <a href="mailto:support@hirelyzer.com" class="hl-btn-g" style="font-size:16px;padding:16px 32px">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" stroke-width="1.5" fill="none"/>
          <polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="1.5" fill="none"/>
        </svg>
        Contact us
      </a>
    </div>
    <div class="hl-check-row">
      {check_row_html}
    </div>
  </div>
</div>
""")

# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
html(f"""
<footer>
  <div class="hl-footer">
    <div style="font-size:14px;font-weight:600;color:var(--m)">&copy; 2025 HIRELYZER &middot; Intelligent Career Platform</div>
    <div class="hl-footer-links">
      <a href="#">Privacy</a>
      <a href="#">Terms</a>
      <a href="mailto:support@hirelyzer.com">support@hirelyzer.com</a>
      <a href="{APP_URL}" target="_blank">Open App &rarr;</a>
    </div>
  </div>
</footer>
""")

# ─────────────────────────────────────────
# JS
# ─────────────────────────────────────────
html("""
<script>
(function(){
  var sp = document.getElementById('sp');
  if(sp){
    window.addEventListener('scroll',function(){
      var pct=(window.scrollY/(document.documentElement.scrollHeight-window.innerHeight))*100;
      sp.style.width=pct+'%';
    },{passive:true});
  }
})();
</script>
""")
