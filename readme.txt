Opis programu
Program tworz�cy melodi� (beatbox) z podanych sampli i nut

Opis plik�w
beatbox.py - g��wny program, odpalany z konsoli z argumentem np. "nazwa_utworu"

defs_ins.py - modu� pomocniczy, tworz�cy dzwi�k za pomoc� nazwy nuty oraz definicji instrumentu

Nuty zdefiniowane s� za pomoc� nast�puj�cego wzoru: abc
a - litera oznaczaj�ca dan� nut� w zadanej kolejno�ci:
C, D, E, F, G, A, H

b - oznacza podwy�szenie lub obni�enie dzwi�ku:
b - obni�a o p� tonu
- - nie modyfikuje dzwi�ku
# - podwy�sza dzwi�k o p� tonu

Przyk�ad:
A-4, D#5, Eb3

Nuty mo�na wywo�ywa� po prostu jako np.A-4, lub za pomoc� instrumentu, np. 
01:A-4

Mo�na definiowa� d�ugo�� trwania poszczeg�lnego sampla. �eby to zrobi�, w��czat� t� opcj� w pliku defs.txt i zmieniaj�c length_sample na 1. Nast�pnie w ka�dym pliku trackXY.txt umieszczamy na ko�cu oznaczenie np. 'S1' oznaczaj�ce �wier�nut�.
Odpowiednio - S2 - p�nuta
  	    - S4 ca�a nuta
itd.




