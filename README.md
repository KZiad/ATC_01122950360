# Ehgz
Ehgz is a full-stack event booking system that allows users to browse and book
events, manage their bookings, and provide an integrated web-based admin panel for event
management.

<h1>Deployment</h1>

Ehgz is deployed on 2 services:
- Render: for the Django Rest Framework backend + Postgres database.
- Vercel: for the Vue.js frontend

<h2> Links </h2>

Frontend: https://ehgz.vercel.app/

Backend: https://ehgz-api.onrender.com/docs
<h1>How to run</h1>
Ehgz uses a Django Rest Framework backend and a Vue.js frontend

<h2>Backend</h2>
What You need:

- Docker (linux containers)
- makefile support

To get started, do ```make up``` in the ```ehgz_backend``` directory. This will build the docker image and run the container.
- To run the migrations, do ```make migrate```
- To create a superuser, do ```make createsuperuser```

<h2> Frontend </h2>
The frontend uses Vue.js for development. To get started, do the following:

- Install Node.js and npm
- Install Vue CLI globally using npm: ```npm install -g @vue/cli```
- Install the dependencies: ```npm install```
- Run the development server: ```npm run serve```
OR
- Build the website: ```npm run serve```

