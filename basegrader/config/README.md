# Register custom graders

Register custom graders by putting a JSON file for each grader with the following content:

```
{
  "name": "name of the grader",
  "url": "url where grader is exposed"
}
```

Suppose you have a multiple choice grader that exposes a handler at ```/grader/api/multiplechoice```, put a file named ```mc.json``` with the content:

```
{
  "name": "multiplechoice_grader",
  "url": "/grader/api/multiplechoice"
}
```