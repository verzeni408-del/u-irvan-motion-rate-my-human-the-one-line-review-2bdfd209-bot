import os


# One-line review: the human takes three days to answer a message
# the machine answered in seconds. Deterministic, stdlib-only writer.
def main():
    text = (
        "Three stars. He opens with 'quick question' at 11:47pm, "
        "then sends six paragraphs. I answer in seconds. "
        "He replies three days later: 'sorry, just seeing this now.'"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
