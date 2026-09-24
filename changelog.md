# Changelog

Wszystkie istotne zmiany w projekcie są opisywane w tym pliku.

## [0.5.1] - 2026-09-24

### Added

- Mechanizm walidacji pól wprowadzania: zablokowano możliwość wprowadzania znaków innych niż cyfry na poziomie zdarzeń systemowych Tkinter.
- Dynamiczne placeholdery: zastąpiono statyczne prefillowanie danych wyszarzonymi placeholderami, które znikają przy interakcji, zwiększając czytelność UX.
- Asynchroniczny „Key Grabber”: dodano wielowątkowy system nasłuchujący z wykorzystaniem biblioteki `pynput` dla opcji „Custom”. Przechwytuje on globalne zdarzenia klawiatury oraz dodatkowych przycisków i rolki myszy.
- Debouncing: wprowadzono czasowe opóźnienia i warunki ucieczki w asynchronicznym rejestratorze wejść, zapobiegając wychwytywaniu lewego kliknięcia aktywującego pole.

### Changed

- Zarządzanie stanem: pola wprowadzania dla „Offsets”, „Custom key” oraz „Repeat X times” są domyślnie wyszarzone i zablokowane (`state="disabled"`). Ich edycja jest możliwa dopiero po aktywacji dedykowanego przełącznika.
- Logika trybu „Hold”: zaznaczenie opcji „Hold” wymusza typ kliknięcia „Single” oraz dezaktywuje i wyszarza całą sekcję zarządzania powtórzeniami („Click Repeat”).
- Wzajemne wykluczanie (radio behavior): skonfigurowano wykluczanie się opcji dla pętli powtarzania (limitowana ilość vs nieskończoność) oraz dla klawiszy modyfikujących (Ctrl, Alt, Shift, Custom).

## [0.5.0] - 2026-09-24

### Added

- Architektura środowiska: zainicjalizowano projekt ze środowiskiem wirtualnym (`venv`) oraz systemem kontroli wersji Git, zabezpieczonym plikiem `.gitignore`.
- Szkielet graficzny GUI: utworzono w pełni responsywny interfejs przy użyciu CustomTkinter i systemu Grid, zgodny z bazowym schematem ułożenia.
- Autorski system nawigacyjny (Custom Router): wdrożono dynamiczne zarządzanie widokami poprzez metody `.grid()` i `.grid_forget()`, co umożliwiło horyzontalne wyrównanie przycisku „Settings” z głównymi trybami działania.
- System kontenerów: podzielono logikę wizualną na oflagowane obramowaniem grupy robocze (Group Boxes) dla sekcji „Click Interval”, „Click Options” oraz „Offsets”.
- Przyciski funkcyjne i status: wdrożono sekcję kontrolną ze statusem działania, przypisanymi elementami Start/Stop oraz stopką z danymi o wersji.
