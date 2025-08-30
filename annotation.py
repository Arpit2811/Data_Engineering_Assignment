import pandas as pd

# Load cleaned dataset
df = pd.read_csv("clean_questions.csv")

# Function to assign category based on keywords
def categorize_question(question):
    q = question.lower()

    if any(word in q for word in ["data science", "data analytics", "career", "skills", "tools", "python", "sql"]):
        return "Basics"
    elif any(word in q for word in ["sample", "sampling", "p-value", "hypothesis", "covariance", "correlation", "bias", "probability", "distribution"]):
        return "Statistics & Probability"
    elif any(word in q for word in ["linear regression", "logistic regression", "random forest", "svm", "support vector", "model", "roc curve", "rmse", "mse", "grid search", "parameter"]):
        return "Machine Learning"
    elif any(word in q for word in ["deep learning", "neural network", "gradient descent", "vanishing gradient", "exploding gradient", "gan", "computational graph"]):
        return "Deep Learning"
    elif any(word in q for word in ["clean", "missing values", "data cleaning", "feature selection", "dimensionality reduction", "imbalanced data", "resampling"]):
        return "Data Handling & Cleaning"
    elif any(word in q for word in ["confusion matrix", "roc curve", "false positive", "false negative", "validation", "test set", "evaluation", "mse", "rmse"]):
        return "Model Evaluation"
    elif any(word in q for word in ["time series", "stationary", "univariate", "bivariate", "multivariate", "kernel trick"]):
        return "Specialized Topics"
    else:
        return "Other"

# Function to assign difficulty
def assign_difficulty(question):
    words = str(question).split()
    length = len(words)

    #Deciding the difficulty based on the length of question
    if length <= 6:
        return "Easy"
    elif length <= 12:
        return "Medium"
    else:
        return "Hard"

# Apply both functions
df["Category"] = df["Question"].apply(categorize_question)
df["Difficulty"] = df["Question"].apply(assign_difficulty)

# Save categorized + difficulty annotated dataset
df.to_csv("categorized_questions.csv", index=False)

print("Execution Successful")
