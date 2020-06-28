
from .models import State, Transition, Docket, FlowLog
from rest_framework import serializers


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class TransitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transition
        fields = '__all__'


class DocketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Docket
        fields = '__all__'


class FlowLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlowLog
        fields = '__all__'
        depth = 1


