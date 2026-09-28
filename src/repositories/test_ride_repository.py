import os
import pandas as pd
from .base_repository import BaseRepository

class TestRideRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="test_rides.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["BookingID", "CustomerID", "Model", "Date", "Time", "Contact"])
            df.loc[0] = ["TR001", "C001", "Classic 350", "2023-10-25", "10:00 AM", "9876543210"]
            self.save_all(df)
