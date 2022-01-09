from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words = user_text.split()
	nw = len(words)
	reversed_text = user_text[::-1]
    
	return render(request, 'reverse.html', {'usertext':user_text, 'revtext':reversed_text, 'nw':nw})