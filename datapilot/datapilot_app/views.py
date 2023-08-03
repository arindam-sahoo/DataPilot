import os
import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from .utils import assign_database

def create_connection(database_path):
    try:
        conn = sqlite3.connect(database_path)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        if query.strip().split()[0].upper() == "DESC":
            table_name = query.strip().split()[1][:-1]
            query = f"PRAGMA table_info({table_name});"
        cursor.execute(query)
        connection.commit()  # Commit the changes made to the database
        return cursor
    except sqlite3.Error as e:
        print(e)
        return None

@login_required
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            sql_query = request.POST['sql_query']
            database_name = assign_database(request.user)
            database_path = os.path.join(settings.BASE_DIR, "user_databases", database_name)

            try:
                conn = create_connection(database_path)
                cursor = execute_query(conn, sql_query)
                if cursor is not None:
                    rows = cursor.fetchall()
                else:
                    rows = []
            except sqlite3.Error as e:
                error_message = str(e)
                return render(request, 'datapilot_app/home.html', {'error_message': error_message})

            conn.close()
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