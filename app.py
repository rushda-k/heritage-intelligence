# ============================================================
# HERITAGE INTELLIGENCE
# Comparative Museum Data Analytics Dashboard
# ============================================================

import re
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Heritage Intelligence",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL DARK THEME
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b1220;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    h1 {
        color: #f8fafc !important;
        font-size: 2.7rem !important;
        font-weight: 700 !important;
    }

    h2 {
        color: #e5e7eb !important;
        font-weight: 650 !important;
        margin-top: 1.8rem !important;
    }

    h3 {
        color: #cbd5e1 !important;
    }

    p {
        color: #cbd5e1;
    }

    [data-testid="stMetric"] {
        background-color: #172033;
        border: 1px solid #2b3a50;
        border-radius: 12px;
        padding: 18px;
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }

    .hero-text {
        color: #aebbcf;
        font-size: 1.05rem;
        line-height: 1.7;
        max-width: 1050px;
    }

    .finding-box {
        background-color: #172033;
        border: 1px solid #29384d;
        border-left: 4px solid #60a5fa;
        border-radius: 9px;
        padding: 14px 18px;
        margin: 9px 0;
        color: #dbe4f0;
        line-height: 1.6;
    }

    .method-box {
        background-color: #111827;
        border: 1px solid #29384d;
        border-radius: 10px;
        padding: 20px;
        color: #cbd5e1;
        line-height: 1.7;
    }

    .section-note {
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: -8px;
        margin-bottom: 15px;
    }

    hr {
        border-color: #29384d !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FILE PATHS
# ============================================================

SCORECARD_PATH = "data/processed/final_scorecard.csv"
GEOGRAPHIC_PATH = "data/processed/geographic_concentration.csv"
COUNTRIES_PATH = "data/processed/top_country_comparison.csv"


# ============================================================
# LOAD ONLY SMALL PROCESSED FILES
# ============================================================

@st.cache_data
def load_data():

    scorecard = pd.read_csv(SCORECARD_PATH)
    geographic = pd.read_csv(GEOGRAPHIC_PATH)
    countries = pd.read_csv(COUNTRIES_PATH)

    return scorecard, geographic, countries


try:
    scorecard_df, geographic_df, countries_df = load_data()

except Exception as error:

    st.error("The dashboard could not load the processed data files.")

    st.write(
        "Please make sure these three files exist inside "
        "`data/processed/`:"
    )

    st.code(
        "final_scorecard.csv\n"
        "geographic_concentration.csv\n"
        "top_country_comparison.csv"
    )

    st.stop()


# ============================================================
# PROJECT VALUES
# ============================================================

SMITHSONIAN = "Smithsonian National Museum of American History"
MET = "The Metropolitan Museum of Art"

smithsonian_objects = 15000
met_objects = 584

smithsonian_score = 53.16
met_score = 40.13

smithsonian_metadata = 47.85
met_metadata = 68.49

smithsonian_digital = 53.31
met_digital = 61.30

smithsonian_artist = 51.77
met_artist = 85.45

smithsonian_culture = 0.64
met_culture = 27.40

smithsonian_country = 34.71
met_country = 16.95

smithsonian_geographies = 175
met_geographies = 18

smithsonian_top5 = 81.19
met_top5 = 76.77


# ============================================================
# HELPER: CLEAN RAW METADATA VALUES
# ============================================================

def clean_metadata_value(value):

    if pd.isna(value):
        return "Unknown"

    text = str(value).strip()

    if not text:
        return "Unknown"

    # Extract content from values such as:
    # [{'label': 'place made', 'content': 'United States'}]
    content_match = re.search(
        r"""['"]content['"]\s*:\s*['"]([^'"]+)['"]""",
        text
    )

    if content_match:
        return content_match.group(1).strip()

    # Extract label if content is unavailable
    label_match = re.search(
        r"""['"]label['"]\s*:\s*['"]([^'"]+)['"]""",
        text
    )

    if label_match:
        return label_match.group(1).strip()

    # Remove common list/dictionary characters
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("{", "")
    text = text.replace("}", "")

    return text.strip()


# ============================================================
# HELPER: FIND COLUMN
# ============================================================

def find_column(df, possible_names):

    for name in possible_names:

        if name in df.columns:
            return name

    return None


# ============================================================
# HEADER
# ============================================================

st.title("🏛️ Heritage Intelligence")

st.markdown(
    """
    <div class="hero-text">

    <b>Comparative Data Intelligence for Cultural Heritage Collections</b>

    <br><br>

    An analytical comparison of the <b>Smithsonian National Museum of
    American History</b> and <b>The Metropolitan Museum of Art</b>,
    examining collection scale, metadata quality, digital accessibility,
    geographic representation, and cultural metadata coverage.

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Dashboard Controls")

selected_museum = st.sidebar.selectbox(
    "Museum View",
    [
        "Both Museums",
        SMITHSONIAN,
        MET
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Project-specific comparative analysis of cultural heritage "
    "collection data."
)


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

st.header("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Objects Analyzed",
        "15,584"
    )

with col2:
    st.metric(
        "Smithsonian Score",
        "53.16 / 100"
    )

with col3:
    st.metric(
        "The Met Score",
        "40.13 / 100"
    )

with col4:
    st.metric(
        "Museums Compared",
        "2"
    )

st.markdown(
    '<div class="section-note">'
    '15,000 Smithsonian records and 584 Met records are represented '
    'in the comparative analysis.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# COLLECTION SCALE
# ============================================================

st.header("Collection Scale")

collection_data = pd.DataFrame(
    {
        "Museum": [
            "Smithsonian NMAH",
            "The Met"
        ],
        "Objects": [
            smithsonian_objects,
            met_objects
        ]
    }
)

st.bar_chart(
    collection_data.set_index("Museum"),
    use_container_width=True
)

st.caption(
    f"The Smithsonian sample is approximately "
    f"{smithsonian_objects / met_objects:.1f}× larger than "
    f"the Met sample."
)


# ============================================================
# METADATA & DIGITAL QUALITY
# ============================================================

st.header("Metadata & Digital Quality")

quality_data = pd.DataFrame(
    {
        "Metric": [
            "Metadata Quality",
            "Digital Accessibility",
            "Artist Metadata",
            "Culture Metadata",
            "Country Metadata"
        ],
        "Smithsonian NMAH": [
            smithsonian_metadata,
            smithsonian_digital,
            smithsonian_artist,
            smithsonian_culture,
            smithsonian_country
        ],
        "The Met": [
            met_metadata,
            met_digital,
            met_artist,
            met_culture,
            met_country
        ]
    }
)

quality_display = quality_data.copy()

quality_display["Smithsonian NMAH"] = quality_display[
    "Smithsonian NMAH"
].map(
    lambda value: f"{value:.2f}%"
)

quality_display["The Met"] = quality_display[
    "The Met"
].map(
    lambda value: f"{value:.2f}%"
)

st.dataframe(
    quality_display,
    use_container_width=True,
    hide_index=True
)

st.bar_chart(
    quality_data.set_index("Metric"),
    use_container_width=True
)


# ============================================================
# GEOGRAPHIC DIVERSITY
# ============================================================

st.header("Geographic Diversity")

geo_display = pd.DataFrame(
    {
        "Measure": [
            "Unique Geographies",
            "Top 5 Geographic Concentration"
        ],
        "Smithsonian NMAH": [
            f"{smithsonian_geographies:,}",
            f"{smithsonian_top5:.2f}%"
        ],
        "The Met": [
            f"{met_geographies:,}",
            f"{met_top5:.2f}%"
        ]
    }
)

st.dataframe(
    geo_display,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Unique geographies indicate the number of standardized geographic "
    "categories represented in the analyzed records. Top-5 concentration "
    "shows the share associated with the five most frequent categories."
)


# ============================================================
# TOP GEOGRAPHIC ORIGINS
# ============================================================

st.header("Top Geographic Origins")

countries_display = countries_df.copy()


# ------------------------------------------------------------
# Museum filtering
# ------------------------------------------------------------

museum_column = find_column(
    countries_display,
    [
        "museum",
        "Museum"
    ]
)

if (
    selected_museum != "Both Museums"
    and museum_column is not None
):

    countries_display = countries_display[
        countries_display[museum_column] == selected_museum
    ].copy()


# ------------------------------------------------------------
# Identify geographic column
# ------------------------------------------------------------

geo_column = find_column(
    countries_display,
    [
        "country",
        "country_standardized",
        "country_name",
        "geography",
        "geographic_origin",
        "place",
        "place_made",
        "location",
        "origin",
        "top_country"
    ]
)


# ------------------------------------------------------------
# Clean geographic values
# ------------------------------------------------------------

if geo_column is not None:

    countries_display[geo_column] = (
        countries_display[geo_column]
        .apply(clean_metadata_value)
    )

    countries_display = countries_display.rename(
        columns={
            geo_column: "Country / Geography"
        }
    )


# ------------------------------------------------------------
# Clean numeric/count columns
# ------------------------------------------------------------

count_column = find_column(
    countries_display,
    [
        "object_count",
        "objects",
        "count",
        "records",
        "frequency",
        "n"
    ]
)

if count_column is not None:

    numeric_counts = pd.to_numeric(
        countries_display[count_column],
        errors="coerce"
    )

    countries_display[count_column] = numeric_counts.map(
        lambda value:
        f"{int(value):,}"
        if pd.notna(value)
        else "—"
    )

    countries_display = countries_display.rename(
        columns={
            count_column: "Objects"
        }
    )


# ------------------------------------------------------------
# Clean percentage/share columns
# ------------------------------------------------------------

share_column = find_column(
    countries_display,
    [
        "share",
        "share_percent",
        "percentage",
        "percent",
        "proportion",
        "percentage_share"
    ]
)

if share_column is not None:

    numeric_share = pd.to_numeric(
        countries_display[share_column],
        errors="coerce"
    )

    countries_display[share_column] = numeric_share.map(
        lambda value:
        f"{value:.2f}%"
        if pd.notna(value)
        else "—"
    )

    countries_display = countries_display.rename(
        columns={
            share_column: "Share"
        }
    )


# ------------------------------------------------------------
# Remove technical columns
# ------------------------------------------------------------

technical_columns = [
    "label",
    "content",
    "field",
    "source",
    "source_field",
    "raw_value",
    "raw",
    "id"
]

countries_display = countries_display.drop(
    columns=[
        column
        for column in technical_columns
        if column in countries_display.columns
    ],
    errors="ignore"
)


# Remove museum column when a specific museum was selected
if (
    selected_museum != "Both Museums"
    and museum_column is not None
    and museum_column in countries_display.columns
):

    countries_display = countries_display.drop(
        columns=[museum_column]
    )


# ------------------------------------------------------------
# Display
# ------------------------------------------------------------

if countries_display.empty:

    st.info(
        "No geographic-origin records are available for this museum view."
    )

else:

    st.dataframe(
        countries_display,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# HERITAGE INTELLIGENCE SCORE
# ============================================================

st.header("Heritage Intelligence Score")

score_data = pd.DataFrame(
    {
        "Museum": [
            "Smithsonian NMAH",
            "The Met"
        ],
        "Score": [
            smithsonian_score,
            met_score
        ]
    }
)

st.bar_chart(
    score_data.set_index("Museum"),
    use_container_width=True
)

score_display = pd.DataFrame(
    {
        "Museum": [
            "Smithsonian NMAH",
            "The Met"
        ],
        "Heritage Intelligence Score": [
            "53.16 / 100",
            "40.13 / 100"
        ]
    }
)

st.dataframe(
    score_display,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# KEY FINDINGS
# ============================================================

st.header("Key Findings")

findings = [
    (
        "Collection Scale",
        "The Smithsonian sample contains 15,000 objects compared "
        "with 584 objects at The Met, making the Smithsonian sample "
        "approximately 25.7× larger."
    ),
    (
        "Metadata Quality",
        "The Met shows stronger metadata completeness in this analysis, "
        "with 68.49% compared with 47.85% for the Smithsonian sample."
    ),
    (
        "Digital Accessibility",
        "The Met has higher digital accessibility in the analyzed "
        "records, at 61.30% compared with 53.31%."
    ),
    (
        "Artist Metadata",
        "Artist metadata coverage is substantially stronger at The Met, "
        "at 85.45% compared with 51.77%."
    ),
    (
        "Culture Metadata",
        "Culture metadata coverage is substantially stronger at The Met, "
        "at 27.40% compared with 0.64%."
    ),
    (
        "Country Metadata",
        "Country metadata coverage is higher in the Smithsonian sample, "
        "at 34.71% compared with 16.95%."
    ),
    (
        "Geographic Representation",
        "The Smithsonian sample contains more standardized geographic "
        "categories in the current analysis: 175 compared with 18."
    ),
    (
        "Geographic Concentration",
        "The top five geographic categories account for 81.19% of "
        "Smithsonian records with geographic data and 76.77% of "
        "the Met records in the corresponding analysis."
    ),
    (
        "Overall Score",
        "The Smithsonian receives the higher Heritage Intelligence Score "
        "because the project framework combines collection scale, "
        "geographic indicators, and metadata-related measures."
    )
]

for title, description in findings:

    st.markdown(
        f"""
        <div class="finding-box">
        <b>{title}</b><br>
        {description}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# METHODOLOGY
# ============================================================

st.divider()

st.header("Methodology")

st.markdown(
    """
    <div class="method-box">

    The Heritage Intelligence framework combines multiple indicators
    to provide a comparative analytical view of two cultural heritage
    datasets.

    <br><br>

    <b>Data sources</b>

    <br>
    • Metropolitan Museum of Art Collection API<br>
    • Smithsonian Open Access / National Museum of American History data

    <br><br>

    <b>Analytical dimensions</b>

    <br>
    • Collection scale<br>
    • Metadata completeness<br>
    • Artist metadata coverage<br>
    • Cultural metadata coverage<br>
    • Country metadata coverage<br>
    • Digital image availability<br>
    • Geographic representation<br>
    • Geographic concentration

    <br><br>

    The Heritage Intelligence Score is a project-specific analytical
    framework created for comparative exploration. It should not be
    interpreted as an official ranking of museum quality.

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA NOTE
# ============================================================

st.divider()

st.subheader("Data Availability")

st.caption(
    "The public dashboard uses the processed analytical outputs "
    "included in this repository. The larger master dataset is "
    "not included in the public repository because of file-size "
    "constraints."
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Heritage Intelligence • Cultural Heritage Data Analytics Project"
)