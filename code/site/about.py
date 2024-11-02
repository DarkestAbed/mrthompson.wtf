# mrthompson.wft/code/site/about.py

import fasthtml.common as fhtml

from code.components.footer import Footer
from code.components.header import Navbar

def about():
    page = (
        fhtml.Title("mrthompson's personal read-along blog: About Mister Thompson"),
        fhtml.Main(
            # first component is navbar
            Navbar(),
            # second component is small intro
            fhtml.Main(
                    fhtml.Article(
                        fhtml.Div("Primera seccion: que hago"),
                    ),
                    # this is a test component
                    # TODO: remove
                    fhtml.Article(
                        fhtml.P("Segunda seccion: que quiero hacer"),
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
                        fhtml.P("Tercera seccion: que importa el nombre"),
                    ),
            ),
            Footer(),
            cls="container",
        ),
    )
    return page
