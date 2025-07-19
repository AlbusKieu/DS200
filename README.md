
# Events Extraction from Vietnamese Political News

## 📰 Introduction

This project focuses on extracting political event information from Vietnamese news articles, mainly collected from [baochinhphu.vn](https://baochinhphu.vn). The main objectives are:

- Event Trigger Tagging  
- Argument Detection  
- Event Type Classification  

The project supports automatic and accurate analysis of political information in Vietnamese.

---

## 🔄 Data Processing Pipeline

### 📥 Data Collection
- Crawl articles from sources such as **baochinhphu.vn** and **vnexpress.net**.
- Mainly use data from **baochinhphu.vn** due to its focus on political content.

### ⚙️ Preprocessing & Labeling
- Sentence and word segmentation, and labeling each token according to three criteria:
  - **Trigger Tagging**: Identify words/phrases that trigger events.
  - **Argument Detection**: Identify components such as subject, location, time, etc.
  - **Event Type Classification**: Classify the type of event.

---

## 🧠 Model Approaches

### 1. 📍 Pipeline Approach
- **Trigger Tagging**: Use XLM-RoBERTa model to identify triggers.
- **Argument Detection**: Continue using XLM-RoBERTa based on identified triggers.
- **Event Type Classification**: Classify event type from the entire sentence.
- Each step is a separate model, linked in a pipeline.

### 2. 🔗 Joint Learning (OneIE-based)
- Integrated model that simultaneously trains all 3 tasks:
  - Trigger Tagging
  - Argument Detection
  - Event Type Classification
- Uses **XLM-RoBERTa** as the backbone.
- Leverages information between tasks to improve model performance.

---

## 📁 Main Directory and File Structure

| File / Folder                  | Description |
|-------------------------------|-------------|
| `baochinhphu_crawler.ipynb`   | Crawl data from baochinhphu.vn |
| `autolabel.ipynb`             | Automatic labeling using rule-based + Gemini Flash 2.5 |
| `token_tags.ipynb`            | BIO labeling for tasks |
| `json_to_csv.ipynb`           | Convert data from JSON to CSV |
| `Pipeline_Joint_Learning.ipynb` | Train and evaluate models |
| `results.csv`, `final_output.csv` | Labeled data (manual + automatic) |
| `streaming/`                  | Streaming using Kafka and Spark |
| `oneie_encoders/`             | Encoders and trained models |

---

## 💻 System Requirements

- Python >= 3.7  
- Required libraries:
  ```bash
  pip install transformers datasets scikit-learn torch seqeval openai pandas kafka-python pyspark

## 🚀 Quick Start Guide
### 1. Install libraries:

### 2. Run the following notebooks in order:
| Notebook                        | Function                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------|
| `baochinhphu_crawler.ipynb`     | Crawl data from baochinhphu.vn and automatically label using rule-based method |
| `autolabel.ipynb`               | Automatically label using Gemini Flash 2.5 API for remaining cases             |
| `token_tags.ipynb`              | BIO labeling for trigger, argument, event type                                 |
| `json_to_csv.ipynb`             | Convert labeled data to CSV                                                    |
| `Pipeline_Joint_Learning.ipynb` | Train pipeline and joint learning models                                       |

### 3. Real-time Inference (Streaming):
- Use the streaming/ directory to set up the Kafka pipeline.
- The inference model is OneIE-like integrated with Spark Structured Streaming.
- Configure the trained model and Kafka topic in the corresponding files.
