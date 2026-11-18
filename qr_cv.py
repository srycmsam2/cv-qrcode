
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Adresse de ta page web après publication
URL_SITE = "https://github.com/srycmsam2.io/cv-qrcode/"

# Configuration du QR code
qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=20,
    border=4
)

# Ajouter l'adresse du site
qr.add_data(URL_SITE)
qr.make(fit=True)

# Génération de l'image
image = qr.make_image(
    fill_color="#182431",
    back_color="white"
)

# Enregistrement
image.save("QR_CV_Sara.png")

print("QR code généré avec succès !")
print("Fichier : QR_CV_Sara.png")
print("Adresse :", URL_SITE)
