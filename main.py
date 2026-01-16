from summarizer import summarize_text

print("Text Summarization Program")
print("Paste your long text below. Type END when finished:\n")

lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

# Join all lines into one big text
long_text = " ".join(lines)

# Get summary from model
summary = summarize_text(long_text)

print("\n----- SUMMARY -----\n")
print(summary)
