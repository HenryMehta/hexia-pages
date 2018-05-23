===========
Hexia Pages
===========

Hexia Pages is a simple Django app for create pages editable within Admin.  It is useful for things like
terms and conditions and privacy policy where you might want to edit the pages, don't need a full CMS
but don't want to be changing templates all the time.  

Detailed documentation is needs writing.

Quick start
-----------

1. pip install hexia-pages

2. Add "hexia_pages" and dependencies to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ckeditor',
        'ckeditor_uploader',
        'hexia_pages',
    ]

3. Include the hexia_pages URLconf in your project urls.py like this::

    path('pages/', include('hexia_pages.urls', namespace='hexia_pages')),

4. Run `python manage.py migrate` to create the hexia_pages models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a Page (you'll need the Admin app enabled).  Simple create a page with a unique slug.

6. Add a link to your template.

    <a href="{% url 'hexia_pages:page_view' object.slug %}">Link Text</a> provides the detail of a specific page. 
   Template: hexia_pages/page_detail.html

7. Visit http://127.0.0.1:8000/.
