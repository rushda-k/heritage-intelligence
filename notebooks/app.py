# ============================================================
# HERITAGE INTELLIGENCE
# Interactive Museum Data Analytics Dashboard
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heritage Intelligence",
    page_icon="🏛️",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    master = pd.read_csv(
        "data/processed/heritage_master_dataset.csv"
    )

    scorecard = pd.read_csv(
        "data/processed/final_scorecard.csv"
    )

    geographic = pd.read_csv(
        "data/processed/geographic_concentration.csv"
    )

    countries = pd.read_csv(
        "data/processed/top_country_comparison.csv"
    )

    return master, scorecard, geographic, countries


master_df, scorecard_df, geographic_df, countries_df = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("🏛️ Heritage Intelligence")

st.markdown(
    """
    ### Comparative Data Intelligence for Cultural Heritage Collections

    An analytical comparison of the **Smithsonian National Museum of
    American History** and **The Metropolitan Museum of Art**, examining
    metadata quality, digital accessibility, geographic diversity,
    cultural representation, and collection scale.
    """
)


st.divider()


# ============================================================
# SCORECARD
# ============================================================

st.header("📊 Executive Overview")

col1, col2, col3, col4 = st.columns(4)

smithsonian_objects = 15000
met_objects = 584

smithsonian_score = 53.16
met_score = 40.13

smithsonian_metadata = 47.85
met_metadata = 68.49

smithsonian_digital = 53.31
met_digital = 61.30


with col1:
    st.metric(
        "Objects Analyzed",
        "15,584"
    )

with col2:
    st.metric(
        "Smithsonian Score",
        f"{smithsonian_score}/100"
    )

with col3:
    st.metric(
        "The Met Score",
        f"{met_score}/100"
    )

with col4:
    st.metric(
        "Museums Compared",
        "2"
    )


st.divider()


# ============================================================
# MUSEUM SELECTOR
# ============================================================

st.sidebar.header("Dashboard Controls")

museum_options = [
    "Both Museums",
    "Smithsonian National Museum of American History",
    "The Metropolitan Museum of Art"
]

selected_museum = st.sidebar.selectbox(
    "Select Museum",
    museum_options
)


# ============================================================
# COLLECTION COMPARISON
# ============================================================

st.header("📦 Collection Scale")

collection_data = pd.DataFrame({
    "Museum": [
        "Smithsonian NMAH",
        "The Met"
    ],
    "Objects": [
        smithsonian_objects,
        met_objects
    ]
})

st.bar_chart(
    collection_data.set_index("Museum")
)

st.caption(
    "The Smithsonian sample is approximately "
    f"{smithsonian_objects / met_objects:.1f}× larger than the Met sample."
)


# ============================================================
# QUALITY COMPARISON
# ============================================================

st.header("🔎 Metadata & Digital Quality")

quality_data = pd.DataFrame({
    "Metric": [
        "Metadata Quality",
        "Digital Accessibility",
        "Artist Coverage",
        "Culture Coverage",
        "Country Coverage"
    ],

    "Smithsonian NMAH": [
        47.85,
        53.31,
        51.77,
        0.64,
        34.71
    ],

    "The Met": [
        68.49,
        61.30,
        85.45,
        27.40,
        16.95
    ]
})

st.dataframe(
    quality_data,
    use_container_width=True,
    hide_index=True
)


st.bar_chart(
    quality_data.set_index("Metric")
)


# ============================================================
# GEOGRAPHIC DIVERSITY
# ============================================================

st.header("🌍 Geographic Diversity")

geo_display = geographic_df.copy()

geo_display = geo_display.rename(
    columns={
        "top_1_share": "Top 1 (%)",
        "top_3_share": "Top 3 (%)",
        "top_5_share": "Top 5 (%)",
        "top_10_share": "Top 10 (%)"
    }
)

st.dataframe(
    geo_display,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# TOP COUNTRIES
# ============================================================

st.header("🌎 Top Geographic Origins")

if selected_museum == "Both Museums":

    st.dataframe(
        countries_df,
        use_container_width=True,
        hide_index=True
    )

else:

    filtered_countries = countries_df[
        countries_df["museum"] == selected_museum
    ]

    st.dataframe(
        filtered_countries,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FINAL SCORECARD
# ============================================================

st.header("🏆 Heritage Intelligence Score")

score_data = pd.DataFrame({
    "Museum": [
        "Smithsonian NMAH",
        "The Met"
    ],
    "Score": [
        smithsonian_score,
        met_score
    ]
})

st.bar_chart(
    score_data.set_index("Museum")
)

st.dataframe(
    scorecard_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# KEY FINDINGS
# ============================================================

st.header("💡 Key Findings")

findings = [
    "The Smithsonian dataset contains substantially more objects, providing greater collection scale.",
    
    "The Met demonstrates stronger overall metadata completeness.",
    
    "The Met has higher digital image availability.",
    
    "Artist metadata coverage is substantially stronger at The Met.",
    
    "Culture metadata coverage is substantially stronger at The Met.",
    
    "The Smithsonian provides much broader geographic representation.",
    
    "The Smithsonian has greater geographic concentration around the United States.",
    
    "The final Heritage Intelligence Score is higher for the Smithsonian because the scoring framework rewards collection scale and geographic breadth alongside metadata quality."
]

for finding in findings:

    st.markdown(
        f"• {finding}"
    )


# ============================================================
# METHODOLOGY
# ============================================================

st.divider()

st.header("📐 Methodology")

st.markdown(
    """
    The analysis combines collection-scale, metadata-quality,
    digital-accessibility, and geographic indicators into a
    comparative Heritage Intelligence framework.

    **Data sources**

    • Metropolitan Museum of Art Collection API  
    • Smithsonian Open Access / NMAH collection data

    **Core dimensions**

    • Collection scale  
    • Metadata completeness  
    • Artist metadata  
    • Cultural metadata  
    • Country/geographic metadata  
    • Digital image availability  
    • Geographic diversity  
    • Geographic concentration

    The resulting Heritage Intelligence Score provides a
    comparative analytical framework rather than a universal
    ranking of museum quality.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Heritage Intelligence • Cultural Heritage Data Analytics Project"
)