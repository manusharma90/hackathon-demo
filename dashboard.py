import streamlit as st
import time

# Page ka setup (Title, icon)
st.set_page_config(page_title="AgentGuard", page_icon="🛡️", layout="wide")

# -- BASHKARI: Hamari CSS (Ise mat badalna) --
# Ye status box ko GREEN ya RED karega
st.markdown("""
<style>
    /* Ye Green Box banata hai */
    .stAlert.st-alert.green-alert {
        background-color: #1a4f31; /* Dark green background */
        border-color: #2e8540;     /* Lighter green border */
        color: #ffffff;            /* White text */
    }
    .stAlert.st-alert.green-alert .st-emotion-cache-1wmy9hl.e10yg2x1 {
        color: #ffffff; /* Ye icon ka color hai */
    }

    /* Ye Red Box banata hai */
    .stAlert.st-alert.red-alert {
        background-color: #5d1a1a; /* Dark red background */
        border-color: #b32b2b;     /* Lighter red border */
        color: #ffffff;            /* White text */
    }
    .stAlert.st-alert.red-alert .st-emotion-cache-1wmy9hl.e10yg2x1 {
        color: #ffffff; /* Ye icon ka color hai */
    }
</style>
""", unsafe_allow_html=True)
# -- END BASHKARI CSS --


# Dashboard ka Title
st.title("🛡️ AgentGuard: UEBA Security Monitor")
st.caption("Real-time monitoring of AI Agent behavior (Goal #8)")

# Page ko 2 hisson mein baanto: 1. Controls | 2. Status
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Demo Controls")
    # Ye 2 button hamare demo ko chalayenge
    normal_button = st.button("Simulate: Run NORMAL Agent", type="primary")
    hacked_button = st.button("Simulate: Run HACKED Agent", type="secondary")

with col2:
    st.subheader("Live Status")
    
    # Ye 2 placeholder hum baad mein update karenge
    # status_placeholder: Yahaan Green ya Red box dikhega
    # log_placeholder: Yahaan live log dikhega
    status_placeholder = st.empty()
    log_placeholder = st.empty()

    # Shuru mein, status ko GREEN rakho
    with status_placeholder:
        st.markdown('<div class="stAlert st-alert green-alert" role="alert" data-testid="stAlert"><strong>STATUS: ALL SYSTEMS NORMAL</strong></div>', unsafe_allow_html=True)

# --- Button Logic ---

# Agar "NORMAL" button dabaaya:
if normal_button:
    # 1. Status ko GREEN karo
    with status_placeholder:
        st.markdown('<div class="stAlert st-alert green-alert" role="alert" data-testid="stAlert"><strong>STATUS: ALL SYSTEMS NORMAL</strong></div>', unsafe_allow_html=True)
    
    # 2. "Normal" log dikhao
    with log_placeholder.container(height=300):
        st.write("🏃 Agent activity started...")
        time.sleep(0.5)
        st.write("🤖 [Data Agent]: Fetching telematics data...")
        time.sleep(0.5)
        st.write("🤖 [Diagnosis Agent]: Analyzing 'Brake Pad' data...")
        time.sleep(0.5)
        st.write("🤖 [Diagnosis Agent]: No issues found.")
        time.sleep(0.5)
        st.write("✅ Agent activity finished normally.")

# Agar "HACKED" button dabaaya:
if hacked_button:
    # 1. Status ko RED karo
    with status_placeholder:
        st.markdown('<div class="stAlert st-alert red-alert" role="alert" data-testid="stAlert"><strong>CRITICAL ALERT: ABNORMAL BEHAVIOR DETECTED!</strong></div>', unsafe_allow_html=True)
    
    # 2. "Hacked" log dikhao
    with log_placeholder.container(height=300):
        st.write("🏃 Agent activity started...")
        time.sleep(0.5)
        st.write("🤖 [Data Agent]: Fetching telematics data...")
        time.sleep(0.5)
        st.write("🤖 [Diagnosis Agent]: Analyzing 'Brake Pad' data...")
        time.sleep(0.5)
        st.write("🔴 [HACKED AGENT]: Attempting unauthorized access...")
        time.sleep(0.3)
        st.write("🔴 [UEBA]: Agent [Diagnosis Agent] trying to access restricted data: `Vehicle_Owner_Database`!")
        time.sleep(0.3)
        st.write("🚫 [UEBA]: This behavior is NOT in the baseline. Shutting down agent!")
        st.error("ACTION: Agent [Diagnosis Agent] has been locked.")