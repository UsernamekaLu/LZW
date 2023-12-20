
def lzw_kompresija(sekvenca):
    rjecnik = dict() 
    
    for i in range(0,256):
        rjecnik[str(i)] = i  
        
    trenutni_kod = str(sekvenca[0])
    
    izlaz = [] 
    
    for piksel in sekvenca[1:]:
        temp_kod = trenutni_kod + ',' + str(piksel) 
        if temp_kod in rjecnik:
            trenutni_kod = temp_kod 
        else:
            izlaz.append(rjecnik[trenutni_kod]) 
            
            rjecnik[temp_kod] = len(rjecnik)  
            
            trenutni_kod = str(piksel)
            
          
    izlaz.append(rjecnik[trenutni_kod])
    return izlaz


def lzw_dekompresija(sekvenca):
    rjecnik = dict() 
    
    for i in range(0,256):
        rjecnik[i] = [i] 
    
    izlaz = []
    
    temp = sekvenca[0]
    
    izlaz.append(temp) 
    
    stari_kod = temp
    
    temp_sekvenca = []
    
    for novi_kod in sekvenca[1:]:
        if novi_kod in rjecnik:
            temp_sekvenca = rjecnik[novi_kod]
        else:
            temp_sekvenca = rjecnik[stari_kod] + [temp]
            
        izlaz.extend(temp_sekvenca)
    
        temp = temp_sekvenca[0]
    
        rjecnik[len(rjecnik)] = rjecnik[stari_kod] + [temp]
    
        stari_kod = novi_kod
    return izlaz