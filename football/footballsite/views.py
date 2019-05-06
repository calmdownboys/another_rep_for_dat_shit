from django.shortcuts import render
def post_list(request):
    return render(request, 'footballsite/post_list.html', {})