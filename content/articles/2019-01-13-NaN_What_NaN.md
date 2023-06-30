title: Handling Missing Values in your Data.
slug: nan-what-nan-handling-missing-values
date: 2019-01-13 18:40
category: Data Science
tags: Data Science, ML, scikit-learn
summary: _NaN, what NaN? How to cope with missing values without tearing up._

Machine Learning algorithms work well depending on a number of factors; one being the quality of the presented data. In fact, preparing/preprocessing your data to make a magical input is somewhere in the critical zone on a Wizard's(here, Data Scientist) orb, and should, like other factors, be taken seriously in preparing, before pushing it into an ML vanishing cabinet.

We will look at how to achieve quality data using some preprocessing techiques inorder to build a robust machine learning model, and we might be lucky enough to test it on real data.

## workflow:
- Identifying missing values or unknown values.
- Removing/imputing missing values from the dataset
- Getting categorical data to play nice with our ML model.
- Drop this. Drop that. Selecting relevant features.

Having one or more missing values(_NaN - Not a Number_) lurking around in a dataset is something that shouldn't worry you, if any thing having not to see one in a big dataset should even scare you before you go hunting for the powerhouse behind such beauty disguised as data. Why? Like most scientific data collecting there's prone to be an error; error in reading a value or just sheer oversight, or leaving a particular field blank for a couple of reasons. These empty fields are registed as either <code>NULL</code> or <code>NaN</code>.

Let's delve into some practical techniques for dealing with missing values, by either removing these NaNs or imputing them.


### Identifying missing values or unknown values.

For the sake of this post I have prepared a sample data with some intentionally missing values so as to give us a somewhat personal insight at this.

{% notebook ./notebooks/NaN_What_NaN.ipynb cells[2:4] %}

As we can see Age has no presence of NaN, Salary and Desk number have a value of 1. By looking at df you can point them out.

Easy peasy lemon squeezy. Let's move on, shall we?


### Removing/imputing missing values from the dataset.

Simply removing missing values could be a fun task, albiet a problematic one. Inorder to do this one would have to decide on which to remove; columns(features) or rows(samples). And even then you'd still have to live through the judgemental feeling by the gods of data on why you would snap your fingers on some (potentially) good data.

Again, it's a fun task. See how:

{% notebook ./notebooks/NaN_What_NaN?.ipynb cells[5:7] %}

Easy peasy? yeah?

#### NB:
1. This method of dropping rows and columns can prove to be detrimental in the long run as (valuable) samples/features could be eliminated, risking a reliable analysis.
2. The <code>dropna</code> method is a fully equipped method. Do check around for other implementations, including dropping specific rows that contain NaNs, subsets and threshes.


### Imputing missing values

This is the recommended approach when it's dealing with missing values. It entails replacing Nan with mean, median or mode of that particular row/column.
A convenient way to achieve this is by using the <code>Imputer</code> class from __scikit-learn__, as shown below:

{% notebook ./notebooks/NaN_What_NaN?.ipynb cells[9:11] %}

Not much of a task, yeah? no? Okay. We imported the <code>Imputer</code> class from __scikit-learn__, gave it a 'strategy' to handle the data, fitted the data and then transformed it. Easy peasy--no? Just go over it line by line.

#### NB:
1. The strategy <code>most_frequent</code> is suitable for imputing categorical feature values, for         example, a feature column that contains an encoding of color names, such as green, orange, and blue.
2. Understanding the scikit-learn estimator API:
![Fit-transform - sklearn](https://i.stack.imgur.com/PiaIX.png)
*image source: [imgur](https://i.stack.imgur.com/PiaIX.png)
3. The <code>fit</code> method learns the parameter from the training data, and the <code>transform</code> method use these parameters to transform the data. 
4. There are other ways of handling NaN. Go find out!

##### Resources:
1. Python Machine Learning by Sebastian Raschka.
2. [scikit data transformation](https://scikit-learn.org/stable/data_transforms.html#dataset-transformations)

