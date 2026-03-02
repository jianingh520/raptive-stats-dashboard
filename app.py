import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Raptive Brand Guidelines (Official Colors)
# ==========================================
RAPTIVE_PURPLE = "#5A61F5"  # Primary Brand Color
RAPTIVE_LIME = "#D5FB70"    # Highlight (Lime Green)
RAPTIVE_ORANGE = "#F37555"  # Secondary Accent (Soft Orange)
OFF_WHITE = "#F9F9F7"       # Background
CHARCOAL = "#1A1A1A"        # Main Text

# Page Configuration
st.set_page_config(
    page_title="Raptive | Data-Driven Simulation",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for Premium UI and "Fixed" Layout
st.markdown(f"""
    <style>
    /* Prevent vertical scrolling on the main block for a 'Dashboard' feel */
    .main {{ 
        background-color: {OFF_WHITE}; 
        max-height: 100vh;
        overflow: hidden;
    }}
    
    /* Global Text Styles */
    h1, h2, h3 {{ color: {CHARCOAL}; font-family: 'Inter', sans-serif; }}
    
    /* Metric Card Styling */
    [data-testid="stMetric"] {{
        background-color: white;
        border-radius: 12px;
        border-left: 5px solid {RAPTIVE_LIME};
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        padding: 15px;
    }}
    
    /* Sidebar Branding */
    .brand-text {{ 
        color: {RAPTIVE_PURPLE}; 
        font-size: 28px; 
        font-weight: 900; 
        letter-spacing: -1px;
        margin-bottom: 10px; 
    }}
    
    /* Sidebar styling for fixed height */
    section[data-testid="stSidebar"] {{
        background-color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# Sidebar - Interaction Controls
# ==========================================
with st.sidebar:
    st.markdown('<p class="brand-text">RAPTIVE</p>', unsafe_allow_html=True)
    st.title("Analytics Engine")
    st.info("🌟 Developed with Gemini to showcase the power of Central Limit Theorem (CLT).")
    
    st.markdown("---")
    # Selection for Population Distribution
    dist_choice = st.selectbox(
        "1. Select Population Distribution",
        ["Exponential (Highly Skewed)", "Uniform (Balanced)"]
    )
    
    # Sliders - Keep 'n' small for visual clarity, but set trials to 4000
    sample_size = st.slider("2. Sample Size (n)", min_value=2, max_value=100, value=30, help="Number of sessions per sample.")
    num_simulations = st.slider("3. Number of Trials", min_value=500, max_value=5000, value=4000, step=100, help="Matches our 4,000 session dataset.")
    
    st.markdown("---")
    st.caption("Raptive Data Science Assessment - Task 2")

# ==========================================
# Statistical Logic (Central Limit Theorem)
# ==========================================
def run_simulation(dist, n, trials):
    """
    Simulates the CLT by drawing samples and calculating their means.
    """
    means = []
    # Seed for reproducibility
    np.random.seed(42)
    for _ in range(trials):
        if dist == "Exponential (Highly Skewed)":
            sample = np.random.exponential(1.0, n)
        else:
            sample = np.random.uniform(0.0, 1.0, n)
        means.append(np.mean(sample))
    return np.array(means)

# Execute core logic
sample_means = run_simulation(dist_choice, sample_size, num_simulations)

# ==========================================
# Main Dashboard UI
# ==========================================
st.title("📈 Statistical Foundation: Central Limit Theorem")
st.markdown(f"""
This interactive tool demonstrates why our model is reliable. Regardless of initial data skewness, 
the distribution of sample means converges to a **Normal Distribution** as $n$ increases.
""")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("Context for Analysis")
    st.write(f"""
    In our analysis of **4,000 sessions**, the CLT ensures that even if individual **Time on Page** data is extremely skewed, our regression coefficients ($t=30.03$) remain robust and valid.
    """)
    
    # Quantitative Insights
    st.metric("Simulations (Sessions)", f"{num_simulations:,}")
    st.metric("Sample Size (n)", sample_size)
    st.metric("Mean of Sample Means", round(np.mean(sample_means), 3))
    
    # Strategic conclusion with brand accent
    st.markdown(f"""
        <div style="padding:15px; border-radius:8px; border: 1px solid {RAPTIVE_ORANGE}; color:{RAPTIVE_ORANGE}; font-weight:bold; font-size: 0.9em;">
        Insight: Higher 'n' creates a tighter, more symmetric bell curve.
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Visualization using Seaborn and Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor(OFF_WHITE)
    
    # Histogram + Kernel Density Estimate (KDE)
    sns.histplot(sample_means, kde=True, color=RAPTIVE_PURPLE, bins=40, ax=ax, alpha=0.8)
    
    # Styling and Labels
    ax.set_title(f"Sampling Distribution (Trials={num_simulations})", fontsize=14, fontweight='bold', color=CHARCOAL)
    ax.set_xlabel("Sample Mean Value", fontsize=10)
    ax.set_ylabel("Frequency", fontsize=10)
    ax.set_facecolor("white")
    sns.despine()
    
    st.pyplot(fig)

# Footer - Fixed at bottom
st.markdown(
    f"<div style='text-align: center; color: #888; margin-top: 10px; font-size: 0.8em;'>© 2026 Raptive Candidate Assessment | Powered by Streamlit & Gemini</div>", 
    unsafe_allow_html=True
)