from src.repositories.customer_repository import CustomerRepository
import pandas as pd

class CustomerService:
    def __init__(self):
        self.repo = CustomerRepository()

    def get_all_customers(self) -> pd.DataFrame:
        return self.repo.load_all()

    def add_customer(self, name: str, phone: str, email: str, address: str) -> str:
        if not name or not phone:
            return "❌ Name and Phone are required."
        
        df = self.repo.load_all()
        new_id = f"C{len(df) + 1:03d}"
        new_row = {
            "CustomerID": new_id, 
            "Name": name, 
            "Phone": phone, 
            "Email": email, 
            "Address": address
        }
        
        self.repo.append_row(new_row)
        return f"✅ Customer {name} added successfully! ID: {new_id}"

    def search_customer(self, search_term: str) -> pd.DataFrame:
        df = self.repo.load_all()
        if not search_term: 
            return df
        
        return df[df["CustomerID"].str.contains(search_term, case=False, na=False) | 
                  df["Name"].str.contains(search_term, case=False, na=False)]
