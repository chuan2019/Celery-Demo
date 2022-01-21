# Demo #3: Scheduling Recurring Tasks using Celery Beat

To start the application, just need to run one command: `docker-compose up -d --build`

After the application is up and running, once every 10 seconds, a record about the weather
information in Los Angeles is inserted into the Postgres database. Every Monday morning at
7:30am, a record about the weather forecast in the city of Lomita (90717) is inserted into
the Postgres database.

To access the Flower web site monitoring the task queue, you can simply visit http://localhost:5555
on the machine you started the application.

Detailed explanation on how to schedule recurring tasks using Celery Beat is provided in this post: <a href="https://python.plainenglish.io/scheduling-jobs-2-using-celery-7464ca0aed6d">How to Schedule Recurring Jobs or Tasks Using Celery</a>.
