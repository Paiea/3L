#!/usr/bin/env python3
import hashlib, json, subprocess, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAPTURES=ROOT/"drafts/record-133/audio/captures.json"
BUILD=ROOT/"build/ending-last-meal"
FINAL=BUILD/"ending-last-meal-experiment.mp3"
VERIFY=BUILD/"verification.json"
BUILD.mkdir(parents=True,exist_ok=True)
clips=BUILD/"clips"; wavs=BUILD/"wavs"
clips.mkdir(exist_ok=True); wavs.mkdir(exist_ok=True)

data=json.loads(CAPTURES.read_text())
segments=sorted(data["segments"],key=lambda x:x["index"])
indices=[s["index"] for s in segments]
assert indices==list(range(1,157)), f"bad indices: {indices[:3]}..{indices[-3:]}"
assert data.get("routing_mode")=="exact_quote_locked"
voices={}
for s in segments:
    voices[s["voice_id"]]=voices.get(s["voice_id"],0)+1
assert voices=={"deep":82,"normal":74}, voices

def run(*args):
    subprocess.run(args,check=True)

for s in segments:
    idx=s["index"]
    mp3=clips/f"{idx:03}.mp3"
    wav=wavs/f"{idx:03}.wav"
    if not mp3.exists():
        urllib.request.urlretrieve(s["preview_url"],mp3)
    run("ffmpeg","-y","-loglevel","error","-i",str(mp3),"-ar","44100","-ac","1","-c:a","pcm_s16le",str(wav))

silences={}
for ms in sorted({s.get("pause_after_ms",0) for s in segments if s.get("pause_after_ms",0)} | {2000}):
    p=wavs/f"silence-{ms}.wav"
    run("ffmpeg","-y","-loglevel","error","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t",f"{ms/1000:.3f}","-c:a","pcm_s16le",str(p))
    silences[ms]=p

concat=BUILD/"concat.txt"
with concat.open("w") as f:
    for s in segments:
        f.write(f"file '{wavs/f'{s['index']:03}.wav'}'\n")
        ms=int(s.get("pause_after_ms",0) or 0)
        if ms:
            f.write(f"file '{silences[ms]}'\n")
    f.write(f"file '{silences[2000]}'\n")

combined=BUILD/"combined.wav"
run("ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",str(concat),"-c:a","pcm_s16le",str(combined))
run("ffmpeg","-y","-loglevel","error","-i",str(combined),"-codec:a","libmp3lame","-b:a","128k","-ar","44100","-ac","1",str(FINAL))

probe=subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(FINAL)],text=True).strip()
duration=float(probe)
sha=hashlib.sha256(FINAL.read_bytes()).hexdigest()
verification={
  "record":"ending-experiment-133",
  "title":"THE LAST MEAL",
  "authority":"noncanonical ending experiment",
  "routing_mode":"exact_quote_locked",
  "segment_count":len(segments),
  "voice_counts":voices,
  "index_range":[indices[0],indices[-1]],
  "missing_indices":[],
  "duplicate_indices":[],
  "handoff_floor_ms":1100,
  "tail_ms":2000,
  "duration_seconds":round(duration,3),
  "sha256":sha,
  "bytes":FINAL.stat().st_size,
  "automated_qc":"passed",
  "listen_back":"public experiment; ear-level approval remains separate from canon production approval"
}
VERIFY.write_text(json.dumps(verification,indent=2)+"\n")
print(json.dumps(verification,indent=2))
