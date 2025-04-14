import streamlit as st
import time

# Page setup
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

# CSS Styling
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        [data-testid="stHeader"] {
            background: rgba(255, 255, 255, 0);
        }

        [data-testid="stToolbar"] {
            display: none;
        }

        .countdown-title {
            font-size: 42px;
            color: #00334d;
            font-weight: 700;
            text-align: center;
            margin-top: 20px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        .timer-box {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            margin: 20px auto;
            width: fit-content;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            font-size: 32px;
            font-weight: bold;
            color: #cc0000;
            text-align: center;
        }

        .stButton>button {
            background-color: #0099cc;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 24px;
            margin: 5px;
            transition: 0.3s ease-in-out;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        }

        .stButton>button:hover {
            background-color: #007399;
            transform: scale(1.05);
        }

        .footer-text {
            background-color: rgba(255, 255, 255, 0.8);
            text-align: center;
            font-size: 16px;
            color: #00334d;
            padding: 12px 20px;
            margin-top: 30px;
            margin-bottom: 10px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            text-shadow: 1px 1px 1px rgba(255,255,255,0.6);
        }

        hr {
            border: 1px solid #ffffff55;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='countdown-title'>⏳ Countdown Timer</h1>", unsafe_allow_html=True)

# Initialize session state
if "total_seconds" not in st.session_state:
    st.session_state.total_seconds = 0
if "paused" not in st.session_state:
    st.session_state.paused = False
if "started" not in st.session_state:
    st.session_state.started = False

# Main Box
with st.container():
    st.markdown("<div class='main-box'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        hours = st.number_input("Hours", min_value=0, step=1, key="hours")
    with col2:
        minutes = st.number_input("Minutes", min_value=0, step=1, key="minutes")
    with col3:
        seconds = st.number_input("Seconds", min_value=0, max_value=59, step=1, key="seconds")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("▶️ Start"):
            st.session_state.total_seconds = int(hours * 3600 + minutes * 60 + seconds)
            st.session_state.paused = False
            st.session_state.started = True

    with col_b:
        if st.button("⏸️ Pause"):
            st.session_state.paused = not st.session_state.paused

    with col_c:
        if st.button("🔄 Restart"):
            st.session_state.total_seconds = int(hours * 3600 + minutes * 60 + seconds)
            st.session_state.started = True
            st.session_state.paused = False

    # Timer Display
    if st.session_state.started:
        placeholder = st.empty()

        # Display current time always
        mins, secs = divmod(st.session_state.total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        time_display = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        placeholder.markdown(f"<div class='timer-box'>{time_display}</div>", unsafe_allow_html=True)

        # Countdown logic
        while st.session_state.total_seconds > 0 and st.session_state.started:
            if not st.session_state.paused:
                time.sleep(1)
                st.session_state.total_seconds -= 1
                # Update timer every second
                mins, secs = divmod(st.session_state.total_seconds, 60)
                hrs, mins = divmod(mins, 60)
                time_display = f"{hrs:02d}:{mins:02d}:{secs:02d}"
                placeholder.markdown(f"<div class='timer-box'>{time_display}</div>", unsafe_allow_html=True)
                # We avoid rerunning the script automatically, so use `st.session_state` to manage updates
                st.session_state.update()
            else:
                time.sleep(0.1)  # Pause but allow page interaction

        if st.session_state.total_seconds == 0:
            placeholder.markdown("<h2 style='text-align:center; color:green;'>⏰ Time's Up!</h2>", unsafe_allow_html=True)
            st.session_state.started = False

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div class="footer-text">Created by Sabila Aleem 💖</div>
""", unsafe_allow_html=True)


