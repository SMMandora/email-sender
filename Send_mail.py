from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "<Sender mail ID>"
password = "<Sender password for mail ID>"
from_email = username
to_list = ["<List of people you want to send mail to >"]

try:
    email_conn  = smtplib.SMTP(host, port)
    email_conn.ehlo()
    # print("hello")
    email_conn.starttls()
    email_conn.login(username, password)

    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "This is a test mail with some plain text as well as html"
    the_msg['From'] = from_email
    the_msg['To'] = to_list

    plain_text = "This is normal plain text of email"  
    html_text = """
    <html>
    <head></head>
        <body>
        <p>This is <b> html text </b> of <i> email </i> </p>   
        </body>
    </html>
    """
    plain_txt = MIMEMultipart(plain_text, "plain")
    html_txt = MIMEMultipart(html_text, "html")
    the_msg.attach(plain_txt)
    the_msg.attach(html_txt)
    print(the_msg.as_string())
    #email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("Error sending email") 