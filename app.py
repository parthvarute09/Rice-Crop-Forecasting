
import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent

DATA_PATH = ROOT / "data" / "rice_dataset.csv"
MODEL_PATH = ROOT / "models" / "rice_yield_pipeline.joblib"
METRICS_PATH = ROOT / "models" / "model_metrics.json"

st.set_page_config(
    page_title="Rice Yield Forecasting",
    page_icon="🌾",
    layout="wide",
)

st.title("🌾 Rice Yield Forecasting System")
st.write(
    "Estimate rice yield using agricultural and weather inputs."
)

if not MODEL_PATH.exists() or not METRICS_PATH.exists():
    st.error("Train the model first using src/train_model.py.")
    st.stop()

df = pd.read_csv(DATA_PATH)

with open(METRICS_PATH, encoding="utf-8") as f:
    metrics = json.load(f)

model = joblib.load(MODEL_PATH)
feature_cols = metrics.get(
    "features",
    metrics.get("feature_columns", [])
)

st.caption(
    f"Model: {metrics['selected_model']} | "
    "Predictions are estimates, not guarantees."
)

with st.form("yield_prediction_form"):
    st.subheader("Enter crop and weather details")
    inputs = {}

    columns = st.columns(2)

    for i, col in enumerate(feature_cols):
        with columns[i % 2]:
            series = df[col]

            if pd.api.types.is_numeric_dtype(series):
                median = float(series.median())
                minimum = float(series.min())
                maximum = float(series.max())

                # Permit values outside the historical range,
                # but warn users below if they do so.
                margin = max((maximum - minimum) * 0.1, 1.0)

                inputs[col] = st.number_input(
                    col,
                    value=median,
                    min_value=minimum - margin,
                    max_value=maximum + margin,
                )
            else:
                choices = sorted(
                    series.dropna().astype(str).unique().tolist()
                )

                if not choices:
                    st.warning(f"No valid options for {col}")
                    st.stop()

                inputs[col] = st.selectbox(col, choices)

    submitted = st.form_submit_button("Predict rice yield")

if submitted:
    input_df = pd.DataFrame([inputs], columns=feature_cols)

    try:
        prediction = float(model.predict(input_df)[0])

        if prediction < 0:
            st.warning(
                "The model returned a negative yield. "
                "Check the model and input data."
            )
        else:
            st.success("Prediction completed")
            st.metric(
                "Estimated rice yield",
                f"{prediction:,.2f} kg/ha",
            )
            st.caption(
                "This estimate is only as reliable as the "
                "training data and its validation."
            )

    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
