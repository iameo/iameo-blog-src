title: My Analysis on WHO Suicide Data
tags: graphs, health, visuals, analysis
summary: _The rate of suicide in the world and where should help be targeted to inorder to reduce the numbers_



This is my first public notebook and why it's on suicide is merely a thing of coincidence.
I'll try to be brief while simplistic in pouring out figures and graphs, so let's get started.

### Workflow:
- import the needed packages; from visualization tools to number handingling tools
- load dataset
- produce graphs, more graphs and even more graphs.
- summary on visualization.
- possible ML implementation(s)
- summary


{% notebook ./notebooks/WHO_suicide__notebook.ipynb %}

## Observation/Summary:

1. 5-14 years and 75+ years have low suicide rate.
2. 15-24 years, 25-34 years and 35-54 years consist of high suicide rates.
3. Nigeria is a no show here.
4. Russia has the highest number of suicides and we checked that out.
5. I accomodated the idea of using a Linear Regression model to predict for 2016-2018. I might add that.

(If we'd be predicting based on year then onehot encoding most of the features(e.g sex, age) should be employed)


## Resources:
1. [WHO suicide Data (Kaggle)](https://www.kaggle.com/szamil/who-suicide-statistics/kernels)
2. [Wikipedia: Suicide in Russia](https://en.wikipedia.org/wiki/Suicide_in_Russia)
3. [Wikipedia - Suicide](https://en.wikipedia.org/wiki/Suicide)
4. [Nationsonline](https://www.nationsonline.org/oneworld/third_world.htm)
