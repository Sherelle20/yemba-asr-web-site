import streamlit as st
import tempfile
import os

# Ici tu importes ton modèle ASR
# Exemple : from my_asr_module import transcribe_audio
# Pour démo sans modèle, on simule une transcription
def transcribe_audio(audio_path, lang="fr"):
    # À remplacer par ton vrai code de prédiction
    return f"Transcription de démo pour le fichier : {os.path.basename(audio_path)}"

# Titre
st.title("🎙️ Démonstration Yemba ASR - Transcription Automatique")

st.write("Cette application permet de charger un fichier audio (WAV, MP3, etc.) et d’obtenir une transcription en langue Yemba.")

# Upload de fichier
uploaded_file = st.file_uploader("Choisissez un fichier audio", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    # Sauvegarde temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.audio(tmp_path, format="audio/wav")

    st.write("🔄 Transcription en cours...")

    # Appel au modèle
    transcript = transcribe_audio(tmp_path)

    # Affichage du résultat
    st.success("✅ Transcription terminée")
    st.text_area("Résultat :", transcript, height=200)

    # Suppression du fichier temporaire
    os.remove(tmp_path)
