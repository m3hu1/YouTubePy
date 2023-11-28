import customtkinter
from pytube import YouTube

def downloadFile():
    try:
        link = linkEntry.get()
        obj = YouTube(link)
        video = obj.streams.get_highest_resolution()
        
        titleLabel.configure(text=obj.title)
        endLabel.configure(text="")
        
        video.download()

        endLabel.configure(text="Downloaded", text_color="green")

    except Exception as e:
        endLabel.configure(text=f"Error: {str(e)}", text_color="red")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("400x150")
app.title("YouTubePy")

titleLabel = customtkinter.CTkLabel(app, text="Paste the video's URL below")
titleLabel.pack(padx=5,pady=5)

url = customtkinter.StringVar()

linkEntry = customtkinter.CTkEntry(app, width=380, height=35, textvariable=url)
linkEntry.pack()

endLabel = customtkinter.CTkLabel(app, text="")
endLabel.pack()

download = customtkinter.CTkButton(app, text="Download", command=downloadFile)
download.pack(padx=5,pady=5)

app.mainloop()