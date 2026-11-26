
import json
from pathlib import Path
from jsonschema import Draft202012Validator


def validate_storyboard():
    storyboard_path = Path("storyboard.json")
    schema_path = Path("schema/storyboard.schema.json")

    # Check required files
    if not storyboard_path.exists():
        print("ERROR: storyboard.json was not found.")
        return

    if not schema_path.exists():
        print("ERROR: storyboard.schema.json was not found.")
        return

    # Load storyboard and schema
    try:
        with storyboard_path.open("r", encoding="utf-8") as file:
            storyboard = json.load(file)

        with schema_path.open("r", encoding="utf-8") as file:
            schema = json.load(file)

    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON: {error}")
        return

    # Validate the schema itself
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as error:
        print(f"ERROR: Invalid JSON Schema: {error}")
        return

    # Validate storyboard against schema
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(storyboard),
                    key=lambda error: list(error.path))

    if errors:
        print("STORYBOARD SCHEMA VALIDATION FAILED")

        for error in errors:
            location = ".".join(str(item) for item in error.path)
            print(f"- {location}: {error.message}")

        return

    print("JSON SCHEMA VALIDATION PASSED")

    # Check shot timing
    shots = storyboard.get("shots", [])

    expected_start = 0
    shot_ids = set()

    for shot in shots:
        shot_id = shot["shot_id"]
        start = shot["start_seconds"]
        duration = shot["duration_seconds"]

        if shot_id in shot_ids:
            print(f"ERROR: Duplicate shot ID: {shot_id}")
            return

        shot_ids.add(shot_id)

        if start != expected_start:
            print(
                f"ERROR: Timing gap or overlap at {shot_id}. "
                f"Expected {expected_start}, found {start}"
            )
            return

        expected_start = start + duration

    print("STORYBOARD VALID")
    print(f"Number of shots: {len(shots)}")
    print(f"Total duration: {expected_start} seconds")
    print("All shots have continuous timing.")


if __name__ == "__main__":
    validate_storyboard()
