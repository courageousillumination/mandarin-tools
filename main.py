from vocab import load_vocab_database_from_csv, save_to_csv, clean_vocab_list
from export_anki import create_deck

if __name__ == "__main__":
    vocab = load_vocab_database_from_csv('vocab.csv')
    vocab = clean_vocab_list(vocab)
    create_deck(vocab)
    save_to_csv(vocab, 'vocab.csv')  # Standardize
