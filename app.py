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
    
    /* Custom button styles for all 8 buttons */
    .custom-button {{
        display: block;
        width: 100%;
        margin: 5px 0;
        padding: 10px;
        background-color: #00B4D8;
        color: white;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        transition: all 0.3s;
        cursor: pointer;
    }}
    
    .custom-button:hover {{
        background-color: #0077B6;
        transform: scale(1.02);
    }}
    
    .custom-button.active {{
        background-color: #000080;  /* Navy blue */
        box-shadow: 0 0 0 2px #FFFFFF, 0 0 0 4px #000080;
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
    
    /* Additional styles for new pages */
    details {{
        margin-bottom: 10px;
        padding: 10px;
        background-color: #F8F9FA;
        border-radius: 5px;
    }}

    details summary {{
        font-weight: bold;
        cursor: pointer;
    }}

    details p {{
        margin-left: 20px;
        padding-top: 10px;
    }}
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)

# Rest of your code remains the same until the main() function

# Main App Logic
def main():
    # Company Header
    st.markdown('<div class="header">Orbt-Learn</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Complete your final year projects with excellence</div>', unsafe_allow_html=True)

    # Navigation Menu - only show if not in admin views
    if not st.session_state.admin_logged_in and not st.session_state.show_admin_login:
        # Create a container for our custom navigation
        nav_container = st.container()
        
        with nav_container:
            # Create columns for the navigation
            cols = st.columns(8)
            
            # Define our navigation items
            nav_items = [
                ("Home", "house"),
                ("Projects", "folder"),
                ("Team", "people"),
                ("Contact", "envelope"),
                ("Internship", "briefcase"),
                ("Job", "suitcase"),
                ("Education", "book"),
                ("FAQ", "question-circle")
            ]
            
            # Create each button
            for i, (item, icon) in enumerate(nav_items):
                with cols[i]:
                    # Determine if this is the active button
                    is_active = st.session_state.selected_menu == item
                    
                    # Create the button with appropriate class
                    button_html = f"""
                    <button class="custom-button {'active' if is_active else ''}" onclick="window.location.href='?page={item}'">
                        <i class="fas fa-{icon}"></i> {item}
                    </button>
                    """
                    st.markdown(button_html, unsafe_allow_html=True)
                    
                    # Add click handler
                    if st.button(item, key=f"nav_{item}", help=f"Go to {item}"):
                        st.session_state.selected_menu = item

        # Add some spacing
        st.markdown("<br>", unsafe_allow_html=True)

    # Page routing
    if st.session_state.admin_logged_in:
        admin_dashboard()
    elif st.session_state.show_admin_login:
        admin_login_page()
    else:
        if st.session_state.selected_menu == "Home":
            show_home_page()
        elif st.session_state.selected_menu == "Projects":
            show_projects_page()
        elif st.session_state.selected_menu == "Team":
            show_team_page()
        elif st.session_state.selected_menu == "Contact":
            show_contact_page()
        elif st.session_state.selected_menu == "Internship":
            show_internship_page()
        elif st.session_state.selected_menu == "Job":
            show_job_page()
        elif st.session_state.selected_menu == "Education":
            show_education_page()
        elif st.session_state.selected_menu == "FAQ":
            show_faq_page()

if __name__ == "__main__":
    main()
