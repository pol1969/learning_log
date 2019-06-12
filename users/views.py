from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
    """Завершает сеанс работы с приложением"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
