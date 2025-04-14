import streamlit as st

# Page Config
st.set_page_config(page_title="Mad Libs Game", page_icon="📝", layout="centered")

# Custom CSS for styling with transitions, background & vintage story card
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #f3e9dc, #fef7f1);
    }

    .title-box {
        background: url("https://www.transparenttextures.com/patterns/wood-pattern.png"), linear-gradient(to right, #d2b48c, #deb887);
        background-blend-mode: overlay;
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 30px;
        transition: all 0.4s ease-in-out;
        border: 1px solid #bfa88b;
    }

    .title-box:hover {
        transform: scale(1.01);
        box-shadow: 0 4px 20px rgba(184, 134, 11, 0.3);
    }

    .title {
        font-size: 45px;
        font-weight: bold;
        color: #3e2f1c;
        text-align: center;
        margin: 0;
        letter-spacing: 1px;
        text-shadow: 1px 1px 0 #fdf5e6;
    }

    .subtitle {
        font-size: 20px;
        text-align: center;
        margin-top: 10px;
        color: #5c3d2e;
    }

    .story-box {
        background: url("https://www.transparenttextures.com/patterns/wood-pattern.png");
        background-size: cover;
        background-position: center;
        padding: 60px 50px;
        border-radius: 12px;
        color: #3e2f1c;
        font-family: 'Georgia', serif;
        font-size: 19px;
        line-height: 1.8;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #bfa88b;
        margin-top: 20px;
        text-shadow: 1px 1px 0 #fdf5e6;
    }

    .footer {
        font-size: 15px;
        color: #8d6e63;
        text-align: center;
        margin-top: 50px;
        padding: 10px;
        background-color: #f3e5ab;
        border-radius: 10px;
    }
    .stButton > button {
        background: linear-gradient(to right, #a97454, #8b5e3c);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 8px;
        font-weight: bold;
        font-size: 18px;
        transition: transform 0.3s ease-in-out;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #8b5e3c, #a97454);
        transform: scale(1.05); /* Slight scale effect on hover */
    }

    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="title-box">
        <h1 class="title">🎉 Mad Libs Story Generator</h1>
        <p class="subtitle">Fill in the blanks below and watch your silly story come to life 🧠📖</p>
    </div>
""", unsafe_allow_html=True)

# Form Inputs
with st.form("mad_libs_form"):
    col1, col2 = st.columns(2)
    with col1:
        adjective = st.text_input("✨ Enter an adjective:")
        animal = st.text_input("🦁 Enter an animal:")
        verb = st.text_input("🏃 Enter a verb:")
    with col2:
        exclamation = st.text_input("😲 Enter an exclamation:")
        noun = st.text_input("📦 Enter a noun:")
        verb_past = st.text_input("🎬 Enter a verb (past tense):")
    
    submitted = st.form_submit_button("🚀 Create My Story")

# Display story
if submitted:
    if all([adjective, animal, verb, exclamation, noun, verb_past]):
        story = f"""
        Today I went to the zoo and saw a really **{adjective}** {animal} jumping up and down in its tree.  
        It **{verb}** through the large tunnel that led to its **{noun}**.  
        I got so excited, I yelled, "**{exclamation}!**"  
        Then I **{verb_past}** all the way home.
        """
        st.markdown("### 📖 Your Mad Libs Story:")
        st.markdown(f'<div class="story-box">{story}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please fill in all the blanks to generate your story!")

# Footer
st.markdown('<div class="footer">🧁 Developed with creativity by <strong>Sabila Aleem</strong> 💥</div>', unsafe_allow_html=True)
