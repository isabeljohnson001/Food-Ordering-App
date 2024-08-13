# Food-Ordering-App
EatMe is a full-stack, microservice-based food ordering application designed for scalability and efficiency. Built with modern technologies like Python's FastAPI and Javascript. This application follows best practices in object-oriented design and microservices architecture. It serves as a robust template to create advanced backend microservice projects.

Technology Stack and Features:

- [**FastAPI**](https://fastapi.tiangolo.com):
    - [pydantic](https://docs.pydantic.dev) for settings and request/response validation.
    - JWT middleware for secure authentication.
    - Permission manager for role-based access control on routes.
    - Rate limiting for API protection.
    - RequestId, Timing, and many exciting middlewares!
    - Secure password hashing by default.
    - Customizable profilers with [Prometheus](https://prometheus.io/).

- [**MongoDB**](https://www.mongodb.com/): 
  - Async client with [motor](https://github.com/mongodb/motor) and Object Document Mapping (ODM) 

- [**Redis**](https://redis.io/):
  - Async operations for caching and session management.
  - [redis-py](https://github.com/redis/redis-py).

- **PostgreSQL**:
  - Async client with [aqlachemy](https://github.com/sqlalchemy/sqlalchemy) ORM & automatic migrations with [alembic](https://github.com/sqlalchemy/alembic)..
  - [asyncpg-client](https://github.com/deepmancer/asyncpg-client) as the session manager.

- [**RabbitMQ**](https://www.rabbitmq.com/):
  - Utilizing [rabbitmq-rpc](https://github.com/deepmancer/rabbitmq-rpc) and [aio-pika](https://github.com/mosquito/aio-pika).
  - No server-side implementation.

- [**Docker Compose**](https://www.docker.com):
  - Containers for simplified deployment and scaling.

- [**Pytest**](https://github.com/pytest-dev/pytest):
  - Async tests with pytest and pytest-async.

## **GUI Management Tools**
- [**Grafana**](https://grafana.com/): Automatic metric dashboards on endpoints using [Prometheus](https://prometheus.io/).
- [**Metabase**](https://www.metabase.com/): PostgreSQL/MongoDB analytics and reporting.
- [**RedisInsight**](https://redis.io/insight/): Redis data visualization and management.
- [**Mongo-Express**](https://github.com/mongo-express/mongo-express): MongoDB admin interface.
- [**RabbitMQ Management**](https://www.rabbitmq.com/docs/management): Visualizing and monitoring events.
 
These tools are configured and run via Docker in the `infra/admin/docker-compose.yaml`.

## **Setup Instructions**

### **Step 1: Create Docker Networks**

Create Docker networks for backend and frontend services.

```bash
docker network create --driver bridge backend-network
docker network create --driver bridge frontend-network
```

### **Step 2: Build and Run Infrastructure**

Navigate to the infrastructure directory and start the services, including databases and GUI tools.

```bash
cd backend/infra
docker compose up --build
```

#### **Infrastructure Layout:**

```bash
backend/infra
├── admin (Metabase, RedisInsight, Mongo-Express)
├── mongo
├── monitoring (Grafana, Prometheus)
├── postgres
├── rabbitmq (with the Management extension)
└── redis
```

### **Step 3: Build and Run Microservices**

Navigate to the backend directory and start all microservices.

```bash
cd backend/
docker compose up --build
```

## **Frontend Setup**

The frontend is built with Vue.js for a dynamic and responsive user experience.

### **Step 1: Install Dependencies**

Navigate to the `ui/` directory and install the required packages.

```bash
cd ui/
npm install
```

### **Step 2: Start Development Server**

Run the development server with hot-reloading enabled.

```bash
npm run serve
```

## Interactive API Documentation
![image](https://github.com/isabeljohnson001/Food-Ordering-App/blob/5c751cbaa7477a719dfb2c0b00f2c7f7ebdf434f/images/api_documentation.png)

## Admin Dashboards
### Grafana
![image](https://github.com/isabeljohnson001/Food-Ordering-App/blob/5c751cbaa7477a719dfb2c0b00f2c7f7ebdf434f/images/grafana.png)

### Metabase
![image](https://github.com/isabeljohnson001/Food-Ordering-App/blob/5c751cbaa7477a719dfb2c0b00f2c7f7ebdf434f/images/metabase.png)

### Redis
![image](https://github.com/isabeljohnson001/Food-Ordering-App/blob/5c751cbaa7477a719dfb2c0b00f2c7f7ebdf434f/images/redis.png)

### RabbitMQ Management
![image](https://github.com/isabeljohnson001/Food-Ordering-App/blob/5c751cbaa7477a719dfb2c0b00f2c7f7ebdf434f/images/rabbitmq.png)

### MongoDB Compass
![image](https://github.com/isabeljohnson001/Food-Ordering-App/blob/5c751cbaa7477a719dfb2c0b00f2c7f7ebdf434f/images/mongodb.png)
