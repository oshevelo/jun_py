from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    """ Client account """
    name = models.CharField(
        max_length=100
    )

    description = models.CharField(
        max_length=100,
        null=True, blank=True
    )

    external_id = models.CharField(
        verbose_name="external ID",
        max_length=100,
        null=True, blank=True
    )

    # managers
    MANAGER_FIELDS = ['delivery_director', 'assistant', 'account_owner']

    delivery_director = models.ForeignKey(
        verbose_name="delivery director",
        to=User, related_name="accounts_where_dd",
        null=True, blank=True, on_delete=models.SET_NULL
    )
    assistant = models.ForeignKey(
        verbose_name="assistant",
        to=User, related_name="accounts_where_assistant",
        null=True, blank=True, on_delete=models.SET_NULL
    )
    account_owner = models.ForeignKey(
        verbose_name="account owner",
        to=User, related_name="accounts_where_owner",
        null=True, blank=True, on_delete=models.SET_NULL
    )

    account_staff = models.ManyToManyField(
        verbose_name='account_staff',
        to=User, related_name='accounts'
    )

    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"
        ordering = ['name', 'id']
