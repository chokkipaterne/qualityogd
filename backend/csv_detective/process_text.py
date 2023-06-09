
#### Process text
def _process_text(val):
    '''Met le unicode val sous sous sa forme normee'''
    val = val.lower()
    val = val.replace(u'-', u' ')
    val = val.replace(u'_', u' ')
    val = val.replace(u"'", u' ')
    val = val.replace(u',', u' ')
    # add by chokki
    val = remove_extra_spaces(val)
    # val = val.replace('\xc3\xa8', 'e')
    # val = val.replace('\xc3\xa9', 'e')
    # val = val.replace('\xc3\xaa', 'e')
    # val = val.replace('\xc3\x8e', 'i')
    # val = val.replace('\xc3\xb4', 'o')
    # val = val.replace('\xc3\xa7', 'c')
    # val = val.replace('\xc3\xa0', 'a')
    # val = val.replace('\xc3\xa2', 'a')
    # val = val.replace('\xc3\xae', 'i')
    val = val.replace(u'Ã©', u'e')
    val = val.replace(u'é', u'e')
    val = val.replace(u'è', u'e')
    val = val.replace(u'ê', u'e')
    val = val.replace(u'î', u'i')
    val = val.replace(u'ô', u'o')
    val = val.replace(u'ç', u'c')
    val = val.replace(u'à', u'a')
    val = val.replace(u'â', u'a')
    val = val.replace(u'î', u'i')
    val = val.replace(u'û', u'u')


    val = val.strip()

    return val

def _mini_process_text(val):
    '''Met le unicode val sous sous sa forme normee'''
    val = val.lower()
    # add by chokki
    val = remove_extra_spaces(val)
    val = val.replace(u'  ', ' ')
    val = val.replace(u'Ã©', u'e')
    val = val.replace(u'é', u'e')
    val = val.replace(u'è', u'e')
    val = val.replace(u'ê', u'e')
    val = val.replace(u'î', u'i')
    val = val.replace(u'ô', u'o')
    val = val.replace(u'ç', u'c')
    val = val.replace(u'à', u'a')
    val = val.replace(u'â', u'a')
    val = val.replace(u'î', u'i')
    val = val.replace(u'û', u'u')

    val = val.strip()

    return val

def _process_text_phone(val):
    '''Met le unicode val sous sous sa forme normee'''
    val = val.lower()
    val = val.replace(u'-', '')
    val = val.replace(u'(', '')
    val = val.replace(u')', '')
    # add by chokki
    val = remove_extra_spaces(val)
    val = val.replace(u' ', '')
    val = val.strip()

    return val

# add by chokki
def remove_extra_spaces(s):
    """
    Remove unnecessary spaces
    :param s:
    :return:
    """
    return " ".join(s.split())
