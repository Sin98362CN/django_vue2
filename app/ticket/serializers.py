from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        # fields = ['id', 'title', 'open_time', 'description', 'assigner_group', 'assigner',
        #           'approver_group', 'approver', 'state', 'last_reviser', 'create_time', 'modify_time', 'uuid',
        #           'request_id']
        fields = '__all__'


class EventSerializerDept(serializers.ModelSerializer):

    class Meta:
        model = Event
        # fields = ['id', 'title', 'open_time', 'description', 'assigner_group', 'assigner',
        #            'approver_group', 'approver', 'state', 'last_reviser', 'create_time', 'modify_time', 'uuid',
        #           'request_id']
        fields = '__all__'
        depth = 2



