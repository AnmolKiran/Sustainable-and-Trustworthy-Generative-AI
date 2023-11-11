from django.urls import path
from .views import get_weather
from .views import chat_view, search_view, trusted_sources_view, single_value_dashboard_view, chart_dashboard_view, news_dashboard_view, patents_search_view, myweather_view


urlpatterns = [
    path('get_weather/', get_weather, name='get_weather'),
    path('myweather/', get_weather, name='myweather'),
    path('chat/', chat_view, name='chat_function'),
    path('search/', search_view, name='search_function'),
    path('trusted_sources/', trusted_sources_view, name='trusted_sources_function'),
    path('single_value_dashboard/', single_value_dashboard_view, name='single_value_dashboard_function'),
    path('chart_dashboard/', chart_dashboard_view, name='chart_dashboard_function'),
    path('news_dashboard/', news_dashboard_view, name='news_dashboard_function'),
    path('patents_search/', patents_search_view, name='patents_search_function'),

]




