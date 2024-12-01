from inverted_index import InvertedIndex
from boolean_retrieval import BooleanRetrieval
import pyfiglet

def main():
    print(pyfiglet.figlet_format("PART 1"))
    # parser = InvertedIndex('./dataset')
    parser = InvertedIndex('textretrieval-exc1\dataset')
    parser.extract_docs(limit=40)
    parser.extract_indices_from_text(limit=500)
    # parser.print_top_n_words(n=20)
    # parser.print_bottom_n_words(n=20)

    print(pyfiglet.figlet_format("PART 2"))
    q_path = 'textretrieval-exc1\BooleanQueries.txt'
    b_retiver = BooleanRetrieval(parser, queries_path=q_path)
    for query in b_retiver.queries():
        print(f"Query: {query}")
        print(f"Result: {b_retiver.process_query_rpn(query)}")
    
if __name__=="__main__":
    main()