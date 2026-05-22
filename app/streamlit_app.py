import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FraudShield X - UPI Fraud Risk App",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FraudShield X: UPI Fraud Risk Prediction App")
st.markdown(
    """
    This Streamlit app demonstrates a real-time fraud risk scoring interface
    for UPI transaction monitoring using transaction, temporal, balance, and
    network-risk signals.
    """
)

st.sidebar.header("Transaction Input")

transaction_amount = st.sidebar.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=5000.0,
    step=100.0
)

hour_of_day = st.sidebar.slider(
    "Hour of Day",
    min_value=0,
    max_value=23,
    value=22
)

night_transaction_flag = 1 if hour_of_day >= 22 or hour_of_day <= 5 else 0

sender_old_balance = st.sidebar.number_input(
    "Sender Old Balance",
    min_value=0.0,
    value=10000.0,
    step=100.0
)

sender_new_balance = st.sidebar.number_input(
    "Sender New Balance",
    min_value=0.0,
    value=0.0,
    step=100.0
)

receiver_old_balance = st.sidebar.number_input(
    "Receiver Old Balance",
    min_value=0.0,
    value=0.0,
    step=100.0
)

receiver_new_balance = st.sidebar.number_input(
    "Receiver New Balance",
    min_value=0.0,
    value=5000.0,
    step=100.0
)

sender_network_txn_count = st.sidebar.number_input(
    "Sender Network Transaction Count",
    min_value=0,
    value=5,
    step=1
)

receiver_network_txn_count = st.sidebar.number_input(
    "Receiver Network Transaction Count",
    min_value=0,
    value=8,
    step=1
)

edge_txn_count = st.sidebar.number_input(
    "Sender-Receiver Edge Transaction Count",
    min_value=0,
    value=3,
    step=1
)

transaction_type = st.sidebar.selectbox(
    "Transaction Type",
    ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN", "DEBIT"]
)

st.subheader("Transaction Details")

input_data = pd.DataFrame({
    "Transaction_Amount": [transaction_amount],
    "Hour_Of_Day": [hour_of_day],
    "Night_Transaction_Flag": [night_transaction_flag],
    "Sender_Old_Balance": [sender_old_balance],
    "Sender_New_Balance": [sender_new_balance],
    "Receiver_Old_Balance": [receiver_old_balance],
    "Receiver_New_Balance": [receiver_new_balance],
    "Sender_Network_Txn_Count": [sender_network_txn_count],
    "Receiver_Network_Txn_Count": [receiver_network_txn_count],
    "Edge_Txn_Count": [edge_txn_count],
    "Transaction_Type": [transaction_type]
})

st.dataframe(input_data, use_container_width=True)

def calculate_demo_risk_score(row):
    score = 0

    # Transaction amount risk
    if row["Transaction_Amount"] >= 100000:
        score += 30
    elif row["Transaction_Amount"] >= 50000:
        score += 20
    elif row["Transaction_Amount"] >= 10000:
        score += 10

    # Night transaction risk
    if row["Night_Transaction_Flag"] == 1:
        score += 10

    # Sender balance depletion risk
    if row["Sender_Old_Balance"] > 0:
        balance_drop_ratio = (
            row["Sender_Old_Balance"] - row["Sender_New_Balance"]
        ) / row["Sender_Old_Balance"]

        if balance_drop_ratio >= 0.90:
            score += 25
        elif balance_drop_ratio >= 0.50:
            score += 15

    # Risky transaction type
    if row["Transaction_Type"] in ["TRANSFER", "CASH_OUT"]:
        score += 15

    # Network velocity risk
    if row["Sender_Network_Txn_Count"] >= 10:
        score += 10

    if row["Receiver_Network_Txn_Count"] >= 10:
        score += 10

    if row["Edge_Txn_Count"] >= 5:
        score += 10

    return min(score, 100)

risk_score = calculate_demo_risk_score(input_data.iloc[0])

if risk_score >= 70:
    prediction = "Fraud / High Risk"
    risk_level = "High"
elif risk_score >= 40:
    prediction = "Suspicious / Medium Risk"
    risk_level = "Medium"
else:
    prediction = "Genuine / Low Risk"
    risk_level = "Low"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Fraud Risk Score", f"{risk_score}/100")

with col2:
    st.metric("Risk Level", risk_level)

with col3:
    st.metric("Prediction", prediction)

st.subheader("Risk Explanation")

explanations = []

if transaction_amount >= 10000:
    explanations.append("High transaction amount increased the risk score.")

if night_transaction_flag == 1:
    explanations.append("Transaction occurred during night hours.")

if sender_old_balance > 0 and sender_new_balance <= sender_old_balance * 0.10:
    explanations.append("Sender balance was almost fully depleted.")

if transaction_type in ["TRANSFER", "CASH_OUT"]:
    explanations.append("Transaction type is commonly associated with fraud risk.")

if sender_network_txn_count >= 10 or receiver_network_txn_count >= 10:
    explanations.append("High sender/receiver transaction velocity detected.")

if edge_txn_count >= 5:
    explanations.append("Repeated sender-receiver interaction detected.")

if not explanations:
    explanations.append("No major high-risk pattern detected.")

for item in explanations:
    st.write(f"- {item}")

st.subheader("Project Model Summary")

metrics = pd.DataFrame({
    "Metric": [
        "Total Transactions Used",
        "Fraud Percentage",
        "Best Model",
        "Best Model Recall",
        "Best Model F1 Score",
        "Best Model ROC-AUC"
    ],
    "Value": [
        "508,213",
        "1.6161%",
        "Strict Random Forest",
        "0.997",
        "0.9985",
        "0.9997"
    ]
})

st.table(metrics)

st.info(
    """
    Note: This Streamlit app demonstrates the project interface and risk-scoring logic.
    The trained Random Forest model is stored locally in the project models folder and
    excluded from GitHub using .gitignore because binary model files can be large.
    """
)