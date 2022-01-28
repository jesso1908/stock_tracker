
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.StockPicker,name="stockpicker"),
    path('stocktracker/',views.StockTracker,name='stocktracker')
]