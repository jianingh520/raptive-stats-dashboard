import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Raptive Brand Guidelines (Updated from Official Site)
# ==========================================
RAPTIVE_PURPLE = "#5A61F5"  # Primary Brand Color (Main Distribution)
RAPTIVE_LIME = "#D5FB70"    # High Highlight (Lime Green)
RAPTIVE_ORANGE = "#F37555"  # Secondary Highlight (Soft Orange)
OFF_WHITE = "#F9F9F7"       # Main Background
CHARCOAL = "#1A1A1A"        # Text

# Page Configuration
st.set_page_config(
    page_title="Raptive | Statistical Property Simulation",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for Premium UI
st.markdown(f"""
    <style>
    .main {{ background-color: {OFF_WHITE}; }}
    h1, h2, h3 {{ color: {CHARCOAL}; font-family: 'Inter', sans-serif; }}
    
    /* Metric Card Styling */
    [data-testid="stMetric"] {{
        background-color: white;
        border-radius: 12px;
        border-left: 5px solid {RAPTIVE_LIME}; /* Use Lime for Highlight */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        padding: 20px;
    }}
    
    /* Sidebar Branding */
    .brand-text {{ 
        color: {RAPTIVE_PURPLE}; 
        font-size: 28px; 
        font-weight: 900; 
        letter-spacing: -1px;
        margin-bottom: 20px; 
    }}
    
    /* Custom Info Box */
    .stAlert {{
        background-color: white;
        border: 1px solid {RAPTIVE_PURPLE};
        border-radius: 8px;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# Sidebar - Interaction Controls
# ==========================================
with st.sidebar:
    st.markdown('<p class="brand-text">RAPTIVE</p>', unsafe_allow_html=True)
    st.title("Simulation Controls")
    st.info("💡 Developed with Codex/Jules to showcase the power of Central Limit Theorem (CLT).")
    
    st.markdown("---")
    dist_choice = st.selectbox(
        "1. Select Population Distribution",
        ["Exponential (Highly Skewed)", "Uniform (Balanced)"]
    )
    
    # Using the orange accent for the sliders via custom theme if needed, 
    # but here we keep standard Streamlit sliders.
    sample_size = st.slider("2. Sample Size (n)", min_value=2, max_value=100, value=30)
    num_simulations = st.slider("3. Number of Trials", min_value=500, max_value=10000, value=2000, step=500)
    
    st.markdown("---")
    st.caption("Raptive Data Science Assessment - Task 2")

# ==========================================
# Statistical Logic (Central Limit Theorem)
# ==========================================
def run_simulation(dist, n, trials):
    means = []
    for _ in range(trials):
        if dist == "Exponential (Highly Skewed)":
            sample = np.random.exponential(1, n)
        else:
            sample = np.random.uniform(0, 1, n)
        means.append(np.mean(sample))
    return np.array(means)

sample_means = run_simulation(dist_choice, sample_size, num_simulations)

# ==========================================
# Main Dashboard UI
# ==========================================
st.title("🎲 Statistical Property: Central Limit Theorem")
st.markdown(f"""
這個工具展示了統計學的核心特性：**不論原始數據分佈如何，只要樣本量 ($n$) 足夠，平均值的分佈都會趨向於正態分佈。**
""")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("Context for Analysis")
    st.write(f"""
    在分析 **4,000 名用戶** 時，即使 **Time on Page** 的原始數據可能極度偏斜，
    我們依然能依賴 CLT 確保迴歸模型的係數 ($t=30.03$) 在統計上是可靠的。
    """)
    
    # Metrics
    st.metric("Total Simulations", f"{num_simulations:,}")
    st.metric("Sample Size (n)", sample_size)
    st.metric("Mean of Means", round(np.mean(sample_means), 3))
    
    # Using the Orange highlight for the result text
    st.markdown(f"""
        <div style="padding:15px; border-radius:8px; border: 1px solid {RAPTIVE_ORANGE}; color:{RAPTIVE_ORANGE}; font-weight:bold;">
        Conclusion: Larger 'n' leads to a more symmetric Normal distribution.
        </div>
    """, unsafe_allow_html=True)

with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(OFF_WHITE)
    
    # Use the Brand Purple for the histogram
    sns.histplot(sample_means, kde=True, color=RAPTIVE_PURPLE, bins=40, ax=ax, alpha=0.8)
    
    ax.set_title(f"Distribution of Sample Means (n={sample_size})", fontsize=15, fontweight='bold', color=CHARCOAL)
    ax.set_xlabel("Mean Value", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_facecolor("white")
    sns.despine()
    
    st.pyplot(fig)

# Footer
st.divider()
st.markdown(
    f"<div style='text-align: center; color: #888;'>© 2024 Raptive Candidate Assessment | Powered by Streamlit & Codex/Jules</div>", 
    unsafe_allow_html=True
)