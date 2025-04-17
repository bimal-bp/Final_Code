
import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2
from psycopg2 import sql
import random
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Orbt-Learn",
    page_icon="🚀",
    layout="wide"
)

# Initialize session state
def init_session_state():
    if 'admin_logged_in' not in st.session_state:
        st.session_state.admin_logged_in = False
    if 'show_admin_login' not in st.session_state:
        st.session_state.show_admin_login = False
    if 'selected_menu' not in st.session_state:
        st.session_state.selected_menu = "Home"

init_session_state()

# Generate random color for project cards
def get_random_color():
    colors = [
        "#00B4D8", "#48CAE4", "#90E0EF", "#ADE8F4", "#CAF0F8",  # Sky blue shades
        "#FF6B6B", "#4CC9F0", "#4361EE", "#3A0CA3", "#4895EF",
        "#2EC4B6", "#E71D36", "#FF9F1C", "#011627", "#1B98E0"
    ]
    return random.choice(colors)

# CSS styling with sky blue color scheme
st.markdown(f"""
    <style>
    /* Base styles */
    .header {{
        font-size: 2rem;
        text-align: center;
        margin-bottom: 1rem;
        color: white;
        background-color: #00B4D8;
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
        background-color: #F8F9FA;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {get_random_color()};
    }}
    .team-card {{
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        background-color: #F8F9FA;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #00B4D8;
    }}
    .contact-button {{
        display: block;
        margin: 15px auto;
        padding: 8px 16px;
        background-color: #00B4D8;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        text-align: center;
        transition: all 0.3s;
    }}
    .contact-button:hover {{
        background-color: #0077B6;
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
        background-color: #E9ECEF;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #0077B6;
    }}
    .job-button {{
        display: block;
        margin: 15px auto;
        padding: 10px 20px;
        background-color: white;
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
        background-color: #F8F9FA;
        transform: scale(1.05);
        border-color: #ADB5BD;
    }}
    .admin-button {{
        display: block;
        margin: 15px auto;
        padding: 10px 20px;
        background-color: #212529;
        color: white !important;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        text-align: center;
        transition: all 0.3s;
        width: 80%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-decoration: none;
    }}
    .admin-button:hover {{
        background-color: #495057;
        transform: scale(1.05);
    }}
    .back-to-home {{
        display: block;
        margin: 15px auto;
        padding: 10px 20px;
        background-color: #00B4D8;
        color: white !important;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        text-align: center;
        transition: all 0.3s;
        width: 80%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-decoration: none;
    }}
    .back-to-home:hover {{
        background-color: #0077B6;
        transform: scale(1.05);
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
    
    /* Form styling - Improved dropdown visibility */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>select,
    .stTextArea>div>div>textarea {{
        font-size: 14px !important;
        color: #212529 !important;
        background-color: white !important;
    }}
    .st-b7 {{
        background-color: #F8F9FA !important;
        border-radius: 10px;
        padding: 8px;
    }}
    .st-c7 {{
        color: #00B4D8 !important;
        font-weight: bold;
    }}
    .stButton>button {{
        background-color: #00B4D8;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
        width: 100%;
    }}
    .stButton>button:hover {{
        background-color: #0077B6;
    }}
    
    /* Navigation menu colors - Changed to sky blue */
    .st-bx {{
        background-color: #F8F9FA !important;
    }}
    .st-c0 {{
        color: #495057 !important;
    }}
    .st-cz {{
        background-color: #00B4D8 !important;
    }}
    
    /* Project cards */
    .card a {{
        color: #0077B6 !important;
        text-decoration: none;
        font-weight: bold;
    }}
    .card a:hover {{
        text-decoration: underline;
    }}
    
    /* Internship cards */
    .internship-card {{
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        background-color: #F8F9FA;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {get_random_color()};
    }}
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)
       
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
            # Create new table if not exists
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

# Get all contacts from database
def get_all_contacts():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM contacts ORDER BY created_at DESC")
            columns = [desc[0] for desc in cur.description]
            data = cur.fetchall()
            return columns, data
        except Exception as e:
            st.error(f"Error fetching data: {e}")
            return None, None
        finally:
            if conn:
                conn.close()
    return None, None

# Initialize database
init_db()

# Admin login page
def admin_login_page():
    st.title("Admin Login")
    
    with st.form("admin_login"):
        admin_id = st.text_input("Admin ID", placeholder="Enter admin ID")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        
        submitted = st.form_submit_button("Login")
        
        if submitted:
            if admin_id == "orbt-learn" and password == "orbtrbi@9":
                st.session_state.admin_logged_in = True
                st.session_state.show_admin_login = False
                st.success("Login successful!")
            else:
                st.error("Invalid credentials")
    
    if st.button("Back to Home"):
        st.session_state.show_admin_login = False

# Admin dashboard
def admin_dashboard():
    st.title("Admin Dashboard")
    st.subheader("Contact Form Submissions")
    
    columns, data = get_all_contacts()
    if columns and data:
        df = pd.DataFrame(data, columns=columns)
        
        # Add filtering options
        st.subheader("Filter Submissions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_project = st.selectbox(
                "Filter by Project Type",
                ["All"] + sorted(df['project_type'].unique().tolist())
            )
        
        with col2:
            date_sort = st.selectbox(
                "Sort by Date",
                ["Newest First", "Oldest First"]
            )
        
        with col3:
            search_term = st.text_input("Search in Messages")
        
        # Apply filters
        if filter_project != "All":
            df = df[df['project_type'] == filter_project]
        
        if search_term:
            df = df[df['project_description'].str.contains(search_term, case=False) | 
                   df['message'].str.contains(search_term, case=False, na=False)]
        
        if date_sort == "Newest First":
            df = df.sort_values('created_at', ascending=False)
        else:
            df = df.sort_values('created_at', ascending=True)
        
        # Show statistics
        st.markdown(f"""
        <div class="card" style="border-left-color: #7209B7">
            <b>📈 Submission Statistics</b>
            <p>Total Submissions: {len(df)}</p>
            <p>Last Submission: {df['created_at'].max()}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display filtered data
        st.dataframe(df, use_container_width=True, height=600)
        
        # Add bulk actions
        st.subheader("Bulk Actions")
        if st.button("Delete All Submissions"):
            conn = get_db_connection()
            if conn:
                try:
                    cur = conn.cursor()
                    cur.execute("TRUNCATE TABLE contacts RESTART IDENTITY")
                    conn.commit()
                    st.success("All submissions have been deleted")
                except Exception as e:
                    st.error(f"Error deleting data: {e}")
                finally:
                    if conn:
                        conn.close()
    else:
        st.warning("No contact submissions found in the database")
    
    if st.button("Logout"):
        st.session_state.admin_logged_in = False
        st.session_state.show_admin_login = False

# Home Page
def show_home_page():
    st.subheader("Our Services")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card" style="border-left-color: {get_random_color()}">
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
        <div class="card" style="border-left-color: {get_random_color()}">
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
    
    st.subheader("Why Choose Us?")
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <ul style="padding-left: 20px;">
            <li>100% Project Completion</li>
            <li>Documentation Support</li>
            <li>Regular Updates</li>
            <li>Affordable Pricing</li>
            <li>72+ Completed Projects</li>
            <li>Direct Project Manager Access</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Admin Button at the bottom of the page
    if st.button("Admin Login", key="admin_button"):
        st.session_state.show_admin_login = True

# Projects Page
def show_projects_page():
    st.subheader("Our Projects")
    
    # GitHub button in Projects section
    st.markdown("""
    <div style="text-align:center; margin-bottom: 20px;">
        <a href="https://github.com/bimal-bp" class="github-badge" target="_blank">
            <i class="fab fa-github"></i> View My GitHub (72+ Projects)
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>Right Education for Perfect Job</b>
        <p>ORBT-LeARN</p>
        <p>This app will help you choosing your right education path for your successful job career</p>
        <p>Created by - Bimal Patra</p>
        <p><a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>Bank Customer Analysis</b>
        <p>Predictive analytics for banking sector</p>
        <p><a href="https://bankattritionprojects-tymyqz4hyygziox37gfttt.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>Crime Spot Prediction</b>
        <p>AI system for predicting crime hotspots</p>
        <p><a href="https://crmiespotpredict-zi269clpbwhknp8d3cqqex.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>Legal App</b>
        <p>Legal assistance and documentation platform</p>
        <p><a href="https://legal-app-6ovymevnmlyrcasclwtt8u.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>Student Performance Tracker</b>
        <p>Educational analytics dashboard</p>
        <p><a href="https://studentperformance-fvqesnqvjzxvjcpx78zheo.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>PRODIGY_WebDevelopment</b>
        <p>Analytics dashboard</p>
        <p><a href="https://github.com/GVMNREDDY/PRODIGY_WebDevelopment">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card" style="border-left-color: {get_random_color()}">
        <b>Water Quality Analysis</b>
        <p>Water quality monitoring system</p>
        <p><a href="https://waterqualityproject-fjfw7dmgbjgbzdestmpdsi.streamlit.app/" target="_blank">View Project</a></p>
    </div>
    """, unsafe_allow_html=True)

# Team Page
def show_team_page():
    st.subheader("Our Team")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Bimal Patra</b>
            <p>AI/ML Specialist</p>
            <p>Expert in machine learning and data science</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Rakesh Behera</b>
            <p>Mobile Developer</p>
            <p>Skilled in Android, iOS and cross-platform development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Sravan Sahoo</b>
            <p>Web Developer</p>
            <p>Full stack developer with modern frameworks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Heema Samal</b>
            <p>Project Manager</p>
            <p>Ensuring smooth project execution</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Ramhari Samal</b>
            <p>Data Scientist</p>
            <p>Specialized in predictive analytics</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Mantu Gouda</b>
            <p>ML Developer</p>
            <p>Creating intuitive user interfaces</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Udit kakkar</b>
            <p>web Developer</p>
            <p>Creating intuitive user interfaces</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="team-card" style="border-left-color: {get_random_color()}">
            <b>Pabitra Jena</b>
            <p>Backend Developer</p>
            <p>Database and server-side expert</p>
        </div>
        """, unsafe_allow_html=True)

# Contact Page
def show_contact_page():
    st.subheader("Contact Us")
    
    # Project Manager Contact Cards
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h4 style="text-align: center;">Directly Contact Our Project Managers</h4>
        <div class="manager-card">
            <b>Reema Samal (Project Manager)</b>
            <p>📞 <a href="tel:+919390920256">+91 9390920256</a></p>
            <p>📧 <a href="mailto:heema.samal@orbt-learn.com">heema.samal@orbt-learn.com</a></p>
        </div>
        <div class="manager-card">
            <b>Bimal Kartik (Project Coordinator)</b>
            <p>📞 <a href="tel:+919348245158">+91 9348245158</a></p>
            <p>📧 <a href="mailto:bimal.kartik@orbt-learn.com">jasmine.kartik@orbt-learn.com</a></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Form with improved validation
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name*", placeholder="Your full name")
            email = st.text_input("Email Address*", placeholder="Your email address")
            
        with col2:
            mobile = st.text_input("Mobile Number*", placeholder="Your contact number")
            project_type = st.selectbox("Project Type*", 
                                     ["Select project type", "AI/ML", "Mobile App", "Web App", 
                                      "Data Science", "IoT", "Blockchain", "Other"],
                                     index=0)
        
        project_description = st.text_area("Project Description*", 
                                        placeholder="Detailed description of your project requirements\n"
                                                   "- Specific features needed\n"
                                                   "- Technologies preferred\n"
                                                   "- Deadline if any",
                                        height=150)
        
        message = st.text_area("Additional Information", 
                             placeholder="Any other information you'd like to share\n"
                                        "- Reference projects\n"
                                        "- Share your Budget \n"
                                        "- Special requirements",
                             height=100)
        
        submitted = st.form_submit_button("Submit Request", type="primary",
                                        use_container_width=True,
                                        help="We'll respond within 24 hours")
        
        if submitted:
            if not name or not email or not mobile or project_type == "Select project type" or not project_description:
                st.error("Please fill all required fields (marked with *)")
            elif not email.strip().count('@') == 1 or not email.strip().count('.') >= 1:
                st.error("Please enter a valid email address")
            elif not mobile.strip().isdigit() or len(mobile.strip()) < 10:
                st.error("Please enter a valid 10-digit mobile number")
            else:
                with st.spinner('Submitting your request...'):
                    if insert_contact(name, email, mobile, project_type, project_description, message):
                        st.success("""
                        ✅ Thank you for contacting us!
                        
                        Our team will review your request and get back to you within 24 hours.
                        """)
                        
                        st.balloons()
                        
                        st.markdown("""
                        <div class="card" style="margin-top: 20px; border-left-color: #4CC9F0">
                            <h4>Next Steps:</h4>
                            <ol>
                                <li>Our project manager will contact you within 24 hours</li>
                                <li>If you have any emergency contact our manager in the above numbers </li>
                                <li>You'll receive a project proposal with timeline and cost estimate</li>
                            </ol>
                           <p>In the meantime, you can explore our <a href="https://bimal-bp.github.io/Portfolio/" target="_blank">project portfolio</a>, check our <a href="https://github.com/bimal-bp" target="_blank">GitHub page</a>, or try our <a href="https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/" target="_blank">Career Path Finder</a>.</p>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("""
                        ❌ There was an error submitting your request.
                        
                        Please try again or contact us directly via phone or email.
                        """)
def show_education_page():
    st.title("Education & Career Guidance")

    st.header("Why spend your time exploring our website?")
    st.write("We respect your time and we provide:")

    st.write("🚀 **The Right Way to Choose Your Education Path & Job**  \n"
             "Discover how to select the best learning options for your goals")

    st.write("💡 **Practical Career Advice from Industry Professionals**  \n"
             "Get real-world insights from experts across various fields")

    st.write("🏆 **Education-to-Career Roadmaps**  \n"
             "Learn which educational choices lead to your dream jobs")

    st.write("📚 **Education Guidance**  \n"
             "Confused about what to study after 10th/12th/college? We break down all your options with pros and cons.")

    st.write("💼 **Job Explorer**  \n"
             "Discover 200+ career paths you might not have considered, with real salary ranges and growth potential.")

    st.link_button("Explore Now", "https://orbtlearn-jcrdshm6johscwfx3bavgd.streamlit.app/", 
                   help="Click to explore education and career options", 
                   type="primary")  # This makes the button blue


# Internship Page
def show_internship_page():
    st.header("🎯 Internship Opportunities")
    st.write("****-------------------------------------------------------Its a paid internship you have to pay to learn skills and Projects-----------------------------------------**** ")

    
    # Program Options Section
    with st.container(border=True):
        st.subheader("🚀 Internship Programs")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="internship-card">
                <h4>1 Month Intensive</h4>
                <p>✓ Daily mentorship</p>
                <p>✓ Certificate of Completion</p>
                <p>✓ Project Report</p>
                <p>✓ Online/Offline</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="internship-card">
                <h4>3 Month Comprehensive</h4>
                <p>✓ Multiple projects</p>
                <p>✓ Performance Grading</p>
                <p>✓ LOR for top performers</p>
                <p>✓ Detailed Reports</p>
            </div>
            """, unsafe_allow_html=True)
    
    # What We Provide Section
    st.subheader("📜 What We Provide")
    st.markdown("""
    - **Digital Certificate** (Verifiable online)
    - **Physical Certificate** (On request)
    - **Detailed Project Report**
    - **Performance Evaluation**
    - **Letter of Recommendation** (For 3-month interns)
    """)
    
    # Contact Section
    st.subheader("📞 Contact Our Program Manager")
    contact_container = st.container(border=True)
    with contact_container:
        st.markdown("""
        **Reema Samal**  
        📧 [internship@orbt-learn.com](mailto:internship@orbt-learn.com)  
        📞 [+91 9390920256](tel:+919390920256) (WhatsApp available)  
        """)
    

# Job Page

def show_job_page():
    # Initialize session state variables
    if 'show_contact' not in st.session_state:
        st.session_state.show_contact = False

    st.subheader("🚀 Best IT Job Opportunities")
    
    
    # Job Categories Section
    st.write("### Top 15 High-Demand IT Jobs:")
    st.write("### --------If you Want Freelancing Job You can join Our Team Also Contact Us.....")
    jobs = [
        "1. AI/ML Engineer",
        "2. Data Scientist",
        "3. Cloud Architect",
        "4. DevOps Engineer",
        "5. Full Stack Developer",
        "6. Cybersecurity Analyst",
        "7. Blockchain Developer",
        "8. Data Engineer",
        "9. IoT Solutions Architect",
        "10. AR/VR Developer",
        "11. Site Reliability Engineer",
        "12. Big Data Engineer",
        "13. Quantum Computing Specialist",
        "14. UI/UX Designer",
        "15. Technical Product Manager"
    ]
    
    for job in jobs:
        st.write(job)
    
    # Resume Link Section
    st.markdown("---")
    st.write("### 📝 My Resume")
    st.write("View my professional resume:")
    resume_url = "https://drive.google.com/file/d/1C9JuG5zdpdqam93NNUZVOEucvt6WyEVn/view?pli=1"
    st.markdown(f'<a href="{resume_url}" target="_blank"><button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">View My Resume</button></a>', unsafe_allow_html=True)
    
    # Career Consultation Section
    st.markdown("---")
    st.write("### 👨‍💼 Career Consultation Sessions")
    st.write("Book paid 1-on-1 sessions with industry experts:")
    
    st.write("**1-hour Session (₹850) includes:**")
    consultation_points = [
        "Comprehensive resume building",
        "LinkedIn profile optimization",
        "Personalized cover letter writing",
        "Job application strategy",
        "Interview preparation techniques",
        "Salary negotiation guidance"
    ]
    
    for point in consultation_points:
        st.write(f"- {point}")
    

    
    # Contact Section
    st.markdown("---")
    st.write("### 📩 Contact Us")
    st.write("9348245158")
    
def main():
    # Display the header in the main content area
    st.markdown('<div class="header">Orbt-Learn</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Complete your final year projects with excellence</div>', unsafe_allow_html=True)

    # Navigation menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Team", "Internship", "Job", "Education","Contact"],
        icons=["house", "folder", "people", "briefcase", "search", "book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#F8F9FA"},
            "icon": {"color": "#F72585", "font-size": "16px"},
            "nav-link": {
                "font-size": "14px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#E9ECEF",
            },
            "nav-link-selected": {"background-color": "#7209B7"},
        }
    )

    # Update session state with selected menu
    st.session_state.selected_menu = selected

    # Check for admin login state
    if st.session_state.show_admin_login:
        admin_login_page()
        return
    
    if st.session_state.admin_logged_in:
        admin_dashboard()
        return

    # Page routing based on selected menu
    if selected == "Home":
        show_home_page()
    elif selected == "Projects":
        show_projects_page()
    elif selected == "Team":
        show_team_page()
    elif selected == "Internship":
        show_internship_page()
    elif selected == "Job":
        show_job_page()
    elif selected == "Education":
        show_education_page()
    elif selected == "Contact":
        show_contact_page()

if __name__ == "__main__":
    main()
