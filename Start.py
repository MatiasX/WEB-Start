import os
import tkinter as tk
from tkinter import filedialog, messagebox

class WebTemplateApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weboldal Sablon Létrehozása")

        # Színek definiálása
        bg_color = "#1f1f1f"
        fg_color = "#ffffff"
        button_bg_color = "#464545"
        button_fg_color = "#ffffff"
        button_active_bg_color = "#aaaaaa"

        self.root.configure(bg=bg_color)

        # Projekt név címke és beviteli mező
        label_name = tk.Label(self.root, text="Projekt név:", fg=fg_color, bg=bg_color)
        label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Elérési útvonal címke, beviteli mező és tallózás gomb
        label_path = tk.Label(self.root, text="Elérési útvonal:", fg=fg_color, bg=bg_color)
        label_path.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_path = tk.Entry(self.root)
        self.entry_path.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        browse_button = tk.Button(self.root, text="Tallózás", fg=button_fg_color, bg=button_bg_color, command=self.browse_path)
        browse_button.grid(row=1, column=2, padx=5, pady=5)

        # Létrehozás gomb
        create_button = tk.Button(self.root, text="Létrehozás", fg=button_fg_color, bg=button_bg_color, command=self.create_web_template)
        create_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Bezárás gomb
        exit_button = tk.Button(self.root, text="Bezárás", fg=button_fg_color, bg=button_bg_color, command=self.root.quit)
        exit_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_path(self):
        # Elérési útvonal kiválasztása böngészővel
        path = filedialog.askdirectory()
        self.entry_path.delete(0, tk.END)
        self.entry_path.insert(0, path)

    def create_web_template(self):
        # Projekt név és elérési útvonal megszerzése a felhasználótól
        project_name = self.entry_name.get()
        path = self.entry_path.get()

        if not project_name:
            messagebox.showwarning("Hiányzó adat", "Kérlek, add meg a projekt nevét!")
            return

        if not path:
            messagebox.showwarning("Hiányzó adat", "Kérlek, válaszd ki a projekt elérési útvonalát!")
            return

        # Könyvtár létrehozása
        project_path = os.path.join(path, project_name)
        os.makedirs(project_path, exist_ok=True)

        # Könyvtárak létrehozása
        dirs = ['css', 'js', 'images']
        for dir_name in dirs:
            dir_path = os.path.join(project_path, dir_name)
            os.makedirs(dir_path)

        # Fájlok létrehozása
        files = ['index.html', 'css/style.css', 'js/script.js']
        for file_name in files:
            file_path = os.path.join(project_path, file_name)
            open(file_path, 'w').close()

        messagebox.showinfo("Sikeres létrehozás", "A weboldal sablon fájl szerkezet sikeresen létrejött.")

    def run(self):
        # Főhurok futtatása
        self.root.mainloop()

# Alkalmazás példányosítása és futtatása
app = WebTemplateApp()
app.run()
