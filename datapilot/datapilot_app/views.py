from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib.auth import logout
from .utils import assign_database

def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            sql_query = request.POST['sql_query']
            with connection.cursor() as cursor:
                try:
                    cursor.execute(sql_query)
                    rows = cursor.fetchall()
                except Exception as e:
                    error_message = str(e)
                    return render(request, 'datapilot_app/home.html', {'error_message': error_message})

            return render(request, 'datapilot_app/home.html', {'rows': rows, 'sql_query': sql_query})
        else:
            return redirect('account_login')

    return render(request, 'datapilot_app/home.html')

@login_required
def database_assignment(request):
    # Get the user object
    user = request.user

    # Assign a database to the user
    database_name = assign_database(user)

    return render(request, 'datapilot_app/database_assigned.html', {'database_name': database_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect('account_login')