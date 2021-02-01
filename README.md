## A kickstarter to Django framework

# This is entirely performed on windows

Go with using command prompt, which will be easy when moving to server 

Open command prompt in your desired folder, then follow the steps. 

1. Create a Directory 
 command - mkdir dirname
2. Check whether you have your python installed
 command - py
3. To get out of the python interpreter
 command - exit()
4. Install virtual environment 
 command - pip install virtual environment 
5. Activate the virtual environment 
 command - myenv\Scripts\activate 
6. Cross check whether the virtual environment is created, go into the directory click on myenv you will find four folders (Include, Lib, Scripts, tcl) and a txt file
7. Install Django
 command - pip install django 
8. view all the commands available in django 
 command - python -m django 
9. To start a new project 
 command - - python -m django startaproject projectname
10. To run it, we have to get in our project 
 command - cd projectname  
11. Create an app inside the project
 command - python manage.py startapp firstapp (make sure you are creating this inside the the project)
12. Let's make our project live
 command - python manage.py r-unserver
