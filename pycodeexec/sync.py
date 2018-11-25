import docker
from docker.models.containers import Container
from .languages import LANGUAGES

client = docker.from_env()

_language_lookup = LANGUAGES

def get_image_command(language, version):
    language_config = _language_lookup.get(language)
    if language_config:
        versions = language_config['versions']
        default = versions.get('default')
        image = default['image']
        tag = default['tag']
        command = default['command']
        return f"{image}:{tag}", command


class Runner:
    def __init__(self, language, version='default'):
        self.image, self.command = get_image_command(language, version)
        self.container = client.containers.run(
            self.image,
            detach=True,
            command="sleep 3600",
            remove=True,
        )  # type: Container

    def __del__(self):
        self.container.kill()

    def get_output(self, code, decode=True):
        exit_code, result = self.container.exec_run(
            self.command.format(
                code.replace('"', r'\"')
            )
        )
        if decode:
            return result.decode()
        else:
            return result


# for language_name in LANGUAGES:
#     _language_lookup[language_name] = LANGUAGES[language_name]
#     aliases = language_name.get('aliases')
#     if aliases:
#         for alias in aliases:
#             _language_lookup[alias] = LANGUAGES[language_name]

