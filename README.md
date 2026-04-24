# GENOTECH – DNA Sequence Analysis Web App

GENOTECH is a Flask-based bioinformatics web application that performs real-time DNA sequence analysis with interactive visualization and AI-based classification.

It allows users to input or upload DNA sequences and instantly generates insights such as GC content, base composition, mutation detection, codon analysis, and repeating patterns. It also includes machine learning-based classification and downloadable reports.

---

## Features

-  DNA sequence analysis (A, T, G, C counts)
-  Interactive charts (Bar & Pie using Chart.js)
-  GC content & AT/GC ratio analysis
-  AI-based classification (Random Forest model)
-  Mutation detection (sequence comparison with reference)
-  File upload support (.txt / .fasta)
-  Downloadable analysis report
-  Modern animated UI
-  Real-time Flask backend processing

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript, Chart.js  
- Backend: Flask (Python)  
- Machine Learning: Scikit-learn, NumPy  


##  Project Structure

GENOTECH/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

---

## Run Locally

```bash
git clone https://github.com/your-username/genotech.git
cd genotech
pip install -r requirements.txt
python app.py
