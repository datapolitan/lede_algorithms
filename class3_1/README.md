# Algorithms: Week 3, Class 1 (Tuesday, July 28)

Today we'll be reviewing a bit of material from last week, including both your lab assignments from last Tuesday and Thursday's lesson on regression, and then expanding on the latter in a couple ways.

First we'll review, and (roughly) recreate a couple stories that have employed regression in basic ways. Then, in the interests of transparency, we'll talk a bit about what's going on under the hood with the algorithms that comprise regression.

Finally we'll touch briefly on the idea of classification using a portion of a project we're currently implementing at the Times.

## Hour 1/1.5: Review

First we'll talk through some of your story ideas and critiques from last Tuesday. Then we'll revisit some basic regression concepts from last week using [this iPython notebook](https://github.com/datapolitan/lede_algorithms/blob/master/class3_1/regression_review.ipynb), which (very roughly) mimics a project that the St. Paul Pioneer Press did in 2006 and 2010, known as [Schools that Work](http://www.twincities.com/ci_15487174).

## Hour 2: A closer look at regression

Journalists tend to look at linear regression through a statistical lens and use it primarily to describe things, as in the case above. You can see another examples here:

  - [Race gap found in pothole patching](http://www.jsonline.com/watchdog/watchdogreports/32580034.html) (Milwaukee Journal Sentinel). And the [associated explainer](http://www.jsonline.com/news/milwaukee/32580074.html).

But looked at another way, linear regression is also a predictive model -- one that, at scale, is based on an algorithm that we can demystify, per our conversations last week. We'll spend a short amount of time talking about how that works and relate it (hypothetically) to this [interesting story](http://bits.blogs.nytimes.com/2015/07/26/using-algorithms-to-determine-character/) from yesterday's Times.

## Hour 3: Introduction to classification

Using a [project](https://github.com/datapolitan/lede_algorithms/blob/master/class3_1/classification.ipynb) we've been working on at the Times, we'll expand our idea of supervised learning to include something that seems a bit more like what you might consider "machine learning" -- classifying people's jobs based on strings representing their occupation and employer.

We'll also discuss how lots of data problems in journalism are secretly classification problems, including things like [sorting through documents](https://github.com/cjdd3b/nicar2014/tree/master/lightning-talk/naive-bayes) and [extracting quotes from news articles](https://github.com/cjdd3b/citizen-quotes).