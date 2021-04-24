from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'commodity', views.CommodityViewSet)
router.register(r'chemical', views.ChemicalViewSet)
router.register(r'chem-composition', views.ChemCompViewSet)