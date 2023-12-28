from .models import Profile


def get_accounts_data(request):
    accounts_data = Profile.objects.last()
    return {'accounts_data':accounts_data }