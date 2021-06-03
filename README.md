# Password-Strength-Prediction-Using Traditional ML

 ### Demo of the app: 
 
 * If wanted to see App Please click [here](https://password-strength-prediction.herokuapp.com/)
 
 ### Please Enter the value & clisk the predict button
 
 <p float="left">
  <img src="https://user-images.githubusercontent.com/74568334/120509504-db985080-c3c8-11eb-925b-ad17a4e7a932.png" width="400" />
  <img src="https://user-images.githubusercontent.com/74568334/120509748-1306fd00-c3c9-11eb-9b43-44299a9c3b88.png" width="400" /> 
  <img src="https://user-images.githubusercontent.com/74568334/120509999-4d709a00-c3c9-11eb-94a4-57d076ffe96a.png" width="400" />
  <img src="https://user-images.githubusercontent.com/74568334/120510551-d2f44a00-c3c9-11eb-8c2f-b77a96420b8c.png" width="400" /> 
</p>

### 📁 Data Collection

* Password strength data was collected on the Kaggle and this dataset contains 80000 amount of observation as well as two featuresn which are password and strength. This strength has three level which are low strength, medium strength and strong strenth
* This project has tried with SVM, Logistic Regression and XGBoosting ML algorithms wit
* The dataset used can be downloaded [Here](https://raw.githubusercontent.com/KrishArul26/Password-Strength-Prediction-Deployment/main/Password_strength_data.csv) 

### 🔑 Prerequisites
* All the dependencies and required libraries are included in the file [requirements.txt](https://github.com/KrishArul26/End-to-End-Deployment-Air-Quality-Index-prediction/blob/main/requirements.txt)
## This project has tried with SVM, Logistic Regression and XGBoosting ML algorithms with 80000 amount of the data 


### 🚀 Installation

1. Clone the repo

* git clone https://github.com/KrishArul26/Password-Strength-Prediction-Deployment.git

2. Change your directory to the cloned repo

* cd Password-Strength-Prediction-Deployment

3. Create a Python virtual environment named 'test' and activate it

* pip install virtualenv

* virtualenv test

* test\Scripts\activate

4. Now, run the following command in your Terminal/Command Prompt to install the libraries required

* pip install -r requirements.txt

### 💡 Working

1. Open terminal. Go into the cloned project directory and type the following command:

* python Password_app.py

### 🔑 Results 

* This project has tried with SVM, Logistic Regression and XGBoosting ML algorithms with 80000 amount of the data and among them SVM has selected as best performance algorithom interm of ROC values.

### Logistic-Regreesion Confiusion Matrix
<p float="left">
  <img src="https://user-images.githubusercontent.com/74568334/120512003-392d9c80-c3cb-11eb-98aa-6bdf872ec8b8.png" width="400" /> 
</p>

### SVM - Confiusion Matrix
<p float="left">
  <img src="https://user-images.githubusercontent.com/74568334/120510551-d2f44a00-c3c9-11eb-8c2f-b77a96420b8c.png" width="400" /> 
</p>
![SVM_Confusion_Matrix](https://user-images.githubusercontent.com/74568334/120512578-ca047800-c3cb-11eb-920c-624ded17fbf0.png)

### XGBoosting - Confiusion Matrix
<p float="left">
  <img src="https://user-images.githubusercontent.com/74568334/120510551-d2f44a00-c3c9-11eb-8c2f-b77a96420b8c.png" width="400" /> 
</p>
![XGBosst_Confusionmatrx](https://user-images.githubusercontent.com/74568334/120512243-73973980-c3cb-11eb-8326-8e9a8931fe45.png)

# Conclusion
### Among those model SVM has been selected because the SVM has a higher ROC-Value than the logistic regression model.

