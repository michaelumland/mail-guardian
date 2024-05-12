from smtplib import SMTP, SMTPException
from dns.resolver import resolve, NXDOMAIN
from re import compile, match

class MailGuardian:
    def __init__(self, sender='verify@gmail.com', smtp_port=25):
        self.sender = sender
        self.smtp_port = smtp_port
        self.email_regex = compile(
            r'^(([^<>()\[\]\\.,;:\s@\"]+(\.[^<>()\[\]\\.,;:\s@\"]+)*)'
            r'|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])'
            r'|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
        )

    def check_format(self, email: str) -> bool:
        """
        Check if the email address format is valid.
        """
        return bool(match(self.email_regex, email))

    def check_mailbox(self, email: str) -> bool:
        """
        Check if the mailbox exists for the given email address.
        """
        try:
            mx_record = resolve(email.split('@')[1], 'MX')
            mx_exchange = str(mx_record[0].exchange).removeprefix('.')

            with SMTP(mx_exchange, self.smtp_port) as smtp:
                smtp.ehlo(mx_exchange)
                smtp.mail(self.sender)
                smtp.rcpt(email)
                response, _ = smtp.rcpt(email)
                smtp.quit()

                return response == 250 # response 250 means the mailbox should exist

        except (NXDOMAIN, SMTPException, TimeoutError):
            return False
        
    def validate_email(self, email: str) -> bool:
        """
        Validate the given email address by checking format and mailbox existence.
        """
        return self.check_format(email) and self.check_mailbox(email)
