# MSL-719: Statistical Analysis & Parametric Distribution Fitting

## 📌 Overview

This repository contains a Python-based pipeline for **statistical analysis, parametric distribution fitting, confidence interval estimation, and statistical visualization**.

This project was developed as an **academic project for the MSL-719 course at the Indian Institute of Technology Delhi (IIT Delhi)**. It applies statistical and computational methods to analyze a synthetically generated dataset and evaluate its fit against multiple theoretical probability distributions.

---

## 🚀 Features

### 1. Synthetic Data Generation

The pipeline generates a synthetic dataset from a **normal distribution** with:

* Mean (`μ`) = 2
* Standard deviation (`σ`) = 1
* Sample size = 100,000

The generated dataset is saved as:

```text
data/MSL-719.csv
```

If the dataset already exists, the pipeline loads the existing CSV instead of generating a new dataset.

---

### 2. Descriptive Statistics

The project calculates the following descriptive statistical measures:

* Mean
* Median
* Coefficient of Variation
* Coefficient of Skewness
* Coefficient of Kurtosis

These statistics provide a quantitative summary of the generated dataset.

---

### 3. Parametric Distribution Fitting with Fitter

The project uses the `Fitter` library to evaluate the dataset against the following probability distributions:

* Gamma
* Rayleigh
* Uniform
* Normal
* Cauchy
* Exponential

The fitting process identifies the best-fitting distribution and reports its location and scale parameters.

---

### 4. Confidence Interval Estimation

The project calculates a confidence interval for the sample mean using the **t-distribution**.

The calculation uses:

* Significance level: `α = 0.05`
* Degrees of freedom: `n - 1`
* Sample standard deviation
* Sample size
* t-critical value
* Margin of error

The resulting interval provides an estimate of the population mean based on the observed sample.

---

### 5. Parametric Modeling with Distfit

The project additionally uses the `distfit` library to evaluate a broader collection of theoretical distributions:

* Normal
* Exponential
* Cauchy
* Gamma
* Beta
* Chi
* t
* f

The best-fitting model identified by `distfit` is reported as part of the final analysis.

---

### 6. Statistical Visualization

The pipeline automatically generates statistical visualizations using `Matplotlib` and `distfit`.

The generated plots include:

* **Probability Density Function (PDF) plots**
* **Cumulative Distribution Function (CDF) plots**
* **Quantile-Quantile (QQ) plots**

The visualizations are saved to the `data/` directory when the program is executed.

---

## 📂 Repository Structure

```text
.
├── src/
│   └── statistical_analysis.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### File Description

* `src/statistical_analysis.py`
  Contains the core statistical functions for data generation, data loading, descriptive statistics, distribution fitting, confidence interval calculation, and visualization.

* `main.py`
  Acts as the main entry point and orchestrates the complete statistical analysis pipeline.

* `requirements.txt`
  Contains the Python dependencies required to run the project.

* `.gitignore`
  Contains files and directories that should not be tracked by Git.

* `README.md`
  Provides documentation for the project.

The generated dataset and visualization files are produced in the `data/` directory during execution and are not part of the tracked repository files.

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

The project's `requirements.txt` currently specifies these six dependencies.

---

## 💻 Installation & Usage

Clone the repository:

```bash
git clone https://github.com/pundhiranshul/Statistical-Distribution-Fitting.git
```

Navigate to the project directory:

```bash
cd Statistical-Distribution-Fitting
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the complete statistical analysis pipeline:

```bash
python main.py
```

The program will:

1. Generate or load the dataset.
2. Calculate descriptive statistics.
3. Fit the data using the `Fitter` library.
4. Calculate the confidence interval for the sample mean.
5. Perform additional parametric modeling using `distfit`.
6. Generate PDF, CDF, and QQ plots.
7. Save the generated dataset and visualizations to the `data/` directory.

---

## 📊 Analysis Workflow

```text
Dataset
   │
   ▼
Generate / Load Data
   │
   ▼
Descriptive Statistics
   │
   ├── Mean
   ├── Median
   ├── Coefficient of Variation
   ├── Skewness
   └── Kurtosis
   │
   ▼
Fitter Distribution Evaluation
   │
   ├── Gamma
   ├── Rayleigh
   ├── Uniform
   ├── Normal
   ├── Cauchy
   └── Exponential
   │
   ▼
Best-Fit Distribution
   │
   ▼
Confidence Interval
   │
   ▼
Distfit Parametric Modeling
   │
   ├── Normal
   ├── Exponential
   ├── Cauchy
   ├── Gamma
   ├── Beta
   ├── Chi
   ├── t
   └── f
   │
   ▼
Statistical Visualization
   │
   ├── PDF
   ├── CDF
   └── QQ Plots
   │
   ▼
Generated Output
```

---

## 🎓 Academic Context

This project was developed as part of the **MSL-719 course at the Indian Institute of Technology Delhi (IIT Delhi)**.

The project demonstrates the practical implementation of statistical concepts including:

* Probability distributions
* Descriptive statistics
* Statistical parameter estimation
* Parametric distribution fitting
* Confidence interval estimation
* Goodness-of-fit analysis
* Statistical visualization

The implementation translates these statistical concepts into an automated Python workflow for computational analysis.

---

## 👥 Project Information

**Course:** MSL-719
**Institution:** Indian Institute of Technology Delhi
**Project Type:** Academic Project
**Project Group:** Group 5

---

## 📄 License

This project is intended primarily for academic and educational purposes.
