import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertTemplateUsed

from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    profiles_index_url = reverse("profiles:index")
    response = client.get(profiles_index_url)

    assertContains(response, b"<h1>Profiles</h1>", status_code=200)
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view(client):
    first_profile = Profile.objects.first()
    profiles_profile_url = reverse(
        "profiles:profile",
        kwargs={"username": first_profile.user.username}
    )
    response = client.get(profiles_profile_url)

    assertContains(response, "<title>%s</title>" % first_profile.user.username, status_code=200)
    assertTemplateUsed(response, "profiles/profile.html")
