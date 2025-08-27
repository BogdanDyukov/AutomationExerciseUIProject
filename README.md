# https://www.automationexercise.com/

pip install pytest-playwright pytest

pip install pydantic-settings 'pydantic[email]'

- models/ — схемы данных (классы).
- data/ — экземпляры моделей (объекты), которые используются в тестах
- test_data/ — “сырой” вспомогательный материал для тестов: файлы, картинки, csv, pdf и т.д., которые не являются моделями или объектами Python.

В директории common хранятся универсальные компоненты, который повторяются на разных страницах (но короче хлебные крошки могут быть как в навигации, так и в common)