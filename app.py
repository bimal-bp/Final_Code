import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2
from psycopg2 import sql

# Configure page
st.set_page_config(
    page_title="Orbt-Tech",
    page_icon="🚀",
    layout="wide"
)

# CSS styling
st.markdown("""
    <style>
    .header {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 1rem;
        color: white;
        background-color: #1E90FF;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .subheader {
        text-align:center; 
        margin-bottom:30px;
        font-size: 1.2rem;
        color: #555;
    }
    .card {
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        background-color: #f5f5f5;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .nav {
        margin-bottom: 20px;
    }
    .team-card {
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        background-color: #f5f5f5;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .contact-button {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        text-align: center;
        transition: all 0.3s;
    }
    .contact-button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    /* Style for the navigation menu */
    .st-b7 {
        background-color: #f0f2f6 !important;
        border-radius: 10px;
        padding: 10px;
    }
    .st-c7 {
        color: #1E90FF !important;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #0066CC;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Company Header with blue button style
st.markdown('<div class="header">Orbt-Tech</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Complete your final year projects with excellence</div>', unsafe_allow_html=True)

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Services", "Projects", "Team", "Contact"],
    icons=["house", "list-task", "folder", "people", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f0f2f6"},
        "icon": {"color": "orange", "font-size": "18px"}, 
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#1E90FF"},
    }
)

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="neondb",
            user="neondb_owner",
            password="npg_cVaeU8k1ofnZ",
            host="ep-snowy-bar-a59qktoz-pooler.us-east-2.aws.neon.tech",
            port="5432",
            sslmode="require"
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Create contacts table if not exists
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    project_type VARCHAR(50) NOT NULL,
                    message TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
        except Exception as e:
            st.error(f"Error creating table: {e}")
        finally:
            if conn:
                conn.close()

# Insert contact form data
def insert_contact(name, email, project_type, message):
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO contacts (name, email, project_type, message) VALUES (%s, %s, %s, %s)",
                (name, email, project_type, message)
            )
            conn.commit()
            return True
        except Exception as e:
            st.error(f"Error inserting data: {e}")
            return False
        finally:
            if conn:
                conn.close()
    return False

# Initialize database
init_db()

# Page Content
if selected == "Home":
    st.subheader("Our Services")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <b>AI/ML Projects</b>
            <ul>
                <li>Machine Learning</li>
                <li>Natural Language Processing</li>
                <li>Predictive Analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <b>Mobile Applications</b>
            <ul>
                <li>Android Development</li>
                <li>iOS Development</li>
                <li>Cross-platform Apps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <b>Web Applications</b>
            <ul>
                <li>Full Stack Development</li>
                <li>MERN/MEAN Stack</li>
                <li>Cloud Integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("Why Choose Us?")
    st.write("""
    - 100% Project Completion
    - Documentation Support
    - Regular Updates
    - Affordable Pricing
    """)
    
elif selected == "Team":
    st.subheader("Our Team")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <b>John Doe</b>
            <p>AI/ML Specialist</p>
            <p>Expert in machine learning and data science</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <b>Mike Johnson</b>
            <p>Mobile Developer</p>
            <p>Skilled in Android, iOS and cross-platform development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <b>Sarah Williams</b>
            <p>Web Developer</p>
            <p>Full stack developer with modern frameworks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <b>David Smith</b>
            <p>Project Manager</p>
            <p>Ensuring smooth project execution</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <b>Robert Brown</b>
            <p>Data Scientist</p>
            <p>Specialized in predictive analytics</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <b>Emily Davis</b>
            <p>UI/UX Designer</p>
            <p>Creating intuitive user interfaces</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="team-card">
            <b>James Wilson</b>
            <p>Backend Developer</p>
            <p>Database and server-side expert</p>
        </div>
        """, unsafe_allow_html=True)
    
elif selected == "Projects":
    st.subheader("Our Projects")
    
    st.markdown("""
    <div class="card">
        <b>Career Recommendation System</b>
        <p>AI-powered career guidance platform</p>
        <p><a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <b>Bank Customer Analysis</b>
        <p>Predictive analytics for banking sector</p>
        <p><a href="https://bankattritionprojects-tymyqz4hyygziox37gfttt.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <b>Crime Spot Prediction</b>
        <p>AI system for predicting crime hotspots</p>
        <p><a href="https://crmiespotpredict-zi269clpbwhknp8d3cqqex.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <b>Legal App</b>
        <p>Legal assistance and documentation platform</p>
        <p><a href="https://legal-app-6ovymevnmlyrcasclwtt8u.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <b>Student Performance Tracker</b>
        <p>Educational analytics dashboard</p>
        <p><a href="https://studentperformance-fvqesnqvjzxvjcpx78zheo.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <b>Water Quality Analysis</b>
        <p>Water quality monitoring system</p>
        <p><a href="https://waterqualityproject-fjfw7dmgbjgbzdestmpdsi.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
elif selected == "Contact":
    st.subheader("Contact Us")
    
    with st.form("contact_form"):
        name = st.text_input("Name*", placeholder="Your name")
        email = st.text_input("Email*", placeholder="Your email address")
        project_type = st.selectbox("Project Type*", 
                                  ["Select project type", "AI/ML", "Mobile App", "Web App", "Other"],
                                  index=0)
        message = st.text_area("Message", placeholder="Tell us about your project requirements")
        
        # Custom styled submit button
        submit_button = st.form_submit_button("Submit", type="primary")
        
        if submit_button:
            if not name or not email or project_type == "Select project type":
                st.error("Please fill all required fields (marked with *)")
            else:
                if insert_contact(name, email, project_type, message):
                    st.success("Thank you for contacting us! We'll get back to you soon.")
                    # Clear form after successful submission
                    st.experimental_rerun()
                else:
                    st.error("There was an error submitting your form. Please try again.")
