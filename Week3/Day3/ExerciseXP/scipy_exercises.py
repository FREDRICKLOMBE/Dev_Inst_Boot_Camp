"""Developers Institute | Week 3, Day 3 | SciPy and Basic Statistics.

Install dependencies: python -m pip install numpy scipy matplotlib pandas
Run this solution:    python scipy_exercises.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats


def main():
    # 1. Print the SciPy version installed in this Python environment.
    print(f"Exercise 1 - SciPy version: {scipy.__version__}")

    print("\nExercise 2 - Descriptive statistics")
    data = [12, 15, 13, 12, 18, 20, 22, 21]

    # Treat these observations as a sample. ddof=1 divides by n - 1.
    summary = stats.describe(data, ddof=1)
    print(f"Mean: {summary.mean:.4f}")
    print(f"Median: {stats.scoreatpercentile(data, 50):.4f}")
    print(f"Sample variance: {summary.variance:.4f}")
    print(f"Sample standard deviation: {np.sqrt(summary.variance):.4f}")

    print("\nExercise 3 - Normal distribution")
    # Create the distribution, then evaluate its density on either side of 50.
    distribution = stats.norm(loc=50, scale=10)
    x = np.linspace(10, 90, 401)
    density = distribution.pdf(x)

    # Label both axes and save the plot next to this script.
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    ax.plot(x, density, color="teal", label="Mean = 50, SD = 10")
    ax.axvline(50, color="gray", linestyle="--", linewidth=1)
    ax.set(title="Normal Distribution", xlabel="Value", ylabel="Probability density")
    ax.legend()
    plot_path = Path(__file__).resolve().with_name("normal_distribution.png")
    fig.savefig(plot_path, dpi=160)
    plt.close(fig)
    print(f"Plot saved to {plot_path}")

    print("\nExercise 4 - Independent two-sample t-test")
    # Seed the generator so the same two samples are drawn on each run.
    rng = np.random.default_rng(42)
    data1 = rng.normal(loc=50, scale=10, size=100)
    data2 = rng.normal(loc=60, scale=10, size=100)

    # Welch's two-sided test checks for different population means.
    # It allows the two populations to have different variances.
    alpha = 0.05
    t_test = stats.ttest_ind(data1, data2, equal_var=False)
    print(f"Sample means: {data1.mean():.2f} and {data2.mean():.2f}")
    print(f"t = {t_test.statistic:.4f}, p = {t_test.pvalue:.6g}")
    if t_test.pvalue < alpha:
        print("Reject equal population means at the 5% significance level.")
    else:
        print("Fail to reject equal population means at the 5% significance level.")

    print("\nExercise 5 - Linear regression")
    house_sizes = [50, 70, 80, 100, 120]
    house_prices = [150_000, 200_000, 210_000, 250_000, 280_000]

    # Fit price = intercept + slope * size, then plug in 90 square meters.
    model = stats.linregress(house_sizes, house_prices)
    predicted_price = model.intercept + model.slope * 90
    print(f"Slope: {model.slope:,.2f} currency units per square meter")
    print(f"Intercept: {model.intercept:,.2f} currency units")
    print(f"Predicted price at 90 square meters: {predicted_price:,.2f}")
    print(f"Each extra square meter adds {model.slope:,.2f} units to the fitted price.")

    print("\nExercise 6 - One-way ANOVA")
    fertilizer_1 = [5, 6, 7, 6, 5]
    fertilizer_2 = [7, 8, 7, 9, 8]
    fertilizer_3 = [4, 5, 4, 3, 4]

    # Compare variation between fertilizer groups with variation within them.
    # The null hypothesis says all three population mean growth rates are equal.
    anova = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)
    print(f"F(2, 12) = {anova.statistic:.4f}, p = {anova.pvalue:.8g}")
    if anova.pvalue < alpha:
        print("Reject equal means. At least one fertilizer has a different mean growth.")
        print("A follow-up comparison would be needed to identify which pairs differ.")
    else:
        print("Fail to reject equal means at the 5% significance level.")
    print("If p exceeded 0.05, the data would provide insufficient evidence of a difference.")

    print("\nExercise 7 (optional) - Binomial probabilities")
    # For ten independent fair coin flips, calculate P(X = k) for every k.
    heads = np.arange(11)
    probabilities = stats.binom.pmf(heads, n=10, p=0.5)
    for count, probability in zip(heads, probabilities):
        print(f"Exactly {count:2d} heads: {probability:.6%}")

    print("\nExercise 8 (optional) - Pearson and Spearman correlations")
    people = pd.DataFrame({
        "age": [23, 25, 30, 35, 40],
        "income": [35_000, 40_000, 50_000, 60_000, 70_000],
    })

    # Pearson uses the original values. Spearman compares their ranks.
    pearson, _ = stats.pearsonr(people["age"], people["income"])
    spearman, _ = stats.spearmanr(people["age"], people["income"])
    print(f"Pearson r: {pearson:.6f}")
    print(f"Spearman rho: {spearman:.6f}")
    print("Income rises with every increase in age in this sample, so the ranks match.")


if __name__ == "__main__":
    main()
