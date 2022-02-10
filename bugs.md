# Bug Fixes

## requirements.txt file
### The Problem
* The requirements file became corrupted and as such the modules were not working on the required way. 
### The Fix
* After a chat with tutor support I put my requirements.txt file through a converter and readded it to my workspace.

## 500 error on live site and production site css missing
### The Problem
* The live site was not showing on my browser dispite the fact that all the builds and deployments had pulled through to Heroku.
### The Fix
* As it turned out my browser cache needed clearing so that the live site was visible once more.
On the production site the css and images were no longer showing meaning that it was difficult to test new code during development this was fixed by adding a new variable to Gitpod called DEVELOPMENT and setting it to True, this has ment that whilst in development the site can be viewed on the development server again.

## Stripe secret keys not pairing
### The Problem
* The stripe publiv and secret keys were not registering the in the envirnment variables even though hey were saved in Git pod and added to setting.py

### The Fix
* After some consideration I decided to an an env.py file to my workspace and added it to .gitignore to that the secrey keys were not going to be pushed to GitHub and this fixed this issue and stripe payment began to function correctly.

## Operational Error at Checkout
### The Problem
* Two models are not functioning correctly on my live site they throw error 500 messages when the page tries to load. On closer inspection in the admin the model is there but not accessible or with the ability to add data.
### The Fix


