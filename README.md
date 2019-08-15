# hbrsgrader

This repository provides Jupyter Notebook server extensions that expose grading services.

The idea behind this is to build a modular grading architecture that can be easily extended.

## 1. Base Grader

The base grader exposes a handler at ```/grader/api/base``` that provides the list of available graders.

The list of available graders is stored in JSON format at 
```<sys_prefix>/usr/share/grader/```
with one JSON file per grader.

Each grader is registered with a name and url at which the grading service is exposed.

Suppose you have a multiple choice grader that is exposed at ```/grader/api/multiplechoice```.

Then you can put a file called ```mc.json``` in the folder ```<sys_prefix>/usr/share/grader/``` with the following content:

```
{
    "name": "multiplechoice",
    "url": "/grader/api/multiplechoice"
}
```

## 2. Custom Graders

Each custom grader needs to expose a handler for ```POST``` requests that accepts a JSON request of the following form:

```
{
    "task": {
        "cells": [...]
    },
    "solution": {
        "cells": [...]
    }
}
```

Here ```task``` is the student answer consisting of a list of cells. The field ```solution``` holds the cells of the reference solution.

A custom grader is expected to respond with a JSON response of the form:

```
{
    "grade": 0.5,
    "feedback": "partially correct"
}
```

where ```grade``` is a number from 0-1 indicating the percentage to which the answer is correct. The field ```feedback``` holds additional feedback or errors from the grading process.



