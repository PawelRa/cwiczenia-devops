# Zadanie domowe 25 - Jenkins Pipeline

## Cel zadania
Celem zadania było utworzenie pipeline'u w Jenkinsie dla prostej aplikacji z etapami:
- Checkout
- Build
- Test
- Deploy

## Repozytorium
W zadaniu wykorzystano publiczne repozytorium Git:
`https://github.com/PawelRa/cwiczenia-devops.git`

Gałąź robocza:
`Praca_domowa_25`

## Opis pipeline'u

### Checkout
Pipeline pobiera kod z repozytorium GitHub.

### Build
W etapie build tworzony jest artefakt `build/artifact.txt`.

### Test
Pipeline sprawdza:
- czy plik `artifact.txt` istnieje,
- czy zawiera oczekiwaną treść.

### Deploy
Artefakt jest kopiowany do katalogu:
`/tmp/jenkins-deploy`

## Wynik
Pipeline zakończył się statusem **SUCCESS**.

## Artefakty
Dodatkowo artefakt został zapisany w Jenkinsie przez `archiveArtifacts`.

## Użyte technologie
- Ubuntu
- Jenkins
- Git
- GitHub
- Java 21
- Maven

## Pliki wynikowe pipeline

Po wykonaniu pipeline tworzone są następujące pliki:

- `build/artifact.txt` – artefakt utworzony w etapie Build
- `build/notification.txt` – plik z informacją o statusie wykonania pipeline

Pliki są widoczne w workspace Jenkins:
`/var/lib/jenkins/workspace/praca-domowa-25-pipeline/zadanie_domowe_25/build`

Po etapie Deploy artefakt jest kopiowany do katalogu:
`/tmp/jenkins-deploy`
