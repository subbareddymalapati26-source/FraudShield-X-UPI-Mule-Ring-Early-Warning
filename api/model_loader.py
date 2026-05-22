def calculate_demo_risk_score(transaction):
    """
    Rule-based demo risk scoring layer.

    This API layer demonstrates real-time fraud scoring logic using
    transaction amount, temporal behavior, balance depletion, transaction type,
    and sender-receiver network activity.

    The trained Random Forest model is stored locally in the models folder and
    excluded from GitHub using .gitignore because binary model files are not
    suitable for normal GitHub uploads.
    """

    score = 0

    transaction_amount = transaction.Transaction_Amount
    hour_of_day = transaction.Hour_Of_Day
    sender_old_balance = transaction.Sender_Old_Balance
    sender_new_balance = transaction.Sender_New_Balance
    sender_network_txn_count = transaction.Sender_Network_Txn_Count
    receiver_network_txn_count = transaction.Receiver_Network_Txn_Count
    edge_txn_count = transaction.Edge_Txn_Count
    transaction_type = transaction.Transaction_Type.upper()

    night_transaction_flag = 1 if hour_of_day >= 22 or hour_of_day <= 5 else 0

    if transaction_amount >= 100000:
        score += 30
    elif transaction_amount >= 50000:
        score += 20
    elif transaction_amount >= 10000:
        score += 10

    if night_transaction_flag == 1:
        score += 10

    if sender_old_balance > 0:
        balance_drop_ratio = (sender_old_balance - sender_new_balance) / sender_old_balance

        if balance_drop_ratio >= 0.90:
            score += 25
        elif balance_drop_ratio >= 0.50:
            score += 15

    if transaction_type in ["TRANSFER", "CASH_OUT"]:
        score += 15

    if sender_network_txn_count >= 10:
        score += 10

    if receiver_network_txn_count >= 10:
        score += 10

    if edge_txn_count >= 5:
        score += 10

    return min(score, 100)


def predict_transaction_risk(transaction):
    risk_score = calculate_demo_risk_score(transaction)

    if risk_score >= 70:
        prediction = 1
        fraud_probability = round(risk_score / 100, 4)
        risk_status = "Fraud / High Risk"
    elif risk_score >= 40:
        prediction = 1
        fraud_probability = round(risk_score / 100, 4)
        risk_status = "Suspicious / Medium Risk"
    else:
        prediction = 0
        fraud_probability = round(risk_score / 100, 4)
        risk_status = "Genuine / Low Risk"

    return {
        "prediction": prediction,
        "fraud_probability": fraud_probability,
        "risk_status": risk_status,
        "risk_score": risk_score
    }