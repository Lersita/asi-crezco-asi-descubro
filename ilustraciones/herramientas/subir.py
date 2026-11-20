#!/usr/bin/env python3
# uso: subir.py ARCHIVO.png [...]  → imprime la URL temporal de Kie.ai de cada archivo (vence en unos días)
import sys, json, subprocess, os
AUT = ["-H", f"Authorization: Bearer {os.environ['KIE_API_KEY']}"] if os.environ.get("KIE_API_KEY") else []  # en la PC: export KIE_API_KEY=...
for f in sys.argv[1:]:
    nombre = f.replace("/", "_")
    r = json.loads(subprocess.run(["curl", "-sS", *AUT, "-X", "POST", "https://kieai.redpandaai.co/api/file-stream-upload",
        "-F", f"file=@{f}", "-F", "uploadPath=asi-crezco", "-F", f"fileName={nombre}"], capture_output=True, text=True).stdout)
    print(r["data"]["downloadUrl"] if r.get("success") else f"ERROR {f} {r}")
