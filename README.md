# Deploy FastAPI on Render

This project demonstrates how to deploy a FastAPI application on Render.

## Overview

I have created a test FastAPI API and successfully deployed it on Render. Along with the application, I have also set up a PostgreSQL database using Render’s built-in database service.

The setup is working successfully, and the deployed application is accessible via a public URL:

https://test-2-1jtk.onrender.com

## Local Development

To run the project locally, I use the following command:

uvicorn main:app --host 0.0.0.0 --port 9001

## Database & Migrations

* PostgreSQL database is configured using Render
* Alembic is used for database migrations
* A test table (`users`) has been created using Alembic

## Deployment Steps

You can deploy this project on Render by following these steps:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Render will automatically detect it as a Python project
4. Use the following Start Command:

uvicorn main:app --host 0.0.0.0 --port $PORT

5. Click on **Create Web Service**

## Notes

* Render allows managing both application and database in one place
* This simplifies deployment and reduces external dependencies