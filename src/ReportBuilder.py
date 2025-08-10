from pandas import DataFrame
from src.DataAnalyzer import DataAnalyzer

class ReportBuilder:

    def __init__(self, df: DataFrame, target, content):
        self.df = df
        self.target = target
        self.content = content
        self.antisemitic = self.df[self.df[self.target] == 1]
        self.non_antisemitic = self.df[self.df[self.target] == 0]
        self.unspecified = (~self.df[self.target].isin([0, 1]))

    # counts how many tweets are antisemitic/not antisemitic/unclassified
    def total_tweets(self):
        total_tweets = {
            "antisemitic": len(self.antisemitic),
            "non_antisemitic": len(self.non_antisemitic),
            "unspecified": len(self.df[self.unspecified]),
            "total": len(self.df)
        }
        return total_tweets

    def average_length(self):
        average_length = {
            "antisemitic": DataAnalyzer.compute_ave_length(self.antisemitic,self.content),
            "non_antisemitic": DataAnalyzer.compute_ave_length(self.non_antisemitic,self.content),
            "total": DataAnalyzer.compute_ave_length(self.df,self.content),
        }
        return average_length


    def longest_3_tweets(self):
        longest_3_tweets = {
            "antisemitic": DataAnalyzer.longest_3_tweets(self.antisemitic,self.content),
            "non_antisemitic": DataAnalyzer.longest_3_tweets(self.non_antisemitic,self.content),
            "total": DataAnalyzer.longest_3_tweets(self.df,self.content),
        }
        return longest_3_tweets

    def common_words(self):
        common_10_words = {
         "total": DataAnalyzer.common_words(self.df,self.content,10)
        }
        return common_10_words

    def uppercase_words(self):
        uppercase_count = {
            "antisemitic": DataAnalyzer.uppercase_words(self.antisemitic, self.content),
            "non_antisemitic": DataAnalyzer.uppercase_words(self.non_antisemitic, self.content),
            "total": DataAnalyzer.uppercase_words(self.df, self.content)
        }
        return uppercase_count

