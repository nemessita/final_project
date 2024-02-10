from django.urls import path, include
from goods import views
# from .views import ProductDetailView

app_name = 'goods'

urlpatterns = [
    path('search/',views.catalog, name='search'),
    path('<slug:category_slug>/',views.catalog, name='index'),
    path('product/<slug:product_slug>/',views.product, name='product'),

    # path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product'),
]
