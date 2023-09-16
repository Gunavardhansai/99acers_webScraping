#create a new Django project
django-admin startproject property_scraper_project
##Create a Django App
-cd property_scraper_project
-python manage.py startapp property_scraper
##Django Settings
INSTALLED_APPS = [
    # ...
    'property_scraper',
    'crontab',
]
