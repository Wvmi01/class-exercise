import pandas as pd
import matplotlib.pyplot as plt
import re

data = {"ID":range(100),"Score":[10]*2+[20]*3+[30]*5+[50]*15+[60]*20+
[70]*25+[80]*15 +[90]*8 +[100,100,5,5,0,0,5000]}
df = pd.DataFrame(data)
print(df)

# Inspect data before cleaning:
print(df.shape)
print(df.dtypes)
print(df.describe())

# Make copy before cleaning
df_original = df.copy()

# IQR Method - Calculate the bounds:
q1 = df["Score"].quantile(0.25)
q3 = df["Score"].quantile(0.75)
iqr = q3 - q1

# Use the equation above to replace None
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(lower)
print(upper)

df_score_cleaned = df[(df["Score"] >= lower) & (df["Score"] <= upper)]

# Z-Score:
# z-score(s) = (value(s) - mean) / standard deviation

mean = df["Score"].mean()
std = df["Score"].std()
# Use the equation above to replace None
z_scores = (df["Score"] - mean) / std
print(f"Z-score(s): {z_scores}")

# Text Cleaning:
data = {"ID":range(4),"Message":["Now Here "," now here ", " NOW HERE", "Now here"]}
df = pd.DataFrame(data)
print(df)

# Strip Whitespace:
df["Message"] = df["Message"].str.strip()
print(df)

# Convert to Lowercase
df["Message"] = df["Message"].str.lower()
print(df)

# Remove repeated whitespace between words
df["Message"] = df["Message"].str.replace(' ', '')
print(df)

# Difference between "" vs r"":
print("a\nb") #a b
print(r"a\tb") # a\tb

#One or more consecutive whitespace characters
pattern = r"\s+"
#One or more consecutive non-whitespace characters
pattern = r"\S+"

# Regex patterns are written as raw strings(r""):
print(re.sub(r"\s+", " ", "Hi     there"))
print(re.findall(r"\S+", "Hi there"))

def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

df["Message"] = df["Message"].apply(clean_text)

# URL Cleaning Example:
links = ["Visit https://example.com for more info", "My link:www.github.com/mylink/", "Visit http://www.google.com/search"]
data = pd.Series(links)

print(data)

def replace_url(text):
    text = re.sub(r"https?://\S+", "URL", text)
    return text

# Remove URLs:
data = data.apply(replace_url)
print(data)