import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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")

# Quiz questions
quiz = [
    {
        "question": "What is a budget?",
        "options": [
            "A plan for spending money",
            "A type of loan",
            "A credit score"
        ],
        "answer": "A plan for spending money"
    },
    {
        "question": "What is a credit score?",
        "options": [
            "Your financial reputation",
            "Your savings account balance",
            "A retirement fund"
        ],
        "answer": "Your financial reputation"
    },
    {
        "question": "Which is a good habit for saving money?",
        "options": [
            "Spend all you earn",
            "Pay yourself first",
            "Ignore your expenses"
        ],
        "answer": "Pay yourself first"
    },
    {
        "question": "What is interest?",
        "options": [
            "Money you earn or pay for borrowing",
            "A type of credit card",
            "Your monthly income"
        ],
        "answer": "Money you earn or pay for borrowing"
    },
    {
        "question": "Which is the safest place to keep savings?",
        "options": [
            "Under your mattress",
            "A reputable bank or credit union",
            "A risky stock"
        ],
        "answer": "A reputable bank or credit union"
    }
]

# Streamlit setup
st.set_page_config(page_title="💸 AI Financial Literacy Quiz", page_icon="💰")
st.title("💸 AI Financial Literacy Quiz Bot")
st.write("Test your money smarts and get instant AI feedback!")

score = 0

# Loop through quiz
for idx, q in enumerate(quiz):
    st.write("---")
    st.subheader(f"**Q{idx+1}: {q['question']}**")
    user_answer = st.radio("Choose your answer:", q["options"], key=f"q_{idx}")

    if st.button(f"Submit Answer {idx+1}", key=f"submit_{idx}"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Not quite. The correct answer is: {q['answer']}")

        # AI explanation with new API
        with st.spinner("🤖 AI is explaining..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful financial literacy tutor."},
                    {"role": "user", "content": f"Explain why '{q['answer']}' is the correct answer for: '{q['question']}'. The user chose: '{user_answer}'."}
                ]
            )
            explanation = response.choices[0].message.content.strip()
            st.info(explanation)

# Final score display
st.write("---")
st.subheader(f"🎉 Your Final Score: {score} out of {len(quiz)}")

if score == len(quiz):
    st.success("Amazing! You aced it! 💯")
elif score >= len(quiz) // 2:
    st.info("Good job! Keep learning to master your money skills! 📈")
else:
    st.warning("Keep practicing! Financial literacy is key. 🔑")

# Extra learning links
st.markdown("""
---
**💡 Learn More:**
- [Practical Money Skills](https://www.practicalmoneyskills.com)
- [MyMoney.gov](https://www.mymoney.gov)
- [Khan Academy Personal Finance](https://www.khanacademy.org/college-careers-more/personal-finance)
""")
