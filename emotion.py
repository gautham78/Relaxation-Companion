import streamlit as st
from youtubesearchpython import VideosSearch
import time

relaxation_tips = {
    "sadness": {
        "message": " Hey, If you're feeling down...or lonely. Let's take a moment to slow down and breathe.",
        "suggestions": [
            "Write down 3 small things you're grateful for today.Forget the negative thoughts",
            "Try a 5-minute deep breathing exercise.",
            "Go outside and get some sunlight."
        ]
    },
    "anger": {
        "message": " It’s okay to feel angry. Its a part of being a human. Don't worry. Let's cool off together.",
        "suggestions": [
            "You can try to forget about it. Just let it be.Understood?",
            "Do some light stretching or a short walk.",
            "Write out what's making you angry and then tear it up."
        ]
    },
    "fear": {
        "message": "You're safe right now. Let's calm your body and mind.",
        "suggestions": [
            "Look around: name 3 things you see, 2 you can touch, 1 you can hear.",
            "Try grounding yourself by focusing on your breath.",
            "Watch a short calming video or listen to soft music."
        ]
    },
    "joy": {
        "message": "Damn,That's wonderful! Let's celebrate your good mood!",
        "suggestions": [
            "Dance to your favorite song!",
            "Share your joy with someone.",
            "You should treat yourself with something you like."
        ]
    },
    "neutral": {
        "message": " Let’s take a mindful moment for yourself.",
        "suggestions": [
            "You wanna maybe try stretching your neck and shoulders.",
            "Take a few slow breaths.",
            "Plan one simple, positive goal for today."
        ]
    }
}

st.set_page_config(page_title="AI Relaxation Companion", page_icon="🎵", layout="centered")

st.title("🌸 AI Relaxation Companion")
st.write("Let’s find something that helps you feel calm and cared for 💚")

emotion = st.selectbox("How are you feeling right now?", list(relaxation_tips.keys()))

song_name = st.text_input(
    "🎧 What song would you like to listen to?",
    placeholder="e.g., Perfect by Ed Sheeran"
)

def get_youtube_url(query):
    try:
        videos_search = VideosSearch(query, limit=1)
        results = videos_search.result()
        if results and "result" in results and len(results["result"]) > 0:
            link = results["result"][0]["link"]
            # convert standard YouTube link into embed link
            if "watch?v=" in link:
                link = link.replace("watch?v=", "embed/")
            return link
        return None
    except Exception as e:
        st.error(f"Error while searching: {e}")
        return None

if st.button("✨ Show Me Something Relaxing"):
    tip = relaxation_tips.get(emotion)

    st.subheader(tip["message"])
    st.write("### 🌿 Here are some ideas you can try:")
    for s in tip["suggestions"]:
        st.write(f"- {s}")

    if song_name:
        with st.spinner(f"Searching YouTube for '{song_name}'..."):
            video_url = get_youtube_url(song_name)
            time.sleep(1)
        if video_url:
            st.success("Found your song! 🎵")
            st.video(video_url)
        else:
            st.warning("Sorry, couldn't find that song. Try another title?")
    else:
        st.info("You didn’t enter a song. Maybe try adding one!")

    st.write("###  Let's take a short breathing exercise:")
    with st.empty():
        for msg, secs in [("Inhale (4s)...", 4), ("Hold (7s)...", 7), ("Exhale (8s)...", 8)]:
            st.write(msg)
            time.sleep(secs)
        st.write(" Great job! Feeling a little calmer?")

st.markdown("---")

