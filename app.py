import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Titanic: Una Historia de Datos",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

    /* ── Global ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(52, 152, 219, 0.14), transparent 30rem),
            radial-gradient(circle at 85% 15%, rgba(231, 76, 60, 0.12), transparent 28rem),
            linear-gradient(180deg, rgba(13, 27, 42, 0.03) 0%, rgba(255, 255, 255, 0) 22rem);
    }

    .main .block-container {
        padding-top: 1.4rem;
        padding-bottom: 3rem;
        max-width: 1320px;
        animation: fade-in 0.45s ease-out;
    }

    @keyframes fade-in {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1b2a 0%, #1a2744 100%) !important;
        border-right: 1px solid rgba(231, 76, 60, 0.25);
        box-shadow: 12px 0 30px rgba(13, 27, 42, 0.18);
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div {
        color: #cbd5e0 !important;
    }
    [data-testid="stSidebar"] h1 {
        font-family: 'Playfair Display', serif !important;
        color: #ffffff !important;
        letter-spacing: 0.05em;
    }
    [data-testid="stSidebar"] strong {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: rgba(231,76,60,0.3) !important;
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        padding: 0.48rem 0.75rem;
        border-radius: 8px;
        transition: background 0.2s, transform 0.2s, color 0.2s;
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
        background: rgba(231, 76, 60, 0.15);
        color: #fff !important;
        transform: translateX(4px);
    }
    [data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) {
        background: linear-gradient(90deg, rgba(231, 76, 60, 0.34), rgba(52, 152, 219, 0.18));
        box-shadow: inset 3px 0 0 #e74c3c;
    }

    /* ── Metrics ── */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(44,82,130,0.18) 0%, rgba(26,39,68,0.25) 100%);
        border: 1px solid rgba(52, 152, 219, 0.22);
        border-radius: 14px;
        padding: 1rem 1.2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 18px rgba(13, 27, 42, 0.08);
        transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    }
    [data-testid="metric-container"]:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 8px 28px rgba(52, 152, 219, 0.18);
        border-color: rgba(231, 76, 60, 0.32);
    }

    /* ── HR dividers ── */
    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, rgba(231,76,60,0.45), transparent) !important;
        margin: 1.8rem 0 !important;
    }

    /* ── Chapter header ── */
    .chapter-header {
        font-family: 'Playfair Display', serif;
        font-size: 1.95rem;
        font-weight: 700;
        color: var(--text-color);
        border-left: 6px solid #e74c3c;
        padding: 0.5rem 1rem;
        margin: 2rem 0 0.5rem 0;
        background: linear-gradient(90deg, rgba(231,76,60,0.07) 0%, transparent 65%);
        border-radius: 0 10px 10px 0;
        letter-spacing: -0.01em;
        box-shadow: 0 8px 24px rgba(13, 27, 42, 0.06);
    }

    /* ── Insight box ── */
    .insight-box {
        background: linear-gradient(135deg, rgba(52,152,219,0.09) 0%, rgba(52,152,219,0.03) 100%);
        border-left: 5px solid #3498db;
        padding: 1rem 1.4rem;
        border-radius: 0 12px 12px 0;
        margin: 1rem 0 1.5rem 0;
        font-size: 0.96rem;
        color: var(--text-color);
        box-shadow: 0 2px 14px rgba(52,152,219,0.07);
        line-height: 1.75;
        transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    }
    .insight-box:hover {
        transform: translateX(3px);
        border-left-color: #e74c3c;
        box-shadow: 0 8px 24px rgba(52,152,219,0.14);
    }

    /* ── Quote box ── */
    .quote-box {
        background: linear-gradient(135deg, #0d1b2a 0%, #1a2744 100%);
        color: #e2e8f0;
        padding: 2rem 2.5rem;
        border-radius: 16px;
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.2rem;
        margin: 2rem 0;
        text-align: center;
        border: 1px solid rgba(231,76,60,0.2);
        box-shadow: 0 12px 40px rgba(0,0,0,0.28);
        line-height: 1.85;
        position: relative;
        overflow: hidden;
    }
    .quote-box:before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(115deg, transparent 0%, rgba(255,255,255,0.08) 45%, transparent 70%);
        transform: translateX(-120%);
        transition: transform 0.7s ease;
    }
    .quote-box:hover:before {
        transform: translateX(120%);
    }

    /* ── Plotly charts ── */
    [data-testid="stPlotlyChart"] {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(52, 152, 219, 0.14);
        box-shadow: 0 6px 22px rgba(13, 27, 42, 0.12);
        transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
    }
    [data-testid="stPlotlyChart"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 34px rgba(13, 27, 42, 0.2);
        border-color: rgba(231, 76, 60, 0.25);
    }
    [data-testid="stPlotlyChart"] .modebar {
        opacity: 0;
        transition: opacity 0.2s;
    }
    [data-testid="stPlotlyChart"]:hover .modebar {
        opacity: 1;
    }

    /* ── Subheaders ── */
    h2, h3 {
        letter-spacing: -0.02em;
    }
    h1 {
        font-family: 'Playfair Display', serif !important;
        text-shadow: 0 12px 28px rgba(13, 27, 42, 0.12);
    }

    /* ── Tables ── */
    table {
        border-radius: 10px;
        overflow: hidden;
    }
    thead tr th {
        background: rgba(44,82,130,0.25) !important;
    }
    tbody tr:hover td {
        background: rgba(52,152,219,0.06) !important;
    }

    @media (max-width: 760px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        .chapter-header {
            font-size: 1.45rem;
        }
        .quote-box {
            padding: 1.4rem 1.1rem;
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("Titanic-Dataset.csv")
    df["FamilySize"] = df["SibSp"] + df["Parch"]
    df["FamilyGroup"] = df["FamilySize"].apply(
        lambda x: "Solo" if x == 0 else ("Pequeña (1-3)" if x <= 3 else "Grande (4+)")
    )
    df["Clase"] = df["Pclass"].map({1: "Primera Clase", 2: "Segunda Clase", 3: "Tercera Clase"})
    df["Puerto"] = df["Embarked"].map({"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"})
    df["Sexo"] = df["Sex"].map({"male": "Hombre", "female": "Mujer"})
    df["Sobrevivió"] = df["Survived"].map({0: "No", 1: "Sí"})
    return df


df = load_data()

CLASS_COLORS = {"Primera Clase": "#2c3e50", "Segunda Clase": "#2980b9", "Tercera Clase": "#e74c3c"}
CLASS_ORDER = ["Primera Clase", "Segunda Clase", "Tercera Clase"]
SURVIVAL_COLORS = {"Sí": "#2ecc71", "No": "#e74c3c"}
SEX_COLORS = {"Hombre": "#3498db", "Mujer": "#e91e8c"}

PLOTLY_CONFIG = {
    "displaylogo": False,
    "scrollZoom": True,
    "responsive": True,
    "modeBarButtonsToRemove": ["lasso2d", "select2d"],
}

px.defaults.template = "plotly_white"


def render_chart(fig, height=None):
    layout_updates = dict(
        template="plotly_white",
        hovermode="closest",
        margin=dict(l=28, r=24, t=72, b=42),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#f7fafc",
        font=dict(family="Inter, sans-serif", size=13, color="#172033"),
        title=dict(font=dict(family="Playfair Display, serif", size=20, color="#111827"), x=0.02, xanchor="left"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="#172033"),
            bgcolor="rgba(255,255,255,0.92)",
            bordercolor="rgba(52,152,219,0.18)",
            borderwidth=1,
        ),
        transition=dict(duration=450, easing="cubic-in-out"),
    )
    if height is not None:
        layout_updates["height"] = height
    fig.update_layout(**layout_updates)
    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(13,27,42,0.07)",
        linecolor="rgba(13,27,42,0.18)",
        tickfont=dict(color="#172033"),
        title_font=dict(color="#172033"),
        zeroline=False,
        automargin=True,
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(13,27,42,0.07)",
        linecolor="rgba(13,27,42,0.18)",
        tickfont=dict(color="#172033"),
        title_font=dict(color="#172033"),
        zeroline=False,
        automargin=True,
    )
    st.plotly_chart(fig, use_container_width=True, config=PLOTLY_CONFIG)

# ── Sidebar ────────────────────────────────────────────────────────────────────
st.sidebar.title("🚢 Titanic")
st.sidebar.markdown("---")
sections = [
    "🏠  Introducción",
    "👥  I. Perfil de los Pasajeros",
    "💰  II. El Dinero a Bordo",
    "🌊  III. La Noche del Hundimiento",
    "🔗  IV. Patrones y Correlaciones",
    "📊  V. Dashboard Final",
]
selected = st.sidebar.radio("Capítulo:", sections)
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Pasajeros:** {len(df)}  \n**Supervivientes:** {df['Survived'].sum()}  \n**Fallecidos:** {(df['Survived'] == 0).sum()}")

# ══════════════════════════════════════════════════════════════════════════════
# INTRODUCCIÓN
# ══════════════════════════════════════════════════════════════════════════════
if selected == "🏠  Introducción":
    st.markdown("<h1 style='text-align:center; font-size:3.2rem;'>🚢 TITANIC</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.3rem; opacity:0.7;'>Una Historia de Datos &nbsp;·&nbsp; 14–15 de Abril, 1912</p>", unsafe_allow_html=True)
    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Pasajeros registrados", "891")
    c2.metric("Supervivientes", "342", delta="38.4 %")
    c3.metric("Fallecidos", "549", delta="-61.6 %", delta_color="inverse")
    c4.metric("Variables analizadas", "12")

    st.markdown("""
---
### ¿Qué vamos a descubrir?

El **14 de abril de 1912**, el RMS Titanic — considerado insumergible — chocó con un iceberg en el Atlántico Norte
y se hundió en menos de tres horas, llevándose consigo a más de **1 500 personas**.

Pero los datos revelan algo perturbador: **la tragedia no fue aleatoria**.

A lo largo de este análisis exploraremos:

- 👥 ¿**Quiénes** viajaban en el Titanic?
- 💰 ¿Cuánto **pagaron** por sus pasajes y qué revela eso?
- 🌊 ¿Qué **factores** determinaron quién sobrevivió?
- ⚖️ ¿Fue **justa** la distribución del salvamento?

Los números cuentan una historia de **desigualdad social** que se manifestó de forma brutal esa noche.
""")

    st.markdown('<div class="quote-box">"El Titanic no fue solo un naufragio.<br>Fue un espejo de la sociedad de su época."</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CAPÍTULO I
# ══════════════════════════════════════════════════════════════════════════════
elif selected == "👥  I. Perfil de los Pasajeros":
    st.markdown('<div class="chapter-header">Capítulo I: Perfil de los Pasajeros</div>', unsafe_allow_html=True)
    st.markdown("*¿Quiénes eran las personas que abordaron el Titanic?*")

    # ── Pregunta 1: Distribución por clase ────────────────────────────────────
    st.subheader("1. Composición por Clase Social")
    class_counts = df["Clase"].value_counts().reindex(CLASS_ORDER).reset_index()
    class_counts.columns = ["Clase", "Cantidad"]
    class_counts["Porcentaje"] = (class_counts["Cantidad"] / len(df) * 100).round(1)
    class_counts["Label"] = class_counts.apply(lambda r: f"{r['Cantidad']} ({r['Porcentaje']}%)", axis=1)

    fig = px.bar(
        class_counts, x="Clase", y="Cantidad",
        text="Label", color="Clase",
        color_discrete_map=CLASS_COLORS,
        title="Distribución de Pasajeros por Clase Social",
        labels={"Cantidad": "Número de Pasajeros"},
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Número de Pasajeros")
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> El <b>55.1 %</b> de los pasajeros viajaba en Tercera Clase — la mayoría eran emigrantes
y personas de bajos ingresos buscando una nueva vida en América.
Solo el 24.2 % viajaba en Primera Clase.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 2: Distribución de edades ────────────────────────────────────
    st.subheader("2. Distribución de Edades")
    df_age = df.dropna(subset=["Age"])
    mean_age = df_age["Age"].mean()
    median_age = df_age["Age"].median()

    fig = px.histogram(
        df_age, x="Age", nbins=30,
        color_discrete_sequence=["#3498db"],
        title="Distribución de Edades de los Pasajeros",
        labels={"Age": "Edad", "count": "Pasajeros"},
    )
    fig.add_vline(x=mean_age, line_dash="dash", line_color="#e74c3c",
                  annotation_text=f"Media: {mean_age:.1f} años", annotation_position="top right")
    fig.add_vline(x=median_age, line_dash="dot", line_color="#2ecc71",
                  annotation_text=f"Mediana: {median_age:.1f} años", annotation_position="top left")
    fig.update_layout(xaxis_title="Edad", yaxis_title="Número de Pasajeros")
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> La mayoría de los pasajeros tenía entre <b>20 y 35 años</b> — jóvenes adultos en busca de
nuevas oportunidades. Hay un segundo pico para bebés y niños pequeños, reflejo de familias emigrantes.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 3: Edad por clase ─────────────────────────────────────────────
    st.subheader("3. Edad según la Clase Social")
    fig = px.box(
        df_age, x="Clase", y="Age",
        color="Clase",
        color_discrete_map=CLASS_COLORS,
        title="Distribución de Edades por Clase Social (Boxplot)",
        labels={"Age": "Edad", "Clase": ""},
        category_orders={"Clase": CLASS_ORDER},
    )
    fig.update_layout(showlegend=False)
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> Existe una clara <b>estratificación de edad por clase</b>:
Primera Clase (mediana 37 años) — personas económicamente establecidas;
Tercera Clase (mediana 25 años) — jóvenes emigrantes.
La edad refleja el ciclo de vida y la movilidad social de la época.
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CAPÍTULO II
# ══════════════════════════════════════════════════════════════════════════════
elif selected == "💰  II. El Dinero a Bordo":
    st.markdown('<div class="chapter-header">Capítulo II: El Dinero a Bordo</div>', unsafe_allow_html=True)
    st.markdown("*¿Qué tan desiguales eran las fortunas de los pasajeros?*")

    # ── Pregunta 4: Distribución de tarifas ───────────────────────────────────
    st.subheader("4. Distribución de Tarifas de Pasaje")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(df, x="Fare", nbins=50,
                           color_discrete_sequence=["#9b59b6"],
                           title="Escala Lineal",
                           labels={"Fare": "Tarifa (£)", "count": "Pasajeros"})
        fig.add_vline(x=df["Fare"].median(), line_dash="dash", line_color="#e74c3c",
                      annotation_text=f"Mediana: £{df['Fare'].median():.0f}")
        render_chart(fig)
    with col2:
        fare_positive = df.loc[df["Fare"] > 0, "Fare"]
        fare_bins = np.logspace(np.log10(fare_positive.min()), np.log10(fare_positive.max()), 36)
        fare_groups = pd.cut(fare_positive, bins=fare_bins, include_lowest=True)
        fare_log = fare_groups.value_counts(sort=False).reset_index()
        fare_log.columns = ["Rango", "Pasajeros"]
        fare_log["Fare"] = fare_log["Rango"].apply(lambda r: np.sqrt(r.left * r.right))
        fare_log = fare_log[fare_log["Pasajeros"] > 0]
        fig = px.bar(fare_log, x="Fare", y="Pasajeros",
                     log_x=True,
                     color_discrete_sequence=["#e67e22"],
                     title="Escala Logarítmica",
                     labels={"Fare": "Tarifa (£) — log", "Pasajeros": "Pasajeros"})
        fig.update_traces(
            hovertemplate="Tarifa: £%{x:.2f}<br>Pasajeros: %{y}<extra></extra>",
            marker_line_width=0,
        )
        render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> La mediana de las tarifas era <b>£14</b>, pero el máximo llegó a <b>£512</b>.
La distribución extremadamente sesgada revela una enorme <b>desigualdad económica</b> entre los pasajeros.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 5: Tarifa por clase (Violin) ─────────────────────────────────
    st.subheader("5. Estatus Social y Tarifas")
    fig = px.violin(
        df, x="Clase", y="Fare",
        color="Clase", color_discrete_map=CLASS_COLORS,
        box=True, points="outliers",
        title="Distribución de Tarifas por Clase Social (Violin Plot)",
        labels={"Fare": "Tarifa (£)", "Clase": ""},
        category_orders={"Clase": CLASS_ORDER},
    )
    fig.update_layout(showlegend=False)
    render_chart(fig)

    c1, c2, c3 = st.columns(3)
    c1.metric("1ª Clase — promedio", f"£{df[df['Pclass']==1]['Fare'].mean():.0f}")
    c2.metric("2ª Clase — promedio", f"£{df[df['Pclass']==2]['Fare'].mean():.0f}")
    c3.metric("3ª Clase — promedio", f"£{df[df['Pclass']==3]['Fare'].mean():.0f}")

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> El estatus social determinó dramáticamente el precio del pasaje.
La Primera Clase pagó en promedio <b>6× más</b> que la Tercera Clase.
Incluso dentro de la Primera Clase la variación fue enorme: de £25 a £512.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 6: Edad vs Tarifa (Scatter) ──────────────────────────────────
    st.subheader("6. ¿La Edad Determinó la Riqueza?")
    df_scatter = df.dropna(subset=["Age"])
    corr = df_scatter["Age"].corr(df_scatter["Fare"])
    fig = px.scatter(
        df_scatter, x="Age", y="Fare",
        color="Clase", color_discrete_map=CLASS_COLORS,
        opacity=0.6,
        title="Relación entre Edad y Tarifa por Clase Social",
        labels={"Age": "Edad", "Fare": "Tarifa (£)"},
        hover_data=["Name", "Sexo"],
        category_orders={"Clase": CLASS_ORDER},
    )
    fig.add_annotation(text=f"Correlación: {corr:.2f}", xref="paper", yref="paper",
                       x=0.02, y=0.97, showarrow=False,
                       bgcolor="white", bordercolor="gray", borderwidth=1, font=dict(size=13))
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> La correlación entre edad y tarifa es prácticamente nula (<b>0.09</b>).
No era la edad lo que determinaba cuánto pagabas, sino tu <b>clase social de origen</b>.
Las tarifas extremas pertenecen casi exclusivamente a la Primera Clase.
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CAPÍTULO III
# ══════════════════════════════════════════════════════════════════════════════
elif selected == "🌊  III. La Noche del Hundimiento":
    st.markdown('<div class="chapter-header">Capítulo III: La Noche del Hundimiento</div>', unsafe_allow_html=True)
    st.markdown("*¿Qué factores determinaron quién vivía y quién moría?*")

    # ── Pregunta 7: Tasa global ────────────────────────────────────────────────
    st.subheader("7. Tasa Global de Supervivencia")
    surv = df["Sobrevivió"].value_counts().reset_index()
    surv.columns = ["Sobrevivió", "Cantidad"]

    fig = px.pie(
        surv, values="Cantidad", names="Sobrevivió",
        color="Sobrevivió", color_discrete_map=SURVIVAL_COLORS,
        hole=0.42, title="¿Quién Sobrevivió al Titanic?",
    )
    fig.update_traces(textposition="outside", textinfo="percent+label+value")
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> Casi <b>2 de cada 3 pasajeros murió</b> esa noche.
La magnitud de la tragedia (61.6 % de fallecidos) convierte cada análisis posterior en una pregunta
sobre justicia y desigualdad.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 8: Supervivencia por clase ───────────────────────────────────
    st.subheader("8. ¿Importó la Clase Social para Sobrevivir?")
    surv_class = df.groupby(["Clase", "Sobrevivió"]).size().reset_index(name="Cantidad")
    surv_pct = (df.groupby("Clase")["Survived"].mean() * 100).round(1).reset_index()
    surv_pct.columns = ["Clase", "Porcentaje"]

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(
            surv_class, x="Clase", y="Cantidad", color="Sobrevivió",
            barmode="group", color_discrete_map=SURVIVAL_COLORS,
            title="Valores Absolutos",
            labels={"Cantidad": "Pasajeros"},
            category_orders={"Clase": CLASS_ORDER},
        )
        render_chart(fig)
    with col2:
        fig = px.bar(
            surv_pct, x="Clase", y="Porcentaje",
            color="Clase", color_discrete_map=CLASS_COLORS,
            text=surv_pct["Porcentaje"].apply(lambda v: f"{v:.1f}%"),
            title="Tasa de Supervivencia (%)",
            labels={"Porcentaje": "Tasa de Supervivencia (%)"},
            category_orders={"Clase": CLASS_ORDER},
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)
        render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> 1ª Clase: <b>63 %</b> | 2ª Clase: <b>47 %</b> | 3ª Clase: <b>24 %</b>.
Un pasajero de Primera Clase tenía <b>más del doble de probabilidad de sobrevivir</b> que uno de Tercera.
El dinero compró acceso a los botes salvavidas.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 9: Mujeres y niños primero ───────────────────────────────────
    st.subheader("9. El Protocolo «Mujeres y Niños Primero»")
    surv_sex = (df.groupby(["Clase", "Sexo"])["Survived"].mean() * 100).round(1).reset_index()
    surv_sex.columns = ["Clase", "Sexo", "Porcentaje"]
    pivot = surv_sex.pivot(index="Clase", columns="Sexo", values="Porcentaje").reindex(CLASS_ORDER)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(
            surv_sex, x="Clase", y="Porcentaje", color="Sexo",
            barmode="group", color_discrete_map=SEX_COLORS,
            text="Porcentaje",
            title="Supervivencia por Clase y Sexo (%)",
            labels={"Porcentaje": "Tasa de Supervivencia (%)"},
            category_orders={"Clase": CLASS_ORDER},
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        render_chart(fig)
    with col2:
        fig = go.Figure(data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns.tolist(),
            y=pivot.index.tolist(),
            colorscale="RdYlGn",
            text=[[f"{v:.1f}%" for v in row] for row in pivot.values],
            texttemplate="%{text}",
            colorbar=dict(title="% Supervivencia"),
            zmin=0, zmax=100,
        ))
        fig.update_layout(title="Mapa de Calor: Supervivencia por Clase y Sexo",
                          xaxis_title="Sexo", yaxis_title="Clase")
        render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> El protocolo se aplicó de forma <b>desigual</b>:
Mujeres de 1ª Clase: <b>97 %</b> | 2ª Clase: <b>92 %</b> | 3ª Clase: <b>50 %</b> —
cifra similar a los hombres de 1ª Clase (51 %).
Ser mujer ayudaba; ser mujer <em>y rica</em> era lo que realmente salvaba.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 10: Edad y supervivencia ─────────────────────────────────────
    st.subheader("10. ¿La Edad Determinó la Supervivencia?")
    df_age = df.dropna(subset=["Age"]).copy()

    fig = px.histogram(
        df_age, x="Age", color="Sobrevivió",
        barmode="overlay", nbins=25, opacity=0.72,
        color_discrete_map=SURVIVAL_COLORS,
        title="Distribución de Edades: Supervivientes vs. Fallecidos",
        labels={"Age": "Edad", "count": "Pasajeros"},
    )
    render_chart(fig)

    df_age["GrupoEdad"] = pd.cut(
        df_age["Age"],
        bins=[0, 12, 18, 30, 50, 80],
        labels=["Niños (<12)", "Jóvenes (12-18)", "Adultos (18-30)", "Maduros (30-50)", "Mayores (50+)"],
    )
    age_surv = (df_age.groupby("GrupoEdad", observed=True)["Survived"].mean() * 100).round(1).reset_index()
    age_surv.columns = ["GrupoEdad", "Porcentaje"]

    fig = px.bar(
        age_surv, x="GrupoEdad", y="Porcentaje",
        text="Porcentaje",
        color="Porcentaje", color_continuous_scale="RdYlGn",
        title="Tasa de Supervivencia por Grupo de Edad",
        labels={"GrupoEdad": "Grupo de Edad", "Porcentaje": "Tasa de Supervivencia (%)"},
    )
    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> Los niños menores de 12 años tuvieron la mayor tasa de supervivencia (<b>57 %</b>).
Sin embargo, para los adultos el efecto de la clase social dominó claramente sobre el de la edad.
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CAPÍTULO IV
# ══════════════════════════════════════════════════════════════════════════════
elif selected == "🔗  IV. Patrones y Correlaciones":
    st.markdown('<div class="chapter-header">Capítulo IV: Patrones y Correlaciones</div>', unsafe_allow_html=True)
    st.markdown("*¿Qué variables se relacionan entre sí?*")

    # ── Pregunta 11: Heatmap de correlaciones ────────────────────────────────
    st.subheader("11. Correlaciones entre Variables Numéricas")
    num_cols = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
    rename = {"Survived": "Sobrevivió", "Pclass": "Clase", "Age": "Edad",
               "SibSp": "Hermanos/Cónyuge", "Parch": "Padres/Hijos", "Fare": "Tarifa"}
    corr_m = df[num_cols].corr().round(2).rename(index=rename, columns=rename)

    fig = go.Figure(data=go.Heatmap(
        z=corr_m.values,
        x=corr_m.columns.tolist(),
        y=corr_m.index.tolist(),
        colorscale="RdBu", zmid=0, zmin=-1, zmax=1,
        text=corr_m.values,
        texttemplate="%{text:.2f}",
        colorbar=dict(title="Correlación"),
    ))
    fig.update_layout(title="Mapa de Correlaciones entre Variables Numéricas", height=480)
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b>
Clase ↔ Tarifa (<b>−0.55</b>): mayor la clase, más cara la tarifa (inverso por codificación numérica). |
Hermanos ↔ Padres/Hijos (<b>0.41</b>): quienes viajaban con familia tendían a hacerlo en grupos. |
Supervivencia ↔ Clase (<b>−0.34</b>): la clase social es el predictor numérico más fuerte de supervivencia.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 12: Puerto de embarque ───────────────────────────────────────
    st.subheader("12. Puerto de Embarque y Supervivencia")
    df_port = df.dropna(subset=["Puerto"])
    port_class = df_port.groupby(["Puerto", "Clase"]).size().reset_index(name="Cantidad")
    port_pct = (df_port.groupby("Puerto")["Survived"].mean() * 100).round(1).reset_index()
    port_pct.columns = ["Puerto", "Porcentaje"]

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(
            port_class, x="Puerto", y="Cantidad", color="Clase",
            barmode="stack", color_discrete_map=CLASS_COLORS,
            title="Composición por Clase según Puerto",
            labels={"Cantidad": "Pasajeros"},
            category_orders={"Clase": CLASS_ORDER},
        )
        render_chart(fig)
    with col2:
        fig = px.bar(
            port_pct, x="Puerto", y="Porcentaje",
            text="Porcentaje",
            color="Puerto",
            color_discrete_sequence=["#e74c3c", "#3498db", "#2ecc71"],
            title="Tasa de Supervivencia por Puerto (%)",
            labels={"Porcentaje": "Tasa de Supervivencia (%)"},
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig.update_layout(showlegend=False)
        render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> Cherbourg (Francia) tuvo <b>55 %</b> de supervivencia porque embarcó más pasajeros de
Primera Clase. Southampton (Inglaterra) tuvo solo <b>34 %</b> por ser el puerto con más Tercera Clase.
El puerto en sí no salvaba vidas — era la <b>clase social del pasajero</b>.
</div>""", unsafe_allow_html=True)
    st.markdown("---")

    # ── Pregunta 13: Tamaño de familia ────────────────────────────────────────
    st.subheader("13. ¿Ayudó la Familia?")
    fam_surv = (df.groupby("FamilySize")["Survived"].mean() * 100).round(1).reset_index()
    fam_surv.columns = ["TamañoFamilia", "Porcentaje"]
    global_rate = df["Survived"].mean() * 100

    fig = px.line(
        fam_surv, x="TamañoFamilia", y="Porcentaje",
        markers=True, color_discrete_sequence=["#e74c3c"],
        title="Tasa de Supervivencia según Tamaño de Familia",
        labels={"TamañoFamilia": "Tamaño de Familia (SibSp + Parch)", "Porcentaje": "Tasa Supervivencia (%)"},
    )
    fig.add_hline(y=global_rate, line_dash="dash", line_color="gray",
                  annotation_text=f"Media global: {global_rate:.1f}%")
    fig.update_traces(marker=dict(size=10))
    render_chart(fig)

    group_surv = (df.groupby("FamilyGroup")["Survived"].mean() * 100).round(1).reset_index()
    group_surv.columns = ["GrupoFamiliar", "Porcentaje"]
    fig = px.bar(
        group_surv, x="GrupoFamiliar", y="Porcentaje",
        text="Porcentaje",
        color="GrupoFamiliar",
        color_discrete_sequence=["#e74c3c", "#2ecc71", "#f39c12"],
        title="Supervivencia por Tamaño de Grupo Familiar",
        labels={"GrupoFamiliar": "Grupo Familiar", "Porcentaje": "Tasa Supervivencia (%)"},
    )
    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig.update_layout(showlegend=False)
    render_chart(fig)

    st.markdown("""<div class="insight-box">
💡 <b>Hallazgo:</b> Relación no lineal fascinante:
Viajeros solos: <b>30 %</b> | Familias pequeñas (1-3 miembros): <b>55 %</b> (óptimo) |
Familias grandes (4+): <b>16 %</b>.
Las familias pequeñas tenían ventaja por apoyo mutuo; las grandes sufrieron por la
dificultad de reunirse y la escasez de recursos.
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CAPÍTULO V: DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif selected == "📊  V. Dashboard Final":
    st.markdown('<div class="chapter-header">Capítulo V: El Resumen Visual</div>', unsafe_allow_html=True)
    st.markdown("*Toda la historia del Titanic en un solo dashboard interactivo.*")

    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=(
            "Supervivencia Global",
            "Supervivencia por Clase (%)",
            "Protocolo Mujeres y Niños",
            "Edades: Supervivientes vs. Fallecidos",
            "Tarifas por Clase",
            "Tamaño de Familia vs. Supervivencia",
        ),
        specs=[
            [{"type": "pie"}, {"type": "bar"}, {"type": "heatmap"}],
            [{"type": "histogram"}, {"type": "violin"}, {"type": "scatter"}],
        ],
        vertical_spacing=0.14,
        horizontal_spacing=0.08,
    )

    # [0,0] Pie
    sc = df["Survived"].value_counts()
    fig.add_trace(
        go.Pie(labels=["Fallecidos", "Supervivientes"], values=[sc[0], sc[1]],
               marker_colors=["#e74c3c", "#2ecc71"], hole=0.35,
               textinfo="percent+label", showlegend=False),
        row=1, col=1,
    )

    # [0,1] Bar — survival by class
    sp = (df.groupby("Clase")["Survived"].mean() * 100).round(1).reindex(CLASS_ORDER).reset_index()
    sp.columns = ["Clase", "Pct"]
    fig.add_trace(
        go.Bar(x=sp["Clase"], y=sp["Pct"],
               marker_color=["#2c3e50", "#2980b9", "#e74c3c"],
               text=[f"{v:.0f}%" for v in sp["Pct"]], textposition="outside",
               showlegend=False),
        row=1, col=2,
    )

    # [0,2] Heatmap
    hm = (df.groupby(["Clase", "Sexo"])["Survived"].mean() * 100).unstack().reindex(CLASS_ORDER)
    fig.add_trace(
        go.Heatmap(z=hm.values, x=hm.columns.tolist(), y=hm.index.tolist(),
                   colorscale="RdYlGn", showscale=False, zmin=0, zmax=100,
                   text=[[f"{v:.0f}%" for v in row] for row in hm.values],
                   texttemplate="%{text}"),
        row=1, col=3,
    )

    # [1,0] Histogram — age by survival
    df_age = df.dropna(subset=["Age"])
    for val, color, name in [(1, "#2ecc71", "Sí"), (0, "#e74c3c", "No")]:
        fig.add_trace(
            go.Histogram(x=df_age[df_age["Survived"] == val]["Age"],
                         nbinsx=20, opacity=0.65,
                         name=f"Sobrevivió: {name}", marker_color=color,
                         showlegend=(val == 1), legendgroup="survival"),
            row=2, col=1,
        )

    # [1,1] Violin — fare by class
    for clase, color in CLASS_COLORS.items():
        fig.add_trace(
            go.Violin(y=df[df["Clase"] == clase]["Fare"],
                      name=clase, line_color=color,
                      box_visible=True, meanline_visible=True, showlegend=False),
            row=2, col=2,
        )

    # [1,2] Line — family size
    fs = (df.groupby("FamilySize")["Survived"].mean() * 100).reset_index()
    fs.columns = ["TamFam", "Pct"]
    fig.add_trace(
        go.Scatter(x=fs["TamFam"], y=fs["Pct"],
                   mode="lines+markers", line_color="#e74c3c",
                   showlegend=False, marker=dict(size=8)),
        row=2, col=3,
    )

    fig.update_layout(
        height=720,
        title_text="Dashboard Completo: La Historia del Titanic",
        title_font_size=18,
        barmode="overlay",
    )
    render_chart(fig)

    st.markdown("---")
    st.markdown("### Conclusiones Finales")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
**Lo que los datos revelan:**

1. **La clase fue el destino** — Primera Clase tuvo 3× más probabilidad de sobrevivir que Tercera Clase
2. **El dinero compró acceso** — las diferencias en tarifas reflejaron el acceso diferencial a botes salvavidas
3. **El género protegió de forma selectiva** — la prioridad a mujeres se aplicó sobre todo en clases altas
4. **La edad importó en los extremos** — los niños fueron protegidos; los adultos de mediana edad, no tanto
5. **El tamaño familiar importó** — las familias pequeñas tuvieron ventaja; las grandes, desventaja
""")
    with col2:
        st.markdown("""
**Los números clave:**

| Factor | Tasa de Supervivencia |
|--------|-----------------------|
| 1ª Clase | 63 % |
| 2ª Clase | 47 % |
| 3ª Clase | 24 % |
| Mujeres 1ª Clase | 97 % |
| Mujeres 3ª Clase | 50 % |
| Hombres 3ª Clase | 14 % |
| Niños (<12 años) | 57 % |
| Familias pequeñas (1-3) | 55 % |
""")

    st.markdown("""
---
<div class="quote-box">
"El Titanic no fue solo un naufragio. Fue un espejo de la sociedad de su época:<br>
el agua que entró en el barco siguió los mismos caminos que seguía el dinero."
</div>
""", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; opacity:0.6;'>Datos: 891 pasajeros · 12 variables · Abril 1912</p>", unsafe_allow_html=True)
