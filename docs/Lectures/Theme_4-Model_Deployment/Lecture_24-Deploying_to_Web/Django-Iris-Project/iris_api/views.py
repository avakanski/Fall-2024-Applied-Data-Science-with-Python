from django.shortcuts import render
from django.http import HttpResponse
from . import model

def index_view(request):
    return render(request, 'index.html')

def predict_class(request):
    try:
        slen = float(request.GET.get('slen'))
        swid = float(request.GET.get('swid'))
        plen = float(request.GET.get('plen'))
        pwid = float(request.GET.get('pwid'))

        # Get the output from the classification model
        variety = model.classify(slen, swid, plen, pwid)

        # Render the output in a new HTML page
        return render(request, 'output.html', {'variety': variety})
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500) 