from django.test import TestCase
from apps.logs_page.tasks import check_page_status
from apps.logs_page.models import SiteRegister
class TestTasks(TestCase):
    fixtures = [
        'apps/logs_page/fixtures/message_type.yaml',
        'apps/logs_page/fixtures/site_alert.yaml',

    ]

    def test_check_page_status(self):
        r = check_page_status()
        s = SiteRegister.objects.all()
        for r in s:
            print(r.page)
            print(r.is_alerted)


