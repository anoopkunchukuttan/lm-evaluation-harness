from lm_eval.api.task import ConfigurableTask
import copy
import re

from jinja2 import Environment
from lm_eval.tasks.indic.igb_xquad_lm.chat_templates import CHAT_TEMPLATE_MAP
import os

def render_chat_template(example):
    # Only apply chat template if environment variable is set to 1
    if os.environ.get("IGB_RENDER_CHAT_TEMPLATE") == "1" and \
       os.environ.get("IGB_RENDER_CHAT_TEMPLATE_NAME") in CHAT_TEMPLATE_MAP:
        env = Environment()
        template = env.from_string(CHAT_TEMPLATE_MAP[os.environ["IGB_RENDER_CHAT_TEMPLATE_NAME"]])
        rendered = template.render(
            messages=[
                {"role": "user", "content": example["context"]}
            ],
            bos_token="",
            add_generation_prompt=False,
        )
        return {"context_final": rendered}
    else:
        # Return the original context without applying chat template
        return {"context_final": example["context"]}

class IGB_XQuad_LM(ConfigurableTask):
    VERSION = 1
    DATASET_PATH = "google/IndicGenBench_xquad_in"
    TEXT_FIELD = "context_final"

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

    def create_docs(self, split):
        return self.dataset[split].filter(
            lambda example: example["lang"] == self.task_lang(),
            num_proc=8,
            desc=f"Dropping {split} instances whose language is not {self.LANG}",
        ).map(render_chat_template, num_proc=8)

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

    def task_lang(self):
        return self.LANG

    # def create_docs(self, split):
    #     return self.dataset[split].filter(
    #         lambda example: example["lang"] == self.LANG,
    #         num_proc=8,
    #         desc=f"Dropping {split} instances whose language is not {self.LANG}",
    #     )

class En_IGB_XQuad_LM(IGB_XQuad_LM):

    LANG = "en"

    def __init__(self, config=None):

        lang_config = copy.deepcopy(self.COMMON_CONFIG)
        lang_config["task"] = f"igb_xquad_lm_{self.LANG}"

        super().__init__(config=lang_config)

    def task_lang(self):
        return self.LANG

class Ml_IGB_XQuad_LM(IGB_XQuad_LM):

    LANG = "ml"

    def __init__(self, config=None):

        lang_config = copy.deepcopy(self.COMMON_CONFIG)
        lang_config["task"] = f"igb_xquad_lm_{self.LANG}"

        super().__init__(config=lang_config)

    def task_lang(self):
        return self.LANG

