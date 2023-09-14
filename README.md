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