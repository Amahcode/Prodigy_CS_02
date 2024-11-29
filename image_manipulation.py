from PIL import Image

def encrypt_image(image_path, key):
    """
    Encrypts an image by swapping pixel values and applying XOR operation.

    Args:
        image_path (str): Path to the image file.
        key (int): Key for XOR operation.

    Returns:
        str: Path to the encrypted image file.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Swap pixel values of each row and column
    for x in range(image.width):
        for y in range(image.height):
            pixels[x, y] = (pixels[x, y][0] ^ key, pixels[x, y][1] ^ key, pixels[x, y][2] ^ key)

    # Apply XOR operation to each pixel
    for x in range(image.width):
        for y in range(image.height):
            pixels[x, y] = (pixels[x, y][0] ^ key, pixels[x, y][1] ^ key, pixels[x, y][2] ^ key)

    # Save the encrypted image
    encrypted_image_path = "encrypted_" + image_path
    image.save(encrypted_image_path)

    return encrypted_image_path

def decrypt_image(image_path, key):
    """
    Decrypts an image by swapping pixel values and applying XOR operation.

    Args:
        image_path (str): Path to the encrypted image file.
        key (int): Key for XOR operation.

    Returns:
        str: Path to the decrypted image file.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Apply XOR operation to each pixel
    for x in range(image.width):
        for y in range(image.height):
            pixels[x, y] = (pixels[x, y][0] ^ key, pixels[x, y][1] ^ key, pixels[x, y][2] ^ key)

    # Swap pixel values of each row and column
    for x in range(image.width):
        for y in range(image.height):
            pixels[x, y] = (pixels[x, y][0] ^ key, pixels[x, y][1] ^ key, pixels[x, y][2] ^ key)

    # Save the decrypted image
    decrypted_image_path = "decrypted_" + image_path
    image.save(decrypted_image_path)

    return decrypted_image_path

# Example usage
image_path = "path_to_your_image.jpg"
key = 123

encrypted_image_path = encrypt_image(image_path, key)
print("Encrypted image saved at:", encrypted_image_path)

decrypted_image_path = decrypt_image(encrypted_image_path, key)
print("Decrypted image saved at:", decrypted_image_path)


