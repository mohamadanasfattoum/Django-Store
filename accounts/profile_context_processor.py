from .models import Profile


def get_accounts_data(request):
    accounts_data = Profile.objects.get(user=request.user)
    return {'accounts_data':accounts_data }




