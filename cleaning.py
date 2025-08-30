import pandas as pd
import re

# Load dataset
df = pd.read_csv("raw_dataset.csv")

# Assume column name is "Question"
col_name = df.columns[0]
questions = df[col_name].dropna().astype(str)

cleaned = []

for q in questions:
    # Remove numbering like "12." or "45)" at start
    q = re.sub(r"^\d+[\.\)]\s*", "", q.strip())

    # Split if multiple questions in same cell (by '?')
    parts = re.split(r"\?\s*", q)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Add back question mark if it's a question
        if not part.endswith("?"):
            part += "?"

        # Normalize spaces & remove quotes or specials
        part = re.sub(r"[^A-Za-z0-9 ,\?\-\(\)]", "", part)
        part = re.sub(r"\s+", " ", part).strip()

        # Keep only valid questions
        if re.match(r"^(What|How|Why|Explain|Define|Differentiate|Is|Can|When|Where|Which|Give|Write)", part,
                    re.IGNORECASE):
            cleaned.append(part)

# Deduplicate
cleaned = list(dict.fromkeys(cleaned))

# Save cleaned dataset
clean_df = pd.DataFrame(cleaned, columns=["Question"])
clean_df.to_csv("clean_questions.csv", index=False)

print("Execution Successful")
