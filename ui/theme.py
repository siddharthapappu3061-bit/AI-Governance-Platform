# ui/theme.py
import base64
import streamlit as st

LOGO_PATH = "assets/logo2.png"

def _get_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def apply_global_styles():

    # ── 1. Hide Streamlit's built-in multipage nav & header chrome ──────────
    st.markdown("""
    <style>
    /* Hide Streamlit default nav */
    [data-testid="stSidebarNav"]          { display: none !important; }
    section[data-testid="stSidebar"] nav  { display: none !important; }
                
                /* Remove Streamlit sidebar header */
[data-testid="stSidebarHeader"]{
    display:none !important;
    height:0 !important;
    min-height:0 !important;
    padding:0 !important;
    margin:0 !important;
}

    /* Kill the default top header bar (Deploy button, hamburger, etc.) */
    [data-testid="stHeader"]              { display: none !important; }
    #MainMenu                             { display: none !important; }
    footer                                { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

    # ── 2. Global layout — zero top gap, correct sidebar colour ─────────────
    st.markdown("""
    <style>
    html, body { margin: 0; padding: 0; }

    /* Remove ALL top padding Streamlit injects */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    /* Push main content down by exactly the navbar height (48px) */
    section.main > div.block-container {
        margin-top: 48px;
    }

    .main { background-color: #f8fafc; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
        top: 48px !important;          /* starts BELOW the navbar */
        padding-top: 0 !important;
    }
    [data-testid="stSidebar"] * { color: white; }

    /* No gap above sidebar content */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── 3. Sticky top navbar ────────────────────────────────────────────────
    st.markdown("""
    <style>
    .cx-navbar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 48px;
        z-index: 1000;
        background: #0B1220;
        border-bottom: 1px solid #1E293B;
        display: flex;
        align-items: center;
        padding: 0;
    }

    /* Make the Streamlit column wrapper inside the navbar flex-friendly */
    .cx-navbar [data-testid="stHorizontalBlock"] {
        width: 100% !important;
        gap: 0 !important;
        align-items: center !important;
        height: 48px;
    }

    /* All page_link anchors inside navbar */
    .cx-navbar [data-testid="stPageLink-NavLink"] {
        padding: 0 !important;
        border-radius: 0 !important;
        background: transparent !important;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .cx-navbar [data-testid="stPageLink-NavLink"] p {
        font-size: 0.88rem !important;
        font-weight: 500 !important;
        color: #94A3B8 !important;
        margin: 0 !important;
        white-space: nowrap;
    }
    .cx-navbar [data-testid="stPageLink-NavLink"]:hover p {
        color: #E2E8F0 !important;
    }

    /* Active main tab */
    .cx-top-active [data-testid="stPageLink-NavLink"] {
        border-bottom: 2px solid #5B8DEF !important;
        height: 48px;
    }
    .cx-top-active [data-testid="stPageLink-NavLink"] p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* Inactive main tab */
    .cx-top-item [data-testid="stPageLink-NavLink"] {
        border-bottom: 2px solid transparent !important;
        height: 48px;
    }

    /* Instructions link — smaller, muted, top right */
    .cx-instructions-link [data-testid="stPageLink-NavLink"] {
        background: rgba(255,255,255,0.07) !important;
        border-radius: 6px !important;
        padding: 4px 10px !important;
        height: auto !important;
        margin: auto;
    }
    .cx-instructions-link [data-testid="stPageLink-NavLink"] p {
        font-size: 0.75rem !important;
        color: #94A3B8 !important;
        font-weight: 500 !important;
    }
    .cx-instructions-link [data-testid="stPageLink-NavLink"]:hover p {
        color: #E2E8F0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── 4. Sidebar logo + workflow list ─────────────────────────────────────
    st.markdown("""
    <style>
    .sidebar-logo {
        background: #FFFFFF;
        border-radius: 12px;
        margin: 14px 16px 0 16px;
        padding: 10px 14px;
        text-align: center;
        border: 1px solid #E5E7EB;
    }
    .sidebar-logo img { width: 180px; height: auto; }

    .cx-workflow-label {
        color: #7C8AA8; font-size: 0.68rem; font-weight: 700;
        letter-spacing: 0.08em; margin: 18px 0 8px 14px;
    }

    .cx-nav-item {
        border-radius: 10px; overflow: hidden; margin-bottom: 2px;
    }
    .cx-nav-item [data-testid="stPageLink-NavLink"] {
        width: 100% !important;
        padding: 7px 10px !important;
        border-radius: 10px !important;
        background: transparent !important;
    }
    .cx-nav-item [data-testid="stPageLink-NavLink"] > div {
        display: flex; align-items: center; justify-content: flex-start !important; gap: 9px;
    }
    .cx-nav-item [data-testid="stPageLink-NavLink"] p {
        font-size: 0.88rem !important; font-weight: 500 !important;
        color: #CBD5E1 !important; margin: 0 !important;
    }
    .cx-nav-item [data-testid="stPageLink-NavLink"] span { font-size: 0.88rem !important; }
    .cx-nav-item:hover { background: rgba(255,255,255,0.06); }

    .cx-nav-active { background: #1F2B4D; border-left: 3px solid #5B8DEF; }
    .cx-nav-active [data-testid="stPageLink-NavLink"] p {
        color: #FFFFFF !important; font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── 5. Breadcrumb + sub-tab pills ───────────────────────────────────────
    st.markdown("""
    <style>
    .cx-breadcrumb {
        font-size: 0.82rem; margin: 0.3rem 0 0.8rem 0;
    }
    .cx-breadcrumb-muted  { color: #94A3B8; }
    .cx-breadcrumb-sep    { color: #CBD5E1; margin: 0 5px; }
    .cx-breadcrumb-active { color: #0F172A; font-weight: 700; }

    .cx-subtabs [data-testid="stPageLink-NavLink"] {
        background: #F1F5F9 !important; border-radius: 10px !important;
        padding: 0.45rem 0.85rem !important; border: 1px solid #E2E8F0 !important;
    }
    .cx-subtabs [data-testid="stPageLink-NavLink"] p {
        font-size: 0.84rem !important; color: #374151 !important;
    }
    .cx-subtabs-active [data-testid="stPageLink-NavLink"] {
        background: #EEF2FF !important; border: 1px solid #6C63FF !important;
    }
    .cx-subtabs-active [data-testid="stPageLink-NavLink"] p {
        color: #6C63FF !important; font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── 6. Cards, buttons, forms ─────────────────────────────────────────────
    st.markdown("""
    <style>
    .card {
        background: white; border: 1px solid #e5e7eb; border-radius: 16px;
        padding: 24px; box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
    }
    .stepper {
        background: white; border: 1px solid #e5e7eb; border-radius: 12px;
        padding: 18px; margin-bottom: 20px;
    }
    .stButton > button {
        background-color: #6D5DFC; color: white; border: none;
        border-radius: 8px; font-weight: 600;
    }
    .stButton > button:hover { background-color: #5848f5; color: white; }
    .review-box {
        border: 1px solid #e5e7eb; border-radius: 12px;
        padding: 20px; background: white;
    }
    .review-label { font-weight: 600; color: #4b5563; margin-top: 12px; }

    div[data-baseweb="select"] > div {
        background: linear-gradient(135deg, #6C63FF, #5A54E8) !important;
        color: white !important; border: none !important; border-radius: 14px !important;
    }

    [data-testid="stVerticalBlock"] > div:has(.card-title) {
        background: white; border: 1px solid #E5E7EB;
        border-radius: 16px; padding: 20px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }
    .score-number { text-align: center; font-size: 72px; font-weight: 700; }
    .score-label  { text-align: center; font-size: 24px; font-weight: 600; color: #22c55e; }
    </style>
    """, unsafe_allow_html=True)

    # ── 7. Status badges ─────────────────────────────────────────────────────
    st.markdown("""
    <style>
    .badge { display:inline-block; padding:3px 11px; border-radius:20px; font-size:0.73rem; font-weight:700; }
    .b-submitted { background:#EDE9FF; color:#4A42CC; }
    .b-review    { background:#FFF3CD; color:#856404; }
    .b-approved  { background:#D1F5EA; color:#0f6e56; }
    .b-rejected  { background:#FDE8E8; color:#c0392b; }
    .b-deferred  { background:#F0F0F0; color:#555; }
    </style>
    """, unsafe_allow_html=True)

    # ── 8. Info tooltip + score basis (used in M3 Gain-Pain) ────────────────
    st.markdown("""
    <style>
    .info-wrap {
        display: inline-block; position: relative;
        vertical-align: middle; margin-left: 5px; cursor: pointer;
    }
    .info-icon {
        display: inline-flex; align-items: center; justify-content: center;
        width: 16px; height: 16px; border-radius: 50%;
        background: #6C63FF; color: #fff;
        font-size: 0.62rem; font-weight: 800; font-style: normal;
        line-height: 1; user-select: none;
    }
    .info-wrap .info-tooltip {
        visibility: hidden; opacity: 0;
        transition: opacity 0.18s ease;
        position: absolute; bottom: 130%; left: 50%;
        transform: translateX(-50%);
        background: #1a1a2e; color: #f0f0f0;
        border-radius: 10px; padding: 0.7rem 0.9rem;
        font-size: 0.76rem; line-height: 1.6;
        width: 330px; z-index: 9999;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35);
        white-space: normal; pointer-events: none;
    }
    .info-wrap .info-tooltip code {
        background: rgba(255,255,255,0.12); border-radius: 4px;
        padding: 1px 5px; font-size: 0.74rem; color: #C5C1FF;
    }
    .info-wrap .info-tooltip::after {
        content: ""; position: absolute; top: 100%; left: 50%;
        transform: translateX(-50%);
        border: 6px solid transparent; border-top-color: #1a1a2e;
    }
    .info-wrap:hover .info-tooltip { visibility: visible; opacity: 1; }

    .score-basis {
        background: #F7F7FF; border-left: 3px solid #C5C1FF;
        border-radius: 0 6px 6px 0; padding: 0.4rem 0.75rem;
        margin-top: 6px; font-size: 0.72rem; color: #555; line-height: 1.5;
    }
    .score-basis .basis-label {
        font-weight: 700; color: #6C63FF; font-size: 0.67rem;
        text-transform: uppercase; letter-spacing: 0.06em;
        display: block; margin-bottom: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ── 9. Sidebar expander styling ──────────────────────────────────────────
    st.markdown("""
    <style>
    [data-testid="stExpander"] details summary {
        background: #1f2b4d !important; color: white !important;
        border-radius: 10px !important; border: none !important;
    }
    [data-testid="stExpander"] details summary:hover { background: #2b3b66 !important; }
    [data-testid="stExpander"] details { background: transparent !important; border: none !important; }
    [data-testid="stExpander"] details div[role="group"] { background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)


def apply_background_logo():
    try:
        logo_base64 = _get_base64(LOGO_PATH)
    except Exception:
        return
    st.markdown(f"""
    <style>
    .stApp::before {{
        content: "";
        position: fixed; top: 50%; left: 50%;
        width: 700px; height: 700px;
        transform: translate(-50%, -50%);
        background-image: url("data:image/png;base64,{logo_base64}");
        background-repeat: no-repeat; background-position: center;
        background-size: contain; opacity: 0.08;
        z-index: 1; pointer-events: none;
    }}
    </style>
    """, unsafe_allow_html=True)


def apply_theme():
    apply_global_styles()
