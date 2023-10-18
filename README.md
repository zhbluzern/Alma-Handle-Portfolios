# Handle Electronic Portfolios in ExL Alma for ZentralGut

## Beschreibung

Dieses Code-Repository beinhaltet eine leichtgewichtige Python-Klasse mit der electronic Portfolios in ExLibris verhandelt werden können. Das Anwendungsszenario ist für die Kommunikation aus Intranda Goobi gedacht. Dort auf Basis von ExL-Katalogisaten angelegte Vorgänge schicken vor dem Export in den Viewer eine URL mit permanenten Identifikator in Form eines electronic portfolios zurück nach Alma.

## Hinweise

### XML statt JSON-Response
Response wird standardmässig mit dieser Python-Klasse als `json` erwartet. Soll dies geändert werden ist in der jeweiligen Funktion der Header des API-Calls zu ändern

```python
self.headers = {"Accept": "application/xml"}    
```

um den Response dann mit `lxml` zu bearbeiten soll die Funktion nicht `r.json()` retournieren sondern `r.content`. Die Weiterverabeitung kann dann bspw. erfolgen

```python
root = ET.fromstring(r.content)
```

## Create Portfolio

Necessary Metadata from MODS File for Portfolio Creation

* CatalogIDDigital -> `portfolio_data["resource_metadata"]["mms_id"]`
* mms-URL -> https://api-eu.hosted.exlibrisgroup.com/almaws/v1/bibs/{CatalogIDDigital} -> `portfolio_data["resource_metadata"]["link"]`
* TitleDocMain -> `portfolio_data["resource_metadata"]["title"]`
* MaterialType CODE -> `portfolio_data["material_type"]["value"]` (see following table)
* MaterialType Description -> `portfolio_data["material_type"]["desc"]` (see following table)
* activation date (current Date in Format YYYY-MM-DDZ e.g. 2023-09-28Z) -> `portfolio_data["activation_date"]` 
* Linking Details -> ARK-Resolving URL with prefix jkey= "jkey=https://n2t.net/{ARK}" -> `portfolio_data["linking_details"]["url"]` and  `portfolio_data["linking_details"]["static_url"]` 

### Material Type

Read in MODS-File `mets:div[@id='LOG_0000']` Attribute `TYPE` auslesen

| Code         | Description           | MODS DocStruct                |
|--------------|-----------------------|-------------------------------|
| BOOK         | Book                  | Monograph                     |
| CDROM        | CD-ROM                |                               |
| CONFERENCE   | Conference            |                               |
| DATABASE     | Database              |                               |
| DATASET      | Data Set              |                               |
| DISSERTATION | Dissertation          |                               |
| DOCUMENT     | Document              |                               |
| GOVRECORD    | Government Document   |                               |
| JOURNAL      | Journal               | PeriodicalVolume              |
| MANUSCRIPT   | Manuscript            | Manuscript, Act               |
| MAP          | Map                   |                               |
| MASTERTHESIS | Master Thesis         |                               |
| NEWSPAPER    | Newspaper             | NewspaperVolume               |
| OTHERVM      | Other Visual Material | Graphic, Object, Postcard     |
| PROCEEDING   | Proceeding            |                               |
| RECORD       | Sound Recording       |                               |
| REPORT       | Report                |                               |
| SCORE        | Musical Score         |                               |
| SERIES       | Series                |                               |
| STREAMINGA   | Streaming Audio       |                               |
| STREAMINGV   | Streaming Video       |                               |
| TRANSCRIPT   | Transcript            |                               |
| VIDEO        | Video                 | Video                         |
| WEBSITE      | Website               |                               |
| WIRE         | Wire                  |                               |

