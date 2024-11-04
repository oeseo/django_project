from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .forms import CustomUserCreationForm, PositionForm
from .models import CustomUser, Position
from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages


@login_required
def users_page(request):
    return render(request, 'users/users_list.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

@login_required
def users_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/users_list.html', {'users': users})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                dismissed_value = form.cleaned_data['dismissed'] == 'True'
                user.dismissed = dismissed_value
                user.set_password(form.cleaned_data['password1'])
                user.save()
                messages.success(request, 'Пользователь успешно добавлен.')
                return redirect('users_list')
            except Exception as e:
                messages.error(request, 'Произошла ошибка при добавлении пользователя.')
        else:
            messages.error(request, 'Форма содержит ошибки.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/add_user.html', {'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.user.id == user.id:
        messages.error(request, 'Вы не можете удалить себя.')
        return redirect('users_list')
    if request.method == 'POST':
        try:
            user.delete()
            messages.success(request, 'Пользователь успешно удалён.')
            return redirect('users_list')
        except Exception as e:
            messages.error(request, 'Произошла ошибка при удалении пользователя.')
    return render(request, 'users/delete_user_confirm.html', {'user': user})

@login_required
def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Должность успешно добавлена.')
                return redirect('positions_list')
            except Exception as e:
                messages.error(request, 'Произошла ошибка при добавлении должности.')
        else:
            messages.error(request, 'Форма содержит ошибки.')
    else:
        form = PositionForm()
    return render(request, 'users/add_position.html', {'form': form})

@login_required
def positions_list(request):
    positions = Position.objects.all()
    return render(request, 'users/positions_list.html', {'positions': positions})

@login_required
def delete_position(request, position_id):
    position = get_object_or_404(Position, id=position_id)
    if request.method == 'POST':
        try:
            position.delete()
            messages.success(request, 'Должность успешно удалена.')
            return redirect('positions_list')
        except Exception as e:
            messages.error(request, 'Произошла ошибка при удалении должности.')
    return render(request, 'users/delete_position_confirm.html', {'position': position})

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        dismissed = self.request.query_params.get('dismissed')
        if dismissed is not None:
            queryset = queryset.filter(dismissed=dismissed)
        return queryset

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
