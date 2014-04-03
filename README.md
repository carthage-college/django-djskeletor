django-djskeletor
=================

Skeleton project for Django development

##Quick Start

1. copy settings_default.py to settings.py
2. copy wsgi_default.py to wsgi.py
3. customize those files to your needs.
4. add the wsgi parameters to apache2 configuration file
5. restart apache2

_Note:_ replace djskeletor with the name of _your_ project e.g. djmyproj

##Sample wsgi configuration for apache2

```
<Location /djskeletor>
WSGIProcessGroup djskeletor
WSGIApplicationGroup djskeletor
</Location>
WSGIDaemonProcess djskeletor user=www-data group=www-data processes=1 threads=5 
WSGIImportScript /d2/django_projects/djskeletor/wsgi process-group=djskeletor application-group=djskeletor
WSGIScriptAlias /djskeletor "/d2/django_projects/djskeletor/wsgi.py"
```

##Pro Tips

1. Take advantage of reuseable apps in the djtools project
2. Use the templates in the djskins project
