import qrcode

# Ask the user for a link
data = input("Enter the link you want to generate a QR code for: ")

# Create the QRCode object with some settings
qr = qrcode.QRCode(
    version=15,  # Controls the size of the QR code
    box_size=18,  # Size of each box in the QR code
    border=5  # Border around the QR code
)

# Add the user-provided data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill="black", back_color="white")

# Save the generated QR code as an image file
img.save("qrcode.png")

print("QR code has been generated and saved as 'qrcode.png'!")
