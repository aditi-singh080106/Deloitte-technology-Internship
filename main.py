import json
from datetime import datetime
import os

def load_json_file(filename):
    """
    Helper function to load JSON data from a file
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {filename}: {e}")
        return None

def iso_to_milliseconds(iso_timestamp):
    """
    Convert ISO timestamp string to milliseconds since epoch
    """
    try:
        # Parse the ISO timestamp
        dt = datetime.fromisoformat(iso_timestamp.replace('Z', '+00:00'))
        # Convert to milliseconds since epoch
        return int(dt.timestamp() * 1000)
    except ValueError as e:
        print(f"Error converting timestamp: {e}")
        return None

def convert_format_1_to_unified(data_1):
    """
    IMPLEMENT: Convert data format 1 to unified format
    
    This function takes data in format 1 (data-1.json structure) and converts it
    to the unified format (data-result.json structure).
    
    Args:
        data_1: Dictionary containing data in format 1
"""