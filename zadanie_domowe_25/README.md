# Jenkins Pipeline – wersja podstawowa i zaawansowana

## Opis

Repozytorium zawiera rozwiązania zadań związanych z budową pipeline'ów w Jenkinsie.

W poprzednim zadaniu został utworzony podstawowy pipeline Jenkins z etapami:
- Checkout
- Build
- Test
- Deploy

Pipeline integrował się z publicznym repozytorium GitHub i tworzył artefakt wdrażany do wskazanego katalogu.

W obecnym zadaniu pipeline został rozbudowany do wersji zaawansowanej, zawierającej:
- obsługę błędów,
- warunkowe wykonywanie etapów,
- system powiadomień,
- zmienne środowiskowe,
- dodatkowe informacje o czasie wykonania, autorze zmian i wyniku builda.

## Repozytorium i gałęzie

Repozytorium:
`https://github.com/PawelRa/cwiczenia-devops.git`

Przykładowe gałęzie:
- `Praca_domowa_25` – wersja podstawowa pipeline
- `Praca_domowa_26_zadanie1` – wersja zaawansowana pipeline

## Etapy pipeline

Pipeline zawiera cztery główne etapy:

### 1. Checkout
Pobranie kodu z repozytorium GitHub oraz odczyt autora ostatniej zmiany.

### 2. Build
Symulacja budowy aplikacji poprzez utworzenie artefaktu tekstowego zawierającego:
- wersję aplikacji,
- środowisko,
- informację o wykonaniu builda,
- datę utworzenia.

### 3. Test
Weryfikacja poprawności artefaktu:
- sprawdzenie istnienia pliku,
- sprawdzenie oczekiwanej treści,
- potwierdzenie wersji aplikacji.

### 4. Deploy
Symulacja wdrożenia przez skopiowanie artefaktu do katalogu docelowego.

## Obsługa błędów

W każdym etapie zastosowano bloki `try-catch`.

W przypadku wystąpienia błędu:
- ustawiany jest status `FAILURE`,
- wyświetlany jest komunikat o błędzie,
- wykonywanie dalszych etapów zostaje przerwane lub ograniczone przez warunki `when`.

Dodatkowo pipeline posiada blok `post`, który obsługuje:
- sukces wykonania,
- niepowodzenie wykonania,
- akcje wykonywane zawsze po zakończeniu.

## Powiadomienia

Pipeline generuje powiadomienia zawierające:
- nazwę joba,
- numer builda,
- wynik wykonania,
- autora ostatniej zmiany,
- czas rozpoczęcia i zakończenia,
- adres URL builda.

Powiadomienia są:
- wyświetlane w logach Jenkins,
- zapisywane do pliku `notification.txt`,
- przygotowane do wysłania e-mail w przypadku sukcesu i błędu.

Uwaga:
rzeczywista wysyłka e-mail wymaga poprawnej konfiguracji SMTP w Jenkinsie.

## Zmienne środowiskowe

W pipeline wykorzystano zmienne środowiskowe:
- `APP_DIR` – katalog aplikacji,
- `BUILD_DIR` – katalog builda,
- `DEPLOY_DIR` – katalog wdrożenia,
- `APP_VERSION` – wersja aplikacji,
- `TARGET_ENV` – środowisko docelowe,
- `ENABLE_DEPLOY` – flaga włączająca wdrożenie,
- `NOTIFY_EMAIL` – adres do powiadomień,
- `BUILD_STATUS` – status pipeline,
- `COMMIT_AUTHOR` – autor ostatniej zmiany,
- `START_TIME` – czas rozpoczęcia pipeline.

Zmienne są używane zarówno w etapach, jak i w warunkach wykonywania.

## Pliki wynikowe pipeline

Po wykonaniu pipeline tworzone są następujące pliki:

- `build/artifact.txt` – artefakt utworzony w etapie Build
- `build/notification.txt` – plik z informacją o statusie wykonania pipeline

Pliki są widoczne w workspace Jenkins:
`/var/lib/jenkins/workspace/praca-domowa-25-pipeline/zadanie_domowe_25/build`

Po etapie Deploy artefakt jest kopiowany do katalogu:
`/tmp/jenkins-deploy-advanced`

## Archiwizacja artefaktów

Pipeline wykorzystuje `archiveArtifacts`, dzięki czemu pliki wynikowe mogą być przeglądane bezpośrednio w Jenkinsie po zakończeniu builda.

## Jak uruchomić

1. Uruchomić Jenkins.
2. Skonfigurować job typu Pipeline.
3. Ustawić repozytorium GitHub.
4. Ustawić odpowiednią gałąź, np. `Praca_domowa_26_zadanie1`.
5. Wskazać właściwą ścieżkę do `Jenkinsfile`.
6. Uruchomić build i przeanalizować wynik w `Console Output`.

## Wnioski

Wersja podstawowa pipeline pozwoliła zrozumieć działanie etapów Checkout, Build, Test i Deploy.

Wersja zaawansowana rozszerza pipeline o:
- obsługę błędów,
- kontrolę przebiegu wykonywania,
- system powiadomień,
- wykorzystanie zmiennych środowiskowych,
- lepszą dokumentację działania.

Dzięki temu pipeline jest bliższy rozwiązaniom stosowanym w rzeczywistych procesach CI/CD.

## Powiadomienia e-mail

Pipeline zawiera mechanizm wysyłki powiadomień e-mail po sukcesie i niepowodzeniu.
W przypadku braku konfiguracji SMTP w Jenkinsie błąd wysyłki jest przechwytywany, a informacje
o wyniku zapisywane są w pliku `notification.txt` oraz widoczne w logach pipeline.
