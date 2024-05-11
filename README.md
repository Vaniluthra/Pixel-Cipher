# PixelCipher - Steganography Application

PixelCipher is a simple steganography application built with Python, Tkinter, and Pillow (PIL) for encoding and decoding hidden messages within images.

## Requirements

- **Python**:
  - Ensure Python 3 is installed on your computer. If not, download and install Python from the [official Python website](https://www.python.org/downloads/).

- **Tkinter**:
  - Tkinter comes bundled with Python and serves as the standard GUI library for creating graphical user interfaces.

- **PIL (Pillow)**:
  - Pillow (PIL fork) is used for image processing tasks such as opening, manipulating, and saving various image file formats. Install Pillow using pip:
    ```
    pip install pillow
    ```

## Running the Application

1. **Download the Code**:
   - Download or clone the provided Python script (`stegno_app.py`) to your local machine.

2. **Install Dependencies**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `stegno_app.py`.
   - Install Pillow library using pip if not already installed:
     ```
     pip install pillow
     ```

3. **Run the Application**:
   - In the terminal or command prompt, navigate to the directory containing `stegno_app.py`.
   - Execute the script using Python:
     ```
     python stegno_app.py
     ```

## Using the Application

- Upon running the application, a window titled "PixelCipher" will appear with a main menu interface offering two options:

- **Encoding Instructions**:
  - Click `Encode` and follow the prompts to select a cover image and enter a message.
  - Provide a password to encrypt the hidden message.
  - Upon successful encoding, a confirmation message will be displayed.

- **Decoding Instructions**:
  - Click `Decode` and choose an encoded image.
  - Enter the password used during encoding.
  - The hidden message will be extracted and displayed in a message box.

## Additional Notes

- Supported image formats for encoding and decoding include `.png`, `.jpg`, and `.jpeg`.

## Screenshots

![image](https://github.com/Vaniluthra/Pixel-Cipher/assets/94587714/e437519a-9dbe-4a21-aa17-3549812c2a5c)

![image](https://github.com/Vaniluthra/Pixel-Cipher/assets/94587714/203c53f4-9dd4-4999-a67e-4592a7d3cf52)

