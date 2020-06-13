# Diplom

Genererer diplom med grafikk som genereres basert på navnet i diplomet, så ulike navn gir ulike bilder.
Algoritmen for generere bildet er basert på en fra s 118 i boka [print 10](https://10print.org/10_PRINT_121114.pdf)

## Bruk
Lag og aktiver virtuelt miljø

Installere avhengigheter
```
pip install -r requirements.txt
```
Png- og pdf-filer lagres i en output folder, default `out`, denne mappen må lages først.
Kjør programmet med 
```
python main.py -name "Testulf Testesen" -text "for strålende innsats på introduksjonskurs i programmering"
```
I tillegg til de påkrevde parametrene `name` og `text`, kan man også angi `title` (default `kursbevis`), `subtitle` (default `tildeles`) og `out_folder` (default `out`).
