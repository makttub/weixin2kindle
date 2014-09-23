#coding: utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
import os
from email.mime.base import MIMEBase


def send(u):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((\
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    from_addr = os.environ.get('EMAIL_USERNAME')
    password = os.environ.get('EMAIL_PASSWORD')
    to_addr = u.email
    smpt_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = _format_addr('weixin2kindle <%s>' % from_addr)
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header('News of Your Weixin', 'utf-8').encode()

    msg.attach(MIMEText('Please check attachment', 'plain', 'utf-8'))

    mobipath = u.dirpath + os.sep + u.timenow + '.mobi'
    with open(mobipath, 'rb') as f:
        mime = MIMEBase('text', 'plain', filename=u.timenow+'.mobi')
        mime.add_header('Content-Disposition', 'attachment', filename=u.timenow+'.mobi')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')

        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    server = smtplib.SMTP(smpt_server, smtp_port)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    print u.name + ': sending...'
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit

    logpath = os.path.join(u.dirpath, u.timenow+'.log')
    with open(logpath, 'a') as f:
        f.write('\n---------------------------------------------\nStatus of send:\n')
        f.write("Success")
