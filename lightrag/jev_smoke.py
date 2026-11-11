"""
Jev smoke test (TypeSafe System One). Notes from the harvester project (HANDOFF-JEV, PLAN-JEV-REVIEW-LOG, jev2-calibration, 509 labelled pairs):
- Alias `jev-latest` works; response field `model` reports the served model (jev-1.13.0 on 2026-10-14). Answer shape: body["answers"][qid]["noul"] = float in [0,1]; body["usage"] has token counts.
- Question ids are not sent to the model: every question must be self-contained (instructions + criteria true/false).
- Errors: 401, 422, 429, 529. Retry 429/529 with backoff; harvester used 1 retry after 3 s, 20 s timeout. Fail open: no key / any error -> carry on, never kill the run.
- Host Python needs the system SOCKS proxy bypassed: httpx.AsyncClient(trust_env=False) / NO_PROXY=*. Console cp1251 crashes on non-ASCII titles: reconfigure stdout to utf-8.
- Labelling trap: preprint/journal twins have different DOIs, so labelling by identifier equality mislabels the key positive class. Analog here: labels must come from the substance, not from string equality; form words vs hydration/composition.
- Companion records (Supplementary document, retraction notice) were scored 'same' by Jev (correct as a work, wrong deliverable): Jev answers the literal question, so wording of the question decides edge cases.
- Calibration result there: same-pairs median p 0.94, different-pairs median 0.03; worst real false accept was 0.79 and a real twin landed at 0.78, i.e. the 0.8 line sits where hard cases land; thresholds 0.8/0.2 tradeoff: 0.80 accepted 40/43 twins, 0.85 -> 37, 0.90 -> 32. 'rule'-labelled pairs were only spot-checked (30/300): labels not hand-read are weaker.
- Labels here (`by: claude-review`) are Claude's judgement, not chemical ground truth.
"""
import os
import sys

import httpx

sys.stdout.reconfigure(encoding="utf-8")

BASE = "https://api.typesafe.ai/v1"
INSTRUCTIONS = (
    "Decide whether the PubChem record (pubchem_iupac, pubchem_formula) is the SAME substance "
    "that entity_name denotes. Form words (Nanoparticles, Powder, Nanofluid, Nanowire, Flakes) "
    "do not change the substance. A different compound, hydration state or composition is NOT the same."
)
PAIRS = [
    ("Aluminum", "aluminum", "Al", True),
    ("Carbon Dioxide", "carbon dioxide", "CO2", True),
    ("Graphene Oxide Nanoparticles", "graphene oxide", "(none)", True),
    ("Zno/water Nanofluid", "oxidane", "H2O", False),
    ("Graphene Oxide", "methane", "CH4", False),
    ("Sodium Sulfate Decahydrate", "disodium;sulfate", "Na2O4S", False),
]


def main() -> int:
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        print("no key")
        return 2
    hdr = {"Authorization": f"Bearer {key}"}
    ok_all = True
    model = usage = None
    with httpx.Client(trust_env=False, timeout=20) as c:
        try:
            r = c.get(f"{BASE}/models", headers=hdr)
            try:
                j = r.json()
                items = j.get("data", j) if isinstance(j, dict) else j
                print(r.status_code, [m.get("id") for m in items])
            except (ValueError, AttributeError, TypeError):
                print(r.status_code)
        except httpx.HTTPError as e:
            print("models error", type(e).__name__)
        for name, iupac, formula, expected in PAIRS:
            body = {
                "model": "jev-latest",
                "state": {"entity_name": name, "pubchem_iupac": iupac, "pubchem_formula": formula},
                "questions": {
                    "same": {
                        "type": "noul",
                        "instructions": INSTRUCTIONS,
                        "criteria": {
                            "true": "Same substance (form words ignored)",
                            "false": "Different compound, hydration state or composition",
                        },
                    }
                },
            }
            p = None
            try:
                r = c.post(f"{BASE}/systemone", headers=hdr, json=body)
                if r.status_code == 200:
                    j = r.json()
                    p = float(j["answers"]["same"]["noul"])
                    model, usage = j.get("model", model), j.get("usage", usage)
                else:
                    print(name, "HTTP", r.status_code)
            except (httpx.HTTPError, KeyError, TypeError, ValueError) as e:
                print(name, "error", type(e).__name__)
            ok = p is not None and (p > 0.5 if expected else p < 0.5)
            ok_all &= ok
            print(f"{name} | p={p} | expected={expected} | ok={ok}")
    print("model:", model, "usage:", usage)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
