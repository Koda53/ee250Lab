# Lab 3

## Team Members
- Ernest Guo
- Joel Sedillo

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

REST optimizes client-server interactions. According to the article, statelessness removes server load because the server does 
not have to retain past client request information. Well-managed caching eliminates some client-server interactions. 
All these features support scalability without causing communication bottlenecks that reduce performance.

Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?

The resources that are being provided to clients can be images, videos, text, numbers, or any type of data, but in our case it is the mailboxes.

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

The main method that we are using for our mail server is GET so another common REST Mehod that is not used in our mail server is DELETE. In order to extend our mail server to do this, we can add a DELETE endpoint to the mail server. 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

API keys are used to authenticate the client and to make sure that they are authorized to access the API.
