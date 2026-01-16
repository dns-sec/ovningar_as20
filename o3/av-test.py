#!/usr/bin/env python3
import platform
import time
from pathlib import Path

system = platform.system()

if system == "Windows":
    print("Windows upptäckt. Scriptet fortsätter..")
elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    raise SystemExit(1)
elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    raise SystemExit(1)
else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    raise SystemExit(1)

eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

desktop = Path.home() / "Desktop"
file_path = desktop / "av-test-fil.txt"

try:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        f.write(eicar_str)

    print(f"[+++] Fil skapad på skrivbordet: {file_path}")
    time.sleep(3)

    with open(file_path, "r", encoding="utf-8") as f:
        fil_innehall = f.read()

    if fil_innehall == eicar_str:
        print("[+++] Filen kunde läsas och innehållet matchar EICAR-signaturen.")
        print("[---] Antivirus har inte tagit bort/karantänat filen (än).")
    else:
        print("[!!!] Filen kunde läsas men innehållet matchar inte EICAR-signaturen.")
        print("[---] Något har ändrat filen eller skrivningen blev inte korrekt.")

except Exception:
    print("[!!!] Filen kunde inte läsas!")
    print("[!!!] AV har tagit bort/karantänat filen.")
    print("[---] Din AV/EDR-lösning är helt fungerande och skyddar mot kända virus-signaturer.")

