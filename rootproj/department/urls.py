from rest_framework.routers import DefaultRouter
from .views import DeptViewSet,SubjectViewSet,StudentViewSet,HobbiesViewSet

api_router=DefaultRouter()
api_router.register('v1/dept',DeptViewSet)
api_router.register('v1/subject',SubjectViewSet)
api_router.register('v1/student',StudentViewSet)
api_router.register('v1/hobbies',HobbiesViewSet)

urlpatterns=api_router.urls