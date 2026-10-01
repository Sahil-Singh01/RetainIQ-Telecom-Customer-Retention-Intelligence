# Phase 7 Configuration

## Required input

After running `01_business_analysis_dataset_and_intervention_input.ipynb`, edit:

`ease_of_intervention_scores.csv`

Enter an integer from **1 to 5** for every segment.

Interpretation used by the project:

- 1 = harder to intervene on operationally
- 5 = easier to intervene on operationally

The score is subjective and should reflect the business context you want to document.

## Optional geography input

`geography_ease_of_intervention_scores.csv` is created with every state/city market. You may fill a 1–5 score for markets where you have a defensible operational view. If you leave those scores blank, Phase 7 uses revenue-at-risk only for geography prioritization.
