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
This was actually and error with my browser! once the cache was fully cleared the pages loaded correctly.

## Superuser missing
### The Problem
* My superuser stopped working on both the development and live site, meaning that I could no longer access the admin panel or backend of my site.

### The Fix
* After some checking I found that I had forgotten to add the DATABASE_URL to my env.py and as such changes had not been migrating to my live site correctly. Once this was re-established and the migrations added I set up a new super user through the terminal and full access was once again working.

## Live emails not sending
### The Problem
* On registration the email to the user for email validation is not sending as such registration cannot be completed.
### The Fix
* On checking through my code I couldn't see why the email would not be sending, I revisited the lesson on email set up and stil couldn't see what was wrong.
* After a nudge from a tutor I realised that I had not remove the development variable from my config vars in Heroku so after removing that and restarting the appit was all working fine.