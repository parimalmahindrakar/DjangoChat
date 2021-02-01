from django.shortcuts import render
from django.http import HttpResponse
from account.models import *

def index(request):
    return render(request, "DjangoChatApp/index.html")

def account_view(request, *args, **kwargs):

	context = {}
	user_id = kwargs.get("user_id")
	try:
		account = Account.objects.get(pk=user_id)
	except:
		return HttpResponse("Something went wrong.")
	if account:
		context['id'] = account.id
		context['username'] = account.username
		context['email'] = account.email
		context['profile_image'] = account.profile_image.url
		context['hide_email'] = account.hide_email

		# Define template variables
		is_self = True
		is_friend = False
		user = request.user
		if user.is_authenticated and user != account:
			is_self = False
		elif not user.is_authenticated:
			is_self = False

		# Set the template variables to the values
		context['is_self'] = is_self
		context['is_friend'] = is_friend
		context['BASE_URL'] = settings.BASE_URL
		return render(request, "DjangoChatApp/account.html", context)


def account_search_view(request, *args, **kwargs):
	context = {}
	if request.method == "GET":
		search_query = request.GET.get("q")
		if len(search_query) > 0:
			search_results = Account.objects.filter(email__icontains=search_query) | Account.objects.filter(username__icontains=search_query)
			search_results = search_results.distinct()
			accounts = []
			for account in search_results:
				accounts.append((account,False))
			context['accounts'] = accounts
	return render(request, "DjangoChatApp/search_results.html",context)

