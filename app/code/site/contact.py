# mrthompson.wft/code/site/contact.py

import fasthtml.common as fhtml

from code.components.footer import Footer
from code.components.header import Navbar

def contactme():
    page = (
        fhtml.Title("mrthompson's personal read-along blog: About Mister Thompson"),
        fhtml.Main(
            # first component is navbar
            Navbar(),
            # second component is small intro
            fhtml.Main(
                fhtml.H2("Human after all"),
                fhtml.NotStr('<div style="width:100%;height:0;padding-bottom:100%;position:relative;"><iframe src="https://giphy.com/embed/eIERe7YjwgF9SXqaiy" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/IntoAction-puzzle-mental-health-im-a-work-in-progress-eIERe7YjwgF9SXqaiy">via GIPHY</a></p>'),
            ),
            Footer(),
            cls="container",
        ),
    )
    return page
