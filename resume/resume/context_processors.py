from django.contib.auth.models import User

def project_context(request):

    context = {
        'me': User.objects.first(),
    }

    return context