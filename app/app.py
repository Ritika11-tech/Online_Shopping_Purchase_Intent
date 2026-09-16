
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Purchase Intent Predictor",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "random_forest_purchase_intent_model.pkl"
)

model = joblib.load(MODEL_PATH)


# ============================================================
# HEADER
# ============================================================

st.title("🛒 Online Shopping Purchase Intent Predictor")

st.write(
    "Enter the details of an online shopping session to estimate "
    "the likelihood that the customer will make a purchase."
)

st.divider()


# ============================================================
# CUSTOMER & SESSION INFORMATION
# ============================================================

st.subheader("👤 Customer & Session Information")

col1, col2 = st.columns(2)

with col1:

    device_options = {
        "Device 0": 0,
        "Device 1": 1,
        "Device 2": 2
    }

    device_label = st.selectbox(
        "Device Type",
        list(device_options.keys())
    )

    device_type = device_options[device_label]


    user_options = {
        "User Type 0": 0,
        "User Type 1": 1
    }

    user_label = st.selectbox(
        "User Type",
        list(user_options.keys())
    )

    user_type = user_options[user_label]


    channel_options = {
        "Marketing Channel 0": 0,
        "Marketing Channel 1": 1,
        "Marketing Channel 2": 2,
        "Marketing Channel 3": 3,
        "Marketing Channel 4": 4,
        "Marketing Channel 5": 5
    }

    channel_label = st.selectbox(
        "Marketing Channel",
        list(channel_options.keys())
    )

    marketing_channel = channel_options[channel_label]


with col2:

    category_options = {
        "Product Category 0": 0,
        "Product Category 1": 1,
        "Product Category 2": 2,
        "Product Category 3": 3,
        "Product Category 4": 4,
        "Product Category 5": 5,
        "Product Category 6": 6,
        "Product Category 7": 7
    }

    category_label = st.selectbox(
        "Product Category",
        list(category_options.keys())
    )

    product_category = category_options[category_label]


    product_id = st.number_input(
        "Product ID",
        min_value=0,
        max_value=898,
        value=100,
        step=1
    )


    location = st.number_input(
        "Location Code",
        min_value=0,
        max_value=224,
        value=50,
        step=1
    )


st.divider()


# ============================================================
# PRODUCT & SHOPPING BEHAVIOUR
# ============================================================

st.subheader("🛍️ Product & Shopping Behaviour")

col1, col2 = st.columns(2)

with col1:

    unit_price = st.number_input(
        "Unit Price",
        min_value=50.05,
        max_value=1999.83,
        value=500.00,
        step=10.00
    )


    quantity = st.selectbox(
        "Quantity",
        [1, 2, 3, 4]
    )


    discount_percent = st.slider(
        "Discount Percentage",
        min_value=0,
        max_value=30,
        value=10,
        step=1
    )


with col2:

    discount_amount = st.number_input(
        "Discount Amount",
        min_value=0.0,
        max_value=2388.26,
        value=50.0,
        step=10.0
    )


    pages_viewed = st.slider(
        "Pages Viewed",
        min_value=1,
        max_value=24,
        value=8,
        step=1
    )


    added_to_cart = st.selectbox(
        "Added to Cart?",
        ["No", "Yes"]
    )

    added_to_cart = 1 if added_to_cart == "Yes" else 0


st.divider()


# ============================================================
# SESSION INFORMATION
# ============================================================

st.subheader("⏱️ Session Information")

col1, col2 = st.columns(2)

with col1:

    time_on_site_sec = st.slider(
        "Time on Site (seconds)",
        min_value=10,
        max_value=1799,
        value=300,
        step=10
    )


    session_duration_options = [
        "Very Short",
        "Short",
        "Long",
        "Very Long"
    ]

    session_duration_bucket = st.selectbox(
        "Session Duration",
        session_duration_options
    )


with col2:

    weekday_options = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    weekday_label = st.selectbox(
        "Visit Weekday",
        list(weekday_options.keys())
    )

    visit_weekday = weekday_options[weekday_label]


    visit_month = st.selectbox(
        "Visit Month",
        list(range(1, 13)),
        format_func=lambda x: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ][x - 1]
    )


    visit_day = st.selectbox(
        "Visit Day",
        list(range(1, 32))
    )


st.divider()


# ============================================================
# OTHER CUSTOMER DETAILS
# ============================================================

st.subheader("⭐ Other Details")

col1, col2 = st.columns(2)

with col1:

    rating = st.select_slider(
        "Rating",
        options=[1, 2, 3, 4, 5],
        value=4
    )


with col2:

    season_options = {
        "Season 0": 0,
        "Season 1": 1,
        "Season 2": 2,
        "Season 3": 3
    }

    season_label = st.selectbox(
        "Visit Season",
        list(season_options.keys())
    )

    visit_season = season_options[season_label]


st.info(
    "📅 The dataset contains shopping sessions from 2024, "
    "so the visit year is automatically set to 2024."
)


st.divider()


# ============================================================
# PREDICTION
# ============================================================

st.subheader("🔮 Prediction")

if st.button(
    "Predict Purchase Intent",
    use_container_width=True
):

    # Create input dataframe
    input_data = pd.DataFrame([{

        "device_type": device_type,
        "user_type": user_type,
        "marketing_channel": marketing_channel,
        "product_id": product_id,
        "product_category": product_category,
        "unit_price": unit_price,
        "quantity": quantity,
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "pages_viewed": pages_viewed,
        "time_on_site_sec": time_on_site_sec,
        "added_to_cart": added_to_cart,
        "rating": rating,
        "visit_day": visit_day,
        "visit_month": visit_month,
        "visit_weekday": visit_weekday,
        "visit_season": visit_season,
        "session_duration_bucket": session_duration_bucket,
        "location": location,
        "visit_year": 2024

    }])


    # Prediction
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0][1]


    st.divider()


    # ========================================================
    # RESULT
    # ========================================================

    if prediction == 1:

        st.success(
            "🛍️ Purchase Likely"
        )

    else:

        st.warning(
            "👀 Purchase Unlikely"
        )


    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Purchase Probability",
            f"{probability:.2%}"
        )

    with col2:

        st.metric(
            "No-Purchase Probability",
            f"{1 - probability:.2%}"
        )


    # Progress bar
    st.write("Purchase Probability")

    st.progress(float(probability))


    if probability >= 0.70:

        st.success(
            "High purchase likelihood"
        )

    elif probability >= 0.40:

        st.info(
            "Moderate purchase likelihood"
        )

    else:

        st.warning(
            "Low purchase likelihood"
        )


st.divider()

st.caption(
    "Machine Learning Model: Random Forest Classifier | "
    "Dataset: Online Shopping Behaviour"
)

