from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Abdul Mannan"
PAGE_ICON = ":wave:"
NAME = "Abdul Mannan"
TITTLE = """ Data scientist"""
DESCRIPTION = """  
 Assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "www.abdulmannan133@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCf1IA59_Bm_bvMyvtrdCNIg",
    "LinkedIn": "https://www.linkedin.com/in/abdul-mannan-se/",
    "GitHub": "https://github.com/Abdul-Mannan-17",
    "Twitter": "https://twitter.com/mannan__01",
}
Certifications = {
    "🏆 Data Manipulation in Python: Master Python, Numpy & Pandas": "https://www.udemy.com/certificate/UC-5879a92b-b8ee-4111-a50d-8fe14809e550/",
    "🏆 Python Data Science Toolbox": "https://www.datacamp.com/completed/statement-of-accomplishment/course/c1c3a942b577ca2b839f92c093d5324617ffaf09",
    "🏆 IBM Full Stack Software Developer": "https://www.coursera.org/account/accomplishments/specialization/certificate/HXPTE5CYF8WL",
    "🏆 Big Data Analytics Workshop": "https://dicecamp.com/lms/certificate-public-link/2tgaUHMpqWDVecsyBk4IC9Q37bfoAv6rOzThNjFxLKd8PRZlYm",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.subheader(TITTLE)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy, ), SQL, VBA, C++, C#, JS
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, Classification, NLP, decision tree
- 🗄️ Databases: Postgres, MongoDB, MySQL, Oracle
"""
)
st.write('\n')
st.subheader("SOFT Skills")
st.write(
    """
- ✔️ Communication Skills
- ✔️ Problem-Solving
- ✔️ Time Management
- ✔️ Teamwork
- ✔️ Adaptability
- ✔️ Attention to Detail
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- JOB 1
st.write("🚧", "[**Houses Price Prediction Model**](https://github.com/Abdul-Mannan-17/Houses_price_prediction-Model)")
st.write(
    """
- ► Developed a Houses Price Prediction Model using XGBoost
- ► Conducted comprehensive data preprocessing, feature engineering, and exploratory data analysis to enhance model performance and interpretability.
- ► Created data visualizations and interpreted feature importance to explain the model's predictions to stakeholders.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "[**Resturant Reviews Classification Model**](https://github.com/Abdul-Mannan-17/Machine-Learning-Models/blob/main/Natural_language_processing.ipynb)")
st.write(
    """
- ► Developed a Restaurant Reviews Classification Model using NLP techniques and Gaussian Naive Bayes (GaussianNB) algorithm, achieving an 73% accuracy.
- ► Preprocessed and cleaned text data, including tasks such as tokenization, stop word removal, and stemming/lemmatization, to improve the quality of input features.
- ► Engineered textual features like TF-IDF and word embeddings to capture semantic meaning and sentiment in reviews.
- ► Conducted exploratory data analysis (EDA) and visualizations to gain insights into the dataset's characteristics, which informed feature engineering decisions.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "[**Social Network Ads Classifier**](https://github.com/Abdul-Mannan-17/Machine-Learning-Models/blob/main/K_nearest_neighbors.ipynb)")
st.write(
    """
- ► Developed a Social Network Ads Classifier using the K-Nearest Neighbors (K-NN) algorithm, achieving an 93% accuracy
- ► Conducted data preprocessing and feature scaling to ensure accurate and efficient classification of social media users' ad interactions.
- ► Engineered relevant features and performed exploratory data analysis (EDA) to better understand the data's characteristics and improve model performance.
- ► Implemented cross-validation techniques to assess the model's generalization and robustness, ensuring reliable predictions for new data.
"""
)


# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
for Certifications, link in Certifications.items():
    st.write(f"[{Certifications}]({link})")


# ---education  ---
st.write('\n')
st.subheader("Education")
st.write(
    """
-  BS SOFTWARE ENGINEERING 
-  2020-2024
-  Islamia University of Bahawalpur, Pakistan

"""
)


<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.2/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.5.2/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyB2cj1-1X1ywxMz0JypU3BgGwwKOny6CgM",
    authDomain: "digital-cv-caad4.firebaseapp.com",
    projectId: "digital-cv-caad4",
    storageBucket: "digital-cv-caad4.appspot.com",
    messagingSenderId: "1010512043108",
    appId: "1:1010512043108:web:f1cfb52c01f3b7a4cd9371",
    measurementId: "G-JFNLJMV8R4"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>