spokojni = [0]* 24
nespokojni = [0] * 24


subor=open ('spokojny.txt','r')
for riadok in subor:
        riadok = riadok.strip()
        info = riadok.split()
        spokojnost= info[1]
        cas = info[0].split(':')
        hodina = int(cas[0])
        minuta = int(cas[1])
        if spokojnost == 'áno':
                spokojni[hodina] +=1
        else:
                nespokojni[hodina] +=1

pocet_spokojnych = sum(spokojni)
pocet_nespokojnych = sum(nespokojni)
spolu = pocet_spokojnych + pocet_nespokojnych
print('vyjadrilo sa { } zákaznikov.'.format(spolu))
pocet_ok = max(spokojni)
hodina = spokojni.indfex(pocet_ok)
print('Najviac spokojný zák. ({ }) je cez hodinu: { }'.format(pocet_ok,hodina)
nespokojni2 = []
for pocet in nespokojni:
        if pocet >0:
                nespokojni2.append(pocet)
pocet_zle = min(nespokojni2)
hodina = nespokojnií.index(pocet_zle)
print('Najmenej spokojnych zak. ({ }) je cez hodinu:{}'.format(pocet_zle,hodina)

percenta_spokojnosti = [0]* 24
for i in range(24):
      pocet = spokojni[i] + nespokojni[i]
      if pocet >0:
              percenta_spokojnosti[i] = spokojni[i] = spokojni[i] / pocet * 100
for i in range(24):
      if percenta_spokojnosti[i] > 0:
              print('V { }. hodine je spokojnych {:5.2f}%'.format(i,percenta_spokojnosti[i]))
      
