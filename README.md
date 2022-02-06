# TECHNICAL ASSESSMENT 2

## Technology Stack

- MongoDB
- Python[flask]
- Docker
- Docker Compose

## How to Run

There are two applications in this repository, a CLI app and a API backend. The database used and these applications are orchestrated by the docker compose file to ensure environment is fully setup before checking out the applications.

To setup the environment using the `docker-compose.yml` file, simply run

```shell
docker-compose build
```

at the root of this project. This will download all necessary packages for this project, including the database used.

### To Run API Backend

After successful docker build, simply run

```shell
docker-compose up
```

to run the database instance and the API backend instance. This would automatically start the API backend server on port 5000. Valid endpoints for the API backend are in [the postman documentation here](https://documenter.getpostman.com/view/11647149/UVeGrRxb).

### To Run the CLI

After successful docker build, simply run

```shell
docker-compose up
```

Open a new terminal where commands would be executed.
Here are valid actions for the CLI

To get the aggregate count for a column

`docker-compose exec backend python cli.py count [column]`

To get the aggregate average for a column [column]

`docker-compose exec backend python cli.py avg Age`

## Assumptions/Choice

- The structure of the record to upload would be consistent with structure of existing record in database; MongoDB was used for this reason, this application is not strict on the structure of records

- At application startup, the database collection is empty. This application is built to automatically seed records into the database only when the collection os empty.

- Since the backend API and the CLI would be running on the same host, the business logic of this application is centralised to the `logics.py` file.
