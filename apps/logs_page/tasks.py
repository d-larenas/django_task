from config import celery_app
from django.utils import timezone
from apps.drf_api_logger.models import APILogsModel
import requests


@celery_app.task(name='test')
def test_db():
    print(f"hola mundo {timezone.now()}")


@celery_app.task(name='get_data_ip')
def get_data_ip():
    print(f"update ip {timezone.now()}")
    logs_ip = APILogsModel.objects.filter(client_ip_data__isnull=True)
    if not logs_ip.exists():
        print("empty")
        return
    url = "https://ip.guide/"
    for log_ip in logs_ip:
        try:
            ip = log_ip.client_ip_address
            url_get = f"{url}{ip}"
            print(url_get)
            response = requests.get(url_get)
            if response.status_code == 200:
                response_json = response.json()
                log_ip.client_ip_data = response_json
                log_ip.save()
        except Exception as err:
            print(err)

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
