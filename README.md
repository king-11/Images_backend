# Images_backend
- Authorization and Image Storage Backend
- Swagger UI Deployed at https://wallpaper-apiv1.herokuapp.com/
- Redoc docs for reference are at https://wallpaper-apiv1.herokuapp.com/docs/

[![GitHub issues](https://img.shields.io/github/issues/king-11/Images_backend?style=plastic)](https://github.com/king-11/Images_backend/issues)
[![GitHub license](https://img.shields.io/github/license/king-11/Images_backend?style=plastic)](https://github.com/king-11/Images_backend/blob/master/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/king-11/images_backend?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/king-11/images_backend?style=plastic)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/king-11/images_backend/djangorestframework?style=plastic)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/king-11/images_backend/drf-yasg?style=plastic)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/king-11/images_backend?style=plastic)
![Website](https://img.shields.io/website?down_color=lightgrey&up_color=orange&up_message=live&url=https%3A%2F%2Fwallpaper-apiv1.herokuapp.com%2F?style=plastic)

### About

This project allows artist from various fields to store their work securely as well as provide people with good material as the content is verified before its displayed to users by admin. Basic rest framework token authentication is enabled future goals are to create a frontend site  using nuxt js that will also include firebase authentication. It will enable anyone to see the content download it appreciate the owner by visiting their instagram handles and reading about them. As well a Teams page to showcase the team members.

### Packages used:
- [Django](https://pypi.org/project/Django/)
- [Django RestFramework](https://www.django-rest-framework.org/)
- [Django Heroku](https://pypi.org/project/django-heroku/)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [DRF Yasg](https://pypi.org/project/drf-yasg/)
- [WhiteNoise](https://pypi.org/project/whitenoise/)
- [Django Cors Header](https://pypi.org/project/django-cors-headers/)

### To deploy api locally follow below procedure :

- Install pipenv in your os `pip3 install pipenv`
- Go to the main folder and run `pipenv shell`
- perform migrations `python3 manage.py makemigrations`
- perform migrate `python3 manage.py migrate`
- run server `python3 manage.py runserver`

![logo](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimg.clipartlook.com%2Fcamera-lens-clipart-camera-lens-shutter-aperture-clip-art-lens-photo-photography-photos-pictures-900.jpg&f=1&nofb=1)
