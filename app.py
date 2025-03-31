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
    
elif selected == "Our Team":
    st.header("Meet Our Expert Team")
    
    # Team Members List
    st.markdown("""
    <div style="background-color:#f8fafc; padding:20px; border-radius:10px; margin-bottom:20px;">
        <h3 style="color:#2563eb;">Our Core Team</h3>
        <ol>
            <li><b>Bimal Patra</b> - AI/ML Engineer (Project: Career Recommendation System)</li>
            <li><b>Priya Sharma</b> - Project Manager (Project: Bank Customer Attrition Prediction)</li>
            <li><b>Ananya Gupta</b> - ML Developer (Project: Crime Spot Prediction System)</li>
            <li><b>Rahul Verma</b> - Mobile Application Developer (Project: Legal Document Analysis App)</li>
            <li><b>Arjun Mehta</b> - Web Application Developer (Project: Student Performance Analyzer)</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Projects Assignment with Review Links
    st.subheader("Current Projects & Reviews")
    st.markdown("""
    <div style="background-color:#f8fafc; padding:20px; border-radius:10px;">
        <h4 style="color:#2563eb;">Active Projects</h4>
        <ul>
            <li><b>Orbt-Learn Career System</b> - Bimal Patra (AI/ML) 
                <br>➤ <a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" target="_blank">Live Demo</a> | 
                <a href="https://github.com/orbt-tech/career-system-reviews" target="_blank">Client Reviews</a></li>
            
            <li><b>Bank Attrition Prediction</b> - Priya Sharma (Project Lead) 
                <br>➤ <a href="https://bankattritionprojects-tymyqz4hyygziox37gfttt.streamlit.app/" target="_blank">Live Demo</a> | 
                <a href="https://github.com/orbt-tech/bank-attrition-reviews" target="_blank">Client Reviews</a></li>
            
            <li><b>Crime Spot Prediction</b> - Ananya Gupta (ML Dev) 
                <br>➤ <a href="https://crmiespotpredict-zi269clpbwhknp8d3cqqex.streamlit.app/" target="_blank">Live Demo</a> | 
                <a href="https://github.com/orbt-tech/crime-spot-reviews" target="_blank">Client Reviews</a></li>
            
            <li><b>Legal Document App</b> - Rahul Verma (Mobile Dev) 
                <br>➤ <a href="https://legal-app-6ovymevnmlyrcasclwtt8u.streamlit.app/" target="_blank">Live Demo</a> | 
                <a href="https://github.com/orbt-tech/legal-app-reviews" target="_blank">Client Reviews</a></li>
            
            <li><b>Student Analyzer</b> - Arjun Mehta (Web Dev) 
                <br>➤ <a href="https://studentperformance-fvqesnqvjzxvjcpx78zheo.streamlit.app/" target="_blank">Live Demo</a> | 
                <a href="https://github.com/orbt-tech/student-analyzer-reviews" target="_blank">Client Reviews</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
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
