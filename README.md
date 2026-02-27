# MCP triggers for Corelyn

1. **create_new_project.py**

	|- > Ever wanted to create a html project from AI

	|- > 1. Download the file

	|- > 2. Run it

	|- > 3. create a trigger named new_html_project with the code :

	```javascript
	fetch("http://127.0.0.1:5000/create", {
	                method: "POST"
	            })
	            .then(response => response.json())
	            .then(data => {
	                console.log(data);
	                alert(data.message || data.error);
	            })
	            .catch(error => {
	                console.error("Error:", error);
	            });
	```
