from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .runner import predict

@csrf_exempt
def predict_view(request):
    text = request.body.decode("utf-8")
    return HttpResponse(predict(text))
