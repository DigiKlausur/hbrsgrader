# Tutorial

## 1. Template

Take this custom grader as a template

## 2. Implement your grader

Open the file ```api_handlers.py``` and create your own handler class.

Make sure that you expose a ```post``` function that takes a JSON request in the format:

```
{
  "task": {
    "cells": []
  },
  "solution": {
    "cells": []
  }
}
```

Here ```task``` will hold all the cells of the student answer for a given task and ```solution``` will hold the corresponding cells from the reference solution.

You can get the body of the JSON request by calling ```self.get_json_body()```.

Your grader should return a JSON response in the format:

```
{
  "grade": 0.3,
  "feedback": "partially correct"
}
```

Here ```grade``` is a float between 0 and 1, indicating the percentage to which the student answer is correct. The field ```feedback``` can hold additional information as a string.

## 3. Specify the server extension paths

Open the file ```__init__.py``` and edit the function ```_jupyter_server_extension_paths()```.

Change the name of the module to your module.


## 4. Write your config files

### 4.1 Grader config file

This file registers the grader with the base grader service.

Go to the folder ```config``` and create a JSON file in it that should be named like your grader (e.g. ```customgrader.json```).

The config file needs to have two fields, ```name``` and ```url```, where ```url``` specifies where the grader is exposed (e.g. ```/grader/api/customgrader```).

### 4.2 Jupyter config file

This file registers your server extension with the Jupyter Notebook.

Go to the folder ```jupyter-config/jupyter_notebook_config.d/``` and create a JSON file named like your grader (e.g. ```customgrader.json```.

The content of the file should look like this:

```
{
    "NotebookApp": {
        "nbserver_extensions": {
            "customgrader": true
        }
    }
}
```

Here ```customgrader``` is the name of your Python module.

## 5. Adapt the setup file

Open the file ```setup.py``` and make sure to name everything according to your grader.
