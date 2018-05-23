from django.urls import path

from hexia_pages import views

app_name = 'Hexia Pages'

urlpatterns = [
    path('<slug:slug>/', views.PageView.as_view(), name="page_view"),
]