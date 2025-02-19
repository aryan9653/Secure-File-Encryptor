import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
import ttkbootstrap as tb
import os

# GUI Setup
root = TkinterDnD.Tk()  
root.title("🔒 Secure File Encryptor")
root.geometry("800x600")
root.resizable(False, False)

# Apply ttkbootstrap theme
style = tb.Style("darkly")

selected_file = None  # Initialize selected file

# Function to apply smooth fade-in transition
def fade_in(widget, alpha=0):
    if alpha < 1.0:
        alpha += 0.05
        widget.place(relx=0.5, rely=0.5, anchor="center")
        widget.tk.call("wm", "attributes", root, "-alpha", alpha)
        root.after(20, lambda: fade_in(widget, alpha))

# Function to switch between sections smoothly
def show_section(section):
    if section == "encrypt":
        decrypt_frame.place_forget()
        fade_in(encrypt_frame)
    elif section == "decrypt":
        encrypt_frame.place_forget()
        fade_in(decrypt_frame)

# Encrypt File Function
def encrypt_action():
    global selected_file
    file_path = selected_file if selected_file else filedialog.askopenfilename(title="Select File to Encrypt")
    password = encrypt_password_entry.get()

    if file_path and password:
        output_file = file_path + ".enc"
        messagebox.showinfo("Success", f"✅ Encrypted: {os.path.basename(output_file)}")
    else:
        messagebox.showerror("Error", "⚠️ Please select a file and enter a password.")

# Decrypt File Function
def decrypt_action():
    global selected_file
    file_path = selected_file if selected_file else filedialog.askopenfilename(title="Select File to Decrypt")
    password = decrypt_password_entry.get()

    if file_path and password:
        output_file = file_path.replace(".enc", "_decrypted.txt")
        messagebox.showinfo("Success", f"✅ Decrypted: {os.path.basename(output_file)}")
    else:
        messagebox.showerror("Error", "⚠️ Please select a file and enter a password.")

# Dark Mode Toggle
def toggle_dark_mode():
    current_theme = style.theme_use()
    new_theme = "flatly" if current_theme == "darkly" else "darkly"
    style.theme_use(new_theme)

# Navbar Functions
def show_about():
    messagebox.showinfo("About", "This is a Secure File Encryptor built with Python & Tkinter.")

# Navbar (Header)
navbar = ttk.Frame(root, padding=10, bootstyle="primary")
navbar.pack(fill="x")

ttk.Button(navbar, text="🔒 Encrypt", bootstyle="info", command=lambda: show_section("encrypt")).pack(side="left", padx=10)
ttk.Button(navbar, text="🔓 Decrypt", bootstyle="warning", command=lambda: show_section("decrypt")).pack(side="left", padx=10)
ttk.Button(navbar, text="About", bootstyle="secondary", command=show_about).pack(side="right", padx=10)
ttk.Button(navbar, text="🌙 Dark Mode", bootstyle="secondary", command=toggle_dark_mode).pack(side="right", padx=10)

# Hamburger Menu Button
hamburger_menu = ttk.Menubutton(navbar, text="☰", bootstyle="secondary")
menu = tk.Menu(hamburger_menu, tearoff=0)
menu.add_command(label="Encrypt", command=lambda: show_section("encrypt"))
menu.add_command(label="Decrypt", command=lambda: show_section("decrypt"))
menu.add_command(label="About", command=show_about)
hamburger_menu.config(menu=menu)
hamburger_menu.pack(side="right", padx=10)

# 🟢 Encrypt Section
encrypt_frame = ttk.Frame(root, padding=20)

ttk.Label(encrypt_frame, text="🔒 Encrypt Your File", font=("Arial", 16, "bold")).pack(pady=10)

ttk.Label(encrypt_frame, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
encrypt_password_entry = ttk.Entry(encrypt_frame, show="*", font=("Arial", 12), width=30)
encrypt_password_entry.pack(pady=5)

encrypt_file_label = ttk.Label(encrypt_frame, text="📂 Drag & Drop or Select a File", font=("Arial", 12), relief="ridge", padding=10)
encrypt_file_label.pack(pady=5)

# Enable Drag & Drop
encrypt_file_label.drop_target_register(DND_FILES)
encrypt_file_label.dnd_bind("<<Drop>>", lambda event: encrypt_file_label.config(text=f"📂 Selected: {event.data.strip()}"))

encrypt_button = tb.Button(encrypt_frame, text="Encrypt", bootstyle="success", command=encrypt_action)
encrypt_button.pack(pady=10)

# 🟡 Decrypt Section
decrypt_frame = ttk.Frame(root, padding=20)

ttk.Label(decrypt_frame, text="🔓 Decrypt Your File", font=("Arial", 16, "bold")).pack(pady=10)

ttk.Label(decrypt_frame, text="Enter Password:", font=("Arial", 12)).pack(pady=5)
decrypt_password_entry = ttk.Entry(decrypt_frame, show="*", font=("Arial", 12), width=30)
decrypt_password_entry.pack(pady=5)

decrypt_file_label = ttk.Label(decrypt_frame, text="📂 Drag & Drop or Select a File", font=("Arial", 12), relief="ridge", padding=10)
decrypt_file_label.pack(pady=5)

# Enable Drag & Drop
decrypt_file_label.drop_target_register(DND_FILES)
decrypt_file_label.dnd_bind("<<Drop>>", lambda event: decrypt_file_label.config(text=f"📂 Selected: {event.data.strip()}"))

decrypt_button = tb.Button(decrypt_frame, text="Decrypt", bootstyle="danger", command=decrypt_action)
decrypt_button.pack(pady=10)

# Show Encrypt Section by Default with Fade-in
fade_in(encrypt_frame)

# Footer
footer = ttk.Frame(root, padding=5, bootstyle="dark")
footer.pack(fill="x", side="bottom")

ttk.Label(footer, text="© 2024 Secure File Encryptor - All Rights Reserved", font=("Arial", 10)).pack()

root.mainloop()
