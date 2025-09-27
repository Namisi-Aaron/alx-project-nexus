# E-Commerce Backend

## Real-World Application

The e-commerce backend simulates a real-world development environment, emphasizing *scalability*, *security*, and *performance*. This project showcases:
- Design of optimal relational database schemas.
- Well documented APIs for frontend integration.
- Enhanced backend performance through query optimization and indexing.

The **video presentation** for this project can be found [here](https://app.presentations.ai/view/5OHwWiE7sC).

## Overview

This case study focuses on developing a robust backend system to support an e-commerce product catalog. The backend will handle product data management, user authentication, and APIs for filtering, sorting, and pagination, simulating a real-world scenario for backend engineers.

## Project Goals

- **CRUD APIs:** Build APIs for managing products, categories, and user authentication.
- **Filtering, Sorting, Pagination:** Implement robust logic for efficient product discovery.
- **Database Optimization:** Design a high-performance database schema to support seamless queries.

## Technologies Used

- **Django:** For building a scalable backend framework.
- **PostgreSQL:** As the relational database for optimized performance.
- **JWT:** For secure user authentication.
- **Swagger/OpenAPI:** To document and test APIs.

## Key Features

### 1. CRUD Operations

- Create, read, update, and delete operations for products and categories.
- User authentication and management features using JWT.

### 2. API Features

- *Filtering and Sorting:* Allow users to filter products by category and sort by price.
- *Pagination:* Implement paginated responses for large product datasets.

### 3. API Documentation

- Use Swagger or Postman to generate API documentation.
- Publish hosted API docs for easy frontend consumption.

### 4. Permissions

The API contains a series of enforced permissions that ensure security and Role Based Access. These include:
- Only admins users can create, update and delete products and categories
- Only admins users can retrieve and update details of other users other than themselves
- Regular users can only create payments for orders that they are ssociated with
- Regular users can only retrieve, update and delete payments and orders that they are associated with. Admin users can view the entire dataset

### 5. Background Tasks

The API utilizes **Celery** as it's background worker. **Redis** serves as a storage backend for results, while **RabbitMQ** servers as a message broker.
Background tasks include:
- *send_order_creation_email* - sends a notification when a new order instance is created
- *send_payment_completion_email* - sends a notification when a payment is completed (both failed or successful payments)
- *send_low_stock_alert* - alerts the admin user when stock levels reduce below the set threshold
- *send_user_creation_email* - sends a notification when a new user is created successfully.

## Submission Details

- API Deployment: Host the API with documentation published (e.g., Swagger or Postman).

## Evaluation Criteria

**1. Functionality**
 - CRUD APIs for products, categories, and user authentication.
 - Filtering, sorting, and pagination logic implemented effectively.

**2. Code Quality**
 - Clean, maintainable, and well-documented code.
 - Proper database indexing for high-performance queries.

**3. User Experience**
 - API documentation is comprehensive and user-friendly.
 - Secure authentication implementation.

**4. Version Control**
 - Frequent and descriptive Git commit messages.
 - Well-organized repository structure.

---
## Running the application

This backend uses Docker Compose to run a multi-container Django application along with its dependencies (i.e., PostgreSQL, Redis, Celery, and RabbitMQ).

## Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/) (for cloning the project)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Namisi-Aaron/alx-project-nexus.git
cd alx-project-nexus
```

### 2. Configure Environment Variables

Create a .env file in the project root. Example:

```bash
DJANGO_SECRET_KEY=your_secret_key
DEBUG=debug_value

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=db_name
DATABASE_USER=db_user
DATABASE_PASSWORD=db_password
DATABASE_HOST=db_host
DATABASE_PORT=db_port

DJANGO_SUPERUSER_USERNAME=db_admin_username
DJANGO_SUPERUSER_PASSWORD=db_admin_password
DJANGO_SUPERUSER_EMAIL=db_admin_email

CELERY_BROKER_URL=broker_url
CELERY_RESULT_BACKEND=result_backend_url
REDIS_URL=redis_url_

CHAPA_SECRET_KEY=chapa_secret_key
CHAPA_PUBLIC_KEY=chapa_public_key
CHAPA_API_BASE=chapa_api_base
CHAPA_CALLBACK_URL=chapa_callback_url
```

Configure these with your credentials

### 3. Build and Start Containers

Run the following command to build and start all services:

```bash
docker compose up --build
```

A seeding file exists in products/management/commands that adds sample data to the database when initialization. It is run when building the app

### 4. Access the Application

- API documentation (swagger) will be available at: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

### 5. Stopping Containers

To stop all running containers:

```bash
docker compose down
```

Add *--volumes* to stop but keep volumes

### 6. Useful Commands

- Check running logs:

```bash
docker compose logs -f
```

- Run shell inside Django container:

```bash
docker compose exec web python manage.py shell
```

- Rebuild after changes:

```bash
docker compose up --build
```

A version of this app is hosted on Render. Access it 👉 [here](https://alx-project-nexus-gckp.onrender.com)