import joblib
import numpy as np

# model load
model = joblib.load("models/customer_classifier.pkl")


def predict_customer(data):
    try:

        features = np.array([
            data.Age,
            data.Education,
            data.Marital_Status,
            data.Parental_Status,
            data.Children,
            data.Income,
            data.Total_Spending,
            data.Days_as_Customer,
            data.Recency,
            data.Wines,
            data.Fruits,
            data.Meat,
            data.Fish,
            data.Sweets,
            data.Gold,
            data.Web,
            data.Catalog,
            data.Store,
            data.Discount_Purchases,
            data.TotalPromo,
            data.NumWebVisitsMonth
        ]).reshape(1, -1)

        # debugging (optional but useful)
        print("INPUT FEATURES:", features)

        prediction = model.predict(features)

        print("MODEL PREDICTION:", prediction)

        return int(prediction[0])

    except Exception as e:
        print("PREDICTION ERROR:", e)
        raise ValueError(f"Prediction failed: {str(e)}")