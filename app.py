import streamlit as st
from pathlib import Path
import base64
import html
import urllib.parse

# ============================================================
# Mobile-Optimized Configuration
# ============================================================
st.set_page_config(
    page_title="CapitUp | Insurance Portal",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Safe Source Tracking
try:
    source_param = str(st.query_params.get("source", "")).strip()[:100]
except Exception:
    source_param = ""

def build_url(base_url: str, src: str) -> str:
    if not src:
        return base_url
    delimiter = "&" if "?" in base_url else "?"
    return f"{base_url}{delimiter}source={urllib.parse.quote(src)}"

# Put your official WhatsApp number here (digits only, with country code)
WHATSAPP_NUMBER = "919000169185" 
wa_text = urllib.parse.quote(f"Hi CapitUp Team! I am attending the Insurance Camp ({source_param or 'Direct'}) and need assistance choosing a plan.")
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_text}"

CARDS_DATA = [
    {
        "id": "health",
        "title": "Health & Medical",
        "icon": "🏥",
        "perk": "10,000+ Cashless • Tax Saver 80D",
        "pill": "Most Popular",
        "accent": "emerald",
        "url": build_url("https://tally.so/r/KYbbbD", source_param),
        "cta": "Get Quote",
    },
    {
        "id": "term",
        "title": "Term Life Protection",
        "icon": "🛡️",
        "perk": "₹1 Cr - ₹5 Cr Cover • Fast Payout",
        "pill": "High Cover",
        "accent": "gold",
        "url": build_url("https://tally.so/r/A7Z1GD", source_param),
        "cta": "Explore",
    },
    {
        "id": "motor",
        "title": "Motor & EV Insurance",
        "icon": "🚗",
        "perk": "Zero Dep • 1-Min Instant Renewal",
        "pill": "Instant Policy",
        "accent": "cyan",
        "url": build_url("https://tally.so/r/PdKVJb", source_param),
        "cta": "Renew",
    },
]

# Logo Loader
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
# Pure Light Theme CSS (No Markdown Render Glitches)
# ============================================================
st.markdown(
"""<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header, [data-testid="stToolbar"] {
    display: none !important;
}

.stApp {
    background-color: #F8FAFC !important;
    background-image: 
        radial-gradient(circle at 10% 5%, rgba(245, 197, 66, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 90% 15%, rgba(14, 165, 233, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 50% 90%, rgba(16, 185, 129, 0.06) 0%, transparent 50%) !important;
    color: #0F172A !important;
}

.block-container {
    max-width: 460px !important;
    padding: 0.6rem 0.85rem 4.5rem 0.85rem !important;
}

/* App Header */
.app-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
}
.brand-badge {
    display: flex;
    align-items: center;
    gap: 7px;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    padding: 5px 12px;
    border-radius: 99px;
    box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
}
.brand-badge-name {
    font-size: 13px;
    font-weight: 800;
    color: #0F172A;
    letter-spacing: 0.5px;
}
.camp-badge {
    display: flex;
    align-items: center;
    gap: 6px;
    background: #ECFDF5;
    border: 1px solid #A7F3D0;
    padding: 4px 10px;
    border-radius: 99px;
    font-size: 11px;
    font-weight: 700;
    color: #047857;
}
.pulse-indicator {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #10B981;
    animation: livePulse 1.8s infinite;
}
@keyframes livePulse {
    0% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6); }
    70% { transform: scale(1.2); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.9); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

/* Compact Light Hero */
.hero-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 22px;
    padding: 16px 14px 14px;
    text-align: center;
    box-shadow: 0 8px 24px -6px rgba(15, 23, 42, 0.05);
    margin-bottom: 12px;
}
.hero-logo-img {
    max-width: 155px;
    height: auto;
    max-height: 44px;
    object-fit: contain;
    margin: 0 auto 8px;
    display: block;
}
.hero-headline {
    font-size: 21px;
    font-weight: 900;
    color: #0F172A;
    letter-spacing: -0.4px;
    margin: 0 0 4px;
    line-height: 1.2;
}
.hero-subline {
    font-size: 12.5px;
    color: #64748B;
    line-height: 1.45;
    margin: 0 auto;
    max-width: 95%;
}

/* Micro Trust Counters */
.trust-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin-bottom: 12px;
}
.trust-col {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 7px 4px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(15, 23, 42, 0.02);
}
.trust-val {
    font-size: 12px;
    font-weight: 800;
    color: #926A00;
}
.trust-lbl {
    font-size: 10px;
    color: #64748B;
    font-weight: 600;
    margin-top: 1px;
}

/* Compact 3-Card Stack (All in one view) */
.cards-deck {
    display: flex;
    flex-direction: column;
    gap: 9px;
    margin-bottom: 14px;
}

.action-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 11px 13px;
    text-decoration: none !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    -webkit-tap-highlight-color: transparent;
    user-select: none;
    box-shadow: 0 3px 10px rgba(15, 23, 42, 0.03);
}

.action-card:hover {
    border-color: #EAB308;
    box-shadow: 0 8px 20px -4px rgba(234, 179, 8, 0.15);
    transform: translateY(-1px);
}

.action-card:active {
    transform: scale(0.975);
    background: #F8FAFC;
}

/* Card Content Styling */
.card-left {
    display: flex;
    align-items: center;
    gap: 11px;
    min-width: 0;
    flex: 1;
}

.icon-square {
    width: 42px;
    height: 42px;
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
}
.icon-emerald { background: #ECFDF5; border: 1px solid #A7F3D0; }
.icon-gold { background: #FEFCE8; border: 1px solid #FEF08A; }
.icon-cyan { background: #F0F9FF; border: 1px solid #BAE6FD; }

.card-text {
    min-width: 0;
    flex: 1;
}
.card-title-row {
    display: flex;
    align-items: center;
    gap: 6px;
}
.card-title {
    font-size: 14.5px;
    font-weight: 800;
    color: #0F172A;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.card-tag {
    font-size: 9px;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 99px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    background: #FEF3C7;
    color: #92400E;
    border: 1px solid #FDE68A;
}
.card-perk {
    font-size: 11px;
    color: #64748B;
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Button Pill */
.card-right {
    margin-left: 8px;
    flex-shrink: 0;
}
.cta-pill {
    background: #0F172A;
    color: #FFFFFF;
    padding: 7px 12px;
    border-radius: 10px;
    font-size: 11.5px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 3px;
    transition: background 0.15s ease;
}
.action-card:hover .cta-pill {
    background: #B45309;
}

/* Mobile Quick Assist Dock */
.quick-dock {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 9px 13px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
}
.dock-msg {
    font-size: 11.5px;
    font-weight: 700;
    color: #334155;
    display: flex;
    align-items: center;
    gap: 5px;
}
.dock-wa-btn {
    background: #10B981;
    color: #FFFFFF !important;
    text-decoration: none !important;
    padding: 6px 12px;
    border-radius: 99px;
    font-size: 11px;
    font-weight: 800;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    box-shadow: 0 3px 8px rgba(16, 185, 129, 0.25);
    transition: transform 0.15s ease;
}
.dock-wa-btn:active {
    transform: scale(0.96);
}

.brand-footer {
    text-align: center;
    margin-top: 14px;
    font-size: 10px;
    color: #94A3B8;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# APP BAR
# ============================================================
st.markdown("""
<div class="app-nav">
    <div class="brand-badge">
        <span>🛡️</span>
        <span class="brand-badge-name">CAPITUP</span>
    </div>
    <div class="camp-badge">
        <span class="pulse-indicator"></span>
        Camp Live Today
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HERO PANEL
# ============================================================
logo_markup = (
    f'<img class="hero-logo-img" src="{logo_uri}" alt="CapitUp">'
    if logo_uri
    else '<div style="font-size:18px; font-weight:900; color:#B45309; letter-spacing:0.5px; margin-bottom:4px;">CAPITUP INSURANCE</div>'
)

st.markdown(f"""
<div class="hero-card">
    {logo_markup}
    <h1 class="hero-headline">Insurance, Made Simple.</h1>
    <p class="hero-subline">
        Special corporate & retail assistance. Select an option below to get quotes in under 90 seconds.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# MICRO TRUST COUNTERS
# ============================================================
st.markdown("""
<div class="trust-row">
    <div class="trust-col">
        <div class="trust-val">100%</div>
        <div class="trust-lbl">Paperless</div>
    </div>
    <div class="trust-col">
        <div class="trust-val">30+</div>
        <div class="trust-lbl">Insurers</div>
    </div>
    <div class="trust-col">
        <div class="trust-val">Free</div>
        <div class="trust-lbl">Claim Desk</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 3 COMPACT TOUCH CARDS (Built Cleanly to Avoid Markdown Bugs)
# ============================================================
cards_html_parts = ['<div class="cards-deck">']

for card in CARDS_DATA:
    cards_html_parts.append(
        f'<a class="action-card" href="{card["url"]}" target="_blank" rel="noopener noreferrer">'
        f'<div class="card-left">'
        f'<div class="icon-square icon-{card["accent"]}">{card["icon"]}</div>'
        f'<div class="card-text">'
        f'<div class="card-title-row">'
        f'<span class="card-title">{html.escape(card["title"])}</span>'
        f'<span class="card-tag">{card["pill"]}</span>'
        f'</div>'
        f'<div class="card-perk">{html.escape(card["perk"])}</div>'
        f'</div>'
        f'</div>'
        f'<div class="card-right">'
        f'<span class="cta-pill">{card["cta"]} →</span>'
        f'</div>'
        f'</a>'
    )

cards_html_parts.append('</div>')
st.markdown("".join(cards_html_parts), unsafe_allow_html=True)

# ============================================================
# QUICK WHATSAPP DOCK & FOOTER
# ============================================================
st.markdown(f"""
<div class="quick-dock">
    <div class="dock-msg">
        <span>💬</span> Need help choosing?
    </div>
    <a class="dock-wa-btn" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">
        WhatsApp Desk
    </a>
</div>

<div class="brand-footer">
    CapitUp India Pvt. Ltd. • Corporate & Retail Insurance Advisory
</div>
""", unsafe_allow_html=True)

# Save session lead tracking
if source_param:
    st.session_state["lead_source"] = source_param
