# Student-Performance-ML

An end-to-end machine learning project that predicts a student's **math score** from their demographic information and their reading/writing scores, structured as a modular, production-style ML pipeline.

## Dataset

`Notebook/data/stud.csv` — student records with the following fields:

- **Categorical**: `gender`, `race/ethnicity`, `parental level of education`, `lunch`, `test preparation course`
- **Numerical**: `reading score`, `writing score`
- **Target**: `math score`

## Project structure

```
├── Notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb   # exploratory data analysis
│   ├── 2. MODEL TRAINING.ipynb              # notebook-based model experimentation
│   └── data/stud.csv                        # raw dataset
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # reads raw data, splits into train/test, saves to artifact/
│   │   ├── data_transformation.py  # builds preprocessing pipeline (imputation, scaling, one-hot encoding)
│   │   └── model_trainer.py        # trains and evaluates multiple regression models
│   ├── pipelines/
│   │   ├── train_pipeline.py       # orchestrates the training pipeline
│   │   └── predict_pipeline.py     # loads saved artifacts to serve predictions
│   ├── exception.py                 # custom exception handling
│   ├── logger.py                    # centralized logging setup
│   └── utils.py                     # shared helper functions (e.g. save/load objects, model evaluation)
├── artifact/                        # generated train/test splits, preprocessor, and trained model
├── requirements.txt
└── setup.py
```

## How it works

1. **Data ingestion** (`data_ingestion.py`): reads `stud.csv`, saves a raw copy, and splits it into train/test sets (80/20) under `artifact/`.
2. **Data transformation** (`data_transformation.py`): builds a `ColumnTransformer` pipeline — numerical features are median-imputed and scaled (`StandardScaler`), categorical features are mode-imputed, one-hot encoded, and scaled. The fitted preprocessor is saved as `artifact/preprocessor.pkl`.
3. **Model training** (`model_trainer.py`): trains and compares several regressors — `LinearRegression`, `KNeighborsRegressor`, `DecisionTreeRegressor`, `RandomForestRegressor`, `AdaBoostRegressor`, `GradientBoostingRegressor`, `XGBRegressor`, and `CatBoostRegressor` — evaluating with R² score to pick the best-performing model.
4. **Prediction pipeline** (`predict_pipeline.py`): loads the saved preprocessor and trained model to generate predictions on new input.

## Requirements

```
pandas
numpy
seaborn
matplotlib
scikit-learn
xgboost
catboost
dill
```

## Setup & usage

Install the project (and its dependencies) locally:

```bash
pip install -r requirements.txt
pip install -e .
```

Run the full training pipeline (ingestion → transformation → training):

```bash
python -m src.components.data_ingestion
```

Explore the analysis and experimentation notebooks under `Notebook/` for the exploratory data analysis and initial model comparisons.

## Notes

- Logs from each run are written via the custom `logger.py` setup; check the generated log files for pipeline run details.
- `catboost_info/` is CatBoost's own training-log directory, generated automatically during training.
