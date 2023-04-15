import tiktoken
from typing import List

def encoding_for_model(model: str) -> str:
	encoding = tiktoken.encoding_for_model(model)
	return encoding.name

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def array_to_markdown_table(array: List[List[str]]) -> str:
    table = []

    # Calculate the maximum width for each column
    column_widths = [max(len(str(cell)) for cell in col) for col in zip(*array)]

    # Generate the table header
    header = "| " + " | ".join(str(cell).ljust(width) for cell, width in zip(array[0], column_widths)) + " |"
    table.append(header)

    # Generate the table separator
    separator = "|-" + "-|-".join("-" * width for width in column_widths) + "-|"
    table.append(separator)

    # Generate the table rows
    for row in array[1:]:
        table_row = "| " + " | ".join(str(cell).ljust(width) for cell, width in zip(row, column_widths)) + " |"
        table.append(table_row)

    return "\n".join(table)


questions = [
    "What does favCountParams do?",
    "is it Likes + Bookmarks, or not clear from the code?",
    "What are the major negative modifiers that lower your linear ranking parameters?",
    "How do you get assigned to SimClusters?",
    "What is needed to migrate from one SimClusters to another SimClusters?",
    "How much do I get boosted within my cluster?",
    "How does Heavy ranker work. what are it’s main inputs?",
    "How can one influence Heavy ranker?",
    "why threads and long tweets do so well on the platform?",
    "Are thread and long tweet creators building a following that reacts to only threads?",
    "Do you need to follow different strategies to get most followers vs to get most likes and bookmarks per tweet?",
    "Content meta data and how it impacts virality (e.g. ALT in images).",
    "What are some unexpected fingerprints for spam factors?",
    "Is there any difference between company verified checkmarks and blue verified individual checkmarks?",
]

models = ['gpt-3.5-turbo', 'gpt-4']

# Using list comprehension
encodings = [encoding_for_model(model) for model in models]

# # Using map function
# encodings = list(map(encoding_for_model, models))

table = [['question'] + models]

for question in questions:
	row = [question] + [num_tokens_from_string(question, encoding) for encoding in encodings]
	table.append(row)

print(array_to_markdown_table(table))
