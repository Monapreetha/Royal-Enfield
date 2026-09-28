import os
import pandas as pd
from .base_repository import BaseRepository

class PurchaseRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="purchases.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["InvoiceNo", "CustomerID", "Model", "Color", "Quantity", "BikePrice", "Accessories", "Insurance", "Registration", "TotalAmount", "PaymentMethod", "PurchaseDate"])
            df.loc[0] = ["INV001", "C001", "Classic 350", "Halcyon Black", 1, 193000, 5000, 12000, 15000, 225000, "UPI", "2023-10-26"]
            self.save_all(df)
