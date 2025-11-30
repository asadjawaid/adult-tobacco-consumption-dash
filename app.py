import dash
from dash import Input, Output, State
from src.layout import create_layout
from src.model import load_trained_model, make_prediction

app = dash.Dash(__name__)
server = app.server

# Load trained model once at startup
model = load_trained_model()

app.layout = create_layout()


@app.callback(
    Output("prediction_output", "children"),
    Input("predict_button", "n_clicks"),
    State("input_year", "value"),
    State("input_state", "value"),
    State("input_demographic_type", "value"),
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


if __name__ == "__main__":
    app.run(debug=True)
