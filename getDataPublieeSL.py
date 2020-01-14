def getDataDiffusee(annonceRevisionColList,
                    typeTransaction,typeTransactionColList,
                    typeBien,typeBienColList,
                    dateFrom,dateTo):

    """Génère une requete SQL qui récupère les annonces diffusées sur SL
    en fonction du type de transactions, type de biens, avec un historique 
    entre deux dates 
    
    Arguments:
        annonceRevisionColList {list of strings} -- la liste des colonnes à selectionner sur annonce_revision
        typeTransaction {string} -- la table at_...revision sur laquelle la jointure est faite
        typeTransactionColList {list of strings} -- la liste des colonnes à selectionner sur at_...revision
        typeBien {string} -- la table ab_...revision sur laquelle la jointure est faite
        typeBienColList {list of strings} -- la liste des colonnes à selectionner sur ab_...revision
        dateFrom {string} -- date de départ de l'historique format YYYY-MM-DD
        dateTo {string} -- date de fin de l'historique format YYYY-MM-DD
    """    
    totalColSel = ''.join(["ar.{}, ".format(k) for k in annonceRevisionColList]) +\
    ''.join(["at.{}, ".format(k) for k in typeTransactionColList]) +\
    ''.join(["ab.{}, ".format(k) for k in typeBienColList])[:-2]
    
    with open('sqlTemplateForPublication','r') as file:
        query = file.read()
        query = query.format(totalColSel,dateFrom,dateTo,typeTransaction,typeBien)
        
    return(query)

