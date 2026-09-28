from src.repositories.test_ride_repository import TestRideRepository
from src.repositories.customer_repository import CustomerRepository
from src.repositories.bike_repository import BikeRepository
import pandas as pd

class TestRideService:
    def __init__(self):
        self.tr_repo = TestRideRepository()
        self.cust_repo = CustomerRepository()
        self.bike_repo = BikeRepository()

    def get_all_test_rides(self) -> pd.DataFrame:
        return self.tr_repo.load_all()

    def book_test_ride(self, cust_id: str, model: str, date: str, time_slot: str, contact: str) -> str:
        cust_df = self.cust_repo.load_all()
        bike_df = self.bike_repo.load_all()
        tr_df = self.tr_repo.load_all()
        
        # Validation Checks
        if cust_id not in cust_df["CustomerID"].values:
            return "❌ Error: Customer ID does not exist. Please register."
        if model not in bike_df["Model"].values:
            return "❌ Error: Bike model not found."
            
        bike_qty = bike_df.loc[bike_df["Model"] == model, "Quantity"].values[0]
        if bike_qty <= 0:
            return "❌ Error: Bike is currently out of stock."
            
        conflict = tr_df[(tr_df["Model"] == model) & (tr_df["Date"] == date) & (tr_df["Time"] == time_slot)]
        if not conflict.empty:
            return "❌ Error: Time slot already booked for this model."
            
        new_id = f"TR{len(tr_df) + 1:03d}"
        new_row = {
            "BookingID": new_id, 
            "CustomerID": cust_id, 
            "Model": model, 
            "Date": date, 
            "Time": time_slot, 
            "Contact": contact
        }
        
        self.tr_repo.append_row(new_row)
        return f"✅ Success: Test ride booked! Booking ID: {new_id}"
