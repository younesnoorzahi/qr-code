import qrcode as qr

# Enter your desired text!(desired)
code = qr.make("text")
code.save("name.png")

# You can create a Wi-Fi QRcode for yourself(desired)
code = qr.make("WIFI:S:{namessd};T:WPA;P:{password wifi}")
code.save("name.png")

# You can create a message for yourself to the desired person (optional)
code = qr.make("SMSTO:+989123456789: text")
code.save("name.png")
