from pyapp.app import CliApplication, CommandOptions
from pyapp.injection import inject_into, FactoryArgs

import sample


app = CliApplication(sample)


@app.command
def send(opts: CommandOptions):
    from pyapp_ext.aiomq import TaskQueue

    @inject_into
    def send_message(*, queue: TaskQueue = FactoryArgs(name="jobs")):
        queue.send("Hi!")

    send_message()


def main(args=None):
    app.dispatch(args)


if __name__ == '__main__':
    main()
