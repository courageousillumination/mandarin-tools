import argparse
from sys import stdin

from vocab import load_vocab_database_from_csv, save_to_csv, clean_vocab_list
from export_anki import create_deck
from build_translation import build_translation
# if __name__ == "__main__":
#     vocab = load_vocab_database_from_csv('vocab.csv')
#     vocab = clean_vocab_list(vocab)
#     create_deck(vocab)
#     save_to_csv(vocab, 'vocab.csv')  # Standardize


def handle_add(args):

    for line in stdin:
        # Look at the input

        # Is it in English? Let's try to translate it.

        # Is it a Character? Do the same.

        # Is it pinyin? Let's try to find the charater.
        print("You said", line)
        build_translation(line)


def handle_export(args):
    print("Loading vocabulary file")
    vocab = load_vocab_database_from_csv(args.vocab_files[0])

    if args.anki:
        print("Created new Anki deck.")
        create_deck(vocab)


def main():
    """Parse arguments, then call out to any sub functions."""

    parser = argparse.ArgumentParser(
        description="Manage Mandarin learning tools")

    subparsers = parser.add_subparsers(dest="subparser_name")

    add_vocab_parser = subparsers.add_parser('add',
                                             help="Add new vocabulary words")
    export_parser = subparsers.add_parser(
        'export', help="Export vocabulary to third party apps")
    export_parser.add_argument("vocab_files",
                               nargs="+",
                               type=str,
                               help="Vocabulary files to load and export")
    export_parser.add_argument('-a',
                               '--anki',
                               help="Export to Anki flash cards.",
                               action='store_const',
                               const=True,
                               default=False)

    args = parser.parse_args()
    if args.subparser_name == 'add':
        handle_add(args)
    elif args.subparser_name == 'export':
        handle_export(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()