import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sample Gene database
gene_database = {
    'AGGAGCTGAGCCGAGCCCGGAGGCAGGAGCAGAGC': {'gene': 'BRCA1', 'mutation': '185delAG', 'disorder': 'Breast cancer'},
    'ATCTTTGGTGTTTCCCTTGCTATGATTTGTCCAGTTTCTCCTGGATGTGCTGTCCTGGCCTCAGTGATGATAGGCAAG': {'gene': 'CFTR', 'mutation': 'F508del', 'disorder': 'Cystic fibrosis'},
    'ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTTACTGAA': {'gene': 'HBB', 'mutation': 'HbS', 'disorder': 'Sickle cell disease'},
    'ATGCATGTCAGAGTGGAGTGAGGTCAGGAGGACAGGAGGA': {'gene': 'TP53', 'mutation': 'R248Q', 'disorder': 'Li-Fraumeni syndrome'},
    'GAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAG': {'gene': 'PHEX', 'mutation': 'D378Y', 'disorder': 'X-linked hypophosphatemia'},
}

def is_valid_dna(sequence):
    return sequence and all(base in 'ATCG' for base in sequence.upper())

def show_error(message):
    messagebox.showerror("Input Error", message)

def calculate_gc_content():
    sequence = entry_dna.get().upper()
    if not is_valid_dna(sequence):
        show_error("Invalid DNA sequence. Only 'A', 'T', 'C', 'G' are allowed.")
        return
    gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    result_gc_content.config(text=f"GC Content: {gc_content:.2f}%")

def transcribe_dna_to_rna():
    sequence = entry_dna.get().upper()
    if not is_valid_dna(sequence):
        show_error("Invalid DNA sequence. Only 'A', 'T', 'C', 'G' are allowed.")
        return
    rna_sequence = sequence.replace('T', 'U')
    result_transcription.config(text=f"RNA Sequence: {rna_sequence}")

def detect_genetic_disorders():
    sequence = entry_dna.get().upper()
    if not is_valid_dna(sequence):
        show_error("Invalid DNA sequence. Only 'A', 'T', 'C', 'G' are allowed.")
        return

    found = any(seq in sequence for seq in gene_database)
    if found:
        for seq, info in gene_database.items():
            if seq in sequence:
                result_disorders.config(text=f"Gene: {info['gene']}\nMutation: {info['mutation']}\nAssociated disorder: {info['disorder']}.")
                break
    else:
        result_disorders.config(text="No known gene or mutations detected.")

def clear_all():
    entry_dna.delete(0, tk.END)
    result_gc_content.config(text="GC Content: ")
    result_transcription.config(text="RNA Sequence: ")
    result_disorders.config(text="Genetic Disorders: ")

def create_gui():
    global entry_dna, result_gc_content, result_transcription, result_disorders

    # Create the main window
    root = tk.Tk()
    root.title("Gene Sequence Analyzer")
    root.state('zoomed')

    # Create and style widgets
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12), padding=6)
    style.configure('TLabel', font=('Arial', 12), padding=6)
    style.configure('TEntry', font=('Arial', 12), padding=6)
    style.configure('TFrame', background='lightgrey')

    frame = ttk.Frame(root, style='TFrame')
    frame.pack(expand=True, fill=tk.BOTH)

    frame_content = ttk.Frame(frame)
    frame_content.pack(expand=True)

    frame_content.grid_columnconfigure(0, weight=1)
    frame_content.grid_columnconfigure(1, weight=1)
    frame_content.grid_rowconfigure(0, weight=0)
    frame_content.grid_rowconfigure(1, weight=0)
    frame_content.grid_rowconfigure(2, weight=0)
    frame_content.grid_rowconfigure(3, weight=1)
    frame_content.grid_rowconfigure(4, weight=1)
    frame_content.grid_rowconfigure(5, weight=1)
    frame_content.grid_rowconfigure(6, weight=0)

    tk.Label(frame_content, text="Enter DNA Sequence:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
    entry_dna = ttk.Entry(frame_content, width=60)
    entry_dna.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    ttk.Button(frame_content, text="Calculate GC Content", command=calculate_gc_content).grid(row=1, column=0, padx=10, pady=10, sticky='ew')
    ttk.Button(frame_content, text="Transcribe DNA to RNA", command=transcribe_dna_to_rna).grid(row=1, column=1, padx=10, pady=10, sticky='ew')
    ttk.Button(frame_content, text="Detect Genetic Disorders", command=detect_genetic_disorders).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    ttk.Button(frame_content, text="Clear", command=clear_all).grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    result_gc_content = ttk.Label(frame_content, text="GC Content: ")
    result_gc_content.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='w')

    result_transcription = ttk.Label(frame_content, text="RNA Sequence: ")
    result_transcription.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='w')

    result_disorders = ttk.Label(frame_content, text="Genetic Disorders: ")
    result_disorders.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='w')

    # Run the application
    root.mainloop()

# Run the GUI
create_gui()
