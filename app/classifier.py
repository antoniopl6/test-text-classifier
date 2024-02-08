from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
model_dir = "model"
tokenizer = DistilBertTokenizer.from_pretrained(model_dir)
model = DistilBertForSequenceClassification.from_pretrained(model_dir)

label_mapping = {
    0: "Solicitudes de ayuda / contacto",
    1: "Reenvío de facturas",
    2: "Consulta contratos y documentación",
    3: "Problemas con el área de clientes y problemas técnicos",
    4: "Cambios de documentación / titularidad / bajas (cambio papeleos)",
    5: "Reclamaciones y quejas",
    6: "Consultas generales"
}

def get_prediccion(email_text):
    tokenized_text = tokenizer.tokenize(email_text)
    input_ids = tokenizer.convert_tokens_to_ids(tokenized_text)
    input_ids = torch.tensor(input_ids).unsqueeze(0) 
    attention_mask = torch.ones_like(input_ids)

    model.eval()
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    predicted_label = label_mapping[predicted_class]
    
    return predicted_label