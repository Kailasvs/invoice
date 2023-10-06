from rest_framework import serializers
from .models import *

class InvoiceDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = InvoiceDetails
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        
        # Create the Invoice instance
        invoice = Invoice.objects.create(**validated_data)
        
        # Create InvoiceDetails associated with the newly created invoice
        for detail_data in details_data:
            InvoiceDetails.objects.create(invoice_id=invoice, **detail_data)
        
        return invoice
    def update(self, instance, validated_data):
        details_data = validated_data.get('details')
        print(details_data,'deeeeeetails')
        # Update Invoice instance fields
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        print(details_data,'details updated')
        # Update or create associated details
        for detail_data in details_data:
            print(detail_data,'dataaaa')
            detail_id = detail_data.get('id', None)
           
            if detail_id:
                # Update existing detail
                detail = instance.details.get(pk=detail_id)
                detail.description = detail_data.get('description', detail.description)
                detail.quantity = detail_data.get('quantity', detail.quantity)
                detail.unit_price = detail_data.get('unit_price', detail.unit_price)
                detail.price = detail_data.get('price', detail.price)
                detail.save()
            else:
                print('else')
                # Create new detail print(instance,'insrnce')
                InvoiceDetails.objects.create(invoice_id=instance, **detail_data)
        
        return instance
