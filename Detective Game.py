import streamlit as st
import random

# --------------------------
# PAGE CONFIG
# --------------------------

st.set_page_config(
    page_title="🕵️ Murder Mystery",
    page_icon="🔎",
    layout="wide"
)

# --------------------------
# GAME DATA
# --------------------------

victims = [
    "Professor Black",
    "Sarah Johnson",
    "David Miller",
    "Emily White"
]

suspects = [
    {
        "name": "Alice",
        "alibi": "I was reading in the library.",
        "contradiction": "The library was closed."
    },
    {
        "name": "Bob",
        "alibi": "I was cooking dinner.",
        "contradiction": "A restaurant receipt was found."
    },
    {
        "name": "Charlie",
        "alibi": "I was walking in the park.",
        "contradiction": "The park was closed due to rain."
    }
]

crime_scene_clues = [
    "🔍 A muddy footprint",
    "⌚ A broken watch",
    "🧣 A red scarf",
    "📱 A deleted text message",
    "🚪 Signs of forced entry"
]

# --------------------------
# SESSION STATE
# --------------------------

if "victim" not in st.session_state:
    st.session_state.victim = random.choice(victims)

if "murderer" not in st.session_state:
    st.session_state.murderer = random.choice(suspects)["name"]

if "collected_clues" not in st.session_state:
    st.session_state.collected_clues = []

if "score" not in st.session_state:
    st.session_state.score = 0

# --------------------------
# CUSTOM STYLE
# --------------------------

st.markdown("""
<style>

.main {
    background-color: #111111;
}

.card {
    background-color: #222222;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.title {
    text-align:center;
    color: gold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# TITLE
# --------------------------

st.markdown(
    "<h1 class='title'>🕵️ Murder Mystery Detective</h1>",
    unsafe_allow_html=True
)

st.write(f"### Victim: {st.session_state.victim}")

# --------------------------
# SIDEBAR
# --------------------------

st.sidebar.title("🔎 Detective Menu")

menu = st.sidebar.radio(
    "Choose Action",
    [
        "Suspects",
        "Crime Scene",
        "Clues",
        "Accuse",
        "Score"
    ]
)

# --------------------------
# SUSPECT CARDS
# --------------------------

if menu == "Suspects":

    st.header("👥 Suspects")

    cols = st.columns(3)

    for i, suspect in enumerate(suspects):

        with cols[i]:
            st.markdown(
                f"""
                <div class="card">
                <h3>{suspect['name']}</h3>
                <p><b>Alibi:</b></p>
                <p>{suspect['alibi']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# --------------------------
# CRIME SCENE
# --------------------------

elif menu == "Crime Scene":

    st.header("🔍 Investigate Crime Scene")

    if st.button("Find Clue"):

        remaining = [
            clue for clue in crime_scene_clues
            if clue not in st.session_state.collected_clues
        ]

        if remaining:

            clue = random.choice(remaining)

            st.session_state.collected_clues.append(clue)

            st.success(f"Clue Found: {clue}")

            st.session_state.score += 10

        else:
            st.warning("No more clues available.")

# --------------------------
# CLUE DISPLAY
# --------------------------

elif menu == "Clues":

    st.header("📋 Collected Clues")

    if st.session_state.collected_clues:

        for clue in st.session_state.collected_clues:
            st.info(clue)

    else:
        st.warning("No clues collected yet.")

# --------------------------
# ACCUSE
# --------------------------

elif menu == "Accuse":

    st.header("⚖️ Make an Accusation")

    suspect_names = [s["name"] for s in suspects]

    accusation = st.selectbox(
        "Who is the murderer?",
        suspect_names
    )

    if st.button("Accuse"):

        if accusation == st.session_state.murderer:

            st.success("🎉 Correct! You solved the case!")

            st.session_state.score += 50

        else:

            st.error(
                f"Wrong! The murderer was "
                f"{st.session_state.murderer}"
            )

# --------------------------
# SCORE
# --------------------------

elif menu == "Score":

    st.header("🏆 Detective Score")

    st.metric(
        label="Points",
        value=st.session_state.score
    )
