#!/bin/bash
docker exec -it shop_shop-django-server_1 bash -c "python /app/manage.py shell < /app/scripts/create_superuser.py"