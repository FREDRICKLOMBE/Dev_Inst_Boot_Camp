# Global Power Plants | NumPy, Pandas and Matplotlib

This project answers all seven tasks in the NumPy Advanced Daily Challenge.
Open [the executed Jupyter notebook](global_power_plants.ipynb) for the code,
tables, figures, and explanations. Data source: [World Resources Institute,
Global Power Plant Database v1.3.0](https://datasets.wri.org/dataset/globalpowerplantdatabase), licensed CC BY 4.0.

## Findings

- The cleaned inventory contains **34,936 plants**.
  **United States of America** has the most records (9,833),
  and **Solar** is the most common primary fuel (10,665 plants).
- **2019** has the most usable observed generation records
  (9,659, or 27.6% of listed plants).
  Coal averaged **3,325.5 GWh** and gas averaged **890.2 GWh** per reporting plant.
  The coal-minus-gas difference was **2,435.2 GWh** (95% CI
  1,997.7 to 2,872.8 GWh, Welch p = 9.012e-24).
  Reject equal means at the 5% level.
- Solar and wind together represented **0.5%** of recorded
  capacity for plants commissioned in the 1990s and **12.8%**
  for the 2010s cohort. Commissioning year was available for 49.9%
  of listed plants, and the cohort comparison reflects recorded capacity.
- The first principal component explains **41.1%** of variance
  in the chosen feature matrix. Its largest absolute weights were
  Commissioning year, Log capacity, Solar. The eigenvector describes how the features vary
  together, and its eigenvalue measures variation along that direction.
  In this dataset, the weights associate later commissioning and solar
  with smaller installed capacity along that component.

[View the four charts](power_plant_charts.png)

The generation comparison applies to reporting plants. Size, geography and
reporting coverage may differ by fuel, so the result is descriptive.
The database is a versioned snapshot and the commissioning cohorts are
historical groups of plants represented in that snapshot.

## Reproduce locally

Keep the bundled WRI ZIP beside the notebook. Install
`jupyter numpy pandas scipy matplotlib seaborn` with pip, open the notebook
in Jupyter, and run all cells. The notebook regenerates the chart and README.
