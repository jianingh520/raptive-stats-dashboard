import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Raptive Visual Identity (Design Tokens)
# ==========================================
RAPTIVE_GREEN = "#00A38D"  # Signature Brand Green
OFF_WHITE = "#F9F9F7"      # Background Off-white
CHARCOAL = "#1A1A1A"       # Deep Charcoal Text

# Page Configuration
st.set_page_config(
    page_title="Raptive | Statistical Property Simulation",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for a Premium UI
st.markdown(f"""
    <style>
    .main {{ background-color: {OFF_WHITE}; }}
    h1, h2, h3 {{ color: {CHARCOAL}; font-family: 'Inter', sans-serif; }}
    .stMetric {{ background-color: white; border-radius: 8px; border: 1px solid #E5E5E1; padding: 15px; }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# Sidebar - Interactive Controls
# ==========================================
with st.sidebar:
    # Official Raptive Logo
    st.image("https://raptive.com/wp-content/uploads/2023/04/Raptive_Logo_RGB_Green.svg", width=160)
    st.title("Simulation Controls")
    st.info("💡 Developed in collaboration with Codex/Jules bots to demonstrate the Central Limit Theorem (CLT).")
    
    st.markdown("---")
    # User-selectable distributions
    dist_choice = st.selectbox(
        "1. Select Population Distribution",
        ["Exponential (Highly Skewed)", "Uniform (Balanced)"]
    )
    
    # Sliders for n-size and trials
    sample_size = st.slider("2. Sample Size (n)", min_value=2, max_value=100, value=30)
    num_simulations = st.slider("3. Number of Trials", min_value=500, max_value=10000, value=2000, step=500)
    
    st.markdown("---")
    st.caption("Raptive Data Science Assessment - Task 2")

# ==========================================
# Statistical Logic (Central Limit Theorem)
# ==========================================
def run_simulation(dist, n, trials):
    """
    Simulates the CLT by calculating sample means over multiple trials.
    """
    means = []
    for _ in range(trials):
        if dist == "Exponential (Highly Skewed)":
            # Represents highly skewed raw data (similar to raw web engagement logs)
            sample = np.random.exponential(1, n)
        else:
            # Represents a balanced/flat distribution
            sample = np.random.uniform(0, 1, n)
        means.append(np.mean(sample))
    return np.array(means)

# Execute simulation
sample_means = run_simulation(dist_choice, sample_size, num_simulations)

# ==========================================
# Main Dashboard UI
# ==========================================
st.title("🎲 Statistical Property: Central Limit Theorem")
st.markdown(f"""
This interactive tool demonstrates a fundamental statistical principle: **Regardless of the underlying population distribution, 
the distribution of sample means converges to a Normal Distribution as the sample size ($n$) increases.**
""")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("Context for Analysis")
    st.write(f"""
    In our analysis of **4,000 users**, the CLT allows us to trust that our regression coefficients 
    (such as the **+9.71e-05** for Time on Page) are robust and statistically significant ($t=30.03$).
    """)
    
    # Metric cards
    st.metric("Total Simulations Run", f"{num_simulations:,}")
    st.metric("Sample Size (n)", sample_size)
    st.metric("Mean of Sample Means", round(np.mean(sample_means), 3))
    
    st.success("Conclusion: A larger 'n' leads to a more symmetric (Normal) distribution of means.")

with col2:
    # Visualization using Seaborn & Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(OFF_WHITE)
    
    # Histogram + Kernel Density Estimate (KDE)
    sns.histplot(sample_means, kde=True, color=RAPTIVE_GREEN, bins=40, ax=ax, alpha=0.7)
    
    # Chart styling
    ax.set_title(f"Distribution of Sample Means (n={sample_size})", fontsize=15, fontweight='bold', color=CHARCOAL)
    ax.set_xlabel("Mean Value", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_facecolor("white")
    sns.despine()
    
    st.pyplot(fig)

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center; color: #888;'>© 2024 Raptive Candidate Assessment | Powered by Streamlit & Codex/Jules</div>", 
    unsafe_allow_html=True
)