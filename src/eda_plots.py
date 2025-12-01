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

# 1. LINE CHART — National Smoking Trend Over Time
def plot_national_trend():
    trend = df.groupby("year")["prevalence_focus"].mean().reset_index()
    fig = px.line(
        trend,
        x="year",
        y="prevalence_focus",
        title="National Smoking Prevalence Trend Over Time",
        labels={"prevalence_focus": "Smoking Prevalence (%)", "year": "Year"}
    )
    return fig


# 2. LINE CHART — Trend by Income Group
def plot_income_trend():
    income_df = df[df["demographic_type"] == "income"]
    fig = px.line(
        income_df,
        x="year",
        y="prevalence_focus",
        color="comparing_focus_group",
        title="Smoking Trend by Income Group",
        labels={"prevalence_focus": "Smoking Prevalence (%)", "comparing_focus_group": "Income Group"}
    )
    return fig


# 3. BAR CHART — Smoking by Age Group
def plot_age_groups():
    age_df = df[df["demographic_type"] == "age"]
    fig = px.bar(
        age_df.groupby("comparing_focus_group")["prevalence_focus"].mean().reset_index(),
        x="comparing_focus_group",
        y="prevalence_focus",
        title="Smoking Prevalence by Age Group",
        labels={"comparing_focus_group": "Age Group", "prevalence_focus": "Smoking Prevalence (%)"}
    )
    return fig


# 4. BAR CHART — Smoking by Race/Ethnicity
def plot_race_groups():
    race_df = df[df["demographic_type"] == "race"]
    fig = px.bar(
        race_df.groupby("comparing_focus_group")["prevalence_focus"].mean().reset_index(),
        x="comparing_focus_group",
        y="prevalence_focus",
        title="Smoking Prevalence by Race/Ethnicity",
        labels={"comparing_focus_group": "Race/Ethnicity", "prevalence_focus": "Smoking Prevalence (%)"}
    )
    return fig


# 5. BAR CHART — Smoking by Income Group
def plot_income_groups():
    income_df = df[df["demographic_type"] == "income"]
    fig = px.bar(
        income_df.groupby("comparing_focus_group")["prevalence_focus"].mean().reset_index(),
        x="comparing_focus_group",
        y="prevalence_focus",
        title="Smoking Prevalence by Income Group",
        labels={"comparing_focus_group": "Income Group", "prevalence_focus": "Smoking Prevalence (%)"}
    )
    return fig


# 6. BAR CHART — Smoking by Employment Status
def plot_employment_groups():
    emp_df = df[df["demographic_type"] == "employment"]
    fig = px.bar(
        emp_df.groupby("comparing_focus_group")["prevalence_focus"].mean().reset_index(),
        x="comparing_focus_group",
        y="prevalence_focus",
        title="Smoking Prevalence by Employment Status",
        labels={"comparing_focus_group": "Employment Status", "prevalence_focus": "Smoking Prevalence (%)"}
    )
    return fig


# 7. SCATTER PLOT — Mental Health vs Smoking
def plot_mental_health_scatter():
    mh_df = df[df["demographic_type"] == "mental_health"]
    fig = px.scatter(
        mh_df,
        x="prevalence_reference",
        y="prevalence_focus",
        color="comparing_focus_group",
        title="Mental Health vs Smoking Prevalence",
        labels={
            "prevalence_reference": "Reference Group Prevalence (%)",
            "prevalence_focus": "Mental Health Group Prevalence (%)",
            "comparing_focus_group": "Mental Health Category"
        }
    )
    return fig


# 8. SCATTER PLOT — Prevalence vs Disparity
def plot_prevalence_vs_disparity():
    fig = px.scatter(
        df,
        x="prevalence_focus",
        y="disparity_value",
        title="Smoking Prevalence vs Disparity Value",
        labels={"prevalence_focus": "Smoking Prevalence (%)", "disparity_value": "Disparity Value"}
    )
    return fig


# 9. BOX PLOT — Smoking Distribution by Employment
def plot_employment_boxplot():
    emp_df = df[df["demographic_type"] == "employment"]
    fig = px.box(
        emp_df,
        x="comparing_focus_group",
        y="prevalence_focus",
        title="Distribution of Smoking Prevalence by Employment Status",
        labels={"comparing_focus_group": "Employment Status", "prevalence_focus": "Smoking Prevalence (%)"}
    )
    return fig


# 10. HISTOGRAM — Disparity Value Distribution
def plot_disparity_histogram():
    fig = px.histogram(
        df,
        x="disparity_value",
        nbins=30,
        title="Distribution of Disparity Values",
        labels={"disparity_value": "Disparity Value"}
    )
    return fig