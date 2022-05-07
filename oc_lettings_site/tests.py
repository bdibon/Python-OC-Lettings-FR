from pytest_django.asserts import assertContains, assertTemplateUsed
from django.urls import reverse


def test_homepage_view(client):
    homepage_url = reverse("site:index")
    response = client.get(homepage_url)

    assertContains(response, "<title>%s</title>" % "Holiday Homes", status_code=200)
    assertTemplateUsed(response, "index.html")
