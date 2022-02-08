# Bug Fixes

## requirements.txt file
* The requirements file became corrupted and as such the modules were not working on the required way. After a chat with tutor support I put my requirements.txt file through a converter and readded it to my workspace.

## 500 error on live site and production site css missing
* The live site was not showing on my browser dispite the fact that all the builds and deployments had pulled through to Heroku, as it turned out my browser cache needed clearing so that the site was visible once more.
On the production site the css and images were no longer showing meaning that it was difficult to test new code during development this was fixed by adding a new variable to Gitpod called DEVELOPMENT and setting it to True, this has ment that whilst in development the site can be viewed on the development server again.

