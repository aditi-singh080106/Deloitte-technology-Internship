#!/usr/bin/env python3
"""
Automated test runner for the Deloitte data unification assessment
"""

import json
import sys
from main import convert_format_1_to_unified, convert_format_2_to_unified, iso_to_milliseconds, load_json_file

def run_comprehensive_tests():
    """
    Run comprehensive tests to validate the solution
    """
    print("Running Deloitte Assessment Tests...")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Load and validate data files
    total_tests += 1
    print(f"\nTest {total_tests}: Data file validation")
    try:
        data_1 = load_json_file("data-1.json")
        data_2 = load_json_file("data-2.json")
        target = load_json_file("data-result.json")
        
        if data_1 and data_2 and target:
            print("✓ PASS: All data files loaded successfully")
            tests_passed += 1
        else:
            print("✗ FAIL: Could not load one or more data files")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    # Test 2: Timestamp conversion accuracy
    total_tests += 1
    print(f"\nTest {total_tests}: ISO to milliseconds conversion")
    try:
        test_cases = [
            ("2024-12-26T00:00:00.000Z", 1735171200000),
            ("2024-01-01T00:00:00.000Z", 1704067200000),
            ("2023-12-31T23:59:59.999Z", 1704067199999)
        ]
        
        all_correct = True
        for iso_time, expected_ms in test_cases:
            result = iso_to_milliseconds(iso_time)
            if result != expected_ms:
                print(f"  ✗ {iso_time} -> Expected: {expected_ms}, Got: {result}")
                all_correct = False
        
        if all_correct:
            print("✓ PASS: All timestamp conversions correct")
            tests_passed += 1
        else:
            print("✗ FAIL: Timestamp conversion errors detected")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    # Test 3: Format 1 to unified conversion
    total_tests += 1
    print(f"\nTest {total_tests}: Format 1 to unified conversion")
    try:
        data_1 = load_json_file("data-1.json")
        target = load_json_file("data-result.json")
        result = convert_format_1_to_unified(data_1)
        
        if result == target:
            print("✓ PASS: Format 1 conversion produces correct unified format")
            tests_passed += 1
        else:
            print("✗ FAIL: Format 1 conversion does not match target")
            print("  Key differences found in output structure")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    # Test 4: Format 2 to unified conversion
    total_tests += 1
    print(f"\nTest {total_tests}: Format 2 to unified conversion")
    try:
        data_2 = load_json_file("data-2.json")
        target = load_json_file("data-result.json")
        result = convert_format_2_to_unified(data_2)
        
        if result == target:
            print("✓ PASS: Format 2 conversion produces correct unified format")
            tests_passed += 1
        else:
            print("✗ FAIL: Format 2 conversion does not match target")
            print("  Key differences found in output structure")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    # Test 5: Data integrity validation
    total_tests += 1
    print(f"\nTest {total_tests}: Data integrity validation")
    try:
        data_1 = load_json_file("data-1.json")
        data_2 = load_json_file("data-2.json")
        
        result_1 = convert_format_1_to_unified(data_1)
        result_2 = convert_format_2_to_unified(data_2)
        
        # Both should produce the same unified result since they represent the same message
        if result_1 == result_2:
            print("✓ PASS: Both formats produce identical unified output")
            tests_passed += 1
        else:
            print("✗ FAIL: Format conversions produce different results")
            print("  Both input formats should yield the same unified output")
    except Exception as e:
        print(f"✗ ERROR: {e}")
    
    # Print final results
    print("\n" + "=" * 50)
    print(f"ASSESSMENT RESULTS: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 EXCELLENT! All tests passed. Your solution is ready for submission.")
        return True
    else:
        print("❌ Some tests failed. Please review your implementation.")
        print("\nHints for debugging:")
        print("- Check that your functions handle all required field mappings")
        print("- Ensure ISO timestamp conversion is accurate")
        print("- Verify the unified output structure matches the target exactly")
        return False

if __name__ == "__main__":
    success = run_comprehensive_tests()
    sys.exit(0 if success else 1)
