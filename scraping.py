import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of GeeksforGeeks Data Science interview questions
url = "https://www.interviewbit.com/data-science-interview-questions/"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract questions from <strong> and <p> tags
questions = []
for tag in soup.find_all("h3"):
    text = tag.get_text(strip=True)
    if "?" in text and len(text.split()) > 3:  # basic filter
        questions.append(text)

# Save raw dataset
df = pd.DataFrame({"question": questions})
df.to_csv("raw_dataset.csv", index=False)

print("Execution Successful")
