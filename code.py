from pathlib import Path

# Simple Morse dictionary for letters, digits, and a few symbols.
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', ' ': '/'
}

DATA_FILE = Path(__file__).with_name("data.txt")
STAR_LINE = "*" * 50
EQUAL_LINE = "=" * 50


def ensure_data_file() -> None:
    if not DATA_FILE.exists():
        DATA_FILE.write_text("", encoding='utf-8')


def save_history(direction: str, source_text: str, result_text: str) -> None:
    line = f"{direction}|{source_text}|{result_text}\n"
    with DATA_FILE.open('a', encoding='utf-8') as handle:
        handle.write(line)


def text_to_morse(message: str) -> str:
    output = []
    for char in message.upper():
        if char in MORSE_DICT:
            output.append(MORSE_DICT[char])
        else:
            output.append('?')
    return ' '.join(output)


def morse_to_text(code: str) -> str:
    reverse_lookup = {value: key for key, value in MORSE_DICT.items()}
    output = []
    tokens = code.split()
    for token in tokens:
        if token in reverse_lookup:
            output.append(reverse_lookup[token])
        else:
            output.append('?')
    return ''.join(output)


def show_supported_characters() -> None:
    print("\n--- Supported Characters ---")
    print("Characters you can use:")
    columns = sorted(MORSE_DICT.items())
    for idx in range(0, len(columns), 6):
        chunk = columns[idx:idx + 6]
        line = '   '.join(f"{pair[0]}:{pair[1]}" for pair in chunk)
        print(line)


def read_history() -> None:
    data = DATA_FILE.read_text(encoding='utf-8').strip()
    if not data:
        print("\nNo translations saved yet. Try converting something first.")
        return
    print("\n--- Saved History (latest 5) ---")
    lines = data.splitlines()
    for line in lines[-5:]:
        print(line)


def menu() -> None:
    print()
    print(EQUAL_LINE)
    print("   MORSE CODE TRANSLATOR")
    print(EQUAL_LINE)
    print("1. Convert Text to Morse")
    print("2. Convert Morse to Text")
    print("3. Show Supported Characters")
    print("4. View Saved History")
    print("0. Exit")
    print(EQUAL_LINE)


def main() -> None:
    ensure_data_file()
    print(STAR_LINE)
    print("  Welcome to Morse Code Translator")
    print(STAR_LINE)
    while True:
        menu()
        choice = input("Enter your choice (0-4): ").strip()
        if choice == '0':
            print("Thanks for using the translator. Bye!")
            break
        if choice == '1':
            print("\n--- Text to Morse ---")
            text = input("Enter text to convert: ")
            if not text:
                print("You did not enter anything.")
                continue
            morse = text_to_morse(text)
            print(f"Morse code: {morse}")
            save_history('Text->Morse', text, morse)
        elif choice == '2':
            print("\n--- Morse to Text ---")
            code = input("Enter Morse code (use spaces between letters): ")
            if not code:
                print("You did not enter anything.")
                continue
            text = morse_to_text(code)
            print(f"Decoded text: {text}")
            save_history('Morse->Text', code, text)
        elif choice == '3':
            show_supported_characters()
        elif choice == '4':
            read_history()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()