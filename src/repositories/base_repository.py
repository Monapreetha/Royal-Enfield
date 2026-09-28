import os
import pandas as pd

class BaseRepository:
    """
    Base Repository for handling generic CSV operations.
    Follows Single Responsibility Principle (SRP) for data access.
    """
    def __init__(self, data_dir="data", filename=""):
        self.data_dir = data_dir
        self.filename = filename
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self._ensure_file_exists()

    def get_file_path(self):
        return os.path.join(self.data_dir, self.filename)

    def _ensure_file_exists(self):
        """Override this in child classes if specific initial data is needed"""
        if not os.path.exists(self.get_file_path()):
            pd.DataFrame().to_csv(self.get_file_path(), index=False)

    def load_all(self):
        try:
            return pd.read_csv(self.get_file_path())
        except FileNotFoundError:
            return pd.DataFrame()

    def save_all(self, df):
        df.to_csv(self.get_file_path(), index=False)

    def append_row(self, row_dict):
        df = self.load_all()
        # Using concat instead of append since append is deprecated in newer pandas
        new_df = pd.DataFrame([row_dict])
        df = pd.concat([df, new_df], ignore_index=True)
        self.save_all(df)
        return df

