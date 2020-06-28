
# 根据模型名称获取模型
from django.apps import apps

from datetime import datetime

# from app.event.models import Event


# 在模型调用的时候不行，这个是通过模型找本模型，所以需要调整在本类里写，也可能是自己不会用
def get_request_id(app_name, model_name):
    dt = datetime.now()
    num_str = '000000'

    # 根据名字获取模型
    model_obj = apps.get_model(app_name, model_name)
    id_str = str(model_obj.objects.first().id + 1)
    str_id = num_str[len(id_str):] + id_str
    return "Eve{y}{m}{d}{str_id}".format(y=dt.strftime('%Y'), m=dt.strftime('%m'), d=dt.strftime('%d'), str_id=str_id)


# 根据传入的模型，判断获取那个模型的最后一个id
# def by_model_name_get_request_id(model_name):
#     dt = datetime.now()
#     num_str = '000000'
#
#     # 根据名字判断对应的模型
#     if model_name == 'Event':
#         id_str = str(Event.objects.first().id + 1)
#     str_id = num_str[len(id_str):] + id_str
#     return "Eve{y}{m}{d}{str_id}".format(y=dt.strftime('%Y'), m=dt.strftime('%m'), d=dt.strftime('%d'), str_id=str_id)





