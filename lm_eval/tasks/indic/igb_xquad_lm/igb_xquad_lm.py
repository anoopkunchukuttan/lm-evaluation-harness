from lm_eval.api.task import ConfigurableTask
import copy
import re

class IGB_XQuad_LM(ConfigurableTask):
    VERSION = 1
    DATASET_PATH = "google/IndicGenBench_xquad_in"
    TEXT_FIELD = "context"

    COMMON_CONFIG = {
        "metadata": {"version": VERSION},
        "task": f"igb_xquad_lm",
        "tag": "igb_xquad_lm",
        "dataset_path": DATASET_PATH,
        "dataset_kwargs": {"field": "examples"},
        "output_type": "loglikelihood_rolling",
        "doc_to_text": "{{"+ TEXT_FIELD + "}}",
        "doc_to_target": "{{"+ TEXT_FIELD + "}}",
        "metric_list": [
            {
                "metric": "word_perplexity",
                # "aggregation": "mean",
                "higher_is_better": False,
            },                    {
                "metric": "byte_perplexity",
                # "aggregation": "mean",
                "higher_is_better": False,
            },
            {
                "metric": "bits_per_byte",
                # "aggregation": "mean",
                "higher_is_better": False,
            },                               
        ],
    }    
    
    def __init__(self, config=None):

        super().__init__(
            config=config
        )

    def has_training_docs(self):
        return True

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return True

    def training_docs(self):
        return self.create_docs("train")

    def validation_docs(self):
        return self.create_docs("validation")

    def test_docs(self):
        return self.create_docs("test")

    def should_decontaminate(self):
        return False

    def process_results(self, doc, results):
        (loglikelihood,) = results
        
        # Get the text for the specific language
        text = doc.get(self.TEXT_FIELD, "")
        
        # Count words and bytes
        _words = len(re.split(r"\s+", text))
        _bytes = len(text.encode("utf-8"))
        
        return {
            "word_perplexity": (loglikelihood, _words),
            "byte_perplexity": (loglikelihood, _bytes),
            "bits_per_byte": (loglikelihood, _bytes),
        }

class Hi_IGB_XQuad_LM(IGB_XQuad_LM):

    LANG = "hi"

    def __init__(self, config=None):

        lang_config = copy.deepcopy(self.COMMON_CONFIG)
        lang_config["task"] = f"igb_xquad_lm_{self.LANG}"

        super().__init__(config=lang_config)

    def create_docs(self, split):
        return self.dataset[split].filter(
            lambda example: example["lang"] == self.LANG,
            num_proc=8,
            desc=f"Dropping {split} instances whose language is not {self.LANG}",
        )

class En_IGB_XQuad_LM(IGB_XQuad_LM):

    LANG = "en"

    def __init__(self, config=None):

        lang_config = copy.deepcopy(self.COMMON_CONFIG)
        lang_config["task"] = f"igb_xquad_lm_{self.LANG}"

        super().__init__(config=lang_config)

    def create_docs(self, split):
        return self.dataset[split].filter(
            lambda example: example["lang"] == self.LANG,
            num_proc=8,
            desc=f"Dropping {split} instances whose language is not {self.LANG}",
        )

class Ml_IGB_XQuad_LM(IGB_XQuad_LM):

    LANG = "ml"

    def __init__(self, config=None):

        lang_config = copy.deepcopy(self.COMMON_CONFIG)
        lang_config["task"] = f"igb_xquad_lm_{self.LANG}"

        super().__init__(config=lang_config)

    def create_docs(self, split):
        return self.dataset[split].filter(
            lambda example: example["lang"] == self.LANG,
            num_proc=8,
            desc=f"Dropping {split} instances whose language is not {self.LANG}",
        )

