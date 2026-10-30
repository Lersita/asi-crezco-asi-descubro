#!/usr/bin/env python3
# uso: kie.py MODELO ASPECTO RESOLUCION SALIDA.png "PROMPT" [URL_REF ...]
import sys, json, subprocess, time
model, ar, res, out, prompt, *refs = sys.argv[1:]
import os
AUT = ["-H", f"Authorization: Bearer {os.environ['KIE_API_KEY']}"] if os.environ.get("KIE_API_KEY") else []  # en la PC: export KIE_API_KEY=...
def curl(*a): return json.loads(subprocess.run(["curl","-sS",*AUT,*a],capture_output=True,text=True).stdout)
inp={"prompt":prompt,"aspect_ratio":ar,"resolution":res,"output_format":"png"}
if refs: inp["image_input"]=refs
r=curl("-X","POST","https://api.kie.ai/api/v1/jobs/createTask","-H","Content-Type: application/json","-d",json.dumps({"model":model,"input":inp}))
if r.get("code")!=200: print("ERROR",r); sys.exit(1)
tid=r["data"]["taskId"]
for _ in range(80):
    d=curl(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}")["data"]
    if d["state"] in ("success","fail"): break
    time.sleep(5)
if d["state"]!="success": print("FAIL",d.get("failMsg")); sys.exit(1)
url=json.loads(d["resultJson"])["resultUrls"][0]
subprocess.run(["curl","-sS","-o",out,url])
print(json.dumps({"out":out,"url":url,"credits":d.get("creditsConsumed")}))
