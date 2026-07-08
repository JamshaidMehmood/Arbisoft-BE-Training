"""Application entry point."""

from server import HttpServer


def main():
    """Start the application."""

    server = HttpServer()
    server.run()


if __name__ == "__main__":
    main()
