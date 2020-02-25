
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from apiclasses import views as hh
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#my heart my soul my happiness

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/',views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),


    path('login/', TokenObtainPairView.as_view(), name="api-login"),
    path('register/', hh.signup.as_view(), name="api-register"),
    path('list', hh.ClassroomList.as_view(), name="api-classroom-list"),
    path('list/<int:classroom_id>/', hh.ClassroomDetails.as_view(), name="api-classroom-detail"),
    path('apiclassrooms/<int:classroom_id>/cancel/', hh.CancelClassroom.as_view(), name="api-classroom-delete"),
    path('apiclassrooms/create/', hh.CreatClassroom.as_view(), name="api-classroom-create"),
    path('apiclassrooms/<int:classroom_id>/update/', hh.UpdateClassroom.as_view(), name="api-classroom-update"),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
