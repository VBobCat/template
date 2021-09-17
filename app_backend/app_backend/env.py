# noinspection PyPackageRequirements
import environ


def load_env(path) -> environ.Env:
    env = environ.Env(
        DEBUG=(bool, False),
        DJANGO_DEBUG=(bool, False),
        ALLOWED_HOSTS=(list, []),
        DJANGO_ALLOWED_HOSTS=(list, []),
    )
    env.read_env(path)
    return env
