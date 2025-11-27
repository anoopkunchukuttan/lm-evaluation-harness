"""
Script to generate XQuad-IN language configuration files.

This script generates:
1. Individual YAML config files for each language
2. Python class definitions for each language in igb_xquad_lm.py
3. Updates the main group YAML file with all languages
"""

import os
from pathlib import Path

# Language configurations
LANGUAGES = [
    ("as", "Assamese"),
    ("bn", "Bengali"),
    ("en", "English"),
    ("gu", "Gujarati"),
    ("hi", "Hindi"),
    ("kn", "Kannada"),
    ("ml", "Malayalam"),
    ("mr", "Marathi"),
    ("or", "Odia"),
    ("pa", "Punjabi"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
]

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent


def generate_yaml_config(lang_code):
    """Generate individual YAML config file for a language."""
    class_name = f"{lang_code.capitalize()}_IGB_XQuad_LM"
    content = f"""task: igb_xquad_lm_{lang_code}
class: !function igb_xquad_lm.{class_name}
"""
    return content


def generate_python_class(lang_code):
    """Generate Python class definition for a language."""
    class_name = f"{lang_code.capitalize()}_IGB_XQuad_LM"
    content = f'''class {class_name}(IGB_XQuad_LM):

    LANG = "{lang_code}"

    def __init__(self, config=None):

        lang_config = copy.deepcopy(self.COMMON_CONFIG)
        lang_config["task"] = f"igb_xquad_lm_{{self.LANG}}"

        super().__init__(config=lang_config)

    def task_lang(self):
        return self.LANG
'''
    return content


def generate_group_yaml():
    """Generate the main group YAML file."""
    tasks = [f"  - igb_xquad_lm_{lang_code}" for lang_code, _ in LANGUAGES]
    content = f"""group: igb_xquad_lm
task:
{chr(10).join(tasks)}
"""
    return content


def write_yaml_configs():
    """Write individual YAML config files for all languages."""
    print("Generating individual YAML config files...")
    for lang_code, lang_name in LANGUAGES:
        filename = SCRIPT_DIR / f"igb_xquad_lm_{lang_code}.yaml"
        content = generate_yaml_config(lang_code)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Created: {filename.name} ({lang_name})")


def write_group_yaml():
    """Write the main group YAML file."""
    print("\nGenerating main group YAML file...")
    filename = SCRIPT_DIR / "igb_xquad_lm.yaml"
    content = generate_group_yaml()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Created: {filename.name}")


def print_python_classes():
    """Print Python class definitions (to be manually added to igb_xquad_lm.py)."""
    print("\n" + "="*80)
    print("Python class definitions to add to igb_xquad_lm.py:")
    print("="*80)
    print("\n# Add these classes after the IGB_XQuad_LM base class:\n")
    
    for lang_code, lang_name in LANGUAGES:
        print(generate_python_class(lang_code))


def main():
    """Main function to generate all configuration files."""
    print("XQuad-IN Configuration Generator")
    print("="*80)
    print(f"Generating configs for {len(LANGUAGES)} languages\n")
    
    # Generate individual YAML configs
    write_yaml_configs()
    
    # Generate group YAML
    write_group_yaml()
    
    # Print Python classes for manual addition
    print_python_classes()
    
    print("\n" + "="*80)
    print("Configuration generation complete!")
    print("="*80)
    print("\nNOTE: Python classes need to be manually added to igb_xquad_lm.py")
    print("      (see the output above)")


if __name__ == "__main__":
    main()
