# The Open Course in Data Science for Neuroscience
These materials are an introduction to the ways in which data is used in order to ask and answer questions about the brain. It cuts across many fields of neuroscience, including cellular, systems, and cognitive neuroscience, and is an introduction to those who are interested in using quantitative methods to study the brain.

These materials are free for users 

# Course tools and materials
The materials are split into two codebases - one in Matlab, one in Python. These aren't the only languages available for doing neuroscience work, but they are by far the two most commonly-used languages. You can get a copy of Matlab by purchasing a license [hereXXX](matlab.com), and you can download a free scientific distribution of python [hereXXX](anaconda.com).

The open-source community has been instrumental in improving quantitiative sophistication in the analysis of the brain. As such these materials utilize open source materials wherever it is possible. Instead of custom code, a strong preference is given to utilizing pre-existing toolboxes. However, it is also important to "get your hands dirty" when analyzing data. As such, we have avoided toolboxes that serve as "one-click" solutions, or which require graphical UIs to perform analyses.

## Python Code
All python tutorials are written as jupyter notebooks. In addition, we have included a python module that contains helper functions to simplify tutorial materials. We urger you to investigate these functions and understand how they work.

## Matlab code
Matlab tutorials are ............

## Datasets
This course uses datasets which are completely open and free to use. As such, any user should be able to copy this repository, along with the relevant datasets, and run the tutorials on their own computers.

# Course topics
Below is a list of topics currently covered by this course.

## Basics
These tutorials cover the basics of data storage, representation, and manipulation.

* Exploring data
  * Goal: create all standard "initial plots" that one might make given this data
  - [x] Data munging - conditions, trials, time, observables
  - [x] Trial timeseries - raster plots
  - [x] Trial averaging - peristimulus time histogram (psth)
    - [x] Temporal smoothing
  - [ ] Inter-spike intervals
* Calculating statistics and uncertainty

## Modeling
These tutorials attempt to answer specific questions about the brain by building computational models.

* Models for anatomical (single unit) response during task
  * Goal: create average response models (nonparametric and parametric) and quantify uncertainty in model
  - [x] Raw response versus task variable
  - [x] Average response versus task variable
  - [x] Parametric response fitting
  - [x] Bootstrapping errorbars for response
  - [ ] MSE on held-out data
  - [x] Machine learning response functions
* Connectivity
* Latent variables and dimensionality reduction
* Linear models for timeseries
