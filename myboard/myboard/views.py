from django.shortcuts import render


def myhome(request):
    return render(request, 'myhome.html')


def reverse(request):
    user_text = request.GET['username']
    reverse_text = user_text[::-1]
    return render(request,
                  'reverse.html',
                  {'reverse_text': reverse_text}
                  )
