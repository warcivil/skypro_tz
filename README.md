# skypro_tz
**ВНИМАНИЕ!**

**для удобства тестирования env.example лежат данные которые надо просто вставить в .env**

Для запуска проекта перенесите из env.example в файл .env все переменные.
Далее запустите docker-compose.

docker-compose up --build -d

**при создании контейнеров автоматически генерируются данные для бд это сделано для упрощения проверки**

после создания контейнеров(должно создать 2 контейнера, web и postgres)
вы можете пользоваться сайтом по адресу http://127.0.0.1:8000/

по адресу http://127.0.0.1:8000/home/products/ - вы получите список продуктов.

по адресу http://127.0.0.1:8000/users/register/ - вы можете зарегестрироваться

по адресу http://127.0.0.1:8000/users/login/ - вы можете залогиниться

по адресу http://127.0.0.1:8000/users/logout/ - вы можете разлогиниться
