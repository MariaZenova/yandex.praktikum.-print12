# Мария Зенова, 23-я когорта — Финальный проект. Инженер по тестированию плюс
# Проверка списка заказов на статус ответа 200 по треку заказа
import api_requests

def test_check_get_order_track_status_200():
	order_track = api_requests.create_order_request()
	assert order_track.status_code == 201 or order_track.status_code == 200
	get_order_by_track = api_requests.get_order_by_track_request(str(order_track.json()["track"]))
	assert get_order_by_track.status_code == 200