import qrcode

def generate_qr_codes(items, color):

    for index, item in enumerate(items, start=1):
        qr = qrcode.QRCode(
            version=4,  # Size of QR (1 = small)
            error_correction=qrcode.ERROR_CORRECT_H,
            box_size=10,  # Size of each box
            border=4,  # Border thickness
        )
        qr.add_data(item)
        qr.make(fit=True)

        img = qr.make_image(fill_color=color, back_color="white")
        filename =f"Qrcode_module_qr_{index}.png"
        img.save(filename)
        print(f"Saved: {filename}")


raw_input_text = input(
    "Enter URLs/texts separated by commas (example: https://a.com,Hello,https://b.com): "
)
items = [part.strip() for part in raw_input_text.split(",") if part.strip()]

if not items:
    print("No valid URLs/texts provided.")
else:
    color = input("Enter any color for the QR codes: ").strip() or "black"
    generate_qr_codes(items, color)





