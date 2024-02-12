from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'upcleads', views.upc_lead.UPCLeadApiViewSet)
#router.register(prefix=r'upclead', basename='upclead', viewset=UPCLeadApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('hello', views.hello_world.test, name="hello")
]