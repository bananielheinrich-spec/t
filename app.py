import streamlit as st
from openai import OpenAI

# Setup für die UI
st.set_page_config(page_title="AI Thumbnail Maker", page_icon="🖼️")
st.title("🚀 AI Thumbnail Generator")
st.write("Gib deine Video-Idee ein und ich erstelle das Thumbnail.")

# API Key Eingabe (Solltest du später in den GitHub Secrets speichern!)
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

video_topic = st.text_area("Worum geht es in deinem Video?", "Das Rätsel um Flug MH370")

if st.button("Thumbnail generieren"):
    if not api_key:
        st.error("Bitte gib zuerst einen API-Key ein!")
    else:
        client = OpenAI(api_key=api_key)
        
        with st.spinner('KI denkt nach und malt...'):
            try:
                # Schritt 1: Prompt-Optimierung für das Bild
                # Wir sagen der KI, dass es ein auffälliges YouTube-Thumbnail sein soll
                image_prompt = f"Professional YouTube thumbnail for a video about: {video_topic}. High contrast, cinematic lighting, vivid colors, clickbait style, 4k resolution, no small text."

                # Schritt 2: Bild-Generierung mit DALL-E 3
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=image_prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )

                image_url = response.data[0].url
                
                # Schritt 3: Ergebnis anzeigen
                st.image(image_url, caption="Dein KI-generiertes Thumbnail")
                st.success("Fertig! Du kannst das Bild mit Rechtsklick speichern.")
                
            except Exception as e:
                st.error(f"Fehler: {e}")

---

### So bringst du es auf GitHub:

1.  **Repository erstellen:** Lade die `app.py` und die `requirements.txt` hoch.
2.  **Deployment:** * Gehe auf [streamlit.io/cloud](https://streamlit.io/cloud).
    * Verknüpfe dein GitHub-Konto.
    * Wähle dein Repository aus und klicke auf "Deploy".
3.  **API Key:** Du benötigst einen API-Key von **OpenAI** (oder einem anderen Anbieter wie Stable Diffusion), damit die KI tatsächlich Bilder malen kann.

**Ein kleiner Profi-Tipp:**
Die Profi-Tools wie auf deinem Screenshot fügen oft noch automatisch Textelemente über das Bild. Dafür müsstest du in Python die Library `Pillow` (PIL) nutzen, um Text-Layer über das generierte Bild zu legen.

Möchtest du, dass ich dir zeige, wie man zusätzlich automatisch Text (wie "MYSTERY" oder "BUSTED") auf das Bild schreibt?
