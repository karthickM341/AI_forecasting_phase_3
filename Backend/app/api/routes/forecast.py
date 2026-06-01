from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import pandas as pd
import numpy as np
import joblib
import os
import uuid

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from app.core.database import get_db
from app.models.forecast import ForecastHistory
from app.models.notification import Notification

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)

MODEL_PATH = "saved_models"
os.makedirs(MODEL_PATH, exist_ok=True)


def calculate_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": round(mae, 2),
        "MSE": round(mse, 2),
        "RMSE": round(rmse, 2),
        "R2_SCORE": round(r2, 2)
    }


def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train):
    model = RandomForestRegressor(
        n_estimators=150,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model


@router.post("/generate")
async def generate_forecast(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        if not file.filename.endswith((".csv", ".xlsx")):
            raise HTTPException(
                status_code=400,
                detail="Only CSV and Excel files are supported"
            )

        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)

        
        required_columns = ["month", "sales"]

        for col in required_columns:
            if col not in df.columns:
                raise HTTPException(
                    status_code=400,
                    detail=f"Missing column: {col}"
                )

        
        df = df.dropna()

        df["month"] = pd.to_datetime(df["month"])

        df = df.sort_values("month")

        # Feature Engineering
        df["month_number"] = np.arange(len(df))

        X = df[["month_number"]]
        y = df["sales"]

        
        linear_model = train_linear_regression(X, y)
        rf_model = train_random_forest(X, y)

        
        linear_predictions = linear_model.predict(X)
        rf_predictions = rf_model.predict(X)

        
        linear_metrics = calculate_metrics(
            y,
            linear_predictions
        )

        rf_metrics = calculate_metrics(
            y,
            rf_predictions
        )

        
        if rf_metrics["RMSE"] < linear_metrics["RMSE"]:
            best_model = rf_model
            best_model_name = "Random Forest"
            best_metrics = rf_metrics
        else:
            best_model = linear_model
            best_model_name = "Linear Regression"
            best_metrics = linear_metrics

        
        future_months = 6

        future_index = np.arange(
            len(df),
            len(df) + future_months
        ).reshape(-1, 1)

        future_predictions = best_model.predict(future_index)

        future_dates = pd.date_range(
            start=df["month"].max(),
            periods=future_months + 1,
            freq="M"
        )[1:]

        forecast_result = []

        for date, value in zip(future_dates, future_predictions):

            forecast_result.append({
                "month": date.strftime("%Y-%m"),
                "predicted_sales": round(float(value), 2)
            })

        
        model_filename = f"{uuid.uuid4()}.pkl"

        model_full_path = os.path.join(
            MODEL_PATH,
            model_filename
        )

        joblib.dump(best_model, model_full_path)

        
        history = ForecastHistory(
            model_name=best_model_name,
            file_name=file.filename,
            accuracy_score=best_metrics["R2_SCORE"],
            rmse_score=best_metrics["RMSE"],
            created_at=datetime.utcnow()
        )

        db.add(history)

        # ------------------------------

        notification = Notification(
            title="Forecast Completed",
            message=f"Forecast generated successfully using {best_model_name}",
            created_at=datetime.utcnow()
        )

        db.add(notification)

        db.commit()

        
        return {
            "success": True,
            "selected_model": best_model_name,
            "metrics": best_metrics,
            "forecast": forecast_result,
            "saved_model": model_filename
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/history")
def get_forecast_history(db: Session = Depends(get_db)):

    history = db.query(ForecastHistory).all()

    results = []

    for item in history:
        results.append({
            "id": item.id,
            "model_name": item.model_name,
            "file_name": item.file_name,
            "accuracy_score": item.accuracy_score,
            "rmse_score": item.rmse_score,
            "created_at": item.created_at
        })

    return {
        "total_records": len(results),
        "history": results
    }


@router.post("/compare-models")
async def compare_models(
    file: UploadFile = File(...)
):

    try:

        # Read File
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)

        df = df.dropna()

        df["month"] = pd.to_datetime(df["month"])

        df["month_number"] = np.arange(len(df))

        X = df[["month_number"]]
        y = df["sales"]

        # Train Models
        linear_model = train_linear_regression(X, y)
        rf_model = train_random_forest(X, y)

        # Predictions
        linear_predictions = linear_model.predict(X)
        rf_predictions = rf_model.predict(X)

        # Metrics
        linear_metrics = calculate_metrics(
            y,
            linear_predictions
        )

        rf_metrics = calculate_metrics(
            y,
            rf_predictions
        )

        return {
            "Linear Regression": linear_metrics,
            "Random Forest": rf_metrics
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )