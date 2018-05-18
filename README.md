# Smart dataset growth (Work in Progress)

Forum Discussion Post : [Link](http://forums.fast.ai/t/research-collaboration-opportunity-with-leslie-smith/16454/34)



Google spreadsheet for task assignment:  [Link](https://docs.google.com/spreadsheets/d/14eH9A-CPLCjrdCFNJWBLO4t1rLgva9uvQtHuEOCacGU/edit?usp=sharing)

Tasks : Training in Stages
* Hypothesis 1: Increase Number of Samples in Dataset Progressively (P.S : Leslie Smith's Idea)

  What if one trained in stages where the first stage includes only one image per class for a couple of hundred iterations/epochs, the second stage included 10 images per class, third stage 100 images, and finally all the images. This should be very fast so the question is does it perform well. One can even choose the first image to be iconic for the class so the network learns a good initial set of weights to initialize the next stage’s weights
  
 * Hypothesis 2:  Increase Number of Classes Fed into the model Progressively (Coarse to Fine Differences in Classes)
 
 So I guess another alternative would be: in the first stage just include a small number of very different classes (e.g. one type of fish, one type of plant, one type of vehicle). Then gradually add more classes, and towards the end of training add more similar classes (e.g. different breeds of dog). My intuition is that the latter approach might be more successful, especially when trying to train with large learning rates.

* Hypothesis 3: Progressively Increase the size of Image (Check the rate of Convergence)

Proposed Experiment : 
  Start Pretrainning the network with sz = 64 and keep doubling the size for every 3/5 iterations ?
  

Metrics and plot to be Generated : 
  Test Loss,Train Loss vs Iteration  - Check the Effect of Convergence
  
  
