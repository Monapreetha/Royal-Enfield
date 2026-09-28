import os
import pandas as pd
from .base_repository import BaseRepository

class FeedbackRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="feedback.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["FeedbackID", "CustomerID", "InvoiceNo", "Model", "TestRideRating", "SalesRating", "DeliveryRating", "OverallRating", "Comments"])
            df.loc[0] = ["FB001", "C001", "INV001", "Classic 350", 5, 4, 5, 5, "Great experience!"]
            self.save_all(df)
