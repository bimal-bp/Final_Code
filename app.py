import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2
from psycopg2 import sql
import random

# Configure page
st.set_page_config(
    page_title="Orbt-Tech",
    page_icon="🚀",
    layout="wide"
)

# Generate random color for project cards and backgrounds
def get_random_color():
    # Softer pastel colors that work well as backgrounds
    colors = [
        "#FFD6E0", "#C8E7FF", "#E0F9FF", "#FFF2D7", "#E8FFD7",
        "#F0E6FF", "#FFE6EE", "#E6F9FF", "#FFF0E6", "#F0FFF0",
        "#F5E6FF", "#FFE6F5", "#E6FFEC", "#FFF9E6", "#E6F5FF",
        "#FFEDE6", "#E6FFF5", "#F9E6FF", "#FFFAE6", "#E6FFFA"
    ]
    return random.choice(colors)

def get_random_accent_color():
    # Brighter accent colors
    colors = [
        "#FF6B6B", "#4CC9F0", "#7209B7", "#F72585", "#4361EE", 
        "#3A0CA3", "#4895EF", "#3F37C9", "#560BAD", "#B5179E",
        "#2EC4B6", "#E71D36", "#FF9F1C", "#011627", "#2EC4B6"
    ]
    return random.choice(colors)

# Generate a few random colors for the page
page_bg_color = get_random_color()
header_color = get_random_accent_color()
card_bg_color = get_random_color()
section_bg_color = get_random_color()

# CSS styling with random color scheme
st.markdown(f"""
    <style>
    /* Base styles */
    .stApp {{
        background-color: {page_bg_color};
    }}
    .header {{
        font-size: 2rem;
        text-align: center;
        margin-bottom: 1rem;
        color: white;
        background-color: {header_color};
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }}
    .subheader {{
        text-align:center; 
        margin-bottom:20px;
        font-size: 1rem;
        color: #6C757D;
    }}
    .card {{
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        background-color: {card_bg_color};
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {get_random_accent_color()};
    }}
    .team-card {{
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        background-color: {get_random_color()};
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {get_random_accent_color()};
    }}
    .section {{
        padding: 15px;
        margin: 15px 0;
        border-radius: 10px;
        background-color: {section_bg_color};
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .contact-button {{
        display: block;
        margin: 15px auto;
        padding: 8px 16px;
        background-color: {get_random_accent_color()};
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        text-align: center;
        transition: all 0.3s;
    }}
    .contact-button:hover {{
        background-color: {get_random_accent_color()};
        transform: scale(1.05);
    }}
    .github-badge {{
        display: inline-block;
        background-color: #212529;
        color: white !important;
        padding: 6px 12px;
        border-radius: 5px;
        margin: 8px 0;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
        border: 1px solid #495057;
    }}
    .manager-card {{
        padding: 12px;
        margin: 10px 0;
        border-radius: 8px;
        background-color: {get_random_color()};
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {get_random_accent_color()};
    }}
    .job-button {{
        display: block;
        margin: 15px auto;
        padding: 10px 20px;
        background-color: {get_random_color()};
        color: #212529;
        border: 1px solid #DEE2E6;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        text-align: center;
        transition: all 0.3s;
        width: 80%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .job-button:hover {{
        background-color: {get_random_color()};
        transform: scale(1.05);
        border-color: #ADB5BD;
    }}
    
    /* Mobile optimizations */
    @media screen and (max-width: 768px) {{
        .header {{
            font-size: 1.5rem;
            padding: 10px;
        }}
        .subheader {{
            font-size: 0.9rem;
        }}
        .card, .team-card, .manager-card {{
            padding: 10px;
            margin: 6px 0;
        }}
        .stButton>button {{
            padding: 8px 16px;
            font-size: 14px;
        }}
        /* Make columns stack on mobile */
        .st-cq {{
            flex-direction: column;
        }}
    }}
    
    /* Form styling */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stTextArea>div>div>textarea {{
        font-size: 14px !important;
        background-color: {get_random_color()} !important;
    }}
    .st-b7 {{
        background-color: {get_random_color()} !important;
        border-radius: 10px;
        padding: 8px;
    }}
    .st-c7 {{
        color: {get_random_accent_color()} !important;
        font-weight: bold;
    }}
    .stButton>button {{
        background-color: {get_random_accent_color()};
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
        width: 100%;
    }}
    .stButton>button:hover {{
        background-color: {get_random_accent_color()};
    }}
    .whatsapp-button {{
        background-color: #25D366 !important;
        color: white !important;
    }}
    .call-button {{
        background-color: #34B7F1 !important;
        color: white !important;
    }}
    
    /* Navigation menu colors */
    .st-bx {{
        background-color: {get_random_color()} !important;
    }}
    .st-c0 {{
        color: #495057 !important;
    }}
    .st-cz {{
        background-color: {get_random_accent_color()} !important;
    }}
    
    /* Project cards */
    .card a {{
        color: {get_random_accent_color()} !important;
        text-decoration: none;
        font-weight: bold;
    }}
    .card a:hover {{
        text-decoration: underline;
    }}
    
    /* Floating WhatsApp button */
    .floating-button {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #25D366;
        color: white;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }}
    @media screen and (min-width: 768px) {{
        .floating-button {{
            display: none;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# Add Font Awesome for icons
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)

# Company Header
st.markdown('<div class="header">Orbt-Tech</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Complete your final year projects with excellence</div>', unsafe_allow_html=True)

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Team", "Contact"],
    icons=["house", "folder", "people", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": get_random_color()},
        "icon": {"color": get_random_accent_color(), "font-size": "16px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#E9ECEF",
        },
        "nav-link-selected": {"background-color": get_random_accent_color()},
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

# Create contacts table if not exists (updated schema)
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Drop existing table if it has old schema
            cur.execute("DROP TABLE IF EXISTS contacts")
            # Create new table with updated schema
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    mobile VARCHAR(20) NOT NULL,
                    project_type VARCHAR(50) NOT NULL,
                    project_description TEXT NOT NULL,
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

# Insert contact form data (updated)
def insert_contact(name, email, mobile, project_type, project_description, message):
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO contacts 
                (name, email, mobile, project_type, project_description, message) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (name, email, mobile, project_type, project_description, message)
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
    # Job Career Button
    st.markdown(f"""
    <div class="section">
        <div style="text-align: center; margin-bottom: 30px;">
            <a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" class="job-button" target="_blank">
                <i class="fas fa-briefcase"></i> Find Your Perfect Job Career Path
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="section">
        <h2 style="color: {get_random_accent_color()};">Our Services</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card">
            <b>AI/ML Projects</b>
            <ul style="padding-left: 20px;">
                <li>Predictive Analytics Projects</li>
                <li>Classification Models</li>
                <li>Recommendation Systems</li>
                <li>Deep Learning Projects</li>
                <li>Unsupervised Learning</li>
                <li>Generative AI Projects</li>
                <li>Natural Language Processing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card">
            <b>Software Development</b>
            <ul style="padding-left: 20px;">
                <li>Mobile Applications (Android/iOS)</li>
                <li>Web Applications (Full Stack)</li>
                <li>MERN/MEAN Stack Development</li>
                <li>Cross-platform Apps</li>
                <li>Cloud Integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="section">
        <h2 style="color: {get_random_accent_color()};">Why Choose Us?</h2>
        <div class="card">
            <ul style="padding-left: 20px;">
                <li>100% Project Completion</li>
                <li>Documentation Support</li>
                <li>Regular Updates</li>
                <li>Affordable Pricing</li>
                <li>72+ Completed Projects</li>
                <li>Direct Project Manager Access</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
elif selected == "Team":
    st.markdown(f"""
    <div class="section">
        <h2 style="color: {get_random_accent_color()};">Our Team</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="team-card">
            <b>Bimal Patra</b>
            <p>AI/ML Specialist</p>
            <p>Expert in machine learning and data science</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card">
            <b>Rakesh Behera</b>
            <p>Mobile Developer</p>
            <p>Skilled in Android, iOS and cross-platform development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card">
            <b>Sravan Sahoo</b>
            <p>Web Developer</p>
            <p>Full stack developer with modern frameworks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="team-card">
            <b>Heema Samal</b>
            <p>Project Manager</p>
            <p>Ensuring smooth project execution</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card">
            <b>Ramhari Sasmal</b>
            <p>Data Scientist</p>
            <p>Specialized in predictive analytics</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card">
            <b>Mantu Gouda</b>
            <p>ML Developer</p>
            <p>Creating intuitive user interfaces</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card">
            <b>Pabitra Jena</b>
            <p>Backend Developer</p>
            <p>Database and server-side expert</p>
        </div>
        """, unsafe_allow_html=True)
    
elif selected == "Projects":
    st.markdown(f"""
    <div class="section">
        <h2 style="color: {get_random_accent_color()};">Our Projects</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # GitHub button in Projects section
    st.markdown(f"""
    <div class="section">
        <div style="text-align:center; margin-bottom: 20px;">
            <a href="https://github.com/bimal-bp" class="github-badge" target="_blank">
                <i class="fab fa-github"></i> View My GitHub (72+ Projects)
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <b>Right Education for Perfect Job</b>
        <p>ORBT-LeARN</p>
        <p>This app will help you choosing your right education path for your successful job career</p>
        <p>Created by - Bimal Patra</p>
        <p><a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <b>Bank Customer Analysis</b>
        <p>Predictive analytics for banking sector</p>
        <p><a href="https://bankattritionprojects-tymyqz4hyygziox37gfttt.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <b>Crime Spot Prediction</b>
        <p>AI system for predicting crime hotspots</p>
        <p><a href="https://crmiespotpredict-zi269clpbwhknp8d3cqqex.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <b>Legal App</b>
        <p>Legal assistance and documentation platform</p>
        <p><a href="https://legal-app-6ovymevnmlyrcasclwtt8u.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <b>Student Performance Tracker</b>
        <p>Educational analytics dashboard</p>
        <p><a href="https://studentperformance-fvqesnqvjzxvjcpx78zheo.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <b>Water Quality Analysis</b>
        <p>Water quality monitoring system</p>
        <p><a href="https://waterqualityproject-fjfw7dmgbjgbzdestmpdsi.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
elif selected == "Contact":
    st.markdown(f"""
    <div class="section">
        <h2 style="color: {get_random_accent_color()};">Contact Us</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Manager Contact Cards
    st.markdown(f"""
    <div class="section">
        <div style="margin-bottom: 20px;">
            <h4 style="text-align: center;">Directly Contact Our Project Managers</h4>
            <div class="manager-card">
                <b>Heema Samal (Project Manager)</b>
                <p>📞 <a href="tel:+919876543210">+91 98765 43210</a></p>
                <p>📱 <a href="https://wa.me/919876543210" target="_blank">WhatsApp</a></p>
            </div>
            <div class="manager-card">
                <b>Jasmine Kartik (Project Coordinator)</b>
                <p>📞 <a href="tel:+919876543211">+91 98765 43211</a></p>
                <p>📱 <a href="https://wa.me/919876543211" target="_blank">WhatsApp</a></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Form
    st.markdown(f"""
    <div class="section">
    """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Name*", placeholder="Your name")
        email = st.text_input("Email*", placeholder="Your email address")
        mobile = st.text_input("Mobile Number*", placeholder="Your WhatsApp number")
        project_type = st.selectbox("Project Type*", 
                                  ["Select project type", "AI/ML", "Mobile App", "Web App", "Data Science", "Other"],
                                  index=0)
        project_description = st.text_area("Project Description*", 
                                         placeholder="Detailed description of your project requirements",
                                         height=150)
        message = st.text_area("Additional Message", 
                              placeholder="Any other information you'd like to share",
                              height=100)
        
        # Custom styled submit button
        submitted = st.form_submit_button("Submit Request", type="primary")
        
        if submitted:
            if not name or not email or not mobile or project_type == "Select project type" or not project_description:
                st.error("Please fill all required fields (marked with *)")
            else:
                if insert_contact(name, email, mobile, project_type, project_description, message):
                    st.success("Thank you for contacting us! Our team will get back to you within 24 hours.")
                else:
                    st.error("There was an error submitting your request. Please try again or contact us directly.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Floating WhatsApp button for mobile
st.markdown("""
<a href="https://wa.me/919876543210" class="floating-button" target="_blank">
    <i class="fab fa-whatsapp"></i>
</a>
""", unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="section" style="text-align: center; margin-top: 50px; padding: 20px; color: #6C757D; font-size: 0.9rem;">
    <p>© 2023 Orbt-Tech. All rights reserved.</p>
    <p style="margin-top: 10px;">
        <a href="https://www.linkedin.com/company/orbt-tech" target="_blank" style="color: #6C757D; margin: 0 10px;"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/bimal-bp" target="_blank" style="color: #6C757D; margin: 0 10px;"><i class="fab fa-github"></i></a>
        <a href="https://twitter.com/orbt_tech" target="_blank" style="color: #6C757D; margin: 0 10px;"><i class="fab fa-twitter"></i></a>
    </p>
</div>
""", unsafe_allow_html=True)
