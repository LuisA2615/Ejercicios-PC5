import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del correo
from_addr = 'tu_email@example.com'
to_addr = 'destinatario@example.com'
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Reporte de Vinos'

# Adjuntar el archivo
with open('mejores_vinos_por_continente.csv', 'r') as file:
    msg.attach(MIMEText(file.read(), 'plain'))

# Conectar y enviar el correo
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login(from_addr, 'tu_contraseña')
    server.send_message(msg)

print("Correo enviado.")
