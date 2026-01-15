# Educational Tutorial: Generating Personalized QR Codes with Dynamic Text and Color

# Learning Objective:
# This tutorial will guide you through creating personalized QR codes in Python.
# We will learn how to dynamically embed text into a QR code and customize its appearance
# with different colors for the QR code itself and its background.
# This is a practical skill for creating unique and informative QR codes for various purposes.

# We will use the 'qrcode' and 'PIL' (Pillow) libraries.
# If you don't have them installed, you can install them using pip:
# pip install qrcode[pil]

import qrcode
from PIL import Image

def generate_personalized_qr_code(data_text, filename="personalized_qr.png", qr_color="black", bg_color="white"):
    """
    Generates a personalized QR code with customizable text and colors.

    Args:
        data_text (str): The text or URL to be encoded in the QR code.
        filename (str, optional): The name of the output image file. Defaults to "personalized_qr.png".
        qr_color (str, optional): The color of the QR code modules (dots).
                                  Can be a color name (e.g., "red", "blue") or a hex code (e.g., "#FF5733").
                                  Defaults to "black".
        bg_color (str, optional): The color of the QR code background.
                                  Can be a color name or a hex code. Defaults to "white".
    """

    # --- Step 1: Create a QR Code object ---
    # The qrcode.QRCode class is the core of our QR code generation.
    # We initialize it with parameters that control its appearance and error correction.
    # version: Controls the size of the QR code. Higher numbers mean larger QR codes and can hold more data.
    #          We're leaving it to None to let the library automatically determine the best size for our data.
    # error_correction: How much redundancy is built into the QR code.
    #                   This allows the QR code to be scanned even if it's partially damaged or obscured.
    #                   qrcode.constants.ERROR_CORRECT_L: ~7% error correction
    #                   qrcode.constants.ERROR_CORRECT_M: ~15% error correction (default and often sufficient)
    #                   qrcode.constants.ERROR_CORRECT_Q: ~25% error correction
    #                   qrcode.constants.ERROR_CORRECT_H: ~30% error correction
    #                   We'll use M for a good balance between size and robustness.
    # box_size: The number of pixels for each box (module) in the QR code.
    #           A larger box_size will result in a larger overall QR code image.
    # border: The thickness of the border around the QR code. A border is important for reliable scanning.
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    # --- Step 2: Add the data to the QR code object ---
    # This is where we tell the QR code what information it needs to store.
    # The data_text variable can be a URL, a plain text string, contact information, etc.
    qr.add_data(data_text)

    # --- Step 3: Make the QR code fit the data ---
    # This method calculates the best QR code version (size) and generates the matrix
    # representing the QR code's pattern based on the added data and error correction.
    qr.make(fit=True)

    # --- Step 4: Create an image from the QR code matrix with custom colors ---
    # The make_image() method converts the QR code matrix into a Pillow Image object.
    # We can specify the fill_color (for the QR code modules) and back_color (for the background).
    # These parameters accept color names or hex codes.
    img = qr.make_image(fill_color=qr_color, back_color=bg_color)

    # --- Step 5: Save the generated QR code image ---
    # We save the Pillow Image object to a file with the specified filename.
    img.save(filename)

    # Print a confirmation message to the console.
    print(f"Successfully generated '{filename}' with data: '{data_text}'")
    print(f"QR Code Color: {qr_color}, Background Color: {bg_color}")

# --- Example Usage ---
# Now let's demonstrate how to use the function with different customizations.

if __name__ == "__main__":
    # Example 1: Basic QR code for a website
    print("--- Generating Example 1: Basic Website QR Code ---")
    generate_personalized_qr_code("https://www.python.org/")
    print("-" * 40) # Separator for clarity

    # Example 2: QR code with custom colors (blue QR, yellow background)
    print("--- Generating Example 2: Custom Colored QR Code ---")
    generate_personalized_qr_code(
        data_text="This is a custom message!",
        filename="custom_colored_qr.png",
        qr_color="blue",
        bg_color="yellow"
    )
    print("-" * 40)

    # Example 3: QR code using hex color codes
    print("--- Generating Example 3: Hex Color Codes QR Code ---")
    generate_personalized_qr_code(
        data_text="Check out this cool project!",
        filename="hex_color_qr.png",
        qr_color="#800080", # Purple
        bg_color="#ADD8E6"  # Light Blue
    )
    print("-" * 40)

    # Example 4: QR code for contact information (vCard format is common but for simplicity, just text here)
    print("--- Generating Example 4: Text-Based Contact QR Code ---")
    contact_info = "Name: Jane Doe\nEmail: jane.doe@example.com\nPhone: 123-456-7890"
    generate_personalized_qr_code(
        data_text=contact_info,
        filename="contact_qr.png",
        qr_color="darkgreen",
        bg_color="lightgray"
    )
    print("-" * 40)

    print("\nCheck your project directory for the generated QR code images!")
# End of tutorial.