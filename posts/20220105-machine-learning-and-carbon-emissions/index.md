---
title: "Machine learning and carbon emissions"
date: 2022-01-05
type: ["posts"]
draft: false
tags:
categories:
---


Recently I have been looking into the environmental impact of machine learning in relation to ongoing research projects at work.
Carbon emissions are high on the agenda for everyone, especially if one works at a research group with the term "Green" in it's name.
Lots is already written on the topic, but I wanted to share a few of the most interesting articles and research papers I found, with a few comments of my own.

[Deep learning's carbon emissions problem](https://www.forbes.com/sites/robtoews/2020/06/17/deep-learnings-climate-change-problem/) from Forbes summarizes well some of the most problematic issues of machine learning. 
It is mainly focused on deep learning and natural language processing (NLP), which entails developing models that consist of an enormous amounts of parameters.
Many of the article's key points stems from a paper that in 2019 really brought awareness to the gigantic energy usage of some of the largest deep learning models: [Energy and Policy Considerations for Deep Learning in NLP](https://arxiv.org/pdf/1906.02243.pdf).
As a machine learning practitioner, the following quote from the article is something I'm especially concerned with:

> Another factor driving AI’s massive energy draw is the extensive experimentation and tuning required to develop a model. Machine learning today remains largely an exercise in trial and error. Practitioners will often build hundreds of versions of a given model during training, experimenting with different neural architectures and hyperparameters before identifying an optimal design.

Luckily, there exist several frameworks that can help reducing the number of experiments needed during model development.
Personally, I use [Data Version Control (DVC)](https://dvc.org/), an excellent tool for structuring machine learning experiments.
Not only does it helps you keep track of models and hyperparameters, but you can also use it to track all stages of a machine learning pipeline (which typically consists of several preprocessing stages).
Since it keeps all intermediate results between stages in cache, you can save a lot of computation time when experimenting with different control parameters.

I think the article concludes with an important note:

> The AI community must begin to work toward new paradigms in artificial intelligence that do not require exponentially growing datasets nor outrageously vast energy expenditures.

Another article, [The drive to make machine learning greener](https://www.discovermagazine.com/technology/the-drive-to-make-machine-learning-greener) from Discover Magazine, quotes a researcher team from the University of California, Berkeley, on how reporting on carbon emissions might help reduce them:

> Patterson and colleagues conclude by recommending that computer scientists report the energy their calculations consume and the carbon footprint associated with this, along with the time and number of processors involved. Their idea is to make it possible to directly compare computing practices and to reward the most efficient. “If the machine learning community working on computationally intensive models starts competing on training quality and carbon footprint rather than on accuracy alone, the most efficient data centers and hardware might see the highest demand,” they say. 

The paper [Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning](https://jmlr.csail.mit.edu/papers/volume21/20-312/20-312.pdf) argues similarly for the importance of measuring and reporting the carbon footprint of machine learning experiments. 
The paper is an especially interesting read, as the authors suggest a set of concrete courses of actions based on their findings.
The main points are to be consistent in reporting energy and carbon metrics, and using leaderboards of these metrics as incentive for reducing carbon emissions in research.
They also write that one should consider "energy-performance trade-offs before deploying energy hungry models".
It's also interesting to note that one of the most intuitive (at least in my opinion) ways of measuring the energy-efficiency of any computer program, namely to count the number of Floating Point Operations (FPOs), actually can be misleading (read section 5.1 of the paper for a discussion on this).
This is one of the reasons for why there is a need for frameworks that can measure or more accurately estimate the actual carbon emission of training or running a machine learning model.
The authors have published an open source [Experiment impact tracker](https://github.com/Breakend/experiment-impact-tracker) that can be used for this purpose.

Another paper that looks into methods for tracking energy-efficiency is this: [Quantifying the Carbon Emissions of Machine Learning](https://arxiv.org/pdf/1910.09700.pdf).
The authors have contributed to two tools that can be employed for emissions tracking. 
The first one is an [emission calculator](https://mlco2.github.io/impact/#compute), where you compute emissions based on hardware type, runtime and cloud provider/region.
The second one, which I personally have started testing in my projects, is the [CodeCarbon](https://codecarbon.io/) framework.
CodeCarbon can be embedded in Python code, and automatically tracks the energy usage and carbon emissions of your experiments.
The tool is very easy to use and generates results in a csv-file that can be used for your own analysis.
Additionally, the tool provides an interactive dashboard based on the results, which makes it very quick and easy to get up and running with emission tracking.

### Conclusion

Even though the emissions of "small-scale" machine learning practitioners like myself are dwarfed by the gargantuan carbon footprint of big tech companies like Google and Amazon, I think it is important that we are all aware of these issues, and try to mitigate them at any scale.
A shift towards more green machine learning would benefit us all, and hopefully also affect the large players in the industry.

To summarize, here's a few concrete actions that can help reduce the carbon footprint of machine learning:

- Reduce the number of unnecessary training runs, for example using frameworks like [DVC](https://dvc.org/).
- Employ efficient methods for hyperparameter tuning.
- Measure and report on energy usage for your experiments. Use an [emission calculator](https://mlco2.github.io/impact/#compute), or use the [CodeCarbon](https://codecarbon.io/) framework to automatically measure the impact of all your experiments. Another option is the [Experiment impact tracker](https://github.com/Breakend/experiment-impact-tracker) (this one I have not tested myself yet).
- If you run your experiments on external servers ("in the cloud"), be aware of which data centers you use, and how they are powered.
