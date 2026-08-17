import os
from src.statistical_analysis import (
    generate_and_save_data,
    load_data,
    descriptive_statistics,
    fit_fitter_distribution,
    calculate_confidence_interval,
    plot_distfit_analysis
)

def main():
    filepath = 'data/MSL-719.csv'
    
    print("="*50)
    print(" STATISTICAL ANALYSIS & DISTRIBUTION FITTING ")
    print("="*50)
    
    # Data pipeline
    if not os.path.exists(filepath):
        data = generate_and_save_data(filepath)
    else:
        print(f"Loading existing data from {filepath}...")
        data = load_data(filepath)
        
    # Question 1: Descriptive Statistics
    print("\n[1] Descriptive Statistics:")
    stats = descriptive_statistics(data)
    for key, val in stats.items():
        print(f"  • {key}: {val:.6f}")
        
    # Questions 2 & 3: Fitter Evaluation
    print("\n[2 & 3] Parametric Distribution Fitting (Fitter):")
    best_dist, loc, scale = fit_fitter_distribution(data)
    print(f"  • Best Fit Distribution: {best_dist}")
    print(f"  • Location (Mean)      : {loc}")
    print(f"  • Scale (Std Dev)      : {scale}")
    
    # Question 4: Confidence Intervals
    print("\n[4] Confidence Interval Calculation (Alpha = 0.05):")
    sample_mean, t_crit, ci = calculate_confidence_interval(data)
    print(f"  • Sample Mean         : {sample_mean:.6f}")
    print(f"  • T-Critical Value    : {t_crit:.6f}")
    print(f"  • Confidence Interval : ({ci[0]:.6f}, {ci[1]:.6f})")
    
    # Advanced Plotting using Distfit
    print("\n[5] Distfit Evaluation & Visualization:")
    best_model = plot_distfit_analysis(data)
    print(f"  • Distfit Best Model: {best_model['name']}")
    
    print("\n" + "="*50)
    print("✅ ANALYSIS COMPLETE")
    print("="*50)

if __name__ == "__main__":
    main()