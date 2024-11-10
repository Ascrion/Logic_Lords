from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer
model_name = "facebook/bart-large-cnn"  # Can replace with a different model if needed
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

def summarize_text(text, max_chunk_size=1024, max_output_tokens=100):
    """
    Summarizes any given text, handling chunking for long texts.
    Arguments:
        text (str): The input text to summarize.
        max_chunk_size (int): The max token length per chunk for input.
        max_output_tokens (int): The max length of output tokens for each summary.
    Returns:
        final_summary (str): A concise summary of the input text.
    """
    # Tokenize and chunk text if too long
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=max_chunk_size)
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    # Summarize each chunk independently
    summaries = []
    with torch.no_grad():
        for chunk in chunks:
            inputs = tokenizer(chunk, return_tensors="pt", truncation=True, padding="max_length", max_length=max_chunk_size).to(device)
            summary_ids = model.generate(
                inputs["input_ids"],
                max_length=max_output_tokens,
                min_length=30,
                num_beams=5,
                length_penalty=1.5,
                do_sample=False
            )
            summaries.append(tokenizer.decode(summary_ids[0], skip_special_tokens=True))

    # Join all summaries into a final consolidated summary
    final_summary = " ".join(summaries)
    return final_summary

# Example usage
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

summary = summarize_text(text)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("General summarization complete. Summary saved to 'output.txt'.")
