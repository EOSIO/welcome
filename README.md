# Documentation Migration Staging Area

This repository is a temporary and private repository for migrating documentation from Readme.io to markdown format in accordance with our established content architecture. All documents in this repository are WIP and subject to change.

## Status
Phase 1:
- [x] Migrate Documents from Readme.io (only current version!) into this repository.
- [x] Migrate glossary from Readme.io (only current version!) into this repository.
- [] Sanitize Readme.io documents to be pure markdown using Ovi's python script.
- [] Evaluate required graphical assets for any documentation, if any: See asset request process.

Phase 2:
- [] Reevaluate documentation for articles that have been reorganized, and make necessary changes.
- [] Project manuals have been merged into their respective repositories.

## Phase 1: Sanitization/Review

The documents exported from readme.io have been more or less adjusted to the new content architecture, albeit it not perfectly. We'll address remaining discrepancies in the next phase.

### Preparation
- Pull the most recent version of the `develop` branch.
- Pick a populated document to work on.
- Assign yourself to the document in Notion, if it does not exist on the board, create it and self-assign.
- Create a new branch from `develop`

### Sanitization
- Run `sanitize.py`
  - Usage: `python sanitize.py ORIGINALFILE.md ORIGINALFILE.sanitized.md`
  - Note: The script creates a new file, for good practice, add `.sanitized` before the `.md` extension
- Review it throughly. The script does not fix everything. For example, image blocks will require an additional step, see "Migrating Images from Readme"
- Move the item in Notion to "sanitized"
- Delete the old file, rename the new file.
- Commit your changes.
- Push your branch.
- Submit pull request.
- Start on a new document.

#### Next steps...
- A reviewer will check the PR, and move it to reviewed.
- Sean will merge the PR and move it to Merged.

### Notes:
- Do not make any changes to architecture during phase 1, this could create some complex merge conflicts.
- Do not work on another person's document.
- Pull requests will be reviewed and merged daily.

## Phase 2: Content Architecture
WIP

## Phase 3: Fill Gaps
WIP

## Phase 3: Final Migration, Dissolve Repo
WIP

## Migrating Images
- Download the image.
- Place the image into the `/images` directory.
- Name the image after its associated article.
- Add the image to the corresponding markdown file to replace it's readme.io image markup counter-part.
- For path, use a root path "/this-is-my-image.png"
- For now, all images will exist in the root directory, this path will be readjusted at a later time, after all content architecture changes have been finalized.

## Glossary
Glossary terms are added to the `glossary.yaml`

A utility will iterate through the items in the file and export markdown files, and in the future, add tooltips for "glossary keywords" throughout articles on the site.

## .skip files

Any directory with a `.skip` file is not being managed in this repository. It signals that the directory in question is already being managed by it's respective project. These directories are included to demonstrate the final content architecture.

# Content Architecture

Over the last few months we collaborated on a content architecture. Please review this architecture for a better understanding of what we're trying to achieve. See the `_workflow` directory for content architecture assets.

# Issues

The use of issues in this repo should be restricted to one of the following cases.

## Requesting Assets

If you believe a piece of content requires a diagram or an image, open a new image and include the following information
- Requirements
- For diagrams, a simple sketch or detailed outline.
- Which document needs it, and where

Place `[asset]` at the beginning of the title of the issue.

## Content Architecture Changes/Additions

If you believe a change needs to be made to architecture, describe the changes, and place `[architecture]` at the beginning of the title of the issue.

## Technical Issues.

If you find a bug in the `sanitize.py` script, please open an issue, prepend with `[bug]`
