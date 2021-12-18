import docx
d={}
def main():
    try:
        file=docx.Document('file.docx')
        data=""
        Text=[]
        for para in file.paragraphs:
            Text.append(para.text)
            data='\n'.join(Text)
            for i in data.split():
                if i in d:
                    d[i]=d[i]+1
                else:
                    d[i]=1
        print("Occurence of each word is:\n\n")
        for i in d:
                print(i,':',d[i])
        c={}
        print("\n\n Occurrence of each sentence:\n\n")
        for k in data.split('.'):
            if k in c:
                c[k]=c[k]+1
            else:
                c[k]=1
        for i in c:
            print(i,':',c[i])
    except IOError:
        print("Error opening the file")
        return
if __name__=='__main__':
    main()

'''Output:-

Occurence of each word is:


Subhas : 8
Chandra : 8
Bose : 9
now : 1
started : 3
a : 3
mass : 1
movement : 5
against : 4
utilizing : 1
Indian : 7
resources : 1
and : 17
men : 1
for : 3
the : 26
great : 1
war. : 2
There : 1
was : 10
tremendous : 2
response : 1
to : 5
his : 11
call : 1
he : 11
put : 1
under : 5
house : 1
arrest : 1
in : 15
Calcutta. : 1
In : 6
January : 3
1941, : 1
disappeared : 1
from : 5
home : 1
Calcutta : 1
reached : 1
Germany : 2
via : 1
Afghanistan. : 1
Working : 1
on : 3
maxim : 1
that : 3
"an : 1
enemy's : 1
enemy : 1
is : 1
friend", : 1
sought : 1
cooperation : 1
of : 14
Japan : 1
British : 2
Empire. : 1
1942, : 1
began : 1
regular : 1
broadcasts : 1
Radio : 1
Berlin, : 1
which : 1
aroused : 1
enthusiasm : 1
India. : 3
July : 1
1943, : 1
arrived : 1
Singapore : 2
Germany. : 1
took : 1
over : 1
reins : 1
Independence : 3
Movement : 1
East : 2
Asia : 1
Rash : 1
Behari : 1
organised : 1
Azad : 3
Hind : 3
Fauj : 3
(Indian : 1
National : 3
Army) : 1
comprising : 1
mainly : 1
prisoners : 1
He : 5
hailed : 1
as : 3
Netaji : 3
by : 4
Army : 1
well : 1
civilian : 1
population : 1
Asia. : 1
proceeded : 1
towards : 1
India : 3
liberate : 1
it : 2
rule. : 1
Enroute : 1
lliberated : 1
Andeman : 1
Nicobar : 1
Islands. : 1
The : 1
INA : 1
Head : 1
quarters : 1
shifted : 1
Rangoon : 1
1944. : 1
crossed : 1
Burma : 1
Border, : 1
stood : 1
soil : 1
March : 1
18 : 1
,1944.After : 1
returning : 2
Subhash : 2
came : 2
influence : 2
Mahatma : 2
Gandhi : 2
joined : 2
Congress. : 2
On : 2
Gandhiji's : 2
instructions, : 2
working : 2
Deshbandhu : 2
Chittaranjan : 2
Das, : 2
whom : 2
later : 2
acknowledged : 2
political : 2
guru. : 2
Soon : 2
showed : 2
leadership : 2
mettle : 2
gained : 2
way : 2
up : 2
Congress' : 2
hierarchy. : 2
1928 : 2
Motilal : 2
Nehru : 4
Committee : 2
appointed : 2
Congress : 2
declared : 2
favour : 2
Domination : 2
Status, : 2
but : 2
along : 2
with : 4
Jawaharlal : 2
opposed : 4
it, : 2
both : 2
asserted : 2
they : 2
would : 2
be : 2
satisfied : 2
nothing : 2
short : 2
complete : 2
independence : 2
also : 2
announced : 2
formation : 2
League. : 2
jailed : 2
during : 2
Civil : 4
Disobedience : 4
1930. : 2
released : 2
1931 : 2
after : 2
Gandhi-Irwin : 4
pact : 4
signed. : 2
protested : 2
suspension : 2
specially : 2
when : 2
Bhagat : 2
Singh : 2
associates : 2
were : 2
hanged.After : 1
hanged. : 1


 Occurrence of each sentence:


Subhas Chandra Bose now started a mass movement against utilizing Indian resources and men for the great war : 1
 There was a tremendous response to his call and he was put under house arrest in Calcutta : 1
 In January 1941, Subhas Chandra Bose disappeared from his home in Calcutta and reached Germany via Afghanistan : 1
 Working on the maxim that "an enemy's enemy is a friend", he sought cooperation of Germany and Japan against British Empire : 1
 In January 1942, he began his regular broadcasts from Radio Berlin, which aroused tremendous enthusiasm in India : 1
 In July 1943, he arrived in Singapore from Germany : 1
 In Singapore he took over the reins of the Indian Independence Movement in East Asia from Rash Behari Bose and organised the Azad Hind Fauj (Indian National Army) comprising mainly of Indian prisoners of war : 1
 He was hailed as Netaji by the Army as well as by the Indian civilian population in East Asia : 1
 Azad Hind Fauj proceeded towards India to liberate it from British rule : 1
 Enroute it lliberated Andeman and Nicobar Islands : 1
 The INA Head quarters was shifted to Rangoon in January 1944 : 1
 Azad Hind Fauj crossed the Burma Border, and stood on Indian soil on March 18 ,1944 : 1
After returning to India Netaji Subhash Chandra Bose came under the influence of Mahatma Gandhi and joined the Indian National Congress : 2
 On Gandhiji's instructions, he started working under Deshbandhu Chittaranjan Das, whom he later acknowledged his political guru : 2
 Soon he showed his leadership mettle and gained his way up in the Congress' hierarchy : 2
 In 1928 the Motilal Nehru Committee appointed by the Congress declared in favour of Domination Status, but Subhas Chandra Bose along with Jawaharlal Nehru opposed it, and both asserted that they would be satisfied with nothing short of complete independence for India : 2
 Subhas also announced the formation of the Independence League : 2
 Subhas Chandra Bose was jailed during Civil Disobedience movement in 1930 : 2
 He was released in 1931 after Gandhi-Irwin pact was signed : 2
 He protested against the Gandhi-Irwin pact and opposed the suspension of Civil Disobedience movement specially when Bhagat Singh and his associates were hanged : 2
 : 1
'''
