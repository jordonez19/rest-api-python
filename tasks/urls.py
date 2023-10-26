from django.urls import path, include
from .views import TaskView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'tasks')


#api versioning
urlpatterns = [
    path('api/v1', include(router.urls)),
]
