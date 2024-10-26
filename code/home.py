# app/src/home.py

import fasthtml.common as fhtml

from code.components.footer import Footer
from code.components.header import Navbar


def home():
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
