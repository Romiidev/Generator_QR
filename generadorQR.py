import qrcode
import qrcode.constants
import streamlit as st

nombrefile = "qr_codigo/qr_code.png"

def generador_qr(url,nombrefile):
    qr= qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color= "pink", back_color= "black") 
    img.save(nombrefile)

st.set_page_config(page_title="Generador de QR", page_icon="o", layout="centered")
st.image(r"C:\Users\romii\OneDrive\Documentos\python\.venv\images\qr.jpg", use_container_width=True)
st.title("Generar codigo QR")
url = st.text_input("Ingrese el URL")

if st.button("Generar Codigo QR "):
    generador_qr(url, nombrefile)
    st.image(nombrefile, use_container_width=True)
    with open(nombrefile,"rb") as f:
                image_data = f.read()
    download = st.download_button(label= "Descarga el QR", data=image_data, file_name= "qr_generated.png",)



