from django.db import models

class Query(models.Model):
    sql_query = models.TextField()
    executed_at = models.DateTimeField(auto_now_add=True)
