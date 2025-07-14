import torch
import torch.nn as nn
from transformers import XLMRobertaModel

# Model cải thiện với weighted loss
class JointModel(nn.Module):
    def __init__(self, model_name, num_trigger_labels, num_arg_labels, num_event_labels, dropout_rate=0.1):
        super().__init__()
        self.xlm_roberta = XLMRobertaModel.from_pretrained(model_name)
        hidden_size = self.xlm_roberta.config.hidden_size

        self.trigger_classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_size // 2, num_trigger_labels)
        )

        self.arg_classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_size // 2, num_arg_labels)
        )

        self.event_classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_size // 2, num_event_labels)
        )

    def forward(self, input_ids, attention_mask):
        outputs = self.xlm_roberta(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = outputs.last_hidden_state
        cls_output = sequence_output[:, 0, :]

        trigger_logits = self.trigger_classifier(sequence_output)
        arg_logits = self.arg_classifier(sequence_output)
        event_logits = self.event_classifier(cls_output)

        return trigger_logits, arg_logits, event_logits