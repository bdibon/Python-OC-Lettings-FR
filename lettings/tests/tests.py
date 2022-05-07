from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed

from lettings.models import Letting


@pytest.mark.django_db
def test_index_view(client):
    lettings_index_url = reverse("lettings:index")
    response = client.get(lettings_index_url)

    assertContains(response, b"<title>Lettings</title>", status_code=200)
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view(client):
    first_letting = Letting.objects.first()
    lettings_letting_url = reverse("lettings:letting", kwargs={"letting_id": first_letting.id})
    response = client.get(lettings_letting_url)

    assertContains(response, "<title>%s</title>" % first_letting.title, status_code=200)
    assertTemplateUsed(response, "lettings/letting.html")
