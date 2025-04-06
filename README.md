Purpose: Developing a CI pipeline solution for re-rendering a repository's image files, based on specifications in the galleryze.yaml
Ideally.. any commit to a galleryze file or a defined image file will:
  Run check - are the valid new entries in the .yaml?
  Run re-rendering - as per the .yaml

Decisions down the line:
  GitHub Actions or Hooks?
  Server-side or remote image rendering? Which API or web service could be relevant?
  
  
  ++ List ++

>.*galleryze has to exist in the repository.
>The folder 'Gallerized Images' is created if not there, in the same folder as .*galleryze
>Each image file in this folder is scripted to have a '_RENDERED' suffix - as it could help situations where users toss input files up in there.
>If an image has more than 5% fully transparent pixels (alpha value of 0), it would be safe to say it's 'backgroundless' - the logo itself would never contain invisible pixels...
>In the abscence of valid file types outside this folder, the 'full-transparancy-rate' calculation is run only for 'Gallerized Images',
	excluding files ending with _RENDERED. Any misplaced files could be tossed into a 'Failed Galleryzations'-type-folder (?)
>YAML schema : 
	fileType:					        // Each of these keys need at least one value
	fileTypeInput: "PNG"		  // Validated against Python's os import AND a defined array of acceptable file types.
    fileTypeOutput: "PNG"		
	newBackgroundColorsHex:		// Max set to 4. Invalid if < 1
	- "#1E1E1E"					      // Hex code could be validated via Pillow
	- "#9CDCFE"					      // Colors are concatinated onto the rendered filename if valid.
>Any changes to the yaml-file 
>An arbitrary maximum of 1000 valid files is set for the population of validated images files in the repo.
>Valid file types' names are listed in a temp-array, for the following re-rending via Pillow.
