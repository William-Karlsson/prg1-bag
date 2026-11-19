# Hangman

Välkommen till Påsen! :D

Programmet var skapat för Python 3.13.15. För att starta appen, kör ```__main__.py```. 

Det speciella med den här påsen är att du kan klicka på alternativen i listan av alternativ om du vill!

Liten sak som jag *antar* att jag inte tappar poäng på: jag använder inte input() för menyn, utan istället pratar jag med STD_INPUT_HANDLE från kernel32 då jag ville att mus-input skulle fungera. 