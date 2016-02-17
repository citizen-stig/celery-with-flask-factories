# -*- encoding: utf-8 -*-
from factories.application import create_application


def run():
    app = create_application()
    app.run(debug=True)

if __name__ == '__main__':
    run()
