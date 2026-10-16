# OCR draft from screenshot; verify syntax and completeness before running.
s[5): dmport qrcode
urlzinput ("Enter URL to Make QR: ")
Af url.startsuith(*http://*) or url.startswith("https://*):
arzqrcode.QRcode(version=1,
‘error_correction=qrcode.constants.ERROR_CORRECT H,
box_sizesia,# 1810
border=4
)
ar.add_data(uel)
ar.make()
Amage=qrmake_image(Fill_colors"blue", back_color="red")
mage. save(“Thirdgr-png")
else:
print("Invalid Url..1I! Must start with http on https")
Enter URL to Make QR: https://mu.the-grcode-generator.con/
