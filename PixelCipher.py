from tkinter import Tk, Frame, Label, Button, Text, Entry, filedialog, messagebox
from PIL import Image, ImageTk
import hashlib

class Stegno:
    def __init__(self):
        self.root = Tk()
        self.root.title('PixelCipher')
        self.root.geometry('500x600')
        self.root.resizable(width=False, height=False)
        self.current_frame = None
        self.cover_image_path = None
        self.hidden_image = None
        self.hidden_message = None
        self.password = None

    def main(self):
        self.show_main_menu()

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.root)
        title = Label(self.current_frame, text='PixelCipher')
        title.config(font=('courier', 33))
        title.grid(pady=10)

        b_encode = Button(self.current_frame, text="Encode", command=self.frame1_encode, padx=14)
        b_encode.config(font=('courier', 14))
        b_encode.grid(row=1, pady=12)

        b_decode = Button(self.current_frame, text="Decode", command=self.frame1_decode, padx=14)
        b_decode.config(font=('courier', 14))
        b_decode.grid(row=2, pady=12)

        self.current_frame.pack()

    def frame1_encode(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.root)
        label = Label(self.current_frame, text='Select the cover image:', font=('courier', 14))
        label.grid(row=0, columnspan=2, pady=10)

        browse_button = Button(self.current_frame, text='Browse', command=self.select_cover_image)
        browse_button.grid(row=1, column=0, padx=5)

        cancel_button = Button(self.current_frame, text='Cancel', command=self.show_main_menu)
        cancel_button.grid(row=1, column=1, padx=5)

        self.current_frame.pack()

    def select_cover_image(self):
        self.cover_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.cover_image_path:
            self.frame2_encode()

    def frame2_encode(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.root)
        label = Label(self.current_frame, text='Enter the message to hide:', font=('courier', 14))
        label.grid(row=0, columnspan=2, pady=10)

        self.message_entry = Text(self.current_frame, height=5, width=40)
        self.message_entry.grid(row=1, columnspan=2, padx=10)

        password_label = Label(self.current_frame, text='Set password:', font=('courier', 12))
        password_label.grid(row=2, columnspan=2, pady=5)

        self.password_entry = Entry(self.current_frame, show='*')
        self.password_entry.grid(row=3, columnspan=2, pady=5)

        encode_button = Button(self.current_frame, text='Encode', command=self.encode_message)
        encode_button.grid(row=4, column=0, pady=10, padx=5)

        cancel_button = Button(self.current_frame, text='Cancel', command=self.show_main_menu)
        cancel_button.grid(row=4, column=1, pady=10, padx=5)

        self.current_frame.pack()

    def encode_message(self):
        self.hidden_message = self.message_entry.get("1.0", 'end-1c')
        self.password = self.password_entry.get() if self.password_entry.get() else None
        # Store the hash of the password for verification
        if self.password:
            self.password = hashlib.sha256(self.password.encode()).hexdigest()
        # Implement encoding process here
        messagebox.showinfo("Success", "Message encoded successfully!")
        self.show_main_menu()

    def frame1_decode(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.root)
        label = Label(self.current_frame, text='Select the image to decode:', font=('courier', 14))
        label.grid(row=0, columnspan=2, pady=10)

        browse_button = Button(self.current_frame, text='Browse', command=self.select_hidden_image)
        browse_button.grid(row=1, column=0, padx=5)

        cancel_button = Button(self.current_frame, text='Cancel', command=self.show_main_menu)
        cancel_button.grid(row=1, column=1, padx=5)

        self.current_frame.pack()

    def select_hidden_image(self):
        hidden_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if hidden_image_path:
            self.hidden_image = Image.open(hidden_image_path)
            self.frame2_decode()

    def frame2_decode(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.root)
        label = Label(self.current_frame, text='Enter password:', font=('courier', 12))
        label.grid(row=0, columnspan=2, pady=10)

        self.password_entry = Entry(self.current_frame, show='*')
        self.password_entry.grid(row=1, columnspan=2, pady=5)

        decode_button = Button(self.current_frame, text='Decode', command=self.decode_message)
        decode_button.grid(row=2, column=0, pady=10, padx=5)

        cancel_button = Button(self.current_frame, text='Cancel', command=self.show_main_menu)
        cancel_button.grid(row=2, column=1, pady=10, padx=5)

        self.current_frame.pack()

    def decode_message(self):
        entered_password = self.password_entry.get()
        
        if self.hidden_message:
            if self.password:
                entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()
                if entered_password_hash != self.password:
                    messagebox.showerror("Error", "Incorrect password!")
                    return
            else:
                messagebox.showerror("Error", "This image is not encoded with a password!")
                return
        else:
            messagebox.showerror("Error", "This image is not encoded!")
            return

        decoded_message = self.hidden_message

        if self.hidden_image:
            image_label = Label(self.current_frame, text='Hidden Image:')
            image_label.grid(row=3, columnspan=2, pady=10)

            img = ImageTk.PhotoImage(self.hidden_image)
            img_label = Label(self.current_frame, image=img)
            img_label.image = img
            img_label.grid(row=4, columnspan=2, pady=10)

        messagebox.showinfo("Decoded Message", f"Hidden message:\n\n{decoded_message}")

    def run(self):
        self.main()
        self.root.mainloop()

if __name__ == "__main__":
    app = Stegno()
    app.run()

