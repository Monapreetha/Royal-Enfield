from src.repositories.bike_repository import BikeRepository
import pandas as pd
from typing import List

class BikeService:
    def __init__(self):
        self.repo = BikeRepository()

    def get_all_bikes(self) -> pd.DataFrame:
        return self.repo.load_all()

    def add_bike(self, model: str, engine_cc: str, color: str, price: float, quantity: int, features: str) -> str:
        if not model or not price: 
            return "❌ Model and Price are required."
        
        df = self.repo.load_all()
        new_id = f"B{len(df) + 1:03d}"
        new_row = {
            "BikeID": new_id, 
            "Model": model, 
            "EngineCC": engine_cc, 
            "Color": color, 
            "Price": float(price), 
            "Quantity": int(quantity), 
            "Features": features
        }
        
        self.repo.append_row(new_row)
        return f"✅ Bike {model} added successfully! ID: {new_id}"

    def get_bike_models(self) -> List[str]:
        df = self.repo.load_all()
        if df.empty: 
            return []
        return df["Model"].unique().tolist()
