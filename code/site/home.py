# mrthompson.wft/code/site/home.py

import fasthtml.common as fhtml

from typing import Any

from code.components.footer import Footer
from code.components.header import Navbar
from code.utils.get_posts import parse_all_posts


def post_list(input_list: list[dict]) -> Any:

    def parse_post_item(obj: dict) -> Any:
        fm: dict[str, str] = obj.get("fm")
        html_r: Any = fhtml.Div(
            fhtml.H1(fm.get("title")),
            fhtml.Em(fm.get("date")),
            fhtml.P(f"{fm.get('description')}"),
            fhtml.Hr(),
        )
        return html_r

    div_obj: Any = fhtml.Div(
        *[ parse_post_item(obj=post) for post in input_list ],
    )
    return div_obj


def home():
    posts = post_list(input_list=parse_all_posts())
    page = (
        fhtml.Title("mrthompson's personal read-along blog"),
        fhtml.Main(
            # first component is navbar
            Navbar(),
            # second component is small intro
            fhtml.Header(
                fhtml.Article(
                    fhtml.Div(
                        fhtml.Div("Wilkommen!"),
                        fhtml.Div("Speak _mellon_ and enter"),
                        fhtml.Div("Nada mas que decir"),
                        cls="grid",
                    ),
                ),
            ),
            fhtml.Main(
                    fhtml.Article(
                        fhtml.Div("Primera seccion: intro"),
                    ),
                    # this is a test component
                    # TODO: remove
                    fhtml.Article(
                        fhtml.P("Segunda seccion: testeos"),
                        fhtml.Div(
                            "Aqui hay algo de texto ",
                            fhtml.A("Un link", href="https://mrthompson.xyz"),
                        ),
                        fhtml.Div(
                            fhtml.Img(src="https://placehold.co/200"),
                        ),
                    ),
                    # this is the REAL second component
                    fhtml.Article(
                        posts,
                    ),
                    # third component is blogpost categories
                    fhtml.Article(
                        fhtml.P("Tercera seccion: categorias"),
                    ),
                    fhtml.Article(
                        fhtml.P("Cuarta seccion: articulos"),
                    )
            ),
            Footer(),
            cls="container",
        ),
    )
    return page
