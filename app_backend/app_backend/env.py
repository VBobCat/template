from os import getenv

# noinspection PyPackageRequirements
import environ


def load_env(dotenv_file_path: str) -> environ.Env:
    env = environ.Env(
        DEBUG=(bool, False),
        DJANGO_DEBUG=(bool, False),
        ALLOWED_HOSTS=(list, []),
        DJANGO_ALLOWED_HOSTS=(list, []),
    )
    if not getenv('INSIDE_DOCKER_CONTAINER'):
        env.read_env(dotenv_file_path)
    return env
