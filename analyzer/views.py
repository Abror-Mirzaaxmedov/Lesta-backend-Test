from django.shortcuts import render
from analyzer.forms import UploadFileForm
from analyzer.utils import calculate_tfidf

def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            text = request.FILES['file'].read().decode('utf-8')
            tfidf_data = calculate_tfidf(text)
            context['data'] = tfidf_data
    else:
        form = UploadFileForm()
    context['form'] = form
    return render(request, 'analyzer/upload.html', context)
