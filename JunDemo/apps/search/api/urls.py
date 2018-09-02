from django.conf.urls import url

from apps.search.api.views import AccountsList


urlpatterns = [
    url(r'^account/$',
        AccountsList.as_view(), name='api_profile_account_list')
]
