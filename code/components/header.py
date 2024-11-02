# app/src/home.py

import fasthtml.common as fhtml


def Navbar():
    navbar = (
        fhtml.Nav(
            fhtml.Ul(
                fhtml.Li(
                    fhtml.Strong(
                        fhtml.A("MrThompson's Personal Read-Along Blog", href="/"),
                    )
                ),
            ),
            fhtml.Ul(
                fhtml.Li(
                    fhtml.A("Yo ☺️", href="about-me"),
                ),
                fhtml.Li(
                    fhtml.A("Escribeme 💌", href="contact-us"),
                ),
            ),
            fhtml.Ul(
                fhtml.Li(
                    fhtml.Details(
                        fhtml.Summary(
                            "Tema",
                            cls="secondary"
                        ),
                        fhtml.Ul(
                            fhtml.Li("Auto 🌜",),
                            fhtml.Li("Correcto 😌",),
                            fhtml.Li("Incorrecto 🤔",),
                        ),
                        cls="dropdown",
                    ),
                ),
            ),
        ),
    )
    return navbar
