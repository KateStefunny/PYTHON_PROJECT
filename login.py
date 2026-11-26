"""Login and logout functions for Campus Insights.

Run the dashboard with: streamlit run app.py
"""
import hmac
import os

import streamlit as st

st.title("Registration")
def check_credentials(username: str, password: str) -> bool:
    """Compare credentials with local configuration (demo defaults)."""
    expected_user = os.getenv("DASHBOARD_USERNAME", "admin")
    expected_password = os.getenv("DASHBOARD_PASSWORD", "admin123")
    user_ok = hmac.compare_digest(username.strip().encode("utf-8"),
                                  expected_user.encode("utf-8"))
    password_ok = hmac.compare_digest(password.encode("utf-8"),
                                      expected_password.encode("utf-8"))
    return user_ok and password_ok


def login():
    """Display the login page when the current session is not authenticated."""
    if st.session_state.get("authenticated", False):
        return True

    st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }
    .block-container {max-width: 1100px; padding-top: 4rem;}
    .login-brand {background: linear-gradient(135deg, #172B4D, #3559E0);
        color: white; padding: 32px; border-radius: 18px; min-height: 330px;}
    .login-brand h1 {color: white; font-size: 2.2rem; line-height: 1.18;}
    .login-brand p {color: #DCE5FF; line-height: 1.6;}
    .login-brand small {color: #DCE5FF; letter-spacing: 2px; font-weight: 700;}
    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.1, 1], gap="large")
    with left:
        st.markdown("""
        <div class="login-brand">
          <small>CAMPUS INSIGHTS &nbsp; / &nbsp; 2026–2027</small>
          <h1>Student performance, made clearer.</h1>
          <p>Explore academic results, monitor student progress and identify
          opportunities for additional support.</p>
          <p>Academic analytics &nbsp; • &nbsp; Demonstration portal</p>
        </div>
        """, unsafe_allow_html=True)
    with right:
        with st.container(border=True):
            st.subheader("Welcome back")
            st.caption("Sign in to access your analytics dashboard.")
            with st.form("login_form", clear_on_submit=True):
                username = st.text_input("Username", placeholder="Enter your username")
                password = st.text_input("Password", type="password",
                                         placeholder="Enter your password")
                submitted = st.form_submit_button("Sign in", type="primary", width="stretch")
            if submitted:
                if check_credentials(username, password):
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username.strip()
                    st.rerun()
                else:
                    st.error("Invalid username or password. Please try again.")
            if "DASHBOARD_USERNAME" not in os.environ and "DASHBOARD_PASSWORD" not in os.environ:
                st.caption("Demo account: admin / admin123")
    return False


def logout():
    """Clear session data and return to the login page."""
    st.session_state.clear()
    st.rerun()
