# Проект сайт магазина "Loft World"
________
В данном проекте представлен сайт продажи и изготовления мебели и прочих услуг в стиле "Loft"<br>
В проекте подключены:
1. Регистрация и авторизация пользователя;
3. Админ-панель для суперпользователя;
4. Фильтрация товаров по категориям;
5. Страничная пагинация;
6. Профиль пользователя с возможностью менять данные, добавления аватарки и отображение товаров корзины;
7. Возможность оставлять коментарии под товаром;
8. Возможность писать, редактировать, удалять отдельный отзыв в разделе отзывы.
9. Подключена отдельная админ панель, где администратор может добовлять сообщения для рассылки всем клиентам сайта, создавать рассылку с установкой даты и периодичнсть отправки, удалять клиентов
10. Есть форма с обратной связью, где клиент подписывается под рассылку всех акций скидок, новостей и т.д.

Данный проект написан не фрейморке Django, с подключением реляционной базы данных "PostgreSQL"<br>
Подключена БД "Redis", для работы с кешем сайта<br>
Ипользовалось вирутальное окружение ```venv```
В  проекте построенно 7 модель БД:
1. Таблица "category";
2. Таблица "Product" прямая связь с "category";
3. Таблица "Users" прямая связь с "category" и "products";
4. Таблица "recipient";
5. Таблица "mailingmessage";
6. Таблица "mailingsettings";
7. Таблица "mailingstatus".

Для запуска проекта необходимо сделать 
1. git clone репозитория
```
git@github.com:Meatdam/Loft_world.git
```
2. Установить виртуальное окружение ```venv```
```
python3 -m venv venv
```
3. Подключить виртуальное окружение
```
source venv/bin/activate
```
4. Создать базу данных в ```PgAdmin```, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'config' в константе (словаре) 'DATABASES'
5. Обязательно установить пакет со всеми зависимостями 
```
pip install -r requirements.txt
```
6. Создать файл .env в корне проекта и заполнить следующие данные:
```
SECRET_KEY=

DEBUG=

# db_settings
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

# email settings
EMAIL_HOST_USER_MAIL=
EMAIL_HOST_PASSWORD_MAIL=

ADMIN_EMAIL=

# cache settings
CACHE_ENABLED=
CACHES_BACKEND=
CACHES_LOCATION=
```

