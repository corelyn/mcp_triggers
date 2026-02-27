from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_project():
    try:
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        project_path = os.path.join(documents_path, "New_project")

        os.makedirs(project_path, exist_ok=True)

        html_file_path = os.path.join(project_path, "index.html")

        html_content = """<!DOCTYPE html>
<html>
<head>
    <title>New Project</title>
</head>
<body>
    <h1>Hello, Windows World!</h1>
    <p>This is a basic index.html file.</p>
</body>
</html>
"""

        with open(html_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # ✅ Open the folder in VS Code (Windows)
        os.system(f'code "{project_path}"')

        return jsonify({
            "message": f"Project created successfully in {project_path}!"
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
