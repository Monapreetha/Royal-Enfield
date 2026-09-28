import os
import pandas as pd
from .base_repository import BaseRepository

class BikeRepository(BaseRepository):
    def __init__(self, data_dir="data"):
        super().__init__(data_dir=data_dir, filename="bikes.csv")

    def _ensure_file_exists(self):
        if not os.path.exists(self.get_file_path()):
            df = pd.DataFrame(columns=["BikeID", "Model", "EngineCC", "Color", "Price", "Quantity", "Features"])
            sample_bikes = [
                ["B001", "Classic 350", "349cc", "Halcyon Black", 193000, 10, "Dual Channel ABS, Alloy Wheels"],
                ["B002", "Hunter 350", "349cc", "Rebel Blue", 170000, 15, "Tripper Navigation, Alloy Wheels"],
                ["B003", "Bullet 350", "349cc", "Standard Black", 175000, 5, "Single Channel ABS, Spoke Wheels"],
                ["B004", "Meteor 350", "349cc", "Fireball Red", 205000, 8, "Tripper Navigation, Windshield"],
                ["B005", "Interceptor 650", "648cc", "Canyon Red", 303000, 3, "Dual Channel ABS, Slipper Clutch"],
                ["B006", "Continental GT 650", "648cc", "Mr Clean", 319000, 2, "Clip-on Handlebars, Cafe Racer Design"]
            ]
            for i, bike in enumerate(sample_bikes):
                df.loc[i] = bike
            self.save_all(df)
            
    def update_quantity(self, model: str, new_quantity: int):
        df = self.load_all()
        if not df.empty and model in df["Model"].values:
            idx = df.index[df["Model"] == model].tolist()[0]
            df.at[idx, "Quantity"] = new_quantity
            self.save_all(df)
