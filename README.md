# REACH
### Condition reports from the mountains, written by climbers, for climbers.

![Overall site view across different devices](README_images/responsive_preview.png)

## Live Site
[Hosted on Heroku](https://reach-reports-e02886ddeda3.herokuapp.com/)

## Repository
[Github Repo](https://github.com/mtmanning93/Reach_reports)

## Introduction

Reach is a website where users have the abiltiy to create and post condition reports from their climbing adventures and expeditions. Non registered users have the ability to read reports and comments. Registered users have full CRUD functionailty over their reports, along with extra features, such as, commenting and liking other users reports.

## Built With:
Django, Python, JavaScript, Bootstrap 5.2, CSS, HTML

### Includes:
Cloudinary, CrispyForms

## Contents

- [REACH](#reach)
    - [Live Site](#live-site)
    - [Repository](#repository)
    - [Introduction](#introduction)
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
        - [Wireframe](#wireframe)
    - [Technologies](#technologies)

## Design Thinking

### Problem ID

The initial idea arose whilst reading a facebook group post. The group is called the ['Die 48 Schweizer 4000er'](https://www.facebook.com/groups/255829887155). In the post the user expressed their frustration, and having decision fatigue, due to the uncertainty of conditions across the alps on a weekend they wished to climb. They had asked where could they find more information.

Using the 5c's approach it became apparent that having a centralised place where users could read and create reports based on the conditions they had experienced, would solve the problem.

### Problem Statement

> "As a passionate climber, I am trying to climb on my free days, but I'm unsure of the mountain conditions and can't decide whats the best option. This makes me frustrated. How do I find out up to date conditions?"

### Brainstorm

As a passionate alpinist, it was possible to gather a group of climbers and hold a brainstorming session. The sessions provided an insight into what was important to the target audience.

There were 3 key takeaways from the brainstorming session:
    
    1. Images Are Important
        - An image says a thousand words, with experience you can tell a lot from an image.
    2. Comments
        - A discussion on each report would provide even further information for users.
        - Other user input on each report would create more in depth reports.
    3. Key Information
        - Every report should be simple but provide enough information in order to give an insight.
        - Key information such as number of people and an overall grade should be given on all reports.

### Site Goals

#### - User Goals

The user would like the ability to read and post condition updates from recent climbs they have done, or want to do. Providing real and current information from the mountains.

#### - Owners Goals

The goal is to create a discussion and library of up to date condition reports to enable climbers to make easier decisions and ultimately become more successful.

## UX / User Experience Design

Example user stories which have affected the overall design and functionailty of the project.

### User Stories

#### - Site Admin
> "As a site admin I can create, read, update and delete reports so that I can manage the site content"
>
> "As a site admin I can approve or disapprove comments so that I can keep the content specific and non offensive"

#### - User

> "As a user I can easily locate each page of the site so that navigation is smooth and consistant throughout the site"
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

## Development

### Agile Design
----------------

Due to the size of the Reach project and the many different parts. It was crucial to adopt an Agile methodology. In a project with many different functionalities it can be easy to move between the tasks, forgetting parts or even leaving them unfinished. With the Agile approach I was able to identify the key components which would build the project, and seperate them into smaller more manageable tasks. Always carrying manual testing to ensure each component was working as expected before moving on to the next task. It enables regular reflection on the project and attention to each technicality.

### Github Issues

#### Templates

Throughout the build I used three templates:
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

The next issue template created was the bug report. As the project grew I was constantly carrying out manual testing to check the functionailty of the component being built. Whilst doing so, occassionally, I would notice bugs in other components of the site. In order to keep the flow of the agile method I would create bug reports and add them to the list of issues. The bug reports were then addressed when the priority to do so was high, for example, when labelled a 'Must Have' within the current iteration.

If it was a bug within the current user story task I would assign the label 'Bug' to it.

[Example of assigning the 'Bug' label](https://github.com/mtmanning93/Reach_reports/issues/22)
 
[Example full Bug Report](https://github.com/mtmanning93/Reach_reports/issues/32)

#### Feature Request

The final template created was a feature request. Whilst building the project and showing others a new component, a new idea for a feature would come to mind. Some ideas would be a great addition to the current deployed version of the site whereas others would be great in a later version. All feature requests were labelled with the 'Feature Request' label and/or 'Improvement' depending on the implementation of the idea.

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

To help the visualisation of tasks in the project I implemented a Kanban board, using GitHub projects. The board was seperated into 3 columns; To Do, In Progress, and Done. All issues in the backlog were automatically added to the Kanban 'To Do' column. Throughout the build I would take all issues from the current iteration into the 'In Progress' column. Once all tasks were completed in the issue I would move the issue over to the 'Done' column. 

When possible I would close an issue from the terminal using the `close #10` command from inside a commit message. This would automatically move the issue into the 'Done' column.

[Reach Kanban Board](https://github.com/users/mtmanning93/projects/7)

