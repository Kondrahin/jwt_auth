# FastAPI application with JWT authorization

# Deploy

- Clone the repository: `git clone https://github.com/Kondrahin/jwt_auth.git && cd jwt_auth`
- Fill **.env** file: `echo -n SECRET_KEY=>.env && openssl rand -hex 32 >> .env`
- Run Docker: `docker compose up -d`

# Send Requests
- For getting valid JWT token send GET request to `http://127.0.0.1:80/token/`
- Copy `access_token` part
- Send GET request to `‌http://127.0.0.1:80/patients/` with token in the header `Authorization` and get list of the patients
