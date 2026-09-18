# 🤖 AI Text Summarizer

An AI-powered text summarization web application built with **Python, FastAPI, Hugging Face Transformers, and T5**.

The application accepts long-form text through a web interface and generates a concise summary using a fine-tuned T5 Transformer model.

---

## 📌 Project Overview

Reading and understanding long pieces of text can be time-consuming.

This project demonstrates how a **Transformer-based NLP model** can be integrated into a real web application to automatically summarize text.

The project combines:

- Natural Language Processing (NLP)
- Deep Learning
- Transformer models
- Hugging Face Transformers
- PyTorch
- FastAPI
- HTML/CSS/JavaScript
- REST API development
- Git/GitHub

### Workflow

```text
User
 │
 ▼
Web Interface
 │
 │  Text
 ▼
FastAPI Backend
 │
 ▼
Text Cleaning
 │
 ▼
T5 Tokenizer
 │
 ▼
Fine-Tuned T5 Model
 │
 ▼
Summary Generation
 │
 ▼
FastAPI Response
 │
 ▼
Web Interface
 │
 ▼
Generated Summary
````

---

# ✨ Features

* 📝 Text input through a web interface
* 🤖 Transformer-based text summarization
* 🧠 Fine-tuned T5 model
* ⚡ FastAPI backend
* 🔌 REST API endpoint for summarization
* 🧹 Basic text preprocessing and cleaning
* 🔢 Tokenization using Hugging Face T5 tokenizer
* 🚀 GPU acceleration when available
* 🍎 Apple Silicon MPS support
* 🖥️ CPU fallback
* 📱 Responsive frontend
* ⏳ Loading/processing state during summary generation
* ❌ Basic input and API error handling
* 📦 Git/GitHub version control

---

# 🏗️ Architecture

The application follows a simple client-server architecture.

```text
                  USER
                    │
                    ▼
        ┌─────────────────────┐
        │    Web Frontend     │
        │   HTML / CSS / JS   │
        └──────────┬──────────┘
                   │
              HTTP POST
                   │
                   ▼
        ┌─────────────────────┐
        │      FastAPI        │
        │      Backend        │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Text Cleaning     │
        │      + Regex        │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   T5 Tokenizer      │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Fine-Tuned T5      │
        │  Transformer Model  │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Generated Summary  │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │    Web Frontend     │
        └─────────────────────┘
```

---

# 🛠️ Technology Stack

| Component               | Technology                |
| ----------------------- | ------------------------- |
| Programming Language    | Python                    |
| Deep Learning           | PyTorch                   |
| NLP / Transformers      | Hugging Face Transformers |
| Model                   | T5                        |
| Backend                 | FastAPI                   |
| Frontend                | HTML5                     |
| Styling                 | CSS3                      |
| Client-side Logic       | JavaScript                |
| API Format              | JSON                      |
| Development Environment | VS Code                   |
| Version Control         | Git                       |
| Repository              | GitHub                    |

---

# 🧠 Model Details

## T5 Transformer

The project uses **T5 (Text-to-Text Transfer Transformer)** for text summarization.

T5 approaches NLP tasks using a text-to-text framework:

```text
Input Text
    │
    ▼
T5 Tokenizer
    │
    ▼
Token IDs
    │
    ▼
T5 Transformer
    │
    ▼
Generated Token IDs
    │
    ▼
Decoded Text
    │
    ▼
Summary
```

The application loads the trained model from:

```text
saved_summary_model/
```

The directory contains the locally saved model and tokenizer required for inference.

> **Note:** `saved_summary_model/` is intentionally excluded from Git using `.gitignore` because model files can be large. The current GitHub repository contains the application source code, not the local model files.

---

## 📚 Training Data

The model was fine-tuned for dialogue/text summarization using the **SAMSum** dataset.

The training workflow included:

```text
SAMSum Dataset
      │
      ▼
Text Cleaning
      │
      ▼
Tokenization
      │
      ▼
T5 Fine-Tuning
      │
      ▼
Validation
      │
      ▼
Saved Model
      │
      ▼
FastAPI Application
```

The project training experiment used sampled training and validation data and fine-tuned a T5-small model.

---

# 🔄 Text Processing Pipeline

Before the text is passed to the model, basic preprocessing is applied.

The current preprocessing includes:

* Removing Windows line breaks
* Normalizing whitespace
* Removing HTML-like tags
* Removing leading/trailing whitespace
* Converting text to lowercase

Conceptually:

```text
Raw Text
   │
   ▼
Remove Line Breaks
   │
   ▼
Normalize Spaces
   │
   ▼
Remove HTML-like Tags
   │
   ▼
Strip Whitespace
   │
   ▼
Lowercase
   │
   ▼
Clean Text
```

---

# 📁 Project Structure

```text
ai-text-summarizer/
│
├── app.py
├── index.html
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
└── saved_summary_model/
    └── Local trained T5 model
```

### File Responsibilities

#### `app.py`

Main FastAPI application.

Responsible for:

* Loading the T5 model
* Loading the tokenizer
* Selecting the available compute device
* Cleaning input text
* Tokenizing input
* Generating summaries
* Providing API endpoints
* Serving the frontend

#### `index.html`

Frontend structure and user interface.

#### `static/style.css`

Application styling and responsive layout.

#### `static/script.js`

Frontend JavaScript responsible for:

* Form submission
* Sending requests to FastAPI
* Handling API responses
* Displaying summaries
* Handling loading/error states

#### `requirements.txt`

Python dependencies required to run the application.

#### `.gitignore`

Prevents local and sensitive files from being committed to Git.

---

# ⚙️ Setup

## 1. Clone the Repository

```bash
git clone https://github.com/azizch2618/ai-text-summarizer.git
```

Move into the project:

```bash
cd ai-text-summarizer
```

---

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Add the Trained Model

The application expects the trained T5 model to be available at:

```text
saved_summary_model/
```

Because the model directory is excluded from Git, cloning the repository alone does **not** include the trained model.

The directory should contain the model and tokenizer files required by:

```python
T5ForConditionalGeneration.from_pretrained(
    "./saved_summary_model"
)

T5Tokenizer.from_pretrained(
    "./saved_summary_model"
)
```

---

# ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Open the address in your browser.

---

# 🔌 API Usage

The application provides a POST endpoint for text summarization.

## Endpoint

```http
POST /summarize/
```

---

## Request

Send JSON containing the text to summarize:

```json
{
    "dialogue": "Artificial intelligence is changing many industries..."
}
```

---

## Response

The API returns:

```json
{
    "summary": "Artificial intelligence is changing many industries..."
}
```

---

# 🧪 Example API Request

Using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/summarize/" \
-H "Content-Type: application/json" \
-d '{"dialogue":"Artificial intelligence is being used across many industries to automate tasks, improve decision making, and enhance customer experiences."}'
```

---

# 🌐 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

This allows you to test the `/summarize/` endpoint directly from the browser.

---

# 💻 Frontend

The frontend provides a simple workflow:

```text
1. Open the application
        ↓
2. Enter text
        ↓
3. Click "Summarize Content"
        ↓
4. JavaScript sends POST request
        ↓
5. FastAPI processes the text
        ↓
6. T5 generates summary
        ↓
7. Summary returned as JSON
        ↓
8. Summary displayed in UI
```

---

# 📸 Screenshots

## Application Interface

Add a screenshot of the main application here.

```text
screenshots/homepage.png
```

Example Markdown:

```markdown
![AI Text Summarizer](screenshots/homepage.png)
```

---

## Generated Summary

Add a screenshot showing a generated summary.

```text
screenshots/summary-result.png
```

Example:

```markdown
![Generated Summary](screenshots/summary-result.png)
```

> Screenshots can be added to the repository later as the project documentation is expanded.

---

# 🚀 Current Project Status

### Completed

* [x] T5 Transformer model
* [x] Model loading
* [x] Tokenizer integration
* [x] Text preprocessing
* [x] Text summarization function
* [x] FastAPI backend
* [x] REST API endpoint
* [x] HTML frontend
* [x] CSS styling
* [x] JavaScript API integration
* [x] Loading state
* [x] Error handling
* [x] Apple Silicon MPS support
* [x] Git repository
* [x] GitHub repository

### Future Improvements

* [ ] Improve summary quality
* [ ] Experiment with decoding parameters
* [ ] Improve fine-tuning strategy
* [ ] Evaluate summaries using appropriate NLP metrics
* [ ] Test on a wider range of inputs
* [ ] Add better input validation
* [ ] Add summary length controls
* [ ] Add automated tests
* [ ] Add deployment configuration
* [ ] Improve documentation and project screenshots

---

# 🎯 Learning Objectives

This project was developed as a practical Deep Learning and NLP project to understand how a trained Transformer model can be integrated into a complete application.

Key learning areas include:

* NLP preprocessing
* Tokenization
* Transformer architecture
* T5 sequence-to-sequence models
* Model inference
* PyTorch
* Hugging Face Transformers
* FastAPI
* REST APIs
* Frontend/backend communication
* JSON data exchange
* Git and GitHub
* Basic ML application architecture

---

# 🔐 Git & Model Management

The repository intentionally excludes:

```text
.venv/
saved_summary_model/
__pycache__/
.env
.vscode/
```

This keeps the GitHub repository focused on source code and prevents local environments, model files, and environment configuration from being committed.

---

# 👨‍💻 Author

**Aziz Ullah**

Electrical Engineer transitioning into **AI/ML**, with a focus on:

* Machine Learning
* Deep Learning
* NLP
* Generative AI
* Python
* AI-powered applications

---

# 📄 License

No license has currently been added to this project.

````

### One important adjustment

I deliberately **did not put fake screenshots, fake evaluation scores, deployment claims, or performance claims** into the README. Your project is currently at the working local-application stage, so the README should accurately represent that.

I also kept the model section clear about `saved_summary_model/`: because we intentionally ignored that directory, someone cloning the GitHub repo will need access to the trained model before the application can run.

### Next Git step

Save this as:

```text
README.md
````

inside:

```text
TEXT_SUMMARIZER_AP/
```

Then we'll do:

```bash
git status
git add README.md
git commit -m "Add project documentation"
git push
```

That will give you a clean second commit rather than modifying your protected initial version.

