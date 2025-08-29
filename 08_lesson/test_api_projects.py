import requests
import pytest

BASE_URL = 'https://ru.yougile.com/api-v2/'
API_KEY = "p5H7p9bR8N-WPBCwYxX9IDl6Kdpdx-gebNqBiw0KBDvn2Gvv0yQ1ntRn0dEWsBIs"  # Здесь укажите ваш реальный токен API


# Фикстура для общих заголовков авторизации
@pytest.fixture
def headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


# Фикстура для создания нового проекта перед каждым тестом
@pytest.fixture
def create_project(headers):
    data = {
        "title": "Тестовый проект",  # Название проекта
        "users": {
            "170f6025-0a44-4b0f-806d-c7088f00b11d": "admin"
            # Пример ID сотрудников
        }
    }
    response = requests.post(
        BASE_URL + 'projects',
        headers=headers,
        json=data
    )
    assert response.status_code == 201, \
        f"Failed to create project: {response.text}"
    return response.json()["id"]  # Возвращаем ID созданного проекта


# Тест успешного создания проекта
def test_create_project_positive(headers):
    data = {
        "title": "Новый тестовый проект",
        "users": {
            "f3d388f7-4c11-4903-9d08-10e09bfa57b7": "admin",
            # Пример ID сотрудников
        }
    }
    response = requests.post(
        BASE_URL + 'projects',
        headers=headers,
        json=data
    )
    print_response(response)  # Выводим ответ для отладки
    assert response.status_code == 201  # Проверяем, что статус успешен


# Тест неудачного создания проекта (например, пустое название)
def test_create_project_negative(headers):
    data = {
        "title": "",  # Пустое имя проекта должно привести к ошибке
        "users": {}
    }
    response = requests.post(
        BASE_URL + 'projects',
        headers=headers,
        json=data
    )
    print_response(response)  # Выводим ответ для отладки
    assert response.status_code == 400
    # Ожидаем ошибку 400 при отсутствии заголовка title


# Тест успешного обновления проекта
def test_update_project_positive(create_project, headers):
    project_id = create_project
    update_data = {
        "deleted": True,
        "title": "Обновленное название проекта",
        "users": {
            "f3d388f7-4c11-4903-9d08-10e09bfa57b7": "admin",
        }
    }

    response = requests.put(
        f"{BASE_URL}projects/{project_id}",
        headers=headers,
        json=update_data
    )
    print_response(response)  # Выводим ответ для отладки
    assert response.status_code == 200  # Ожидаем успешное обновление


# Тест неуспешного обновления несуществующего проекта
def test_update_project_negative_invalid_id(headers):
    invalid_id = "non_existent_project_id"  # Не существующий ID
    update_data = {
        "title": "Обновленное название проекта",
        "users": {}
    }

    response = requests.put(
        f"{BASE_URL}projects/{invalid_id}",
        headers=headers,
        json=update_data
    )
    print_response(response)  # Выводим ответ для отладки
    assert response.status_code == 404  # Ожидаем, что проект не найден


# Тест успешного получения проекта
def test_get_project_positive(create_project, headers):
    project_id = create_project
    response = requests.get(
        f"{BASE_URL}projects/{project_id}",
        headers=headers
    )
    print_response(response)  # Выводим ответ для отладки
    assert response.status_code == 200  # Ожидаем успешный ответ


# Тест попытки получить несуществующий проект
def test_get_project_negative(headers):
    project_id = "non_existent_project_id"
    response = requests.get(
        f"{BASE_URL}projects/{project_id}",
        headers=headers
    )
    print_response(response)  # Выводим ответ для отладки
    assert response.status_code == 404  # Ожидаем, что проект не найден


def print_response(response):
    print(f"Status Code: {response.status_code}")
    if response.content:
        print(f"Response JSON: {response.json()}")
    else:
        print("No content in response")


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
