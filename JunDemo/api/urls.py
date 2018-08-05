from django.conf.urls import url, include

urlpatterns = [
    # Auth
    url(r'^auth/',
    include('apps.auth.api.urls')),

]
