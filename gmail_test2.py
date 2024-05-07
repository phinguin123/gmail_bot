import smtplib
import schedule
import time
from pathlib import Path
from email.mime.text import MIMEText

count = 0

def sendMail(me, you, msg):
    print("inside")
    global count
    count += 1
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, 'hwlo pved ctuo onky')
    msg = MIMEText(msg)
    msg['Subject'] = str(count) + '일차 : 형, 오늘도 고생했어. 내일도 화이팅이야!'
    smtp.sendmail(me, you, msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    from_email = ""
    to_email = ""

    home = str(Path.home())
    with open(home+"/gmail_bot/emails", 'r') as file:
        from_email = file.readline()
        to_email = file.readline()

    schedule.every().day.at("14:59").do(sendMail, from_email, to_email,'아자아자 화이팅!!!!')

    while True:
        schedule.run_pending()
        time.sleep(59)
        print("outside")
