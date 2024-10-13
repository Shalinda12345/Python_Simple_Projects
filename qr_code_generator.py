# install all the libraries needed (pip3 install qrcode Image)
# create a function that collects a text and convert it to a qr code
# save the qr code as an image
# run the function


import qrcode

def generate_qrcode(text, saveName):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(saveName + ".png")

url = input("Enter your url: ")
saveName = input("Enter the save name of QR Code: ")
generate_qrcode(url, saveName)