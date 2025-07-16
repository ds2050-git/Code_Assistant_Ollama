# Code Assistant — Local LLM + Gradio

## Overview
An AI coding assistant that runs entirely on your machine using Ollama for model inference and Gradio for a lightweight chat UI. Ideal for local development, code explanations, and lightweight AI assistance without relying on cloud APIs.

## Dependencies
- Python 3.10+
- Required packages (listed in `requirements.txt`):


> Additionally, [Ollama](https://ollama.com/) must be installed on your machine to serve the local LLM model.

---

## Installation

1. **Clone the repository**:
 ```bash
 git clone https://github.com/ds2050-git/Code_Assistant_Ollama.git
 cd Code_Assistant_Ollama
 ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and set up Ollama**:
   - Download Ollama from: https://ollama.ai/download

---

## Running the Project

- **Start the Code Assistant App**:
  ```bash
  python app.py
  ```

- **Open the Gradio interface**:
  After running, Gradio will automatically open in your browser at:
  ```
  http://localhost:7860
  ```

- **Start interacting**:
  Type a prompt like:
  ```
  Write a Python function to perform binary search on a sorted vector.
  ```
  and receive a contextual response from the local LLM model.

---


