from django.urls import path
from django.views.decorators.cache import cache_page
from mailing.apps import MailingConfig
from mailing.views import (MainView, MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView,
                           MailingDeleteView, MessageCreateView, MessageListView, MessageUpdateView,
                           MessageDeleteView, ClientCreateView, ClientListView, ClientUpdateView,
                           ClientDeleteView, LogsListView)

app_name = MailingConfig.name

urlpatterns = [
    path('', cache_page(60)(MainView.as_view()), name='main'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/', MailingListView.as_view(), name='mailings'),
    path('mailing/detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('logs/', LogsListView.as_view(), name='logs'),
]
