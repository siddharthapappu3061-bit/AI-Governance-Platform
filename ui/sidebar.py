# ui/sidebar.py
# ─────────────────────────────────────────────────────────────────────────
# Figma-aligned sidebar redesign (figma.com/make/.../Cortexa-AIGovernance-V1.1).
#
# The Figma reference uses a slim dark sidebar with a single "WORKFLOW"
# header and a flat list of three steps — Idea Submission, Assessment,
# Governance Board — no nested expanders. "Assessment" covers what this
# app implements as two pages (Feasibility Assessment + Gain-Pain
# Analysis) via an in-page tab switcher (see ui/navbar.py's breadcrumb +
# the sub-tab pills added at the top of those two pages). "Governance
# Board" covers what this app implements as the Governance Dashboard
# (Overview / ISO 42001 / NIST / Visuals tabs already match the Figma
# design 1:1) — the standalone Governance Review (committee decision
# form) page still exists and is linked to from inside the dashboard.
#
# The logo block at the top is kept exactly as before — only the nav list
# below it changes. Project Execution / Tracking are out of this sidebar
# entirely now since Figma treats them as their own top-level sections
# (see ui/navbar.py) — both remain placeholder pages per the brief.
# ─────────────────────────────────────────────────────────────────────────

import streamlit as st

from utils.helpers import get_api_key, resolve_model

import base64

def _logo_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = _logo_base64("assets/logo2.png")

PAGE_BADGES = {
    "landing":           ("🤖", "AI Governance Platform"),
    "instructions":      ("📘", "Instructions"),
    "idea_submission":   ("💡", "Idea Submission"),
    "m2":                ("📊", "Feasibility Assessment"),
    "m3":                ("⚖️", "Gain-Pain Analysis"),
    "m4":                ("🏛️", "Governance Review"),
    "m5":                ("📊", "Governance Board"),
    "m6":                ("🧑‍⚖️", "Expert Advice"),
    "project_execution": ("🚧", "Project Execution"),
    "tracking":          ("📍", "Tracking"),
}

# Pages that belong to the "Problem Selection" workflow section — the
# sidebar's WORKFLOW list only appears for these, matching the Figma
# behaviour where Instructions / Project Execution / Tracking show no
# left sidebar at all.
WORKFLOW_SECTION = {"idea_submission", "m2", "m3", "m4", "m5", "m6"}

# The three flat WORKFLOW entries, Figma-style. "Assessment" routes to the
# Feasibility Assessment page (the first of the two assessment sub-pages);
# "Governance Board" routes to the Analytics/Governance dashboard.
WORKFLOW_ITEMS = [
    ("idea_submission",  "💡 Idea Submission",   "pages/1_Idea_Submission.py"),
    ("assessment",       "📊 Assessment",        "pages/2_Feasibility_Assessment.py"),
    ("governance_review","🏛️ Governance Review", "pages/4_Governance_Review.py"),
    ("governance_board", "✅ Governance Board",  "pages/5_Analytics_Dashboard.py"),
]


def _init_llm_defaults():
    """Resolve provider + model automatically from whichever API key is
    available (Streamlit secrets > env vars > config/app_config.json),
    with zero UI. Runs once per session — call_ai() reads the results
    from st.session_state. Unchanged from the original sidebar."""
    if "llm_provider" in st.session_state and "llm_model" in st.session_state:
        return
    api_key = get_api_key()
    if not api_key:
        return
    provider, model = resolve_model(api_key)
    st.session_state["api_key_input"] = api_key
    st.session_state["llm_provider"] = provider
    st.session_state["llm_model"] = model


def render_sidebar(active: str = "landing"):

    st.markdown("""
        <style>
        /* Expander header */
        [data-testid="stExpander"] details summary {
            background: #1f2b4d !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }

        /* Hover */
        [data-testid="stExpander"] details summary:hover {
            background: #2b3b66 !important;
        }

        /* Expanded content */
        [data-testid="stExpander"] details {
            background: transparent !important;
            border: none !important;
        }

        /* Remove white body */
        [data-testid="stExpander"] details div[role="group"] {
            background: transparent !important;
        }
        </style>
        """, unsafe_allow_html=True)

    _init_llm_defaults()

    with st.sidebar:

        st.markdown(
            f"""
            <div class="sidebar-logo">
                <img src="data:image/png;base64,{logo}">
            </div>

            <div class="sidebar-title">
            </div>
            """,
            unsafe_allow_html=True
        )

        # Flat WORKFLOW list — only for pages inside the Problem Selection
        # section, matching the Figma reference's collapsed/expanded states.
        if active in WORKFLOW_SECTION:
            st.markdown('<div class="cx-workflow-label">WORKFLOW</div>', unsafe_allow_html=True)

            assessment_active = active in ("m2", "m3")
            review_active = active == "m4"
            governance_active = active in ("m4", "m5")

            for code, label, target in WORKFLOW_ITEMS:
                is_active = (
                    (code == "idea_submission" and active == "idea_submission") or
                    (code == "assessment" and assessment_active) or
                    (code == "governance_review" and review_active) or
                    (code == "governance_board" and governance_active)
                )
                css_class = "cx-nav-item cx-nav-active" if is_active else "cx-nav-item"
                st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
                st.page_link(target, label=label)
                st.markdown('</div>', unsafe_allow_html=True)

            # Expert Advice kept reachable but tucked out of the primary
            # three-item list, same as Figma keeps secondary tools subtle.
