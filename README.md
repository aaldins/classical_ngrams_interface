Welcome to the Classical N-grams downloadable interface!

Developed out of the MIT Digital Humanities Lab, Classical Ngrams is a project seeking to better understand word usage and frequency in Greek and Latin literary corpora.

The Classical N-grams interface traces word usage across Greek and Latin literature, surveying our corpus for instances of a given word and tracking that word’s use across time.

With this interface, users are able to interact with our corpus and search through over 1000 Greek and Latin texts, spanning over 1000 years. This corpus of xml files is possible through the Diogenes project (https://d.iogen.es/).

This program generally consists of three separate pages:

main.py hosts our user interface (run_baby_UI), through which one can run searches and have more guided interactions with the program. Please note that lxml and bs4 are necessary to be installed for any corpus search to run.

CorpusSearch.py allows for both advanced searches of the corpus (advanced_search) and searches across the entire corpus (search_corpus), in addition to housing programs for transliteration into Greek (beta_code_transliterator) and searching individual texts (find_soup). The Beta Code transliterator is based off of the TLG's Beta Code system (http://www.tlg.uci.edu/encoding/quickbeta.pdf), with a few key differences, as noted in the docs for that function.

MetadataBits.py contains a dictionary of the metadata for the entire Classical N-grams corpus (classical_ngrams_corpus_dict), as well as a program that allows for selecting titles out of the corpus based on the texts' characteristics.

For any questions, suggestions, general comments, or for access to our corpus, please reach out to us via classicalngrams@mit.edu.
