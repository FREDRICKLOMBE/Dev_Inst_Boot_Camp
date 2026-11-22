# Diabetes Classification | Completed Exercises XP

The notebook follows the six exercises in the supplied Colab template.
All preprocessing is fitted on training data. Positive metrics refer to label 1.

- Source records: 100,000, with 8,500 positives and 91,500 negatives.
- Exact duplicate rows removed before splitting: 3,854.
- Cleaned records: 96,146, with 8,482 positives and 87,664 negatives.
- Stratified 80/20 split: 76,916 training and 19,230 test rows.
- Accuracy: 95.96%, versus always-negative baseline 91.18%.
- Positive-class precision: 86.86%; recall: 63.92%; F1: 0.7364.
- Confusion counts: TN 17,370, FP 164, FN 612, TP 1,084.
- ROC AUC: 0.9598.
- Separate two-feature decision-boundary model accuracy: 95.56%.

This exercise classifies the recorded diabetes label. Future onset has no
defined follow-up window in these data. The probability estimates and intended
use would need further assessment.

Open diabetes_classification.ipynb in Jupyter or upload it to Colab. Keep
diabetes_prediction_dataset.zip beside it. Install numpy, pandas, scikit-learn
and matplotlib before running locally. The course asks you to share the
completed Colab link publicly and paste it into DI Learning after review.
