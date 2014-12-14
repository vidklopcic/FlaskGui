Desktop GUI with Flask
=============

This is template, which can be used for building user interfaces connected to python scripts or programs using HTML5.

Concept
------------
1. Python app is initialized.
2. Instance of app is passed to flask using app.config['app_name'] = python_instance
3. Flask development server is started on localhost:80
4. Your gui is opened in default browser or in embeded browser using other gui framework

In views.py you can specify what does specific url. It can return html gui or call python function. <br>For simple way of enablyng every function to be called using same url pattern see views.py -> /api

Dependencies
------------
- Flask - http://flask.pocoo.org/docs/0.10/installation/
