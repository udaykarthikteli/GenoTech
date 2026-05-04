from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

# ---------------- DNA UTILS ----------------

def is_valid_dna(sequence):
    return all(char in "ATGC" for char in sequence)

def calculate_gc(sequence):
    if len(sequence) == 0:
        return 0
    g = sequence.count('G')
    c = sequence.count('C')
    return round(((g + c) / len(sequence)) * 100, 2)

def base_count(sequence):
    return [
        sequence.count('A'),
        sequence.count('T'),
        sequence.count('G'),
        sequence.count('C')
    ]

def find_codons(sequence):
    start, stop = [], []
    for i in range(len(sequence) - 2):
        codon = sequence[i:i+3]
        if codon == "ATG":
            start.append(i)
        if codon in ["TAA", "TAG", "TGA"]:
            stop.append(i)
    return start, stop

def find_repeats(sequence):
    repeats = {}
    for i in range(len(sequence) - 2):
        pattern = sequence[i:i+3]
        repeats[pattern] = repeats.get(pattern, 0) + 1
    return {k: v for k, v in repeats.items() if v > 1}

def detect_mutations(seq1, seq2):
    mutations = []
    min_len = min(len(seq1), len(seq2))
    for i in range(min_len):
        if seq1[i] != seq2[i]:
            mutations.append((i, seq2[i], seq1[i]))
    return mutations

# ---------------- AI MODEL ----------------

def train_model():
    # Simple synthetic dataset
    X = [
        [10, 40, 40, 10],  # GC-rich
        [40, 40, 10, 10],  # AT-rich
        [25, 25, 25, 25],  # balanced
        [5, 5, 45, 45],
        [45, 45, 5, 5],
        [20, 30, 30, 20]
    ]
    y = ["GC-rich", "AT-rich", "Balanced", "GC-rich", "AT-rich", "Balanced"]

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# ---------------- ROUTE ----------------

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        seq = request.form.get('sequence', '').upper().strip()
        ref = request.form.get('reference', '').upper().strip()

        if not seq or not ref:
            error = "Enter both sequences"
        elif not is_valid_dna(seq) or not is_valid_dna(ref):
            error = "Only A, T, G, C allowed"
        else:
            gc = calculate_gc(seq)
            counts = base_count(seq)
            start, stop = find_codons(seq)
            repeats = find_repeats(seq)
            mutations = detect_mutations(seq, ref)

            # AI Prediction
            prediction = model.predict([counts])[0]

            result = {
                'gc': gc,
                'counts': counts,
                'length': len(seq),
                'start_codons': start,
                'stop_codons': stop,
                'repeats': repeats,
                'mutations': mutations,
                'prediction': prediction
            }

    return render_template('index.html', result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

