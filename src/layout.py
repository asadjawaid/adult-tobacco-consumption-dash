from dash import html, dcc
from src.eda_plots import (
    df,
    plot_national_trend,
    plot_income_trend,
    plot_age_groups,
    plot_race_groups,
    plot_income_groups,
    plot_employment_groups,
    plot_mental_health_scatter,
    plot_prevalence_vs_disparity,
    plot_employment_boxplot,
    plot_disparity_histogram
)


def create_layout():
    return html.Div(
        style={"padding": "20px"},
        children=[
            html.H1("Adult Tobacco Consumption Dashboard"),
            html.Hr(),

            # ===================================
            # EDA VISUALIZATIONS
            # ===================================
            html.H2("1. National Smoking Trend Over Time"),
            html.P("Shows the national decline in smoking prevalence from 2000 to 2023."),
            dcc.Graph(figure=plot_national_trend()),

            html.H2("2. Smoking Trend by Income Group"),
            html.P("Lower-income groups consistently have higher smoking prevalence."),
            dcc.Graph(figure=plot_income_trend()),

            html.Hr(),

            html.H2("3. Smoking by Age Group"),
            html.P("Younger adults (18–24) show the highest smoking prevalence."),
            dcc.Graph(figure=plot_age_groups()),

            html.H2("4. Smoking by Race/Ethnicity"),
            html.P("American Indian/Alaska Native groups show the highest smoking prevalence."),
            dcc.Graph(figure=plot_race_groups()),

            html.H2("5. Smoking by Income Group"),
            html.P("Clear socioeconomic gradient: lower income groups smoke more."),
            dcc.Graph(figure=plot_income_groups()),

            html.H2("6. Smoking by Employment Status"),
            html.P("Unemployed individuals show higher smoking prevalence."),
            dcc.Graph(figure=plot_employment_groups()),

            html.Hr(),

            html.H2("7. Mental Health vs Smoking Prevalence"),
            html.P("Individuals with psychological distress show higher smoking rates."),
            dcc.Graph(figure=plot_mental_health_scatter()),

            html.H2("8. Smoking Prevalence vs Disparity Value"),
            html.P("Higher smoking prevalence often corresponds with higher disparities."),
            dcc.Graph(figure=plot_prevalence_vs_disparity()),

            html.Hr(),

            html.H2("9. Smoking Distribution by Employment Status"),
            html.P("Unemployed groups show greater variability in smoking prevalence."),
            dcc.Graph(figure=plot_employment_boxplot()),

            html.H2("10. Distribution of Disparity Values"),
            html.P("Most disparities cluster near zero with spikes for vulnerable groups."),
            dcc.Graph(figure=plot_disparity_histogram()),

            html.Hr(),

            # ===================================
            # PREDICTION UI
            # ===================================
            html.H2("Predict Smoking Prevalence"),
            html.P("Use the model below to estimate smoking prevalence for a demographic group."),

            html.Label("Select Year:"),
            dcc.Dropdown(
                id="input_year",
                options=[{"label": str(year), "value": year} for year in sorted(df["year"].unique())],
                value=2023,
                clearable=False
            ),

            html.Br(),

            html.Label("Select State:"),
            dcc.Dropdown(
                id="input_state",
                options=[{"label": s, "value": s} for s in sorted(df["state"].unique())],
                value="United States",
                clearable=False
            ),

            html.Br(),

            html.Label("Select Demographic Type:"),
            dcc.Dropdown(
                id="input_demo_type",
                options=[{"label": t.capitalize(), "value": t} for t in sorted(df["demographic_type"].unique())],
                value="age",
                clearable=False
            ),

            html.Br(),

            html.Label("Select Demographic Group:"),
            dcc.Dropdown(
                id="input_group",
                placeholder="Loading demographic groups...",
                clearable=False
            ),

            html.Br(),

            html.Button("Predict", id="predict_button", n_clicks=0),

            html.Br(),
            html.Br(),

            html.Div(
                id="prediction_output",
                style={"fontSize": "20px", "fontWeight": "bold"}
            ),

            html.Br(),
            html.Hr(),
        ]
    )
