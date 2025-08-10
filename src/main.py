import json
from src.data_load import DataLoader
from src.data_cleaner import Cleaner
from src.ReportBuilder import ReportBuilder

# שלב 1: טעינת הדאטה
dataset_path = "../data/tweets_dataset.csv"
data_loader = DataLoader(dataset_path)
df = data_loader.load()

# שלב 2: ניקוי הדאטה
cleaner = Cleaner(df)
cleaner.remove_punctuation()
cleaner.to_lower()
cleaner.remove_uncategorized_tweets()
clean_df = cleaner.get_clean_df()

# שלב 3: שמירת הדאטה הנקי
clean_df.to_csv("../results/tweets_dataset_cleaned.csv", index=False)

# שלב 4: ניתוח סטטיסטי
report = ReportBuilder(clean_df, "Biased", "Text")
result = {
    "total_tweets": report.total_tweets(),
    "average_length": report.average_length(),
    "longest_3_tweets": report.longest_3_tweets(),
    "common_words": report.common_words(),
    "uppercase_words": report.uppercase_words()
}

# שלב 5: שמירת תוצאות JSON
with open("../results/results.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)


print(json.dumps(result, indent=4, ensure_ascii=False))
