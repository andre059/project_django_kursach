from mailing.services import send_mailing
from mailing.models import Mailing


def daily_tasks():
    mailings = Mailing.objects.filter(periodicity="DAILY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def weekly_tasks():
    mailings = Mailing.objects.filter(periodicity="WEEKLY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def monthly_tasks():
    mailings = Mailing.objects.filter(periodicity="MONTHLY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)
