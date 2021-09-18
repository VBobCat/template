FROM python:3-bullseye

# install linux dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install \
    apt-utils \
    smbfs \
    firefox-esr \
    firefox-esr-l10n-pt-br \
    postgresql-client \
    pulseaudio \
    unixodbc-dev \
    xyfb \
    -y --fix-missing
RUN date

# setup python environment
ENV PYTHONUNBUFFERED=TRUE
ENV INSIDE_DOCKER_CONTAINER=TRUE
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
RUN python -m pip install --upgrade wheel
RUN python -m pip install --upgrade gunicorn

# install source code and dependencies
WORKDIR /app_backend
COPY . /app_backend
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --clear --noinput

# do not set a CMD here but in docker-compose.yml,
# so that you can use this image both for starting a web server of an internal script