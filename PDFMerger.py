import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFMerger:
    def __init__(self, master):
        self.master = master
        master.title("PDF Merger")

        # Add widgets
        self.button_add = tk.Button(master, text="Add PDF", command=self.add_pdf)
        self.button_add.pack(padx=10, pady=5)

        self.button_up = tk.Button(master, text="Move Up", command=self.move_up)
        self.button_up.pack(padx=10, pady=5)

        self.button_down = tk.Button(master, text="Move Down", command=self.move_down)
        self.button_down.pack(padx=10, pady=5)

        self.button_remove = tk.Button(master, text="Remove PDF", command=self.remove_pdf)
        self.button_remove.pack(padx=10, pady=5)

        self.button_merge = tk.Button(master, text="Merge PDFs", command=self.merge_pdfs)
        self.button_merge.pack(padx=10, pady=5)

        self.listbox = tk.Listbox(master)
        self.listbox.pack(padx=10, pady=5)

    def add_pdf(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file_path in file_paths:
            if file_path:
                self.listbox.insert(tk.END, file_path)

    def remove_pdf(self):
        index = self.listbox.curselection()
        if index:
            self.listbox.delete(index)

    def merge_pdfs(self):
        if self.listbox.size() > 0:
            merger = PyPDF2.PdfMerger()
            for pdf in self.listbox.get(0, tk.END):
                merger.append(pdf)

            output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
            if output_file:
                merger.write(output_file)
                merger.close()
                messagebox.showinfo("Success", "PDFs merged successfully!")
        else:
            messagebox.showerror("Error", "Please select PDFs to merge.")

    def move_up(self):
        selected = self.listbox.curselection()
        if selected:
            if selected[0] > 0:
                self.listbox.insert(selected[0]-1, self.listbox.get(selected[0]))
                self.listbox.delete(selected[0]+1)
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(selected[0]-1)

    def move_down(self):
        selected = self.listbox.curselection()
        if selected:
            if selected[0] < self.listbox.size()-1:
                self.listbox.insert(selected[0]+2, self.listbox.get(selected[0]))
                self.listbox.delete(selected[0])
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(selected[0]+1)

root = tk.Tk()
pdf_merger = PDFMerger(root)
root.mainloop()
