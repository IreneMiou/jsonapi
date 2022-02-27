from rest_framework_json_api import serializers
from quotes.models import Quotes


class QuotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quotes
        fields = ("quote", "category")
