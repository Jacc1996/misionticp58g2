from django.urls import path
from django.urls.conf import include
#from django.urls.resolvers import URLPatterns

urlpatterns = [
    #path('user/<int:pk>/', UserDetailView.as_view()),
    path('', include('ecommerce_tienda.routers'))
]