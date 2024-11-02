# mrthompson.wft/code/site/posts.py

import fasthtml.common as fhtml

from typing import AnyStr

from code.components.footer import Footer
from code.components.header import Navbar

def retrieve_post(title: str) -> AnyStr:

    def get_post_html(title: str) -> AnyStr:
        from code.utils.get_posts import parse_all_posts

        post_list: list[dict] = parse_all_posts()
        for post in post_list:
            if post["addr"] == title:
                print(post.get("file"))
                post_title: str = post.get("fm").get("title")
                post_desc: str = post.get("fm").get("description")
                post_date: str = post.get("date")
                post_html: str = post.get("html")
                break
        obj_ret: dict[str, str] = {
            "title": post_title,
            "desc": post_desc,
            "date": post_date,
            "html": post_html,
        }
        return obj_ret

    post: dict = get_post_html(title=title)
    page = (
        fhtml.Title("mrthompson's personal read-along blog"),
        fhtml.Main(
            # first component is navbar
            Navbar(),
            # then, post data
            fhtml.Main(
                fhtml.H1(f"{post.get('title')}"),
                fhtml.H4(post.get("desc")),
                fhtml.H6(f"Burped on {post.get("date")}"),
                # this is the REAL second component
                fhtml.NotStr(
                    *[ post.get("html") ],
                ),
            ),
            fhtml.Container(
                fhtml.Hr(),
            ),
            Footer(),
            cls="container",
        ),
    )
    return page
