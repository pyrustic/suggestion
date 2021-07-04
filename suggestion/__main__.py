# "__main__.py" generated by Pyrustic Project Manager
from pyrustic.app import App
from pyrustic.hello import HelloView
from cyberpunk_theme import Cyberpunk


def main():
    # The App
    app = App()
    # Set the title
    app.title = "suggestion"
    # Set the theme
    app.theme = Cyberpunk()
    # Set the view
    app.view = lambda app: HelloView(app)
    # Center the window
    app.center()
    # Lift off !
    app.start()


if __name__ == "__main__":
    main()
