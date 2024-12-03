from inverted_index import InvertedIndex
from boolean_retrieval import BooleanRetrieval
#import pyfiglet


def main():
    retrievaled_q_str = ""
    # Part 1
    print("PART 1")
    parser = InvertedIndex('dataset')
    parser.extract_docs()
    parser.extract_indices_from_text()

    # Part 2
    print("PART 2")
    q_path = 'BooleanQueries.txt'
    b_retiver = BooleanRetrieval(parser, queries_path=q_path)
    for query in b_retiver.queries():
        print(f"Query: {query}")
        # print(f"Result: {b_retiver.process_query_rpn(query)}")
        retrievaled_q_str += f"Result for query \"{query}\" :\n" + " ".join([item[1] for item in b_retiver.process_query_rpn(query)]) + "\n\n"
    
    with open('Part_2.txt', 'w') as f:
        f.write(retrievaled_q_str)

    # Part 3
    print("PART 3")
    top_terms = parser.get_top_n_words(n=10)
    bottom_terms = parser.get_bottom_n_words(n=10, print=True)
    with open('Part_3.txt', 'w') as f:
        f.write("Top 10 terms:\n")
        for idx, term in enumerate(top_terms):
            f.write(f"{idx + 1}: {term}\n")
        f.write("\n")
        f.write("Bottom 10 terms:\n")
        for idx, term in enumerate(bottom_terms):
            f.write(f"{idx + 1}: {term}\n")
        f.write("\n")
        f.write("The different characteristics between the group of terms is:\n")
        f.write("The top 10 terms are preposition words, the the bottom 10 terms are words with spelling errors")

if __name__ == "__main__":
    main()
    