from django.urls import path
from . import views


urlpatterns  = [
  path('',views.home,name='home'),
  path('about',views.about,name='about'),
  path('subcategory/<str:pk>',views.subcategory,name='subcategory'),
  path('products/<str:pk>',views.products,name='products'),
  path('detailedview/<str:pk>',views.detailedview,name='detailedview'),
  path('awards/',views.awards,name='awards'),
]