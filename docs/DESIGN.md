# Sito portfolio "Anno di Prova" — Riccardo Callà

> Spec di progettazione approvata il 10/06/2026 (brainstorming superpowers + ui-ux-pro-max).

## Contesto

Riccardo (docente di Informatica A041, neoassunto) sostiene il **colloquio davanti al Comitato di Valutazione lunedì 15 giugno 2026** (tutor: prof. Gammino). Il dossier è già consegnato; il sito è lo strumento con cui guiderà l'esposizione del percorso dell'anno di prova e risponderà alle domande del Comitato. Un tentativo precedente (`Scuola/anno di prova/sito_portfolio/`) è stato scartato: questa è una riprogettazione da zero.

**Scadenza: sito completo e testato entro il 13–14 giugno 2026.**

## Decisioni prese con l'utente

| Decisione | Scelta |
|---|---|
| Scopo | Supporto al colloquio del 15/6 |
| Fruizione | Offline dal portatile (piano A) **e** online su GitHub Pages (link al Comitato) |
| Contenuti | Percorso completo: anno di prova + didattica 5 classi + ed. civica + innovazione |
| Struttura | Ibrido: home one-page narrativa (timeline) + 3 pagine di approfondimento |
| Stile | **Taglio moderno** (no editoriale); progetto grafico delegato alle skill frontend-design + ui-ux-pro-max |
| Hosting | GitHub Pages |

## Architettura

- **Sito statico puro**: HTML + CSS + JS vanilla. Zero build, zero CDN, zero dipendenze runtime.
- **Font self-hosted** (`assets/fonts/*.woff2`): serviti in locale con `@font-face` + `font-display: swap`. Requisito critico per l'uso offline al colloquio.
- **Grafici = SVG statici** scritti a mano coi dati reali (niente Chart.js).

### Struttura file

```
anno_di_prova/
├── index.html            ← racconto one-page (guida il colloquio)
├── classi.html           ← approfondimento didattica 5 classi
├── ed_civica.html        ← fake news / uso etico dell'IA
├── innovazione.html      ← script Python, Classroom, Veyon, db Biblioteca
├── assets/
│   ├── css/style.css     ← design system + componenti + print CSS
│   ├── js/main.js        ← nav mobile, count-up KPI, reveal-on-scroll
│   ├── fonts/            ← woff2 self-hosted
│   └── img/              ← eventuali SVG decorativi
├── design-system/
│   └── MASTER.md         ← design system generato da ui-ux-pro-max (fonte di verità grafica)
├── docs/
│   └── DESIGN.md         ← questa spec
└── README.md             ← come aprire offline + URL pubblico
```

## Pagine e contenuti

### index.html — "Il percorso"
1. **Hero**: H1 "Riccardo Callà", sottotitolo (Docente di Informatica — A041, IIS Curie-Vittorini), meta dell'anno di prova.
2. **KPI row** (count-up, `prefers-reduced-motion` rispettato): 5 classi · ~95 studenti · 20h formazione IA · 27 esercizi differenziati.
3. **Timeline verticale del percorso** (ancore navigabili):
   - Bilancio iniziale (ott 2025)
   - Laboratorio Scuola Futura "IA applicata alla didattica" 20h (12–17 feb 2026)
   - Peer-to-peer col tutor Gammino: osservazione lezioni (mar–apr 2026) — interrogazione laboratoriale con estrazione casuale + esercizio parallelo
   - Esperienza didattica: coding con Flowgorithm su 3 classi seconde (7–19 gen 2026)
   - Incarichi collegiali: segretario CdC 2C e Dipartimento Informatica
   - Dossier finale e colloquio (giu 2026)
4. **Chiusura**: "sguardo al futuro" (sviluppo professionale, standard rafforzati 1–6, 8).

### classi.html — "La didattica"
- Le 5 classi (2B/2C/2D SA, 3P/4S SIA) con numeri aggregati.
- Percorsi per corso: SA Anno 2 (Flowgorithm → C++ Dev-C++), SIA Anno 3 (flowchart → C++ solo selezione), SIA Anno 4 (Database → ER → SQL con db "Biblioteca di Quartiere").
- Sistema verifiche: Fila A/B/C a pari difficoltà + versione PDP; regolamenti di laboratorio; consegna via Classroom con Veyon.

### ed_civica.html — "Ed. civica e IA etica"
- Percorso fake news con le classi seconde.
- Collegamento col laboratorio formativo IA: limiti, bias, responsabilità.

### innovazione.html — "Strumenti e automazione"
- Script Python (python-docx) per generare verifiche differenziate e griglie di valutazione.
- Flussi Google Classroom, supervisione Veyon, database HSQLDB.
- Frammenti di codice reali (C++/SQL/Python) come elementi grafici.

**Fonti dei contenuti** (estrarre e riadattare, non copiare verbatim):
- `Scuola/anno di prova/esperienze_portfolio_indire.md` (le 3 esperienze — nucleo narrativo)
- `Scuola/anno di prova/dossier_finale/CHECKLIST_DOSSIER.md` (date e tappe)
- `Scuola/CLAUDE.md` (programmi didattici, struttura classi, convenzioni verifiche)
- Relazione P2P per la sezione peer-to-peer

**Privacy**: nessun nome studente, nessun voto individuale, solo numeri aggregati. Nomi tutor/scuola ok. Nessun riferimento a documenti personali sensibili.

## Indicazioni di design (NON prescrittive — il progetto grafico lo fanno le skill)

**Vincoli e direzione voluti dall'utente:**
- **Taglio moderno e contemporaneo** — NON editoriale (niente serif da rivista, niente impostazione da pubblicazione di pregio).
- **Vietati i toni sabbia/crema/beige** che ricordano il branding Claude/Anthropic. Vietati anche i gradienti viola/rosa da "estetica AI generica".
- Identità del soggetto: docente di **Informatica** — dettagli tech (monospazio per dati/codice, riferimenti al coding) benvenuti.
- Tema chiaro come modalità principale (proiezione al colloquio); contrasto WCAG AA; `prefers-reduced-motion`; focus visibili; niente emoji come icone (SVG).
- Responsive 375/768/1024/1440; print CSS essenziale.

**Componenti richiesti** (resa grafica libera): navbar sticky, hero d'impatto, riga KPI con numeri animati, timeline verticale con ancore, card di approfondimento, blocchi codice, footer sobrio.

**Checkpoint visivo:** anteprima della home (hero + tratto di timeline) da confermare con l'utente PRIMA di costruire tutte le pagine.

## Verifica

- `index.html` via `file://` **senza rete** (font e asset devono caricare).
- Responsive a 375px e 1440px; nessuno scroll orizzontale.
- Tutte le ancore della timeline e i link tra pagine.
- Contrasti AA; tab-order e focus visibili.
- `prefers-reduced-motion`: KPI mostrano subito il valore finale.
- Anteprima di stampa decente.
- Dopo il deploy: check sull'URL GitHub Pages da altro dispositivo.
- Scansione finale privacy nel HTML.
