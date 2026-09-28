from src.repositories.feedback_repository import FeedbackRepository
import pandas as pd

class FeedbackService:
    def __init__(self):
        self.repo = FeedbackRepository()

    def get_all_feedback(self) -> pd.DataFrame:
        return self.repo.load_all()

    def submit_feedback(self, cust_id: str, invoice_no: str, model: str, tr_rating: int, sales_rating: int, del_rating: int, overall_rating: int, comments: str) -> str:
        df = self.repo.load_all()
        new_id = f"FB{len(df) + 1:03d}"
        new_row = {
            "FeedbackID": new_id, 
            "CustomerID": cust_id, 
            "InvoiceNo": invoice_no, 
            "Model": model,
            "TestRideRating": int(tr_rating), 
            "SalesRating": int(sales_rating), 
            "DeliveryRating": int(del_rating), 
            "OverallRating": int(overall_rating), 
            "Comments": comments
        }
        
        self.repo.append_row(new_row)
        return "✅ Thank you for your feedback!"
