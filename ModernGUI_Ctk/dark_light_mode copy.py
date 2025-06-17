import customtkinter as ctk

# Set initial appearance and theme
ctk.set_appearance_mode("Light")  # Default mode
ctk.set_default_color_theme("blue")  # Optional theme

# Main window
app = ctk.CTk()
app.geometry("300x200")
app.title("Light/Dark Mode with Radio Buttons")

# Function to switch theme based on radio button selection
def switch_theme():
    mode = theme_var.get()
    if mode == "Light":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

# Variable to hold radio button selection
theme_var = ctk.StringVar(value="Light")

# Label
label = ctk.CTkLabel(app, text="Choose Theme Mode")
label.pack(pady=10)

# Light Mode Radio Button
light_radio = ctk.CTkRadioButton(app, text="Light Mode", variable=theme_var, value="Light", command=switch_theme)
light_radio.pack()

# Dark Mode Radio Button
dark_radio = ctk.CTkRadioButton(app, text="Dark Mode", variable=theme_var, value="Dark", command=switch_theme)
dark_radio.pack()

# Run the app
app.mainloop()
