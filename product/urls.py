from django.urls import path

from . import views

urlpatterns = [
    #path('products/', views.get_all_products),
    path("products", views.AlltProductList.as_view(), name="all-product"),
    path('latest-products/', views.LatestProductList.as_view()),
    path('products/<str:slug>/', views.get_single_product),
    path('<str:cat_slug>', views.get_category_products)
]
