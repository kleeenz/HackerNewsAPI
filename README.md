All libraries can be found in requirements.txt. The application was created in isolated virtual environment. No global site-pckages was used.
The Api pulls data from Hackernews
HackerNews is an open source API that developers can use to create application https://hackernews.api-docs.io/v0/overview/introduction
i connected to the API using the request python library "pip install requests"
The appliction pulls the first 100 items from the first request and pulls data periodically. I set the timer for every 5 minutes
to do this i used a python library called advanced scheduler "pip install APScheduler"
To connect the scheduler
i created a python file called updater to schedule the function i wish to apply the scheduler to "sync_items"
The application has two parts, the API part and the application itself
For the API part, i used modelmixins to define my HTTP actions (GET, POST, PATCH and DELETE).
