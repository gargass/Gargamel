Opis programu
Program tworz¹cy melodiê (beatbox) z podanych sampli i nut

Opis plików
beatbox.py - g³ówny program, odpalany z konsoli z argumentem np. "nazwa_utworu"

defs_ins.py - modu³ pomocniczy, tworz¹cy dzwiêk za pomoc¹ nazwy nuty oraz definicji instrumentu

Nuty zdefiniowane s¹ za pomoc¹ nastêpuj¹cego wzoru: abc
a - litera oznaczaj¹ca dan¹ nutê w zadanej kolejnoœci:
C, D, E, F, G, A, H

b - oznacza podwy¿szenie lub obni¿enie dzwiêku:
b - obni¿a o pó³ tonu
- - nie modyfikuje dzwiêku
# - podwy¿sza dzwiêk o pó³ tonu

Przyk³ad:
A-4, D#5, Eb3

Nuty mo¿na wywo³ywaæ po prostu jako np.A-4, lub za pomoc¹ instrumentu, np. 
01:A-4

Mo¿na definiowaæ d³ugoœæ trwania poszczególnego sampla. ¯eby to zrobiæ, w³¹czat¹ t¹ opcjê w pliku defs.txt i zmieniaj¹c length_sample na 1. Nastêpnie w ka¿dym pliku trackXY.txt umieszczamy na koñcu oznaczenie np. 'S1' oznaczaj¹ce æwierænutê.
Odpowiednio - S2 - pó³nuta
  	    - S4 ca³a nuta
itd.




