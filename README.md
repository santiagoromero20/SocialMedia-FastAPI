# Social Media Development

 The goal of this project was to develop a sort of "Twitter Toy" full-fledged API with the microservice **FastAPI**.
 This API imitates the main functionallities of any other Social Media. It has to hande with User registrations and Authentications, and enables it to perform different things such as uploading, deleting, liking or disliking a Post.
 
 ![Alt ](img/mamadera.jpeg "Title")
## **Motivation, Technologies and Teachings**

Well, the main Motivation was to learn the fundamentals of API design.

As the main teachings I should include importan concepts such as Decorators, Routes, the most use HTTPS Request Methods, such as Create, Read, Update and Delete (CRUD).

Also, about Databases. Starting from how to create classes or models, which under the hood will be playing the role of different tables on our Database. Basic **SQL** Language to handle querys, and even better, how to use ORM (Object Relational Mapper), **SQLAlchemy** in this case, to handle this querys and table creations. The importance of ForeignKeys to handle the relationship between Columns of different tables, Joins and so more. And finally, in relation with databases, the utility of Migration Tools, for this particular case the most well known, **Alembic**. The Database system chosen was **PostgresSQL**.

Moving on from the Databases, good practices about handling users regisratin and logins, such as hashing the passwords before store them on the database and the importance of JWT tokens to "keep track" of the Users.
About Schemas and how practical they are to "clearly" manage what data should enter and leave an specific request and how to integrate it to each particullary function of the different routes.

Finally, testing with pytest already integrated with TestClient (FastApi Class), and how to build out a **CI/CD pipeline** using **GitHub actions**.

All the app had been containerized using Docker, and the data recieved saved on cache with the use of the volume feature enabling the elimination of the Container. You can pull the image of the project on my [DockerHub](https://hub.docker.com/repository/docker/santiagoromero20/fastapi_api) , by the name of santiagoromero20/fastapi_api.

## **Project Structure**

      └── FASTAPI
            ├── alembic
            │    ├── env.py
            │    ├── script.py.mako
            │    ├── README.md
            │    └── versions
            ├── app
            │    ├── init.py
            │    ├── config.py
            │    ├── main.py
            │    ├── models.py
            │    ├── oauth2.py
            │    ├── schemas.py
            │    ├── utils.py
            │    └── routers.py
            │          ├── auth.py
            │          ├── post.py
            │          ├── user.py
            │          └── vote.py
            ├── test
            │    ├── conftest.py   
            │    ├── database.py
            │    ├── test_posts.py
            │    ├── test_users.py
            │    ├── test_votes.py
            │    └── init.py
            ├── Dockerfile
            ├── Docker-Compose-prod.yml
            ├── requirements.txt
            ├── .gitignore
            ├── README.md
            └── Workflow.pdf


**I really recommend reading the `Workflow.pdf` to gain a deeper and clearer understanding of the project and how it works internally. I try to do so, by using Flow Diagrams and showing the experiene of the User step by step.**

## **Installation**

You can pull the image from DockerHub, to do so you must have an account. If you don´t, you can clone my project into your local repo and run this command:

      docker-compose -f docker-compose-prod.yml up -d


By doing this you will be building the image and start running your container on the same step, it isn´t mandatory to do it in this way as there are others, it´s just a recommendation. On the Dockerfile, you can see the use of two services (the app itself and the database) which logically are started by different images. The App image is declare and "build" it on the Dockerfile and the Postgresql is the official one from DockerHub. 

Be aware that if you change the places from files of folders or anything like that you may be probably harming the full functionallity of the API for different reasons. 