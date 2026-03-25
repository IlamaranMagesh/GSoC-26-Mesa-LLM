import coverage
import json
import ast
import collections
import os


def get_function_line_ranges(filepath):
    """Parses a Python file and maps line numbers to function/class names."""
    line_to_func = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()

        # Parse the source code into an Abstract Syntax Tree
        tree = ast.parse(source, filename=filepath)

        for node in ast.walk(tree):
            # Check for functions, async functions, or classes
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                # Map every line inside the function to the function's name
                # (Note: end_lineno requires Python 3.8+)
                if hasattr(node, 'end_lineno') and node.end_lineno is not None:
                    for line in range(node.lineno, node.end_lineno + 1):
                        line_to_func[line] = node.name
    except Exception as e:
        print(f"Skipping AST parse for {filepath}: {e}")

    return line_to_func


def generate_coverage_mapping(coverage_file=".coverage", output_file="test_mapping.json"):
    if not os.path.exists(coverage_file):
        print(f"Error: Could not find '{coverage_file}'. Did you run pytest with --cov-context=test?")
        return

    # 1. Load the coverage data via the official API
    data = coverage.CoverageData(coverage_file)
    data.read()

    # Dictionary to hold our final mapping: {filepath: {function_name: set(tests)}}
    mapping = collections.defaultdict(lambda: collections.defaultdict(set))

    # 2. Iterate through every file measured by coverage
    for filepath in data.measured_files():

        # Get the mapping of line numbers to test names
        contexts_by_line = data.contexts_by_lineno(filepath)

        # Get the mapping of line numbers to function names
        line_to_func = get_function_line_ranges(filepath)

        for lineno, contexts in contexts_by_line.items():
            # Filter out empty contexts (code executed during import/setup, not by a specific test)
            test_names = [ctx for ctx in contexts if ctx]

            if not test_names:
                continue

            # Determine if the line belongs to a function, otherwise label it as module-level
            func_name = line_to_func.get(lineno, "<module_level_code>")

            # Add the tests to our mapping
            for test in test_names:
                # Strip out any parameterized pytest data (optional, but keeps the list cleaner)
                clean_test_name = test.split('|')[0]
                mapping[filepath][func_name].add(clean_test_name)

    # 3. Convert sets to lists so we can export to JSON
    final_mapping = {}
    for filepath, funcs in mapping.items():
        # Keep relative paths for cleaner output
        rel_path = os.path.relpath(filepath)
        final_mapping[rel_path] = {func: list(tests) for func, tests in funcs.items()}

    # 4. Save to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_mapping, f, indent=4)

    print(f"Success! Mapping written to {output_file}")


if __name__ == "__main__":
    generate_coverage_mapping()