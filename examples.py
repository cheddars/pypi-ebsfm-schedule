from datetime import datetime, timedelta
from unittest import TestCase

from ebsfm import schedule

class TestEbsfm(TestCase):
    def test_today_ebsfm_schedule(self):
        df = schedule("RADIO")
        print(df)
        assert len(df) > 0


    def test_yesterday_ebsfm_schedule(self):
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        df = schedule("RADIO", yesterday.strftime("%Y%m%d"))
        print(df)
        assert len(df) > 0


    def test_today_iradio_schedule(self):
        df = schedule("IRADIO")
        print(df)
        assert len(df) > 0