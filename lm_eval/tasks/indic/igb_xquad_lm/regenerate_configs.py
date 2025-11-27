#!/usr/bin/env python3
"""
Quick script to regenerate all XQuad-IN config files.
Run this script from the igb_xquad_lm directory.
"""

import subprocess
import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    generator_script = script_dir / "generate_configs.py"
    
    if not generator_script.exists():
        print(f"Error: {generator_script} not found!")
        sys.exit(1)
    
    print("Running configuration generator...")
    result = subprocess.run([sys.executable, str(generator_script)], cwd=script_dir)
    
    if result.returncode == 0:
        print("\n✓ Configuration files generated successfully!")
    else:
        print("\n✗ Configuration generation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
