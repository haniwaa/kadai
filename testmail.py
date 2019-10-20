import smtplib, ssl
from email.mime.text import MIMEText


def mysendmail():
    # 以下にGmailの設定を書き込む★ --- (*1)
    gmail_account = "tarooyamaaa@gmail.com"
    gmail_password = "Mikann19"
    # メールの送信先★ --- (*2)
    mail_to = "tarooyamaaa@gmail.com"
    #複数の時 --- mail_to = "tarooyamaaa@gmail.com, medium39s@gmail.com"

    # メールデータ(MIME)の作成 --- (*3)
    subject = "send mail test"
    body = "<h1>メール送信テスト</h1><img src='https://chart.apis.google.com/chart?cht=qr&chs=150x150&chl=%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AF%20http://example.com/%20%E3%81%A7%E3%81%99%E3%80%82'>"
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account

    # Gmailに接続 --- (*4)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
        context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg) # メールの送信
    print("ok.")
