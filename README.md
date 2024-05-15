# Arabic-Autocorrect-system


## Overview
The "Twitter/twhin-bert-large" model is a variant of BERT pre-trained on Twitter data, optimized for large-scale language modeling tasks. It is part of the WHIN (Wearable Health Information Networks) initiative and aims to provide socially enriched pre-trained language representations for multilingual tweet data.

## Model Information
- **Model Name:** Twitter WHIN BERT Large
- **Model Architecture:** BERT (Bidirectional Encoder Representations from Transformers)
- **Model Size:** Large
- **Language:** Multilingual
- **Training Data:** Twitter data
- **Task:** Language modeling, fine-tuned for Arabic sentence autocorrection.
  
## Fine Tune Details
- Task: Autocorrection of Arabic sentences
- Training Data: [here](https://www.kaggle.com/datasets/oyounis/cleaned-auto-correct-dataset)
- Fine-Tuning Process: The model was fine-tuned using a masked language modeling objective to predict and correct incorrect words in Arabic sentences.
  
