# Basic Docker Flask Template

This project is a basic `Docker` (and `docker-compose`) Flask project that can be used as a base template.

This project has the following features:

* Bootstrap 4 frontend
* A single container hosting a Flask application
* Utilizes best practices including:
    * Flask application context
    * Flask logging and error handling
    * Flask Blueprints
    * Utilizes a base template inherited within all blueprints
    * Plus more!

> NOTE: This is docker-compose project with only one container

### Prerequisites

To use this project you must download Docker and docker-compose on your local system. You can find more information about how to do that [here](https://docs.docker.com/compose/install/).

### Installing

To get started you must first clone this repository to your local system.

```
git clone https://github.com/MSAdministrator/docker-flask-template.git
cd docker-flask-template
```

Once you have your repository on your system then you can run the following to rebuild and setup your containers:

```
docker-compose up --build --remove-orphans
```

### Structure

All sections of the website should be segmented into blueprints. Each `blueprint` should have the following structure:

```
📦home
 ┣ 📂templates
 ┃ ┗ 📂home
 ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┗ 📜thanks.html
 ┣ 📜__init__.py
 ┣ 📜forms.py
 ┗ 📜views.py
```

Not all modules (single .py files) may be needed. For example not every blueprint will have a `forms.py` or a `models.py` but each blueprint should have a `__init__.py`, a `views.py`, and a `template/{blueprint_name}` folder structure.

## Deployment

Currently there is `NO` production deployment docker-compose file.

## Built With

* [carcass](https://github.com/MSAdministrator/carcass) - Python packaging template

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* Josh Rickard - *Initial work* - [MSAdministrator](https://github.com/MSAdministrator)

See also the list of [contributors](https://github.com/MSAdministrator/attck_viz/contributors) who participated in this project.
