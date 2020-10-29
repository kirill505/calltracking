# from connector import Connector
# from bqhandler import BQTableHanler
from comagichandler import ComagicHandler
from credfile import *

if __name__ == '__main__':
    """Функция принимает на вход event, context
    Подбробнее тут:
    https://cloud.google.com/functions/docs/writing/background#functions-writing-background-hello-pubsub-python"""

    #import base64
    #pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    #создает иcточник данных и место назначения данных
    comagic_handler = ComagicHandler(COMAGIC_LOGIN, COMAGIC_PASSWORD, FIRST_CALL_DATE, TOKEN)
    res = comagic_handler.get_call_legs_report('2020-09-01 00:00:00', '2020-09-01 23:59:59')
    print(res)
    # bq_handelr = BQTableHanler(full_table_id, google_credintials_key_path)
    #созздаем коннектор
    # connector = Connector(comagic_handler, bq_handelr)
    #обновляем данные в месте назначения
    # connector.update_dest_data()

