import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

# Function to generate abstractive summary
def generate_summary(text,min,max):
    # Preprocess the text
    preprocess_text = "summarize: " + text.strip()

    # Tokenize the input text and encode it into input_ids
    input_ids = tokenizer.encode(preprocess_text, padding='max_length', truncation=True, max_length=512, return_tensors='pt')

    # Generate summary
    summary_ids = model.generate(input_ids, max_length=max, min_length=min, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode summary and return it
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


