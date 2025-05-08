from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfMerger

root = Tk()
root.title("PDF Merger")

def merge_pdfs():
    pdfs = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if pdfs:
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
        merger.write(output_path)
        merger.close()
        status_label.config(text="PDFs merged successfully!", fg="green")
    else:
        status_label.config(text="Please select PDFs to merge.", fg="red")

select_button = Button(root, text="Select PDFs", command=merge_pdfs)
select_button.pack(pady=10)

status_label = Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
