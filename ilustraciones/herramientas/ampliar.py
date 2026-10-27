#!/usr/bin/env python3
# Amplía una imagen para imprenta con Kie.ai.
# uso: ampliar.py recraft|topaz URL_IMAGEN SALIDA.png   (topaz: ×2; recraft: crisp upscale)
import sys, json, subprocess, time
modelo, url, out = sys.argv[1:4]
def curl(*a): return json.loads(subprocess.run(["curl", "-sS", *a], capture_output=True, text=True).stdout)
if modelo == "recraft":
    cuerpo = {"model": "recraft/crisp-upscale", "input": {"image": url}}
else:
    cuerpo = {"model": "topaz/image-upscale", "input": {"image_url": url, "upscale_factor": "2"}}
r = curl("-X", "POST", "https://api.kie.ai/api/v1/jobs/createTask", "-H", "Content-Type: application/json", "-d", json.dumps(cuerpo))
if r.get("code") != 200: print("ERROR", r); sys.exit(1)
tid = r["data"]["taskId"]
for _ in range(120):
    d = curl(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}")["data"]
    if d["state"] in ("success", "fail"): break
    time.sleep(5)
if d["state"] != "success": print("FAIL", d.get("failMsg")); sys.exit(1)
res = json.loads(d["resultJson"])["resultUrls"][0]
subprocess.run(["curl", "-sS", "-o", out, res])
print(json.dumps({"out": out, "credits": d.get("creditsConsumed")}))
