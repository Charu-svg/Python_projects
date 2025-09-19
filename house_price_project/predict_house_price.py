import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

def predict_house_price(GrLivArea, OverallQual, TotalBsmtSF, FullBath, GarageCars):
    new_house = pd.DataFrame({
        "GrLivArea": [GrLivArea],
        "OverallQual": [OverallQual],
        "TotalBsmtSF": [TotalBsmtSF],
        "FullBath": [FullBath],
        "GarageCars": [GarageCars]
    })
    return model.predict(new_house)[0]

if __name__ == "__main__":
    print("Enter house details to predict price:")
    GrLivArea = float(input("GrLivArea: "))
    OverallQual = int(input("OverallQual (1-10): "))
    TotalBsmtSF = float(input("TotalBsmtSF: "))
    FullBath = int(input("FullBath: "))
    GarageCars = int(input("GarageCars: "))

    price = predict_house_price(GrLivArea, OverallQual, TotalBsmtSF, FullBath, GarageCars)
    print(f"\nPredicted house price: {price:.2f}")
