# Pollen Measurement Web Application Repository

This repository contains the files and folders that are required to set up Pollen Measurement Application. There are multiple branches covering different steps of creation of the app. You can clone/download this repository and checkout the branch of interest.

# Application Description

Pollen Measurement is an easy to use application that allows user to input and store pollen count data. Each row of an input consists of pollen type, count and measurement location. Additionally application provides information of the date when the data was provided. This way user can keep track of the pollen count levels.

## Technologies

- Python version 3.10.1 - an interpreted high-level general-purpose programming language, used to create web application.
- Django version 4.0.1 - high-level Python web framework that encourages rapid development and clean, pragmatic design.
- Sqlite - default Django database, included in the Python itself.
- Bootstrap version 4 - an HTML, CSS & JS Library that focuses on simplifying the development of informative web pages.

# Requirements

- Installed Python
- Installed Django

# Users's guide

To start application, go into pollen_measurement_app folder, open system console and run python manage.py runserver command. Application is accessible under localhost:8000/measurement/.
To add new measurement press +Add New, then enter required information such as Pollen type, Pollen count, Measurement location. You can submit your measurement or go back to the list of all measurements without saving the current one. After submitting, the measurement will be visible in the list.
Measurement can be updated or deleted.

Views:

- list of all measurements

![Screenshot 2022-01-25 at 23 15 28](https://user-images.githubusercontent.com/33236011/151068871-bdba8299-b562-415d-ba05-277f1204d74d.png)



- creation of measurement

![Screenshot 2022-01-25 at 23 15 21](https://user-images.githubusercontent.com/33236011/151068874-95e22f36-464f-4ffa-a54b-e17aa184db43.png)


# Developer's guide

To start application run python manage.py runserver.
Application uses Sqlite database.
In case of any changes to the application db model run python manage.py makemigrations, and apply python manage.py migrate.

# Api documentation

All the endpoint are accessible under root path measurement/.
When running locally host and port became localhost:8000.
- (GET) host:port/measurement/list/ - lists all measurements
- (POST) host:port/measurement/ - insert new measurement
- (POST) host:port/measurement/measurementId/ - update existing measurement
- (POST) host:port/measurement/delete/measurementId/ - delete existing measurement

### Clone Repository

Clone the repository ([instructions can be found here](https://help.github.com/articles/cloning-a-repository/)). The files are copied to your local machine.

# License

This project is licensed under the MIT License. See the [LICENSE file](https://github.com/limak360/PollenMeasurement/blob/main/LICENSE).
