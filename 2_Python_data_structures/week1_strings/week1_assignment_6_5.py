# Extract the value at the end of the string
text = "X-DSPAM-Confidence:    0.8475";
text_clean = text.replace(' ', '')

start_text = text_clean.find(':')
result = text_clean[start_text + 1:]
result_num = float(result)

print(result_num)