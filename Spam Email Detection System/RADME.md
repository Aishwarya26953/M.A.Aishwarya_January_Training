Spam Email Detection System

About This Project
This project is about building a simple system that can detect whether an email is **Spam** or **Not Spam (Ham)** using Machine Learning.  
The model learns from past email messages and then predicts the category for new emails entered by the user.


Dataset Used
The dataset is stored in an Excel file:

Spam Email Detection.xlsx

Important Columns:
- `v1` → Contains the label (spam or ham)  
- `v2` → Contains the email message text  

Extra empty columns were removed during data cleaning.



What This Project Does
- Reads the dataset from Excel file  
- Cleans and prepares the data  
- Converts text into numbers using TF-IDF  
- Trains a machine learning model  
- Tests the model using new email input  
- Shows results using accuracy and confusion matrix  



Tools and Libraries
- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Jupyter Notebook / Anaconda  
