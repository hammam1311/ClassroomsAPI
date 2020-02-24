
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView

from classes import views
from classes_api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    # API Endpoints
    path('api/classrooms/', api_views.ClassroomListAPIView.as_view(), name='api-classroom-list'),
    path('api/classrooms/<int:classroom_id>/', api_views.ClassroomDetailAPIView.as_view(), name='api-classroom-detail'),
    path('api/classrooms/create/', api_views.ClassroomCreateAPIView.as_view(), name='api-classroom-create'),
    path('api/classrooms/<int:classroom_id>/update/', api_views.ClassroomUpdateView.as_view(), name='api-classroom-update'),
    path('api/classrooms/<int:classroom_id>/delete/', api_views.ClassroomDeleteView.as_view(), name='api-classroom-delete'),

    path('login/', TokenObtainPairView.as_view(), name="api-login"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
