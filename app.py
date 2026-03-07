from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")


model = joblib.load("models/customer_classifier.pkl")


CLUSTER_INFO = {
    0: {
        "title": "High Value Customers",
        "emoji": "💎",
        "color": "#00e5c0",
        "badge_bg": "rgba(0,229,192,0.12)",
        "badge_border": "rgba(0,229,192,0.35)",
        "behavior": [
            "Highest income group",
            "Highest spending customers",
            "Do not rely heavily on discounts",
            "More loyal and premium buyers",
        ],
        "business": [
            "These are high-value customers",
            "They contribute the most revenue",
        ],
        "strategy": [
            "Loyalty programs",
            "Premium product recommendations",
            "Exclusive offers and VIP services",
        ],
    },
    1: {
        "title": "Medium Value Customers",
        "emoji": "⚡",
        "color": "#4f7cff",
        "badge_bg": "rgba(79,124,255,0.12)",
        "badge_border": "rgba(79,124,255,0.35)",
        "behavior": [
            "Medium income and medium spending",
            "Highly responsive to discounts",
            "Frequently visit the website",
        ],
        "business": [
            "These are price-sensitive customers",
        ],
        "strategy": [
            "Discount campaigns",
            "Coupons and bundle deals",
            "Promotional offers",
        ],
    },
    2: {
        "title": "Low Value Customers",
        "emoji": "🎯",
        "color": "#a259ff",
        "badge_bg": "rgba(162,89,255,0.12)",
        "badge_border": "rgba(162,89,255,0.35)",
        "behavior": [
            "Lowest income group",
            "Very low spending",
            "Visit website often but rarely purchase",
        ],
        "business": [
            "These are low-value customers or browsers",
        ],
        "strategy": [
            "Entry-level products",
            "Strong promotions",
            "Retargeting marketing campaigns",
        ],
    },
}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "customer.html",
        {"request": request, "result": None}
    )


@app.post("/")
async def predict_form(
    request: Request,
    Age: int = Form(...),
    Education: int = Form(...),
    Marital_Status: int = Form(...),
    Parental_Status: int = Form(...),
    Children: int = Form(0),
    Income: float = Form(...),
    Total_Spending: float = Form(...),
    Days_as_Customer: int = Form(...),
    Recency: int = Form(...),
    Wines: float = Form(0),
    Fruits: float = Form(0),
    Meat: float = Form(0),
    Fish: float = Form(0),
    Sweets: float = Form(0),
    Gold: float = Form(0),
    Web: int = Form(0),
    Catalog: int = Form(0),
    Store: int = Form(0),
    Discount_Purchases: int = Form(0),
    TotalPromo: int = Form(0),
    NumWebVisitsMonth: int = Form(0),
):
    try:
        features = np.array([
            Age, Education, Marital_Status, Parental_Status, Children,
            Income, Total_Spending, Days_as_Customer, Recency,
            Wines, Fruits, Meat, Fish, Sweets, Gold,
            Web, Catalog, Store, Discount_Purchases, TotalPromo,
            NumWebVisitsMonth
        ]).reshape(1, -1)

        print("INPUT FEATURES:", features)
        cluster_id = int(model.predict(features)[0])
        print("PREDICTED CLUSTER:", cluster_id)

        cluster_info = CLUSTER_INFO.get(cluster_id, {
            "title": f"Cluster {cluster_id}",
            "emoji": "❓",
            "color": "#6b7599",
            "badge_bg": "rgba(107,117,153,0.12)",
            "badge_border": "rgba(107,117,153,0.35)",
            "behavior": [],
            "business": [],
            "strategy": [],
        })

        return templates.TemplateResponse(
            "customer.html",
            {
                "request": request,
                "result": {"cluster_id": cluster_id, **cluster_info},
            }
        )

    except Exception as e:
        print("PREDICTION ERROR:", e)
        return templates.TemplateResponse(
            "customer.html",
            {"request": request, "result": None, "error": str(e)}
        )


@app.post("/predict")
async def predict_api(request: Request):
    from src.schema import CustomerData
    body = await request.json()
    data = CustomerData(**body)
    features = np.array([
        data.Age, data.Education, data.Marital_Status, data.Parental_Status,
        data.Children, data.Income, data.Total_Spending, data.Days_as_Customer,
        data.Recency, data.Wines, data.Fruits, data.Meat, data.Fish,
        data.Sweets, data.Gold, data.Web, data.Catalog, data.Store,
        data.Discount_Purchases, data.TotalPromo, data.NumWebVisitsMonth
    ]).reshape(1, -1)
    return {"cluster": int(model.predict(features)[0])}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=7860)