# Påsen

Välkommen till Påsen! :D

Programmet var skapat för Python 3.13.15. För att starta den, kör ```__main__.py```. 

Det speciella med den här påsen är att du kan klicka på alternativen i listan istället för att skriva dem! Du kan dock också använda tangentbordet om du föredrar. 

Liten sak som jag *antar* att jag inte tappar poäng på: jag använder inte input() för menyn, utan istället pratar jag med STD_INPUT_HANDLE från Windows kernel32 då jag ville att mus-input skulle fungera. 

Det innebär också att det här programmet inte är det minsta cross-platform. Men, det var inte heller ett krav. 