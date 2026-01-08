```markdown
# Image Captioning (Hugging Face VisionEncoderDecoderModel)

This repo contains a small example to generate captions from images using a pretrained VisionEncoderDecoderModel.

Model used (default):
- nlpconnect/vit-gpt2-image-captioning — Vision Transformer encoder + GPT-2 decoder

Requirements:
- Python 3.8+
- See `requirements.txt`

Install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Usage (single image):
```bash
python caption.py --image ./examples/dog.jpg
```

Usage (folder):
```bash
python caption.py --images_dir ./images --output captions.json --batch_size 8
```

Options:
- `--device` set device (e.g. `cuda` or `cpu`). Defaults to `cuda` if available.
- `--max_length` maximum output token length (default 16).
- `--num_beams` beam search size (default 4).
- `--batch_size` for folder processing (default 4).
- `--model` to override the model checkpoint (default `nlpconnect/vit-gpt2-image-captioning`).

Example:
```bash
python caption.py --image dog.jpg --num_beams 5 --max_length 20
```

Notes:
- If you use GPU make sure `torch` is installed with CUDA support.
- The script can read local image files or HTTP URLs (prefix `http://` or `https://`).

If you'd like training/fine-tuning code, evaluation metrics (BLEU/CIDEr), or a web interface (Flask/Streamlit), tell me which and I'll add it.
```