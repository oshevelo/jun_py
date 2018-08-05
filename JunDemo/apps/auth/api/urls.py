from django.conf.urls import url

from apps.auth.api.views import FakeLogin
'''
LogoutView, UserSelfView, ForgotPasswordCreate, \
    ForgotPasswordDetails, PasswordResetRetrieve, FakeLogin
'''


urlpatterns = [
    #url(r'^self/$',
    #    UserSelfView.as_view(), name='api_user_self'),    
    url(r'^fake/$',  # WAAAARNINGGG! Remove before production deployment!
        FakeLogin.as_view(), name='api_auth_fake_login'),

    #url(r'^logout/$',
    #    LogoutView.as_view(), name='api_auth_logout'),

]
