#!/usr/bin/env python3
import json
import zipfile
import os
from xml.etree import ElementTree as ET

def analyze_tm7(file_path):
    """Analyze .tm7 file and extract threat information"""
    print(f"=== ANALYZING {file_path} ===")
    
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Extract model.json if it exists
            if 'model.json' in zip_ref.namelist():
                model_data = zip_ref.read('model.json')
                model = json.loads(model_data)
                
                print(f"Model Name: {model.get('summary', {}).get('title', 'Unknown')}")
                print(f"Description: {model.get('summary', {}).get('description', 'No description')}")
                
                # Extract threats
                threats = model.get('detail', {}).get('threats', [])
                if threats:
                    print(f"\n=== THREATS FOUND ({len(threats)}) ===")
                    for i, threat in enumerate(threats[:10], 1):  # Show first 10
                        print(f"{i}. {threat.get('title', 'Unknown Threat')}")
                        print(f"   Status: {threat.get('status', 'Unknown')}")
                        print(f"   Priority: {threat.get('priority', 'Unknown')}")
                else:
                    print("\n=== NO THREATS FOUND ===")
                    
            else:
                print("No model.json found in .tm7 file")
                
    except Exception as e:
        print(f"Error analyzing .tm7 file: {e}")

# Check for .tm7 files in current directory
tm7_files = [f for f in os.listdir('.') if f.endswith('.tm7')]

if tm7_files:
    for tm7_file in tm7_files:
        analyze_tm7(tm7_file)
        print("\n" + "="*50 + "\n")
else:
    print("No .tm7 files found in current directory")
    print("Place your .tm7 file here and run: python tm7_analyzer.py")