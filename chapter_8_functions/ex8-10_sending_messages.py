# 8-10: SENDING MESSAGES

texts = ["u up?", "on my way", "can u get milk?"]
text_out = texts[:]
sent_texts = []

def send_messages(txt, sent):
    while txt:
        t = txt.pop()
        print(t)
        sent.append(t)

send_messages(txt = text_out, sent = sent_texts)

print(text_out)
print(sent_texts)