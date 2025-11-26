import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.sticky_header import sticky_header

# ----- PAGE SETTINGS -----
st.set_page_config(
    page_title="Health AI Assistant",
    page_icon="🏥",
    layout="centered"
)

# ----- MAIN HEADER -----
colored_header(
    label="🏥 Health AI Assistant",
    description="Your personal health companion for reminders, hydration, sleep and daily recommendations.",
    color_name="blue-70",
)

st.markdown("""
<style>
    .stButton button {
        background-color: #0066ff;
        color: white;
        padding: 12px 16px;
        border-radius: 10px;
        font-size: 18px;
        width: 100%;
    }
    .block {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("### ✨ Enter Your Details")
    st.markdown('<div class="block">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input("Height (cm)", min_value=50, max_value=250)
        age = st.number_input("Age", min_value=1, max_value=120)
    with col2:
        weight = st.number_input("Weight (kg)", min_value=10, max_value=300)
        sleep = st.number_input("Sleep Yesterday (hrs)", min_value=0.0, step=0.5)

    water = st.number_input("Water Intake Today (liters)", step=0.1)
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("✨ Generate My Health Insights"):
    st.markdown("## 📊 Your Personalized Health Report")
    st.markdown('<div class="block">', unsafe_allow_html=True)

    # ---- BMI Calculation ----
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    st.write(f"### 🔢 Your BMI: **{bmi}**")

    if bmi < 18.5:
        st.warning("⚠ You are **underweight**. Add protein, nuts, and healthy carbs.")
    elif 18.5 <= bmi <= 24.9:
        st.success("✔ You have a **healthy weight**. Maintain your daily routine!")
    else:
        st.error("⚠ You are **overweight**. Avoid sugar and increase your activity.")

    # ---- Water Intake ----
    if water < 2:
        st.info("💧 You need to drink **more water!** Minimum: 2–3 liters/day.")
    else:
        st.success("💧 Great! You are well hydrated.")

    # ---- Sleep ----
    if sleep < 7:
        st.info("😴 Try to sleep **at least 7–8 hours** daily.")
    else:
        st.success("🌙 Great! Your sleep duration is healthy.")

    # ---- Extra Tip ----
    st.markdown("### ⭐ Daily Health Tip")
    st.write("Take a 10-minute walk every 2 hours to stay active and reduce stress.")

    st.markdown("</div>", unsafe_allow_html=True)