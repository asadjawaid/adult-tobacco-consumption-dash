import dash
from dash import Input, Output, State
from src.layout import create_layout
from src.model import load_trained_model, make_prediction
from src.eda_plots import df   # Needed for dynamic dropdown callback


# Initialize Dash
app = dash.Dash(__name__)
server = app.server

# Load the trained model once
model = load_trained_model()

# Set app layout
app.layout = create_layout()


# -----------------------------------------------------------
# CALLBACK 1: Update demographic GROUP dropdown dynamically
# -----------------------------------------------------------
@app.callback(
    Output("input_group", "options"),
    Input("input_demo_type", "value"),
)
def update_group_options(selected_demo):
    if selected_demo is None:
        return []

    filtered = df[df["demographic_type"] == selected_demo]

    groups = sorted(filtered["comparing_focus_group"].dropna().unique())

    return [{"label": g, "value": g} for g in groups]


# -----------------------------------------------------------
# CALLBACK 2: Make prediction using ML model
# -----------------------------------------------------------
@app.callback(
    Output("prediction_output", "children"),
    Input("predict_button", "n_clicks"),
    State("input_year", "value"),
    State("input_state", "value"),
    State("input_demo_type", "value"),
    State("input_group", "value"),
)
def update_prediction(n_clicks, year, state, demographic_type, group):
    if not n_clicks:
        return "Select values above and click 'Predict Smoking Prevalence'."

    if year is None or state is None or demographic_type is None or group is None:
        return "Please fill in all fields before predicting."

    try:
        pred = make_prediction(model, year, state, demographic_type, group)
        return f"Predicted smoking prevalence for this group is {pred:.1f}%."
    except Exception as e:
        return f"An error occurred while making prediction: {e}"


# Run app
if __name__ == "__main__":
    app.run(debug=True)
