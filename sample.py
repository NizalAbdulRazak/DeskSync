import customtkinter
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class gui(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Remote Desktop System")
        self.geometry("640x376")
        self.resizable(False, False)
        # self.overrideredirect("True")
        self.grid_rowconfigure((0, 1), weight = 1)
        # self.grid_rowconfigure(1, weight = 1)
        # self.grid_columnconfigure(1, weight = 1)
        
        self.sidebar = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar.grid(row = 0, column = 0, sticky = 'nsew')

        self.home = customtkinter.CTkButton(self.sidebar, text = "Home")
        self.home.grid(row = 0, column = 0, padx = 20, pady = (70, 10))

        self.connect = customtkinter.CTkButton(self.sidebar, text = "Connect")
        self.connect.grid(row = 1, column = 0, padx = 20, pady = 10)

        self.settings = customtkinter.CTkButton(self.sidebar, text = "Settings")
        self.settings.grid(row = 2, column = 0, padx = 20, pady = 10)

        self.disconnect = customtkinter.CTkButton(self.sidebar, text = "Disconnect")
        self.disconnect.grid(row = 3, column = 0, padx = 10, pady = (50,10))

        self.homepage = customtkinter.CTkFrame(self, corner_radius=0, fg_color='#121212', width = 100)
        self.homepage.grid(row = 0, column = 1, sticky = 'nsew')

        # self.time = customtkinter.CTkLabel(self.homepage, text = time.time())
        # self.time.grid(row = 0, column = 0)



        
        


app = gui()
app.mainloop()



