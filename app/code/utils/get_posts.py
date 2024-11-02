# mrthompson.wtf/code/utils/get_posts.py

from frontmatter import load
from markdown import markdown
from operator import itemgetter
from os import getcwd, listdir
from os.path import basename, exists, join


def get_md_file_list() -> list[str]:
    POSTS_PATH: str = join(getcwd(), "app", "static", "posts")
    if not exists(POSTS_PATH):
        raise FileNotFoundError(f"Path with posts '{POSTS_PATH}' is not found on server")
    else:
        pass
    files_list: list[str] = listdir(POSTS_PATH)
    md_list: list[str] = list()
    for file in files_list:
        if ".md" in file:
            md_list.append(join(POSTS_PATH, file))
    return md_list


def read_frontmatter(path: str) -> str:
    with open(file=path) as f:
        frontmatter: dict[str, str] = dict(load(fd=f))
    return frontmatter


def read_markdown(path: str) -> str:
    # getting the line number where fm ends
    with open(file=path) as f:
        raw_md: list[str] = f.readlines()
    i: int = 0
    index: int = 0
    for idx, val in enumerate(raw_md):
        if "---" in val:
            i += 1
        if i == 2:
            index = idx + 1
            break
    # parsing only the html portion of file
    parsed_md: str = " ".join(raw_md[index:])
    html: str = markdown(text=parsed_md)
    return html


def parse_post(path: str) -> list[str, str, str]:

    def get_post_link(path: str) -> tuple[str, str]:
        file_name: str = basename(path)
        post_link: str = file_name.replace(".md", "")
        return (file_name, post_link)

    if not exists(path):
        raise FileNotFoundError(f"Post located on '{path}' was not found")
    else:
        pass
    post_file, post_link = get_post_link(path)
    post_items: dict[str, str] = {
        "file": post_file,
        "addr": post_link,
        "date": read_frontmatter(path=path).get("date"),
        "published": read_frontmatter(path=path).get("published"),
        "fm": read_frontmatter(path=path),
        "html": read_markdown(path=path),
    }
    return post_items


def parse_all_posts() -> list[dict]:
    post_list: list[str] = get_md_file_list()
    parsed_post_list: list[dict] = list()
    for post in post_list:
        try:
            post_data: dict[str, str] = parse_post(path=post)
        except FileNotFoundError:
            pass
        except Exception as e:
            pass
        if post_data.get("published") is True:
            parsed_post_list.append(post_data)
    sorted_post_list: list[str] = sorted(parsed_post_list, key=itemgetter("date"), reverse=True)
    return sorted_post_list


def main() -> None:
    return None


if __name__ == "__main__":
    main()
else:
    pass
