import streamlit as st
import base64
from textwrap import dedent

st.set_page_config(page_title="HIRELYZER — Cinematic Landing", page_icon="🚀", layout="wide")

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
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-10px) rotate(1deg); }
  66% { transform: translateY(5px) rotate(-1deg); }
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: var(--card-shadow), var(--glow); }
  50% { box-shadow: var(--card-shadow), 0 0 60px rgba(79,70,229,0.4); }
}

@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes scale-in {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
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
}

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
}

.hero::before {
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
}

.btn:hover{
  background:var(--accent-hover);
  transform: translateY(-2px) scale(1.02);
  box-shadow:0 16px 32px rgba(79,70,229,0.35), 0 8px 16px rgba(0,0,0,0.2);
}

.btn:active{
  transform: translateY(0) scale(0.98);
}

.btn.secondary{
  background:transparent;
  border:2px solid rgba(255,255,255,0.1);
  color:white;
  backdrop-filter: blur(10px);
}

.btn.secondary:hover{
  background:rgba(255,255,255,0.05);
  border-color: rgba(255,255,255,0.2);
  transform: translateY(-2px) scale(1.02);
}

.features{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:24px;
  margin-top:32px;
}

.feature-card{
  padding:28px;
  border-radius:20px;
  background:linear-gradient(135deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
  backdrop-filter: blur(20px);
  border:1px solid rgba(255,255,255,0.06);
  box-shadow: 0 8px 32px rgba(0,0,0,0.3);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  animation: scale-in 0.6s ease-out;
}

.feature-card:hover{
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 60px rgba(0,0,0,0.4), 0 0 40px rgba(79,70,229,0.2);
  border-color: rgba(255,255,255,0.12);
}

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
}

.feature-card:hover::before {
  transform: scaleX(1);
}

.feature-title{
  font-weight:800;
  margin-top:12px;
  font-size:18px;
  color: rgba(255,255,255,0.95);
}

.feature-desc{
  color:rgba(255,255,255,0.7);
  font-size:15px;
  margin-top:8px;
  line-height: 1.6;
}

.footer{
  padding:32px 16px;
  margin-top:32px;
  color:rgba(255,255,255,0.6);
  text-align: center;
  border-top: 1px solid rgba(255,255,255,0.05);
}

.nav-container {
  backdrop-filter: blur(20px);
  background: rgba(5,8,22,0.8);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  position: sticky;
  top: 0;
  z-index: 100;
  animation: slide-up 0.6s ease-out;
}

.nav-link {
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: rgba(255,255,255,0.95) !important;
  transform: translateY(-1px);
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
}

.nav-link:hover::after {
  width: 100%;
}

.logo-container {
  transition: all 0.3s ease;
}

.logo-container:hover {
  transform: scale(1.05);
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
}

.ats-preview:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow:0 30px 100px rgba(0,0,0,0.8), 0 0 60px rgba(79,70,229,0.2);
}

.skill-tag {
  transition: all 0.3s ease;
}

.skill-tag:hover {
  background: rgba(79,70,229,0.3) !important;
  transform: scale(1.05);
}

.section-title {
  background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: slide-up 0.8s ease-out;
}

.pricing-card-featured {
  position: relative;
  overflow: hidden;
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
}

@media (max-width: 900px){
  .hero{flex-direction:column; padding: 40px 20px;}
  .hero-right{width: 100%; min-width: auto;}
  .features{grid-template-columns:repeat(1,1fr)}
  .h-title{font-size:40px}
  .cta-row{flex-direction: column; align-items: center;}
  .btn{width: 100%; text-align: center;}
}

@media (max-width: 600px){
  .h-title{font-size:32px}
  .hero{padding: 30px 16px;}
  .feature-card{padding: 20px;}
}

.typewriter{
  display:inline-block;
  overflow:hidden;
  white-space:nowrap;
}

.typewriter-text{
  border-right:3px solid rgba(255,255,255,0.7);
  padding-right:8px;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { border-color: rgba(255,255,255,0.7); }
  51%, 100% { border-color: transparent; }
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
}

.parallax-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
}

.floating-element {
  position: absolute;
  opacity: 0.1;
  animation: float 10s ease-in-out infinite;
}

.floating-element:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
.floating-element:nth-child(2) { top: 20%; right: 10%; animation-delay: 2s; }
.floating-element:nth-child(3) { bottom: 30%; left: 20%; animation-delay: 4s; }
.floating-element:nth-child(4) { bottom: 10%; right: 20%; animation-delay: 6s; }
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
</div>
""", unsafe_allow_html=True)

# ---------------------- Enhanced Top Nav ----------------------
st.markdown("""
<div class='nav-container'>
<div style='display:flex;justify-content:space-between;align-items:center;padding:16px 24px;max-width:1200px;margin:0 auto;'>
  <div style='display:flex;align-items:center;gap:16px' class='logo-container'>
    <div style='width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,#ff6a88,#5f2c82);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:20px;box-shadow:0 8px 20px rgba(79,70,229,0.3)'>HL</div>
    <div style='font-weight:800;font-size:18px'>HIRELYZER</div>
  </div>
  <div style='display:flex;gap:32px;align-items:center'>
    <a href='#features' class='nav-link' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600;font-size:15px'>Features</a>
    <a href='#pricing' class='nav-link' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600;font-size:15px'>Pricing</a>
    <a href='#contact' class='nav-link' style='text-decoration:none;color:rgba(255,255,255,0.75);font-weight:600;font-size:15px'>Contact</a>
    <a href="https://hirelyzer-ch2pihnds3cktdxkvu84er.streamlit.app/" target="_blank" class='btn' style='text-decoration:none'>
      🚀 Open App
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
      <a href="https://hirelyzer-ch2pihnds3cktdxkvu84er.streamlit.app/" target="_blank" class='btn'>
        ✨ Launch App
      </a>
      <a href='#pricing' class='btn secondary'>
        💎 View Plans
      </a>
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
        </div>
        <div style='display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-top:1px solid rgba(255,255,255,0.05)'>
          <div style='font-size:13px;color:rgba(255,255,255,0.7)'>🎯 ATS Score</div>
          <div style='font-weight:900;font-size:24px;background:linear-gradient(135deg,#10b981,#3b82f6);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent'>78%</div>
        </div>
        <div style='width:100%;height:6px;background:rgba(255,255,255,0.1);border-radius:3px;margin-top:8px;overflow:hidden'>
          <div style='width:78%;height:100%;background:linear-gradient(90deg,#10b981,#3b82f6);border-radius:3px;animation:pulse 2s ease-in-out infinite'></div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>

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
      </div>
    </div>
    <div class='feature-card'>
      <div style='font-size:32px;margin-bottom:8px'>📝</div>
      <div class='feature-title'>Smart Resume Builder</div>
      <div class='feature-desc'>Create professional resumes and cover letters using modern, ATS-friendly templates. Generate tailored content with AI assistance and export in multiple formats (PDF, DOCX).</div>
      <div style='margin-top:16px;padding:12px;background:rgba(34,197,94,0.1);border-radius:8px;border-left:3px solid #22c55e'>
        <div style='font-size:12px;color:rgba(255,255,255,0.8);font-weight:600'>🎨 Professional Templates</div>
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
      </div>
      <div class='feature-card' style='text-align:center;padding:24px'>
        <div style='font-size:32px;margin-bottom:12px'>🌐</div>
        <div style='font-weight:700;margin-bottom:8px'>Visit Website</div>
        <a href='https://hirelyzer-ch2pihnds3cktdxkvu84er.streamlit.app/' target='_blank' style='color:#8ab4f8;text-decoration:none;font-weight:600'>https://hirelyzer-ijkfwqydjqz3wqyvjkhegw.streamlit.app/</a>
      </div>
    </div>
    <div style='padding:32px;background:linear-gradient(135deg,rgba(79,70,229,0.1),rgba(59,130,246,0.05));border-radius:16px;border:1px solid rgba(79,70,229,0.2)'>
      <div style='font-size:18px;font-weight:700;margin-bottom:12px;color:rgba(255,255,255,0.95)'>🚀 Ready to Transform Your Career?</div>
      <p style='color:rgba(255,255,255,0.8);margin-bottom:20px'>Join thousands of professionals who have already upgraded their resumes with HIRELYZER</p>
      <a href="https://hirelyzer-ch2pihnds3cktdxkvu84er.streamlit.app/" target="_blank" class='btn' style='text-decoration:none'>
        ✨ Start Your Journey Now
      </a>
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
    </div>
  </div>
</div>
"""
st.markdown(contact_html, unsafe_allow_html=True)
