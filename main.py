# A simple QR generator in Python

import qrcode

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter the data to be encoded: ")
    filename = input("Enter the filename to save the QR code as: ")
    generate_qr(data, filename)
    print("QR code generated successfully!")