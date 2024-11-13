# app/src/home.py

import fasthtml.common as fhtml


def Footer():
    footer = (
        fhtml.Footer(
                fhtml.Div(
                    "Mr Thompson ©️ 2024",
                    id="copyright"
                )
            ),
    )
    return footer
