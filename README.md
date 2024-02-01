# Fastinni

Fastinni is a project inspired by conversations with the developer of [Flaskinni](https://github.com/dadiletta/flaskinni). It serves as a starter FastAPI application with the following stack:

1. **[SQLModel Database](https://sqlmodel.tiangolo.com/)**: Tested with PostgresQL, it stores users, OAuth2 client registrations, roles, groups, blog posts, and more.

2. **[FastAPI & Python](https://fastapi.tiangolo.com/)**: FastAPI simplifies managing a stateless server. Additional libraries like FastAPI-CSRF-Protect and FastAPI-Mail enhance functionality.

3. **[Uvicorn](https://www.uvicorn.org/)**: Uvicorn serves as the ASGI framework, replacing WSGI frameworks like Gunicorn.

4. **[ReactJS Frontend](https://react.dev/)**: Provides an appealing display for the application's complex functionality.

In addition to these main components, other elements such as a reverse proxy (e.g., NGINX or Apache) for added robustness and cloud products like AWS, Cloudflare, or Google Cloud to mitigate DDOS and other attacks may be incorporated. However, for the most part, these components suffice to initiate a FastAPI/React full stack project.