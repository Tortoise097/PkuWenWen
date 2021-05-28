from django.shortcuts import render

# Create your views here.
def vue_test(request):
    return render(request, 'myapp/vue-test.html')

def vue_test2(request):
    return render(request, 'myapp/vue-test2.html')