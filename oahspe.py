import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader

def open_pdf():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        display_pdf_text(file_path)

def display_pdf_text(file_path):
    reader = PdfReader(file_path)
    text_widget.delete('1.0', tk.END)  # Clear previous text
    for page in reader.pages:
        text_widget.insert(tk.END, page.extract_text())  # Add each page's text

# Initialize Tkinter app
app = tk.Tk()
app.title("Oahspe Reader")

# Create text widget with scrollbar
text_frame = tk.Frame(app)
text_frame.pack(expand=True, fill='both')

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget = tk.Text(text_frame, wrap='word', font=('Arial', 12), yscrollcommand=scrollbar.set)
text_widget.pack(side=tk.LEFT, expand=True, fill='both')
scrollbar.config(command=text_widget.yview)

# Add button to open PDF
open_button = tk.Button(app, text="Open Oahspe PDF", command=open_pdf)
open_button.pack()

app.mainloop()