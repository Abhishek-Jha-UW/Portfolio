from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence

import streamlit as st


@dataclass(frozen=True)
class Project:
    name: str
    url: str
    category: str
    tagline: str
    tags: Sequence[str]


PROJECTS: List[Project] = [
    Project(
        name="Timeseries Forecasting",
        url="https://abhishek-jha-uw-forecasting-app-bu6esr3b9qxhwgkeu6rer7.streamlit.app/",
        category="Forecasting & Revenue",
        tagline="Time series forecasting for demand / revenue planning.",
        tags=("Time Series", "Forecasting", "Python"),
    ),
    Project(
        name="Dynamic Pricing & Elasticity Simulator",
        url="https://dynamic-pricing-elasticity-simulator-m9pycn5tudxyqrevs3spwl.streamlit.app/",
        category="Forecasting & Revenue",
        tagline="Scenario simulation to understand price–demand trade-offs.",
        tags=("Pricing", "Elasticity", "Simulation"),
    ),
    Project(
        name="A/B Testing Experimentation Tool",
        url="https://a-b-testing-experimentation-lqmnpr27pbuqetibd5xdjk.streamlit.app/",
        category="Experimentation & Growth",
        tagline="Statistical testing workflow for product experiments.",
        tags=("Experimentation", "Causal", "Statistics"),
    ),
    Project(
        name="Customer Health & Churn Early Warning System",
        url="https://customer-health-churn-early-warning-system-bwvjzcmbxnmvxgrudsv.streamlit.app/",
        category="Experimentation & Growth",
        tagline="Signals and models to identify churn risk earlier.",
        tags=("Churn", "Classification", "ML"),
    ),
    Project(
        name="Competitive Landscape Mapping",
        url="https://competitive-landscape-mapping-f66enxmzgca3xjuvhzozae.streamlit.app/",
        category="Market Intelligence",
        tagline="LLM-assisted strategic mapping to reveal positioning and whitespace.",
        tags=("LLM", "PCA/MDS", "Strategy"),
    ),
    Project(
        name="GuardianSQL (Data Health & Quality)",
        url="https://guardiansql-xuah5wqluljyfhb5fe9olu.streamlit.app/",
        category="Data Systems",
        tagline="Data quality monitoring for SQL pipelines and checks.",
        tags=("Data Quality", "SQL", "Monitoring"),
    ),
    Project(
        name="Recommendation System",
        url="https://recommendation-system-user-based-collaborative-filtering-b5tvg.streamlit.app/",
        category="Data Systems",
        tagline="User-based collaborative filtering for personalization.",
        tags=("Recommenders", "Collaborative Filtering", "ML"),
    ),
    Project(
        name="Document Q&A Assistant (RAG)",
        url="https://rag-abhi-uw.streamlit.app/",
        category="GenAI",
        tagline="RAG interface for querying documents with semantic retrieval.",
        tags=("RAG", "LLM", "Search"),
    ),
    Project(
        name="CLV vs Bootstrap",
        url="https://clt-vs-bootstrap.streamlit.app/",
        category="Decision Science",
        tagline="Compare CLT intuition vs bootstrap uncertainty, interactively.",
        tags=("Inference", "Bootstrap", "Stats"),
    ),
    Project(
        name="Conjoint Analysis",
        url="https://conjoint-analysis-strategy-assistant.streamlit.app/",
        category="Decision Science",
        tagline="AI-assisted conjoint exploration for attribute trade-offs.",
        tags=("Conjoint", "Pricing", "Strategy"),
    ),
    Project(
        name="Analytics Decision Systems",
        url="https://aanalytics-app-abhishek-jha-uw.streamlit.app/",
        category="Portfolio",
        tagline="Primary portfolio app (legacy / prior hub).",
        tags=("Portfolio", "Landing Page"),
    ),
]


def _inject_css() -> None:
    st.markdown(
        """
<style>
/* Layout breathing room */
.block-container { padding-top: 2.0rem; padding-bottom: 2.5rem; }

/* Sidebar tone */
section[data-testid="stSidebar"] {
  border-right: 1px solid rgba(17,24,39,0.08);
}

/* Headline hierarchy */
h1, h2, h3 { letter-spacing: -0.02em; }

/* Subtle section label */
.ah-section-label {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: rgba(17,24,39,0.60);
  margin: 0.75rem 0 0.35rem 0;
}

/* Card */
.ah-card {
  border: 1px solid rgba(17,24,39,0.10);
  border-radius: 12px;
  background: #fff;
  padding: 18px 18px 14px 18px;
  height: 100%;
}
.ah-card:hover { border-color: rgba(17,24,39,0.35); }
.ah-title { font-size: 1.05rem; font-weight: 700; color: #111827; margin-bottom: 0.25rem; }
.ah-tagline { font-size: 0.90rem; color: rgba(17,24,39,0.72); margin-bottom: 0.65rem; }
.ah-meta { font-size: 0.80rem; color: rgba(17,24,39,0.55); margin-bottom: 0.6rem; }
.ah-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.18rem 0.45rem;
  border-radius: 999px;
  border: 1px solid rgba(17,24,39,0.10);
  background: rgba(17,24,39,0.03);
  margin-right: 0.35rem;
  margin-bottom: 0.35rem;
}

/* Link button: darker, more "product" */
div.stLinkButton > a {
  background-color: #111827 !important;
  color: #ffffff !important;
  border-radius: 10px !important;
  font-weight: 700 !important;
  padding: 0.55rem 0.95rem !important;
  border: 1px solid #111827 !important;
}
div.stLinkButton > a:hover { background-color: #1f2937 !important; border-color: #1f2937 !important; }

/* Reduce extra whitespace around markdown blocks used as components */
div[data-testid="stMarkdownContainer"] > p { margin-bottom: 0.25rem; }
</style>
        """,
        unsafe_allow_html=True,
    )


def _matches_search(p: Project, q: str) -> bool:
    if not q:
        return True
    hay = " ".join([p.name, p.category, p.tagline, " ".join(p.tags)]).lower()
    return q.lower() in hay


def _unique(values: Iterable[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for v in values:
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


def _render_project_card(p: Project) -> None:
    tags_html = "".join([f"<span class='ah-tag'>{t}</span>" for t in p.tags])
    st.markdown(
        f"""
<div class="ah-card">
  <div class="ah-title">{p.name}</div>
  <div class="ah-meta">{p.category}</div>
  <div class="ah-tagline">{p.tagline}</div>
  <div>{tags_html}</div>
</div>
        """.strip(),
        unsafe_allow_html=True,
    )
    st.link_button("Open app", p.url, use_container_width=True)


st.set_page_config(page_title="Analytics Hub | Abhishek Jha", layout="wide")
_inject_css()


with st.sidebar:
    st.markdown("### Abhishek Jha")
    st.caption("Analytics • Decision Science • GenAI")
    st.markdown("---")
    st.markdown("**Links**")
    st.markdown("- [GitHub](https://github.com/Abhishek-Jha-UW)")
    st.markdown("- [LinkedIn](https://www.linkedin.com/)")

    st.markdown("---")
    st.markdown("**How to use**")
    st.caption("Search by keyword, filter by category, then open an app in a new tab.")


st.title("Analytics Hub")
st.write(
    "A curated set of portfolio-grade analytics applications: forecasting, experimentation, pricing, data systems, and GenAI tools."
)


top = st.container()
with top:
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Apps", len(PROJECTS))
    with m2:
        st.metric("Categories", len(set(p.category for p in PROJECTS)))
    with m3:
        st.metric("Focus", "Decision Systems")


st.markdown("<div class='ah-section-label'>Browse</div>", unsafe_allow_html=True)

left, right = st.columns([1.3, 1.0])
with left:
    query = st.text_input("Search", placeholder="Try: pricing, RAG, churn, conjoint…")
with right:
    categories = ["All"] + _unique(p.category for p in PROJECTS)
    category = st.selectbox("Category", options=categories, index=0)


filtered = [
    p
    for p in PROJECTS
    if _matches_search(p, query)
    and (category == "All" or p.category == category)
]

st.caption(f"Showing {len(filtered)} of {len(PROJECTS)} apps.")


if not filtered:
    st.info("No matches. Try a different keyword or switch category.")
else:
    # 2-column grid for a clean professional layout
    for i in range(0, len(filtered), 2):
        row = filtered[i : i + 2]
        cols = st.columns(2)
        for c, p in zip(cols, row):
            with c:
                _render_project_card(p)


st.divider()
st.caption("© 2026 Abhishek Jha • Analytics & Decision Science")

