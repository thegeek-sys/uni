# UniQuizzes
| Homepage | Domande |
| ---- | ---- |
| ![image](https://github.com/dag7dev/UniQuizzes/assets/44711271/8db55bbd-3a28-459f-a0af-c74e8294924a) | ![image](https://github.com/dag7dev/UniQuizzes/assets/44711271/b7ab4ad4-1358-4c48-bb46-8b2e63b97338) |



Repository che contiene tanti test, che trattano Sistemi Operativi (entrambi), Ingegneria del Software e molto altro.

Semplice app **ora anche da web** che si occuperà di addestrare il cadetto all'esame di SO1, SO2 e tante altre materie.

Cerchi un'altra versione? [Clicca qui](https://github.com/dag7dev/UniQuizzes?tab=readme-ov-file#altre-versioni)

## Disclaimer
> Ci solleviamo da ogni responsabilità di utilizzo improprio di questo strumento, e non garantiamo in alcun modo che le risposte siano corrette o errate.

Utilizzalo a tuo rischio e pericolo ma cosa più importante: dai una mano ai tuoi colleghi aggiungendo o modificando domande, **basta una PR o una issue!**

## Informazioni generali
Il punteggio è calcolato nel seguente modo: +2 punti per ogni risposta corretta, -1 punto per ogni risposta errata, 0 per ogni risposta saltata

La versione web è stata scritta in un orribile **JavaScript** in fretta e furia e si basa su  [JSQuizee](https://github.com/dag7dev/JSQuizee/), un motore di quiz offline.

Solitamente il codice javascript viene aggiornato grazie a quest'ultima repo: non è sempre così, ma se vuoi contribuire ed aggiungere funzionalità, consiglio di aggiornare direttamente l'engine!

### Info sul JSON
`code`: se contiene del testo, verrà mostrato in forma di codice sorgente subito dopo il testo della domanda

`answers_have_code`: se a "1", le domande verranno renderizzate come codice in un box.

**ATTENZIONE**: il codice deve essere propriamente escapizzato, e ogni nuova riga deve avere `\n` alla fine

## Istruzioni per l'offline
### Requisiti
1. Un qualunque web server (si consiglia `python -m http.server` per semplicità)
2. Un browser
3. Git

### Istruzioni 
1. clonare questa cartella

2. andare nella cartella di UniQuizzes e digitare:
```
python -m http.server
```

Potrai eseguirlo in locale digitando `http://0.0.0.0:8000/` sul tuo browser.

## Come contribuire
- **inserendo nuovi quiz**:
   - vai nella cartella `json` e crea un file in `.json`. Usa come modello i JSON già esistenti
   - vai nel file `config.js` nella cartella `js` e aggiungi il tuo file nella lista dei file
- **revisionando i quiz esistenti**:
   - vai nella cartella `json` e modifica il file che vuoi correggere
   - in alternativa, apri una issue dove specifichi: `file, risposta attuale, risposta corretta, motivo` 
- **implementando nuove funzionalità su JSQuizee**: l'engine sul quale si basa UniQuizzes è [JSQuizee](https://github.com/dag7dev/JSQuizee/), un engine di quiz offline. Se verranno implementate modifiche su JSQuizee, UniQuizzes verrà aggiornato all'ultima versione di JSQuizee.

Se il progetto ti è stato utile, o se hai passato esami, non dimenticare di lasciare una stella :D

## Troubleshooting sull'offline
Q: L'app non legge i JSON tramite file locali. Normale?
- Non l'hai avviata tramite server. È requisito fondamentale farlo, poiché normalmente i browser non possono accedere ai file locali.

Q: L'app non legge i JSON nonostante il server tramite file locali. Che ho sbagliato?
- Il JSON

Q: Quando implementerai la pagina di creazione semplice dei JSON?
- Non ho una deadline, e lavoro a questo progetto nel tempo libero.

## Funzionalità future
- [X] GUI cross-platform
- [X] Una GUI fatta come si deve _Implementata nel 2024_ 
- [X] Un json che **include quesiti SO1**
- [X] Linee guida per contribuire
- [ ] Editor json in-browser (aggiungere, modificare, rimuovere domande): potrebbe essere un'idea farlo in markdown
- [ ] Analytics: attualmente non c'è un modo di sapere se state usando UniQuizzes. Avevo dato il progetto per morto, ma ho visto che è ancora usato. Se volete contribuire allo sviluppo, supportate il progetto con una stella e una PR.

## Altre versioni
- Versione Java **(cross platform)** solo domande SO modulo 2 (NON AGGIORNATA E NON MANTENUTA)**: [so2-exam-sim](https://github.com/andrea-gasparini/SO2-exam-simulator)
- Telegram: [so1bot](https://github.com/appinfosapienza/so-un-bot)
