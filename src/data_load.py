import  pandas as pd

class DataLoader:
    def __init__(self,filepath:str):
        self.filepath = filepath

    def load(self):
        try:
            df = pd.read_csv(self.filepath)
            return df
        except FileNotFoundError:
            print(f"Error: the {self.filepath} not found")
            return pd.DataFrame()