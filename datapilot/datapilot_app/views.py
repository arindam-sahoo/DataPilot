from django.shortcuts import render, redirect
from django.db import connection

def home(request):
    if request.method == 'POST':
        sql_query = request.POST['sql_query']
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql_query)
                rows = cursor.fetchall()
            except Exception as e:
                error_message = str(e)
                return render(request, 'datapilot_app/home.html', {'error_message': error_message})

        return render(request, 'datapilot_app/home.html', {'rows': rows, 'sql_query': sql_query})
    return render(request, 'datapilot_app/home.html')
