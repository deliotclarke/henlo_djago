from django.urls import path
from henlo import views
from henlo.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # 5 limits results
    context_object_name="message_list",
    template_name="henlo/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("henlo/<name>", views.henlo_there, name="henlo_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]
