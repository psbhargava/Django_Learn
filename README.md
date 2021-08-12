# Django_Learn

Step-by-Step Flow :

1. django-admin startproject
2. python manage.py startapp testapp
3. templates --> testapp --> HTML files
4. statics --> css --> *.css
5. statics --> images --> *.jpg
6. settings.py
		add application
		add template folder path
		add static folder path
		add staticfiles_dirs path
7. models.py 
		class HydJob(modles.Model):
			field declartion
8. Check db connection -- python manage.py shell
9. python manage.py makemigrations	
10. python manage.py migrate
11. register the model to the admin inside admin.py
12. create super user	
13. Check in the admin interface whether our tables are reflecting or not
14. populate tables with required records
15. views.py
16. urls.py
17. python manage.py runserver

