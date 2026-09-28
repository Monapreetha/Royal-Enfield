import os
import pandas as pd
from .base_repository import BaseRepository

class CustomerRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="customers.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["CustomerID", "Name", "Phone", "Email", "Address"])
            df.loc[0] = ["C001", "John Doe", "9876543210", "john@example.com", "123 Main St, City"]
            self.save_all(df)
