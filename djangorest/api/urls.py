from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IngredientView,SizeView,ClientView,OrderView,OrderDetailView,MostPopularIngredientView
from django.urls import path

urlpatterns = {
    path('pizzeria/ingredients',IngredientView.as_view()),
    path('pizzeria/size',SizeView.as_view()),
    path('pizzeria/client',ClientView.as_view()),
    path('pizzeria/order/<int:order_id>',OrderDetailView.as_view()),
    path('pizzeria/orders',OrderView.as_view()),
    path('pizzeria/report',MostPopularIngredientView.as_view()),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)