# milestone3b
Second attempt at Data Centric Development Project

In this project I hope to create a simple website called suburban dictionary 
This website will allow visitors to upload their own puns or play on words.
As is often the case with this kind of dad-jokery, these puns can be cringe-inducing;
and so users will also be able to makes changes or even simply delete uploads 
that they feel are of an (in)sufficient embarrassment quotient.

In this way I hope to demonstrate my ability to CRUD using a database of user-generated puns.

UX

For all paternal-types or paternal-at-heart, I hope to have created a space for uers to upload and peruse the best 
puns and play on words they can find. I'm using a simple, interactive layout, to help draw the eye's attention to one 
expression at a time while still displaying the other possible puns for users to view.

I also have several calls to action on the home screen for users to upload they're own turns of phrases, in the navbar
and in the "About" Card.

User Stories:

    As a fan of puns, I want to view others' puns, so that I can sprinkle them into my day-to-day conversations.
    As a pun-skeptic, I want to view others' puns, so that I can audibly groan and roll my eyes in disgust.
    As a particularly witty wordsmith, I want to upload my play on words, so that I can demonstrate my mastery of the English language.

--------------------------------------------------------------------------------------------------------------------
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.
Features
--------------------------------------------------------------------------------------------------------------------

Existing Features

    Accordion display of puns [READ]
        an interactive display of the site's repository of puns, that neatly allows users to view available content,
        while organising it in such a way as to not overburden the visual field.
    navbar
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

    ...

Features Left to Implement

    Error messages for the submission of incomplete forms
    Password protection to prevent rampant deletion, or hostile edits
    5-star rating system, allowing users to provide feedback for each pun

Technologies Used

    JQuery
        The project uses JQuery to simplify DOM manipulation.
    HTML
    CSS
    JavaScript
    Python
    Bootstrap
    Materialize
    
-------------------------------------------------------------------------------------------------------------------------
Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

    Contact form:
        Go to the "Contact Us" page
        Try to submit the empty form and verify that an error message about the required fields appears
        Try to submit the form with an invalid email address and verify that a relevant error message appears
        Try to submit the form with all inputs valid and verify that a success message appears.
-----------------------------------------------------------------------------------------------------------------------
Using Bootstrap and Materialize, the website has been designed to be responsive, and adapts to smaller resolutions with 
more appropiate layouts.

Known Bugs
    pun category dropdown does not display correctly on Edit page

--------------------------------------------------------------------------------------------------------------------------
Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

    Different values for environment variables (Heroku Config Vars)?
    Different configuration files?
    Separate git branch?
-------------------------------------------------------------------------------------------------------------------------