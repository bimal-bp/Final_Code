def show_home_page():
    st.subheader("Our Services")
    
    # New Career and Job Buttons Section
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h3>Looking for Opportunities?</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚀 Career Opportunities", key="career_button", 
                    help="Explore internships and training programs"):
            st.session_state.show_career_opportunities = True
            st.session_state.show_job_opportunities = False
    
    with col2:
        if st.button("💼 Freelance Jobs", key="job_button", 
                    help="Find freelance and project-based work"):
            st.session_state.show_job_opportunities = True
            st.session_state.show_career_opportunities = False
    
    # Career Opportunities Section
    if st.session_state.get('show_career_opportunities', False):
        st.markdown("""
        <div class="card" style="border-left-color: #4CC9F0; margin-top: 20px;">
            <h4>🎓 Internship Programs</h4>
            <ul>
                <li><b>AI/ML Internship</b> - 3 months program with hands-on projects</li>
                <li><b>Web Development Internship</b> - Learn full stack development</li>
                <li><b>Data Science Internship</b> - Work on real-world datasets</li>
                <li><b>Mobile App Development</b> - Build Android/iOS applications</li>
            </ul>
            <p><b>Benefits:</b> Certificate, Letter of Recommendation, Stipend for top performers</p>
            <p><a href="#contact" style="color: #0077B6;">Apply Now →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Back to Services", key="back_services1"):
            st.session_state.show_career_opportunities = False
    
    # Job Opportunities Section
    elif st.session_state.get('show_job_opportunities', False):
        st.markdown("""
        <div class="card" style="border-left-color: #4361EE; margin-top: 20px;">
            <h4>💻 Freelance Opportunities</h4>
            <ul>
                <li><b>AI Model Development</b> - ₹8,000-15,000 per project</li>
                <li><b>Website Development</b> - ₹5,000-20,000 per project</li>
                <li><b>Mobile App Development</b> - ₹10,000-30,000 per project</li>
                <li><b>Data Analysis Projects</b> - ₹4,000-12,000 per project</li>
            </ul>
            <p><b>Requirements:</b> Portfolio or GitHub profile, Availability for weekly syncs</p>
            <p><a href="#contact" style="color: #0077B6;">Apply for Freelance Work →</a></p>
        </div>
        
        <div class="card" style="border-left-color: #3A0CA3; margin-top: 15px;">
            <h4>🏆 Current Openings</h4>
            <ul>
                <li><b>Python Developer</b> - Part-time (10-15 hrs/week)</li>
                <li><b>React Native Developer</b> - Project-based</li>
                <li><b>Data Annotation Specialist</b> - Flexible hours</li>
                <li><b>Technical Content Writer</b> - AI/ML topics</li>
            </ul>
            <p><b>Perks:</b> Flexible timing, Remote work, Performance bonuses</p>
            <p><a href="#contact" style="color: #0077B6;">Submit Your Profile →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Back to Services", key="back_services2"):
            st.session_state.show_job_opportunities = False
    
    # Original Services Section (only shown when not viewing opportunities)
    if not st.session_state.get('show_career_opportunities', False) and not st.session_state.get('show_job_opportunities', False):
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


/* New button styles */
.stButton>button[kind="secondary"] {
    background-color: white !important;
    color: #212529 !important;
    border: 1px solid #DEE2E6 !important;
    height: 80px;
    font-size: 1.1rem !important;
    margin: 10px 0;
}

.stButton>button[kind="secondary"]:hover {
    background-color: #F8F9FA !important;
    transform: scale(1.02);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* Opportunity cards */
.opportunity-card {
    padding: 15px;
    margin: 10px 0;
    border-radius: 8px;
    background-color: #F8F9FA;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border-left: 4px solid #00B4D8;
}

.opportunity-card h4 {
    color: #212529;
    margin-top: 0;
}

.opportunity-card ul {
    padding-left: 20px;
}

.opportunity-badge {
    display: inline-block;
    background-color: #E9ECEF;
    color: #212529 !important;
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.8rem;
    margin-right: 5px;
    margin-bottom: 5px;
}

def init_session_state():
    if 'admin_logged_in' not in st.session_state:
        st.session_state.admin_logged_in = False
    if 'show_admin_login' not in st.session_state:
        st.session_state.show_admin_login = False
    if 'selected_menu' not in st.session_state:
        st.session_state.selected_menu = "Home"
    if 'show_career_opportunities' not in st.session_state:
        st.session_state.show_career_opportunities = False
    if 'show_job_opportunities' not in st.session_state:
        st.session_state.show_job_opportunities = False
