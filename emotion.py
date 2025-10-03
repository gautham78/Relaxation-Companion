import streamlit as st
from youtubesearchpython import VideosSearch

relaxation_tips = {
    "sadness": {
        "message": "Hey, If you're feeling down...or lonely. Let's take a moment to slow down and breathe.",
        "suggestions": [
            "Write down 3 small things you're grateful for today.",
            "Try a 5-minute deep breathing exercise.",
            "Go outside and get some sunlight."
        ]
    },
    "anger": {
        "message": "It’s okay to feel angry. It's part of being human. Let's cool off together.",
        "suggestions": [
            "Try to let it go — not everything needs your energy.",
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
        "message": "That's wonderful! Let's celebrate your good mood!",
        "suggestions": [
            "Dance to your favorite song!",
            "Share your joy with someone.",
            "Treat yourself with something you like."
        ]
    },
    "neutral": {
        "message": "Let’s take a mindful moment for yourself.",
        "suggestions": [
            "Stretch your neck and shoulders.",
            "Take a few slow breaths.",
            "Plan one simple, positive goal for today."
        ]
    }
}

st.set_page_config(page_title="AI Relaxation Companion", page_icon="🎵", layout="centered")

st.title("🌸 AI Relaxation Companion")
st.write("Tell me how you feel and what song you’d like, and I’ll make this moment calmer for you 💚")

emotion = st.selectbox("How are you feeling right now?", list(relaxation_tips.keys()))

song_name = st.text_input(
    "🎧 Type a song you want to listen to:",
    placeholder="e.g., Perfect by Ed Sheeran"
)

def get_youtube_embed(query):
    try:
        videos_search = VideosSearch(query, limit=1)
        results = videos_search.result()
        if results and "result" in results and len(results["result"]) > 0:
            link = results["result"][0]["link"]
            if "watch?v=" in link:
                link = link.replace("watch?v=", "embed/")
            return link
        return None
    except Exception as e:
        st.error(f"Error while searching: {e}")
        return None

if song_name:
    st.subheader(relaxation_tips[emotion]["message"])
    st.write("### 🌿 Here are some ideas you can try:")
    for s in relaxation_tips[emotion]["suggestions"]:
        st.write(f"- {s}")

    video_url = get_youtube_embed(song_name)
    if video_url:
        st.write("### 🎵 Here’s your song:")
        st.markdown(
            f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            unsafe_allow_html=True
        )
    else:
        st.warning("Sorry, I couldn't find that song. Try another title!")

st.markdown("---")
st.caption("Built with Streamlit 💚")
