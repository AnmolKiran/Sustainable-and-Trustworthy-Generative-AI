from django.shortcuts import render
from django.http import JsonResponse
from .function import run_conversation

 




from django.http import JsonResponse
from .function import chat_function, search_function, trusted_sources_function, single_value_dashboard_function, chart_dashboard_function, news_dashboard_function, patents_search_function

def chat_view(request):
    # Get the user's message from the request, assuming it's in the GET parameters for simplicity
    message = request.GET.get('message', '')
    response = chat_function(message)
    return JsonResponse(response, safe=False)

def get_weather(request):
     response = run_conversation()
     return JsonResponse({"response": response})    

def search_view(request):
    query = request.GET.get('query', '')
    response = search_function(query)
    return JsonResponse(response, safe=False)

def trusted_sources_view(request):
    topic = request.GET.get('topic', '')
    response = trusted_sources_function(topic)
    return JsonResponse(response, safe=False)

def single_value_dashboard_view(request):
    metric = request.GET.get('metric', '')
    response = single_value_dashboard_function(metric)
    return JsonResponse(response, safe=False)

def chart_dashboard_view(request):
    chart_type = request.GET.get('chart_type', '')
    data = request.GET.get('data', '')
    response = chart_dashboard_function(chart_type, data)
    return JsonResponse(response, safe=False)

def news_dashboard_view(request):
    response = news_dashboard_function()
    return JsonResponse(response, safe=False)

def patents_search_view(request):
    query = request.GET.get('query', '')
    response = patents_search_function(query)
    return JsonResponse(response, safe=False)

def myweather_view(request):
    location = request.GET.get('location', '')
    unit = request.GET.get('unit', 'fahrenheit')  # Default unit is Fahrenheit
    response = myweather_function(location, unit)
    return JsonResponse(response, safe=False)

