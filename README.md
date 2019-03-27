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

## Workflow (Phase 1)
- Pull the most recent version of the `develop` branch.
- Pick a document to work on.
- Assign yourself to the document, if it does not exist on the board, create it and self-assign.
- Create a new branch from `develop`
- Sanitize it.
- Review it throughly.
- Make any necessary changes.
- Commit your changes.
- Push your branch.
- Submit pull request.

## Notes:
- Do not make any changes to architecture during phase 1, this could create some complex merge conflicts.
- Do not work on another person's document.
- Pull requests will be reviewed and merged daily.

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

If you believe a change needs to be made to architecture.
