import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

CLEANED_DATA_PATH = "data/cleaned/final_cleaned_data.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "best_model.joblib")

def load_data():
  """Load the cleaned dataset used for modeling."""
  df = pd.read_csv(CLEANED_DATA_PATH)

  # Remove rows where target (prevalence_focus) is missing
  df = df.dropna(subset=["prevalence_focus"])

  return df

def get_feature_target(df: pd.DataFrame):
  """
  Select features and target for the regression model.

  Target:
      prevalence_focus  (smoking prevalence % for the focus group)

  Features:
      year, state, demographic_type, comparing_focus_group
  """
  feature_cols = ["year", "state", "demographic_type", "comparing_focus_group"]
  target_col = "prevalence_focus"

  X = df[feature_cols].copy()
  y = df[target_col].copy()
  return X, y

def build_preprocessor():
  """Build a ColumnTransformer to handle numeric and categorical features."""
  numeric_features = ["year"]
  categorical_features = ["state", "demographic_type", "comparing_focus_group"]

  numeric_transformer = "passthrough"
  categorical_transformer = OneHotEncoder(handle_unknown="ignore")

  preprocessor = ColumnTransformer(
      transformers=[
          ("num", numeric_transformer, numeric_features),
          ("cat", categorical_transformer, categorical_features),
      ]
  )

  return preprocessor

def train_models():
  """
  Train two models:
    - Linear Regression
    - Random Forest Regressor

  Compare their MAE and R², select the best model based on MAE.
  Save the best as a sklearn Pipeline (preprocessor + estimator).
  """
  df = load_data()
  X, y = get_feature_target(df)
  preprocessor = build_preprocessor()

  X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
  )

  # ----- Model 1: Linear Regression -----
  lin_reg_pipeline = Pipeline(
    steps=[
      ("preprocessor", preprocessor),
      ("model", LinearRegression()),
    ]
  )

  lin_reg_pipeline.fit(X_train, y_train)
  y_pred_lin = lin_reg_pipeline.predict(X_test)
  mae_lin = mean_absolute_error(y_test, y_pred_lin)
  r2_lin = r2_score(y_test, y_pred_lin)

  # ----- Model 2: Random Forest Regressor -----
  rf_pipeline = Pipeline(
    steps=[
      ("preprocessor", preprocessor),
      ("model", RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
      )),
    ]
  )

  rf_pipeline.fit(X_train, y_train)
  y_pred_rf = rf_pipeline.predict(X_test)
  mae_rf = mean_absolute_error(y_test, y_pred_rf)
  r2_rf = r2_score(y_test, y_pred_rf)

  print("Linear Regression - MAE:", mae_lin, "R²:", r2_lin)
  print("Random Forest       - MAE:", mae_rf, "R²:", r2_rf)

  # Select best model by MAE (lower is better)
  if mae_rf <= mae_lin:
    best_model = rf_pipeline
    best_name = "RandomForestRegressor"
    best_mae, best_r2 = mae_rf, r2_rf
  else:
    best_model = lin_reg_pipeline
    best_name = "LinearRegression"
    best_mae, best_r2 = mae_lin, r2_lin

  print(f"\nBest model: {best_name}")
  print(f"Best MAE: {best_mae:.3f}, Best R²: {best_r2:.3f}")

  # Save best model
  os.makedirs(MODEL_DIR, exist_ok=True)
  joblib.dump(best_model, MODEL_PATH)
  print(f"Saved best model pipeline to: {MODEL_PATH}")

def load_trained_model():
  """
  Load the trained model pipeline from disk.
  Assumes train_models() has been run at least once.
  """
  if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
      f"Model file not found at {MODEL_PATH}. "
      f"Run `python src/model.py` first to train and save the model."
    )
  model = joblib.load(MODEL_PATH)
  return model

def make_prediction(model, year, state, demographic_type, group):
  """
  Use the trained model pipeline to predict smoking prevalence (%)
  for a single demographic configuration.
  """
  data = {
    "year": [year],
    "state": [state],
    "demographic_type": [demographic_type],
    "comparing_focus_group": [group],
  }
  X_new = pd.DataFrame(data)
  pred = model.predict(X_new)[0]
  return float(pred)

def get_dropdown_options():
  """
  Helper for the Dash layout:
  Return unique values for years, states, demographic types, and groups.
  """
  df = load_data()
  years = sorted(df["year"].dropna().unique().tolist())
  states = sorted(df["state"].dropna().unique().tolist())
  demo_types = sorted(df["demographic_type"].dropna().unique().tolist())
  groups = sorted(df["comparing_focus_group"].dropna().unique().tolist())

  return {
    "years": years,
    "states": states,
    "demographic_types": demo_types,
    "groups": groups,
  }

# -------------------------------------------------------------------------
# MAIN: Run this script directly to train and save the best model
# -------------------------------------------------------------------------
def main():
  """
  Train and evaluate multiple models, then save the best one to disk.
  Run this once after generating the cleaned dataset.
  """
  train_models()


if __name__ == "__main__":
  main()