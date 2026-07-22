"""Application entry point."""

from .server import HttpServer


def main():
    server = HttpServer()
    server.run()


if __name__ == "__main__":
    main()
