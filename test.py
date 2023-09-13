import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Algo Analyzer")
        self.geometry(f"{1000}x{600}")

        # configure grid layout 
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=3)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure((0), weight=1)

         # create left column frame with about section
        self.left_frame = customtkinter.CTkFrame(self, width=100, corner_radius=25)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.left_frame, text="Algorithm Analyzer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        logo_image = ImageTk.PhotoImage(Image.open("img/header_image.jpg").resize((30,30)))
        self.about_button = customtkinter.CTkButton(self.left_frame, text="About", image=logo_image)
        self.about_button.grid(row=1, column=0, padx=20, pady=10)

        # tabview for different modes 
        self.modesview = customtkinter.CTkTabview(self, width=200, corner_radius=25)
        self.modesview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.modesview.add("Easy Mode")
        self.modesview.add("Mode 2")
        self.modesview.add("Mode3 3")
    
        # setting up the info/ optput box 
        self.infobox = customtkinter.CTkTextbox(self, width=250)
        self.infobox.grid(row=0, column=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()