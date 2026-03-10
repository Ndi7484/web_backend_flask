from flask import Blueprint, jsonify, request
from flask_cors import CORS
from lib.pan.task01_1 import panTask01_1
from lib.pan.task01_2 import panTask01_2
from lib.pan.task01_3 import panTask01_3

# test debug libs
from lib.test.number_np import *

api_bp = Blueprint("api", __name__)
CORS(api_bp)

TASK_FUNCTIONS = {
    "pan": {
        "task01_1": panTask01_1,
        "task01_2": panTask01_2,
        "task01_3": panTask01_3,
    }
}


@api_bp.post("/api/index")
def getTask():
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "Invalid JSON body", "details": str(e)}), 400

    # Required fields
    folder = data.get("folder")
    task = data.get("task")

    if not folder or not task:
        return jsonify({"error": "Missing required fields: folder and task"}), 400

    # Collect all optional fields into a dict
    optional_fields = {k: v for k, v in data.items() if k not in ["folder", "task"]}

    output = TASK_FUNCTIONS[folder][task](**optional_fields)

    return jsonify({"output": output})


@api_bp.get("/api/test/<int:item_id>")
def get_test_results(item_id: int):
    return jsonify({"output": numpTest() if item_id == 1 else pandTest()})


@api_bp.get("/api/data")
def get_sample_data():
    return jsonify(
        {
            "data": [
                {"id": 1, "name": "Sample Item 1", "value": 100},
                {"id": 2, "name": "Sample Item 2", "value": 200},
                {"id": 3, "name": "Sample Item 3", "value": 300},
            ],
            "total": 3,
            "timestamp": "2024-01-01T00:00:00Z",
        }
    )


@api_bp.get("/api/items/<int:item_id>")
def get_item(item_id: int):
    return jsonify(
        {
            "item": {
                "id": item_id,
                "name": f"Sample Item {item_id}",
                "value": item_id * 100,
            },
            "timestamp": "2024-01-01T00:00:00Z",
        }
    )
