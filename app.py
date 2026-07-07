import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="EduPro Personalized Learning Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduPro Personalized Learning Dashboard")

# -----------------------------
# Load Data
# -----------------------------

@st.cache_data
def load_data():

    learners = pd.read_csv("clustered_learners.csv")

    courses = pd.read_csv(
        "dataset_EduPro/EduPro Online Platform.xlsx - Courses.csv"
    )

    transactions = pd.read_csv(
        "dataset_EduPro/EduPro Online Platform.xlsx - Transactions.csv"
    )

    return learners, courses, transactions


learners, courses, transactions = load_data()

st.sidebar.title("Navigation")

user_id = st.sidebar.selectbox(

    "Select Learner",

    learners["UserID"]

)

category_filter = st.sidebar.selectbox(

    "Course Category",

    ["All"] + sorted(courses["CourseCategory"].dropna().unique())

)

level_filter = st.sidebar.selectbox(

    "Course Level",

    ["All"] + sorted(courses["CourseLevel"].dropna().unique())

)

st.header("👤 Learner Profile")

user = learners[learners["UserID"] == user_id].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Age", user["Age"])

col2.metric("Gender", user["Gender"])

col3.metric("Cluster", int(user["Cluster"]))

col1.metric(
    "Preferred Category",
    user["PreferredCategory"]
)

col2.metric(
    "Preferred Level",
    user["PreferredLevel"]
)

col3.metric(
    "Total Courses",
    int(user["TotalCourses"])
)

st.header("📊 Cluster Distribution")

fig = px.histogram(

    learners,

    x="Cluster",

    color="Cluster"

)

st.plotly_chart(fig, use_container_width=True)