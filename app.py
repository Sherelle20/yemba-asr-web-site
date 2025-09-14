import streamlit as st
import tempfile
import os
import pandas as pd

# ========================
# Démo de 2 modèles ASR
# ========================

def transcribe_model1(audio_path, lang="fr"):
    # ⚠️ Remplacer par ton vrai modèle Kaldi / ASR 1
    test = 'test 1'
    return f"[Modèle 1] Transcription de démo pour {test}"

def transcribe_model2(audio_path, lang="fr"):
    # ⚠️ Remplacer par ton vrai modèle Kaldi / ASR 2
    test = 'test 2'
    return f"[Modèle 2] Transcription de démo pour {test}"

# ========================
# Interface Streamlit
# ========================
st.title("🎙️ Démonstration Yemba ASR - Transcription Automatique")

st.write("Cette application permet de charger un fichier audio (WAV) et d’obtenir une transcription en langue Yemba avec deux modèles différents.")

# Choix du modèle
model_choice = st.radio(
    "Sélectionnez le modèle ASR à utiliser :",
    ("Modèle 1 - Kaldi baseline", "Modèle 2 - Modele GNN")
)

# Upload de fichier
uploaded_file = st.file_uploader("Choisissez un fichier audio", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    # Sauvegarde temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.audio(tmp_path, format="audio/wav")

    st.write("🔄 Transcription en cours...")

    # Sélection du modèle
    if "Modèle 1" in model_choice:
        transcript = transcribe_model1(tmp_path)
    else:
        transcript = transcribe_model2(tmp_path)

    # Affichage du résultat
    st.success("✅ Transcription terminée")
    st.text_area("Résultat :", transcript, height=200)

    # Nettoyage
    os.remove(tmp_path)

# ========================
# Section métriques
# ========================
st.header("📊 Comparaison des modèles")

# Exemple de métriques — à remplacer par tes vraies valeurs
metrics_data = {
    "Modèle": ["Kaldi baseline", "Modele GNN "],
    "WER (%) Erreur sur le mot": [6.61, 64.67],
}

metrics_df = pd.DataFrame(metrics_data)

st.table(metrics_df)
