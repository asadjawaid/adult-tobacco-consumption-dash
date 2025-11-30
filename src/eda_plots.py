# ALL 10 plots live here
import plotly.express as px
import pandas as pd

# Load the dataset once
df = pd.read_csv("data/cleaned/final_cleaned_data.csv")

def plot_overall_trend():
  """Plot 1: Overall smoking trends over time."""
  trend = df.groupby("year")["prevalence_focus"].mean().reset_index()

  fig = px.line(trend, x="year", y="prevalence_focus", title="Overall Smoking Prevalence Over Time")
  
  return fig

def plot_age_groups():
  """Plot 2: Smoking by age groups."""
  age_df = df[df["demographic_type"] == "age"]
  
  fig = px.bar(
    age_df,
    x="comparing_focus_group",
    y="prevalence_focus",
    title="Smoking Prevalence by Age Group"
  )

  return fig

def plot_race_groups():
  """Plot 3: Race/Ethnicity Disparities"""
  race_df = df[df["demographic_type"] == "race"]
  fig = px.bar(
    race_df,
    x="comparing_focus_group",
    y="prevalence_focus",
    title="Smoking Prevalence by Race & Ethnicity",
    labels={"comparing_focus_group": "Race/Ethnicity", "prevalence_focus": "Smoking Prevalence (%)"}
  )
  return fig

def plot_income_over_time():
  """Plot 4: Income-Level Trends Over Time"""
  income_df = df[df["demographic_type"] == "income"]
  fig = px.line(
    income_df,
    x="year",
    y="prevalence_focus",
    color="comparing_focus_group",
    title="Income Level vs Smoking Prevalence Over Time",
    labels={"comparing_focus_group": "Income Level"}
    )
  return fig

def plot_employment_groups():
  """Plot 5: Employment Status Distribution"""
  emp_df = df[df["demographic_type"] == "employment"]
  fig = px.box(
      emp_df,
      x="comparing_focus_group",
      y="prevalence_focus",
      title="Smoking Rate Distribution by Employment Status"
  )
  return fig

def plot_mental_health():
  """Plot 6: Mental Health & Smoking Relationship"""
  mh_df = df[df["demographic_type"] == "mental_health"]
  fig = px.scatter(
    mh_df,
    x="prevalence_reference",
    y="prevalence_focus",
    color="comparing_focus_group",
    title="Mental Health Comparison: Reference vs Focus Group Smoking Rates",
    labels={
        "prevalence_reference": "Reference Prevalence (%)",
        "prevalence_focus": "Focus Prevalence (%)"
    }
  )
  return fig

def plot_disparity_heatmap():
  """Plot Disparity Heatmap (All Demographic Types)"""
  heat_df = df.pivot_table(
    index="comparing_focus_group",
    columns="demographic_type",
    values="disparity_value",
    aggfunc="mean"
  )
  fig = px.imshow(
    heat_df,
    title="Average Disparity Value by Demographic Type",
    labels=dict(x="Demographic Type", y="Group", color="Disparity")
  )
  return fig

def plot_faceted_trends():
  """Plot 8: Faceted Trends by Demographic Type"""
  fig = px.line(
    df,
    x="year",
    y="prevalence_focus",
    color="comparing_focus_group",
    facet_col="demographic_type",
    facet_col_wrap=2,
    title="Trends in Smoking Prevalence Across Demographic Types"
  )
  return fig

def plot_state_disparities():
  """Plot 9: State-Level Disparity Distribution"""
  fig = px.histogram(
    df,
    x="disparity_value",
    nbins=30,
    title="Distribution of Disparity Values Across States"
  )
  return fig

def plot_outliers():
  """Plot 10: Outlier Detection"""
  fig = px.scatter(
    df,
    x="prevalence_focus",
    y="disparity_value",
    color="demographic_type",
    title="Outlier Analysis: Prevalence vs Disparity",
    labels={
        "prevalence_focus": "Smoking Prevalence (%)",
        "disparity_value": "Disparity Value"
    }
  )
  return fig
