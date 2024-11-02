# mrthompson.wtf/main.py

from fasthtml.common import FastHTML, picolink, Style, serve

from code.site.home import home as homepage
from code.site.about import about as aboutpage


css = Style(
    ':root {--pico-font-size:90%,--pico-font-familly:Pacifico, cursive;}'
)

app = FastHTML(
    hdrs=(
        picolink,
        css,
    ),
)


@app.get("/")
def home():
    return homepage()


@app.get("/about-me")
def page2():
    return aboutpage()


def main() -> None:
    serve()
    return None


if __name__ == "__main__":
    main()
else:
    pass
