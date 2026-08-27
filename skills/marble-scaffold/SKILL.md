---
name: marble-scaffold
description: Name and bootstrap a new MarbleLabs project. Use when the user wants to start a new repo/app in the MarbleLabs/Cosmic Nexus family and needs a codename plus a clean starter README/index.html/package.json with no third-party AI-builder branding.
---

# marble-scaffold

Generates a project codename in MarbleLabs' own house style and a matching
starter kit, so a new repo never has to be cleaned of borrowed boilerplate
later.

## When to use this

The user says something like "start a new project for X", "I need a name for
this", or "scaffold a repo for Y" in the context of MarbleLabs / Cosmic Nexus
work.

## How to use it

Run the generator with a short description of the project idea:

```bash
python scaffold.py "wallet balance dashboard"
```

It prints a codename (e.g. `nebula-balance-forge-9f21ac3`) and writes three
files into `./out/<codename>/`:

- `README.md` — project title, one-line description from the idea text, a
  "Getting started" section (`npm i && npm run dev`), and a tech-stack list.
- `index.html` — a bare Vite/React shell: no `og:image`/`twitter:*` meta
  pointing at a third-party builder, no injected generator `<script>` tag.
- `package.json` — minimal Vite + React + TypeScript + Tailwind scaffold.

Naming is deterministic: the same idea text always produces the same
codename (seeded from a SHA-256 hash of the input, not `random`), so re-running
the generator for the same project idea is safe and reproducible.

Hand the generated files to the user as the first commit of the new repo.
