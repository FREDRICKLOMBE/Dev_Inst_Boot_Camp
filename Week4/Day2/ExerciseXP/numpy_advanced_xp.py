"""Week 4, Day 2 | NumPy Advanced | Exercises XP.

Install: python -m pip install numpy pandas matplotlib
Run:     python numpy_advanced_xp.py
The script prints the answers and saves both images beside this file.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTPUT_FOLDER = Path(__file__).resolve().parent


def exercise_1():
    """Calculate the determinant and inverse of a 3 x 3 matrix."""
    # Choose a square matrix with a nonzero determinant.
    matrix = np.array([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
    determinant = np.linalg.det(matrix)
    inverse = np.linalg.inv(matrix)

    # Check the inverse by multiplying it by the original matrix.
    is_identity = np.allclose(matrix @ inverse, np.eye(3))
    print(f"\nExercise 1 - Matrix operations\n{matrix}")
    print(f"Determinant: {determinant:.6g}\nInverse:\n{inverse}")
    print(f"Matrix times inverse equals the identity: {is_identity}")


def exercise_2():
    """Summarize 50 random numbers."""
    # Generate 50 uniform values between 0 and 1 with a reproducible seed.
    rng = np.random.default_rng(42)
    values = rng.random(50)

    # Describe the full generated array, so the standard deviation uses ddof=0.
    print("\nExercise 2 - Statistical analysis")
    print(f"Mean: {values.mean():.6f}")
    print(f"Median: {np.median(values):.6f}")
    print(f"Standard deviation: {values.std(ddof=0):.6f}")


def exercise_3():
    """Create every date in January 2023 and format it as YYYY/MM/DD."""
    # NumPy excludes the stop date, so use February 1 to include January 31.
    dates = np.arange("2023-01-01", "2023-02-01", dtype="datetime64[D]")

    # Convert each date to an ISO string, then swap the separators.
    formatted_dates = np.char.replace(np.datetime_as_string(dates, unit="D"), "-", "/")
    print(f"\nExercise 3 - Date manipulation ({dates.size} days)")
    print(formatted_dates)


def exercise_4():
    """Filter a DataFrame and calculate column totals and averages."""
    # Generate a small table with three columns and integer values from 0 to 99.
    rng = np.random.default_rng(43)
    frame = pd.DataFrame(rng.integers(0, 100, size=(6, 3)), columns=["A", "B", "C"])

    # Keep rows where A exceeds 50, then summarize the selected rows by column.
    selected = frame.loc[frame["A"] > 50]
    summary = selected.agg(["sum", "mean"])
    print(f"\nExercise 4 - Data manipulation\n{frame}")
    print(f"\nRows where A > 50:\n{selected}")
    print(f"\nSelected rows: column sums and averages\n{summary}")


def exercise_5():
    """Represent and save a 5 x 5 grayscale image."""
    # In grayscale, each array element is one pixel's brightness.
    # Uint8 stores 0 (black) through 255 (white). RGB adds a third axis
    # with three channels, giving an array shaped (height, width, 3).
    brightness = np.array([0, 64, 128, 192, 255], dtype=np.uint8)
    pixels = np.tile(brightness, (5, 1))

    # Set the full brightness range when mapping pixel values to gray shades.
    plt.imsave(OUTPUT_FOLDER / "grayscale_5x5.png", pixels, cmap="gray", vmin=0, vmax=255)
    print(f"\nExercise 5 - Grayscale pixel array\n{pixels}")


def exercise_6():
    """Use a paired, one-sided t-test to test for improved productivity."""
    # Simulate the same 30 employees before and after training.
    rng = np.random.default_rng(44)
    before = rng.normal(loc=50, scale=10, size=30)
    after = before + rng.normal(loc=5, scale=3, size=30)

    # H0: The population mean change is zero or negative.
    # H1: The population mean change is positive.
    # Pair each employee's scores, then calculate the t statistic with NumPy.
    changes = after - before
    sample_size = changes.size
    mean_change = changes.mean()
    standard_error = changes.std(ddof=1) / np.sqrt(sample_size)
    t_value = mean_change / standard_error

    # At alpha = 0.05, the upper-tail t critical value for 29 df is 1.699127.
    # Using the table value keeps the test calculation in NumPy.
    critical_value = 1.699127
    print("\nExercise 6 - Paired hypothesis test")
    print(f"Mean before: {before.mean():.2f}; mean after: {after.mean():.2f}")
    print(f"Mean paired increase: {mean_change:.2f} points")
    print(f"t({sample_size - 1}) = {t_value:.3f}; critical t = {critical_value:.3f}")
    if t_value > critical_value:
        print("Reject H0 at the 5% level. The simulated scores support improvement.")
    else:
        print("Fail to reject H0 at the 5% level.")
    print("The simulated gains were generated with a positive mean.")


def exercise_7():
    """Compare two arrays element by element."""
    # Equal and smaller values both give False under a strict comparison.
    first = np.array([3, 9, 2, 8, 5])
    second = np.array([4, 7, 2, 3, 6])
    print(f"\nExercise 7 - Element-wise comparison\n{first} > {second}")
    print(first > second)


def exercise_8():
    """Slice a daily time series into the four quarters of 2023."""
    # Make one observation per day and start each slice at a quarter boundary.
    rng = np.random.default_rng(45)
    dates = np.arange("2023-01-01", "2024-01-01", dtype="datetime64[D]")
    values = rng.integers(0, 101, size=dates.size)
    quarter_edges = np.array(
        ["2023-01-01", "2023-04-01", "2023-07-01", "2023-10-01", "2024-01-01"],
        dtype="datetime64[D]",
    )

    # Find the index of each boundary and exclude the next quarter's first day.
    edges = np.searchsorted(dates, quarter_edges)
    print("\nExercise 8 - Quarterly time series slices")
    for quarter, (start, stop) in enumerate(zip(edges[:-1], edges[1:]), start=1):
        quarter_dates = dates[start:stop]
        quarter_values = values[start:stop]
        print(
            f"Q{quarter}: {quarter_dates[0]} to {quarter_dates[-1]} | "
            f"{quarter_values.size} daily observations | first 5: {quarter_values[:5]}"
        )


def exercise_9():
    """Convert an array to a DataFrame and back."""
    # Add column labels in pandas, then recover the underlying numeric values.
    original = np.array([[1, 2, 3], [4, 5, 6]])
    frame = pd.DataFrame(original, columns=["A", "B", "C"])
    restored = frame.to_numpy()
    print(f"\nExercise 9 - Array to DataFrame\n{frame}")
    print(f"\nDataFrame back to array\n{restored}")
    print(f"Values and shape preserved: {np.array_equal(original, restored)}")


def exercise_10():
    """Visualize a NumPy dataset as a line graph."""
    # Generate 20 values and plot them in the order they were drawn.
    rng = np.random.default_rng(46)
    values = rng.random(20)
    observations = np.arange(1, values.size + 1)
    fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
    ax.plot(observations, values, marker="o", color="#146b77")
    ax.set(title="20 Random Values", xlabel="Observation", ylabel="Value", ylim=(0, 1))
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.grid(alpha=0.25)

    # Write the chart to disk so the script also works without a display.
    fig.savefig(OUTPUT_FOLDER / "random_values_line_plot.png", dpi=160)
    plt.close(fig)
    print("\nExercise 10 - Saved random_values_line_plot.png")


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()
