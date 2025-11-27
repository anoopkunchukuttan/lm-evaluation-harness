# IndicGenBench XQuad-IN LM Modeling Task

## Overview

This task adapts the [XQuad-IN dataset](https://huggingface.co/datasets/google/IndicGenBench_xquad_in) for language modeling evaluation. XQuad-IN dataset is part of [IndicGenBench](https://arxiv.org/abs/2407.09435).

This task evaluates language models on the XQuad-IN dataset, which has been repurposed for language modeling evaluation. XQuad-IN is originally a question-answering dataset containing context paragraphs, questions, and answers across multiple Indic languages.

## Dataset Repurposing

For language modeling purposes, the XQuad-IN dataset is transformed as follows:

- **Context passages** from the original QA dataset are extracted and used as the primary text for perplexity evaluation
- The model is evaluated on its ability to predict the next token in these passages
- Questions and answers are excluded, focusing solely on the context paragraphs which contain natural, fluent text in each language

Note that the context passages have been professionally translated, so they are of high-quality. On the other hand, since these are translations from English there might some **translationese artifacts**. This choice of this dataset was made to ensure we have a dataset that is unlikely to be part of any LM training set - the price for this choice is to rely on potential translationese effects.

This approach allows us to measure how well language models understand and generate text in low-resource Indic languages using high-quality, multilingual parallel content.

## Evaluation Metric

The task uses **perplexity** as the primary metric to assess language model performance across different Indic languages.

## Supported languages 

| Language Code | Language Name |
|---------------|---------------|
| as | Assamese |
| bn | Bengali |
| gu | Gujarati |
| hi | Hindi |
| kn | Kannada |
| ml | Malayalam |
| mr | Marathi |
| or | Odia |
| pa | Punjabi |
| ta | Tamil |
| te | Telugu |
| en | English|

## Generating Configuration Files

**Note** These config generation scripts have been automatically generated using LLM and not checkec. Please check before use. 

Configuration files for all supported languages can be automatically generated using the provided scripts:

### Method 1: Using the Python generator script

```bash
cd lm_eval/tasks/indic/igb_xquad_lm
python generate_configs.py
```

This will:
- Generate individual YAML config files for each language (`igb_xquad_lm_*.yaml`)
- Generate the main group YAML file (`igb_xquad_lm.yaml`)
- Print Python class definitions that need to be manually added to `igb_xquad_lm.py`

### Method 2: Using the quick regeneration script

```bash
cd lm_eval/tasks/indic/igb_xquad_lm
python regenerate_configs.py
```

This is a wrapper script that runs `generate_configs.py` with error handling.

### Adding a New Language

To add a new language:

1. Edit `generate_configs.py` and add the language to the `LANGUAGES` list:
   ```python
   LANGUAGES = [
       # ... existing languages ...
       ("xx", "New Language Name"),
   ]
   ```

2. Run the generator script:
   ```bash
   python generate_configs.py
   ```

3. Copy the printed Python class definition and add it to `igb_xquad_lm.py`

4. Verify the generated files are correct