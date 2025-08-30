# Data_Engineering_Assignment
Data Engineering Assignment for Parishak.ai

# About The Project
In order to prepare the dataset for use in learning or training AI models, the objective was to gather interview questions from the Data Science domain, clean the data, and then add helpful labels (tags).


# What I Did
1. Collected Questions
Used BeautifulSoup and Requests Library in Python to scrape the data (interview questions) from interviewbit and then used Pandas to save the collected data in csv format (collected data is raw)

2. Removed duplicates and empty rows.
Fixed text formatting (lowercase, no extra spaces or symbols) using Regex and then saved the cleaned version in clean_questions.csv.

3.Added Labels (Annotation)
I defined two labels for each question:
 a. Category Example: Machine Learning, Statistics, Deep Learning, Data Cleaning, Basics, etc.
 b. Difficulty: Easy, Medium, Hard (depending upon the length of the questions)
by Writing a small Python script to tag each question.
Final labeled file is annotated_questions.csv.


# Tools Used
1. Python - as the main language
2. BeautifulSoup  and Requests - for web scraping
3. Pandas and re - for cleaning and saving, labelling and storing the collected data into csv format


# Difficulties Faced
1. Collecting enough relevant Data Science interview questions took time.
2. While cleaning, I had to make sure duplicates and formatting issues were handled carefully.
3. Designing good categories was tricky because some questions could fit into more than one topic.
4. Deciding the difficulty level (Easy, Medium, Hard) was subjective, so I had to rely on my own
judgment and standard interview expectations.
5. Balancing automation and manual tagging  the script helped a lot, but I still had to check results manually to make sure they made sense.
   
