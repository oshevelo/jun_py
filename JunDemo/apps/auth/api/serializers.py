from collections import OrderedDict
from django.shortcuts import get_object_or_404
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils import timezone
from rest_framework.serializers import ValidationError
from rest_framework import serializers
from rest_framework import status




