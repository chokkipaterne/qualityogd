from csv_detective.process_text import _process_text

PROPORTION = 0.55

def _is(val):
    '''Repere des adresses'''
    voies = [
        'Aire',
        'Allée',
        'Avenue',
        'Base',
        'Boulevard',
        'Cami',
        'Carrefour',
        'Chemin',
        'Cheminement',
        'Chaussée',
        'Cité',
        'Clos',
        'Coin',
        'Corniche',
        'Cote',
        'Cour',
        'Cours',
        'Domaine',
        'Descente',
        'Ecart',
        'Esplanade',
        'Faubourg',
        'Gare',
        'Grande Rue',
        'Hameau',
        'Halle',
        'Ilôt',
        'Impasse',
        'Lieu dit',
        'Lotissement',
        'Marché',
        'Montée',
        'Parc',
        'Passage',
        'Place',
        'Plan',
        'Plaine',
        'Plateau',
        'Pont',
        'Port',
        'Promenade',
        'Parvis',
        'Quartier',
        'Quai',
        'Résidence',
        'Ruelle',
        'Rocade',
        'Rond Point',
        'Route',
        'Rue',
        'Sente - Sentier',
        'Square',
        'Tour',
        'Terre-plein',
        'Traverse',
        'Villa',
        'Village',
        'Voie',
        'Zone artisanale',
        'Zone d’aménagement concerté',
        'Zone d’aménagement différé',
        'Zone industrielle',
        'Zone',
        'r',
        'av',
        'pl',
        'bd',
        'cami',
        'che',
        'chs',
        'dom',
        'ham',
        'ld',
        'pro',
        'rte',
        'vlge',
        'za',
        'zac',
        'zad',
        'zi',
        'car',
        'fg',
        'lot',
        'imp',
        'qu',
        'mte'
    ]

    val = _process_text(val)
    arrval = val.split(' ')
    match = False
    for val in arrval:
        a = any([val == x.lower() for x in voies])
        if a:
            match = True
    return match
