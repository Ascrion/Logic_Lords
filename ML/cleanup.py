import re
from transformers import pipeline, BartTokenizer
import torch

# Step 1: Define the file names
input_file = './output.txt'
output_file = 'final_summary.txt'

# Step 2: Read the input text file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Step 3: Clean the text to remove appendices or irrelevant parts
cleaned_text = re.sub(r'(Appendix|References|Supplementary).*$', '', text, flags=re.IGNORECASE | re.DOTALL)

# Step 4: Load the tokenizer and model, and set device to GPU if available
device = 0 if torch.cuda.is_available() else -1  # 0 means using the first GPU; -1 means using CPU
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

# Step 5: Tokenize and truncate the input to a maximum of 1024 tokens
inputs = tokenizer(cleaned_text, return_tensors="pt", max_length=1024, truncation=True)

# Step 6: Convert tokens back to string for the summarizer
input_text_truncated = tokenizer.decode(inputs['input_ids'][0], skip_special_tokens=True)

# Step 7: Summarize the truncated text
summary = summarizer(input_text_truncated, max_length=500, min_length=300, do_sample=False)
summarized_text = summary[0]['summary_text']

# Step 8: Write the summary to an output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(summarized_text)

print("Advanced Summarization Complete:", output_file)
