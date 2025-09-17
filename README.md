# E-Commerce Backend

## Real-World Application

The e-commerce backend simulates a real-world development environment, emphasizing *scalability*, *security*, and *performance*. This project showcases:
- Design of optimal relational database schemas.
- Well documented APIs for frontend integration.
- Enhanced backend performance through query optimization and indexing.

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

- Filtering and Sorting: Allow users to filter products by category and sort by price.
- Pagination: Implement paginated responses for large product datasets.

### 3. API Documentation

- Use Swagger or Postman to generate API documentation.
- Publish hosted API docs for easy frontend consumption.

## Implementation Process

### Git Commit Workflow

```bash
feat: set up Django project with PostgreSQL
feat: implement user authentication with JWT
feat: add product APIs with filtering and pagination
feat: integrate Swagger documentation for API endpoints
perf: optimize database queries with indexing
docs: add API usage instructions in Swagger
```

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

## Prerequisites

Ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/) (for cloning the project)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Namisi-Aaron/alx-project-nexus.git
cd alx-project-nexus
```

### 2. Create and activate virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependancies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

The app's API documentation (swagger) will be available at: http://127.0.0.1:8000/
