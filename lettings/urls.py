from django.urls import path

import views


urlpatterns = [
    path('/', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
