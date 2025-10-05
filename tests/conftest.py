import pytest
from django.contrib.auth.models import User, Group
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
@pytest.fixture
def medecin(db):
    u = User.objects.create_user("dr","dr@example.com","dr")
    u.groups.add(Group.objects.get_or_create(name="Médecin")[0])
    return u
