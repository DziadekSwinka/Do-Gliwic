import smtplib

email="jakub.kleczek.72@gmail.com"
email_reciver="swinkadziadek@gmail.com"
text=f"Mail wyslany przez pytona\n\nPyton to taki wunsz.\nPozdrawiam serdecznie \nMietek"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email,"iijhyuixgffabgxp")
server.sendmail(email,email_reciver,text)
print(f"Wysłano maila do"+email_reciver)