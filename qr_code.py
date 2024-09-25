import qrcode
img=qrcode.make("https://www.youtube.com/watch?v=YZlt9Nr0bn0")
print(type(img))
img.save("Binod.png")
print("QR code has been generated successfully")