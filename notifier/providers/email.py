from email.mime.text import MIMEText
from email import charset
charset.add_charset('utf-8', charset.QP, charset.QP, 'utf-8')
import platform
import smtplib

from notifier.provider import Provider


class EmailNotify(Provider):
    def __init__(self, sender=None, addresses=[], *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not isinstance(addresses, list):
            addresses = [addresses]
        elif not addresses:
            import xdg.BaseDirectory as xdgb

            p = xdgb.load_first_config('notifier', 'addresses')
            if p is not None:
                with open(p, 'r') as f:
                    addresses = f.read().split()
            if not addresses:
                raise ValueError('No email addresses (defaults are read from {}/addresses, one address per line)'
                                 .format(xdgb.save_config_path('notifier')))
        for addr in addresses:
            if not isinstance(addr, str) or not '@' in addr:
                raise TypeError('`addresses` must be an email address or a list of email addresses')
        self._addresses = addresses

        if sender is None:
            sender = 'Notifier'
        self._sender = sender

        self._addr = 'notifier@{}'.format(platform.node())

    def notify(self):
        msg = MIMEText(self.text, 'plain', 'utf-8')
        msg['To'] = ', '.join(self._addresses)
        msg['From'] = '{} <{}>'.format(self._sender, self._addr)
        msg['Subject'] = self.subject
        msg['X-Mailer'] = 'notify.py'

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
