from dash import html, dcc
from src.eda_plots import (
    plot_overall_trend,
    plot_age_groups,
    plot_race_groups,
    plot_income_over_time,
    plot_employment_groups,
    plot_mental_health,
    plot_disparity_heatmap,
    plot_faceted_trends,
    plot_state_disparities,
    plot_outliers,
)
from src.model import get_dropdown_options

options = get_dropdown_options()


def create_layout():
    return html.Div(
        children=[

            html.H1(
                "Adult Tobacco Consumption Dashboard",
                style={"textAlign": "center", "padding": "20px"},
            ),

            html.H2(
                "Exploratory Data Analysis",
                style={"marginTop": "20px", "borderBottom": "2px solid #ccc"},
            ),

            # Plot 1
            html.Div(
                [
                    html.H3("1. Overall Smoking Trend Over Time"),
                    dcc.Graph(figure=plot_overall_trend()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 2
            html.Div(
                [
                    html.H3("2. Smoking Prevalence by Age Group"),
                    dcc.Graph(figure=plot_age_groups()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 3
            html.Div(
                [
                    html.H3("3. Smoking Prevalence by Race & Ethnicity"),
                    dcc.Graph(figure=plot_race_groups()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 4
            html.Div(
                [
                    html.H3("4. Income Level Trends Over Time"),
                    dcc.Graph(figure=plot_income_over_time()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 5
            html.Div(
                [
                    html.H3("5. Smoking Rate Distribution by Employment Status"),
                    dcc.Graph(figure=plot_employment_groups()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 6
            html.Div(
                [
                    html.H3("6. Mental Health & Smoking Relationship"),
                    dcc.Graph(figure=plot_mental_health()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 7
            html.Div(
                [
                    html.H3("7. Disparity Heatmap Across Demographic Types"),
                    dcc.Graph(figure=plot_disparity_heatmap()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 8
            html.Div(
                [
                    html.H3("8. Faceted Trends by Demographic Type"),
                    dcc.Graph(figure=plot_faceted_trends()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 9
            html.Div(
                [
                    html.H3("9. State-Level Disparity Value Distribution"),
                    dcc.Graph(figure=plot_state_disparities()),
                ],
                style={"marginBottom": "40px"},
            ),

            # Plot 10
            html.Div(
                [
                    html.H3("10. Outlier Analysis: Prevalence vs Disparity"),
                    dcc.Graph(figure=plot_outliers()),
                ],
                style={"marginBottom": "40px"},
            ),

            # ------------------------------------------------------------------
            # ML Prediction Section
            # ------------------------------------------------------------------
            html.H2(
                "Machine Learning Prediction",
                style={
                    "marginTop": "50px",
                    "borderTop": "2px solid #ccc",
                    "paddingTop": "20px",
                },
            ),

            html.Div(
                [
                    html.Div(
                        [
                            html.Label("Year"),
                            dcc.Dropdown(
                                id="input_year",
                                options=[{"label": y, "value": int(y)} for y in options["years"]],
                                placeholder="Select year",
                            ),
                        ],
                        style={"width": "24%", "display": "inline-block", "paddingRight": "10px"},
                    ),
                    html.Div(
                        [
                            html.Label("State"),
                            dcc.Dropdown(
                                id="input_state",
                                options=[{"label": s, "value": s} for s in options["states"]],
                                placeholder="Select state",
                            ),
                        ],
                        style={"width": "24%", "display": "inline-block", "paddingRight": "10px"},
                    ),
                    html.Div(
                        [
                            html.Label("Demographic Type"),
                            dcc.Dropdown(
                                id="input_demographic_type",
                                options=[
                                    {"label": d, "value": d}
                                    for d in options["demographic_types"]
                                ],
                                placeholder="Select demographic type",
                            ),
                        ],
                        style={"width": "24%", "display": "inline-block", "paddingRight": "10px"},
                    ),
                    html.Div(
                        [
                            html.Label("Focus Group"),
                            dcc.Dropdown(
                                id="input_group",
                                options=[{"label": g, "value": g} for g in options["groups"]],
                                placeholder="Select focus group",
                            ),
                        ],
                        style={"width": "24%", "display": "inline-block"},
                    ),
                ],
                style={"marginBottom": "20px"},
            ),

            html.Button("Predict Smoking Prevalence", id="predict_button", n_clicks=0),

            html.Div(
                id="prediction_output",
                style={
                    "marginTop": "20px",
                    "fontSize": "18px",
                    "fontWeight": "bold",
                },
            ),

        ],
        style={"width": "80%", "margin": "auto", "paddingBottom": "50px"},
    )
