import json
import sys

def fill_values(node, values_map):
    if isinstance(node, dict):
        node_id = node.get("id")
        if node_id in values_map:
            node["value"] = values_map[node_id]
        for value in node.values():
            fill_values(value, values_map)
    elif isinstance(node, list):
        for item in node:
            fill_values(item, values_map)


def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py values.json tests.json report.json")
        return 

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    with open(values_path, "r", encoding="utf-8") as f:
        values_data = json.load(f)

    with open(tests_path, "r", encoding="utf-8") as f:
        tests_data = json.load(f)

    values_map = {
        item["id"]: item.get("value")
        for item in values_data.get("values", [])
    }

    fill_values(tests_data, values_map)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(tests_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()