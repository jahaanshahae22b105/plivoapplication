from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LocalLLMDiarizer:
    def __init__(self, model_name="EleutherAI/gpt-j-6B"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
        self.model.eval()
        if torch.cuda.is_available():
            self.model.to('cuda')

    def diarize(self, transcript_text: str) -> str:
        prompt = (
            "You are an assistant that assigns speaker labels (Speaker 1, Speaker 2, ...) "
            "to this conversation transcript that has no speaker labels:\n\n"
            f"{transcript_text}\n\n"
            "Add speaker labels clearly before each utterance."
        )
        inputs = self.tokenizer(prompt, return_tensors='pt', truncation=True, max_length=1024)
        if torch.cuda.is_available():
            inputs = {k: v.to('cuda') for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
            )
        decoded = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        diarized_text = decoded[len(prompt):].strip()
        return diarized_text

# Optional helper function for direct calling

def diarize(transcript_text: str) -> str:
    diarizer = LocalLLMDiarizer()
    return diarizer.diarize(transcript_text)

    # Apply diarization to audio file
    diarization = pipeline(tmp_file_path)

    # Cleanup temp file
    os.remove(tmp_file_path)

    # Format diarization result: speaker segments with start/end and speaker labels
    diarized_text = ""
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        start_time = turn.start
        end_time = turn.end
        diarized_text += f"{speaker} [{start_time:.1f}s - {end_time:.1f}s]\n"

    return diarized_text

