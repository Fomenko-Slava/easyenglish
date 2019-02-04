Start project (localhost)
---------------------------------------
1. Make sure you run script nginx-overlay

2. Adding hosts 

    Add a few lines in file /etc/hosts:

    127.0.0.1 shop.loc
    127.0.0.1 shop.django.loc

3. Start project

    console$ docker-compose up
    
4. Create admin user. Get output "admin@admin.com created successfully"

    #console$ docker/create_superuser.sh  (in dev environment only.)
    выдаёт ошибку, по этому просто заходим в контейнер
    $ docker/bash.sh
    $ python manage.py createsuperuser - создаём админа
    

Иконки
https://fontawesome.com/icons