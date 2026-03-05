# Statistical Property Dashboard
## Live Demo
👉 [Dashboard](https://raptive-stats-dashboard.streamlit.app/#statistical-property-central-limit-theorem)

## Project Overview
This interactive dashboard is a supplementary tool developed for the Raptive Data Science assessment. It is designed to demonstrate the **Central Limit Theorem** (CLT)—a fundamental statistical property that explains why our linear regression models remain robust and valid even when dealing with highly skewed user engagement data.

## Key Features
- **Dynamic Distribution Simulation**: Users can choose between Exponential (highly skewed, reflecting raw user behavior) or Uniform distributions.
- **Interactive Parameters**: Real-time adjustment of Sample Size (n) and Number of Trials to visualize how sample means converge toward a Normal (Gaussian) distribution.
- **Analytical Context**: Directly connects the simulation to the Task 1 dataset (4,000 sessions), bridging the gap between statistical theory and practical business insights.

## Tech Stack
- **Streamlit**: Web interface and interactivity.
- **Numpy**: Numerical computing and statistical simulation.
- **Matplotlib & Seaborn**: data visualization.

## File Structure
- **app.py**: The main Streamlit application logic.
- **requirements.txt**: List of Python dependencies for deployment.

Developed as part of the Raptive Candidate Assessment - 2026
