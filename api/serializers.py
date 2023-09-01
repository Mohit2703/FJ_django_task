from rest_framework import serializers

from api.models import CreditCard, Payment, Order, EBTCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = [
            "id",
            "last_4",
            "brand",
            "exp_month",
            "exp_year",
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "order_total",
            "status",
            "success_date",
            # "ebt_total",
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "order", # The id of the associated Order object
            "amount",
            "description",
            "payment_method", # The id of the associated CreditCard object
            "status",
            "success_date",
            "last_processing_error"
        ]

# EBT Card Serializer
class EBTCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBTCard
        fields = [
            "id",
            "number",
            "last_4",
            "brand",
            "issue_state",
            "issue_month",
            "issue_year",
        ]