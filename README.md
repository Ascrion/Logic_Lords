### Branch Creation:
git checkout -b Backend  
git add .  
git commit -m "Basic Backend"  
git push -u origin Backend  

### Server Runtime:
i)To run: python manage.py runserver 192.168.161.163:8000  
ii)To stop: Ctrl + C  
iii) Superuser: http://192.168.161.163:8000/admin  
(Admin1,Password_Admin)

### Website Files:
html -> templates folder  
css,js -> static folder

Loading Methods:
{% load static %}
<link rel="stylesheet" href="{% static 'theme.css' %}">
href="{% url 'my_profile_page' %}"
add requests to urls.py and views.py of the app


