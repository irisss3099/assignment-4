import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import datetime

# Page config
st.set_page_config(page_title="Sabila Kiran | Portfolio", layout="wide")

# Sidebar navigation
st.sidebar.title("🌸 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Skills", "Contact"])

# Custom styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
    padding: 30px;
}

.section {
    background-color: rgba(255,255,255,0.95);
    border-radius: 16px;
    padding: 50px;
    margin-top: 30px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.project-card {
    background-color: #e0f2f1;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.project-card:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
}

.footer {
    text-align: center;
    padding: 30px;
    margin-top: 40px;
    font-size: 16px;
    color: white;
    background-color: #004d40;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

if page == "Home":
    # Inject CSS with typing animation
    st.markdown("""
        <style>
            .typewriter {
                overflow: hidden;
                border-right: 3px solid #004d40;
                white-space: nowrap;
                margin: 0 auto;
                letter-spacing: 2px;
                width: 0;
                font-size: 64px;
                font-weight: 800;
                color: #004d40;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                margin-top: 20px;
                animation: typing 3.5s steps(12, end) infinite, blink 0.25s step-end infinite;
            }

            @keyframes typing {
                0% { width: 0 }
                50% { width: 12ch }  /* Exact length of your name */
                100% { width: 0 }
            }

            @keyframes blink {
                0%, 100% { border-color: transparent }
                50% { border-color: #004d40 }
            }


            .description {
                font-size: 24px;
                color: #444;
                max-width: 900px;
                text-align: center;
                line-height: 1.7;
                font-family: 'Segoe UI', sans-serif;
                margin: 0 auto;
                padding-top: 20px;
            }

            .logo-container {
                display: flex;
                justify-content: center;
                margin-top: 60px;
                margin-bottom: 20px;
            }

            .circular-img {
                width: 160px;
                height: 160px;
                border-radius: 50%;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                object-fit: cover;
            }
        </style>
    """, unsafe_allow_html=True)

    # Load and encode image
    image = Image.open("sk logo.jpg")
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Show circular logo
    st.markdown(f"""
        <div class="logo-container">
            <img class="circular-img" src="data:image/png;base64,{img_str}" />
        </div>
    """, unsafe_allow_html=True)

    # Typing animated name
    st.markdown('<div class="typewriter">Sabila Kiran</div>', unsafe_allow_html=True)

    # Description
    st.markdown("""
        <div class="description">
            I’m a passionate <strong>Web Developer</strong> and a dedicated <strong>Microbiologist</strong> — blending logic, elegance, and scientific precision  
            to create <strong>interactive, responsive, and user-friendly websites</strong> using <em>Streamlit</em>, <em>HTML/CSS</em>, <em>Next.js</em>, <em>Typescript</em>, and <em>Python</em>.  
            <br><br>
            Always curious and eager to grow, I'm on a mission to evolve and make an impact in the dynamic world of tech..!!
        </div>
    """, unsafe_allow_html=True)



elif page == "About Me":
    st.markdown("""
        <style>
            .about-container {
                max-width: 850px;
                margin: 0 auto;
                padding: 20px 20px 0 20px;
                font-family: 'Segoe UI', sans-serif;
                color: #333;
                line-height: 1.8;
            }
            .about-heading {
                text-align: center;
                font-size: 48px;
                color: #004d40;
                font-weight: 800;
                margin-bottom: 30px;
            }
            .highlight {
                color: #00796b;
                font-weight: 600;
            }
            .quote {
                text-align: center;
                font-style: italic;
                color: #004d40;
                font-size: 20px;
                border-left: 4px solid #00796b;
                padding-left: 16px;
                margin: 40px 0 20px 0;
            }
        </style>

        <div class='about-container'>
            <div class='about-heading'>👩‍💻 About Me</div>
            <p>
                Hey there! I’m <span class='highlight'>Sabila Kiran</span>, a passionate <span class='highlight'>Web Developer</span> and curious <span class='highlight'>Microbiologist</span> with a unique blend of technical flair and scientific precision. 
                I recently completed my graduation from <span class='highlight'>Jinnah University</span> and currently, I’m part of the 
                <span class='highlight'>Governor’s Initiative on Generative AI, Metaverse, and Web 3.0</span> as a driven and motivated developer.
            </p>
            <p>
                I craft elegant, responsive, and user-friendly websites using technologies like <span class='highlight'>HTML</span>, 
                <span class='highlight'>CSS</span>, <span class='highlight'>TypeScript</span>, <span class='highlight'>Next.js</span>, 
                <span class='highlight'>Tailwind CSS</span>, and <span class='highlight'>Python</span>. Streamlit is one of my favorite tools to build 
                graceful and interactive applications with simplicity and speed.
            </p>
            <p>
                Beyond coding and microbiology, I’m an explorer at heart — always eager to learn, grow, and dive into new experiences. Whether I’m styling a frontend layout or analyzing microscopic life, I bring creativity, detail, and a love for problem-solving to everything I do.
            </p>
            <div class='quote'>
                “Every line of code and every cell under the microscope tells a story — and I’m here to write mine, beautifully.”
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True) 
    st.success("💡 Favorite Stack: Python | Streamlit | HTML/CSS | TypeScript | Next.js | Tailwind CSS | Scientific Research")


elif page == "Projects":
    st.markdown("""
        <style>
            .projects-section {
                padding: 40px 10px;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
            }
            .projects-heading {
                font-size: 48px;
                font-weight: 800;
                color: #004d40;
                margin-bottom: 40px;
            }
            .project-card {
                background-color: #f0fdfa;
                border: 1px solid #b2dfdb;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                margin-bottom: 20px;
                height: 100%;
                text-align: left;
            }
            .project-title {
                font-size: 20px;
                font-weight: 700;
                color: #00695c;
                margin-bottom: 10px;
            }
            .project-desc {
                font-size: 15px;
                color: #444;
                margin-bottom: 10px;
            }
            .project-link a {
                text-decoration: none;
                font-weight: 600;
                color: #00796b;
            }
        </style>

        <div class='projects-section'>
            <div class='projects-heading'>🚀 My Projects</div>
    """, unsafe_allow_html=True)

    projects = [
        ("📊 BMI Calculator", "Calculates BMI with health categories.", "https://your-link.com/bmi"),
        ("🎮 Rock Paper Scissors", "Play against computer in real-time.", "https://your-link.com/rps"),
        ("⏳ Countdown Timer", "Stylish scenic countdown timer.", "https://your-link.com/timer"),
        ("🌍 Time Zone Converter", "Roman clock and time zone viewer.", "https://your-link.com/clock"),
        ("🔐 Password Generator", "Generate secure random passwords.", "https://your-link.com/pass"),
        ("🧠 Quiz App", "Fun quiz with scoring & themes.", "https://your-link.com/quiz"),
        ("📝 To-do List", "Organize tasks beautifully.", "https://your-link.com/todo"),
        ("🔄 Unit Converter", "Convert units of measure easily.", "https://your-link.com/convert"),
        ("🌈 Mood Tracker", "Track your moods with simplicity.", "https://your-link.com/mood"),
        ("🧮 Calculator", "A stylish functional calculator.", "https://your-link.com/calc"),
        ("💬 Chat with AI", "Streamlit chatbot interface.", "https://your-link.com/chat"),
        ("🕹️ Hangman Game", "Play hangman in Python.", "https://your-link.com/hangman"),
        ("🎭 Madlib Game", "Fun interactive madlib.", "https://your-link.com/madlib"),
        ("🔢 Number Guess (Computer)", "Computer guesses your number.", "https://your-link.com/guess-comp"),
        ("🔢 Number Guess (User)", "Guess the number challenge.", "https://your-link.com/guess-user"),
        ("🐍 Snake Game", "Classic snake game in Python.", "https://your-link.com/snake"),
        ("📚 Library Manager", "Library management system.", "https://your-link.com/library"),
        ("🧠 Growth Mindset Project", "Inspirational learning journey.", "https://your-link.com/mindset"),
        ("📦 My Portfolio", "Personal portfolio website.", "https://your-link.com/portfolio"),
        ("🤖 FastAPI Chatbot", "Chatbot using FastAPI.", "https://your-link.com/fastapi"),
        ("🤖 Agent Chatbot", "AI chatbot with logic handling.", "https://your-link.com/agent"),
        ("😂 Joke Generator", "Get fun, random jokes.", "https://your-link.com/jokes"),
        ("💸 Money Making Machine", "A fun simulation app.", "https://your-link.com/money"),
    ]

    cols = st.columns(3)

    for idx, (title, desc, link) in enumerate(projects):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class='project-card'>
                    <div class='project-title'>{title}</div>
                    <div class='project-desc'>{desc}</div>
                    <div class='project-link'><a href="{link}" target="_blank">🔗 View Project</a></div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Skills":
    st.markdown("""
        <style>
                
            .skills-heading {
                font-size: 48px;
                font-weight: 800;
                color: #004d40;
                margin-bottom: 40px;
                background-color: transparent !important;
                padding: 0;
                border-radius: 0;
                box-shadow: none;
                display: block;
                text-align: center;
                font-family: 'Segoe UI', sans-serif;
            }
                
            .skills-category {
                font-size: 24px;
                color: #004d40;
                font-weight: 700;
                margin-top: 30px;
                margin-bottom: 15px;
                background-color: transparent !important;
            }

            .skill-list {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 12px;
                background-color: transparent !important;
            }

            .skill-chip {
                display: flex;
                align-items: center;
                gap: 10px;
                color: #004d40;
                font-size: 18px;
                font-weight: 600;
                padding: 10px 16px;
                border-radius: 30px;
                background-color: #e0f2f1;
                transition: all 0.3s ease;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
            }

            .skill-chip:hover {
                background-color: #b2dfdb;
                transform: translateY(-2px);
            }

            .skill-chip img {
                height: 28px;
                width: 28px;
                object-fit: contain;
                border-radius: 4px;
                background-color: transparent !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 🔥 Plain “My Skills” Heading
    st.markdown("<div class='skills-heading'>🧠 My Skills</div>", unsafe_allow_html=True)

    # 💻 Web Dev Skills
    st.markdown("<div class='skills-category'>💻 Web Developer Skills</div><div class='skill-list'>", unsafe_allow_html=True)

    web_skills = [
        ("HTML", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"),
        ("CSS", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"),
        ("Tailwind CSS", "https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg"),
        ("JavaScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"),
        ("TypeScript", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg"),
        ("React", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"),
        ("Next.js", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original-wordmark.svg"),
        ("Python", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"),
        ("Streamlit", "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg"),
        ("Git", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"),
        ("GitHub", "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"),
        ("Canva", "https://cdn.worldvectorlogo.com/logos/canva-1.svg"),
        ("Video Editing", "https://cdn-icons-png.flaticon.com/512/841/841364.png"),
    ]

    for skill, icon in web_skills:
        st.markdown(f"<div class='skill-chip'><img src='{icon}' alt='{skill}' />{skill}</div>", unsafe_allow_html=True)

    # 🔬 Microbiology Skills
    st.markdown("</div><div class='skills-category'>🔬 Microbiology & Scientific Skills</div><div class='skill-list'>", unsafe_allow_html=True)

    micro_skills = [
        "Microbial Culture",
        "Identification Techniques",
        "Microscopy",
        "Slide Preparation",
        "Biochemical Testing",
        "Lab Analysis",
        "Research Methodology",
        "Scientific Report Writing",
        "APA / MLA Referencing",
        "Critical Thinking",
        "Lab Documentation",
        "Data Analysis"
    ]

    for skill in micro_skills:
        st.markdown(f"<div class='skill-chip'>🧬 {skill}</div>", unsafe_allow_html=True)







elif page == "Contact":
    st.markdown("""
        <style>
            .contact-section {
                text-align: center;
                font-family: 'Segoe UI', sans-serif;
                padding: 40px 20px;
            }

            .contact-title {
                font-size: 36px;
                font-weight: 800;
                color: #004d40;
                margin-bottom: 10px;
            }

            .contact-desc {
                font-size: 18px;
                color: #333;
                margin-bottom: 30px;
            }

            .form-container {
                max-width: 600px;
                margin: auto;
                background-color: #f9f9f9;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
            }

            input, textarea {
                width: 100%;
                padding: 14px;
                margin-bottom: 18px;
                border: 1px solid #ccc;
                border-radius: 10px;
                font-size: 16px;
                box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
            }

            button {
                padding: 14px 32px;
                background-color: #90ee90;
                color: #004d40;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
            }

            button:hover {
                background-color: #77dd77;
                transform: scale(1.05);
            }

            .social-icons {
                margin-top: 40px;
                display: flex;
                justify-content: center;
                gap: 60px;
                font-size: 18px;
            }

            .social-icons a {
                text-decoration: none;
                text-align: center;
                transition: 0.3s ease-in-out;
                color: #004d40;
            }

            .social-icons a:hover {
                transform: scale(1.1);
                color: #00695c;
            }

            .social-icons img {
                width: 40px;
                height: 40px;
                transition: transform 0.3s ease;
            }

            .icon-label {
                font-size: 14px;
                display: block;
                margin-top: 6px;
                color: #333;
            }

            .footer {
                margin-top: 60px;
                font-size: 14px;
                color: white;
                text-align: center;
                padding: 25px 10px;
                background-color: seagreen;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="contact-section">
            <div class="contact-title">📩 Contact Me</div>
            <div class="contact-desc">Feel free to reach out or connect with me on social platforms below! 👇</div>
        </div>
    """, unsafe_allow_html=True)

    # ✅ Local message handler (no email)
    def save_message(name, email, message):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("messages.txt", "a") as f:
            f.write(f"---\nTime: {now}\nName: {name}\nEmail: {email}\nMessage: {message}\n\n")
        return True

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            save_message(name, email, message)
            st.success("✅ Thank you! Your message has been recorded.")

    # ✅ Social icons
    st.markdown("""
        <div class="social-icons">
            <a href="https://github.com/irisss3099?tab=repositories" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
                <span class="icon-label">GitHub</span>
            </a>
            <a href="https://www.linkedin.com/in/s-kiran-ss8730" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
                <span class="icon-label">LinkedIn</span>
            </a>
            <a href="mailto:workhard358900@gmail.com">
                <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" alt="Email">
                <span class="icon-label">Email</span>
            </a>
        </div>
    """, unsafe_allow_html=True)



    # ✅ Footer
st.markdown("""
        <div class="footer">
            © 2025 Sabila Kiran | All Rights Reserved.
        </div>
    """, unsafe_allow_html=True)







