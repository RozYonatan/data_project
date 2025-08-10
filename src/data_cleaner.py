import re
from pandas import DataFrame

class Cleaner:
    def __init__(self, df: DataFrame):
        self.df = df

    def remove_punctuation(self):
        self.df["Text"] = self.df["Text"].astype(str).apply(lambda x: re.sub(r'[^\w\s]', '', x))

    def to_lower(self):
        self.df["Text"] = self.df["Text"].astype(str).str.lower()

    def remove_uncategorized_tweets(self):
        self.df = self.df[self.df["Biased"].isin([0, 1])]

    def get_clean_df(self):
        return self.df[["Text", "Biased"]]