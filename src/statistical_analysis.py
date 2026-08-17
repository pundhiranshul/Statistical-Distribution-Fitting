import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import skew, variation, kurtosis
from fitter import Fitter
from distfit import distfit

def generate_and_save_data(filepath, mu=2, sigma=1, size=100000):
    """Generates a normal distribution dataset and saves it to a CSV[cite: 14]."""
    print(f"Generating synthetic data (mu={mu}, sigma={sigma}, size={size})...")
    data = np.random.normal(mu, sigma, size)
    df = pd.DataFrame(data, columns=['datapoints'])
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath)
    print(f"Data saved to {filepath}")
    return data

def load_data(filepath):
    """Loads dataset from the specified CSV file[cite: 14]."""
    df = pd.read_csv(filepath, index_col=0)
    return df['datapoints'].values

def descriptive_statistics(data):
    """Calculates mean, median, CV, skewness, and kurtosis[cite: 14]."""
    return {
        'Mean': np.mean(data),
        'Median': np.median(data),
        'Coefficient of Variation': variation(data),
        'Coefficient of Skewness': skew(data),
        'Coefficient of Kurtosis': kurtosis(data)
    }

def fit_fitter_distribution(data):
    """Uses the Fitter library to evaluate parametric distributions[cite: 14]."""
    print("\nFitting distributions using Fitter...")
    f = Fitter(data, distributions=["gamma", "rayleigh", "uniform", "norm", "cauchy", "expon"])
    f.fit()
    
    best_dist = f.get_best()
    dist_name = list(best_dist.keys())[0]
    loc = best_dist[dist_name].get('loc', 'N/A')
    scale = best_dist[dist_name].get('scale', 'N/A')
    
    return dist_name, loc, scale

def calculate_confidence_interval(data, alpha=0.05):
    """Calculates the confidence interval for the sample mean using a t-distribution[cite: 14]."""
    sample_mean = data.mean()
    sample_std = np.std(data, ddof=1)
    sample_size = len(data)
    
    degrees_of_freedom = sample_size - 1
    t_critical = stats.t.ppf(alpha / 2, df=degrees_of_freedom)
    margin_of_error = -t_critical * (sample_std / np.sqrt(sample_size))
    
    ci_lower = sample_mean - margin_of_error
    ci_upper = sample_mean + margin_of_error
    
    return sample_mean, t_critical, (ci_lower, ci_upper)

def plot_distfit_analysis(data):
    """Uses distfit to evaluate theoretical distributions and plot PDF/CDF/QQ plots[cite: 14]."""
    print("\nInitializing Distfit parametric modeling...")
    dfit = distfit(method='parametric', todf=True, distr=['norm', 'expon', 'cauchy', 'gamma', 'beta', 'chi', 't', 'f'])
    dfit.fit_transform(data)
    
    print("\nGenerating and saving plots...")
    
    # PDF and CDF Plot
    fig, ax = plt.subplots(1, 2, figsize=(20, 8))
    dfit.plot(chart='PDF', n_top=11, ax=ax[0])
    dfit.plot(chart='CDF', n_top=11, ax=ax[1])
    plt.savefig("data/distfit_pdf_cdf_plot.png")
    plt.close()

    # QQ Plot
    fig, ax = plt.subplots(1, 2, figsize=(18, 4))
    dfit.qqplot(data, ax=ax[0])
    dfit.qqplot(data, n_top=11, ax=ax[1])
    plt.savefig("data/distfit_qq_plot.png")
    plt.close()
    
    print("Plots saved successfully to the 'data/' directory.")
    return dfit.model