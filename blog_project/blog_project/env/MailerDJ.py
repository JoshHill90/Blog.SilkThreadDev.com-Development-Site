import ssl
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import os
from dotenv import load_dotenv

current_dir = Path(__file__).resolve().parent
ven = current_dir / ".env"
load_dotenv(ven)
#-------------------------------------------------------------------------------------------------------#
# Secret Values
#-------------------------------------------------------------------------------------------------------#


class AutoReply:

    hosting_SMTP = os.getenv("EMAIL_HOSTING")
    main_email = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_port = os.getenv("EMAIL_PORT")
    email_backend = os.getenv("EMAIL_BACKEND_SMTP")
    alart_email = os.getenv("REPLYER")
    

    #------------------------#
    # Contact form auto reply
    #------------------------#

    def contact_request(self, reciver, name):

        contact_subject = "Thank You for Contacting Silk Thread Dev!"

        contact_body = f""" 
    Dear {name},

Thank you for reaching out to Silk Thread Dev! I'm Josh, the web developer behind this 
platform. I appreciate you taking the time to get in touch with me.

If your inquiry pertains to my web development services, please provide me with more details 
about your project. I am currently open to taking on new projects and would love to learn more 
about your requirements.

For any feedback or questions related to my developer blog, I'm all ears! Your thoughts and 
opinions are invaluable to me, and I'm eager to hear what you have to say.

If your message is regarding my portfolio, I'm delighted to assist you further. 
Let me know how I can be of help, or if you would like to schedule a meeting to 
discuss your needs in detail.

Once again, thank you for contacting Silk Thread Dev. I'm excited to connect 
with you and explore how we can collaborate to achieve your goals.

Regards,
Josh
Silk Thread Dev

Josh@SilkThreaddev.com

P.S. If you have any developer friends who mwight find our blog helpful, feel free to share the subscription 
link with them. Your support is greatly appreciated. Blog.SilkThreadDev.com

"""
        
        mailer = EmailMessage()

        mailer['From'] = formataddr((Header("Silk Thread Blog", 'utf-8').encode(), f"{self.main_email}"))
        mailer['To'] = reciver
        mailer['Subject'] = contact_subject
        mailer.set_content(contact_body)

        with smtplib.SMTP(self.hosting_SMTP, self.email_port) as server:
            try:
                server.starttls()
                server.login(self.main_email, self.email_password)
                server.sendmail(self.main_email, reciver, mailer.as_string())
                server.close()
                print('email sent')
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")
        
    #------------------------#
    # Contact form auto reply
    #------------------------#

    def mailing_list(self, reciver):

        contact_subject = "Thanks for Subscring"
        plain_text = """
Thank You for Subscribing!
        
I wanted to take a moment to express my gratitude for subscribing to the Silk Thread Blog notifications.

As a solo developer, I'm genuinely appreciative of your decision to stay connected with us. Your subscription 
means a lot, and I'm excited to have you as part of our growing community.
In the coming days, you'll receive updates on web development insights, tips, and tutorials straight to your 
inbox. I'm committed to providing valuable content that can enhance your knowledge and skills in Python, 
JavaScript, Django, CSS, HTML, Bootstrap, MySQL, JSON, and more.

If there are specific topics or areas you'd like us to cover, or if you have any questions related to 
development, please don't hesitate to let me know. Your feedback is essential in tailoring our content 
to suit your interests.

Thank you again for joining us on this journey of learning and exploration. Together, we'll continue to 
delve into the world of development and make meaningful contributions to the digital landscape.

Regards,
Josh
Silk Thread Dev

Josh@SilkThreaddev.com

P.S. If you have any developer friends who mwight find our blog helpful, feel free to share the subscription 
link with them. Your support is greatly appreciated. Blog.SilkThreadDev.com

"""

        body_as_text = MIMEText(plain_text, 'plain')

        mailer = EmailMessage()

        mailer['From'] = formataddr((Header("Silk Thread Blog", 'utf-8').encode(), f"{self.main_email}"))
        mailer['To'] = reciver
        mailer['Subject'] = contact_subject
        mailer.set_content(body_as_text)

        with smtplib.SMTP(self.hosting_SMTP, self.email_port) as server:
            try:
                server.starttls()
                server.login(self.main_email, self.email_password)
                server.sendmail(self.main_email, reciver, mailer.as_string())
                server.close()
                print('email sent')
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")


    #------------------------#
    # contact form Alart
    #------------------------#

    def contact_alart(self, email, name, subject, body):

        contact_subject = "Contact Form Alert"

        contact_body = f""" 
        Subject: {subject}

        From: {email} - Name: {name}

        Message:
            {body}"""



        mailer = EmailMessage()

        mailer['From'] = formataddr(("Contact Form", f"{self.alart_email}"))
        mailer['To'] = self.main_email
        mailer['Subject'] = contact_subject
        mailer.set_content(contact_body)

        with smtplib.SMTP(self.hosting_SMTP, self.email_port) as server:
            try:
                server.starttls()
                server.login(self.main_email, self.email_password)
                server.sendmail(self.main_email, self.main_email, mailer.as_string())
                server.close()
                print('alart sent')
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")


    #------------------------#
    #  Comment Secton Alart
    #------------------------#

    def new_comment_posted(self, name, email, user_id, comment, blog ):

        contact_subject = f"New Comment Posted On #{blog} {blog.title}"

        contact_body = f""" 
Subject: {user_id}

From: {email} - {user_id} - Name: {name}

Message:
{comment}"""


        mailer = EmailMessage()

        mailer['From'] = formataddr(("New Comment", f"{self.alart_email}"))
        mailer['To'] = self.main_email
        mailer['Subject'] = contact_subject
        mailer.set_content(contact_body)

        with smtplib.SMTP(self.hosting_SMTP, self.email_port) as server:
            try:
                server.starttls()
                server.login(self.main_email, self.email_password)
                server.sendmail(self.main_email, self.main_email, mailer.as_string())
                server.close()
                print('alart sent')
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")

"""
#### Test
test_send = os.getenv("TEST_SEND")

subject_test = "TEST"

body_test ="body"

SMTP = AutoReply()

SMTP.contact_request(test_send, 'john')
print('smtp request')
SMTP.contact_alart(test_send, 'john', subject_test, body_test)


SMTP.mailing_list('joshua.j.hill90@gmail.com')"""

