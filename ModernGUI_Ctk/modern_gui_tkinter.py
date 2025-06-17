import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
btn = customtkinter.CTkButton(app, text="Click Me")
btn.pack()
app.mainloop()
