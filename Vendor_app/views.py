from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vendor
from .models import PurchaseOrder
from .models import HistoricalPerformance
import json


@csrf_exempt
def create_vendor(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        try:
            data = json.loads(request.body)
            print(data)
            name = data.get('name')
            contact_details = data.get('contact_details')
            address = data.get('address')
            vendor_code = data.get('vender_code')
            on_time_delivery_rate = data.get('on_time_delivery_rate')
            quality_rating_avg = data.get('quality_rating_avg')
            average_response_time = data.get('average_response_time')
            fulfillment_rate = data.get('fulfillment_rate')


            vendor = Vendor.objects.create(
                name=name,
                contact_details=contact_details,
                address=address,
                vendor_code=vendor_code,
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                average_response_time=average_response_time,
                fulfillment_rate=fulfillment_rate
            )

            return JsonResponse({'message': 'vendor created successfully', 'vendor_id': vendor.id}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data. Required fields are missing.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_vendors(request):
    if request.method == 'GET':
        try:
            vendors = Vendor.objects.all()
            data = [{'name': vendor.name, 'vendor_code': vendor.vendor_code} for vendor in vendors]
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)    
    
@csrf_exempt
def get_vendor_by_id(request):
    if request.method == 'GET':
        try:
            params = request.GET
            vendor_id= params.get('id')
            vendor = Vendor.objects.get(id=vendor_id)
            data = {
                'name': vendor.name,
                'contact_details': vendor.contact_details,
                'address': vendor.address,
                'vendor_code': vendor.vendor_code,
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate
            }
            return JsonResponse(data)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
@csrf_exempt
def update_vendor_by_id(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            vendor_id = data.get('id')
            vendor = Vendor.objects.get(id=vendor_id)
            vendor.name = data.get('name', vendor.name)
            vendor.contact_details = data.get('contact_details', vendor.contact_details)
            vendor.address = data.get('address', vendor.address)
            vendor.vendor_code = data.get('vendor_code', vendor.vendor_code)
            vendor.on_time_delivery_rate = data.get('on_time_delivery_rate', vendor.on_time_delivery_rate)
            vendor.quality_rating_avg = data.get('quality_rating_avg', vendor.quality_rating_avg)
            vendor.average_response_time = data.get('average_response_time', vendor.average_response_time)
            vendor.fulfillment_rate = data.get('fulfillment_rate', vendor.fulfillment_rate)
            vendor.save()
            return JsonResponse({'message': 'Vendor updated successfully'})
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor does not exist'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Invalid data. Required fields are missing.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
@csrf_exempt
def delete_vendor_by_id(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            vendor_id = data.get('id')
            vendor = Vendor.objects.get(id=vendor_id)
            vendor.delete()
            return JsonResponse({'message': 'Vendor deleted successfully'})
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    

@csrf_exempt
def create_purchase_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            po_number = data.get('po_number')
            vendor_name = data.get('vendor_name')
            order_date = data.get('order_date')
            delivery_date = data.get('delivery_date')
            items = data.get('items')
            quantity = data.get('quantity')
            status = data.get('status')
            quality_rating = data.get('quality_rating')
            issue_date = data.get('issue_date')
            acknowledgment_date = data.get('acknowledgment_date')

            purchase_order = PurchaseOrder.objects.create(
                po_number=po_number,
                vendor_name=vendor_name,
                order_date=order_date,
                delivery_date=delivery_date,
                items=items,
                quantity=quantity,
                status=status,
                quality_rating=quality_rating,
                issue_date=issue_date,
                acknowledgment_date=acknowledgment_date
            )

            return JsonResponse({'message': 'Purchase order created successfully', 'po_id': purchase_order.id}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data. Required fields are missing.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_purchase_order_all(request):
    if request.method == 'GET':
        try:
            vendor_name = request.GET.get('vendor_name')

            if vendor_name:
                purchase_orders = PurchaseOrder.objects.filter(vendor_name__icontains=vendor_name)
            else:
                purchase_orders = PurchaseOrder.objects.all()

            data = [{'po_number': po.po_number, 'vendor_name': po.vendor_name} for po in purchase_orders]

            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_purchase_order_id_detail(request):
    if request.method == 'GET':
        try:
            params = request.GET
            po_id = params.get('id')
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            data = {
                'po_number': purchase_order.po_number,
                'vendor_name': purchase_order.vendor_name,
                'order_date': purchase_order.order_date,
                'delivery_date': purchase_order.delivery_date,
                'items': purchase_order.items,
                'quantity': purchase_order.quantity,
                'status': purchase_order.status,
                'quality_rating': purchase_order.quality_rating,
                'issue_date': purchase_order.issue_date,
                'acknowledgment_date': purchase_order.acknowledgment_date
            }
            return JsonResponse(data)
        except PurchaseOrder.DoesNotExist:
            return JsonResponse({'error': 'Purchase order does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_purchase_order_update(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            po_id = data.get('id')
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.po_number = data.get('po_number', purchase_order.po_number)
            purchase_order.vendor_name = data.get('vendor_name', purchase_order.vendor_name)
            purchase_order.order_date = data.get('order_date', purchase_order.order_date)
            purchase_order.delivery_date = data.get('delivery_date', purchase_order.delivery_date)
            purchase_order.items = data.get('items', purchase_order.items)
            purchase_order.quantity = data.get('quantity', purchase_order.quantity)
            purchase_order.status = data.get('status', purchase_order.status)
            purchase_order.quality_rating = data.get('quality_rating', purchase_order.quality_rating)
            purchase_order.issue_date = data.get('issue_date', purchase_order.issue_date)
            purchase_order.acknowledgment_date = data.get('acknowledgment_date', purchase_order.acknowledgment_date)
            purchase_order.save()
            return JsonResponse({'message': 'Purchase order updated successfully'})
        except PurchaseOrder.DoesNotExist:
            return JsonResponse({'error': 'Purchase order does not exist'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Invalid data. Required fields are missing.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    
@csrf_exempt
def get_purchase_order_delete(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            po_id = data.get('id')
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.delete()
            return JsonResponse({'message': 'Purchase order deleted successfully'})
        except PurchaseOrder.DoesNotExist:
            return JsonResponse({'error': 'Purchase order does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_vendor_performance(request):
    if request.method == 'GET':
        try:
            vendor_id = request.GET.get('id')
            vendor = Vendor.objects.get(id=vendor_id)
            
            performance = vendor.historicalperformance_set.all()
            data = [
                {
                    'date': p.date,
                    'on_time_delivery_rate': p.on_time_delivery_rate,
                    'quality_rating_avg': p.quality_rating_avg,
                    'average_response_time': p.average_response_time,
                    'fulfillment_rate': p.fulfillment_rate
                }
                for p in performance
            ]
            return JsonResponse(data, safe=False)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)