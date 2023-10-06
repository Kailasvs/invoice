# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Invoice, InvoiceDetails
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer

# class InvoiceAPITestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         # Create some sample data for testing
#         self.invoice_data = {
#             "date": "2023-10-06",
#             "customer_name": "Customer 1"
#         }
#         self.invoice = Invoice.objects.create(**self.invoice_data)
#         self.invoice_details_data = [
#             {
#                 "description": "Item 1",
#                 "quantity": 5.0,
#                 "unit_price": 10.0,
#                 "price": 50.0,
#                 "invoice_id": self.invoice.id
#             },
#             {
#                 "description": "Item 2",
#                 "quantity": 3.0,
#                 "unit_price": 15.0,
#                 "price": 45.0,
#                 "invoice_id": self.invoice.id
#             }
#         ]

#     def test_create_invoice(self):
#         response = self.client.post('/invoices/invoices/', self.invoice_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Invoice.objects.count(), 2)  # Update based on your data

#     def test_retrieve_invoice(self):
#         response = self.client.get(f'/invoices/invoices/{self.invoice.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_invoice(self):
#         updated_data = {
#             "date": "2023-10-07",
#             "customer_name": "Updated Customer"
#         }
#         response = self.client.put(f'/invoices/invoices/{self.invoice.id}/', updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Invoice.objects.get(id=self.invoice.id).date, "2023-10-07")

#     def test_delete_invoice(self):
#         response = self.client.delete(f'/invoices/invoices/{self.invoice.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Invoice.objects.count(), 0)

#     def test_create_invoice_details(self):
#         response = self.client.post('/invoices/invoicedetails/', self.invoice_details_data[0], format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(InvoiceDetails.objects.count(), 2)  # Update based on your data

#     # Similar test methods for retrieving, updating, and deleting InvoiceDetails

#     def test_list_invoices(self):
#         response = self.client.get('/invoices/invoices/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)  # Update based on your data

#     # Add more test methods for listing InvoiceDetails, etc.

