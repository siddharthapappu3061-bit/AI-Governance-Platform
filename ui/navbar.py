# ui/navbar.py
# ─────────────────────────────────────────────────────────────────────────
# Top section-level navbar, modeled on the Figma "Cortexa" reference design
# (figma.com/make/.../Cortexa-AIGovernance-V1.1). The Figma app uses a dark
# top bar with four section tabs — Instructions, Problem Selection, Project
# Execution, Tracking — sitting above a slim left "WORKFLOW" sidebar that
# only lists the steps within the active section.
#
# This module renders that same four-tab row using st.page_link (so it's a
# real, working multipage nav — not decorative HTML), wrapped in a dark
# styled container via theme.py's apply_global_styles(). It does not touch
# any page logic — purely a navigation affordance added above each page's
# existing content.
# ─────────────────────────────────────────────────────────────────────────

import streamlit as st

# Section group each page's "active" code belongs to, used to highlight the
# correct top-level tab regardless of which sub-page within that section is
# currently open.
SECTION_OF = {
    "landing": "problem_selection",
    "instructions": "instructions",
    "idea_submission": "problem_selection",
    "m2": "problem_selection",
    "m3": "problem_selection",
    "m4": "problem_selection",
    "m5": "problem_selection",
    "m6": "problem_selection",
    "project_execution": "project_execution",
    "tracking": "tracking",
}

SECTIONS = [
    ("instructions",       "📘 Instructions",        "pages/0_Instructions.py"),
    ("problem_selection",  "💡 Problem Selection",   "pages/1_Idea_Submission.py"),
    ("project_execution",  "▶️ Project Execution",   "pages/7_Project_Execution.py"),
    ("tracking",           "📈 Tracking",            "pages/8_Tracking.py"),
]


def render_navbar(active: str = "landing"):
    active_section = SECTION_OF.get(active, "problem_selection")

    st.markdown('<div class="cx-navbar">', unsafe_allow_html=True)

    cols = st.columns(len(SECTIONS))

    for i, (code, label, target) in enumerate(SECTIONS):
        with cols[i]:
            css = "cx-top-active" if code == active_section else "cx-top-item"

            st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
            st.page_link(target, label=label)
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def render_subtabs(items, active_target):
    """Render a row of pill-style page_link 'tabs' (Figma's Feasibility
    Assessment | Gain-Pain Analysis switcher, and similarly reused for
    Submit Feedback | Expert Review Panel). `items` is a list of
    (label, target_path) tuples."""
    cols = st.columns(len(items))
    for i, (label, target) in enumerate(items):
        with cols[i]:
            css_class = "cx-subtabs-active" if target == active_target else ""
            st.markdown(f'<div class="cx-subtabs {css_class}">', unsafe_allow_html=True)
            st.page_link(target, label=label)
            st.markdown('</div>', unsafe_allow_html=True)
    st.write("")


def render_breadcrumb(section_label: str, page_label: str):
    """Small breadcrumb under the navbar, e.g. 'Problem Selection / Idea Submission'."""
    st.markdown(f"""
    <div class="cx-breadcrumb">
        <span class="cx-breadcrumb-muted">{section_label}</span>
        <span class="cx-breadcrumb-sep">/</span>
        <span class="cx-breadcrumb-active">{page_label}</span>
    </div>
    """, unsafe_allow_html=True)
