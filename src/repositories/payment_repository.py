import os
import pandas as pd
from .base_repository import BaseRepository

class PaymentRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="payments.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["PaymentID", "InvoiceNo", "CustomerID", "Amount", "Method", "Status", "Date"])
            df.loc[0] = ["PAY001", "INV001", "C001", 225000, "UPI", "Completed", "2023-10-26"]
            self.save_all(df)
