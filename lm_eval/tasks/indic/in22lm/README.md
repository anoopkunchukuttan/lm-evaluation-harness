# IN22LM

Evaluate language model quality using the IN22 texts. These are translated by humans (expert translators) - so quality is good, but translationese effect cannot be ruled out. However, since it is translated text, it is unlikely to be part of any existing corpora.  

### Paper

IndcTrans2 paper released the data: https://arxiv.org/abs/2305.16307

### Citation

```
@article{gala2023indictrans,
title={IndicTrans2: Towards High-Quality and Accessible Machine Translation Models for all 22 Scheduled Indian Languages},
author={Jay Gala and Pranjal A Chitale and A K Raghavan and Varun Gumma and Sumanth Doddapaneni and Aswanth Kumar M and Janki Atul Nawale and Anupama Sujatha and Ratish Puduppully and Vivek Raghavan and Pratyush Kumar and Mitesh M Khapra and Raj Dabre and Anoop Kunchukuttan},
journal={Transactions on Machine Learning Research},
issn={2835-8856},
year={2023},
url={https://openreview.net/forum?id=vfT4YuzAYA},
note={}
}
```

### Groups and Tasks

#### Groups

* `in22lm_gen`: measure perplexity on the IN22-gen dataset, via rolling loglikelihoods. There is a task for every language e.g. `in22lm_gen-hin_Deva`.

### Checklist

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
