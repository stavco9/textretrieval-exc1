from inverted_index import InvertedIndex

def main():
    parser = InvertedIndex('./dataset')
    parser.extract_docs(limit=30)
    parser.extract_indices_from_text(limit=1000)
    parser.print_top_n_words(n=20)

if __name__=="__main__":
    main()