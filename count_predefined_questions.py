def count_sentences(file_path, sentences):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    results = {}
    for sentence in sentences:
        count = content.count(sentence)
        results[sentence] = count
    return results

if __name__ == "__main__":
    predefined_questions = [
        "What should I do if I think a drink was drugged?",
        "Where can I get drink test kits nearby?",
        "How can I protect my drink from being tampered with?",
        "What symptoms should I look for if I feel unwell after drinking?",
        "Can the bar staff help if I suspect drink spiking?"
    ]

    results = count_sentences("chat_logs.txt", predefined_questions)
    for question, count in results.items():
        print(f'"{question}" → {count} time(s)')
