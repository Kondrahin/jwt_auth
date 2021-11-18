FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
# set path to our python api file
#ENV MODULE_NAME="orangutan.server"
# copy contents of project into docker
COPY poetry.lock pyproject.toml ./
# install poetry
RUN pip install poetry
# disable virtualenv for peotry
RUN poetry config virtualenvs.create false
# install dependencies
RUN poetry install

COPY ./ /app
COPY alembic.ini /app

# Apply migrations
CMD ["alembic", "upgrade", "head"]
