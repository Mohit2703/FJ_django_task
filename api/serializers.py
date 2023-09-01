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

        # constraints = [
        #     CheckConstraint(
        #         check = F("order_total") == F("ebt_total") + F("credit_total") and F("order_total") > F("ebt_total"),
        #         name="order_total_gte_ebt_total_plus_credit_total",
        #     )
        # ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "order", # The id of the associated Order object
            "amount",
            "description",
            "payment_method", # credit_card OR ebt_card 
            "credit_card", # The id of the associated CreditCard object
            "ebt_card", # The id of the associated EBTCard object
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