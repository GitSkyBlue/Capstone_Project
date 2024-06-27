from django.shortcuts import render
from .models import JsonData
from polls.recognition import detectAndDisplay
from polls.recognition import getScreen
from django.http import JsonResponse
from django.http import StreamingHttpResponse

def my_view(request):
    return render(request, '1test.html')

def save_data(request):
    frame = getScreen()
    if frame is not None:
        d = detectAndDisplay(frame)
        if len(d) != 0:
            if not JsonData.objects.filter(data=d).exists():
                data = JsonData(data=d)
                data.save()

    return JsonResponse(d, safe=False)

def get_count(request):
    pk_list = JsonData.objects.values_list('pk', flat=True)
    
    pks = list(pk_list)

    return JsonResponse(pks, safe=False)

def api_view(request, pk):
    # 데이터베이스에서 데이터를 가져옵니다.
    queryset = JsonData.objects.get(pk=pk)

    data = queryset.data
    # JsonResponse로 응답
    return JsonResponse(data, safe=False)