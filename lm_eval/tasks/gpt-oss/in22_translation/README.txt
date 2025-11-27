# IN22 Translation Tasks

This directory contains translation tasks for the IN22 dataset, which covers 22 official Indian languages. The tasks evaluate machine translation capabilities between English and various Indian languages in both directions.

## Dataset

The IN22 dataset is a benchmark for evaluating translation quality for Indian languages. It includes parallel corpora for translating between English and 22 constitutionally recognized languages of India.

## Task Overview

These tasks evaluate translation performance using automatic metrics on the IN22 test set. The tasks are structured as follows:

- **in22_gen_eng_Latn-{lang}**: Translation from English to the target language
- **in22_gen_{lang}-eng_Latn**: Translation from the target language to English

where `{lang}` is the language code from the table below.

## Supported Languages

| Language | Script | Code |
|----------|--------|------|
| Assamese | Bengali | asm_Beng |
| Bengali | Bengali | ben_Beng |
| Bodo | Devanagari | brx_Deva |
| Dogri | Devanagari | doi_Deva |
| Gujarati | Gujarati | guj_Gujr |
| Hindi | Devanagari | hin_Deva |
| Kannada | Kannada | kan_Knda |
| Kashmiri (Arabic) | Arabic | kas_Arab |
| Konkani | Devanagari | kok_Deva |
| Maithili | Devanagari | mai_Deva |
| Malayalam | Malayalam | mal_Mlym |
| Manipuri (Meitei) | Meitei | mni_Mtei |
| Marathi | Devanagari | mar_Deva |
| Nepali | Devanagari | npi_Deva |
| Odia | Odia | ory_Orya |
| Punjabi | Gurmukhi | pan_Guru |
| Sanskrit | Devanagari | san_Deva |
| Santali | Ol Chiki | sat_Olck |
| Sindhi (Devanagari) | Devanagari | snd_Deva |
| Tamil | Tamil | tam_Taml |
| Telugu | Telugu | tel_Telu |
| Urdu | Arabic | urd_Arab |