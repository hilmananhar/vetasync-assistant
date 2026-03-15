# VetaSync Assistant — Scientific Animal Education AI

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.42+-red.svg)

**VetaSync Assistant** is an advanced AI-powered educational tool dedicated to providing accurate, scientific, and evidence-based information on animal health. Powered by Google's Gemini 2.5 Flash model, it serves as a reliable knowledge hub for both pet owners and veterinary professionals, ensuring that every advice provided is backed by reputable veterinary journals and global consensus.

## 🚀 Features

- **Evidence-Based Education**: All medical, nutritional, and behavioral advice is supported by citations from reputable veterinary journals (e.g., JAVMA, WSAVA, ISFM).
- **Universal Support**: Expert-level guidance tailored for both pet owners and clinic staff, maintaining a high standard of information for all users.
- **Topical Deep Dives**: Quick access to critical topics such as Clinical Nutrition, Vaccination Protocols, Dental Health, and Senior Pet Care.
- **Scientific Emergency Detection**: Identifies critical symptoms and provides immediate emergency protocols based on clinical urgency.
- **Premium Glassmorphism UI**: A modern, high-contrast dark interface designed for clarity and a premium educational experience.

## 🛠️ Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **AI Model**: [Google Gemini 2.5 Flash](https://ai.google.dev/)
- **SDK**: `google-genai`
- **Language**: Python 3.9+

## ⚙️ Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/hilmananhar/vetasync-assistant.git
    cd vetasync-assistant
    ```

2.  **Install Dependencies**

    ```bash
    pip install streamlit google-genai
    ```

3.  **API Configuration**

    Open `app.py` and ensure the `API_KEY` placeholder is configured with your key from [Google AI Studio](https://aistudio.google.com/).

4.  **Run the Application**

    ```bash
    python -m streamlit run app.py
    ```

## 📖 Usage

- **Scientific Inquiry**: Ask any animal health question to receive detailed, journal-backed explanations.
- **Quick Topics**: Use the sidebar to explore common veterinary topics curated for an intuitive learning flow.
- **Emergency Protocol**: If a life-threatening symptom is detected, follow the highlighted emergency instruction immediately.

## 📁 Directory Structure

```
vetasync-assistant/
├── app.py              # Application core & Scientific AI Logic
├── LICENSE             # MIT License terms
├── README.md           # Documentation
└── .gitignore          # Environment & Cache excludes
```

## 📄 License

This project is licensed under the MIT License.

---

_© 2026 VetaSync Assistant. All Rights Reserved._
