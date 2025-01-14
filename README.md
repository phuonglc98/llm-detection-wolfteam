
<div align="center">

# **Bittensor SN32** <!-- omit in toc -->
[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

---

## Decentralized AI Detection <!-- omit in toc -->

### [⛏️ Mining Docs](docs/mining.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[🧑‍🏫 Validating Docs](docs/validating.md) 

</div>

## Introduction

Our subnet focuses on the detection of AI-generated content. Given the rapid growth of LLM-generated text, such as
ChatGPT's output of 100 billion words daily compared to humans' 100 trillion,
we believe that the ability to accurately determine AI-generated text will become increasingly necessary.


## Problem

With the recent surge in LLMs appeared many cases where we do actually want
to recognize where this text was generated by AI or written by human.
Let's explore some scenarios to highlight the potential and significance of LLM detection.

* **For ML-engineers**. Whether you’re sourcing training data, developing a foundational LLM, or fine tuning on your own data,
you need to ensure generative text does not make it into your training set. We can help.
* **For teachers**. While tools like ChatGPT offer numerous benefits for the educational sector, they also present opportunities for students to cheat on assignments and exams. 
Therefore, it is crucial to differentiate between responses authored by genuine students and those generated by LLMs.
* **For bloggers**. Recently many bloggers faced with a lot of ai-generated comments in 
their social networks. These comments are not really meaningful but attract the attention of their audience and promote unrelated products.
With our subnet, you can easily identify which comments are ai-generated and automatically ban them.

And many more, like:
* **For writers**.  By utilizing an LLM detection system, writers can assess their text segment by segment to identify sections that appear
machine-generated. This enables them to refine these areas to enhance the overall human-like quality of their writing.
* **For recruiting**. Have you also noticed receiving far more applications with lower candidate quality?
AI has enabled people to spam hiring teams with artificially written cover 
letters and assessments. We help you find the candidates who care about your mission and your quality standards.
* **For cyber security**. Scammers can leverage LLMs to quickly and easily create realistic and personalized phishing emails. 
We can help you determine the provenance of any document or email you’re reviewing.

As you can see there are a lot of areas where AI detection can
be very helpful. We believe that creating llm-detection subnet
not only provides a useful tool at a good price for people to use,
but also encourages competition to make better and smarter ways to spot AI-generated content.

## Miners

We made a solid baseline model - [open-source implementation](https://github.com/BurhanUlTayyab/GPTZero/tree/main) of GPTZero, which is based on [DetectGPT: Zero-Shot Machine-Generated Text Detection
using Probability Curvature](https://arxiv.org/pdf/2301.11305v1.pdf) and counting [perplexity of fixed-length models](https://huggingface.co/docs/transformers/perplexity).

On our local validation with baseline model we got overall accuracy about 85% and f1 score 77%, while
the percantage of human-written text, which were recognized as ai-written was only 8%.

| Data Source               | Accuracy |
|---------------------------|-----------|
| LLM (gpt-3.5-turbo )      | 0.880    |
| LLM (gpt-4-turbo-preview) | 0.720    |
| LLM (vicuna)              | 0.840    |
| LLM (mistral)             | 0.880    |
| Human-data                | 0.895    |

## Validators

For validating we use two types of data, which is balanced in proportion 1:1.

### Human-written texts
To gather human-written validation data we use [C4 dataset](https://huggingface.co/datasets/c4).

C4 dataset is a collection of about 750GB of English-language text sourced from the public Common Crawl web scrape. 
It includes heuristics to extract only natural language (as opposed to boilerplate and other gibberish) in addition
to extensive deduplication.

### AI-generated texts
For AI-generated text collection, we utilize the English section of the [hc3 dataset](https://huggingface.co/datasets/Hello-SimpleAI/HC3),
which includes various prompts, human responses, and ChatGPT-generated answers.
To prevent overfitting on this dataset, we exclude ChatGPT answers and 
instead run Large Language Models on random prompts from hc3 each time we conduct validation data.

We use the [Ollama GitHub repository](https://github.com/ollama) to run Large Language Models.
Currently, we are using only Vicuna and Mistral models for text completion, but we are going
to extend them in future to improve the robustness of our metrics.

## Reward counting
Based on [Detecting LLM-Generated Text in Computing Education](https://arxiv.org/pdf/2307.07411.pdf) 
article we decided to dived our reward on 3 parts:

#### F1 score
We decided to use it instead of classic accuracy, because
it better represent quality of model especially on binary-classification tasks.

#### False Positive score
FP_score = 1 - FP / len(samples).

It is usually more important not to mistakenly classify human-written text as AI-generated than the other way around.
It is preferable to tolerate a few more instances of student cheating or read some AI-generated emails than to wrongly penalize a real student or miss an important letter.

#### AP score
AP summarizes a precision-recall curve by calculating the weighted mean of precisions achieved at each threshold.
This allows us to evaluate the quality of the model's ranking.


The final reward is the average of these three values.
