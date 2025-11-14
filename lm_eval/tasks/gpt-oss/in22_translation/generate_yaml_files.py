"""
Script to generate YAML files for IN22 translation tasks between English 
and all 22 scheduled Indian languages (in both directions).
"""

import os
from pathlib import Path

# 22 Scheduled Indian Languages with their BCP-47 codes and scripts
INDIAN_LANGUAGES = {
    'asm_Beng': 'Assamese',
    'ben_Beng': 'Bengali',
    'brx_Deva': 'Bodo',
    'doi_Deva': 'Dogri',
    'gom_Deva': 'Konkani',
    'guj_Gujr': 'Gujarati',
    'hin_Deva': 'Hindi',
    'kan_Knda': 'Kannada',
    'kas_Arab': 'Kashmiri',
    'mai_Deva': 'Maithili',
    'mal_Mlym': 'Malayalam',
    'mni_Mtei': 'Manipuri',
    'mar_Deva': 'Marathi',
    'npi_Deva': 'Nepali',
    'ory_Orya': 'Odia',
    'pan_Guru': 'Punjabi',
    'san_Deva': 'Sanskrit',
    'sat_Olck': 'Santali',
    'snd_Deva': 'Sindhi',
    'tam_Taml': 'Tamil',
    'tel_Telu': 'Telugu',
    'urd_Arab': 'Urdu',
}

ENGLISH_CODE = 'eng_Latn'
ENGLISH_NAME = 'English'


def generate_yaml_content(source_lang_code, target_lang_code, source_lang_name, target_lang_name):
    """
    Generate YAML content for a translation task.
    
    Args:
        source_lang_code: BCP-47 code for source language (e.g., 'eng_Latn')
        target_lang_code: BCP-47 code for target language (e.g., 'hin_Deva')
        source_lang_name: Human-readable name of source language
        target_lang_name: Human-readable name of target language
    
    Returns:
        String containing YAML content
    """
    yaml_content = f"""dataset_path: ai4bharat/IN22-Gen
doc_to_text: 'Translate from {source_lang_name} to {target_lang_name} (generate only the translation): {{{{{source_lang_code}}}}}'
doc_to_target: '{{{{{target_lang_code}}}}}'  
include: _in22_translation_common_yaml
task: in22_translation_gen__{source_lang_code}-{target_lang_code}
metadata:
  version: 1.0
  slang: {source_lang_code}
  tlang: {target_lang_code}
"""
    return yaml_content


def generate_all_yaml_files(output_dir=None):
    """
    Generate YAML files for all translation pairs:
    - English to each Indian language
    - Each Indian language to English
    
    Args:
        output_dir: Directory to save YAML files. If None, uses current directory.
    """
    if output_dir is None:
        output_dir = Path(__file__).parent
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generated_files = []
    
    # Generate English to Indian language files
    print("Generating English to Indian language YAML files...")
    for lang_code, lang_name in INDIAN_LANGUAGES.items():
        filename = f"in22_translation_gen__{ENGLISH_CODE}-{lang_code}.yaml"
        filepath = output_dir / filename
        
        yaml_content = generate_yaml_content(
            ENGLISH_CODE, lang_code, ENGLISH_NAME, lang_name
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(yaml_content)
        
        generated_files.append(filename)
        print(f"  ✓ Generated: {filename}")
    
    # Generate Indian language to English files
    print("\nGenerating Indian language to English YAML files...")
    for lang_code, lang_name in INDIAN_LANGUAGES.items():
        filename = f"in22_translation_gen__{lang_code}-{ENGLISH_CODE}.yaml"
        filepath = output_dir / filename
        
        yaml_content = generate_yaml_content(
            lang_code, ENGLISH_CODE, lang_name, ENGLISH_NAME
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(yaml_content)
        
        generated_files.append(filename)
        print(f"  ✓ Generated: {filename}")
    
    print(f"\n✅ Successfully generated {len(generated_files)} YAML files!")
    print(f"📁 Files saved to: {output_dir.absolute()}")
    
    return generated_files


def main():
    """Main function to run the script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate YAML files for IN22 translation tasks'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default=None,
        help='Output directory for YAML files (default: current directory)'
    )
    
    args = parser.parse_args()
    
    generate_all_yaml_files(args.output_dir)


if __name__ == '__main__':
    main()
