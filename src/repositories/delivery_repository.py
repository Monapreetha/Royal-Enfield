import os
import pandas as pd
from .base_repository import BaseRepository

class DeliveryRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="deliveries.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["DeliveryID", "InvoiceNo", "Model", "DeliveryDate", "Status"])
            df.loc[0] = ["DEL001", "INV001", "Classic 350", "2023-10-28", "Delivered"]
            self.save_all(df)

    def update_delivery(self, invoice_no: str, delivery_date: str, status: str) -> bool:
        df = self.load_all()
        if invoice_no in df["InvoiceNo"].values:
            idx = df.index[df["InvoiceNo"] == invoice_no].tolist()[0]
            df.at[idx, "DeliveryDate"] = delivery_date
            df.at[idx, "Status"] = status
            self.save_all(df)
            return True
        return False
