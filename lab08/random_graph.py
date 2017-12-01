import random
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

x =  random.sample(range(0,501),100)
print x

y = random.sample(range(0,501), 100)
print y

# The following code tests our random sample x against the mean of 250.

print 'H0 = There is no statistical significance between the random sample x and a mean of the value 250.'
print 'HA = There is a statistical significance between the random sample x and a mean of the value 250.'
ttest_sampx = ss.ttest_1samp(x,250)
print ttest_sampx

# The following code uses the output of the t-test to print the correct analysis.

if ttest_sampx [1] > 0.05:
    print "The H0 is not rejected. There is no statistical evidence against the H0."
elif ttest_sampx [1] < 0.01:
    print "H0 is rejected. There is statistical evidence for the H0."
else:
    print "There is a weak correlation between the samples x and a mean of 250, therefore the H0 is rejected."
print "__________________________________"

# The following code tests our random sample y against the mean of 250.

print "___________________________________"
print 'H0 = There is no statistical significance between the random sample y and a mean of the value 250.'
print 'HA = There is a statistical significance between the random sample y and a mean of the value 250.'
ttest_sampy = ss.ttest_1samp(y,250)
print ttest_sampy
# The following code uses the output of the t-test to print the correct analysis.

if ttest_sampy [1] > 0.05:
    print "The H0 is not rejected. There is no statistical evidence against the H0."
elif ttest_sampy [1] < 0.01:
    print "H0 is rejected. There is statistical evidence for the H0."
else:
    print "There is a weak correlation between the samples y and a mean of 250, therefore the H0 is rejected."
print "__________________________________"

# We are now testing the correlation between the two random samples x and y
print 'H0 = There is no correlation between the random sample x and the random sample y.'
print 'HA = There is a correlation between the random sample x and the random sample y.'
relation = ss.ttest_ind(x, y)
# The following code uses the output of the t-test to print the correct analysis.

print relation
if relation [1] > 0.05:
    print "There is no correlation between the two random samples x and y."
elif relation [1] < 0.01:
    print "There is a strong correlation between the two random samples x and y."
else:
    print "There is a weak correlation between the two random samples x and y."

print "_____________________________________________________________________"

print "Task 3"

correlation = ss.pearsonr(x, y)
print correlation
print "____________________________________________________________________"
linregression = ss.linregress(x, y)
print linregression
slope = linregression[0]
intercept = linregression[1]
print "This is the slope of the linear regression of x and y:", slope
print "This is the intercept of the linear regression of x and y:", intercept

# describe the regression



xaxis = x
yaxis = y
colors = []
sizes = []
for y in yaxis:
    if y > 250:
        colors.append('blue')
        sizes.append(15)
    else:
        colors.append('red')
        sizes.append(40)
plt.scatter(xaxis, yaxis, s=sizes, c=colors)
plt.xlim([-5, 505])
plt.ylim([-5, 505])
# We will now add a line graph to the scatter plot
xaxis = range(501)
yaxis = [slope * x + intercept for x in xaxis]
plt.plot(xaxis, yaxis)
plt.savefig("plot2.pdf")


plt.show("plot2.pdf") # to show the graph in a window.

print "______________________________________________"
