from inverted_index import InvertedIndex
from boolean_retrieval import BooleanRetrieval
import pyfiglet


def main():
    retrievaled_q_str = ""
    # Part 1
    print(pyfiglet.figlet_format("PART 1"))
    # parser = InvertedIndex('./dataset')
    parser = InvertedIndex('dataset')
    parser.extract_docs()
    parser.extract_indices_from_text()
    # parser.print_top_n_words(n=20)
    # parser.print_bottom_n_words(n=20)

    # Part 2
    print(pyfiglet.figlet_format("PART 2"))
    q_path = 'BooleanQueries.txt'
    b_retiver = BooleanRetrieval(parser, queries_path=q_path)
    for query in b_retiver.queries():
        print(f"Query: {query}")
        # print(f"Result: {b_retiver.process_query_rpn(query)}")
        retrievaled_q_str += " ".join([item[1] for item in b_retiver.process_query_rpn(query)]) + "\n"
    
    with open('Part_2.txt', 'w') as f:
        f.write(retrievaled_q_str)


if __name__ == "__main__":
    main()
    