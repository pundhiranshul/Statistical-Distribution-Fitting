````markdown
# MSL-719: Statistical Analysis & Parametric Distribution Fitting

## 📌 Overview

This repository contains a comprehensive, automated pipeline for statistical analysis, parametric distribution modeling, and data visualization.

This project was developed as an **academic project for the MSL-719 course at the Indian Institute of Technology Delhi (IIT Delhi)**. It demonstrates the application of statistical methods, probability distributions, descriptive statistics, confidence interval estimation, and programmatic data analysis using Python.

---

## 🚀 Core Capabilities

### 1. Descriptive Statistics

The project calculates key statistical measures, including:

- Mean
- Median
- Coefficient of Variation
- Coefficient of Skewness
- Coefficient of Kurtosis

These metrics provide a statistical summary of the generated or supplied datasets.

### 2. Parametric Distribution Fitting

The pipeline evaluates datasets against multiple theoretical probability distributions to identify suitable statistical models.

#### Fitter Evaluation

The following distributions are evaluated using the `fitter` library:

- Gamma
- Rayleigh
- Uniform
- Normal
- Cauchy
- Exponential

The best-fitting distribution is identified based on the **sum of squared errors (SSE)**.

#### Distfit Modeling

The project also uses the `distfit` library for parametric distribution modeling across a broader collection of probability distributions, including:

- Beta
- Chi
- t
- f
- Normal
- Exponential
- Gamma
- Uniform
- and other supported distributions

### 3. Confidence Interval Calculation

The project programmatically calculates the confidence interval for the population mean using the **t-distribution**.

For a standard 95% confidence level:

- Significance level: `α = 0.05`
- Degrees of freedom: `n - 1`
- Critical value: `t_(α/2, n-1)`
- Margin of error is calculated from the sample standard deviation and sample size.

The resulting interval provides an estimate of the range in which the population mean is expected to lie.

### 4. Automated Visualization

The pipeline automatically generates statistical visualizations and saves them as PNG files.

Generated visualizations include:

- **Probability Density Function (PDF) plots**
- **Cumulative Distribution Function (CDF) plots**
- **Histogram-based distribution comparisons**
- **Quantile-Quantile (QQ) plots**
- **Goodness-of-fit visualizations**

These plots provide a visual assessment of how closely the observed data follows the selected theoretical distributions.

---

## 📂 Repository Structure

```text
.
├── src/
│   └── statistical_analysis.py
│
├── data/
│   ├── *.csv
│   └── *.png
│
├── main.py
├── requirements.txt
└── README.md
````

### File Description

* `src/statistical_analysis.py`
  Contains the core statistical functions for data generation, descriptive analysis, distribution fitting, confidence interval calculation, and visualization.

* `data/`
  Contains datasets and automatically generated statistical visualization outputs.

* `main.py`
  Entry point that orchestrates the complete statistical analysis pipeline and produces the final analytical output.

* `requirements.txt`
  Lists the Python dependencies required to run the project.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Statistical Computing

* NumPy
* SciPy
* Fitter
* Distfit

### Data Processing

* Pandas

### Visualization

* Matplotlib

---

## 💻 Installation & Usage

Clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the complete statistical analysis pipeline:

```bash
python main.py
```

The program will perform the statistical analysis and generate the corresponding visualization files automatically.

---

## 📊 Analysis Workflow

The overall workflow can be summarized as:

```text
Dataset
   │
   ▼
Data Generation / Loading
   │
   ▼
Descriptive Statistical Analysis
   │
   ├── Mean
   ├── Median
   ├── Coefficient of Variation
   ├── Skewness
   └── Kurtosis
   │
   ▼
Parametric Distribution Fitting
   │
   ├── Fitter
   └── Distfit
   │
   ▼
Best-Fit Distribution Selection
   │
   ▼
Confidence Interval Estimation
   │
   ▼
Statistical Visualization
   │
   ├── PDF
   ├── CDF
   └── QQ-Plots
   │
   ▼
PNG Output
```

---

## 🎓 Academic Context

This project was developed as part of **MSL-719 at the Indian Institute of Technology Delhi (IIT Delhi)**.

The work focuses on applying statistical theory and computational methods to practical data analysis problems, with particular emphasis on:

* Probability distributions
* Statistical parameter estimation
* Descriptive statistics
* Distribution fitting
* Confidence intervals
* Goodness-of-fit analysis
* Statistical visualization

The implementation demonstrates how these mathematical and statistical concepts can be translated into an automated Python-based analytical workflow.

---

## 👥 Project Information

**Course:** MSL-719
**Institution:** Indian Institute of Technology Delhi
**Project Type:** Academic Project
**Project Group:** Group 5

---

## 📄 License

This project is intended primarily for academic and educational purposes.

```
```
