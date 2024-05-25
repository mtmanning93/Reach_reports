# REACH
### Condition reports from the mountains, written by climbers, for climbers.

![Overall site view across different devices](README_images/development/preview.png)

## Live Site
[Hosted on Heroku](https://reach-reports-e02886ddeda3.herokuapp.com/)

## Repository
[Github Repo](https://github.com/mtmanning93/Reach_reports)

## Introduction

Reach is a website where users have the ability to create and post condition reports from their climbing adventures and expeditions. Non-registered users have the ability to read reports and comments. Registered users have full CRUD functionality over their reports, along with extra features, such as commenting and liking other users' reports.

## Getting Started
To get started with deploying the project locally, visit this link below:

[Github Cloning](#github-cloning)

## Built With:
Django, Python, JavaScript, Bootstrap 5.2, CSS, HTML

### Includes:
Cloudinary, Crispy Forms

## Contents

- [REACH](#reach)
    - [Live Site](#live-site)
    - [Repository](#repository)
    - [Introduction](#introduction)
    - [Getting Started](#getting-started)
    - [Built With](#built-with)
    - [Design Thinking](#design-thinking)
        - [Problem ID](#problem-id)
        - [Problem Statement](#problem-statement)
        - [Brainstorm](#brainstorm)
        - [Site Goals](#site-goals)
    - [UX](#ux-user-experience-design)
        - [User Stories](#user-stories)
            - [Site Admin](#site-admin)
            - [User](#user)
            - [Registered User](#registered-user)
        - [Wireframe](#wireframe)
        - [Information Architecture](#information-architecture)
        - [Visual Design](#visual-design)
            - [Color Scheme](#color-scheme)
            - [Fonts](#fonts)
            - [Imagery](#imagery)
            - [Logo](#logo)
    - [Database ERD](#database-erd)
        - [User Model](#user-model)
        - [Comment Model](#comment-model)
        - [ImageFile Model](#imagefile-model)
        - [Report Model](#report-model)
    - [Development](#development)
        - [Agile Design](#agile-design)
            - [Github Isssues](#github-issues)
                - [Templates](#templates)
                - [Labels](#labels)
                - [User Story](#user-story)
                - [Bug Report](#bug-report)
                - [Feature Request](#feature-request)
            - [Product Backlog](#product-backlog)
            - [Iterations](#iterations)
            - [Kanban Board](#kanban-board)
    - [Features](#features)
        - [Current Features](#current-features)
            - [Navbar](#navbar)
            - [Footer](#footer)
            - [Home](#home)
            - [Reports](#reports)
            - [Reports Details](#report-details)
                - [Information](#information)
                - [Images](#images)
                - [Fatmap iFrame](#fatmap-iframe)
                - [Likes](#likes)
                - [Comments](#comments)
            - [Create Report](#create-report)
            - [Edit Report](#edit-report)
            - [Account Page](#account)
                - [Edit/ Delete Account Link](#edit-delete-account-link)
                - [Admin Site](#admin-site-staff-users-only)
                - [Edit/ Delete Report Links](#edit-delete-report-links)
            - [Update Account](#update-account)
            - [404/ 500 Errors](#404-500-errors)
            - [Reset Password](#reset-password)
            - [Login](#login)
            - [Logout](#logout)
            - [Signup](#signup)
        - [Future Features](#future-features)
        - [Defensive Design](#defensive-design)
    - [Technologies Used](#technologies-used)
        - [Django](#django)
        - [Python](#python)
        - [JavaScript](#javascript)
        - [CSS & Bootstrap](#css-&-bootstrap)
        - [Cloudinary](#cloudinary)
    - [Testing](README_testing.md)
    - [Bugs](#bugs)
        - [Resolved Bugs](#resolved)
        - [Unresolved Bugs](#unresolved-bugs)
    - [Deployment](#deployment)
        - [Github Cloning](#github-cloning)
        - [Cloudinary Deployment](#cloudinary-deployment)
        - [Elephant SQL Deployment](#elephantsql-deployment)
        - [Neon Deployment](#neon-deployment)
        - [Heroku Deployment](#heroku-deployment)
    - [Credits](#credits)
        - [Tools](#tools)
        - [Resources](#resources)
        - [Tutorials](#tutorials)

## Design Thinking

### Problem ID

The initial idea arose whilst reading a facebook group post. The group is called the ['Die 48 Schweizer 4000er'](https://www.facebook.com/groups/255829887155). In the post the user expressed their frustration, and having decision fatigue, due to the uncertainty of conditions across the alps on a weekend they wished to climb. They had asked where could they find more information.

Using the 5c's approach it became apparent that having a centralized place where users could read and create reports based on the conditions they had experienced, would solve the problem.

### Problem Statement

> "As a passionate climber, I am trying to climb on my free days, but I'm unsure of the mountain conditions and can't decide whats the best option. This makes me frustrated. How do I find out up to date conditions?"

### Brainstorm

As a passionate alpinist, it was possible to gather a group of climbers and hold a brainstorming session. The sessions provided insight into what was important to the target audience.

There were 3 key takeaways from the brainstorming session:
    
1. Images Are Important
    - An image says a thousand words, with experience you can tell a lot from an image.
2. Comments
    - A discussion on each report would provide even further information for users.
    - Other user input on each report would create more in depth reports.
3. Key Information
    - Every report should be simple but provide enough information in order to give an insight.
    - Key information such as the number of people and an overall grade should be given on all reports.

### Site Goals

#### - User Goals

The user would like the ability to read and post condition updates from recent climbs they have done, or want to do. Providing real and current information from the mountains.

#### - Owners Goals

The goal is to create a discussion and library of up to date condition reports to enable climbers to make easier decisions and ultimately become more successful.

[⏫ contents](#contents)

## UX / User Experience Design

### User Stories
----------------
Example user stories which have affected the overall design and functionailty of the project.

#### - Site Admin
> "As a site admin I can create, read, update, and delete reports so that I can manage the site content"
>
> "As a site admin I can approve or disapprove comments so that I can keep the content specific and non-offensive"

#### - User

> "As a user I can easily locate each page of the site so that navigation is smooth and consistent throughout the site"
>
> "As a user I can view a paginated list of condition reports so that I can select one to read"
>
> "As a user I can select a report from the reports list so that I can read its content"
>
> "As a user I can view comments on each report so that I can see the conversation/ questions"
>
> "As a user I can register for an account so that I can access the functionality to create, comment and like reports myself"

#### - Registered User

> "As a registered user I can create my own report so that I can interact with other climbers"
>
> "As a registered user I can view a list of the reports I have written so that I can select between them to read, edit or delete them"
>
> "As a registered user I can comment on reports so that discuss the report further and join the community"
>
> "As a registered user I can login so that I can take advantage of the registered user functions and view my account"
>
> "As a logged in in user I can log out so that I can protect my account"
>
> "As a logged in  user I can like or unlike posts so that I can show my appreciation towards good reports"
>
> "As a site admin/ registered user I can add images to reports so that the report is more informative"

### Wireframe
-------------

To aid in the design of the UI I created a wireframe. My preference was to create a large wireframe incorporating all pages, to visualise the flow of the website as well as the design. I provided wireframes for, desktop/ laptop and mobile devices, along with the deletion confirmation modals.

Line Key:\
**Green** - Creation or Addition\
**Orange** - Action\
**Red** - Deletion

![Full wireframe and flow of Reach website](README_images/development/wirefram_full.png)

### Information Architecture
----------------------------

When building the project's wireframe it was important to take into consideration the positioning of elements. Across the entire site, the user will find the consistent layout of a navbar and footer with the main content sandwiched between. Key aspects of the information architecture, found throughout the site are:

- **Site Wide Navbar:**\
The navbar offers the user links to various pages of the site, such as "Home" and "Reports", the consistency of this navigation aids the user in moving easily between different parts of the site, contributing to a better user experience.

- **Branding:**\
Within the navbar is a large brand logo, this allows users to quickly identify the website and helps establish a visual identity.

- **User Authentication:**\
Depending on whether a user is authenticated or not, the navigation options change to "Account" and "Logout" or "Login" and "Signup." This provides a clear path to the users account management.

- **Footer:**\
The footer contains relevant links, including navigation links, social media links, and a contact email. Footers often serve as a secondary navigation or quick access to important sections and resources. Also the footer includes a short safety message to the user helping to connect at a human level.

- **Report Details:**\
The template displays various details about the report. This organized presentation of the reports details allows users to quickly understand key aspects of the report, without having to read large chunks of information.

- **Images and Map:**\
"A picture tells a thousand words". These visual elements enhance the user's understanding of the climbing experience.

### Visual Design
-----------------

#### Color Scheme

The color scheme was chosen to effectively communicate the adventurous and trustworthy aspects of mountaineers and climbers, and therefore the website. The use of blues, combined with the 'bootstrap-light' theme (#F8F9FA) and black text, allows for strong contrast throughout the site. This was very important within the report's details so users can easily read the information provided. The use of white space also aligns well with the outdoor and exploratory theme of the website.

The main colors used throughout the site were:

![Color palette](README_images/development/color-palette.png)

#### Fonts

I used 2 fonts throughout the site, in different weights, to display hierarchy and guide users. The fonts were chosen due to the versatility and clarity. The two fonts used were; **LATO** for almost all elements, and **Poppins** for stand out headings or alternate text. In the example below the blue text is 'Poppins' and the black is 'Lato'.

![An example use of fonts](README_images/development/fonts.png)

#### Imagery

Across the site, I used just nine images. Seven of these are shown as the 'Home' page's main header image. These images were chosen as they cover a wide range of mountainous activities and all convey the main them of the site, adventure. These header images were taken from [Unsplash](https://unsplash.com/) a loyalty free high-quality image resource.

![Header Images](README_images/development/header_images.png)

#### Logo

The site's logo is a simple mountain emblem with bold and capitalized REACH after it. This is immediately visible to a user and allows the user to quickly identify the site, the colors are in keeping with the site's theme.

![Reach site logo](README_images/development/logo.png)

[⏫ contents](#contents)

## Database ERD

I created an ERD to aid in the creation of the database, below is a screenshot to help visualize the models. Below the image are descriptions for each model.

![Rearch ERD (Database Model)](README_images/development/database_model.png)

### User Model

The user object is created on registration for each user. Within the project I decided to use Django's built-in User model. Due to the simplicity of the information required for each user in this project, the Django User model was a way to simplify the build.

Each user has a one-to-many relationship with both reports and comments, enabling users to create reports and comments as much as they wish.

### Comment Model

The comments model contains information about the user and of course the content. This is relevant when rendering each comment object on the reports details pages. Additionally the 'approved' field is used from inside the admin site, allowing staff to disapprove comments, removing them from the users view.

It has a many-to-one relationship with the user and report models.

### ImageFile Model

A simple model was created to store the report images uploaded when creating a report. The images are stored using Cloudinary, therefore the obvious choice was a CloudinaryField for the actual image file. The images have a many-to-one relationship with the reports, allowing users to add multiple images per report.

### Report Model

The main model in the database, this holds each report objects information, all other models are connected to this model. When creating the ERD the fields to be included were chosen by their use to a user reading the report. The addition of 'required' fields means that a minimum standardized report will be viewable across the site. To create a better user experience when creating and editing forms I added choices to simplify the report creation process. 

- **Success:**
    The success choices allow a user to quickly show if they reached their goal or not, a simple yes/no selection.
- **Grade Choices:**
    These are used when a user specifies the overall condition grade of the route. Were the conditions 'good' or just 'bad'. The four choices make the explanation much simpler.
- **Category Choices:**
    Each report can be placed into a category of activity type, from ice-climbing to hiking. A range of mountain activites can be chosen, and if its not available a selection of 'other' is available.
- **Status:**
    The status selection is simplified by a yes/no choice, 'is the report published or not'. If the report is published it will be displayed in the list of reports for the site, if not it remains only visible to the user in their account.

[⏫ contents](#contents)

## Development

### Agile Design
----------------

Due to the size of the Reach project and the many different parts. It was crucial to adopt an Agile methodology. In a project with many different functionalities, it can be easy to move between the tasks, forgetting parts or even leaving them unfinished. With the Agile approach, I was able to identify the key components which would build the project, and separate them into smaller more manageable tasks. Always carrying manual testing to ensure each component was working as expected before moving on to the next task. It enables regular reflection on the project and attention to each technicality.

### Github Issues

#### Templates

Throughout the build, I used three templates:
- [User Story](https://github.com/mtmanning93/Reach_reports/blob/main/.github/ISSUE_TEMPLATE/reach-user-story.md)
- [Bug Report](https://github.com/mtmanning93/Reach_reports/blob/main/.github/ISSUE_TEMPLATE/reach-bug-report.md)
- [Feature Request](https://github.com/mtmanning93/Reach_reports/blob/main/.github/ISSUE_TEMPLATE/reach-feature-request-form.md)

#### Labels

When beginning the process of creating the user stories I introduced 4 labels using the MoSCoW principle. The labels were used when assessing each iteration, meaning they were not static from the beginning, they were reassigned when necessary to adjust the level of importance, of the user story, throughout the overall project. These labels were:
- Must Have
- Should Have
- Could Have
- Wont have

As the project grew it was important to introduce more labels to assign in arrising situations. The additional labels were:
- Bug
- Improvement
- Feature Request

[Project labels](https://github.com/mtmanning93/Reach_reports/labels)

#### User Story

The first template created was the user story template. Every user story includes **Acceptance Criteria** and **Tasks**. The purpose of the user story was to begin the building process and help decide what features would be potentially included.

* **Acceptance Criteria**:
The acceptance criteria for a user story gives a clear indication of what the expected outcome for the user is, it contains no technical information with regards to completing the user story.

* **Tasks**:
Once the user story was created and the acceptance criteria was assigned, the next step was to break it down into smaller tasks, all of which achievable in a day or less. I created the tasks as a checkable list, making it visually clear, whilst developing the project, what the next step was.

[Issues list](https://github.com/mtmanning93/Reach_reports/issues?q=is%3Aissue+is%3Aclosed)

[Example user story](https://github.com/mtmanning93/Reach_reports/issues/16)

#### Bug Report

The next issue template created was the bug report. As the project grew I was constantly carrying out manual testing to check the functionailty of the component being built. Whilst doing so, occassionally, I would notice bugs in other components of the site. In order to keep the flow of the agile method I would create bug reports and add them to the list of issues. The bug reports were then addressed when the priority to do so was high, for example, when labeled a 'Must Have' within the current iteration.

If it was a bug within the current user story task I would assign the label 'Bug' to it.

[Example of assigning the 'Bug' label](https://github.com/mtmanning93/Reach_reports/issues/22)
 
[Example full Bug Report](https://github.com/mtmanning93/Reach_reports/issues/32)

#### Feature Request

The final template created was a feature request. Whilst building the project and showing others a new component, a new idea for a feature would come to mind. Some ideas would be a great addition to the current deployed version of the site whereas others would be great in a later version. All feature requests were labeled with the 'Feature Request' label and/or 'Improvement' depending on the implementation of the idea.

[Example Feature Request](https://github.com/mtmanning93/Reach_reports/issues/29)

### Product Backlog

When a new issue was created, no matter which the template was used, it was added to the Reach Product Backlog. In here it was prioritized and labels were assigned or reassigned accordingly. This process or reassigning labels continued throughout the build as the importance of certain components or bugs would change. As iterations were created the issues would be moved from the product backlog and into the relevant iteration.

[Reach Product Backlog](https://github.com/mtmanning93/Reach_reports/milestone/1)

### Iterations

In order to manage the complexity of the project I implemented the use of iterations using the issue milestones in GitHub. The use of iterations meant I could breakdown the project and provide incremental delivery. This would help to provide clear feeback on progress throughout.

Each iteration was created with a due date. This was to allow for adaptations throughout. An example would be that if a user story was not complete before the iterations due date it was returned to the product backlog for review of its importance, then reprioritized accordingly.

A great effect that working in iterations has is it maintains a steady pace of work, keeps momentum, and keeps the development team motivated. This is due to the constant assessment of progress.

[Project iterations](https://github.com/mtmanning93/Reach_reports/milestones?state=closed)

### Kanban Board

To help with the visualization of tasks in the project I implemented a Kanban board, using GitHub projects. The board was seperated into 3 columns; To Do, In Progress, and Done. All issues in the backlog were automatically added to the Kanban 'To Do' column. Throughout the build, I would take all issues from the current iteration into the 'In Progress' column. Once all tasks were completed in the issue I would move the issue over to the 'Done' column. 

When possible I would close an issue from the terminal using the `close #10` command from inside a commit message. This would automatically move the issue into the 'Done' column.

[Reach Kanban Board](https://github.com/users/mtmanning93/projects/7)

[⏫ contents](#contents)

## Features

## Current Features

### Navbar
----------
The navbar is simple yet functional, it contains a large logo which makes the site identifiable immediately, the logo is clickable bringing the user to the 'home' page. The nav links are easily distinguishable. 

When an unregistered user is on the site the nav link options will simply be 'home', 'reports', 'login', and 'signup'. The signup is highlighted as that is what the site wants from an unregistered user.

If a logged in, registered user is viewing the navbar they will see their username as a dropdown link. Once clicked the dropdown menu reveals links to 'account' and logout. In addition, if the registered user is a 'staff' member they have access to an extra link 'Admin'. This extra link provides access to the Django admin panel.

<details>
<summary>Unregistered User Navbar Screenshots</summary>

![Unregistered user navbar](README_images/features/base/nav_unreg_m.png)
![Unregistered user navbar mobile](README_images/features/base/nav_unreg.png)
</details>

<details>
<summary>Registered User Navbar Screenshots</summary>

![Registered user navbar](README_images/features/base/navbar.png)
![Registered user navbar mobile](README_images/features/base/navbar_m.png)
</details>

### Footer
----------
The footer again is simple, providing extra navigation links, social links, a friendly safety message and the contact email address. The navigation links are corresponding to the links in the navbar (updating depending on the users role). The social links open in new tabs when clicked, and all links highlight on hover. The footer collapses nicely on itself on smaller screens.

<details>
<summary>Footer Screenshots</summary>

![Footer](README_images/features/base/footer.png)
![Footer mobile](README_images/features/base/footer_m.png)
</details>

### Home
--------
The 'home' page has a bold and simple design, using large landscape imagery. The images are of different mountain activites, relating to the target audience, and the sites image; motivating and adventurous. The images are selected at random each time the page loads giving users a fun experience. Over the images is an inspiring mountain quote which also is chosen at random on page load. More functionality is provided by 2 large buttons. The buttons link to the 'reports' list page and to the 'signup' page for unregistered users, whilst linking to the 'create report' page for registered users.

<details>
<summary>Home Page Screenshots</summary>

![Home](README_images/features/home/home.png)
</details>
<details>
<summary>Home Page Unregistered User Screenshots</summary>

![Home for unregistered user](README_images/features/home/home_unreg.png)
</details>

### Reports
-----------
The reports page is the main reports list. Here users will find all reports. They are able to select a report from the list, filter the list by 'overall condition grade' or 'activity type'. There is also a 'create report' button for ease of access.

Each report object in the list is constructed of key information to enable a user to decide if they wish to read further or not. Each one is implemented as a large clickable button making selection easy.

<details>
<summary>Reports Page Screenshots</summary>

![Reports](README_images/features/reports/reports.png)
![Reports mobile](README_images/features/reports/reports_m.png)
![Filters](README_images/features/reports/filters.png)
![Report Object](README_images/features/reports/report_list_item.png)
</details>

### Report Details
------------------

The 'route name' and 'activity start date' are clearly visible in bold at the top of the page, along with a return button that takes users back to the reports list page.

<details>
<summary>Report Details Screenshots</summary>

![Report details](README_images/features/report_details/report_details.png)
![Report details mobile](README_images/features/report_details/report_details_m.png)
</details>

#### Information

The reports detail page shows the relevant information from each report object. After the design thinking stage of the project, it was clear which pieces of information were valuable to every report. All required fields in the 'Create Report Form' are shown whilst the fields which aren't required are only shown when a value is given.

<details>
<summary>Report Information Screenshot</summary>

![Report details information](README_images/features/report_details/report_info.png)
</details>

#### Images

The images section displays all images related to the report separately in a thumbnail. If clicked they open a modal with an enlarged version of the image inside. Within the modal users can return via one of the 'x' or 'close' buttons or alternatively click outside the modal.

<details>
<summary>Report Images and Modal Screenshots</summary>

![Report details images](README_images/features/report_details/report_details_images.png)
![Report details image modal](README_images/features/report_details/image_modal.png)
</details>

#### Fatmap Iframe

Users have the option to include a [Fatmap.com](https://fatmap.com/adventures/@46.5668314,8.0031898,6596.4744211,-20.0370673,139.3104485,3570.3534546,satellite) url in the report. If they have included one it will appear in the report under the images section. The map is fully interactive, user can move the 3D map using their mouse. Alternatively, they can click the map to go to the official site for an enlarged version.

<details>
<summary>iFrame Screenshot</summary>

![Fatmap iframe](README_images/features/report_details/fatmap.png)
</details>

#### Likes

Each report has a 'like' button. A registered user can click it to like a report. The same user can click the same button then unlike the report. The thumbs-up icon changes color when liked. Providing user feedback the likes counter next to it will also increment or decrement accordingly.

If an unregistered user attempts to click the like button a tooltip shows suggesting them to register in order to like and comment.

<details>
<summary>Like Section Screenshots</summary>

![Liked report](README_images/features/report_details/liked.png)
![Unliked report](README_images/features/report_details/unliked.png)
</details>

#### Comments

Finally, every report has a comment section, all users can read comments. However only accessible to registered users is the ability to post a comment. Additionally, the user can delete only their own comments from the site using the 'x' button. Of course this action requires confirmation from the modal. Each comment posted includes the author's username, content, and date created.

<details>
<summary>Comment Section Screenshots</summary>

![Comments section registered user](README_images/features/report_details/comments.png)
</details>
<details>
<summary>Comment Section Unregistered User Screenshots</summary>

![Comments section unregistered user](README_images/features/report_details/comments_unreg.png)
</details>

### Create Report
-----------------

The main form on the site is found on the 'Create Report' page accessible only as a logged in, registered user. In this form users can provide the information to create their own reports for the site. The form has a minimum requirement, meaning a report cant be created without these pieces of information. This creates a uniformed report site-wide, giving regular users easier reading and faster understanding of each condition report. 

Optionally users can add images and a fatmap url to enhance the report's use. Users are however limited to 12 images per report, as they are made aware of in the images section.

If a user enters too little or wrong information the report will not be saved or posted to the site and they will be made visually aware of the issues in the report creation.

To submit the form they must click the large green button which is carried throughout the site for creative actions.

<details>
<summary>Create Report Form Screenshots</summary>

![Create report form](README_images/features/create_edit/create_form.png)
![Create report form mobile](README_images/features/create_edit/create_form_m.png)
![Create report form errors](README_images/features/create_edit/errors.png)
</details>

### Edit Report
---------------

The edit report page inherits most of its functionality and features from the create report page. The main feature and difference with this page is users are able to delete and add new images to their report. The logic ensures that the total number of images is never more than 12. If the user attempts to have more than 12 even through adding and deleting at the same time the form is considered invalid. If the form is considered invalid no action happens on the images.

To delete images from the report a user just needs to check the box underneath the image, then when submitting the form the selected images will be deleted.

<details>
<summary>Edit Report Screenshots</summary>

![Edit report form image deletion and addition](README_images/features/create_edit/edit_report_images.png)
![Edit report form](README_images/features/create_edit/edit_report.png)
</details>

### Account
-----------

The account page is the where the user can manage their account details and reports. There a large, centered, profile box contiaining the users personal information and no of written reports statistic. Included are 2 links to ['Edit'](#edit-delete-account-link) and ['Delete'](#edit-delete-account-link) their account.

Beneath is the list of the reports written by the user. Each report in the list has similar information to the items on [reports](#reports) page, however, in the account, the user can ['Edit'](#edit-report-link) or ['Delete'](#delete-report-link) their reports via links added to the list item.

<details>
<summary>Account Full Screenshots</summary>

![Account page](README_images/features/account/account.png)
![Account page mobile](README_images/features/account/account_m.png)
</details>

#### Edit/ Delete Account Link

Within the personal details the user can find two links, appropriately colored. The blue 'Edit Account' link will lead the user to the ['Update Account'](#update-account) page. The 'Delete Account' link will open a confirmation modal. Inside the modal will be a list of statistics personal to each user. The statistics tell the user how many reports they've created, images uploaded, and comments left. If confirmed the user's account is deleted and they are redirected to the 'home' page.

<details>
<summary>Account Options Screenshots</summary>

![Account information](README_images/features/account/personal_info.png)
![Delete account modal](README_images/features/account/delete_account.png)
</details>

#### Admin Site (Staff Users Only)

If a user has 'staff' permission they will have an extra button in the personal information section, the button links them to the site's admin page. From here they have full CRUD functionality over users, reports, and images. They can block users and remove comments and likes from reports.

Due to the current scope of the project and time constraints, the current version uses the built-in Django admin site, only accessible from inside a staff account. A future improvement could be a custom admin panel.

<details>
<summary>Admin Site Screenshot</summary>

![Admin button](README_images/features/account/admin_button.png)
</details>

#### Edit/ Delete Report Links

On each report item in the user's personal reports list is an 'Edit' and a 'Delete' icon. If a user chooses to edit they are redirected to the 'edit report' page, whilst if they select 'delete' the confirm deletion modal appears, if confirmed the report is deleted and they're returned to their account page. For clarity, both icons have a tooltip to describe their functionality.

<details>
<summary>Report Management Screenshot</summary>

![Edit/ delete reports links](README_images/features/account/report_links.png)
</details>

### Update Account
------------------

When a user chooses to edit their account from inside the [account](#account) page, they are directed to the 'update account' page. The page contains a simple form where users can update their usernames. Also available to users is an account managements section containing the option to change their password via the ['Reset Account Password' button](#reset-password), and the ['Manage email accounts' button](#manage-email-accounts).

<details>
<summary>Update Account Screenshot</summary>

![Update account page](README_images/features/account/update_account.png)
</details>

### Manage Email Accounts
-------------------------

On this page only, accessible from the user account page, users are able to add emails to their account, re-send verification emails and choose their primary email address. The primary email address is then displayed in their personal information section on the accounts page.

<details>
<summary>Manage Email Accounts Screenshot</summary>

![Manage emails](README_images/features/account/manage_emails.png)
</details>

### 404/ 500 Errors
-------------------

Custom error handlers with a simple back-to-home button provide a better user experience.

<details>
<summary>Error Page Screenshot</summary>

![Error pages](README_images/features/base/404.png)
</details>

### Reset Password
------------------

Users are able to reset their password in case they have forgotten it prior to login or from inside the ['Update Account'](#update-account) page. The user is taken through the steps in order to change their password, they must provide an email in order to recieve a momentary link (3 days). When clicked they're able to input a new password. Once the steps are complete the user is directed to the Login page.

<details>
<summary>Password Reset Screenshots</summary>

![Forgot password link](README_images/features/password/forgot_password.png)
![Password reset step 1](README_images/features/password/enter_email.png)
![Edit report form](README_images/features/password/email_sent.png)
![Edit report form](README_images/features/password/email.png)
![Edit report form](README_images/features/password/change_password.png)
</details>

### Login
---------

When creating the site Django automatically sets the login configured to username and password although I preferred the email and password approach as it ensures users have a working email address for the ['Password Reset'](#reset-password) functions. Now when users log in they must enter an email and password, a username is not required. Also, non-registered users can find a link to the ['Signup'](#signup) page underneath the login form in case they navigated wrongly.

<details>
<summary>Login Screenshot</summary>

![Login page](README_images/features/account/login.png)
</details>

### Logout
----------

Users need to logout in order t protect their accounts. They can do this from inside the navbar by clicking their username, then the 'logout' link in the dropdown menu. Of course, users must first confirm their choice on the 'Logout' confirmation page. If confirmed they are redirected to the 'home' page.

<details>
<summary>Logout Screenshot</summary>

![Logout page](README_images/features/account/logout.png)
</details>

### Signup
----------

Non-registered users can navigate to the 'Signup' page. Here they must fill out the forms required fields in order to create an account. I decided to implement email verification for the project. This means when users click signup they are sent a verification link in an email, this verifies the user's email address. When the email link is clicked the user is taken to the login page.

Additionally, if the user has already registered an account with the same username the relevant error message is shown and the user must enter a different username.

<details>
<summary>Signup Screenshots</summary>

![Verification Sent](README_images/features/account/verification_sent.png)
![Signup](README_images/features/account/signup.png)
</details>

[⏫ contents](#contents)

## Future Features

Whilst building the project new ideas perfect for future releases would come to mind. To stay productive and on track with the current build, I created a [Feature Request Form](#feature-request) using GitHub issues. This meant I could save the ideas for later. Their are still some features in the [Product Backlog](#product-backlog) that would be a great addition to the site at a later point. These features are now marked as ['Won't Do'](#labels) as for this release they aren't of high priority.

[Link To Current 'Wont Dos'](https://github.com/mtmanning93/Reach_reports/issues?q=is%3Aissue+label%3A%22Wont+Have%22+is%3Aopen)

[Link To Left Feature Requests](https://github.com/mtmanning93/Reach_reports/issues?q=is%3Aopen+is%3Aissue+label%3A%22Feature+Request%22)

[⏫ contents](#contents)

## Defensive Design

When in production it was clear that defenses would be needed to prevent unauthorised users from accessing views they shouldn't, for exmple the delete_report, edit_report and toggle_report views. Prior to the custom decorator implementation a unauthorized user had the ability to force their way into these views with any `report.pk` by typing, for example:

    /reports/edit_report/3/ 
_(or any report.pk not owned by the logged in user)_

Here the built iin `@login_required` decorator wouldn't work if the user was logged in but trying to access another users report object. After some deliberation and research, my mentor, Jubril Akolade, told me that a custom decorator checking who owns the report would be a way to control this. He provided an in depth example of how this might work, allowing me to implement it specifically to the site.

The decorator `@user_owns_report` was created to check if the user owns the report before accessing it, if the user does not own the report theyre redirected to the 'home' page. The custom decorator can be found on _lines 16-41 or reports/views.py_.

    def user_owns_report(view_func):
        """
        Decorator to check if the requested report to edit or delete is owned
        by the current user. Applied to:
        - delete_report
        - toggle_report
        - edit_report
        """
        def _wrapped_view(request, *args, **kwargs):
            """
            Logic to check ownership.

            If 'True' the view is accessed.

            If 'False' (the user does not own the report) they are redirected
            to the home page.
            """
            report = get_object_or_404(Report, pk=kwargs['pk'])

            if report.author == request.user:
                return view_func(request, *args, **kwargs)

            else:
                return redirect('home')

        return _wrapped_view

[⏫ contents](#contents)

## Technologies Used

### Django:

Django was used as the core framework during this project, its documentation is second to none and it provides the user with a batteries-included framework making the development of larger-scale sites faster.

[Full Django documentation](https://docs.djangoproject.com/en/3.2/)

#### `django-allauth`
I used Django-allauth django add-on in the project, as it provides a set of views, templates, and functionality that integrate with any Django project to handle user authentication, registration, and password management. Aiding in the speed of the development process.

To install allauth in the command line:

    pip install django-allauth

Next, add to your settings:

    INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    ]

[Link to allauth docs](https://django-allauth.readthedocs.io/en/latest/)

### Python:

I used python for the main logic and functionality of the site, within python I used other packages.

#### `Crispy Forms`

Crispy forms allow your Django forms to be styled with Bootstrap. As my project was using Bootstrap already it made sense to have a uniform styling.

To install crispy-forms in the command line:

    pip install django-crispy-forms

Next, add to your settings:

    INSTALLED_APPS = [
        'crispy_forms',
    ]

    CRISPY_TEMPLATE_PACK = 'bootstrap5'

[Crispy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/)

#### `Coverage`

Coverage allowed me to visually check how much of my Python code was tested in my unit tests. It provides reports and HTML documents to check which lines need to be tested.

To install crispy-forms in the command line:

    pip install coverage

Then to run coverage in the command line:

    coverage run --source=app_name manage.py test
    coverage report
    coverage html
    python3 -m http.server

[Coverage Docs](https://pypi.org/project/coverage/)

### JavaScript

During the build very little javascript was necessary, this was mostly due to the use of `Bootstrap 5.2` which includes a large amount of built-in javascript functionality such as tooltips, navbars, and modals.

In order to include Bootstraps JavScript functionality include this script tag:

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous">
    </script>

### CSS & Bootstrap

As mentioned above `Bootstrap 5.2` was used heavily in this project to provide styling and some JavaScript functionality. The beauty of Bootstrap is it also aids in the responsiveness of the site. Given clear breakpoints to work from. In the instance of XS screens I needto create a new breakpoint myself but the use of `Bootstrap` keeps custom CSS minimal.

In order to include Bootstrap5 include this CDN link:

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

[Bootstrap 5.2 docs](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

### Cloudinary

The primary use of Cloudinary in this project was to upload and destroy stored images. Of course, with a number of users storage would quickly fill up therefore it was important to limit the number of images a user can add to each report. Users can add 12 images to a report. Even within the edit report where users can add and delete images at the same time, it is only possible to have a total of 12 images connected to the report object.

Once set up you must import Cloudinary in your file:

    import cloudinary
    or
    from cloudinary.models import CloudinaryField

I also used Cloudinary in my ImageFile model using:

    image_file = CloudinaryField('image', default='placeholder')

[Cloudinary Docs](https://cloudinary.com/documentation)

[⏫ contents](#contents)

## Bugs

When a bug is identified I was able to raise an issue in GitHub using the [Bug Report Template](#bug-report). As I was building the project I would identify a bug but in order to keep productive I would create a report in order to focus on it at a later time.

[Resolved Bugs](https://github.com/mtmanning93/Reach_reports/issues?q=is%3Aissue+is%3Aclosed+label%3ABug)

### Unresolved Bugs
-------------------

[Unresolved Bug](https://github.com/mtmanning93/Reach_reports/issues?q=is%3Aopen+is%3Aissue+label%3ABug)

When designing the project, even as early as the brainstorming session, it was clear that a [Fatmap](https://fatmap.com/adventures) iframe would be a great addition to the reports. It would provide a wealth of clarity for users regarding the route. Whilst implementing the iframe, and embedding it within a report details page, it would show numerous errors and warnings in the console. Through research, I found that this was unrelated to my project but the errors were actually stemming from the JavaScript in the iframe itself.

I attempted to contact 'fatmap.com' and 'datahappy.co' but neither responded to the issue I had raised.

![Errors with Fatmap iframe](README_images/testing/iframe_errors.png)

[⏫ contents](#contents)

## Deployment

### Github Cloning
------------------

To clone this project from its [GitHub repository](https://github.com/mtmanning93/Reach_reports), follow the steps below:

**1. Navigate to the Reach-reports repository, and click the green 'code' button.**

![Clone button in repo](README_images/deployment/clone.png)

**2. Once clicked, within the dropdown, copy the clone URL.**

![Clone url](README_images/deployment/clone_url.png)

**3. In your local IDE open your Git terminal**

**4. Change your working directory to your preferred location.**

**5. Next type the following command, the 'copied URL' is the URL taken form the Github repo.**

    git clone https://github.com/mtmanning93/Reach_reports

**6. Hit Enter to create the cloned repository.**

**7. Create an `env.py` file. Here will be where you hold the app's environment variables, in order to run the app successfully you will require the following variables.**

    import os

    os.environ["DATABASE_URL"] = "get from your SQL provider"
    os.environ["SECRET_KEY"] = "a secret key of your choice"
    os.environ["CLOUDINARY_URL"] = "get from cloudinary dashboard"
    os.environ["GMAIL_KEY"] = "key generated by gmail"
    os.environ["GMAIL_ACC"] = "email account for sending emails"
    os.environ["EMAIL_HOST"] = "email service provider"

In order to find the above variables you can follow the steps below to set up:
- [Elephant SQL](#elephantsql-deployment)
- [Cloudinary](#cloudinary-deployment)

**8. IMPORTANT! List the following files in your .gitignore file to prevent any private information from being public.**

    annotated-types==0.5.0
    asgiref==3.7.2
    cloudinary==1.33.0
    coverage==7.2.7
    crispy-bootstrap5==0.7
    dj-database-url==0.5.0
    dj3-cloudinary-storage==0.0.6
    Django==3.2.20
    django-allauth==0.54.0
    django-crispy-forms==2.0
    django-summernote==0.8.20.0
    gunicorn==20.1.0
    oauthlib==3.2.2
    psycopg2==2.9.6
    pydantic==2.0.3
    pydantic_core==2.3.0
    PyJWT==2.7.0
    python3-openid==3.2.0
    pytz==2023.3
    requests-oauthlib==1.3.1
    sqlparse==0.4.4
    urllib3==1.26.16

**9. Install all requirements using the following terminal command.**

    pip3 install requirements.txt

**10. Next, to perform database migrations, you can use the following command.**

    python manage.py migrate

**11. Create a new Django superuser. Type the command below and follow the in-terminal prompts to set up.**

    python manage.py createsuperuser

**12. Lastly, run the app using the below command.**

    python manage.py runserver

[⏫ contents](#contents)

### Cloudinary Deployment
-------------------------
I used Cloudinary in the project to store all media files, it's a really easy setup. To do so follow these steps:

**1. Navigate to the Cloudinary website and register or login.**

![Cloudinary landing page](README_images/deployment/cloudinary_site.png)

**2. Once the login or registration is complete, navigate to the 'Dashboard' page.**

![Dashboard button](README_images/deployment/cloudinary_dash.png)

**3. After reaching the dashboard you will find all relevant credentials needed to set up the project with your cloudinary.**

![Cloudinary credentials](README_images/deployment/cloudinary_creds.png)

[⏫ contents](#contents)

### ElephantSQL Deployment
---------------------------
Originally for this project, ElephantSQL was used which uses PostgreSQL databases. However ElephantSQL will reach end of life early 2025, therfore the databases were migrated to Neon, see ['Neon Deployment'](#neon-deployment) for more. In case of necessity, in order to set up ElephantSQL follow these steps:

**1. Create an account or log in to your ElephantSQL dashboard and click the green 'Create New Instance' Button.**

![ElephantSQL dashboard](README_images/deployment/elephant_sql_dash.png)

**2. Next setup the instance plan, when the form is complete click 'Select Region'.**

Generally, the title here is the project title. For my project, I selected the 'Tiny Turtle (Free)' plan and left the tags field blank.

![ElephantSQL plan setup](README_images/deployment/elephant_setup.png)

**3. Select the data center closest to you from the dropdown list, when selected click 'Review'.**

![Select region](README_images/deployment/elephant_region.png)

**4. Check the details are correct and click the green 'Create Instance' button.**

![Review details](README_images/deployment/elephant_review.png)

**5. Return to the dashboard and select the new instance just created by clicking on its name.**

![Select new instance](README_images/deployment/elephant_select_instance.png)

**6. This will display all the necessary credentials to connect this project to your database.**

![Instance details](README_images/deployment/elephant_details.png)

[⏫ contents](#contents)

### Neon Deployment
-------------------
Due to ElephantSQL end of life, the project database was migrated over to [Neon](https://console.neon.tech/realms/prod-realm/protocol/openid-connect/auth?client_id=neon-console&redirect_uri=https%3A%2F%2Fconsole.neon.tech%2Fauth%2Fkeycloak%2Fcallback&response_type=code&scope=openid+profile+email&state=0tRwwIsTryvbbFvrKBn7vA%3D%3D%2C%2C%2C).

I order to use Neon to host your PostgreSQL databases follow these steps:

**1. Navigate to the Neon website and signup.**

![Neon signup](README_images/deployment/neon_login.png)

**2. Once signed up create a project by providing a project name, database name, and selecting the region closest to you. Click create project.**

![Create Project](README_images/deployment/neon_create.png)

**3. Next in the dashboard, locate the 'connection string'. This string will be used as the DATABASE_URL during deployment**

![Connection String](README_images/deployment/neon_dashboard.png)

[⏫ contents](#contents)

### Heroku Deployment
---------------------
The project was deployed using Heroku. Heroku simplifies the deployment process. With a few commands, you can deploy your application without the need to configure servers, networking, or infrastructure. I chose to deploy my project early on to avoid any nasty surprises at the end of the build, this is a great method and reduces stress as the project is already deployed throughout.

In order to deploy my project to Heroku I followed these 10 steps:

**1. Navigate to the Heroku dashboard. Click "New" and select "Create new app".**

![Create new app](README_images/deployment/heroku_new.png)

**2. Create an app name and select a region closest to you.**

![Giving the app a name](README_images/deployment/app_name.png)

**3. Next, navigate to the 'Settings' tab, and select 'Reveal Config Vars'.**

![Settings tab](README_images/deployment/settings.png)
![Config Vars](README_images/deployment/reveal.png)

**4. Add necessary 'Config Vars'.**

For this project, you will need the following 'Config Vars':

- CLOUDINARY_URL: Get from Cloudinary.
- DATABASE_URL: Get from your SQL provider.
- EMAIL_HOST: Get from your email provider.
- GMAIL_ACC: Get from your email provider.
- GMAIL_KEY: Get from your email provider.
- PORT: Set to 8000.
- SECRET_KEY: Django project secret key, generated by your Django project.
- DISABLE_COLLECTSTATIC: Set to 0.

![Project necessary Config Vars](README_images/deployment/config_vars.png)

**5. Navigate to the 'Deploy' tab.**

![Deploy tab](README_images/deployment/deploy.png)

**6. Scroll to the 'Deployment Methods' section and select 'Connect to GitHub'.**

![Step one connect to GitHub](README_images/deployment/github_connect.png)

**7. Once connected to GitHub, search for the repository in the 'Connect to GitHub' section, and click 'Connect'.**

![Step two connect to Github](README_images/deployment/repo_connect.png)

**8. I chose to enable 'Automatic Deploys'. In order to do so click the 'Enable Automatic Deploys' button.**

![Enable automatic deploys](README_images/deployment/auto_deploy.png)

**9. For manual deployment or to deploy when needed use the 'Manual Deploy' section by clicking 'Deploy Branch'.**

![Manual deploys](README_images/deployment/manual_deploys.png)

**10. Click 'View' at the bottom of the 'Manual Deploy' section to view the deployed site.**

![View deployed site button](README_images/deployment/view_site.png)

[⏫ contents](#contents)

## Credits
It would be an incredible feat to remember all information needed to build such a project, to a deployable standard. Therefore I am not ashamed to mention some resources were used to aid me in the process, I have detailed some of the resources used.

I must also credit my mentor Jubril Akolade, for his inputs. Particularly with defensive design and the custom `@user_owns_report` decorator. This decorator was implemented at the beginning of the views.py file _(lines 16-41, reports/views.py)_.

### Tools
---------
* [Lucid Chart](https://www.lucidchart.com/pages/): Wireframe and ERD
* [ESLint](https://eslint.org/): JavaScript Testing
* [PyLint](https://pylint.org/): Python Linting
* [Coverage](https://coverage.readthedocs.io/en/7.2.7/): To test how much of the project had benn test during unit testing.
* [Google Fonts](https://fonts.google.com/)
* [Favicon.io](https://favicon.io/)
* [Am i Responsive](https://ui.dev/amiresponsive?url=https://reach-reports-e02886ddeda3.herokuapp.com/)
* [Looka](https://looka.com/onboarding?gclid=Cj0KCQjwoeemBhCfARIsADR2QCv_4Sk-E2qyPMvF2918hnwloja34mSPjNp3fO0QplTzD7A99QQ1U-UaAt1REALw_wcB): Site Logo and 'no-image' image.

### Resources
-------------
* [Django Documentation](https://docs.djangoproject.com/en/3.2/): The Django docs are really extensive and provide a wealth of support, the main uses I found were:
    - Testing
    - Advanced Testing Topics
    - FormFields
    - UpdateView
    - ReverseLazy
    - Custom Template Tags
    - DateInput Widget

* [Bootstrap 5.2 Docs](https://getbootstrap.com/docs/5.2/getting-started/introduction/): Relied on heavily for styling and JavaScript.

* [FontAwesome](https://fontawesome.com/): For all icons found site wide.

* [Jinja Filters](https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters)

* [Crispy Docs](https://django-crispy-forms.readthedocs.io/en/latest/index.html)\
[Cripsy Bootstrap 5](https://github.com/django-crispy-forms/crispy-bootstrap5): Bootstrap5 form rendering templating

* [Custom Authentication Backend](https://stackoverflow.com/questions/37332190/django-login-with-email): Used to enable email login to override the username input.

* [Email Authenication](https://medium.com/@therealak12/authenticate-using-email-instead-of-username-in-django-rest-framework-857645037bab): Further suport for email login.

* [Assertions](https://www.tutorialspoint.com/unittest_framework/unittest_framework_assertion.htm): Assertion definitions for writing tests.

### Tutorials
-------------
* [Setup SMTP Tutorial](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab), [Setup SMTP Tutorial 2](https://www.codesnail.com/django-allauth-email-authentication-tutorial/#:~:text=password%20with%20login-,Email%20verification,none%20to%20mandatory%20like%20this.&text=Now%20while%20registering%20it%20will%20send%20an%20email%20verification%20link.): These tutorials helped me to set up the gmail smtp required for the password reset functionality. 

* [Password Reset Tutorial](https://learndjango.com/tutorials/django-password-reset-tutorial): This tutorial also helped to set up the password reset using django-allauth.

* [Edit Object Tutorial](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform): Helped when creating views to edit model objects.

* [Code Institute LMS:](https://learn.codeinstitute.net/dashboard): I took a great amount of support from the following modules, setup, deployment, and function, generic and class based views.
    - Agile Development
    - 'I Think Therefore I Blog'
    - 'Hello Django' walkthroughs

* [Defensive Design](https://www.youtube.com/watch?v=TAH01Iy5AuE): For user restrictions, I used this to help implement the custom `@user_owns_report` decorator.

### Example Projects
--------------------
During the project build I used 2 projects as examples to compare structure of the project, and Unit testing ideas. These projects were used purely to compare, as they were rewarded a distinction grade by [Code Institute](). There are some similarities in README structure and appearance, but all content is specific to my site. These projects were:

[BobWritesCode/Server-directory-website](https://github.com/BobWritesCode/server-directory-website/tree/master)

[Edb83/Moose-Juice](https://github.com/Edb83/moose-juice)

[⏫ contents](#contents) [⏩ Testing README](README.md)