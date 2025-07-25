def obscure_image(image_path, output_path):
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        # Simple "obscuring" by converting image bytes to ASCII
        obfuscated_data = ''.join(format(byte, '02x') for byte in image_data)
        # Save the obfuscated data to a text file
        with open(output_path, "w") as output_file:
            output_file.write(obfuscated_data)
        print(f"Image has been obscured and saved as {output_path}.")
    except FileNotFoundError:
        print("Image file not found.")

def deobscure_image(obscured_path, restored_image_path):
    try:
        with open(obscured_path, "r") as obscured_file:
            obfuscated_data = obscured_file.read()
        # Convert the ASCII back to bytes
        restored_data = bytes.fromhex(obfuscated_data)
        # Save the restored data back as an image
        with open(restored_image_path, "wb") as restored_file:
            restored_file.write(restored_data)
        print(f"Image has been restored and saved as {restored_image_path}.")
    except FileNotFoundError:
        print("Obscured file not found.")

# Example usage
image_file_path = "example_image.jpg"  # The image file to be "secured"
obscured_output_path = "obscured_image.txt"
restored_image_output_path = "restored_image.jpg"
# Obscure and then restore the image
#obscure_image(image_file_path, obscured_output_path)
deobscure_image(obscured_output_path, restored_image_output_path)

