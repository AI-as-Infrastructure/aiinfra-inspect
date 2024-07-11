# https://ukgovernmentbeis.github.io/inspect_ai/

# inspect eval theory_of_mind.py --model openai/gpt-4
# inspect eval theory_of_mind.py --model ollama/llama3
# inspect view

from inspect_ai import Task, eval, task
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import (               
  chain_of_thought, generate, self_critique   
) 

from dotenv import load_dotenv
load_dotenv() 

@task
def theory_of_mind():
    return Task(
        dataset=example_dataset("theory_of_mind"),
        plan=[
          chain_of_thought(),
          generate(),
          self_critique()
        ],
        scorer=model_graded_fact()
    )