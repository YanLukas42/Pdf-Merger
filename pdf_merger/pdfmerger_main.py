import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("500x400")
        self.pdf_files = []

        # Layout
        self.label = tk.Label(root, text="PDF Merger", font=("Arial", 20))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar PDFs", command=self.add_files)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remover Selecionado", command=self.remove_file)
        self.remove_button.pack(pady=5)

        self.merge_button = tk.Button(root, text="Mesclar PDFs", command=self.merge_pdfs, bg="green", fg="white")
        self.merge_button.pack(pady=20)

    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Selecione arquivos PDF",
            filetypes=[("PDF Files", "*.pdf")]
        )
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file.split("/")[-1])  # Mostra apenas o nome do arquivo

    def remove_file(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.pdf_files.pop(index)
            self.listbox.delete(index)
        else:
            messagebox.showwarning("Atenção", "Selecione um arquivo para remover.")

    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            messagebox.showerror("Erro", "Selecione pelo menos 2 arquivos para mesclar.")
            return

        save_path = filedialog.asksaveasfilename(
            title="Salvar PDF mesclado como",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if save_path:
            try:
                merger = PdfMerger()
                for pdf in self.pdf_files:
                    merger.append(pdf)
                merger.write(save_path)
                merger.close()
                messagebox.showinfo("Sucesso", "PDFs mesclados com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao mesclar: {e}")

# Executa o app
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()

