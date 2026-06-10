"""Scarica i woff2 (subset latin) da Google Fonts per l'uso self-hosted offline.

Eseguire dalla cartella assets/fonts/:  python download_fonts.py
Genera anche fonts.css con i @font-face locali.
"""
import re
import urllib.request
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

CSS_URL = ("https://fonts.googleapis.com/css2"
           "?family=Outfit:wght@400;500;700;800"
           "&family=JetBrains+Mono:wght@400;500"
           "&display=swap")

OUT = Path(__file__).parent


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as r:
        return r.read()


def main() -> None:
    css = fetch(CSS_URL).decode("utf-8")
    blocks = re.findall(r"/\*\s*(\S+)\s*\*/\s*@font-face\s*\{([^}]+)\}", css)
    faces = []
    for subset, body in blocks:
        if subset != "latin":
            continue
        family = re.search(r"font-family:\s*'([^']+)'", body).group(1)
        weight = re.search(r"font-weight:\s*(\d+)", body).group(1)
        url = re.search(r"url\((https://[^)]+\.woff2)\)", body).group(1)
        slug = family.lower().replace(" ", "-")
        fname = f"{slug}-{weight}.woff2"
        (OUT / fname).write_bytes(fetch(url))
        size_kb = (OUT / fname).stat().st_size // 1024
        print(f"{fname}  {size_kb} KB")
        faces.append((family, weight, fname))

    lines = []
    for family, weight, fname in faces:
        lines.append(
            "@font-face {\n"
            f"  font-family: '{family}';\n"
            "  font-style: normal;\n"
            f"  font-weight: {weight};\n"
            "  font-display: swap;\n"
            f"  src: url('../fonts/{fname}') format('woff2');\n"
            "}"
        )
    (OUT / "fonts.css").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"fonts.css generato con {len(faces)} @font-face")


if __name__ == "__main__":
    main()
