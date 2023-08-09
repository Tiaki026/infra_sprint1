Социальная сеть Kittygram
Описание
Kittygram — социальная сеть для обмена фотографиями любимых питомцев. Это полностью рабочий проект, который состоит из бэкенд-приложения на Django и фронтенд-приложения на React. В нем Вы можете разместить фото любимого котика и посмотретить фото котиков других пользователей. Регистрация обязательна.
Стек технологий
•	Python: Язык программирования
•	Django: Фреймворк для создания веб-приложений
•	Django Rest Framework: Расширение для Django, предоставляющее функциональность REST API
•	Ubuntu: Операционная система
•	JavaScript: Язык программирования для создания динамических веб-страниц
•	React: JavaScript-библиотека для создания пользовательских интерфейсов
•	Nginx: Веб-сервер и обратный прокси-сервер
•	Gunicorn: WSGI-сервер для запуска веб-приложений на Python
Как воспользоваться проектром
Клонирование проекта с GitHub на сервер
Настройка бэкенд-приложения
1.	Перейдите в директорию бэкенд-приложения проекта.
2.	Вместо <название_проекта> укажите название проекта, с которым работаете.
```
cd infra_sprint1/backend/
```
3.	Создайте виртуальное окружение.
```
python3 -m venv venv
```
4.	Активируйте виртуальное окружение.
```
source venv/bin/activate
```
5.	Установите зависимости.
```
pip install -r requirements.txt
```
Выполните миграции и создайте суперюзера из директории с файлом manage.py:
1.	Примените миграции.
python3 manage.py migrate
2.	Создайте суперпользователя.
```
python3 manage.py createsuperuser
```
Соберите статику бэкенд-приложения:
```
python3 manage.py collectstatic
```
```
sudo cp -r infra_sprint1/static_backend /var/www/kittygram
```
Настройка фронтенд-приложения
1.	Находясь в директории с фронтенд-приложением, установите зависимости для него:
```
npm i
```
2.	Из директории с фронтенд-приложением выполните команду:
```
npm run build
```
3.	Скопируйте статику фронтенд-приложения в директорию по умолчанию:
```
sudo cp -r infra_sprint1/frontend/build/. /var/www/kittygram/
```
настройка WSGI-сервера Gunicorn
Перейдите в директорию с файлом manage.py, и запустите Gunicorn:
```
gunicorn --bind 0.0.0.0:8000 backend.wsgi
```
Создайте файл конфигурации юнита systemd для Gunicorn в директории /etc/systemd/system/. Назовите его по шаблону gunicorn_название_проекта.service:
```
sudo nano /etc/systemd/system/gunicorn_kittygram.service
```
Команда sudo systemctl с параметрами start, stop или restart запустит, остановит или перезапустит Gunicorn. Например, вот команда запуска:
```
sudo systemctl start gunicorn_kittygram
```
Чтобы systemd следил за работой демона Gunicorn, запускал его при старте системы и при необходимости перезапускал, используйте команду:
```
sudo systemctl enable gunicorn_kittygram
```
настройка веб- и прокси-сервера Nginx
Запустите Nginx командой:
```
sudo systemctl start nginx
```
Обновите настройки Nginx. Для этого откройте файл конфигурации веб-сервера…
```
sudo nano /etc/nginx/sites-enabled/default
```
Сохраните изменения в файле, закройте его и проверьте на корректность:
```
sudo nginx -t
```
Перезагрузите конфигурацию Nginx
```
sudo systemctl reload nginx
```
Настройка файрвола ufw
Файрвол установит правило, по которому будут закрыты все порты, кроме тех, которые вы явно укажете. Настройка файрвола ufw Получение и настройка SSL-сертификата
1.	Активируйте разрешение принимать запросы только на порты 80, 443 и 22
```
sudo ufw allow 'Nginx Full'
```
```
sudo ufw allow OpenSSH
```
2.	Включите файрвол:
```
sudo ufw enable
```
В терминале выведется запрос на подтверждение операции. Введите y и нажмите Enter. 3. Проверьте работу файрвола:
```
sudo ufw status
```
Получение и настройка SSL-сертификата
1.	Находясь на сервере, установите certbot, если он ещё не установлен:
# Установка пакетного менеджера snap.
```
sudo apt install snapd
```
# Установка и обновление зависимостей для пакетного менеджера snap.
```
sudo snap install core; sudo snap refresh core
```
# Установка пакета certbot.
```
sudo snap install --classic certbot
```
# Обеспечение доступа к пакету для пользователя с правами администратора.
```
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
2.	Запустите certbot и получите SSL-сертификат. Для этого выполните команду:
```
sudo certbot --nginx
```
После этого certbot отправит ваши данные на сервер Let's Encrypt и там будет выпущен сертификат, который автоматически сохранится на вашем сервере в системной директории /etc/ssl/. Также будет автоматически изменена конфигурация Nginx: в файл /etc/nginx/sites-enbled/default добавятся новые настройки и будут прописаны пути к сертификату.
3.	Проверьте конфигурацию Nginx, и если всё в порядке, перезагрузите её.



