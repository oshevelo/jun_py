from django.conf import settings as django_settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View
import logging

logger = logging.getLogger(__name__)

class OAuth2View(View):

    def get(self, request):
        """
        Handles the redirect from ADFS to our site.
        We try to process the passed authorization code and login the user.

        Args:
            request (django.http.request.HttpRequest): A Django Request object
        """
        from django_auth_adfs.config import settings  # direct import fails if ADFS is not set up

        code = request.GET.get("code", None)

        user = authenticate(authorization_code=code)

        if user is not None:
            if user.is_active:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Redirect to the "after login" page.
                # Because we got redirected from ADFS, we can't know where the
                # user came from.
                #
                # We should implement mechanism to redirect user to the page
                # he visited being not authenticated...
                if settings.LOGIN_REDIRECT_URL:
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    return redirect(django_settings.LOGIN_REDIRECT_URL)
            else:
                # Return a 'disabled account' error message
                return HttpResponse(
                    "Account is disabled in Abiliton Metrics system.\n"
                    "Please contact AbilitonDashboardSupportMail@softserveinc.com for "
                    "more information.",
                    status=403
                )
        else:
            # Return an 'invalid login' error message
            logger.warning("Failed to authenticate user from ADFS code: {code}".format(code=code))
            return HttpResponse(
                "User is not registered in Abiliton Metrics system yet.\n"  
                "Please contact AbilitonDashboardSupportMail@softserveinc.com for "
                "more information or try again later.",
                status=401
            )
