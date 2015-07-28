# Algorithms: Week 3, Class 1 (Tuesday, July 28)

Today we'll be reviewing a bit of material from last week, including both your lab assignments from last Tuesday and Thursday's lesson on regression, and then expanding on the latter in a couple ways.

First we'll review, and (roughly) recreate a couple stories that have employed regression in basic ways. Then, in the interests of transparency, we'll talk a bit about what's going on under the hood with the algorithms that comprise regression.

Finally we'll touch briefly on the idea of classification using a portion of a project we're currently implementing at the Times.

## Hour 1/1.5: Review

First we'll talk through some of your story ideas and critiques from last Tuesday. Then we'll revisit some basic regression concepts from last week using [this iPython notebook](https://github.com/datapolitan/lede_algorithms/blob/master/class3_1/regression_review.ipynb), which (very roughly) mimics a project that the St. Paul Pioneer Press did in 2006 and 2010, known as [Schools that Work](http://www.twincities.com/ci_15487174).

## Hour 2: A closer look at regression

Journalists tend to look at linear regression through a statistical lens and use it primarily to describe things, as in the case above. You can see another examples here:

  - [Race gap found in pothole patching](http://www.jsonline.com/watchdog/watchdogreports/32580034.html) (Milwaukee Journal Sentinel). And the [associated explainer](http://www.jsonline.com/news/milwaukee/32580074.html).

But looked at another way, linear regression is also a predictive model -- one that, at scale, is based on an algorithm that we can demystify, per our conversations last week. We'll spend a short amount of time talking about how that works and relate it (hypothetically) to this [fun story](http://fivethirtyeight.com/features/donald-trump-is-the-worlds-greatest-troll/) from FiveThirtyEight.

## Hour 3: Introduction to classification

Using a [project](https://github.com/datapolitan/lede_algorithms/blob/master/class3_1/classification.ipynb) we've been working on at the Times, we'll expand our idea of supervised learning to include something that seems a bit more like what you might consider "machine learning" -- classifying people's jobs based on strings representing their occupation and employer.

We'll also discuss how lots of data problems in journalism are secretly classification problems, including things like [sorting through documents](https://github.com/cjdd3b/nicar2014/tree/master/lightning-talk/naive-bayes) and [extracting quotes from news articles](https://github.com/cjdd3b/citizen-quotes).

## Lab

Like last week, you'll be doing two things in the lab today:

First you'll expand the schools analysis we did earlier by layering in other variables [(documented here)](http://www.cde.ca.gov/ta/ac/ap/reclayout12b.asp) using multiple regression, interpreting the results, and again writing two ledes about what you found. Back those lede up with some internet research. If you find some schools that are over/under-performing or have other interesting characteristics, Google around to see what has been written about them. It's a good way to check your assumptions and to find other interesting facts to round out your story pitches.

This of course comes with a huge, blinking-red caveat: This is an algorithms class, and we're not getting deep enough into the guts of statistical regression for you to run out and write full-on stories based on your findings. There are things like [p-values](http://blog.minitab.com/blog/adventures-in-statistics/how-to-interpret-regression-analysis-results-p-values-and-coefficients) to consider, as well as rules of thumb for interpreting r-squared. If you'd like to get more in depth with that, we can carve out some time later in the course.

Your second assignment today is to write a short story (300-500 words) about [this company](https://www.upstart.com/), which is a startup that uses predictive models to assess creditworthiness using variables that go beyond credit score. No doubt their model is more complex than this, but you can think of the intuition as being similar to regression -- a handful of independent variables that help predict the likelihood that someone will pay their loan back. What are the implications of this? Why might it be good or bad for consumers if this catches on?