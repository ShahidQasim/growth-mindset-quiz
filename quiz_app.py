import streamlit as st
import random


st.set_page_config(
    page_title="Quiz App",
    page_icon="🎓",
    layout="centered" 
)

st.markdown("""
    <style>
    /* Make content width responsive */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* Style radio buttons for better touch targets */
    .stRadio > label {
        padding: 15px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin: 5px 0;
        display: block;
    }

    .stButton > button {
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
    }

    
    h1 {
        font-size: calc(1.5rem + 1vw) !important;
        text-align: center;
    }
    h2 {
        font-size: calc(1.2rem + 1vw) !important;
    }
    p {
        font-size: calc(1rem + 0.5vw) !important;
    }

    /* Make progress bar more visible */
    .stProgress > div > div {
        height: 15px;
        background-color: #4CAF50;
    }

    /* Improve sidebar visibility on mobile */
    @media (max-width: 768px) {
        .css-1d391kg {
            width: 100%;
        }
    }

    /* Center the columns container */
    .css-1r6slb0 {  /* This targets the columns container */
        max-width: 800px;
        margin: 0 auto !important;
    }

    /* Center content inside column 1 */
    [data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    /* Make sure the text container uses full width */
    [data-testid="column"] > div {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)


quiz_data = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["London", "ICT", "lahore", "karachi"],
        "correct": "ICT"
    },
    {
        "question": "Which planet is known as the Cold Planet?",
        "options": ["Jupiter", "Neptune", "Venus", "Saturn"],
        "correct": "Neptune"
    },
    {
        "question": "What is 2 + 4?",
        "options": ["3", "4", "5", "6"],
        "correct": "6"
    },
    {
        "question": "Who painted the sun flowe?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "correct": "Vincent van Gogh"
    },
    {
        "question": "Which programming language is this quiz written in?",
        "options": ["Java", "Python", "JavaScript", "C++"],
        "correct": "Python"
    }
]


if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

if 'score' not in st.session_state:
    st.session_state.score = 0

if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False


st.title("🎓 SHAHID GIAIC QUIZ APPLICATION")


st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
        <div style='text-align: center; width: 100%; padding: 10px;'>
            <h3 style='text-align: center; margin: 0 auto; color: #007BFF;'>Surprise QUIZ!!!</h3>
        </div>
    """, unsafe_allow_html=True)

# Start quiz button with improved styling
if not st.session_state.quiz_started and not st.session_state.quiz_completed:
    st.markdown("""
        <div style='text-align: center; margin: 20px 0;'>
            <h3>Ready to begin?</h3>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()

if st.session_state.quiz_started and not st.session_state.quiz_completed:
    
    progress = st.progress((st.session_state.current_question) / len(quiz_data))
    st.markdown(f"""
        <div style='text-align: center; margin: 10px 0;'>
            <p>Question {st.session_state.current_question + 1} of {len(quiz_data)}</p>
        </div>
    """, unsafe_allow_html=True)
    
    current_q = quiz_data[st.session_state.current_question]
    
    
    st.markdown(f"""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0;'>
            <h2 style='margin-bottom: 15px;'>{current_q["question"]}</h2>
        </div>
    """, unsafe_allow_html=True)
    
    
    user_answer = st.radio("", current_q["options"], key=current_q["question"])
    
   
    if st.button("Submit Answer", key="submit"):
        if user_answer == current_q["correct"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! The correct answer is {current_q['correct']}")
        
        if st.session_state.current_question < len(quiz_data) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.quiz_completed = True
            st.session_state.quiz_started = False
            st.rerun()

#
if st.session_state.quiz_completed:
    percentage = (st.session_state.score / len(quiz_data)) * 100
    
    st.markdown(f"""
        <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin: 20px 0;'>
            <h2>Quiz Completed! 🎊</h2>
            <h3>Your Score: {st.session_state.score}/{len(quiz_data)}</h3>
            <h3>Percentage: {percentage:.1f}%</h3>
        </div>
    """, unsafe_allow_html=True)
    
    
    if percentage == 100:
        st.balloons()
        message = "🏆 Perfect Score! Excellent work!"
    elif percentage >= 70:
        message = "🌟 Great job! Well done!"
    elif percentage >= 50:
        message = "📚 Good effort! Keep practicing!"
    else:
        message = "💪 Keep learning! You can do better!"
    
    st.markdown(f"""
        <div style='text-align: center; margin: 20px 0;'>
            <h3>{message}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    
    if st.button("Restart Quiz", key="restart"):
        st.session_state.quiz_started = False
        st.session_state.quiz_completed = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()

    