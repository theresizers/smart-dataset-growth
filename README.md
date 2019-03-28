# Smart Dataset Growth

# Project Goal
Fast AI instrcutors Jeremy Howard and Leslie Smith had an intuition about a faster method to train deep learning models and also reduce overfitting at the same time.

Here is how Leslie Smith described his idea to Jeremy: “In addition, I can suggest a new idea for faster training. You mentioned progressive resizing. I am toying with a different approach. What if one trained in stages where the first stage includes only one image per class for a couple of hundred iterations/epochs, the second stage included 10 images per class, third stage 100 images, and finally all the images. This should be very fast so the question is does it perform well. One can even choose the first image to be iconic for the class so the network learns a good initial set of weights to initialize the next stage’s weights.”

Jeremy replied with the following idea; “So I guess another alternative would be: in the first stage just include a small number of very different classes (e.g. one type of fish, one type of plant, one type of vehicle). Then gradually add more classes, and towards the end of training add more similar classes (e.g. different breeds of dog). My intuition is that the latter approach might be more successful, especially when trying to train with large learning rates. But I’d be interested to see!”

Ah, the art of science. We have two different hypothesis on ways to potentially speed up training. Which one is right? Or neither? Or both? Experiments must be run!


Forum Discussion Post : [Link](http://forums.fast.ai/t/research-collaboration-opportunity-with-leslie-smith/16454/34)



Google spreadsheet for task assignment:  [Link](https://docs.google.com/spreadsheets/d/14eH9A-CPLCjrdCFNJWBLO4t1rLgva9uvQtHuEOCacGU/edit?usp=sharing)

## Tasks : Training in Stages ##
* #### Hypothesis 1  : Increase Number of Samples in Dataset Progressively (P.S : Leslie Smith's Idea)

  What if one trained in stages where the first stage includes only one image per class for a couple of hundred iterations/epochs, the second stage included 10 images per class, third stage 100 images, and finally all the images. This should be very fast so the question is does it perform well. One can even choose the first image to be iconic for the class so the network learns a good initial set of weights to initialize the next stage’s weights
  * Metrics and plot to be Generated :
    1. Test Loss,Train Loss vs Iteration  - Check the Effect of Convergence
  
  
 * #### Hypothesis 2   Increase Number of Classes Fed into the model Progressively (Coarse to Fine Differences in Classes)
 
 So I guess another alternative would be: in the first stage just include a small number of very different classes (e.g. one type of fish, one type of plant, one type of vehicle). Then gradually add more classes, and towards the end of training add more similar classes (e.g. different breeds of dog). My intuition is that the latter approach might be more successful, especially when trying to train with large learning rates.

* #### Hypothesis 3  Progressively Increase the size of Image (Check the rate of Convergence)
  * Proposed Work flow to Experiment the Hypothesis : 
    1. Prepare the dataset (CIFAR10/ CIFAR 100). Creation of Dataloader. Use fastai- ImageClassifierData.from_paths
    2. Define Multiple Architectures : Fully Connected , CNN , Lenet5
    2. Setup Logging mechanism to Store the Train & Test Loss, Imagesize.
    3. Find Optimal Learning rate using Learing Rate Finder and setup One-Cycle Learning.
    4. Start Trainning the network with sz = 64 and keep doubling the size for every 3/5 iterations ?
    5. 
    
  * Metrics and plot to be Generated :
    1. Plot Train & Test Loss vs Image Size Used. 
  
  
