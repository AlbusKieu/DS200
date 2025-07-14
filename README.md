# Events Extraction from Vietnamese political-theme News

## 📰 Giới thiệu

Dự án này tập trung vào việc trích xuất thông tin sự kiện chính trị từ các bài báo tiếng Việt, chủ yếu thu thập từ trang web [baochinhphu.vn](https://baochinhphu.vn). Mục tiêu chính là:

- Nhận diện sự kiện (Event Trigger Tagging)  
- Xác định các thành phần liên quan (Argument Detection)  
- Phân loại loại sự kiện (Event Type Classification)  

Dự án hỗ trợ phân tích thông tin chính trị một cách tự động và chính xác trong tiếng Việt.

---

## 🔄 Quy trình xử lý dữ liệu

### 📥 Thu thập dữ liệu
- Crawl bài báo từ các trang như **baochinhphu.vn** và **vnexpress.net**.
- Chủ yếu sử dụng dữ liệu từ **baochinhphu.vn** vì tập trung vào nội dung chính trị.

### ⚙️ Tiền xử lý & Gán nhãn
- Tách câu, tách từ và gán nhãn cho từng token theo ba tiêu chí:
  - **Trigger Tagging**: Nhận diện từ/cụm từ kích hoạt sự kiện.
  - **Argument Detection**: Nhận diện các thành phần như chủ thể, địa điểm, thời gian,...
  - **Event Type Classification**: Phân loại loại sự kiện.

---

## 🧠 Các hướng tiếp cận mô hình

### 1. 📍 Pipeline Approach
- **Trigger Tagging**: Sử dụng mô hình XLM-RoBERTa để xác định trigger.
- **Argument Detection**: Sử dụng tiếp XLM-RoBERTa dựa trên trigger đã có.
- **Event Type Classification**: Phân loại loại sự kiện từ toàn bộ câu.
- Mỗi bước là một mô hình riêng biệt, liên kết theo pipeline.

### 2. 🔗 Joint Learning (OneIE-based)
- Mô hình tích hợp huấn luyện đồng thời cả 3 tác vụ:
  - Trigger Tagging
  - Argument Detection
  - Event Type Classification
- Sử dụng **XLM-RoBERTa** làm backbone.
- Tận dụng thông tin giữa các tác vụ để tăng hiệu quả mô hình.

---

## 📁 Cấu trúc thư mục và file chính

| File / Folder                  | Mô tả |
|-------------------------------|-------|
| `baochinhphu_crawler.ipynb`   | Crawl dữ liệu từ baochinhphu.vn |
| `autolabel.ipynb`             | Gán nhãn tự động bằng rule-based + Gemini Flash 2.5 |
| `token_tags.ipynb`            | Gán nhãn BIO cho các tác vụ |
| `json_to_csv.ipynb`           | Chuyển dữ liệu từ JSON sang CSV |
| `Pipeline_Joint_Learning.ipynb` | Huấn luyện và đánh giá mô hình |
| `results.csv`, `final_output.csv` | Dữ liệu đã gán nhãn (thủ công + tự động) |
| `streaming/`                  | Streaming sử dụng Kafka và Spark |
| `oneie_encoders/`             | Các encoder và mô hình huấn luyện |

---

## 💻 Yêu cầu hệ thống

- Python >= 3.7  
- Các thư viện cần thiết:
  ```bash
  pip install transformers datasets scikit-learn torch seqeval openai pandas kafka-python pyspark

## 🚀 Hướng dẫn chạy thử
### 1. Cài đặt thư viện:

### 2. Chạy tuần tự các notebook sau:
| Notebook                        | Chức năng                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------|
| `baochinhphu_crawler.ipynb`     | Crawl dữ liệu từ baochinhphu.vn và gán nhãn tự động bằng phương pháp rule-based |
| `autolabel.ipynb`               | Gán nhãn tự động bằng api của Gemini Flash 2.5 với những trường hợp còn lại     |
| `token_tags.ipynb`              | Đánh nhãn BIO cho trigger, argument, event type                                 |
| `json_to_csv.ipynb`             | Chuyển dữ liệu đã gán nhãn thành CSV                                            |
| `Pipeline_Joint_Learning.ipynb` | Huấn luyện mô hình pipeline và joint learning                                   |

### 3. Inference thời gian thực (Streaming):
- Sử dụng thư mục streaming/ để thiết lập pipeline Kafka.
- Mô hình inference là OneIE-like tích hợp với Spark Structured Streaming.
- Cấu hình mô hình huấn luyện và Kafka topic trong các file tương ứng.
