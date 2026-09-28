from src.repositories.delivery_repository import DeliveryRepository
import pandas as pd

class DeliveryService:
    def __init__(self):
        self.repo = DeliveryRepository()

    def get_all_deliveries(self) -> pd.DataFrame:
        return self.repo.load_all()

    def update_delivery(self, invoice_no: str, delivery_date: str, status: str) -> str:
        success = self.repo.update_delivery(invoice_no, delivery_date, status)
        if success:
            return "✅ Delivery status updated!"
        else:
            return "❌ Invoice not found."
