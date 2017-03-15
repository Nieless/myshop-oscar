from django.http import HttpResponsePermanentRedirect

def url_redirect(request):
    return HttpResponsePermanentRedirect("/catalogue/")