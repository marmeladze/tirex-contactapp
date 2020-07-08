###Steps

1. Get choice
2. Resolve choice to command
3. Prompt inputs
4. Pass inputs to attached story [To make that work, you'll also need to assign a story to each command]

e.g.

```
class Command:
    def __init__(self, name, story, required_inputs):
        self.name = name
        self.story = story
        self.required_inputs = required_inputs

        ....
```

That also will require a change in run method of Application instance

```
  def run(self)
      ...
      command.story.run(**params)
      ...
```
