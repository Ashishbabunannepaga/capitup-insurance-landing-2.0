import streamlit as st
from pathlib import Path
import base64
import html
import urllib.parse

# ============================================================
# Page Configuration & Viewport Optimization
# ============================================================
st.set_page_config(
    page_title="CapitUp | Insurance Portal",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Optional QR / Source tracking logic
try:
    source_param = str(st.query_params.get("source", "")).strip()[:100]
except Exception:
    source_param = ""

def build_url(base_url: str, src: str) -> str:
    if not src:
        return base_url
    delimiter = "&" if "?" in base_url else "?"
    return f"{base_url}{delimiter}source={urllib.parse.quote(src)}"

# Put your official WhatsApp number here (digits only, e.g. 919876543210)
WHATSAPP_NUMBER = "919876543210" 
wa_msg = urllib.parse.quote(f"Hi CapitUp Team! I'm attending the Insurance Camp ({source_param or 'Online'}) and need quick guidance on insurance.")
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg}"

FORMS = {
    "health": {
        "title": "Health & Medical Shield",
        "category": "health",
        "icon": "🏥",
        "tagline": "Family & Individual Comprehensive Cover",
        "description": "10,000+ cashless hospitals, 0% co-pay, pre-existing disease coverage & maternity benefits.",
        "badges": ["✨ Cashless in 30 Mins", "💰 Tax Saver 80D", "👨‍👩‍👧 Family Floater"],
        "accent": "emerald",
        "url": build_url("https://tally.so/r/KYbbbD", source_param),
        "cta": "Get Health Quote",
    },
    "term": {
        "title": "Term Life Protection",
        "category": "term",
        "icon": "🛡️",
        "tagline": "Guaranteed Financial Security for Family",
        "description": "High sum assured (₹1 Cr - ₹5 Cr+) with critical illness rider & accidental disability waivers.",
        "badges": ["💎 Up to ₹5 Cr Cover", "⚡ 99.2% Claim Settlement", "🛡️ Critical Illness Add-on"],
        "accent": "amber",
        "url": build_url("https://tally.so/r/A7Z1GD", source_param),
        "cta": "Explore Term Plans",
    },
    "motor": {
        "title": "Motor & EV Insurance",
        "category": "motor",
        "icon": "⚡",
        "tagline": "Cars, Two-Wheelers & Commercial Fleets",
        "description": "Zero depreciation, instant digital copy issue, roadside breakdown assistance & quick claim inspections.",
        "badges": ["🚗 0% Depreciation", "⏱️ 1-Minute Renewal", "🛠️ 24/7 Roadside Assist"],
        "accent": "cyan",
        "url": build_url("https://tally.so/r/PdKVJb", source_param),
        "cta": "Renew or Buy Cover",
    },
}

# Optional Logo Loader
LOGO_CANDIDATES = [
    Path(__file__).parent / "assets" / "capitup_logo_transparent.png",
    Path(__file__).parent / "assets" / "capitup_logo.png",
    Path(__file__).parent / "assets" / "logo.png",
]

def get_logo_data_uri(path: Path):
    if not path.exists():
        return None
    try:
        encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
        mime = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
            ".svg": "image/svg+xml",
        }.get(path.suffix.lower(), "image/png")
        return f"data:{mime};base64,{encoded}"
    except Exception:
        return None

logo_uri = None
for _p in LOGO_CANDIDATES:
    if _p.exists():
        logo_uri = get_logo_data_uri(_p)
        if logo_uri:
            break

# ============================================================
# Mobile-First Next-Gen Styling & Micro-Interactions
# ============================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

/* Reset and Viewport Lock */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header, [data-testid="stToolbar"] {
    display: none !important;
}

.stApp {
    background: #060911;
    color: #F8FAFC;
    overflow-x: hidden;
}

.block-container {
    max-width: 500px !important; /* Perfect mobile iPhone/Pixel viewport ratio */
    padding: 0.6rem 0.9rem 6rem 0.9rem !important;
}

/* Ambient Animated Radial Light Orbs */
.orb-glow {
    position: fixed;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100vw;
    height: 100vh;
    max-width: 520px;
    pointer-events: none;
    z-index: 0;
}
.orb-1 {
    position: absolute;
    top: -5%;
    right: -10%;
    width: 280px;
    height: 280px;
    background: radial-gradient(circle, rgba(245, 197, 66, 0.16) 0%, transparent 70%);
    filter: blur(40px);
    animation: orbFloat 7s ease-in-out infinite alternate;
}
.orb-2 {
    position: absolute;
    top: 30%;
    left: -15%;
    width: 260px;
    height: 260px;
    background: radial-gradient(circle, rgba(16, 185, 129, 0.14) 0%, transparent 70%);
    filter: blur(45px);
    animation: orbFloat 9s ease-in-out infinite alternate-reverse;
}
@keyframes orbFloat {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(25px, 35px) scale(1.15); }
}

/* App Bar & Brand Header */
.app-header {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 4px 16px;
}
.brand-pill {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 5px 12px;
    border-radius: 99px;
}
.brand-symbol {
    font-size: 14px;
}
.brand-name {
    font-size: 13px;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: 0.5px;
}
.live-badge {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.35);
    padding: 4px 10px;
    border-radius: 99px;
    font-size: 10.5px;
    font-weight: 700;
    color: #34D399;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.live-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #10B981;
    animation: livePulse 1.6s infinite;
}
@keyframes livePulse {
    0% { transform: scale(0.9); opacity: 0.7; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 0 7px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.9); opacity: 0.7; box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

/* Glass Hero Card with Shimmer Border */
.hero-glass {
    position: relative;
    z-index: 2;
    background: linear-gradient(175deg, rgba(26, 34, 54, 0.75) 0%, rgba(12, 17, 29, 0.92) 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border-radius: 26px;
    padding: 24px 20px 20px;
    text-align: center;
    box-shadow: 0 16px 36px -12px rgba(0, 0, 0, 0.7);
    margin-bottom: 18px;
    overflow: hidden;
}
.hero-glass::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(245, 197, 66, 0.6), transparent);
}
.hero-logo-img {
    max-width: 190px;
    height: auto;
    max-height: 60px;
    object-fit: contain;
    margin: 0 auto 12px;
    display: block;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4));
}
.hero-title {
    font-size: clamp(24px, 6.2vw, 30px);
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -0.6px;
    margin: 0 0 8px;
    background: linear-gradient(180deg, #FFFFFF 40%, #CBD5E1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-desc {
    font-size: 13px;
    color: #94A3B8;
    line-height: 1.5;
    margin: 0 auto;
    max-width: 95%;
}

/* Live Activity Ticker */
.activity-ticker {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 6px 12px;
    border-radius: 99px;
    font-size: 11px;
    color: #E2E8F0;
    font-weight: 600;
    margin-top: 14px;
}

/* Category Filter Tabs (Zero-Reload Pure CSS Interactive Switching) */
.filter-tabs {
    position: relative;
    z-index: 2;
    display: flex;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 4px;
    border-radius: 16px;
    margin-bottom: 18px;
    gap: 4px;
}
.filter-tab {
    flex: 1;
    text-align: center;
    padding: 8px 6px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 700;
    color: #94A3B8;
    cursor: pointer;
    transition: all 0.2s ease;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
}
.filter-tab:hover {
    color: #FFF;
    background: rgba(255, 255, 255, 0.06);
}
.filter-tab.active {
    background: linear-gradient(135deg, #F5C542, #E5B229);
    color: #0B0F19;
    font-weight: 800;
    box-shadow: 0 4px 12px rgba(245, 197, 66, 0.35);
}

/* Action Cards */
.cards-deck {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    gap: 15px;
}
.super-card {
    display: block;
    text-decoration: none !important;
    background: linear-gradient(145deg, rgba(22, 29, 46, 0.9) 0%, rgba(13, 18, 30, 0.96) 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 19px 17px;
    position: relative;
    overflow: hidden;
    transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.22s ease, box-shadow 0.22s ease;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
    box-shadow: 0 10px 24px -10px rgba(0, 0, 0, 0.6);
}
.super-card:hover {
    border-color: rgba(245, 197, 66, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 18px 34px -8px rgba(245, 197, 66, 0.12);
}
.super-card:active {
    transform: scale(0.965);
    border-color: rgba(245, 197, 66, 0.6);
}

/* Card Header */
.card-header-flex {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}
.icon-box-3d {
    width: 48px;
    height: 48px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    flex-shrink: 0;
    position: relative;
}
.icon-emerald {
    background: radial-gradient(circle, rgba(16, 185, 129, 0.25) 0%, rgba(16, 185, 129, 0.08) 100%);
    border: 1px solid rgba(16, 185, 129, 0.35);
    box-shadow: 0 0 16px rgba(16, 185, 129, 0.2);
}
.icon-amber {
    background: radial-gradient(circle, rgba(245, 197, 66, 0.25) 0%, rgba(245, 197, 66, 0.08) 100%);
    border: 1px solid rgba(245, 197, 66, 0.35);
    box-shadow: 0 0 16px rgba(245, 197, 66, 0.2);
}
.icon-cyan {
    background: radial-gradient(circle, rgba(6, 182, 212, 0.25) 0%, rgba(6, 182, 212, 0.08) 100%);
    border: 1px solid rgba(6, 182, 212, 0.35);
    box-shadow: 0 0 16px rgba(6, 182, 212, 0.2);
}

.card-title-group {
    flex: 1;
}
.card-headline {
    font-size: 18px;
    font-weight: 800;
    color: #FFF;
    margin: 0;
    letter-spacing: -0.3px;
}
.card-tagline {
    font-size: 11.5px;
    font-weight: 700;
    color: #F8D368;
    margin-top: 2px;
}

.card-summary {
    font-size: 12.5px;
    color: #94A3B8;
    line-height: 1.45;
    margin: 0 0 12px;
}

/* Feature Check Badges */
.card-badges-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 15px;
}
.micro-badge {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 3px 8px;
    font-size: 10.5px;
    font-weight: 600;
    color: #CBD5E1;
}

/* Interactive CTA Strip */
.card-cta-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 11px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}
.cta-label {
    font-size: 13px;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: 0.2px;
}
.action-arrow {
    width: 32px;
    height: 32px;
    border-radius: 12px;
    background: #F8D368;
    color: #090D16;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    font-weight: 900;
    transition: transform 0.18s ease;
}
.super-card:hover .action-arrow {
    transform: translateX(3px) scale(1.05);
    background: #FFE57E;
}

/* Modern Accordion */
.faq-box {
    position: relative;
    z-index: 2;
    margin-top: 24px;
}
.faq-heading-badge {
    text-align: center;
    font-size: 12px;
    font-weight: 800;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 12px;
}
details {
    background: rgba(255, 255, 255, 0.025);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 14px;
    margin-bottom: 8px;
    overflow: hidden;
}
summary {
    padding: 12px 14px;
    font-size: 13px;
    font-weight: 700;
    color: #E2E8F0;
    cursor: pointer;
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
summary::-webkit-details-marker { display: none; }
summary::after {
    content: "↓";
    font-size: 14px;
    color: #F8D368;
    font-weight: 800;
    transition: transform 0.2s ease;
}
details[open] summary::after {
    transform: rotate(180deg);
}
details[open] {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(245, 197, 66, 0.2);
}
.faq-drawer {
    padding: 0 14px 13px;
    font-size: 12px;
    color: #94A3B8;
    line-height: 1.5;
}

/* Floating Bottom Thumb Navigation Bar */
.thumb-dock {
    position: fixed;
    bottom: 12px;
    left: 50%;
    transform: translateX(-50%);
    width: min(94vw, 460px);
    z-index: 999;
    background: rgba(14, 20, 33, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.14);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 99px;
    padding: 6px 12px 6px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.8);
}
.dock-text {
    font-size: 12px;
    font-weight: 700;
    color: #F1F5F9;
    display: flex;
    align-items: center;
    gap: 6px;
}
.dock-actions {
    display: flex;
    gap: 6px;
}
.dock-btn-wa {
    background: #25D366;
    color: #062310;
    padding: 8px 13px;
    border-radius: 99px;
    font-size: 11.5px;
    font-weight: 800;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);
    transition: transform 0.15s ease;
}
.dock-btn-primary {
    background: #F8D368;
    color: #090D16;
    padding: 8px 14px;
    border-radius: 99px;
    font-size: 11.5px;
    font-weight: 800;
    text-decoration: none !important;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    transition: transform 0.15s ease;
}
.dock-btn-wa:active, .dock-btn-primary:active {
    transform: scale(0.95);
}

.footer-credits {
    position: relative;
    z-index: 2;
    text-align: center;
    margin-top: 26px;
    padding-bottom: 10px;
}
.footer-credits strong {
    font-size: 12px;
    color: #64748B;
    letter-spacing: 0.5px;
}
.footer-credits p {
    font-size: 10.5px;
    color: #475569;
    margin: 3px 0 0;
}
</style>

<div class="orb-glow">
    <div class="orb-1"></div>
    <div class="orb-2"></div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# APP BAR
# ============================================================
st.markdown(
    """
    <div class="app-header">
        <div class="brand-pill">
            <span class="brand-symbol">🛡️</span>
            <span class="brand-name">CAPITUP</span>
        </div>
        <div class="live-badge">
            <span class="live-dot"></span>
            Camp Live Today
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HERO GLASS PANEL
# ============================================================
logo_markup = (
    f'<img class="hero-logo-img" src="{logo_uri}" alt="CapitUp">'
    if logo_uri
    else '<div style="font-size:26px; font-weight:900; color:#F8D368; letter-spacing:1px; margin-bottom:8px;">CAPITUP</div>'
)

st.markdown(
    f"""
    <div class="hero-glass">
        {logo_markup}
        <h1 class="hero-title">Insurance, Simplified & Fast.</h1>
        <p class="hero-desc">
            Compare hand-picked plans, unlock exclusive camp pricing, and get assistance from certified advisors.
        </p>
        <div class="activity-ticker">
            <span>🔥</span> <strong>38 people</strong> checking rates right now
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# INTERACTIVE CATEGORY CAROUSEL CHIPS
# ============================================================
st.markdown(
    """
    <div class="filter-tabs">
        <div class="filter-tab active">🌟 All Plans</div>
        <div class="filter-tab" onclick="document.getElementById('card-health').scrollIntoView({behavior:'smooth'})">🏥 Health</div>
        <div class="filter-tab" onclick="document.getElementById('card-term').scrollIntoView({behavior:'smooth'})">🛡️ Life</div>
        <div class="filter-tab" onclick="document.getElementById('card-motor').scrollIntoView({behavior:'smooth'})">⚡ Motor</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# ACTION CARDS
# ============================================================
cards_html = ['<div class="cards-deck">']

for key, item in FORMS.items():
    badges_rendered = "".join([f'<span class="micro-badge">{b}</span>' for b in item["badges"]])
    cards_html.append(
        f"""
        <a id="card-{item['category']}" class="super-card" href="{item['url']}" target="_blank" rel="noopener noreferrer">
            <div class="card-header-flex">
                <div class="icon-box-3d icon-{item['accent']}">
                    {item['icon']}
                </div>
                <div class="card-title-group">
                    <h2 class="card-headline">{html.escape(item['title'])}</h2>
                    <div class="card-tagline">{html.escape(item['tagline'])}</div>
                </div>
            </div>
            <div class="card-summary">{html.escape(item['description'])}</div>
            <div class="card-badges-wrap">
                {badges_rendered}
            </div>
            <div class="card-cta-row">
                <span class="cta-label">{item['cta']}</span>
                <div class="action-arrow">→</div>
            </div>
        </a>
        """
    )

cards_html.append("</div>")
st.markdown("".join(cards_html), unsafe_allow_html=True)

# ============================================================
# FAQ ACCORDION (SMOOTH MOBILE COMPONENT)
# ============================================================
st.markdown(
    """
    <div class="faq-box">
        <div class="faq-heading-badge">Frequently Asked Questions</div>
        <details>
            <summary>How fast will I get policy assistance?</summary>
            <div class="faq-drawer">
                Your enquiry is routed instantly to our camp desk. A dedicated CapitUp insurance specialist will connect via WhatsApp or Call within 15–20 minutes.
            </div>
        </details>
        <details>
            <summary>Can I port my existing policy without losing benefits?</summary>
            <div class="faq-drawer">
                Yes! Your waiting period credits for pre-existing diseases are 100% safeguarded under IRDAI portability regulations.
            </div>
        </details>
        <details>
            <summary>Are there special corporate camp discounts?</summary>
            <div class="faq-drawer">
                Yes, attending through this portal grants you access to preferred corporate group rates, waived medical fees on select covers, and free claim liaison.
            </div>
        </details>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# THUMB-ZONE FLOATING QUICK DOCK & FOOTER
# ============================================================
st.markdown(
    f"""
    <!-- Mobile Floating Dock -->
    <div class="thumb-dock">
        <div class="dock-text">
            <span>💬</span> Need help?
        </div>
        <div class="dock-actions">
            <a class="dock-btn-wa" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">
                WhatsApp ⚡
            </a>
            <a class="dock-btn-primary" href="{FORMS['health']['url']}" target="_blank" rel="noopener noreferrer">
                Apply ↗
            </a>
        </div>
    </div>

    <!-- Minimal Brand Footer -->
    <div class="footer-credits">
        <strong>CAPITUP INDIA PRIVATE LIMITED</strong>
        <p>Direct Brokerage • Risk Underwriting • Fast Claims</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Retain lead source in session state
if source_param:
    st.session_state["lead_source"] = source_param
