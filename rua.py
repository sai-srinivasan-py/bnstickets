import cv2
import smtplib
import qrcode
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyrebase
import random

# me == my email address
# you == recipient's email address
me = "donotreplysuperhacks@gmail.com"
input_emails = input("Emails Seperated by Commas: ")
emails = input_emails.split(',')


firebaseConfig = {
    "apiKey": "AIzaSyB4PU2fxocFm8cFKEQxHCxgBjVh3552Lbg",
    "authDomain": "superhackticketing.firebaseapp.com",
    "projectId": "superhackticketing",
    "storageBucket": "superhackticketing.appspot.com",
    "messagingSenderId": "791811168060",
    "appId": "1:791811168060:web:e4387c96fd26f2d8307039",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)

fstorage = firebase.storage()
fauth = firebase.auth()

email = 'jahsgdjhaSGUDYjahsdg@kajhsbdJKHG.com'
password = '6EsS+Fzg!}sVg-NG'

user = fauth.sign_in_with_email_and_password(email, password)

for you in emails:
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Breathe-n-Sync"
    msg['From'] = me
    msg['To'] = you


    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    message = "Python is fun"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)

    name = you.encode('ascii')
    import datetime
    timestamp = str(datetime.datetime.now()).encode('ascii')
    event_date = "Augest 1st 2021".encode('ascii')
    token_id = str(random.randint(1000000, 99999999)).encode('ascii')

    bytes_1 = base64.b64encode(name)
    bytes_2 = base64.b64encode(timestamp)
    bytes_3 = base64.b64encode(event_date)
    bytes_4 = base64.b64encode(token_id)

    new_name = bytes_1.decode('ascii')
    new_timestamp = bytes_2.decode('ascii')
    new_event_date = bytes_3.decode('ascii')
    new_token_id = bytes_4.decode('ascii')

    qrtoken = f"{new_name}${new_timestamp}${new_event_date}${new_token_id}"
    print(f'Token for {name}: {qrtoken}')
    token_sheet = open('tokens.txt', 'a')
    token_sheet.write(f'{qrtoken},')

    qr.add_data(qrtoken)
    qr.make(fit=True)

    img = qr.make_image()

    import random
    name = f'{random.randint(100000,11111111111100000000)}.png'
    img.save(name)

    fstorage.child(name).put(name)
    ImgUrl = fstorage.child(name).get_url(user['idToken'])
    import os

    os.remove(name)

    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
    <head>
    </head>
    <body>
        <p>Your Ticket!</p>
    """

    html += f"""
        <img src='{ImgUrl}'>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(me, 'QvCa5Rm`R-2Xz6L@')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()

'''
# initalize the cam
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        for i in range(len(bbox)):
            # draw all lines
            cv2.line(img, tuple(bbox[i][0]), tuple(
                bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        if data:
            print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
'''
