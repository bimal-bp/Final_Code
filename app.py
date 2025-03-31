import streamlit as st
from streamlit_option_menu import option_menu

# Configure page
st.set_page_config(
    page_title="Orbt-Tech",
    page_icon="🚀",
    layout="wide"
)

# CSS styling
st.markdown("""
    <style>
    .company-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2563eb;
        text-align: center;
        margin-bottom: 1rem;
    }
    .tagline {
        font-size: 1.2rem;
        text-align: center;
        color: #4b5563;
        margin-bottom: 2rem;
    }
    .service-card {
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        background-color: #f8fafc;
        border-left: 5px solid #2563eb;
    }
    .service-title {
        font-weight: 600;
        color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# Company Header
st.markdown('<div class="company-header">Welcome to Orbt-Tech</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Complete your final year projects with excellence</div>', unsafe_allow_html=True)

# Services Section
st.subheader("Our Specializations")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div class="service-title">AI/ML Projects</div>
        <ul>
            <li>Machine Learning</li>
            <li>Natural Language Processing</li>
            <li>Predictive Analytics</li>
            <li>Deep Learning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div class="service-title">Mobile Applications</div>
        <ul>
            <li>Android (Kotlin/Java)</li>
            <li>iOS (Swift)</li>
            <li>Flutter Cross-platform</li>
            <li>React Native</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div class="service-title">Web Applications</div>
        <ul>
            <li>Full Stack Development</li>
            <li>MERN/MEAN Stack</li>
            <li>Django/Flask</li>
            <li>Cloud Integration</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Our Projects", "Our Team", "Contact Us"],
    icons=["house", "code-slash", "people-fill", "envelope"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px"},
    }
)

# Page Content
if selected == "Home":
    st.write("""
    ## Why Choose Orb-Tech?
    - 100% Project Completion Guarantee
    - Documentation & Deployment Support
    - Regular Progress Updates
    - Post-project Maintenance
    - Affordable Pricing
    """)
    
elif selected == "Our Projects":
    st.header("Our Completed Projects")
    # Add your 7 projects here with expanders
    with st.expander("AI-Based Attendance System (2023)"):
        st.write("""
        - Technologies: Python, OpenCV, Face Recognition
        - Features: Real-time face detection, Excel report generation
        - Completion: 3 months
        """)
    
elif selected == "Our Team":
    st.header("Meet Our Developers")
    # Add your 5-6 team members
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/150", caption="John Doe (AI/ML Specialist)")
    with col2:
        st.image("https://via.placeholder.com/150", caption="Jane Smith (Mobile Dev)")
    
elif selected == "Contact Us":
    st.header("Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        project = st.selectbox("Project Type", ["AI/ML", "Mobile App", "Web App"])
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you! We'll contact you within 24 hours.")
