from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from contracts.views import ContractViewSet, PortfolioViewSet

router = routers.DefaultRouter()
router.register(r'contracts', ContractViewSet)
router.register(r'portfolios', PortfolioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
