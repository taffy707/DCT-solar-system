import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.errors import *

# Email Configuration
smtp_serer = 'your_smtp_server'
smtp_port = 587 # OR ENTER YOUR OWN PORT NUMBER
sender_email = 'your_email@example.com' # This will be taken from the client's data in the database
receiver_email = 'recipient@example.com' # This will always be Damian's Email
password = 'your_password'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Test email from Python'
msg['From'] = sender_email
msg['To'] = receiver_email

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
    <html>
        <body>
            <p>Hi!<br>
                How are you?<br>
                Here is the <a href="https://www.python.org">link</a> you wanted.
            </p>
        </body>
    </html>
"""

# Attach parts into message container.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

# Send the message via the SMTP server.
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")
finally:
    server.quit()