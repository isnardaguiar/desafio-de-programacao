from django.shortcuts import render
from .models  import SalesData
from django.http import HttpResponse
from application.utils import format_currency
import csv
import io

# Create your views here.
def hello_world(request, *args, **kwargs):

    return HttpResponse("Hello World")


def upload_file(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            total_revenue = 0
            file_data = _process_file(request.FILES['file'].read())

            for data in file_data:   
                sale_data = SalesData(
                    purchaser_name=data['purchaser_name'],
                    item_description=data['item_description'],
                    item_price=data['item_price'],
                    purchase_count=data['purchase_count'],
                    merchant_address=data['merchant_address'],
                    merchant_name=data['merchant_name'],
                )
                sale_data.save()

                total_revenue += sale_data.item_price * sale_data.purchase_count
            
            
            context = {
                'total_revenue': format_currency(total_revenue, value_format='decimal'),
                'file_data': file_data,
            }
            return render(request, 'sales/pages/result.html', context=context)

        return render(request, 'sales/pages/upload.html')
    

    except Exception as e:
        print(e)
        return render(request, 'sales/pages/upload.html', context={'error_message': str(e)}, status=400)



def _process_file(file_content):
    
    data = io.TextIOWrapper(io.BytesIO(file_content), encoding='utf-8')

    reader = csv.DictReader(data, delimiter='\t')
    file_data = []

    for row in reader:

        row_data = {
            'purchaser_name': row['purchaser name'],
            'item_description': row['item description'],
            'item_price': float(row['item price'].replace('R$', '').strip()),
            'purchase_count': int(row['purchase count']),
            'merchant_address': row['merchant address'],
            'merchant_name': row['merchant name'],
        }
        file_data.append(row_data)

    return file_data

