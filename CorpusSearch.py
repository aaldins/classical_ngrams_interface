def beta_code_transliterator(beta_code: str) -> str:
    '''
    Takes in a string of Beta Coded Greek, and returns a string in Greek characters, including accents,
    iota subscripts, capitalization, finality (sigma), or breathing marks.

    N.B. that breathing marks are always written before the letter to which they correspond, a grave accent must be
    written as "]", and that final sigma is written as "J".

    Iterates through the characters in the string of Beta Code, transcribing each letter into Unicode Greek text.
    '''
    greek_letters = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ",
                     "σ", "τ", "υ", "φ", "χ", "ψ", "ω", "ς"]
    capitals = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ",
                "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
    greek_special_characters = [" ", ".", "'", ":", ";", "-", "–", ","]
    lower_accent_dict = {"A": ["α", "ά", "ὰ", "ἀ", "ἄ", "ἂ", "ἁ", "ἅ", "ἃ", "ἆ", "ἇ", "ᾶ", "ᾳ", "ᾴ", "ᾲ", "ᾷ",
                               "ᾀ", "ᾄ", "ᾂ", "ᾆ", "ᾁ", "ᾅ", "ᾃ", "ᾇ"],
                         "E": ["ε", "έ", "ὲ", "ἐ", "ἔ", "ἒ", "ἑ", "ἕ", "ἓ"],
                         "H": ["η", "ή", "ὴ", "ἠ", "ἤ", "ἢ", "ἡ", "ἥ", "ἦ", "ἣ", "ἧ", "ῆ", "ῃ", "ῄ", "ῂ", "ῇ",
                               "ᾐ", "ᾔ", "ᾒ", "ᾖ", "ᾑ", "ᾕ", "ᾓ", "ᾗ"],
                         "I": ["ι", "ί", "ὶ", "ἰ", "ἴ", "ἲ", "ἱ", "ἵ", "ἳ", "ἶ", "ἷ", "ῖ"],
                         "O": ["ο", "ό", "ὸ", "ὀ", "ὄ", "ὂ", "ὁ", "ὅ", "ὃ"],
                         "U": ["υ", "ύ", "ὺ", "ὐ", "ὔ", "ὒ", "ὑ", "ὕ", "ὓ", "ὖ", "ὗ", "ῦ"],
                         "W": ["ω", "ώ", "ὼ", "ὠ", "ὤ", "ὢ", "ὡ", "ὥ", "ὣ", "ὦ", "ὧ", "ῶ", "ῳ", "ῴ", "ῲ", "ῷ",
                               "ᾠ", "ᾤ", "ᾢ", "ᾦ", "ᾡ", "ᾥ", "ᾣ", "ᾧ"]}
    upper_accent_dict = {"A": ["Α", "Ά", "Ὰ", "Ἀ", "Ἄ", "Ἂ", "Ἁ", "Ἅ", "Ἃ", "Ἆ", "Ἇ"],
                         "E": ["Ε", "Έ", "Ὲ", "Ἐ", "Ἔ", "Ἒ", "Ἑ", "Ἕ", "Ἓ"],
                         "H": ["Η", "Ή", "Ὴ", "Ἠ", "Ἤ", "Ἢ", "Ἡ", "Ἥ", "Ἣ", "Ἦ", "Ἧ"],
                         "I": ["Ι", "Ί", "Ὶ", "Ἰ", "Ἴ", "Ἲ", "Ἱ", "Ἵ", "Ἳ", "Ἶ", "Ἷ"],
                         "O": ["Ο", "Ό", "Ὸ", "Ὀ", "Ὄ", "Ὂ", "Ὁ", "Ὅ", "Ὃ"],
                         "U": ["Υ", "Ύ", "Ὺ", "Υ", "Υ", "Υ", "Ὑ", "Ὕ", "Ὓ", "Υ", "Ὗ"],
                         "W": ["Ω", "Ώ", "Ὼ", "Ὠ", "Ὤ", "Ὤ", "Ὡ", "Ὥ", "Ὣ", "Ὦ", "Ὧ"]}
    beta_code_letters = ["A", "B", "G", "D", "E", "Z", "H", "Q", "I", "K", "L", "M", "N", "C", "O", "P", "R",
                         "S", "T", "U", "F", "X", "Y", "W", "J"]
    beta_code_vowels = ["A", "E", "H", "I", "O", "U", "W"]
    beta_code_consonants = ["B", "G", "D", "Z", "Q", "K", "L", "M", "N", "C", "P", "R", "S", "T", "F", "X", "Y", "J"]
    beta_code_special = [" ", ".", "'", ":", ";", "-", "–", ","]
    beta_accent_list = ["", "/", "]", ")", ")/", ")]", "(", "(/", "(]", ")=", "(=", "=", "|", "/|", "]|", "=|",
                        ")|", ")/|", ")]|", ")=|", "(|", "(/|", "(]|", "(=|"]
    transliterated_list = []
    beta_code_list = list(beta_code)
    length = len(beta_code_list)
    current_letter = []
    for g in beta_code_list:
        char = g
        char_ind = beta_code_list.index(char)
        if char in beta_code_special:
            ind = beta_code_special.index(char)
            transliterated_list.append(greek_special_characters[ind])
        else:
            current_letter.append(char)
            if char == "|":
                for vow in beta_code_vowels:
                    if vow in current_letter:
                        if "*" in current_letter:
                            current_letter.remove("*")
                            current_letter.remove(vow)
                            accent = "".join(current_letter)
                            letter_ind = beta_accent_list.index(accent)
                            letter_list = upper_accent_dict[vow]
                            letter = letter_list[letter_ind]
                            transliterated_list.append(letter)
                        else:
                            current_letter.remove(vow)
                            accent = "".join(current_letter)
                            letter_ind = beta_accent_list.index(accent)
                            letter_list = lower_accent_dict[vow]
                            letter = letter_list[letter_ind]
                            transliterated_list.append(letter)
                current_letter = []
            elif char in beta_code_letters:
                if beta_code_list.index(char) != length - 1:
                    if beta_code_list[char_ind + 1] != "|":
                        for vow in beta_code_vowels:
                            if vow in current_letter:
                                if "*" in current_letter:
                                    current_letter.remove("*")
                                    current_letter.remove(vow)
                                    accent = "".join(current_letter)
                                    letter_ind = beta_accent_list.index(accent)
                                    letter_list = upper_accent_dict[vow]
                                    letter = letter_list[letter_ind]
                                    transliterated_list.append(letter)
                                else:
                                    current_letter.remove(vow)
                                    accent = "".join(current_letter)
                                    letter_ind = beta_accent_list.index(accent)
                                    letter_list = lower_accent_dict[vow]
                                    letter = letter_list[letter_ind]
                                    transliterated_list.append(letter)
                        for cons in beta_code_consonants:
                            if cons in current_letter:
                                if "*" in current_letter:
                                    ind = beta_code_letters.index(char)
                                    letter = capitals[ind]
                                    transliterated_list.append(letter)
                                else:
                                    ind = beta_code_letters.index(char)
                                    letter = greek_letters[ind]
                                    transliterated_list.append(letter)
                        current_letter = []
                    else:
                        continue
                else:
                    for vow in beta_code_vowels:
                        if vow in current_letter:
                            if "*" in current_letter:
                                current_letter.remove("*")
                                current_letter.remove(vow)
                                accent = "".join(current_letter)
                                letter_ind = beta_accent_list.index(accent)
                                letter_list = upper_accent_dict[vow]
                                letter = letter_list[letter_ind]
                                transliterated_list.append(letter)
                            else:
                                current_letter.remove(vow)
                                accent = "".join(current_letter)
                                letter_ind = beta_accent_list.index(accent)
                                letter_list = lower_accent_dict[vow]
                                letter = letter_list[letter_ind]
                                transliterated_list.append(letter)
                    for cons in beta_code_consonants:
                        if cons in current_letter:
                            if "*" in current_letter:
                                ind = beta_code_letters.index(char)
                                letter = capitals[ind]
                                transliterated_list.append(letter)
                            else:
                                ind = beta_code_letters.index(char)
                                letter = greek_letters[ind]
                                transliterated_list.append(letter)
                    current_letter = []
            else:
                continue
    transliterated_beta_code = "".join(transliterated_list)
    return transliterated_beta_code

##############################################################

def find_soup (path_to_xml_file:str, beta_code:str, with_citation:bool, is_greek:bool):
    '''
    Takes in local XML file and Beta Coded Greek to search through Greek text for examples.

    First runs beta_code through beta_code_translator, then opens and searches through the XML for that text.

    Returns count of matches in the text and (if asked for the citation) a dictionary of the
    text surrounding the match, and the book/chapter/section numbers for that text.
    '''
    from bs4 import BeautifulSoup

    with open(path_to_xml_file) as file:
        content = file.read()
    soup = BeautifulSoup(content, 'lxml')

    if is_greek == True:
        text = beta_code_transliterator(beta_code)
    else:
        text = beta_code
    match_count = 0
    match_dict = {}

    divisions_to_cite = ["book", "chapter", "section", "episode", "anapests", "choral", "strophe", "antistrophe",
                         "epode", "ephymn.", "ephymn", "trochees", "iambics", "lyric", "ephymnion", "witness",
                         "witnesses", "law", "names", "Name", "tetralogy", "fragment", "subsection", "Prologue",
                         "Parodos", "Lyric-Scene", "Parabasis", "prelude", "pnigos", "epirrhema", "antepirrhema",
                         "Episode", "Choral", "Exodus", "monody", "Agon", "katakeleusmenos", "epirrheme",
                         "antikatakeleusmenos", "antepirrheme", "antipnigos", "katakeleusmos", "antikatakeleusmos",
                         "proagon", "Katakeleusmos", "Epirrheme", "Pnigos", "Antikatakeleusmos", "Antepirrheme",
                         "Antipnigos", "antistrohe", "dactyls", "sphragis", "parabasis", "tetrameters", "antiprelude",
                         "elegiacs", "proepirrheme", "antiproepirrheme", "testimonium", "inscription", "bekker page",
                         "verse", "Book", "hexameter", "dact", "iamb", "eleg", "troch", "trimeter", "poem", "statute",
                         "deposition", "terms", "decree", "challenge", "complaint", "counter-plea", "oath", "type",
                         "number", "mesode", "dialogue", "letter", "entry", "epigram", "Extract", "preface", "oracle",
                         "Verse", "paraphrase", "prose", "inscript", "verse-paraphrase", "Prose", "drama", "proverb",
                         "kommos", "praeface", "opener", "topic", "commentary", "actio", "preface", "closer", "signature",
                         "Book", "speech", "fragments", "act", "scene", "prologue", "satire", "body", "fragment", "index"]
    divisions_to_continue = ["work", "text", "edition", "Continued", "continued", "main", "NarrProof"]
    divisions_to_subtype = ["textpart", "commentary"]
    division_names = divisions_to_cite + divisions_to_continue + divisions_to_subtype + ["antistrohe", "part", "secton"]

    for div in soup.find_all(type=True):
        try:
            if div.has_attr("type") and div.get("type") in division_names:
                if div.get("type") in divisions_to_subtype:
                    first_div_name = div.get("subtype")
                    try:
                        num = div.get("n")
                        first_div_num = " " + num
                    except:
                        first_div_num = ""
                elif div.get("type") in divisions_to_cite:
                    first_div_name = div.get("type")
                    try:
                        num = div.get("n")
                        first_div_num = " " + num
                    except:
                        first_div_num = ""
                elif div.get("type" == "part"):
                    first_div_name = ""
                    try:
                        num = div.get("n")
                        first_div_num = num
                    except:
                        first_div_num = ""
                elif div.get("type") == "antistrohe":
                    first_div_name = "antistrophe"
                    try:
                        num = div.get("n")
                        first_div_num = " " + num
                    except:
                        first_div_num = ""
                elif div.get("type") == "secton":
                    first_div_name = "section"
                    try:
                        num = div.get("n")
                        first_div_num = " " + num
                    except:
                        first_div_num = ""
                elif div.get("type") in divisions_to_continue:
                    first_div_name = ""
                    first_div_num = ""
                try:
                    for child in div.children:
                        try:
                            if child.has_attr("type") and child.get("type") in division_names:
                                if child.get("type") in divisions_to_subtype:
                                    second_div_name = child.get("subtype")
                                    try:
                                        num = child.get("n")
                                        second_div_num = " " + num
                                    except:
                                        second_div_num = ""
                                elif child.get("type") in divisions_to_cite:
                                    second_div_name = child.get("type")
                                    try:
                                        num = child.get("n")
                                        second_div_num = " " + num
                                    except:
                                        second_div_num = ""
                                elif child.get("type" == "part"):
                                    second_div_name = ""
                                    try:
                                        num = child.get("n")
                                        second_div_num = num
                                    except:
                                        second_div_num = ""
                                elif child.get("type") == "antistrohe":
                                    second_div_name = "antistrophe"
                                    try:
                                        num = child.get("n")
                                        second_div_num = " " + num
                                    except:
                                        second_div_num = ""
                                elif div.get("type") == "secton":
                                    first_div_name = "section"
                                    try:
                                        num = div.get("n")
                                        first_div_num = " " + num
                                    except:
                                        first_div_num = ""
                                elif child.get("type") in divisions_to_continue:
                                    second_div_name = ""
                                    second_div_num = ""
                                try:
                                    for grandchild in child.children:
                                        try:
                                            if grandchild.has_attr("type") and grandchild.get("type") in division_names:
                                                if grandchild.get("type") in divisions_to_subtype:
                                                    third_div_name = grandchild.get("subtype")
                                                    try:
                                                        num = grandchild.get("n")
                                                        third_div_num = " " + num
                                                    except:
                                                        third_div_num = ""
                                                elif grandchild.get("type") in divisions_to_cite:
                                                    third_div_name = grandchild.get("type")
                                                    try:
                                                        num = grandchild.get("n")
                                                        third_div_num = " " + num
                                                    except:
                                                        third_div_num = ""
                                                elif grandchild.get("type" == "part"):
                                                    third_div_name = ""
                                                    try:
                                                        num = grandchild.get("n")
                                                        third_div_num = num
                                                    except:
                                                        third_div_num = ""
                                                elif grandchild.get("type") == "antistrohe":
                                                    third_div_name = "antistrophe"
                                                    try:
                                                        num = grandchild.get("n")
                                                        third_div_num = " " + num
                                                    except:
                                                        third_div_num = ""
                                                elif div.get("type") == "secton":
                                                    first_div_name = "section"
                                                    try:
                                                        num = div.get("n")
                                                        first_div_num = " " + num
                                                    except:
                                                        first_div_num = ""
                                                elif child.get("type") in divisions_to_continue:
                                                    third_div_name = ""
                                                    third_div_num = ""
                                                for l in grandchild.strings:
                                                    if text in l:
                                                        match_count += 1
                                                        if with_citation:
                                                            l_text = l
                                                            surrounding_text = l_text.strip("\n")
                                                            line_nums = False
                                                            try:
                                                                for line in grandchild.find_all("l"):
                                                                    if l in line.strings:
                                                                        line_num = line.get("n")
                                                                        line_nums = True
                                                            except:
                                                                continue
                                                            if line_nums == True:
                                                                citation = [first_div_name + first_div_num,
                                                                            second_div_name + second_div_num,
                                                                            third_div_name + third_div_num,
                                                                            "line " + line_num]
                                                            else:
                                                                citation = [first_div_name + first_div_num,
                                                                            second_div_name + second_div_num,
                                                                            third_div_name + third_div_num]
                                                            if '' in citation:
                                                                citation.remove('')
                                                            if surrounding_text in match_dict.keys():
                                                                cite_text = surrounding_text + " " + str(match_count)
                                                                match_dict[cite_text] = citation
                                                            else:
                                                                match_dict[surrounding_text] = citation
                                        except:
                                            pass
                                except:
                                    pass
                                for l in child.strings:
                                    if text in l:
                                        if with_citation:
                                            l_text = l
                                            surrounding_text = l_text.strip("\n")
                                            line_nums = False
                                            try:
                                                for line in child.find_all("l"):
                                                    if l == line.strings:
                                                        line_num = line.get("n")
                                                        line_nums = True
                                            except:
                                                continue
                                            if line_nums == True:
                                                citation = [first_div_name + first_div_num,
                                                            second_div_name + second_div_num,
                                                            "line " + line_num]
                                            else:
                                                citation = [first_div_name + first_div_num,
                                                            second_div_name + second_div_num]
                                            if '' in citation:
                                                citation.remove('')
                                            if surrounding_text not in match_dict.keys():
                                                match_count += 1
                                                match_dict[surrounding_text] = citation
                        except:
                            pass
                except:
                    pass
                for l in div.strings:
                    if text in l:
                        if with_citation:
                            l_text = l
                            surrounding_text = l_text.strip("\n")
                            line_nums = False
                            try:
                                for line in div.find_all("l"):
                                    if l == line.strings:
                                        line_num = line.get("n")
                                        line_nums = True
                            except:
                                continue
                            if line_nums == True:
                                citation = [first_div_name + first_div_num,
                                            "line " + line_num]
                            else:
                                citation = [first_div_name + first_div_num]
                            if '' in citation:
                                citation.remove('')
                            if surrounding_text not in match_dict.keys():
                                match_count += 1
                                match_dict[surrounding_text] = citation
        except:
            pass
    if with_citation:
        result = [match_count, match_dict]
        return result
    else:
        return match_count

###########################################

def search_corpus(text_to_search: str, with_citation: bool, is_greek: bool):
    '''
    Takes in text to search, as a string of either Latin characters or Beta-coded Greek,
    whether or not the user wishes to have the citations of the results listed, or simply to have the numerical result,
    and whether or not the text to search is Greek or not.

    Opens the corpus, iterates through each file in the corpus and runs each through find_soup, then writes those into
    a results .txt document.
    '''

    import os

    ###Nota Bene: please ensure that this folder path is correct when using the Classical Ngrams program locally.

    corpus_folder_path = """/Users/a.aldins/Dropbox (MIT)/ClassicalNgrams/DiogenesWeb/Texts"""

    directory = os.fsencode(corpus_folder_path)

    results_file = open("search_results.txt", "w+")

    for files in os.listdir(directory):
        results_dict = {}

        file_name = os.fsdecode(files)
        file_path = corpus_folder_path + "/" + file_name

        results_dict[file_name] = find_soup(file_path, text_to_search, with_citation, is_greek)
        results = str(results_dict)

        results_file.write(results)
        results_file.write("\n")



def advanced_search(text_list: list, text_to_search: str, with_citation: bool, is_greek: bool):
    '''
    Takes in the list of works to be searched (from MetadataBits),
    text to search, as a string of either Latin characters or Beta-coded Greek,
    whether or not the user wishes to have the citations of the results listed, or simply to have the numerical result,
    and whether or not the text to search is Greek or not.

    Opens the corpus, iterates through each file in the corpus and runs each through find_soup, then writes those into
    a results txt document.
    '''

    ###Nota Bene: please ensure that this folder path is correct when using the Classical Ngrams program locally.
    corpus_folder_path = """/Users/a.aldins/Dropbox (MIT)/ClassicalNgrams/DiogenesWeb/Texts"""

    results_file = open("search_results.txt", "w+")

    for file_name in text_list:
        results_dict = {}

        file_path = corpus_folder_path + "/" + file_name

        results_dict[file_name] = find_soup(file_path, text_to_search, with_citation, is_greek)
        results = str(results_dict)

        results_file.write(results)
        results_file.write("\n")