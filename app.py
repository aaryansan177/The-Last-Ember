import streamlit as st
import base64
import time
import re
import os

from scenes import SCENES
from state import GameState



def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def render_home_screen():
    set_background("assets/backgrounds/home.jpg")


    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("▶ Start New Game"):
        st.session_state.mode = "game"
        st.session_state.scene = "intro_winterfell"
        st.rerun()

    if st.button("📜 Continue"):
        st.session_state.mode = "game"
        st.rerun()



# ----------------------------------------
# Initial mode (home / game)
# ----------------------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "home"


st.set_page_config(
    page_title="Game of Thrones: The Last Ember",
    layout="wide"
)

# ----------------------------------------
# Utilities
# ----------------------------------------

def set_background(image_path):
    if not os.path.exists(image_path):
        return
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def typewriter(html_text, speed):
    placeholder = st.empty()
    tokens = re.split(r"(<[^>]+>)", html_text)
    rendered = ""
    for token in tokens:
        if token.startswith("<"):
            rendered += token
            placeholder.markdown(rendered, unsafe_allow_html=True)
        else:
            for char in token:
                rendered += char
                placeholder.markdown(rendered, unsafe_allow_html=True)
                time.sleep(speed)


def apply_effects(state, effects):
    for key, value in effects.items():
        current = getattr(state, key, 0 if isinstance(value, int) else False)
        setattr(state, key, current + value if isinstance(value, int) else value)

# ----------------------------------------
# Session init
# ----------------------------------------

if "state" not in st.session_state:
    st.session_state.state = GameState()

if "current_chapter" not in st.session_state:
    st.session_state.current_chapter = None

state = st.session_state.state
# ----------------------------------------
# HOME SCREEN
# ----------------------------------------
if st.session_state.mode == "home":
    render_home_screen()
    st.stop()

scene = SCENES[state.scene]

# ----------------------------------------
# Sidebar
# ----------------------------------------

with st.sidebar:
    st.title("🔥 The Last Ember")

    state.typing_enabled = st.checkbox("Typing effect", value=True)
    typing_speed = st.slider("Typing speed", 0.01, 0.05, 0.02)
    if st.sidebar.button("🏠 Return to Home"):
        st.session_state.mode = "home"
        st.rerun()


    if st.button("🔄 Restart"):
        st.session_state.clear()
        st.rerun()

# ----------------------------------------
# Background
# ----------------------------------------

set_background(scene["bg"])

# ----------------------------------------
# Content
# ----------------------------------------

st.markdown(f"<h1>{scene['title']}</h1>", unsafe_allow_html=True)

if state.typing_enabled:
    typewriter(scene["text"], typing_speed)
else:
    st.markdown(scene["text"], unsafe_allow_html=True)

# ----------------------------------------
# Choices
# ----------------------------------------

for label, next_scene, effects in scene["choices"]:
    if st.button(label):
        apply_effects(state, effects)
        state.scene = next_scene
        st.rerun()
def render_home_screen():
    st.markdown(
        """
        <style>
        .home-title {
            font-size: 56px;
            font-weight: 800;
            color: #e6c15a;
            margin-bottom: 0.5em;
        }
        .home-subtitle {
            font-size: 20px;
            color: #dddddd;
            max-width: 700px;
        }
        .home-box {
            padding: 60px;
            background: rgba(0,0,0,0.55);
            border-radius: 16px;
            max-width: 900px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="home-box">
            <div class="home-title">Game of Thrones<br>The Last Ember</div>
            <div class="home-subtitle">
                A choice-driven narrative set after the wars of Westeros.<br><br>
                Every decision shapes alliances, trust, and the fate of the realm.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🗡 Start New Game", use_container_width=True):
            from state import GameState
            st.session_state.state = GameState()
            st.session_state.mode = "game"
            st.rerun()

    with col2:
        st.button("📜 Load Game (Coming Soon)", disabled=True, use_container_width=True)
