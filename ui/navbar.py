# ui/navbar.py
import streamlit as st

SECTION_OF = {
    "landing":           "problem_selection",
    "instructions":      "instructions",
    "idea_submission":   "problem_selection",
    "m2":                "problem_selection",
    "m3":                "problem_selection",
    "m4":                "problem_selection",
    "m5":                "problem_selection",
    "m6":                "problem_selection",
    "project_execution": "project_execution",
    "tracking":          "tracking",
}

# Main tabs (centre) — 3 primary sections
MAIN_TABS = [
    ("problem_selection",  "Problem Selection",  "pages/1_Idea_Submission.py"),
    ("project_execution",  "Project Execution",  "pages/7_Project_Execution.py"),
    ("tracking",           "Tracking",           "pages/8_Tracking.py"),
]


def render_navbar(active: str = "landing"):
    active_section = SECTION_OF.get(active, "problem_selection")

    # The navbar is rendered as a Streamlit horizontal block and then
    # repositioned to the top via CSS (position:fixed). We need columns:
    # [logo gap] [tab] [tab] [tab] [spacer] [instructions link]
    # The logo gap matches the sidebar width so tabs start after it.

    st.markdown('<div class="cx-navbar" id="cx-navbar">', unsafe_allow_html=True)

    # columns: sidebar-width spacer | 3 main tabs | flex spacer | instructions
    cols = st.columns([3.5, 1.4, 1.4, 1.4, 3, 0.8])

    # col 0: empty — sits behind the sidebar
    with cols[0]:
        pass

    # cols 1-3: main tabs
    for i, (code, label, target) in enumerate(MAIN_TABS):
        is_active = (code == active_section)
        css = "cx-top-active" if is_active else "cx-top-item"
        with cols[i + 1]:
            st.page_link(target, label=label)

    # col 4: spacer
    with cols[4]:
        pass

    # col 5: Instructions — small, top-right
    with cols[5]:
        st.page_link("pages/0_Instructions.py", label="Help")


def render_subtabs(items, active_target):
    cols = st.columns(len(items) + 4)
    for i, (label, target) in enumerate(items):
        with cols[i]:
            css = "cx-subtabs cx-subtabs-active" if target == active_target else "cx-subtabs"
            st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
            st.page_link(target, label=label)
            st.markdown("</div>", unsafe_allow_html=True)
    st.write("")


def render_breadcrumb(section_label: str, page_label: str):
    st.markdown(f"""
    <div class="cx-breadcrumb">
        <span class="cx-breadcrumb-muted">{section_label}</span>
        <span class="cx-breadcrumb-sep">/</span>
        <span class="cx-breadcrumb-active">{page_label}</span>
    </div>
    """, unsafe_allow_html=True)
