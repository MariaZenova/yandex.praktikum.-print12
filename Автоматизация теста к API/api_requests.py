import configuration
import requests
import data

# Выполнение запроса на создание заказа
def create_order_request():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.create_order)


# Поиск заказа по треку
def get_order_by_track_request(track):
    print(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track)
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track)