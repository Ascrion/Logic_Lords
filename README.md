### Branch Creation:
git checkout -b backender
git add .  
git commit -m "Basic Backend"  
git push -u origin backender

### Server Runtime:
i)To run: python manage.py runserver 192.168.159.174:8000  
ii)To stop: Ctrl + C  
iii) Superuser: http://192.168.159.174:8000/admin  
(Admin1,Password_Admin)

### Website Files:
html -> templates folder  
css,js -> static folder

### Verifying Migrations:  
python manage.py makemigrations
python manage.py migrate

