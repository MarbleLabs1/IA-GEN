#!/usr/bin/env python3
"""Name and bootstrap a new MarbleLabs project. See SKILL.md."""

import hashlib
import os
import sys

ADJECTIVES = [
    "cosmic", "stellar", "nebula", "quantum", "aurora", "vibrant",
    "lunar", "cinder", "cobalt", "prism", "solstice", "onyx",
]

NOUNS = [
    "forge", "dex", "hub", "portal", "boost", "mixer",
    "vault", "drive", "grid", "nexus", "core", "beacon",
]


def slugify(text: str) -> str:
    words = "".join(c.lower() if c.isalnum() else " " for c in text).split()
    return "-".join(words[:2])


def codename(idea: str) -> str:
    digest = hashlib.sha256(idea.strip().lower().encode("utf-8")).hexdigest()
    adjective = ADJECTIVES[int(digest[0:4], 16) % len(ADJECTIVES)]
    noun = NOUNS[int(digest[4:8], 16) % len(NOUNS)]
    suffix = digest[:7]
    idea_slug = slugify(idea)
    return f"{adjective}-{idea_slug}-{noun}-{suffix}"


README_TEMPLATE = """# {name}

{idea}

## Getting started

Requires Node.js & npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
npm i
npm run dev
```

## Tech stack

- Vite
- TypeScript
- React
- Tailwind CSS
"""

INDEX_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name}</title>
    <meta name="description" content="{idea}" />
    <meta name="author" content="MarbleCeo" />
  </head>

  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""

PACKAGE_JSON_TEMPLATE = """{{
  "name": "{name}",
  "private": true,
  "version": "0.0.1",
  "type": "module",
  "scripts": {{
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }},
  "dependencies": {{
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  }},
  "devDependencies": {{
    "@vitejs/plugin-react": "^4.3.1",
    "tailwindcss": "^3.4.10",
    "typescript": "^5.5.4",
    "vite": "^5.4.1"
  }}
}}
"""


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: scaffold.py \"project idea\"", file=sys.stderr)
        raise SystemExit(1)

    idea = " ".join(sys.argv[1:])
    name = codename(idea)
    out_dir = os.path.join("out", name)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(README_TEMPLATE.format(name=name, idea=idea))
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX_HTML_TEMPLATE.format(name=name, idea=idea))
    with open(os.path.join(out_dir, "package.json"), "w", encoding="utf-8") as f:
        f.write(PACKAGE_JSON_TEMPLATE.format(name=name))

    print(name)
    print(f"scaffold written to {out_dir}/")


if __name__ == "__main__":
    main()
