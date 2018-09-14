# LaTeX_Report_Skeleton
This is a latex template made to follow the University of Waterloo Work Term Report Guidelines for Mechanical and Mechatronics Engineering  students. It was used until 2017, so should be more or less up-to-date with requirements at that time. I will attempt to provide further improvements with this over time.

This was developed on Windows, using TexStudio, and MikTex.

## Features and Advantages
This report skeleton comes with many features, both included in LaTeX, by design of this skeleton, or included via custom macros. These include:
 * Automatic Table of Contents, List of Figures, List of Tables
 * Automatic updates of new images (on compilation), as well as data
 * Easy organization of sections
 * Easy numbering and references for figures, tables, references
 * Including code files or snippets
 * Appending PDF documents to the report (CAD drawings, etc)
 * Division of sections into folders (allows easy syncing and reduced conflicts on filesharing platforms)

## Future Work
 * A To-Do macro
 * Better organization of styling files
 * Standardization of methods of compiling the report, and versions of LaTeX compilers.
 * Testing

## Setup
This repository can be cloned in a directory in which to work on the report. It has been cloned it into filesharing directories in past group projects.

The following edits (or not) to files should be made:
 * report.tex is supposed to remain unchanged
 * create a file ```bibliography.bib``` in this directory. This project uses BibTex referencing.
 * Within the ```Sections``` folder, rename ```ex_frontmatter```, ```ex_mainbody``` and ```ex_endmatter``` to no longer have the ```ex_``` portion of their names. Some of these files have example content already. These will be referred to as 'body files'.
 
## Organization
The following directories are used for the following purposes:
 * Figures - This is where the ```addfigure``` macro will look for image files to import
 * Data - This is where the ```addtable``` macro will look for table data files to import
 * Code - This is where the ```addcodesnippet``` and ```addcodefile``` macros will look for code files to import

No changes to these folders will be tracked by git, by default.



## Creating Sections
A good portion of this section is simply suggestions.

Sections are created by creating a folder within the ```Sections``` folder, such as ```Sections/MechanicalDesign``` (please avoid using spaces in filenames). Within this folder, add a ```.tex``` file of the same name, ie: ```Sections/MechanicalDesign/MechanicalDesign.tex```.

In the past, an underscore as been prepended to the file name, so that it will consistently sort to one end of a list of files in the directory, when sorted by name.

This file that you have created is intended to house an upper-level section, ie: ```3.0 Mechanical Design``` (the numbering will be automatic). You can enter the contents of the section into this file, or further distribute this to other files in the directory. Using one file for each sub-section (ie: ```3.1 Chassis```) can be done. This can help prevent editing conflicts when using simple filesharing programs.

### Creating Sections via Python Script

You can use the python script in the ```Sections``` folder to generate a folder and matching .tex file For an upper-level directory. Run the file, and enter the desired section name, again avoiding using spaces. a ```_``` will be prepended to the file.

## Adding sections to the report
Now, in one of the three body files, the command ```/include``` can be used to include this file. You must include a relative path from the body files, and can ignore the ```.tex``` file extension. ie: ```/include{./Sections/MechanicalDesign/_MechanicalDesign}```.

This skeleton has been arranged so that the main content of the body files is a simple listing of these commands. This allows you to easily shuffle the order of sections by changin the order of the addsection commands.


## Available Macros
A few different macros have been developed to make creating a report easier. These are described below:

### addfigure
```addfigure{label}{filename}{caption}{scale}```

This is a macro for adding images to the report. Image files will be pulled on each compile, so and changed/fixed images will be updated. This macro looks in the ```Figures``` directory, although relative paths from that directory can be added to the file name. The figure will be centered, with a box and caption.

```label``` will be used when referencing the figure. It should be unique. ``` filename``` will be the name of the file, including any relative path. The .png extension should be added. ``` caption``` will be the caption underneath the figure. ```Figure X:``` is automatically added. ```scale``` is the horizontal fraction of the page that the image will take up. The range is 0-1.

### addtable
```addtable{label}{filename}{caption}```

This is a macro for adding a table stored in a ```.tex``` file to the report. This files will be found in the ```Data``` folder. The files in this folder do not need all of the usual latex formatting, and can include only the table data and formatting within ```\begin{tabular}...\end{tabular}```. This macro will center the table, and place a caption on top.

```label``` will be used to reference the figure. It should be unique among labels. ```filename``` is the name of the file. ```caption``` is the caption. ```Table X:``` is added automatically.

### addcsvtable
```addcsvtable{label}{filename}{caption}```

This macro is similar to ```addtable```, but allows using a csv-formatted file.

### Referencing Macros
These macros are used for referencing items in the report, such as figures and tables. They use the ```label``` mentioned above. When needed, an numbers will be updated automatically (ex: if a new figure is added).

```reffig{label}``` will produce ```Figure X```

```reftable{label}``` will produce ```Table Y```

```refsection{sectionLabel}``` will produce ```Section A(.B.C)```. This will require adding ```\label{sectionLabel}``` to the end of the line beginning that section.

```refappendix{label}``` will produce ```Appendix A```. A similar label as for sections will be needed.

### addcodesnippet
```addcodesnippet{language}{filename}{firstline}{lastline}{caption}```

This macro adds a snippet of code from a file in the ```Code``` directory. Only lines between ```firstline``` and ```lastline``` are included. ```language``` is the programming language, which may be identified and used for specific auto-formatting of the code.

### addcodefile
```addcodefile{language}{filename}{caption}```

This macro adds an entire code file into the report.



## Bibliography Types
https://en.wikipedia.org/wiki/BibTeX