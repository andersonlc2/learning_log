from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """
    Registrar um novo usuário.
    """
    if request.method != 'POST':
        # Exibe um formulário em branco.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Loga o usuário e redireciona para homepage
            login(request, new_user)
            return redirect('learning_logs:index')

    # Em branco ou dados inválidos.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
