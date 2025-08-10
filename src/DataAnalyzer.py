from collections import Counter
from pandas import DataFrame
class DataAnalyzer:



#function that returns the average length of tweets classified by category
    @staticmethod
    def compute_ave_length(sub_df:DataFrame,content):
        texts = sub_df[content].dropna().astype(str)
        result = texts.apply(lambda x: len(x.split())).mean()
        return  result

    @staticmethod
#function that returns the most common words from all tweets.
    def common_words(sub_df:DataFrame,content,n):
        texts = sub_df[content].dropna().astype(str)
        all_words = []
        for text in texts:
            words = text.split()
            all_words.extend(words)
        return [word for word , _ in Counter(all_words).most_common(n)]

    @staticmethod
#function that returns the three longest tweets for each category(characters)
    def longest_3_tweets(sub_df:DataFrame,content):
        texts = sub_df[content].dropna().astype(str)
        sorted_text = texts.sort_values(key=lambda x: x.str.len(),ascending=False)
        return  sorted_text.head(3).tolist()

    #function that returns the sum of words with uppercase letters
    @staticmethod
    def uppercase_words(sub_df: DataFrame, content: str):
        texts = sub_df[content].dropna().astype(str)
        count = 0
        for text in texts:
            words = text.split()
            count += sum(1 for word in words if word.isupper())
        return count

