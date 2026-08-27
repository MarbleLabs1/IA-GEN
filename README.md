# IA-GEN

Home of MarbleLabs1's custom Claude Agent Skills — reusable playbooks that Claude
follows when working on Marble projects.

## Skills

### [`marble-scaffold`](skills/marble-scaffold/)

Names and bootstraps a new MarbleLabs project in-house. Give it a one-line idea,
it deterministically generates a project codename in the studio's own naming
style (`cosmic-`, `stellar-`, `nebula-`, `-forge`, `-dex`, `-hub`, plus the
short hex suffix already used across the org's repos) and writes a starter
`README.md`, `index.html` and `package.json` — clean from the first commit,
with no third-party generator branding baked in.

## Why this exists

Several MarbleLabs repos were bootstrapped through third-party AI app builders
and inherited that tool's boilerplate (generator meta tags, a
"how to edit this project" README written for a different audience). None of
that described the actual projects, and cleaning it out after the fact meant
touching a dozen repos by hand. `marble-scaffold` exists so new projects start
clean instead.
