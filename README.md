## BUILDING DJANGO BLOG BASED ON RUSSION COMPLETE DJANGO GUIDE COURSE

### 1. Create Django project and app

    0. Create root dir - src
    1. Create virtualnenv
    2. Install django
    3. Create django project - src/config
    4. Create django app - src/blog
    5. Register app
    6. Run server
    7. Create local repository
    8. Git satus
        new file:   blog/admin.py
        new file:   blog/apps.py
        new file:   blog/models.py
        new file:   blog/tests.py
        new file:   blog/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        
### 2. Create Home page views
    1. Git satus
        modified:   README.md
        new file:   blog/urls.py
        modified:   blog/views.py
        modified:   config/urls.py

### 3. Add a template to the project

    0. Download blog template & unzipped it
    1. Create 'static' folder - config/static
    2. Add template assets to - config/static
    3. Test it out - python manage.py collectstatic 
       186 static files copied to 'J:\2020Projects\django3\RussianDjangoCompleteGuideBlog\dartblog\src\static'
    4. Git satus
        modified:   .gitignore
        modified:   README.md
        new file:   blog/templates/blog/index.html
        modified:   blog/views.py
        modified:   config/settings.py
        new file:   templates/base.html
   