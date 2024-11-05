import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

class EmailHandler:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password, sender_email):

        


        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.sender_email = sender_email

    def send_email(self, recipient_email, subject, body, attachment_path=None):
        """
        Send an email with optional attachment.
        
        :param recipient_email: The email address to send the email to.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        :param attachment_path: Optional path to an attachment.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # If there's an attachment, add it
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                    msg.attach(part)

            # Connect to the SMTP server
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())

            print(f"Email successfully sent to {recipient_email}")

        except Exception as e:
            print(f"Error sending email: {e}")
    
    def send_resolution_email(self, recipient_email, downtime_id):
        """
        Send an email notifying that the downtime issue has been resolved.
        
        :param recipient_email: The email address to send the notification to.
        :param downtime_id: The ID of the resolved downtime.
        """
        subject = f"Downtime Resolved - ID: {downtime_id}"
        body = f"The downtime issue with ID {downtime_id} has been resolved. Please check the system for updates."
        self.send_email(recipient_email, subject, body)
