import customtkinter as ctk

# Set default theme and mode
ctk.set_appearance_mode("Light")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")  # Optional: "dark-blue", "green", "blue"

# Main window
app = ctk.CTk()
app.title("Light/Dark Mode Example")
app.geometry("300x200")

# Function to toggle mode
def toggle_mode():
    current = mode_switch.get()
    if current == "Dark":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("Light")

# Label
label = ctk.CTkLabel(app, text="Toggle Light/Dark Mode")
label.pack(pady=20)

# Switch (Dark / Light)
mode_switch = ctk.CTkOptionMenu(app, values=["Light", "Dark"], command=lambda _: toggle_mode())
mode_switch.set("Light")
mode_switch.pack()

# Run the app
app.mainloop()
