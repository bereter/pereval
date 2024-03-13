from django.contrib import admin
from django.urls import path
from pereval_data.views import PerevalCreateViewset, PerevalUpdateViewset, PerevalUserListViewset
from .yasg import url_yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submitData/', PerevalCreateViewset.as_view({'post': 'create'})),
    path('submitData/<int:pk>/', PerevalUpdateViewset.as_view({'put': 'update', 'get': 'retrieve', 'delete':
        'destroy'})),
    path('submitData/user__email=<str:email>/', PerevalUserListViewset.as_view()),
] + url_yasg
