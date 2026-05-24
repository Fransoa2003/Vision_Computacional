import json

datos = {
    "abre": {
        "calculadora": "calc.exe",
        "navegador": "chrome.exe",
        "bloc de notas": "notepad.exe"
    }
}

with open("comandos.json", "w", encoding="utf-8") as file:
    json.dump(datos, file, indent=4, ensure_ascii=False)