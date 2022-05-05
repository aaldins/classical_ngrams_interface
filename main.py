def run_baby_UI ():
    '''
    Requests search parameters (along MetadataBits), if any desired for an advanced search,
    then runs a search of the corpus (via CorpusSearch) and prints out results one-by-one,
    as separate lines in search_results.

    N.B. that lxml and bs4 are necessary to be installed for the corpus search to run.
    '''

    advanced_search = input("Hello. Welcome to Classical N-grams! \nWhat type of search would you like to make? \nIf you would like to make an advanced search, please type 'Yes'. Otherwise, enter 'No'. \n")
    if advanced_search == 'No':
        from CorpusSearch import search_corpus
        text_to_search = input("What text would you like to search? \nPlease note that any Greek needs to be in Beta Code. \n")
        citation_response = input("Would you like each instance of " + text_to_search + " cited and with its surrounding text? \nPlease type 'Yes' or 'No'. \n")
        if citation_response == 'Yes':
            with_citation = True
        else:
            with_citation = False
        greek_response = input("Would you like to search in Greek? \nPlease type 'Yes' or 'No'. \n")
        if greek_response == 'Yes':
            is_greek = True
        else:
            is_greek = False
        return search_corpus(text_to_search, with_citation, is_greek)

    elif advanced_search == 'Yes':
        search_values = []
        title_parameters = input("What works would you like to search? \nPlease write titles separated by commas. If you do not wish to restrict by title, please type 'continue'. \n")
        if title_parameters == 'continue':
            search_values.append([])
        else:
            titles = title_parameters.split(", ")
            search_values.append(titles)
        author_parameters = input("What authors would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by author, please type 'continue.' \nIf you are unsure which authors we have in our database, please type 'What are my options?' \n")
        if author_parameters == 'What are my options?':
            author_options = "['Achilles Tatius', 'Aelian', 'Aelius Aristides', 'Aeneas Tacitus', 'Aeschines', 'Aeschylus', 'Agathemerus', 'Ammianus Marcellinus', \n'Andocides', 'Antiphon', 'Apicius', 'Apollodorus', 'Apollonius Rhodius', 'Appendix Vergiliana', 'Appian', 'Apuleius', \n'Aratus Solensis', 'Aretaeus', 'Aristophanes', 'Aristotle', 'Arrian', 'Asclepiodotus', 'Athenaeus', 'Augustine', \n'Aulus Gellius', 'Ausonius', 'Bacchylides', 'Barnabas', 'St. Basil, Bishop of Caesarea', 'The Venerable Bede', 'Bion of Phlossa', 'Boethius', \n'Callimachus', 'Julius Caesar', 'Callistratus', 'Cassius Dio', 'Cato the Elder', 'Catullus', 'Celsus', 'Chriton', \n'Cicero', 'Claudian', 'Clement of Alexandria', 'Colluthus', 'Columella', 'Cornelius Nepos', 'Curtius Rufus', 'Demades', \n'Demetrius of Phaleron', 'Demosthenes', 'Dinarchus', 'Dio Chrysostom', 'Diodorus Siculus', 'Dionysius of Halicarnassus', 'Epictetus', 'Euclid', \n'Euripides', 'Flavius Josephus', 'Florus', 'Galen', 'Herodotus', 'Hesiod', 'Hippocrates', 'Homer', \n'Horace', 'Hyperides', 'Isaeus', 'Isocrates', 'Jerome', 'John of Damascus', 'Juvenal', 'Livy', \n'Longinus', 'Longus', 'Lucian', 'Lucretius', 'Ludovicus Dindorfius', 'Lycophron', 'Lycurgus', 'Lysias', \n'Marcus Aurelius', 'Martial', 'Minucius Felix', 'Moschus', 'Nonnus of Panopolis', 'Oppian', 'Oppian of Apamea', 'Ovid', \n'Parthenius', 'Pausanias', 'Persius', 'Petronius', 'Phaedrus', 'Philostratus Minor', 'Philostratus the Athenian', 'Philostratus the Lemnian', \n'Pindar', 'Plato', 'Plautus', 'Pliny the Elder', 'Pliny the Younger', 'Plutarch', 'Polybius', 'Proclus', \n'Procopius', 'Propertius', 'Prudentius', 'Pseudo-Plutarch', 'Quintilian', 'Quintus Cicero', 'Quintus Smyrnaeus', 'Sallust', \n'Seneca the Elder', 'Seneca the Younger', 'Sidonius Apollinaris', 'Silius Italicus', 'Sophocles', 'Statius', 'Strabo', 'Suetonius', \n'Sulpicia', 'Tacitus', 'Terence', 'Tertullian', 'Theocritus', 'Theophrastus', 'Tibullus', 'Tryphiodorus', \n'Valerius Flaccus', 'Valerius Haropocration', 'Valerius Maximus', 'Virgil', 'Vitruvius', 'Xenophon', 'Historia Augusta', 'New Testament', 'Anonymous', 'Various', 'Unknown']"
            explained_author_parameters = input("These are the options: \n" + author_options + "\n\nWhat authors would you like to search? Please write these separated by commas. If you do not wish to restrict by author, please type 'continue'. \n")
            if explained_author_parameters == 'continue':
                search_values.append([])
            else:
                authors = explained_author_parameters.split(", ")
                search_values.append(authors)
        elif author_parameters == 'continue':
            search_values.append([])
        else:
            authors = author_parameters.split(", ")
            search_values.append(authors)
        language_parameters = input("What languages would you like to search? \nPlease write either 'Latin', 'Greek', or 'both'. \n")
        search_values.append(language_parameters)
        century_parameters = input("What centuries would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by century, please type 'continue.' \nIf you are unsure which centuries we have in our database, please type 'What are my options?' \n")
        if century_parameters == 'What are my options?':
            century_options = "['8th BCE', '6th BCE', '5th BCE', '4th BCE', '3rd BCE', '2nd BCE', '1st BCE', '1st CE', '2nd CE', '3rd CE', '4th CE', '5th CE', '6th CE', '7th CE', '19th CE', 'Varied']"
            explained_century_parameters = input("These are the options: \n" + century_options + "\n\nWhat centuries would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by century, please type 'continue'. \n")
            if explained_century_parameters == 'continue':
                search_values.append([])
            else:
                centuries = explained_century_parameters.split(", ")
                search_values.append(centuries)
        elif century_parameters == 'continue':
            search_values.append([])
        else:
            centuries = century_parameters.split(", ")
            search_values.append(centuries)
        modern_location_parameters = input("What modern locations would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by modern location, please type 'continue.' \nIf you are unsure which modern locations we have in our database, please type 'What are my options?' \n")
        if modern_location_parameters == 'What are my options?':
            modern_location_options = "['Algeria', 'Egypt', 'England', 'France', 'Germany', 'Greece', 'Israel', 'Italy', 'Macedonia', 'Romania', 'Tunisia', 'Turkey', 'Unknown']"
            explained_modern_location_parameters = input("These are the options: \n" + modern_location_options + "\n\nWhat modern locations would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by modern locations, please type 'continue'. \n")
            if explained_modern_location_parameters == 'continue':
                search_values.append([])
            else:
                modern_locations = explained_modern_location_parameters.split(", ")
                search_values.append(modern_locations)
        elif modern_location_parameters == 'continue':
            search_values.append([])
        else:
            modern_locations = modern_location_parameters.split(", ")
            search_values.append(modern_locations)
        specific_location_parameters = input("What specific locations would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by specific location, please type 'continue.' \nIf you are unsure which locations we have in our database, please type 'What are my options?' \n")
        if specific_location_parameters == 'What are my options?':
            specific_location_options = "['Alexandria', 'Amasia', 'Anazarba', 'Apamea', 'Aphrodisias', 'Ascra', 'Athens', 'Bithynia', \n'Boeotia', 'Burdigala', 'Caesarea', 'Carthage', 'Ceus', 'Chaeronea', 'Chios', 'Corinth', \n'Corsica', 'Cos', 'Ephesus', 'Eresos', 'Gaul', 'Halicarnassus', 'Jerusalem', 'Leipzig', \n'Lemnos', 'Lesbos', 'Lycopolis', 'Lydia', 'Megalopolis', 'Monkwearmouth-Jarrow', 'Mysia', 'Naucratis', \n'Nicaea', 'Nicopolis', 'Panopolis', 'Patmos', 'Pavia', 'Pergamum', 'Phalerum', 'Prusa', \n'Rome', 'Sicily', 'Smyrna', 'Soli', 'Stymphalus', 'Syracuse', 'Tagaste', 'Thurium', 'Tomis', 'Unknown']"
            explained_specific_location_parameters = input("These are the options: \n" + specific_location_options + "\n\nWhat specific locations would you like to search? \nPlease write these separated by commas. If you do not wish to restrict by specifc locations, please type 'continue'. \n")
            if explained_specific_location_parameters == 'continue':
                search_values.append([])
            else:
                specific_locations = explained_specific_location_parameters.split(", ")
                search_values.append(specific_locations)
        elif specific_location_parameters == 'continue':
            search_values.append([])
        else:
            specific_locations = specific_location_parameters.split(", ")
            search_values.append(specific_locations)

        from MetadataBits import metadata_search

        advanced_works_list = metadata_search(search_values)

        from CorpusSearch import advanced_search
        text_to_search = input("What text would you like to search? \nPlease note that any Greek needs to be in Beta Code. \n")
        citation_response = input("Would you like each instance of " + text_to_search + " cited and with its surrounding text? \nPlease type 'Yes' or 'No'. \n")
        if citation_response == 'Yes':
            with_citation = True
        else:
            with_citation = False
        greek_response = input("Would you like to search in Greek? \nPlease type 'Yes' or 'No'. \n")
        if greek_response == 'Yes':
            is_greek = True
        else:
            is_greek = False
        return advanced_search(advanced_works_list, text_to_search, with_citation, is_greek)

print(run_baby_UI())