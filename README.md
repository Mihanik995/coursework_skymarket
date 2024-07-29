# Skystore

Данная работа представляет собой сайт объявлений.

Frontend-часть уже была готова.

Бэкенд-часть проекта предполагала реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

Список доступных эндпоинтов: localhost:8000/swagger/

Для запуска через Docker необходимо не устанавливать параметр DEBUG в переменных окружения.
Для запуска бекэнда на локальной машине необходимо установить параметр DEBUG в любое ненулевое значение.

Для наполнения бекэнда тестовыми данными есть команда **python manage.py filldatabase** 