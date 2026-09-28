from src.repositories.customer_repository import CustomerRepository
from src.repositories.bike_repository import BikeRepository
from src.repositories.purchase_repository import PurchaseRepository

class DashboardService:
    def __init__(self):
        self.cust_repo = CustomerRepository()
        self.bike_repo = BikeRepository()
        self.purchase_repo = PurchaseRepository()

    def get_dashboard_stats(self) -> tuple[int, int, float]:
        c_df = self.cust_repo.load_all()
        b_df = self.bike_repo.load_all()
        p_df = self.purchase_repo.load_all()
        
        tot_cust = len(c_df)
        tot_bikes = int(b_df["Quantity"].sum()) if not b_df.empty else 0
        tot_revenue = float(p_df["TotalAmount"].sum()) if not p_df.empty else 0.0
        
        return tot_cust, tot_bikes, tot_revenue
