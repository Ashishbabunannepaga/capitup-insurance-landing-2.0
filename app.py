import streamlit as st
from pathlib import Path
import base64
import html

# ============================================================
# CapitUp Insurance Camp Landing Page
# ============================================================

st.set_page_config(
    page_title="CapitUp | Insurance Made Simple",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

FORMS = {
    "health": {
        "title": "Health Insurance",
        "icon": "🏥",
        "tagline": "Protect your health & your family",
        "description": "Explore health insurance options for yourself and your loved ones.",
        "url": "https://tally.so/r/KYbbbD",
        "button": "Get Health Assistance",
    },
    "term": {
        "title": "Term Life Insurance",
        "icon": "🛡️",
        "tagline": "Protect your family's financial future",
        "description": "Find life cover that can help protect the people who matter most.",
        "url": "https://tally.so/r/A7Z1GD",
        "button": "Explore Term Insurance",
    },
    "motor": {
        "title": "Motor Insurance",
        "icon": "🚗",
        "tagline": "Protect your vehicle & your journey",
        "description": "Get assistance with new insurance, renewals and motor insurance needs.",
        "url": "https://tally.so/r/PdKVJb",
        "button": "Get Motor Assistance",
    },
}

# Optional: place the actual CapitUp logo at assets/logo.png
LOGO_CANDIDATES = [
    Path(__file__).parent / "logo.png",
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
for _logo_path in LOGO_CANDIDATES:
    if _logo_path.exists():
        logo_uri = get_logo_data_uri(_logo_path)
        if logo_uri:
            break

# Optional QR/source tracking:
try:
    source = str(st.query_params.get("source", "")).strip()[:100]
except Exception:
    source = ""

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
}
.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(244,196,48,.10), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(0,172,193,.08), transparent 28%),
        #f7f8fa;
}
.block-container {
    max-width: 1180px;
    padding-top: 1.2rem;
    padding-bottom: 2.5rem;
}
#MainMenu, footer, header { visibility: hidden; }

.hero {
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    padding: 42px 34px 40px;
    margin-bottom: 28px;
    background: linear-gradient(135deg, #111827 0%, #182334 54%, #101827 100%);
    box-shadow: 0 22px 55px rgba(15,23,42,.16);
    text-align: center;
}
.hero::before {
    content: "";
    position: absolute;
    width: 330px; height: 330px;
    right: -110px; top: -170px;
    border-radius: 50%;
    background: rgba(245,197,66,.12);
}
.hero::after {
    content: "";
    position: absolute;
    width: 240px; height: 240px;
    left: -130px; bottom: -150px;
    border-radius: 50%;
    background: rgba(0,188,212,.10);
}
.brand {
    position: relative; z-index: 1;
    display: inline-flex; align-items: center; justify-content: center;
    gap: 12px; margin-bottom: 20px;
}
.brand-mark {
    width: 50px; height: 50px;
    border: 2px solid rgba(245,197,66,.75);
    border-radius: 15px;
    display: flex; align-items: center; justify-content: center;
    background: rgba(255,255,255,.05);
    font-size: 25px;
}
.brand-text {
    color: #f5c542; font-size: 19px; font-weight: 800;
    letter-spacing: .9px;
}
.hero-logo {
    position: relative; z-index: 1;
    width: min(285px, 78vw);
    height: auto;
    max-height: 105px;
    object-fit: contain;
    object-position: center;
    margin: 0 auto 19px;
    display: block;
}
.hero h1 {
    position: relative; z-index: 1;
    color: #fff; font-size: clamp(30px,4vw,48px);
    line-height: 1.08; margin: 0; font-weight: 800;
    letter-spacing: -1.4px;
}
.strategic-tagline {
    position: relative; z-index: 1;
    max-width: 780px;
    margin: 10px auto 0;
    color: #f5c542;
    font-size: clamp(11px, 1.7vw, 14px);
    line-height: 1.5;
    font-weight: 700;
    letter-spacing: .45px;
}
.hero p {
    position: relative; z-index: 1;
    max-width: 680px; margin: 12px auto 0;
    color: #cbd5e1; font-size: 16px; line-height: 1.65;
}
.hero-pill {
    position: relative; z-index: 1;
    display: inline-block; margin-top: 22px;
    padding: 8px 15px; border-radius: 999px;
    color: #fef3c7; background: rgba(245,197,66,.11);
    border: 1px solid rgba(245,197,66,.25);
    font-size: 12px; font-weight: 700;
    letter-spacing: .6px; text-transform: uppercase;
}
.section-heading { text-align: center; margin: 34px 0 18px; }
.section-heading .eyebrow {
    color: #9a6d00; font-size: 12px; font-weight: 800;
    letter-spacing: 1.4px; text-transform: uppercase; margin-bottom: 7px;
}
.section-heading h2 {
    color: #172033; font-size: clamp(24px,3vw,32px);
    margin: 0; font-weight: 800; letter-spacing: -.6px;
}
.section-heading p {
    color: #64748b; margin: 8px auto 0; max-width: 620px;
    line-height: 1.55; font-size: 14px;
}
.card {
    min-height: 315px; padding: 27px 24px 22px;
    border: 1px solid #e5e7eb; border-radius: 23px;
    background: rgba(255,255,255,.96);
    box-shadow: 0 12px 35px rgba(15,23,42,.07);
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
    margin-bottom: 9px;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 42px rgba(15,23,42,.12);
    border-color: #d8b24b;
}
.icon {
    width: 58px; height: 58px; display: flex;
    align-items: center; justify-content: center;
    border-radius: 17px; background: #fff8df;
    border: 1px solid #f1df9d; font-size: 29px; margin-bottom: 19px;
}
.card h3 {
    color: #172033; font-size: 21px; line-height: 1.2;
    margin: 0 0 7px; font-weight: 800;
}
.tagline {
    color: #9a6d00; font-size: 13px; font-weight: 700;
    line-height: 1.4; margin-bottom: 11px;
}
.description {
    color: #64748b; font-size: 13px; line-height: 1.6;
    min-height: 63px; margin-bottom: 2px;
}
div.stLinkButton > a {
    width: 100%; justify-content: center;
    border-radius: 12px !important; min-height: 46px;
    font-weight: 700 !important; border: 0 !important;
    background: #172033 !important; color: #fff !important;
    transition: all .18s ease !important;
}
div.stLinkButton > a:hover {
    background: #9a6d00 !important; color: #fff !important;
    transform: translateY(-1px);
}
.steps {
    display: flex; justify-content: center; gap: 10px;
    margin: 25px auto 10px; max-width: 920px;
}
.step {
    flex: 1; background: #fff; border: 1px solid #e8ebef;
    border-radius: 16px; padding: 17px 12px; text-align: center;
    box-shadow: 0 6px 20px rgba(15,23,42,.04);
}
.step-number {
    width: 28px; height: 28px; margin: 0 auto 8px;
    display: flex; align-items: center; justify-content: center;
    border-radius: 50%; background: #fff3c4; color: #8a6100;
    font-size: 12px; font-weight: 800;
}
.step strong { color: #172033; font-size: 13px; }
.step span { display: block; color: #7b8798; font-size: 11px; margin-top: 4px; }
.help-box {
    margin: 34px 0 26px; padding: 26px 28px; border-radius: 21px;
    background: linear-gradient(135deg,#fffaf0,#fffdf8);
    border: 1px solid #f0dfaa; text-align: center;
}
.help-box h3 { color: #172033; margin: 0 0 7px; font-size: 20px; }
.help-box p { color: #64748b; margin: 0; font-size: 13px; }
.footer {
    margin-top: 38px; padding: 23px 10px 5px;
    border-top: 1px solid #e5e7eb; text-align: center;
}
.footer-brand {
    color: #172033; font-weight: 800; font-size: 14px; letter-spacing: .5px;
}
.footer-copy {
    color: #94a3b8; font-size: 11px; margin-top: 6px; line-height: 1.5;
}
@media (max-width: 760px) {
    .block-container { padding: .55rem .75rem 1.5rem; }
    .hero { border-radius: 20px; padding: 30px 19px 31px; margin-bottom: 20px; }
    .hero h1 { font-size: 30px; }
    .strategic-tagline { font-size: 11px; padding: 0 8px; }
    .hero p { font-size: 14px; }
    .brand-text { font-size: 15px; }
    .brand-mark { width: 43px; height: 43px; font-size: 21px; }
    .card { min-height: 0; padding: 22px 18px 17px; border-radius: 19px; }
    .description { min-height: 0; margin-bottom: 14px; }
    .steps { flex-direction: column; }
    .step { padding: 13px; }
    .help-box { padding: 22px 17px; border-radius: 18px; }
}
</style>
""",
    unsafe_allow_html=True,
)

if logo_uri:
    st.markdown(
        f"""
        <section class="hero">
            <img class="hero-logo" src="{logo_uri}" alt="CapitUp India Pvt. Ltd.">
            <h1>Insurance, Made Simple.</h1>
            <div class="strategic-tagline">
                Your Strategic Partner in Finance, Insurance, and Compliance
            </div>
            <p>
                Tell us what you need. Our team will help you explore
                the right insurance solution for you, your family or your vehicle.
            </p>
            <div class="hero-pill">CapitUp India Pvt. Ltd.</div>
        </section>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <section class="hero">
            <div class="brand">
                <div class="brand-mark">↗</div>
                <div class="brand-text">CAPITUP INDIA PVT. LTD.</div>
            </div>
            <h1>Insurance, Made Simple.</h1>
            <div class="strategic-tagline">
                Your Strategic Partner in Finance, Insurance, and Compliance
            </div>
            <p>
                Tell us what you need. Our team will help you explore
                the right insurance solution for you, your family or your vehicle.
            </p>
            <div class="hero-pill">CapitUp India Pvt. Ltd.</div>
        </section>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="section-heading">
        <div class="eyebrow">Choose your insurance</div>
        <h2>What can we help you with?</h2>
        <p>
            Select an option below to tell our team what you are looking for.
            The enquiry takes only a few minutes.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

cols = st.columns(3, gap="large")

for col, key in zip(cols, ("health", "term", "motor")):
    item = FORMS[key]
    with col:
        st.markdown(
            f"""
            <div class="card">
                <div class="icon">{item["icon"]}</div>
                <h3>{html.escape(item["title"])}</h3>
                <div class="tagline">{html.escape(item["tagline"])}</div>
                <div class="description">{html.escape(item["description"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button(item["button"], item["url"], use_container_width=True)

st.markdown(
    """
    <div class="section-heading" style="margin-top:48px;">
        <div class="eyebrow">Simple process</div>
        <h2>How it works</h2>
    </div>
    <div class="steps">
        <div class="step"><div class="step-number">1</div><strong>Choose</strong><span>Select your insurance need</span></div>
        <div class="step"><div class="step-number">2</div><strong>Share</strong><span>Tell us a few details</span></div>
        <div class="step"><div class="step-number">3</div><strong>Connect</strong><span>Our team contacts you</span></div>
        <div class="step"><div class="step-number">4</div><strong>Assist</strong><span>Get personalized guidance</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="help-box">
        <h3>Not sure which insurance you need?</h3>
        <p>
            That's okay. Start with the option that best matches your requirement,
            and our team can guide you from there.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer">
        <div class="footer-brand">CAPITUP INDIA PVT. LTD.</div>
        <div class="footer-copy">
            Corporate Insurance &nbsp;•&nbsp; Employee Benefits &nbsp;•&nbsp; Insurance Assistance
            <br>
            Your information is collected through the respective enquiry form
            and used to respond to your request.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if source:
    st.session_state["lead_source"] = source
