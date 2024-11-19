# Prätherapeutisches Tumorboard für Prostatakarzinompatienten

Dieser Algorithmus dient der automatischen Generierung von Empfehlungen für das prätherapeutische Tumorboard.
Es handelt sich hierbei um Patienten mit einem histologisch gesicherten Prostatakarzinom, wo die weitergehende Diagnostik und Therapie multidisziplinär besprochen werden soll.

Das Modell basiert auf dem Sprachmodell GermanT5/t5-efficient-gc4-all-german-small-el32 und wurde mit ca. 4200 Tumorboard-Anmeldungen (Stand November 2024) und den entsprechenden Tumorboard-Empfehlungen als Labels feinreguliert.

Die App benutzt das Streamlit Framework als Frontend und läuft als Server über die [Streamlit Community Cloud](). Das Sprachmodell läuft aktuell als Backend-Server auf einer CPU-Instanz über AWS EC2 t3 micro.

> [!Warning]
> Es handelt sich um ein Projekt in Entwicklung ohne entsprechende Zulassung und ist daher nur für den experimentellen Einsatz geeignet.
