import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyjokes
import threading
import time
import random
import webbrowser

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'listening' not in st.session_state:
    st.session_state.listening = False
if 'engine' not in st.session_state:
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        st.session_state.engine = engine
    except:
        st.session_state.engine = None

# Streamlit page configuration
st.set_page_config(
    page_title="JARVIS Voice Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyjokes
import threading
import time
import random
import webbrowser

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'listening' not in st.session_state:
    st.session_state.listening = False
if 'engine' not in st.session_state:
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        st.session_state.engine = engine
    except:
        st.session_state.engine = None

# Streamlit page configuration
st.set_page_config(
    page_title="JARVIS Voice Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Iron Man style
st.markdown("""
<style>
body {
    background-image: url("https://images.hdqwalls.com/wallpapers/a-dark-knight-5c.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.main-header {
    text-align: center;
    color: #00ffe1;
    font-size: 3rem;
    margin-bottom: 2rem;
    text-shadow: 0 0 10px #00ffe1;
}

.chat-container {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    max-height: 400px;
    overflow-y: auto;
    color: white;
}

.user-message {
    background-color: #1f8ef1;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 15px;
    margin: 0.5rem 0;
    text-align: right;
    box-shadow: 0 0 5px #1f8ef1;
}

.jarvis-message {
    background-color: #00d68f;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 15px;
    margin: 0.5rem 0;
    text-align: left;
    box-shadow: 0 0 5px #00d68f;
}

.status-indicator {
    text-align: center;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 10px;
    font-weight: bold;
}

.listening {
    background-color: #ff4d4f;
    color: white;
    box-shadow: 0 0 10px #ff4d4f;
}

.ready {
    background-color: #52c41a;
    color: white;
    box-shadow: 0 0 10px #52c41a;
}

.sidebar .stButton>button {
    background-color: #111;
    color: #00ffe1;
    border: 1px solid #00ffe1;
}

</style>
""", unsafe_allow_html=True)

# (Remaining code stays unchanged...)

# The rest of your code remains untouched
# It includes speak(), add_to_history(), get_greeting(), listen_to_microphone(), process_command(), main()
# and the Streamlit layout, buttons, handlers, etc.

#Terminal command ---- streamlit run jarvis_app.py

# Speak function
def speak(text):
    """Convert text to speech"""
    try:
        if st.session_state.engine:
            st.session_state.engine.say(text)
            st.session_state.engine.runAndWait()
    except:
        pass  # Fallback if TTS fails

# Add message to conversation history
def add_to_history(sender, message):
    st.session_state.conversation_history.append({
        'sender': sender,
        'message': message,
        'timestamp': datetime.datetime.now().strftime('%H:%M:%S')
    })

# Greeting function
def get_greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Listen to microphone
def listen_to_microphone():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.session_state.listening = True
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)
            
        command = recognizer.recognize_google(audio)
        st.session_state.listening = False
        return command.lower()
    except sr.UnknownValueError:
        st.session_state.listening = False
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        st.session_state.listening = False
        return "Speech service unavailable."
    except sr.WaitTimeoutError:
        st.session_state.listening = False
        return "No speech detected."
    except Exception as e:
        st.session_state.listening = False
        return f"Error: {str(e)}"

# Process command
def process_command(command):
    response = ""
    
    if 'wikipedia' in command:
        topic = command.replace("wikipedia", "").strip()
        try:
            info = wikipedia.summary(topic, sentences=2)
            response = f"According to Wikipedia: {info}"
        except wikipedia.exceptions.DisambiguationError:
            response = "There are multiple results. Please be more specific."
        except:
            response = "Sorry, I couldn't find any results."
    
    elif 'play' in command:
        song = command.replace('play', '').strip()
        try:
            # This will open YouTube in a new tab
            pywhatkit.playonyt(song)
            response = f"Opening YouTube to play '{song}' in a new tab!"
        except Exception as e:
            response = f"Sorry, I couldn't play '{song}'. Error: {str(e)}"
    
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        response = f"The time is {current_time}"
    
    elif 'joke' in command:
        try:
            joke = pyjokes.get_joke()
            response = joke
        except:
            response = "Sorry, I couldn't fetch a joke right now."
    
    elif 'hello' in command or 'hi' in command:
        response = f"{get_greeting()} I am JARVIS. How can I help you today?"
    
    elif 'goodbye' in command or 'bye' in command:
        response = "Goodbye! Have a nice day."
    
    else:
        response = "I didn't understand that. You can ask me about Wikipedia, time, jokes, or just say hello!"
    
    return response

# Main Streamlit App
def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 JARVIS Voice Assistant</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🎛️ Controls")
        
        # Voice input button
        if st.button("🎤 Start Voice Input", type="primary"):
            with st.spinner("Listening..."):
                command = listen_to_microphone()
                if command and not command.startswith("Sorry") and not command.startswith("Error"):
                    add_to_history("You", command)
                    response = process_command(command)
                    add_to_history("JARVIS", response)
                    speak(response)
                else:
                    add_to_history("System", command)
        
        st.divider()
        
        # Quick actions
        st.subheader("⚡ Quick Actions")
        
        if st.button("📰 Wikipedia Search"):
            topic = st.text_input("Enter topic to search:", key="wiki_topic")
            if topic:
                command = f"wikipedia {topic}"
                add_to_history("You", f"Search Wikipedia for: {topic}")
                response = process_command(command)
                add_to_history("JARVIS", response)
                speak(response)
        
        if st.button("🕐 Current Time"):
            add_to_history("You", "What time is it?")
            response = process_command("time")
            add_to_history("JARVIS", response)
            speak(response)
        
        if st.button("😄 Tell a Joke"):
            add_to_history("You", "Tell me a joke")
            response = process_command("joke")
            add_to_history("JARVIS", response)
            speak(response)
        
        if st.button("🎵 Play Music"):
            song_name = st.text_input("Enter song name:", key="song_input")
            if song_name:
                command = f"play {song_name}"
                add_to_history("You", f"Play: {song_name}")
                response = process_command(command)
                add_to_history("JARVIS", response)
                speak(response)
        
        st.divider()
        
        # Clear conversation
        if st.button("🗑️ Clear Conversation"):
            st.session_state.conversation_history = []
            st.rerun()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Text input alternative
        st.subheader("💬 Text Input")
        text_command = st.text_input("Type your command here:", placeholder="Ask me about Wikipedia, time, jokes...")
        
        if st.button("Send", type="secondary") and text_command:
            add_to_history("You", text_command)
            response = process_command(text_command.lower())
            add_to_history("JARVIS", response)
            speak(response)
            st.rerun()
    
    with col2:
        # Status indicator
        if st.session_state.listening:
            st.markdown('<div class="status-indicator listening">🎤 Listening...</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-indicator ready">✅ Ready</div>', unsafe_allow_html=True)
    
    # Conversation history
    st.subheader("💭 Conversation History")
    
    if st.session_state.conversation_history:
        # Create chat container
        chat_container = st.container()
        
        with chat_container:
            for chat in reversed(st.session_state.conversation_history[-10:]):  # Show last 10 messages
                if chat['sender'] == 'You':
                    st.markdown(f"""
                    <div class="user-message">
                        <strong>You ({chat['timestamp']}):</strong> {chat['message']}
                    </div>
                    """, unsafe_allow_html=True)
                elif chat['sender'] == 'JARVIS':
                    st.markdown(f"""
                    <div class="jarvis-message">
                        <strong>JARVIS ({chat['timestamp']}):</strong> {chat['message']}
                    </div>
                    """, unsafe_allow_html=True)
                else:  # System messages
                    st.info(f"System: {chat['message']}")
    else:
        st.info("👋 Welcome! Start a conversation by using voice input or typing a command.")
        # Auto-greet on first load
        if len(st.session_state.conversation_history) == 0:
            greeting = f"{get_greeting()} I am JARVIS. How can I help you today?"
            add_to_history("JARVIS", greeting)
            speak(greeting)
            st.rerun()
    
    # Instructions
    with st.expander("ℹ️ How to use JARVIS"):
        st.markdown("""
        **Voice Commands:**
        - Click "🎤 Start Voice Input" and speak clearly
        - Say "Play [song name]" to play music on YouTube
        - Say "Wikipedia [topic]" to search Wikipedia
        - Say "What time is it?" or "time" for current time
        - Say "Tell me a joke" for a random joke
        - Say "Hello" or "Hi" for a greeting
        - Say "Goodbye" or "Bye" to end conversation
        
        **Music Features:**
        - 🎵 **Play Music:** Search and play any song on YouTube
        - 🔍 **Search Only:** Get YouTube search results without auto-playing
        - 🎲 **Surprise Me:** Play a random popular song
        - Voice command: "Play [artist name] [song name]"
        
        **Text Commands:**
        - Type any command in the text input box
        - Use the quick action buttons in the sidebar
        
        **Features:**
        - Real-time speech recognition
        - Text-to-speech responses
        - **YouTube Music Integration** 🎵
        - Wikipedia integration
        - Random jokes
        - Time queries
        """)

if __name__ == "__main__":
    main()

#Terminal commend ---- streamlit run jarvis_app.py

