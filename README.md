Purpose: Developing a CI pipeline solution for re-rendering a repository's image files, based on specifications in the galleryze.yaml
Ideally.. any commit to a galleryze file or a defined image file will:
  Run check - are the valid new entries in the .yaml?
  Run re-rendering - as per the .yaml

Decisions down the line:
  GitHub Actions or Hooks?
  Local or remote image rendering? Which API or web service could be relevant?
  
  
  
