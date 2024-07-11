Experiments with <https://ukgovernmentbeis.github.io/inspect_ai/> for the Ai as Infrastructure (<https://aiinfra.anu.edu.au>) project.

<https://ukgovernmentbeis.github.io/inspect_ai/>

# Quick Start (run in terminal)

```
inspect eval theory_of_mind.py --model openai/gpt-4
```
```
inspect eval theory_of_mind.py --model ollama/llama3
```
```
inspect view
```

# Note
You can evaluate multiple models in parallel by passing a list of models to the eval() function. For example:

```
eval("mathematics.py", model=[
    "openai/gpt-4-turbo",
    "anthropic/claude-3-opus-20240229",
    "google/gemini-1.5-pro"
])
```

