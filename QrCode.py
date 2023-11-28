import pyqrcode

def create_Code():
    qrcode = pyqrcode.create(input("Digite o link do site: "))
    nome_qr = input("Digite o nome do seu QR Code: ")
# PT: A escala pode ser ajustavel conforme necessário EN: Scale can be adjustable as needed
    qrcode.png(nome_qr+".png", scale=6)
    print("QR Code gerado")

create_Code()
