import streamlit as st
import base64

# Set up the page configuration
st.set_page_config(page_title="Shivani's Data Scientist Portfolio", layout="wide")

# Apply CSS for custom styling
st.markdown("""
    <style>
    body {
        overflow-x: hidden;
        margin: 0;
        padding: 0;
        background-color: #f0f0f0;
    }

    /* Set the background color for the entire page */
    .main {
        max-width: 100vw;
        overflow: hidden;
        background: #e3f2fd; /* Light blue background for both columns */
    }

    body {
        background: #e3f2fd; /* Light blue background */
        color: #333;
        font-family: Arial, sans-serif;
    }

    .profile-pic {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid #4CAF50; /* Green border */
        margin: 10px auto;
    }

    .green-header {
        color: #4CAF50; /* Green color for name */
        font-size: 3rem;
        text-align: left;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }

    .sub-header {
        text-align: left;
        font-size: 1.5rem;
        color: #EF4B4B;
        font-weight: bold;
    }

    .intro-text {
        font-size: 1rem;
        color: #333;
        margin-top: 1rem;
        text-align: justify;
        color: #C5705D;
        font-weight: bold;
    }

    /* Set background for content and sidebar */
    .col1 {
        background-color: #e3f2fd; /* Light blue background for sidebar */
    }

    .col2 {
        background-color: #e3f2fd; /* Light blue background for the main content */
    }

    /* Styling for the sidebar */
    .sidebar .sidebar-content {
        font-weight: bold;
        font-size: 24px;
        color: brown;
    }

    .sidebar .sidebar-header {
        font-size: 24px;
        font-weight: bold;
        color: brown;
    }
    </style>
""", unsafe_allow_html=True)

# Layout: Two columns
col1, col2 = st.columns([1, 3])

with col1:
    # Reading the image and encoding it in Base64
    image_path = "profile.jpeg"  # Make sure the path is correct relative to the app.py location
    try:
        with open(image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode()
        # Display the image with custom styling
        st.markdown(f'<img src="data:image/jpeg;base64,{encoded_image}" class="profile-pic">', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Profile image not found. Please check the file path.")

with col2:
    st.markdown('<div class="green-header">SHIVANI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Data Scientist | Machine Learning Enthusiast | Problem Solver</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-text">
    Hello! I'm a passionate Data Scientist with expertise in building machine learning models, analyzing data trends, 
    and deriving actionable insights. I thrive on solving complex problems and creating value through data.
    </div>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("<h2 style='font-weight: bold; font-size: 24px;'>Explore</h2>", unsafe_allow_html=True)

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Select an Option",  # The options in the selectbox
    ["About", "Skills", "Projects", "Contact"]
)

if menu == "About":
    st.markdown('<h2 style="color:black; text-decoration: underline;">About</h2>', unsafe_allow_html=True)

    st.markdown(""" 
        <h3 style="color:#E07B39;">Certifications:</h3>
        <ul style="color:black;">
            <li>Data Science / AI</li>
            <li>Java J2EE</li>
            <li>Web Development</li>
        </ul>
    """, unsafe_allow_html=True)
elif menu == "Skills":
    st.markdown('<h2 style="color:black; text-decoration: underline;">Skills</h2>', unsafe_allow_html=True)
    st.markdown("""
    - **Programming Languages:** Python, HTML, CSS, SQL
    - **Machine Learning:** Numpy, Pandas, Supervised & Unsupervised Learning, NLP, Decision Trees, Random Forests, KNN, SVM
    - **Data Visualization:** Tableau, Matplotlib, Seaborn
    - **Data Science & Technologies:** Deep Learning, Statistical Analysis, Predictive Modeling, Data Structures & Algorithms, Image Processing, Data Mining, Neural Networks, Database Management, Pycharm, Jupyter Notebooks
    - **Tools & Libraries:** Scikit-learn, TensorFlow, Keras, OpenCV, Git, GitHub, SQL databases (MySQL, PostgreSQL)
    """)

elif menu == "Projects":
    st.markdown('<h2 style="color:black; text-decoration: underline;">Projects</h2>', unsafe_allow_html=True)

    st.markdown("""
    - **[Intelligent Spam-Ham Detector System](https://intelligent-spam-ham-detector-sytstem-3hgxbhzjpewfjcjd2thddk.streamlit.app/):**  
      A machine learning model to classify emails as spam or ham using NLP techniques.
    - **[Movie Recommendation System](https://movie-recommendation-system-9yjcnbwsbsb6wxckhnb4ik.streamlit.app/):**  
      A recommendation system that suggests movies based on user preferences.
    - **[Heart Disease Prediction](https://github.com/shivanirakhroan28/Heart-Disease-Prediction):**  
      A predictive model to assess the likelihood of heart disease based on clinical parameters.
    - **[Uber Trip Analysis](https://github.com/shivanirakhroan28/Uber-Analysis):**  
      Analyzing Uber trip data to understand trip trends, peak hours, and driver performance.
    - **[Hotel Bookings Analysis](https://github.com/shivanirakhroan28/hotel-booking-):**  
      A detailed analysis of hotel booking data to compare pricing trends and booking patterns.
    - **[Regulatory-Affairs-of-Road-Accident-Data-2020-India](https://github.com/shivanirakhroan28/Regulatory-Affairs-of-Road-Accident-Data-2020-India):**  
       Analyzing road accident data from India in 2020 to understand trends, causes, and regulatory impacts, with recommendations for improving road safety measures.
    - **[Cryptocurrency Price Prediction](https://github.com/shivanirakhroan28/Cryptocurrency-Historical-Data-Analysis-):**  
      A machine learning model to predict cryptocurrency prices based on historical data.
    - **[student-performance-academics](https://github.com/shivanirakhroan28/student-performance-academics):**  
        A machine learning model to predict student academic performance based on various factors such as study habits, parental support, and extracurricular activities.
    - **[Image-detection-using-CNN](https://github.com/shivanirakhroan28/Image-detection-using-CNN):**  
       A deep learning project that uses Convolutional Neural Networks (CNN) for image classification & detection tasks in images.
    """)

elif menu == "Contact":
    st.markdown('<h2 style="color:black; text-decoration: underline;">Contact</h2>', unsafe_allow_html=True)

    st.markdown("""
    - **Email:** [rakhroanshivu@gmail.com](mailto:rakhroanshivu@gmail.com)
    - **LinkedIn:** [linkedin.com/in/shivani-rakhroan](https://www.linkedin.com/in/shivani-rakhroan)
    - **GitHub:** [github.com/shivanirakhroan28](https://github.com/shivanirakhroan28)
    - **Phone:** +91 9654944681
    """)
# Footer Section with Social Media Icons
st.markdown("---")
st.markdown("""
### Connect with me:
[![LinkedIn](https://img.icons8.com/ios-filled/50/99ccff/linkedin.png)](https://www.linkedin.com/in/shivani-rakhroan) 
[![GitHub](https://img.icons8.com/ios-filled/50/99ccff/github.png)](https://github.com/shivanirakhroan28) 
[![Email](https://img.icons8.com/ios-filled/50/99ccff/email-sign.png)](mailto:rakhroanshivu@gmail.com)
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color: black; color: white; padding: 10px; text-align: center;">
        © 2024 Shivani. All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
