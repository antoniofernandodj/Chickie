from config import settings as s  # type: ignore
from mailersend import emails  # type: ignore


class EmailService:
    EMAIL = s.EMAIL_ADDRESS
    NAME = s.EMAIL_NAME
    mailer = emails.NewEmail(s.EMAIL_API_KEY)

    @classmethod
    def send_email(cls, to: str, to_name: str, subject: str, html: str):
        result = cls.mailer.send({
            'html': html,
            'subject': subject,
            'reply_to': {"name": cls.NAME, "email": cls.EMAIL},
            'to': [{"name": to_name, "email": to}],
            'from': {"name": cls.NAME, "email": cls.EMAIL}
        })

        return result
