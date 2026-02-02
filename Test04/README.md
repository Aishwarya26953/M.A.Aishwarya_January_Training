Heart Disease Prediction Using Supervised Machine Learning

Project Title
Heart Disease Prediction Using Supervised Machine Learning Algorithms

Problem Statement

The aim of this project is to predict whether a person has heart disease or not using different medical and health-related features such as age, blood pressure, cholesterol, and heart rate. This is a supervised learning classification problem where different machine learning models are trained and tested to check which model gives better accuracy and performance.

Dataset Description

In this project, I used a heart disease dataset which is saved inside the GitHub repository in the dataset folder as heart_disease_dataset.csv.

The dataset contains patient health information with the following columns:

Age
Sex
Chest pain type (cp)
Resting blood pressure (trestbps)
Cholesterol (chol)
Fasting blood sugar (fbs)
Resting ECG (restecg)
Maximum heart rate achieved (thalach)
Exercise induced angina (exang)
Target (heart disease)

Target Column

target = 1 means the person has heart disease
target = 0 means the person does not have heart disease
The dataset file is directly included in the repository and not linked from any external source.

Data Cleaning and Preprocessing Steps
1. Handling Missing Values
First, I checked for missing values using df.isnull().sum(). There were no missing values in the dataset, so I did not need to remove or fill any rows.

2. Fixing Data Types
I checked the data types of all columns using df.dtypes to make sure the data was in the correct format for applying machine learning models.

3. Removing Duplicate Records
I checked for duplicate rows using df.duplicated().sum() and removed them to make sure the dataset does not contain repeated data.

4. Encoding Categorical Variables
Some columns contained categorical values, so I converted them into numerical format using one-hot encoding with get_dummies().

5. Feature Scaling
I applied StandardScaler to scale the numerical values because models like KNN and SVM work better when all features are in the same range.

6. Train-Test Split
I split the dataset into:

80% training data
20% testing data
This helps in testing the model on unseen data.

Algorithms Used

The following supervised machine learning algorithms were used in this project:

1.Linear Regression (used as a baseline and converted into classification)
2.Decision Tree Classifier
3.Random Forest Classifier
4.K-Nearest Neighbors (KNN)
5.Support Vector Machine (SVM)

Evaluation Metrics and Results

To evaluate the models, I used the following classification metrics:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

Results Summary

From the results, I observed that Random Forest and SVM gave better accuracy compared to the other models. KNN also performed well after feature scaling. Linear Regression gave lower accuracy because it is mainly designed for regression problems and not classification.

Conclusion / Observations

In this project, I learned how important data cleaning and preprocessing are before applying machine learning models. I also understood how different models behave on the same dataset and how to compare them using evaluation metrics like accuracy, precision, recall, and F1-score.

Overall, this project helped me gain practical understanding of supervised machine learning and model evaluation.
