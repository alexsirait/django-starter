from django.http import JsonResponse
from django.views import View
from django.db import connection
import json

class BarangView(View):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tbl_barang")
            rows = cursor.fetchall()
            result = []
            for row in rows:
                result.append({
                    'id': row[0],
                    'barang': row[1],
                    'harga': row[2]
                })
        return JsonResponse(result, safe=False)