# Django Project Station
A Django application that allows a user to post a project he/she has created and get it reviewed by his/her peers. API endpoints are provided through DRF. Only logged in user can access the API endpoints.

![](https://github.com/steve-njuguna-k/Django-Awwwards-Clone/blob/master/Screenshots/Screenshot-1.PNG)
![](https://github.com/steve-njuguna-k/Django-Awwwards-Clone/blob/master/Screenshots/Screenshot-2.PNG)
![](https://github.com/steve-njuguna-k/Django-Awwwards-Clone/blob/master/Screenshots/Screenshot-3.PNG)

## Requirements
The user can perform the following functions:

- A user can view posted projects and their details
- A user can post a project to be rated/reviewed
- A user can rate/ review other users' projects
- A user can search for projects 
- A user can view projects overall score
- A user can view my profile page

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 3.9.6

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/steve-njuguna-k/Django-Awwwards-Clone.git
```
2. cd into Django-Awwwards-Clone
```
cd Django-Awwwards-Clone
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please find me on [LinkedIn](https://www.linkedin.com/in/steve-njuguna-aa426096/)

© 2022 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
