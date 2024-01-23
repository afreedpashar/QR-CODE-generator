import qrcode as qr
img = qr.make("https://github.com/afreedpashar/API-s-in-django-restframework")
img.save("github_repo_api_django.png")

