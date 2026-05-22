# ============================================================
# FraudShield X - Dockerfile
# Purpose: Containerize the Streamlit fraud risk web app
# ============================================================

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY api/ ./api/
COPY data/project_metrics_summary.csv ./data/project_metrics_summary.csv
COPY data/model_comparison_results.csv ./data/model_comparison_results.csv
COPY data/top_10_feature_importance.csv ./data/top_10_feature_importance.csv

EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]