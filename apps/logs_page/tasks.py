from config import celery_app
import requests
from apps.logs_page.models import SiteAlert, MessageType
import logging
from django.utils import timezone
from django.conf import settings


@celery_app.task(name='test')
def test_db():
    print(f"hola mundo {timezone.now()}")
#
# @celery_app.task(name='check_page_status')
# def check_page_status():
#
#     site_list = SiteAlert.objects.filter(enable=True)
#     for site in site_list:
#         response = validate_page(site.url_site)
#         if response["status_code"] == 200:
#             data = {"status_code": response["status_code"],
#                     "message_error": response["message"]}
#             create_register(data, site)
#         else:
#             validate_send_email(response, site)
#
#
# def validate_page(url):
#     """Valid the page status."""
#     status_msg = {}
#     try:
#         response = requests.get(url)
#         status_msg["status_code"] = response.status_code
#         status_msg["message"] = response.reason
#         logging.info(msg=status_msg)
#
#     except requests.Timeout as e:
#         status_msg["status_code"] = 500
#         status_msg["message"] = "Timeout error"
#         logging.error(msg=status_msg)
#     except requests.ConnectionError as e:
#         status_msg["status_code"] = 500
#         status_msg["message"] = "Connection error"
#         logging.error(msg=status_msg)
#     except requests.HTTPError as e:
#         status_msg["status_code"] = 500
#         status_msg["message"] = "HTTP error occurred"
#         logging.error(msg=status_msg)
#     except requests.TooManyRedirects as e:
#         status_msg["status_code"] = 500
#         status_msg["message"] = "Too many redirects"
#         logging.error(msg=status_msg)
#     except requests.RequestException as e:
#         status_msg["status_code"] = 500
#         status_msg["message"] = "An error occurreds"
#         logging.error(msg=status_msg)
#     return status_msg
#
#
# def validate_send_email(data, site_instance):
#     """"""
#     new_register = {"status_code": data["status_code"],
#                     "message_error": data["message"]
#                     }
#     old_datetime = timezone.datetime.now() - timezone.timedelta(
#         minutes=settings.TASK_VALIDATE_MINUTES)
#     register = site_instance.siteregister_set.filter(
#         status_code=data["status_code"],
#         created__gte=old_datetime
#     ).first()
#
#     if not register:
#         new_register["is_alerted"] = True
#         send_email(new_register)
#
#     create_register(new_register, site_instance)
#
#
# def send_email(register):
#     pass
#
#
# def create_register(data, site_instance):
#     """"""
#     site_instance.siteregister_set.create(**data)
#
