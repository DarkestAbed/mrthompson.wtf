# mrthompson.wtf/main.py

from fasthtml.common import (
    FastHTML,
    HighlightJS,
    picolink,
    Style,
    serve,
)

from code.site.about import about as aboutpage
from code.site.contact import contactme
from code.site.home import home as homepage
from code.site.posts import retrieve_post as postpage


css = Style(
    ':root {--pico-font-size:90%,--pico-font-familly:Pacifico, cursive;}'
)
highlight = HighlightJS(
        langs=[
            "python",
            "javascript",
            "html",
            "css"
        ]
    )


app = FastHTML(
    debug=True,
    hdrs=(
        highlight,
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


@app.get("/contact-me")
def page2():
    return contactme()


@app.get("/post/{title}")
def get_post(title: str):
    return postpage(title=title)


def main() -> None:
    serve(
        host="0.0.0.0",
        port=8003,
    )
    return None


if __name__ == "__main__":
    main()
else:
    pass
