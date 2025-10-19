import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Gaming Assistant: Sigma Version",
    page_icon="🎮",
    layout="wide"
)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY not found. Please set it in your .env file.")
        st.stop()
    try:
        return Groq(api_key=api_key)
    except Exception as e:
        st.error(f"Error initializing Groq client: {str(e)}")
        st.info("Please check your Groq library version and API key.")
        st.stop()

client = init_groq_client()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "personality" not in st.session_state:
    st.session_state.personality = "Friendly"

# Personality-based system messages
def get_system_message(personality):
    base_content = "You are a gaming AI assistant specializing in all aspects of gaming including game recommendations, strategies, tips, troubleshooting, and gaming discussions. You're knowledgeable about PC, console, mobile, and retro gaming."

    if personality == "Friendly":
        return base_content + " Be warm, friendly, and conversational like chatting with a gaming buddy. Use casual language and show enthusiasm for gaming."
    elif personality == "Professional":
        return base_content + " Maintain a professional, rigorous tone. Provide accurate, well-structured advice and detailed explanations. Be thorough and precise in your responses."
    elif personality == "Humorous":
        return base_content + " Be relaxed, humorous, and entertaining. Use gaming jokes, memes, and witty remarks while staying helpful. Make the conversation fun and engaging."

    return base_content

# Initialize messages with system message if empty
if not st.session_state.messages:
    st.session_state.messages = [
        {
            "role": "system",
            "content": get_system_message(st.session_state.personality)
        }
    ]

# App title and description
st.title("🎮 Gaming Assistant: Sigma Version")
st.markdown("### 🎯 Welcome to Your Personal Gaming AI!")
st.markdown("""🌟 **What I can do for you:**
- 🎲 **Game Recommendations**: Find your next favorite game based on your preferences
- 🏆 **Pro Strategies**: Get expert tips and tactics for competitive gaming
- 🔧 **Tech Support**: Troubleshoot gaming issues and optimize performance
- 📱 **Multi-Platform**: PC, console, mobile, and retro gaming expertise
- 🎨 **Game Development**: Insights into game design and development

💬 **Ready to level up your gaming experience? Let's chat!**
""")

# Sidebar with personality selection and settings
with st.sidebar:
    st.header("🤖 AI Personality")

    new_personality = st.selectbox(
        "Choose your AI's personality:",
        ["Friendly", "Professional", "Humorous"],
        index=["Friendly", "Professional", "Humorous"].index(st.session_state.personality),
        help="Select how you want your AI assistant to interact with you"
    )

    # Personality descriptions with emojis
    personality_info = {
        "Friendly": "😊 Warm and friendly - Chat like gaming buddies!",
        "Professional": "🎯 Rigorous and professional - Get accurate expert advice",
        "Humorous": "😄 Relaxed and humorous - Fun and entertaining conversations"
    }

    st.info(personality_info[new_personality])

    # Update personality if changed
    if new_personality != st.session_state.personality:
        st.session_state.personality = new_personality
        # Update system message
        if st.session_state.messages:
            st.session_state.messages[0] = {
                "role": "system",
                "content": get_system_message(new_personality)
            }
        st.rerun()

    st.header("📊 Quick Stats")
    st.markdown("""
    🎮 **Gaming Platforms Covered:**
    - 💻 PC Gaming (Steam, Epic, etc.)
    - 🎮 Console (PS5, Xbox, Switch)
    - 📱 Mobile Gaming (iOS/Android)
    - 🕹️ Retro Gaming (Classic consoles)
    """)

    st.header("⚙️ Settings")
    if st.button("🗑️ Clear Chat History"):
        # Keep system message with current personality
        st.session_state.messages = [{
            "role": "system",
            "content": get_system_message(st.session_state.personality)
        }]
        st.rerun()

# Display chat messages (excluding system message)
for message in st.session_state.messages[1:]:  # Skip system message
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input with personality-based placeholder
placeholders = {
    "Friendly": "Hey! What gaming topic should we chat about? 🎮",
    "Professional": "Please enter your gaming-related question or request for assistance...",
    "Humorous": "Drop your gaming question and let's have some fun! 😄🎮"
}

if prompt := st.chat_input(placeholders.get(st.session_state.personality, "Ask me anything about gaming...")):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Adjust temperature based on personality
                temp_settings = {
                    "Friendly": 0.8,
                    "Professional": 0.3,
                    "Humorous": 0.9
                }

                # Call Groq API
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages,
                    temperature=temp_settings.get(st.session_state.personality, 0.7),
                    max_tokens=1000,
                    stream=False
                )

                # Get response content
                assistant_response = response.choices[0].message.content

                # Display response
                st.markdown(assistant_response)

                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_response
                })

            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Please check your GROQ_API_KEY and internet connection.")

# Footer with personality-based tips
st.markdown("---")
tips = {
    "Friendly": "💡 **Tip:** Feel free to ask about your favorite games, or just chat about what you're playing! I'm here to help! 😊",
    "Professional": "💡 **Professional Tip:** For optimal assistance, provide specific details about your gaming setup, preferences, or technical issues.",
    "Humorous": "💡 **Pro Gamer Tip:** Ask me anything! Whether you're stuck on a boss fight or need a game to cure your boredom! 🎯😄"
}
st.markdown(tips.get(st.session_state.personality, "💡 **Tip:** Try asking about your favorite games, need recommendations, or want gaming tips!"))