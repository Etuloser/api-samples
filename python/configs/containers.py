from dependency_injector import containers, providers

from pkg.oauth2.obtaining_credentials import obtaining_credentials


class Containers(containers.DeclarativeContainer):
    pass


containers = Containers()
