import re
import argparse
import os

from heart import Heart

GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)
HEART_RATE_HEAD = "| Time | Rate | \n | ---- | ---- | \n"
HEART_RATE_STAT_TEMPLATE = "| {time} | {value} |\n"
OUT_FOLDER = os.path.join(os.getcwd(), "files")


def replace_readme_comments(file_name, comment_str, comments_name):
    with open(file_name, "r+") as f:
        text = f.read()
        # regrex sub from github readme comments
        text = re.sub(
            GITHUB_README_COMMENTS.format(name=comments_name),
            r"\1{}\n\3".format(comment_str),
            text,
            flags=re.DOTALL,
        )
        f.seek(0)
        f.write(text)
        f.truncate()


def parse_ios_str_to_list(list_str):
    l = list_str.splitlines()
    # filter the empty value
    return [i for i in l if i]


def make_summary_str(time_list, value_list):
    s = HEART_RATE_HEAD
    for t, v in zip(time_list, value_list):
        s += HEART_RATE_STAT_TEMPLATE.format(time=t, value=v)
    return s


def main(time_list_str, value_list_str):
    time_list = parse_ios_str_to_list(time_list_str)
    value_list = parse_ios_str_to_list(value_list_str)
    value_list = [int(float(i)) for i in value_list]

    s = make_summary_str(time_list, value_list)
    replace_readme_comments("README.md", s, "my_heart_rate")

    # generate heart rate svg and save
    h = Heart(os.path.join(OUT_FOLDER, "heart.svg"))
    h.set_values(value_list)
    h.make_heart_svg()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("time_list_str", help="time_list_str")
    parser.add_argument("value_list_str", help="value_list_str")
    options = parser.parse_args()
    main(
        options.time_list_str,
        options.value_list_str,
    )
