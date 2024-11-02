# mrthompson.wtf/main.py

from fasthtml.common import FastHTML, picolink, Style, serve

from code.site.home import home as homepage
from code.site.about import about as aboutpage
from code.utils.get_posts import parse_all_posts


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
    post_data = parse_all_posts()
    print(f"post: {post_data[0][0]}\nfrontmatter: {post_data[0][1]}\nhtml: {post_data[0][2]}")
    serve()
    return None


if __name__ == "__main__":
    main()
else:
    pass
