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
    .team-card {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 4px solid #2563eb;
    }
    .project-card {
        background-color: #f0f9ff;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 4px solid #1e40af;
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
    ## Why Choose Orbt-Tech?
    - 100% Project Completion Guarantee
    - Documentation & Deployment Support
    - Regular Progress Updates
    - Post-project Maintenance
    - Affordable Pricing
    """)
    
elif selected == "Our Team":
    st.header("Meet Our Expert Team")
    
    # Team Members in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <h3>Bimal Patra</h3>
            <p><b>Role:</b> AI/ML Engineer</p>
            <p><b>Expertise:</b> Machine Learning, Deep Learning, NLP</p>
            <p><b>Education:</b> M.Tech in Computer Science</p>
            <p><b>Experience:</b> 5+ years in AI development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <h3>Priya Sharma</h3>
            <p><b>Role:</b> Project Manager</p>
            <p><b>Expertise:</b> Agile Methodologies, Client Coordination</p>
            <p><b>Education:</b> MBA in IT Management</p>
            <p><b>Experience:</b> 7+ years in project management</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <h3>Ananya Gupta</h3>
            <p><b>Role:</b> ML Developer</p>
            <p><b>Expertise:</b> Predictive Modeling, Data Analysis</p>
            <p><b>Education:</b> B.Tech in Data Science</p>
            <p><b>Experience:</b> 3+ years in ML projects</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <h3>Rahul Verma</h3>
            <p><b>Role:</b> Mobile Application Developer</p>
            <p><b>Expertise:</b> Android, Flutter, React Native</p>
            <p><b>Education:</b> B.Tech in Computer Engineering</p>
            <p><b>Experience:</b> 4+ years in mobile development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <h3>Arjun Mehta</h3>
            <p><b>Role:</b> Web Application Developer</p>
            <p><b>Expertise:</b> MERN Stack, Django, Cloud Services</p>
            <p><b>Education:</b> M.Tech in Software Engineering</p>
            <p><b>Experience:</b> 6+ years in web development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <h3>Neha Kapoor</h3>
            <p><b>Role:</b> UI/UX Designer</p>
            <p><b>Expertise:</b> Figma, Adobe XD, User Research</p>
            <p><b>Education:</b> B.Des in Interaction Design</p>
            <p><b>Experience:</b> 4+ years in design</p>
        </div>
        """, unsafe_allow_html=True)
    
elif selected == "Our Projects":
    st.header("Our Completed Projects")
    
    st.markdown("""
    <div class="project-card">
        <h3>Orbt-Learn Career Recommendation System</h3>
        <p><b>Lead:</b> Bimal Patra (AI/ML Engineer)</p>
        <p><b>Description:</b> AI-powered career recommendation system using machine learning algorithms</p>
        <p><b>Technologies:</b> Python, Scikit-learn, TensorFlow, Streamlit</p>
        <p>➤ <a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" target="_blank">Live Demo</a> | 
        <a href="https://github.com/orbt-tech/career-system-reviews" target="_blank">Client Reviews</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>Bank Customer Attrition Prediction</h3>
        <p><b>Lead:</b> Priya Sharma (Project Manager)</p>
        <p><b>Description:</b> Predictive model to identify customers likely to churn</p>
        <p><b>Technologies:</b> Python, XGBoost, Flask, AWS</p>
        <p>➤ <a href="https://bankattritionprojects-tymyqz4hyygziox37gfttt.streamlit.app/" target="_blank">Live Demo</a> | 
        <a href="https://github.com/orbt-tech/bank-attrition-reviews" target="_blank">Client Reviews</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>Crime Spot Prediction System</h3>
        <p><b>Lead:</b> Ananya Gupta (ML Developer)</p>
        <p><b>Description:</b> Geographic crime prediction using historical data</p>
        <p><b>Technologies:</b> Python, GeoPandas, Folium, Heroku</p>
        <p>➤ <a href="https://crmiespotpredict-zi269clpbwhknp8d3cqqex.streamlit.app/" target="_blank">Live Demo</a> | 
        <a href="https://github.com/orbt-tech/crime-spot-reviews" target="_blank">Client Reviews</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>Legal Document Analysis App</h3>
        <p><b>Lead:</b> Rahul Verma (Mobile Developer)</p>
        <p><b>Description:</b> Mobile app for legal document analysis and summarization</p>
        <p><b>Technologies:</b> Flutter, Firebase, NLP</p>
        <p>➤ <a href="https://legal-app-6ovymevnmlyrcasclwtt8u.streamlit.app/" target="_blank">Live Demo</a> | 
        <a href="https://github.com/orbt-tech/legal-app-reviews" target="_blank">Client Reviews</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>Student Performance Analyzer</h3>
        <p><b>Lead:</b> Arjun Mehta (Web Developer)</p>
        <p><b>Description:</b> Web application for analyzing student performance trends</p>
        <p><b>Technologies:</b> React.js, Node.js, MongoDB</p>
        <p>➤ <a href="https://studentperformance-fvqesnqvjzxvjcpx78zheo.streamlit.app/" target="_blank">Live Demo</a> | 
        <a href="https://github.com/orbt-tech/student-analyzer-reviews" target="_blank">Client Reviews</a></p>
    </div>
    """, unsafe_allow_html=True)
    
elif selected == "Contact Us":
    st.header("Get In Touch")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        project = st.selectbox("Project Type", ["AI/ML", "Mobile App", "Web App", "UI/UX Design", "Other"])
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you! We'll contact you within 24 hours.")
