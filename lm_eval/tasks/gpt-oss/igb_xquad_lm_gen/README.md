# IGB XQuAD LM Generation Task

## Overview

The `igb_xquad_lm_gen` task evaluates language models on extractive question-answering using the IndicGenBench XQuAD-IN dataset in a generation format similar to SQuAD completion. Unlike the original `igb_xquad_lm` task which uses language modeling perplexity, this task requires models to generate answers based on context and questions.

## Task Format

**Input Format:**
```
Context: [passage text]
Question: [question text]
Answer:
```

**Expected Output:**
The model should generate the answer text that corresponds to the correct answer found in the passage.

## Supported Languages

This task supports 12 Indian languages plus English:

- `igb_xquad_lm_gen_hi`: Hindi
- `igb_xquad_lm_gen_en`: English  
- `igb_xquad_lm_gen_as`: Assamese
- `igb_xquad_lm_gen_bn`: Bengali
- `igb_xquad_lm_gen_gu`: Gujarati
- `igb_xquad_lm_gen_kn`: Kannada
- `igb_xquad_lm_gen_ml`: Malayalam
- `igb_xquad_lm_gen_mr`: Marathi
- `igb_xquad_lm_gen_or`: Odia
- `igb_xquad_lm_gen_pa`: Punjabi
- `igb_xquad_lm_gen_ta`: Tamil
- `igb_xquad_lm_gen_te`: Telugu

## Dataset

- **Source:** `google/IndicGenBench_xquad_in`
- **Splits:** train, validation, test
- **Language filtering:** Each task variant filters examples to only include the specified language

## Evaluation Metrics

The task uses two evaluation metrics:

1. **contains**: Checks if any of the correct answers appears anywhere in the generated text (case-insensitive substring match)
2. **exact_match**: Checks if the generated text exactly matches any of the correct answers (after normalization - stripping whitespace and lowercasing)

## Generation Parameters

- **until**: `["\n", "Context:", "Question:"]` - Stop generation at newlines or when context/question patterns appear
- **max_gen_toks**: `64` - Maximum number of tokens to generate

## Comparison with Related Tasks

### vs. `igb_xquad_lm` (Original)
- **Original**: Language modeling perplexity evaluation (loglikelihood_rolling)
- **This task**: Extractive QA generation (generate_until)
- **Advantage**: This task directly evaluates QA capability rather than just language modeling

### vs. `squad_completion`
- **SQuAD**: English-only, uses hazyresearch/based-squad dataset
- **This task**: Multilingual Indian languages, uses IndicGenBench XQuAD-IN
- **Similarity**: Both use generation-based evaluation with similar metrics

## Generating Configuration Files

The task includes utilities to automatically generate configuration files for all supported languages:

### Method 1: Using the Python generator script

```bash
cd lm_eval/tasks/gpt-oss/igb_xquad_lm_gen
python generate_configs.py
```

This will:
- Validate that all language classes exist in `igb_xquad_lm_gen.py`
- Generate individual YAML config files for each language
- Generate the main group YAML file
- Provide usage examples and summary

### Method 2: Using the quick regeneration script

```bash
cd lm_eval/tasks/gpt-oss/igb_xquad_lm_gen
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

2. Add the corresponding class to `igb_xquad_lm_gen.py`:
   ```python
   class IGB_XQuad_LM_Gen_Xx(IGB_XQuad_LM_Gen_Lang):
       LANG = "xx"
   ```

3. Run the generator script:
   ```bash
   python generate_configs.py
   ```

## Usage

```bash
# Run all languages
lm_eval --model hf --model_args pretrained=your_model --tasks igb_xquad_lm_gen

# Run specific language
lm_eval --model hf --model_args pretrained=your_model --tasks igb_xquad_lm_gen_hi

# Run multiple languages
lm_eval --model hf --model_args pretrained=your_model --tasks igb_xquad_lm_gen_hi,igb_xquad_lm_gen_en
```

## Citation

If you use this task, please cite:

```
@article{gala2024indicgenbench,
  title={IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages},
  author={Gala, Jay and Kunchukuttan, Anoop and others},
  journal={arXiv preprint arXiv:2407.20053},
  year={2024}
}
```

Original XQuAD paper:
```
@article{Artetxe:etal:2019,
  author    = {Mikel Artetxe and Sebastian Ruder and Dani Yogatama},
  title     = {On the cross-lingual transferability of monolingual representations},
  journal   = {CoRR},
  volume    = {abs/1910.11856},
  year      = {2019},
}
```