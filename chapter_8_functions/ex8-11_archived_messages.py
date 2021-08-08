# 8-11: ARCHIVED MESSAGES

def send_messages(txt, sent):
    while txt:
        t = txt.pop()
        print(t)
        sent.append(t)

texts = ["u up?", "on my way", "can u get milk?"]
more_sent_texts = []

send_messages(txt = texts[:], sent = more_sent_texts)

print(texts)
print(more_sent_texts)