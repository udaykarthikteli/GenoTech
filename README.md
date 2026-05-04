# GenoTech – DNA Sequence Analysis Web App

GenoTech is a Flask-based bioinformatics web application that performs real-time DNA sequence analysis with interactive visualization and AI-based classification.

Users can input DNA sequences and instantly get insights including GC content, base composition, mutation detection, codon analysis, and repeating patterns. It also includes machine learning-based classification and downloadable reports.

---

## Features

- DNA sequence analysis (A, T, G, C counts)
- Interactive charts (Bar & Pie using Chart.js)
- GC content and AT/GC ratio analysis
- AI-based classification (Random Forest model)
- Mutation detection (sequence comparison with reference)
- File upload support (.txt / .fasta)
- Downloadable analysis report
- Real-time Flask backend processing

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Backend | Flask (Python >= 3.12) |
| Machine Learning | scikit-learn, NumPy |

---

## Project Structure

```
GenoTech/
├── app.py              # Flask app and analysis logic
├── templates/
│   └── index.html      # Frontend UI
├── pyproject.toml      # Project metadata and dependencies (uv)
├── requirements.txt    # Pip-compatible dependency list
├── uv.lock             # Locked dependency versions
└── README.md
```

---

## Running the Project

### Option 1: Using uv (recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package and project manager.

**Install uv** (if not already installed):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Clone and run:**

```bash
git clone https://github.com/udaykarthikteli/GenoTech.git
cd GenoTech

# Create virtual environment and install dependencies
uv sync

# Run the app
uv run python app.py
```

The app will be available at `http://localhost:8080`.

### Option 2: Using pip

```bash
git clone https://github.com/udaykarthikteli/GenoTech.git
cd GenoTech

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

The app will be available at `http://localhost:8080`.

---

## Usage

1. Open `http://localhost:8080` in your browser.
2. Enter a DNA sequence (only A, T, G, C characters) in the input field.
3. Enter a reference sequence for mutation comparison.
4. Click **Analyze** to see results including:
   - Base counts and GC content
   - Start/stop codon positions
   - Repeating 3-mer patterns
   - Mutation positions relative to the reference
   - AI classification (GC-rich, AT-rich, or Balanced)

---

## Requirements

- Python >= 3.12
- Flask >= 3.1.3
- NumPy >= 2.4.4
- scikit-learn >= 1.8.0
