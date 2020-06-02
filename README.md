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
        
### 4. Create models - Category, Tag, and Post

    1. Git status
        modified:   blog/admin.py
        new file:   blog/migrations/0001_initial.py
        modified:   blog/models.py
       
       
### 5. Install Django Debug Toolbar (Part 1/2)

    1. Register * models to admin.py
    2. Install django-debug-toolbar
       (link: pypi.org)
       (link: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
    3. Follow the instructions
    4. Test it out - runserver
    5. Git status
        modified:   README.md
        modified:   blog/admin.py
        modified:   config/settings.py
        modified:   config/urls.py

### 5. Install Django Ckeditor (Part 2/2)

    1. Go to pypi.org - pip install django-ckeditor
    2. Register ckeditor to Install App
    3. Run - python manage.py collectstatic
    4. Add it to settings - CKEDITOR_UPLOAD_PATH = "uploads/"
    5. Add it to config ulrs - url(r'^ckeditor/', include('ckeditor_uploader.urls')),     
    6. Add CKEDITOR_CONFIGS = [ ... ] to settings.py 
    7. Git status
        modified:   README.md
        modified:   blog/admin.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   media/photos/2020/06/01/post-image2.jpg
        new file:   media/uploads/2020/06/01/post-image1.jpg
        new file:   media/uploads/2020/06/01/post-image4.jpg

### 6. Admin settings
    
    1. Added these lines of code to blob/admin.py 
        list_display = ('id', 'title', 'category', 'created_at', 'get_photo')
        list_display_links = ('id', 'title')
        search_fields = ('title',)
        list_filter = ('category',)
        readonly_fields = ('views', 'created_at', 'get_photo')
        fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')
    2. Git status
        modified:   README.md
        modified:   blog/__pycache__/admin.cpython-37.pyc
        modified:   blog/__pycache__/models.cpython-37.pyc
        modified:   blog/admin.py
        modified:   blog/models.py
        
 ### 7. Menu Template Tag
 
    1. Create include dir for footer and header 
       - templates/inc/_header.html
       - templates/inc/_footer.html
    2. Move header and footer to inc from base.html
    3. Use include {% include 'inc/_header.html' %} and for footer as well
    4. Add link to home - <li><a href="{% url 'home' %}">Home</a></li>
    5. In blog/views.py create this - 
        def get_category(request, slug):
            return render(request, 'blog/category.html')    
    6. In blog/urls.py create this -
        path('category/<str:slug>', get_category, name='category'),
    7. In blog/models.py create this -
        from django.urls import reverse
            def get_absolute_url(self):
                return reverse('category', kwargs={'slug': self.slug}) 
    8. Create templatetags -
        blog/templatetags
        blog/templatetags/__init__.py
        blog/templatetags/menu.py
    9. In blog/templates create -
        /menu_tpl.html
    10. In templatetags/menu.py add this -
        # blog/templatetags/menu.py
        from django import template
        from blog.models import Category
        
        register = template.Library()
        
        @register.inclusion_tag('blog/menu_tpl.html')
        def show_menu(menu_class='menu'):
            categories = Category.objects.all()
            return {'categories': categories, 'menu_class': menu_class}
    11. In templates/inc/_header.html do this -
            {% load menu %}
            <header class="header">
               <div class="container">
                  <div class="row">
                     <div class="col-md-2">
                        <div class="logo">
                           <h2><a href="#">Classic</a></h2>
                        </div>
                     </div>
                     <div class="col-md-10">
                        {% show_menu %}
                     </div>
                  </div>
               </div>
            </header>       
            
    12. In templates/inc/_footer.html to this -
        {% load menu %}
        <footer class="footer">
           <div class="container">
              <div class="row">
                 <div class="col-md-12">
                    <div class="footer-bg">
                       <div class="row">
                          <div class="col-md-9">
                             {% show_menu 'footer-menu' %}
                             <!-- <div class="footer-menu">
                                <ul>
                                   <li class="active"><a href="#">Home</a></li>
                                   <li><a href="#">lifestyle</a></li>
                                   <li><a href="#">Food</a></li>
                                   <li><a href="#">Nature</a></li>
                                   <li><a href="#">photography</a></li>
                                </ul>
                             </div> -->
                          </div>
                          <div class="col-md-3">
                             <div class="footer-icon">
                                <p><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a><a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a><a href="#"><i class="fa fa-dribbble" aria-hidden="true"></i></a></p>
                             </div>
                          </div>
                       </div> .
                    </div>
                 </div>
              </div>
           </div>
        </footer>      
    13. Git status
        modified:   README.md
        modified:   blog/models.py
        new file:   blog/templates/blog/category.html
        new file:   blog/templates/blog/menu_tpl.html
        new file:   blog/templatetags/__init__.py
        new file:   blog/templatetags/menu.py
        modified:   blog/urls.py
        modified:   blog/views.py
        modified:   config/settings.py
        new file:   django_cache/be7c5c70635fbc5edcce3cd5bc69af35.djcache
        new file:   django_cache/c7992ab6d96eef92fdffdac20b764b53.djcache
        modified:   templates/base.html
        new file:   templates/inc/_footer.html
        new file:   templates/inc/_header.html
                 
### 8. Highlighting an active menu item

    1. Open config/static/js/active.js and add this -
        $(document).ready(function () {
    
            $('.menu a').each(function(){
                let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
                let link = this.href;
                if(location == link){
                    $(this).parent().addClass('active');
                }
            });
            
            ...
        }  
    2. Git status
        modified:   README.md
        modified:   blog/__pycache__/urls.cpython-37.pyc
        modified:   blog/urls.py
        modified:   django_cache/be7c5c70635fbc5edcce3cd5bc69af35.djcache
        modified:   django_cache/c7992ab6d96eef92fdffdac20b764b53.djcache
        modified:   templates/inc/_header.html
      


        
              
