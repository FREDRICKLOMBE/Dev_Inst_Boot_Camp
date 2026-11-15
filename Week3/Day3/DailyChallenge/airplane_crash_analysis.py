"""Run with: python airplane_crash_analysis.py
Dependencies: python -m pip install pandas numpy scipy matplotlib seaborn
Keep the course ZIP beside this script. Outputs are also saved there.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


FOLDER = Path(__file__).resolve().parent
SOURCE = (
    "https://github.com/devtlv/Datasets-DA-Bootcamp-2-/blob/main/"
    "W4%20Gen%20AI/W4D3/Airplane%20Crashes%20and%20Fatalities%20upto%202023.zip"
)


def main():
    # 1. Import the single CSV inside the course ZIP. Pandas treats blanks
    # and NULL as missing. Parse the source dates as month/day/year.
    raw = pd.read_csv(FOLDER / "airplane_crashes.zip", encoding="cp1252")
    crashes = raw.drop_duplicates().copy()
    crashes["Date"] = pd.to_datetime(crashes["Date"], format="%m/%d/%Y", errors="coerce")
    for column in ["Aboard", "Fatalities", "Ground"]:
        counts = pd.to_numeric(crashes[column], errors="coerce")
        crashes[column] = counts.where(counts.ge(0) & counts.mod(1).eq(0))

    # Derive year and decade from valid dates. A row without a valid date can
    # still contribute to the overall totals if its counts are known.
    crashes["Year"] = crashes["Date"].dt.year.astype("Int64")
    crashes["Decade"] = (crashes["Year"] // 10) * 10

    # Calculate onboard survival only when both counts are known and compatible.
    # Ground fatalities are separate because they do not affect onboard survival.
    valid_pair = crashes["Aboard"].gt(0) & crashes["Fatalities"].le(crashes["Aboard"])
    paired = crashes.loc[valid_pair].copy()
    paired["Survivors"] = paired["Aboard"] - paired["Fatalities"]
    paired["Survival rate"] = paired["Survivors"] / paired["Aboard"]

    # 2. Count records by year. Fill gaps with zero recorded crashes so the
    # chart has a regular annual axis, then smooth the counts with a rolling mean.
    annual = crashes.groupby("Year").size()
    annual = annual.reindex(range(int(annual.index.min()), int(annual.index.max()) + 1), fill_value=0)
    annual.index.name = "Year"
    fatality_counts = crashes["Fatalities"].dropna().to_numpy()
    survival_rates = paired["Survival rate"].to_numpy()
    pooled_survival = paired["Survivors"].sum() / paired["Aboard"].sum()

    # 3. Use SciPy for sample standard deviations and medians, and NumPy for
    # means and plot bins. Compare two complete decades using Welch's t-test.
    # H0: Both decades have the same mean onboard fatalities per recorded crash.
    fatalities_1990s = crashes.loc[crashes["Decade"].eq(1990), "Fatalities"].dropna().to_numpy()
    fatalities_2010s = crashes.loc[crashes["Decade"].eq(2010), "Fatalities"].dropna().to_numpy()
    test = stats.ttest_ind(fatalities_1990s, fatalities_2010s, equal_var=False)
    ci = test.confidence_interval(confidence_level=0.95)
    decision = (
        "Reject equal means at the 5% significance level."
        if test.pvalue < 0.05
        else "The comparison gives insufficient evidence of different means at the 5% level."
    )

    # 4. Chart annual crash counts and both outcome distributions. Use a
    # symmetric log scale to show zero fatalities and the long upper tail.
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout="constrained")
    axes[0, 0].plot(annual.index, annual, color="#8aa8ba", label="Annual count")
    axes[0, 0].plot(annual.index, annual.rolling(5, min_periods=1).mean(),
                    color="#124a6b", label="5-year trailing mean")
    axes[0, 0].set(title="Crash records by year", xlabel="Year", ylabel="Recorded crashes")
    axes[0, 0].legend()
    bins = np.r_[0, 1, np.geomspace(2, fatality_counts.max() + 1, 16)]
    axes[0, 1].hist(fatality_counts, bins=bins, color="#287c77", edgecolor="white")
    axes[0, 1].set_xscale("symlog", linthresh=1)
    axes[0, 1].set(title="Onboard fatalities per crash", xlabel="Fatalities (log scale above 1)",
                   ylabel="Recorded crashes")
    sns.histplot(survival_rates, bins=np.linspace(0, 1, 11), ax=axes[1, 0], color="#287c77")
    axes[1, 0].set(title="Onboard survival per crash", xlabel="Share of occupants who survived",
                   ylabel="Recorded crashes", xlim=(0, 1))
    axes[1, 0].xaxis.set_major_formatter(PercentFormatter(1))

    # Show the estimated difference and its uncertainty on the same scale.
    difference = np.mean(fatalities_1990s) - np.mean(fatalities_2010s)
    axes[1, 1].errorbar(difference, 0, xerr=[[difference - ci.low], [ci.high - difference]],
                        fmt="o", capsize=6, color="#124a6b")
    axes[1, 1].axvline(0, color="gray", linestyle="--")
    axes[1, 1].set(title="Difference in mean fatalities (95% CI)",
                   xlabel="Fatalities per crash, 1990s minus 2010s", yticks=[])
    fig.savefig(FOLDER / "airplane_crash_charts.png", dpi=170)
    plt.close(fig)

    # 5. Build the written report from the same calculations used in the charts.
    earlier = annual.loc[1990:1999].sum()
    later = annual.loc[2010:2019].sum()
    report = f"""# Analysis of Airplane Crashes and Fatalities

[Developers Institute course dataset]({SOURCE}) · [Python solution](airplane_crash_analysis.py)

## Data preparation

The source contains {len(raw):,} rows. After removing {len(raw) - len(crashes):,}
exact duplicates, {len(crashes):,} crash records remained, covering
{crashes['Date'].min():%B %d, %Y} through {crashes['Date'].max():%B %d, %Y}.
{crashes['Date'].isna().sum():,} records had an invalid or missing date.
After numeric conversion, {crashes['Aboard'].isna().sum():,} records lacked
a valid onboard count and {crashes['Fatalities'].isna().sum():,} lacked a valid
onboard fatality count. Missing counts were left unknown.
Survival calculations used {len(paired):,} records with positive occupancy
and a known onboard death count no larger than occupancy.

## Exploratory analysis

- **Known onboard fatalities:** {fatality_counts.sum():,.0f} across {len(fatality_counts):,} records with known counts.
- **Known ground fatalities:** {crashes['Ground'].sum():,.0f} across {crashes['Ground'].count():,} records with known ground counts.
- **Known onboard survivors:** {paired['Survivors'].sum():,.0f} out of {paired['Aboard'].sum():,.0f} occupants in records eligible for survival calculations. The pooled onboard survival rate was **{pooled_survival:.1%}**.
- **Peak recorded year:** {annual.idxmax()}, with {annual.max():,} crashes. The dataset contains {earlier:,} records in the 1990s and {later:,} in the 2010s. The last year is partial.

| Outcome | Eligible crashes | Mean | Median | Sample standard deviation |
| --- | ---: | ---: | ---: | ---: |
| Onboard fatalities per crash | {len(fatality_counts):,} | {np.mean(fatality_counts):.2f} | {stats.scoreatpercentile(fatality_counts, 50):.0f} | {stats.tstd(fatality_counts):.2f} |
| Onboard survival rate per crash | {len(survival_rates):,} | {np.mean(survival_rates):.1%} | {stats.scoreatpercentile(survival_rates, 50):.1%} | {100 * stats.tstd(survival_rates):.1f} percentage points |

Recorded crashes rose through the early decades, peaked in 1946, and trended downward after the early 1990s. The five-year trailing average shows the decline beyond year-to-year fluctuations.

The mean fatality count exceeds the median, reflecting a long right tail.
In {np.count_nonzero(survival_rates == 0):,} eligible records nobody aboard
survived. In {np.count_nonzero(survival_rates == 1):,} everyone aboard survived.
The pooled rate gives each occupant equal weight, while the mean of crash-level
rates gives each crash equal weight.

## Hypothesis test

A two-sided Welch t-test compared mean onboard fatalities in the 1990s and
2010s. Those complete decades let us compare earlier and later records without
including the partial 2020s. Welch's test allows different group variances.

- **1990s:** {len(fatalities_1990s):,} crashes with known counts, averaging {np.mean(fatalities_1990s):.2f} fatalities.
- **2010s:** {len(fatalities_2010s):,} crashes with known counts, averaging {np.mean(fatalities_2010s):.2f} fatalities.
- **Difference (1990s minus 2010s):** {difference:.2f} fatalities per crash, with a 95% confidence interval from {ci.low:.2f} to {ci.high:.2f}.
- **Test result:** t = {test.statistic:.3f}, df = {test.df:.1f}, p = {test.pvalue:.4g}. {decision}

The comparison assumes independent records. Extreme crashes can influence
the mean, and missing fatality counts or changing coverage and aircraft mix
can affect comparisons. The dataset gives counts of recorded crashes. Estimating
crash risk over time would also require flight exposure, such as annual departures.

## Visualizations and reproducibility

![Annual crash counts, fatality and survival distributions, and the decade comparison](airplane_crash_charts.png)

Pandas imported and cleaned the CSV and grouped crashes by year and decade.
NumPy calculated means and built plot bins. SciPy calculated medians, sample
standard deviations, and the Welch test with its confidence interval.
Matplotlib and Seaborn generated the charts. Run the linked Python script
with the course ZIP beside it to regenerate this report and its figure.
"""
    (FOLDER / "airplane_crash_report.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
