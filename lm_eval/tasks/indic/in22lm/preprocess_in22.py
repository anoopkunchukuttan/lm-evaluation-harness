import re

def create_process_results(language_code):
    """Factory function that creates a process_results function for a specific language"""
    def process_results(doc, results):
        (loglikelihood,) = results
        # language_code is available here via closure
        field_name = f"{language_code}"  # e.g., "hin_Deva"
        
        _words = len(re.split(r"\s+", doc[field_name]))
        _bytes = len(doc[field_name].encode("utf-8"))
        
        return {
            "word_perplexity": (loglikelihood, _words),
            "byte_perplexity": (loglikelihood, _bytes),
            "bits_per_byte": (loglikelihood, _bytes),
        }
    return process_results

# Create specific functions
process_results_hin_Deva = create_process_results("hin_Deva")
process_results_eng_Latn = create_process_results("eng_Latn")