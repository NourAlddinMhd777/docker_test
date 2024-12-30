from django.http import JsonResponse
from rest_framework.views import status

def custom_404_view(request, exception):
    
    context  = "Page not found"
    
    status_code=status.HTTP_404_NOT_FOUND
    
    return JsonResponse(get_middleware_metadata(context), status=status_code)
    
def custom_500_view(request):
    
    context = "Internal Server Error"
    
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    
    return JsonResponse(get_middleware_metadata(context), status=status_code)
    
def custom_505_view(request):
    
    context  = "HTTP Version Not Supported"
    
    status_code=status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    
    return JsonResponse(get_middleware_metadata(context), status=status_code)

def custom_502_view(request):
    
    context  = "Bad Gateway"
    
    status_code=status.HTTP_502_BAD_GATEWAY
    
    return JsonResponse(get_middleware_metadata(context), status=status_code)

def get_middleware_metadata(content):
    return{
        "meta": {'errors': content},
        "data": ""
    }