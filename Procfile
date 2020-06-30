release: python3 managey.py makemigrations --no-input
release: python3 manage.py migrate --no-input

web: gunicorn wallpaper.wsgi --log-file
