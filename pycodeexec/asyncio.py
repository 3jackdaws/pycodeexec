from . import sync
from docker.transport.npipesocket import NpipeSocket

class Runner(sync.Runner):

    def __init__(self, language, version='default'):
        self.image, self.command = sync.get_image_command(language, version)
        self.container = sync.client.containers.create(
            self.image,
            detach=True,
            command="sleep 3600",
        )
        self.container.start()

    def __del__(self):
        self.container.kill()

    async def get_output(self, code, decode=True):
        sock = self.container.exec_run(
            self.command.format(
                code.replace('"', r'\"')
            ),
            socket=True
        )[1]  # type: NpipeSocket
        sock.setblocking(False)
        while 1:
            r = sock.recv(8192)
            print(r)