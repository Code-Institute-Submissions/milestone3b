# milestone3b
Second attempt at Data Centric Development Project

For this project I created a simple website called suburban dictionary 
This website allows visitors to upload their own puns or play on words.
As is often the case with this kind of dad-jokery, these puns can be cringe-inducing;
and so users are able to makes changes or even simply delete uploaded puns 
that they feel are of an (in)sufficient embarrassment quotient.

In this way I hope to demonstrate my ability to CRUD using a database of user-generated puns.

## UX

For all paternal-types or paternal-at-heart, I hope to have created a space for uers to upload and peruse the best 
puns and play on words they can find. I'm using a simple, interactive layout, to help draw the eye's attention to one 
expression at a time while still displaying the other possible puns for users to view.

I also have several calls to action on the home screen for users to upload they're own turns of phrases, in the navbar
and in the "About" Card.

### User Stories:

    As a fan of puns, I want to view others' puns, so that I can sprinkle them into my day-to-day conversations.
    As a pun-skeptic, I want to view others' puns, so that I can audibly groan and roll my eyes in disgust.
    As a particularly witty wordsmith, I want to upload my play on words, so that I can demonstrate my mastery of the English language.

### Wireframes:

![](/images/wireframes-index.png)

Here I've gone for a simple, clean layout using the materialize framework
Puns are displayed list-wise in an accordion format, hat expands to display a defintion and example.
There are also boldly-coloured edit and delete buttons to draw the eye's attention.
A welcome card on the left provides a brief summary of the what the site is about, and also invites visitors to add their own pun to the collection.

![](/images/wireframes-forms.png)

A basic form allows the user to input their own strings of text,
while the dropdown allows them to select from one of four possible categories; adjective, adverb, noun, or verb.
This was made a dropdown to help avoid confusion.

## Features

### Existing Features

    Accordion display of puns [READ]
        an interactive display of the site's repository of puns, that neatly allows users to view available content,
        while organising it in such a way as to not overburden the visual field.
    Navbar
        lists links to both the home page (display of puns), and the submit page.
    About Card
        gives brief description of site's purpose to new visitors, also encourages them to submit their own pun
    Individual pun page
        visitors can click on "view more" when a pun is expanded in the accordion to be brough to a separate page 
        with less visual clutter and a clearer breakdown of the components to the pun.
    Submit Page [CREATE]
        a simple form that allows users to add their own puns to the repository
    Edit Page [UPDATE]
        using the same form as the submit page, allows users to update and amend any existing puns
    Edit and Delete buttons [DELETE]
        visible on both the home page and individual pun pages, allows users access to either the edit page, or to
        delete the particular pun from the repository

### Features Left to Implement

    Error messages for the submission of incomplete forms
    Password protection to prevent rampant deletion, or hostile edits
    5-star rating system, allowing users to provide feedback for each pun
    Modal message asking users to confirm that they wish to delete a pun
    Filtering system to show sub-collections by category

### Technologies Used

    JQuery
        The project uses JQuery to simplify DOM manipulation.
    HTML
        Used to put a basic structure on the web pages
    CSS
        Used to customize formatting and stylistic choices
    Python
        Allows for greater generalization in generating pages, avoiding unnecessary duplication by instead using templates
    Bootstrap
        For styling, layout
    Materialize
        For styling purposes, and some simple functionality, specifically the accordion, and dropdown-selector
    
## Testing

Testing was caried out on multiple browsers, includin Chrome, Firefox and Explorer, at multiple resolutions to ensure that formatting remained consistent.
Links/buttons were tested to ensure they redirected to the correct pages.
Forms were tested to ensure that values were being correctly updated on mongoDB.

### Known Bugs
    no spacing between Welcome card and Pun accordion

### Fixed Bugs
    pun category dropdown does not display correctly on Edit page

## Deployment

This project is deployed on Heroku, and can be visited at the following url: 
    https://suburban-dictionary-project.herokuapp.com/

A development version was hosted on gitpod. 
The  associated mongoDB collection URI had to be stored in a file named "env.py" which was set to be ignored by github
so that I could push updates to github without also publically sharing a personal password.

On Heroku, this URI was stored in Config Vars of the Settings tab as env.py was still not getting pushed due to the git ignore I had set up.

## Credits
Aaron Sinnott, my mentor at Code Institute, for his advice during development

Josh Molloy, my brother, for providing an additional pair of eyes, and far too much patience