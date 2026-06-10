# Portfolio Anno di Prova — Riccardo Callà

Sito statico che racconta l'anno di formazione e prova 2025/2026 (Informatica A041, IIS Curie-Vittorini), costruito come supporto al colloquio davanti al Comitato di Valutazione del **15 giugno 2026**.

## Come aprirlo offline (piano A per il colloquio)

Nessuna dipendenza di rete: font e asset sono tutti locali.

1. Aprire la cartella del progetto.
2. Doppio clic su `index.html` — funziona anche senza wifi.

In alternativa, con un server locale:

```bash
python -m http.server 8741
# poi aprire http://localhost:8741
```

## Versione online

Pubblicazione prevista su GitHub Pages (repo `anno-di-prova`). Una volta attivata, l'URL sarà
`https://<username>.github.io/anno-di-prova/` — da aggiornare qui e da lasciare al Comitato.

## Struttura

```
index.html            ← home one-page: hero bento, KPI, timeline del percorso
classi.html           ← didattica nelle 5 classi (SA biennio, 3P e 4S SIA)
ed_civica.html        ← percorso fake news / uso etico dell'IA
innovazione.html      ← script Python, Classroom, Veyon, db "Biblioteca di Quartiere"
assets/
  css/style.css       ← design system "bento vibrante" (Outfit, blu/cyan/lime)
  js/main.js          ← menu mobile, count-up KPI, reveal-on-scroll
  fonts/              ← woff2 self-hosted (Outfit, JetBrains Mono)
design-system/        ← MASTER.md generato con ui-ux-pro-max (fonte di verità grafica)
docs/DESIGN.md        ← spec di progettazione approvata
```

## Uso durante il colloquio

- La home guida l'esposizione dall'alto verso il basso (bilancio iniziale → release finale).
- Le voci del menu e le ancore della timeline permettono di saltare alla sezione richiesta dal Comitato (`#bilancio`, `#coding`, `#lab-ia`, `#peer-to-peer`, `#collegialita`, `#release`).
- Le tre pagine di approfondimento rispondono alle domande su didattica, educazione civica e strumenti.

## Note tecniche

- Zero build: HTML + CSS + JS vanilla.
- Accessibilità: contrasti WCAG AA, `prefers-reduced-motion`, focus visibili, skip-link.
- Privacy: nessun dato di studenti; solo numeri aggregati.
