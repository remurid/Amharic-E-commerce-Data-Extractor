## 🧪 Task 4: Model Comparison & Selection

### 🎯 Objective
The goal of this task was to evaluate and compare the performance of multiple transformer-based models on the Amharic Named Entity Recognition (NER) task, and select the most suitable model for downstream usage.

---

### 🧪 Methodology

To identify the best-performing model for Amharic NER, we fine-tuned and evaluated three multilingual transformer models:

1. **BERT Multilingual Cased** (`bert-base-multilingual-cased`)  
   A strong baseline model for multilingual NLP tasks.

2. **AfroXLMR Large** (`masakhane/afroxlmr-large-ner-masakhaner-1.0_2.0`)  
   A model pre-trained and fine-tuned specifically on African languages including Amharic.

3. **Tiny BERT for Amharic** (`bert-tiny-amhari`)  
   A small model with faster inference time, intended for low-resource or edge deployment.

Each model was fine-tuned on the same labeled CoNLL-format dataset and evaluated on a held-out validation set using the following metrics:

- **F1 Score** (primary metric for NER)
- **Precision & Recall**
- **Overall Accuracy**

---

### 📊 Results

| Model                             | Epoch | Best F1 | Precision | Recall | Accuracy | Notes                            |
|----------------------------------|--------|---------|-----------|--------|----------|----------------------------------|
| `bert-base-multilingual-cased`   | 9–10   | 0.227   | 0.25      | 0.208  | 82.5%    | Reasonable, but underperforms    |
| `masakhane/afroxlmr-large-ner-masakhaner-1.0_2.0` | 7–9 | **0.723** | 0.65–0.74 | ~0.71 | **90.4%** | ✅ Best overall performance       |
| `bert-tiny-amhari`               | 10     | 0.000   | 0.000     | 0.000  | 64.2%    | ⚠️ Failed to learn meaningful tags |

---

### 🧠 Analysis

- The **AfroXLMR large** model outperformed all others across all evaluation metrics. Its F1 score of **0.723** indicates strong generalization to the validation set, and its accuracy exceeded **90%**.
- The **BERT multilingual** model achieved moderate results, indicating it can recognize entities but struggles due to its lack of Amharic-specific pretraining.
- The **Tiny Amharic BERT** was unable to learn meaningful patterns, likely due to its limited capacity and the small size of the training dataset.

---

### ✅ Model Selection

Based on the F1 score, precision-recall balance, and overall robustness, we selected:

> **✅ Selected Model:** `masakhane/afroxlmr-large-ner-masakhaner-1.0_2.0`

This model demonstrated strong performance and is well-suited for Amharic NER tasks. It will be used in the next stage for deployment and inference.

---

### 🚀 Next Steps

- Save and export the selected model
- Deploy as an inference service (API or interface)
- Optionally continue fine-tuning with more data to improve performance
