from django.urls import path
from.import views
urlpatterns = [
    path('',views.Bhome,name="BlogHome"),
]