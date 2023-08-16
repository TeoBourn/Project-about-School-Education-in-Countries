import streamlit as st    # install graphviz
import pandas as pd
import seaborn as sb
import numpy as np
import altair as alt
import statistics

st.set_page_config(page_title='Σύγκριση εκπαίδευσης παγκοσμίως',page_icon=':chart_with_upwards_trend:',layout='wide')

st.title('Εργασία στο μάθημα: Εφαρμογές στην Python - Μπουρνέλης Θεόδωρος (καλοκαίρι 2023)')

st.header('Ανάλυση χρόνων εκπαίδευσης για κάθε χώρα του κόσμου')

st.write('---')
st.subheader("Δεδομένα για κάθε χώρα: Μέσος Όρος ετών σχολικής Εκπαίδευσης κατ'έτος, από το 1870 έως το 2017.")
#st.markdown("### Δεδομένα για κάθε χώρα: μόσος όρος σχολικής εκπαίδευσης κατ'έτος, από το 1870 έως το 2017.")
st.write('---')

st.write("Ξεκινώντας πρέπει να αναφέρουμε ότι είναι αδύνατη η παρουσίαση των δεδομένων συγκεντρωτικά, καθ'ότι η σύγκριση είναι άδικη όπως θα εξηγήσω παρακάτω. Χωρίζω λοιπόν τα δεδομένα για τις υπάρχουσες χώρες με βάση τις Ηπείρους, οπότε θα παρουσιάσουμε τους Μέσους Όρους ετών σχολικής Εκπαίδευσης (Μ.Ο.Ε.) σε Ευρώπη, Νότια Αμερική, Βόρεια Αμερική, Αφρική, Ασία και Ωκεανία. Χρειάζεται να σημειωθεί ότι ο Μ.Ο.Ε. δεν υπάρχει για κάθε έτος και για κάθε χώρα. Για κάποιες χώρες δεν υπάρχουν δεδομένα. Σε αρκετές περιπτώσεις η απόσταση μεταξύ των μετρήσεων μιας χώρας φτάνει τα 5 χρόνια, ενώ σε κάποιες χώρες οι μετρήσεις ξεκινούν αργότερα σε σχέση με άλλες χώρες. Παρ'όλα αυτά, τελικά παρουσιάζεται ό,τι δεδομένο υπάρχει με σαφή τρόπο.")

Europe=['AUT','BEL','BGR','HRV','CYP','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','IRL','ITA','LVA','LTU','LUX','MLT','NLD','POL','PRT','ROU','SVK','SVN','ESP','SWE','ALB','AND','ARM','BLR','BIH','FRO','GEO','GIB','ISL','IMN','XKX','MKD','LIE','MDA','MCO','MNE','NOR','RUS','SMR','SRB','CHE','TUR','UKR','GBR','VAT']
NorthAmerica=['AIA','ATG','ABW','BRB','BLZ','BMU','BES','VGB','CAN','CYM','CRI','CUB','CUW','DMA','DOM','SLV','GRL','GRD','GLP','GTM','HTI','HND','JAM','MTQ','MEX','MSR','ANT','NIC','PAN','PRI','BLM','KNA','LCA','MAF','SPM','VCT','SXM','BHS','TTO','TCA','USA','VIR']
SouthAmerica=['ARG','BOL','BRA','CHL','COL','ECU','FLK','GUF','GUY','PRY','PER','SUR','URY','VEN']
Asia=['AFG','ARM','AZE','BHR','BGD','BTN','IOT','BRN','KHM','CHN','CCK','GEO','HKG','IND','IDN','IRN','IRQ','ISR','JPN','JOR','KAZ','KWT','KGZ','LAO','LBN','MAC','MYS','MDV','MNG','MMR','NPL','PRK','OMN','PAK','PSE','PHL','QAT','SAU','SGP','KOR','LKA','SYR','TWN','TJK','THA','TUR','TKM','ARE','UZB','VNM','YEM']
Africa=['DZA','AGO','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COD','DJI','EGY','GNQ','ERI','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY','MDG','MWI','MLI','MRT','MUS','MYT','MAR','MOZ','NAM','NER','NGA','COG','REU','RWA','SHN','STP','SEN','SYC','SLE','SOM','ZAF','SSD','SDN','SWZ','TZA','TGO','TUN','UGA','ESH','ZMB','ZWE']
Oceania=['ASM','AUS','CXR','COK','FJI','PYF','GUM','KIR','MHL','FSM','NRU','NCL','NZL','NIU','NFK','MNP','PLW','PNG','PCN','WSM','SLB','TLS','TKL','TON','TUV','VUT','WLF']

#data=pd.read_csv('YearsPerCountry.csv')
data=pd.read_excel('YearsPerCountry.xlsx')   # voleuei to .xlsx anti gia to .csv

years = []
education = []
dictionary={}
countries={}
j=0

for i in range(0,len(data)):
    if i==0:
        years.append(data['Year'][i])
        education.append(data['avg_years_of_schooling'][i])
    else:
        if data['Code'][i]==data['Code'][i-1]:
            years.append(data['Year'][i])
            education.append(data['avg_years_of_schooling'][i])
        else:

            dictionary[j]={'name':data['Code'][i-1],'years':years,'edu':education}
            j+=1
            years=[]
            education=[]
            years.append(data['Year'][i])
            education.append(data['avg_years_of_schooling'][i])

dEur={}
dNA={}
dSA={}
dAs={}
dAf={}
dOc={}

i1=i2=i3=i4=i5=i6=0

for i in range(0,len(dictionary)):
    if dictionary[i]['name'] in Europe:
        dEur[i1]=dictionary[i]
        i1+=1

    elif dictionary[i]['name'] in NorthAmerica:
        dNA[i2]=dictionary[i]
        i2+=1

    elif dictionary[i]['name'] in SouthAmerica:
        dSA[i3]=dictionary[i]
        i3+=1

    elif dictionary[i]['name'] in Asia:
        dAs[i4]=dictionary[i]
        i4+=1

    elif dictionary[i]['name'] in Africa:
        dAf[i5]=dictionary[i]
        i5+=1

    elif dictionary[i]['name'] in Oceania:
        dOc[i6]=dictionary[i]
        i6+=1

st.write('Στις διπλανές καρτέλες μπορείτε να δείτε τα δεδομένα των χωρών όπως παρουσιάζονται ανά 5άδες ώστε να είναι ευανάγνωστα')

st.write('Σαν συγκεντρωτικό (και συγκριτικό) στοιχείο μπορούμε να αποτυπώσουμε τον τελικό Μ.Ο.Ε. ανά Ήπειρο ώστε να έχουμε μια εικόνα για το ποιος είναι ο βαθμός εκπαίδευσης το 2017 στον κόσμο ανά Ήπειρο.')

Eur=[]
As=[]
NA=[]
SA=[]
Af=[]
Oc=[]

for i in range(0,len(dEur)):
    Eur.append(dEur[i]['edu'][-1])
for i in range(0,len(dAs)):
    As.append(dAs[i]['edu'][-1])
for i in range(0,len(dNA)):
    NA.append(dNA[i]['edu'][-1])
for i in range(0,len(dSA)):
    SA.append(dSA[i]['edu'][-1])
for i in range(0,len(dAf)):
    Af.append(dAf[i]['edu'][-1])
for i in range(0,len(dOc)):
    Oc.append(dOc[i]['edu'][-1])

MEur=statistics.mean(Eur)
MAs=statistics.mean(As)
MNA=statistics.mean(NA)
MSA=statistics.mean(SA)
MAf=statistics.mean(Af)
MOc=statistics.mean(Oc)

if st.button("Πατήστε για να δείτε τους Μ.Ο.Ε. του 2017 ανά Ήπειρο"):
    left_col2, middle_col2, right_col2 = st.columns(3)
    with left_col2:
        st.metric(label='Ευρώπη',value=MEur)
        st.metric(label='Βόρεια Αμερική',value=MNA)
    with middle_col2:
        st.metric(label='Νότια Αμερική',value=MSA)
        st.metric(label='Αφρική',value=MAf)
    with right_col2:
        st.metric(label='Ασία',value=MAs)
        st.metric(label='Ωκεανία',value=MOc)



