# Data Unification Algorithm

## Overview

This project implements a data unification algorithm designed to standardize IoT sensor data from multiple formats into a single, consistent schema. The system processes JSON data from different sources and converts them into a unified format, enabling easier data analysis and integration across various IoT device manufacturers and protocols.

## System Architecture

The application follows a simple, functional architecture built in Python:

- **Single-file Processing**: Main logic contained in `main.py` with helper functions for data transformation
- **File-based Input/Output**: Processes JSON files directly from the filesystem
- **Functional Design**: Uses pure functions for data transformation, making the code testable and maintainable
- **Test-driven Approach**: Includes automated testing framework to validate transformations

## Key Components

### Core Modules

1. **main.py**: Primary application containing the data unification logic
   - `load_json_file()`: File I/O handler with error management
   - `iso_to_milliseconds()`: Timestamp conversion utility
   - `convert_format_1_to_unified()`: Transforms format 1 data structure
   - `convert_format_2_to_unified()`: Transforms format 2 data structure (to be implemented)

2. **test_runner.py**: Comprehensive testing framework
   - Validates data file integrity
   - Tests timestamp conversion accuracy
   - Verifies data transformation correctness

### Data Schemas

**Input Format 1** (`data-1.json`):
- Uses nested structure with `device_info`, `telemetry_data`, and `metadata`
- Timestamp in milliseconds since epoch
- Location data with `latitude`/`longitude` keys

**Input Format 2** (`data-2.json`):
- Uses `sensor`, `readings`, and `info` structure
- Timestamp in ISO 8601 format
- Location data with `lat`/`lng` keys

**Unified Output Format** (`data-result.json`):
- Standardized structure with `device`, `telemetry`, and `format_info`
- Consistent field naming and data types
- Unified timestamp format (milliseconds)

## Data Flow

1. **Input Processing**: Load JSON files from filesystem using `load_json_file()`
2. **Format Detection**: Identify source format based on data structure
3. **Data Transformation**: 
   - Convert timestamps to unified format (milliseconds since epoch)
   - Map field names to standardized schema
   - Preserve all telemetry data (temperature, humidity, pressure, battery)
4. **Output Generation**: Produce unified JSON structure for downstream processing

## External Dependencies

- **Python 3.11**: Runtime environment
- **Standard Library Only**: 
  - `json`: JSON parsing and serialization
  - `datetime`: Timestamp conversion utilities
  - `os`: File system operations

**No external packages required** - the solution uses only Python standard library to minimize dependencies and ensure portability.

## Deployment Strategy

- **Replit Environment**: Configured for Python 3.11 with Nix package manager
- **Workflow Automation**: Uses Replit workflows to execute the data unification process
- **Single Command Execution**: Run via `python main.py` for processing
- **File-based I/O**: Processes local JSON files, suitable for batch processing or integration into larger pipelines

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- June 25, 2025. Initial setup