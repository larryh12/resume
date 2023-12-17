import fitz


def generate_readme():
    readme = ""

    doc = fitz.open("current/larry-huynh-resume.pdf")

    for page in doc:
        pix = page.get_pixmap(dpi=300)
        pix.save(f"preview/larry-huynh-resume-page-{page.number}.png")

        readme += f"![](preview/larry-huynh-resume-page-{page.number}.png)\n\n"

    return readme


if __name__ == "__main__":
    readme = generate_readme()

    with open("README.md", "w") as f:
        f.write(readme)
