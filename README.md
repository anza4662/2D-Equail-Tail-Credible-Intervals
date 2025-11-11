**Code can be found below (simple function in Python)**

# Background

In Bayesian analysis, credible intervals are used as an uncertainty estimate of the point estimates for a posterior distribution. 
Two such uncertainty estimates are the **highest posterior density** (HPD) and **equal-tail** (ET) credible intervals. 

In the one dimensional case it is simple to estimate a $100 \cdot (1-\alpha)$% credible interval (both HPD and ET) for data samples 
of a posterior distribution. For the ET one simply sorts the data points and removes $(1-\alpha)/2$ of the lowest and highest ordered data points. 
For the HPD one has to first estimate the density for each of the points, whereafterthe points can be sorted by their density 
and the disired percentage of the points with smallest density can be thrown away.

In the two dimensional case the method for the HPD is the same, a bit trickier since one has to estimate the density for a two
dimensional distribution, but at least the method is well defined. However for the ET credible intervals we have the problem that,
in two dimension, we can not really define what a tail is. This brings us to our goal of this project, that is,to propose a method
for estimating ET credible intervals in the two dimensional case. 

# Method 
We will firstly describe the method by a simple example and then extend it to a more general case. The example is that we constrain
our credible interval to be rectangular and lie parallell to the x- and y-axis.

### Example
We would like the tails in the x-axis be equal to that of the y-axis. Then we will have equal-tails in both directions of intrest. 
The method is as follows, sample $n$ points from the posterior. Then toss a coin, if it is heads choose the x-axis, if it is tails choose the y-axis. 
After sampling an axis, by means of tossing a coin, take all points and order them according to the chosen axis. 
Remove the lowest and highest ordered points (i.e two points in total). Then again sample an axis, order and remove points accordingly. 
We then continue this process until we have $(1-\alpha)\%$ points left. Then, we can take the boundary line for the equal-tail CI as the smallest 
rectangle containing all remaining points.

### General method
The two-parameter equal-tail CI could be further generalized to include not only the $x$ and $y$-axis but a set of axes. Then we would sample the axes uniformly from this set. 
The choice of this set would somehow reflect the shape of the underlying distribution. Suppose that if we knew our underlying distribution to be a multivariate normal, 
choosing the set of all axes that intersect the origin would be a wise choice since the multivariate normal distribution is symmetric in axes that intercept the origin.

