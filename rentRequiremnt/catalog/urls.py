from django.conf.urls import url
from catalog import views
from catalog.views import ProductListView


urlpatterns = [
    # url('', views.index, name='index'),

    url('^$', views.index, name='index'),
    url(r'^products/', views.ProductListView.as_view(), name='products'),
     url(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^brands/', views.BrandListView.as_view(), name='brands'),
    url(r'brand/(?P<pk>\d+)$', views.BrandDetailView.as_view(), name='brand-detail'),

]
