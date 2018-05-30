# Smart Dataset Growth

# Project Goal
Fast AI instrcutors Jeremy Howard and Leslie Smith had an intuition about a faster method to train deep learning models and also reduce overfitting at the same time.

Here is how Leslie Smith described his idea to Jeremy: “In addition, I can suggest a new idea for faster training. You mentioned progressive resizing. I am toying with a different approach. What if one trained in stages where the first stage includes only one image per class for a couple of hundred iterations/epochs, the second stage included 10 images per class, third stage 100 images, and finally all the images. This should be very fast so the question is does it perform well. One can even choose the first image to be iconic for the class so the network learns a good initial set of weights to initialize the next stage’s weights.”

Jeremy replied with the following idea; “So I guess another alternative would be: in the first stage just include a small number of very different classes (e.g. one type of fish, one type of plant, one type of vehicle). Then gradually add more classes, and towards the end of training add more similar classes (e.g. different breeds of dog). My intuition is that the latter approach might be more successful, especially when trying to train with large learning rates. But I’d be interested to see!”

Ah, the art of science. We have two different hypothesis on ways to potentially speed up training. Which one is right? Or neither? Or both? Experiments must be run!

# Join us 
Leave your mail id and we'll send you an invite to join us

Google spreadsheet for task assignment: https://docs.google.com/spreadsheets/d/14eH9A-CPLCjrdCFNJWBLO4t1rLgva9uvQtHuEOCacGU/edit?usp=sharing
