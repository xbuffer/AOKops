# 邮件报警类
from django.core.mail import send_mail
import time
from AOKops import settings
import logging


class SendMail(object):
    def __init__(self, receive_addr, sub_info, content_info):
        sub_data = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        self.receive_addr = receive_addr
        self.sub_info = sub_info + " " + sub_data
        self.content_info = content_info

    def send(self):
        try:
            send_mail(
                subject=self.sub_info,
                message=self.content_info,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=self.receive_addr,
                fail_silently=False,
            )
            return True
        except Exception as e:
            logging.error(str(e))
            return False
