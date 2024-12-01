from django.urls import path
from .views import *

urlpatterns = [
    path('',home1_view,name='home1-page'),
    path('home2/',home2_view,name='home2-page'),

    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),

    path('project/<int:pk>/',PortfolioDetailView.as_view(),name='project-page'),

    path('blog/',BlogListView.as_view(),name='blog-page'),
    
    path('publication/<int:pk>/',BlogDetailView.as_view(),name='publication-page'),

    path('contact/',ContactFormView.as_view(),name='contact-page'),

    path('service/',service_view,name='service-page'),
    
    path('404/',error_view,name='error-page'),
]