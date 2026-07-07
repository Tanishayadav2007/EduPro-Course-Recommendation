# 🎓 EduPro Personalized Learning Recommendation System

<p align="center">
  <b>AI-powered Personalized Learning Analytics and Recommendation Dashboard</b>
</p>

---

## 📌 Project Overview

EduPro Personalized Learning Recommendation System is a machine learning and data analytics project designed to provide personalized learning insights for online learners.

Most online learning platforms follow a **one-size-fits-all approach**, where every learner receives similar course recommendations. This project aims to overcome this limitation by analyzing learner behavior, preferences, and course interactions to create a personalized learning experience.

The system uses machine learning techniques to identify similar learner groups and provides an interactive dashboard for exploring learner profiles, preferences, and learning patterns.

---

# 🎯 Problem Statement

Online learning platforms face several challenges:

- Lack of personalized course recommendations
- Difficulty understanding individual learner behavior
- Same learning path for different types of learners
- Limited insights into learner preferences and interests

EduPro addresses these challenges by using data-driven approaches to analyze learners and create meaningful learner segments.

---

# 💡 Project Objectives

The main objectives of this project are:

- Analyze learner behavior and preferences
- Identify different learner groups using machine learning
- Provide personalized learner insights
- Visualize learning patterns through an interactive dashboard
- Support personalized course discovery

---

# 🚀 Features

## 👤 Learner Profile Analysis

The dashboard provides detailed information about selected learners:

- User ID
- Age
- Gender
- Preferred Course Category
- Preferred Learning Level
- Total Courses Enrolled
- Learner Cluster

---

## 📊 Learner Segmentation

Machine learning clustering techniques are used to group learners based on similar characteristics.

This helps identify:

- Similar learning patterns
- Learner behavior groups
- Course preferences
- Different learner segments

---

## 📚 Course Filtering

Users can explore courses based on:

- Course Category
- Course Level

This helps learners discover courses according to their interests and learning requirements.

---

## 📈 Interactive Dashboard

The project provides an interactive web dashboard built using Streamlit.

Dashboard includes:

- Learner profile visualization
- Cluster distribution analysis
- Interactive charts
- Data exploration features

---

# 🛠️ Technologies Used

## Programming Language

- Python


## Data Analysis

- Pandas
- NumPy


## Machine Learning

- Scikit-learn


## Data Visualization

- Plotly


## Dashboard Development

- Streamlit


## Deployment

- Streamlit Community Cloud

---

# 📂 Project Structure

```
EduPro-Personalized-Learning-Dashboard/

│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── clustered_learners.csv
│
└── dataset_EduPro/
    │
    ├── EduPro Online Platform.xlsx - Courses.csv
    │
    └── EduPro Online Platform.xlsx - Transactions.csv

```

---

# 📊 Dataset Description

The project uses the EduPro Online Platform dataset.

## Learner Dataset

Contains learner-related information:

- UserID
- Age
- Gender
- Learning preferences
- Course enrollment details
- Cluster information


## Course Dataset

Contains course information:

- Course ID
- Course Name
- Course Category
- Course Level


## Transaction Dataset

Contains learner-course interaction data:

- User enrollment details
- Course activity
- Learning history

---

# 🧠 Machine Learning Workflow

## 1. Data Collection

Collected learner, course, and transaction data from the EduPro online learning platform.

---

## 2. Data Preprocessing

Performed:

- Data cleaning
- Missing value handling
- Data transformation
- Feature preparation

---

## 3. Exploratory Data Analysis

Analyzed:

- Learner demographics
- Course preferences
- Learning patterns
- User behavior

---

## 4. Feature Engineering

Created useful learner features:

- Total courses enrolled
- Preferred category
- Preferred learning level
- Learner behavior indicators

---

## 5. Machine Learning Model

Applied clustering techniques to group learners with similar characteristics.

The clustering process helps identify different learner segments based on their learning behavior.

---

## 6. Dashboard Development

Developed an interactive Streamlit dashboard to display:

- Learner profiles
- Cluster distribution
- Course insights
- Personalized learning information

---

# ⚙️ Installation and Setup

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

---

## Step 2: Navigate to Project Folder

```bash
cd EduPro-Personalized-Learning-Dashboard
```

---

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 4: Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

The project requires the following Python libraries:

```
streamlit
pandas
numpy
plotly
scikit-learn
openpyxl
```

---

# 🖥️ Dashboard Screenshots

Add screenshots of your dashboard here.

Example:

```
1. Dashboard Home Page

2. Learner Profile Section

3. Cluster Distribution Visualization

4. Course Filtering Section
```

---

# 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

Deployment Steps:

1. Upload project files to GitHub
2. Create a Streamlit Cloud account
3. Connect GitHub repository
4. Select `app.py`
5. Deploy the application

---

# 🔮 Future Enhancements

Future improvements include:

- Personalized course recommendation engine
- Collaborative filtering recommendation system
- Content-based recommendation model
- AI chatbot for learner assistance
- Learning progress prediction
- Skill gap analysis
- Real-time recommendations

---

# 📌 Project Outcomes

This project demonstrates:

✅ Data preprocessing  
✅ Exploratory Data Analysis  
✅ Machine Learning clustering  
✅ Personalized learning concepts  
✅ Interactive dashboard development  
✅ ML application deployment  

---

# 👩‍💻 Author

**Tanisha Yadav**

---

# ⭐ Acknowledgement

This project was developed to explore the application of Artificial Intelligence, Machine Learning, and Data Analytics in creating personalized learning experiences.
