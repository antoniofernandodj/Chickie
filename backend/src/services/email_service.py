import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import Union
import logging


console = logging.getLogger("FLOW_LOGGER")


class EmailService:
    def __init__(
        self,
        from_email: str,
        senha: str,
        porta: int,
        servidor_smtp: str,
        tls: bool,
        ssl: bool,
    ):

        self.from_email = from_email
        self.sender_password = senha
        self.porta = porta
        self.servidor_smtp = servidor_smtp
        self.tls = tls
        self.ssl = ssl

        try:
            self.server: Union[smtplib.SMTP_SSL, smtplib.SMTP]
        except Exception:
            pass

        if self.ssl:
            self.server = smtplib.SMTP_SSL(servidor_smtp, porta)

        else:
            try:
                self.server = smtplib.SMTP(servidor_smtp, porta)
            except Exception as error:
                Error = type(error)
                raise Error(str(error))

        if self.tls:
            self.server.starttls()

    def render_template(self, arg1, arg2, **kwargs):
        raise

    def render_report(self, **kwargs):
        raise

    def set_subject(self, msg: MIMEMultipart, subject: str, to: str):
        msg.set_charset("utf-8")
        msg["Subject"] = subject
        msg["From"] = self.from_email
        msg["To"] = to
        return msg

    def enviar_email(self, subject: str, to: str, text: str):
        msg = MIMEMultipart("alternative")
        msg = self.set_subject(msg=msg, subject=subject, to=to)
        part1 = MIMEText(text, "plain")
        msg.attach(part1)

        try:
            self.server.ehlo()
            self.server.login(self.from_email, self.sender_password)
            self.server.sendmail(self.from_email, to, msg.as_string())

            console.log(logging.INFO, "Email enviado com sucesso!")
        except Exception as error:
            raise ConnectionError(str(error))
        finally:
            self.server.quit()
        return True

    def enviar_email_html(
        self, template_name: str, to: str, subject: str, contexto: dict
    ):
        msg = MIMEMultipart("alternative")
        msg = self.set_subject(msg=msg, subject=subject, to=to)

        html = self.render_template(
            template_name=template_name,
            dir="email",
            **contexto
        )
        part1 = MIMEText(subject, "plain")
        part2 = MIMEText(html, "html")
        msg.attach(part1)
        msg.attach(part2)

        try:
            self.server.ehlo()
            self.server.login(self.from_email, self.sender_password)
            self.server.sendmail(self.from_email, to, msg.as_string())
            logging.info("Email enviado com sucesso!")
        except Exception as error:
            raise ConnectionError(str(error))
        finally:
            self.server.quit()

        return None

    def enviar_email_html_com_anexo(
        self,
        template: str,
        to: str,
        subject: str,
        contexto: dict,
        anexo_template: str,
        extensao: str,
        nome_documento: str,
    ):
        msg = MIMEMultipart("mixed")
        msg = self.set_subject(msg=msg, subject=subject, to=to)

        html = self.render_template(
            template_name=template,
            dir="email", **contexto
        )

        pdf_bytes = self.render_report(
            template_name=anexo_template,
            contexto=contexto,
            path="email"
        )

        corpo = MIMEText(html, "html")

        anexo_mime = MIMEBase("application", "octet-stream")
        anexo_mime.set_payload(pdf_bytes)
        encoders.encode_base64(anexo_mime)
        anexo_mime.add_header(
            "Content-Disposition",
            "attachment",
            filename=f"{nome_documento}.{extensao}",
        )

        msg.attach(corpo)
        msg.attach(anexo_mime)

        try:
            self.server.ehlo()
            self.server.login(self.from_email, self.sender_password)
            self.server.sendmail(self.from_email, to, msg.as_string())
            logging.info("Email enviado com sucesso!")
        except Exception as error:
            raise ConnectionError(str(error))
        finally:
            self.server.quit()

        return None
