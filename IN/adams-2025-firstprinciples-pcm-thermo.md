---
Title: "First-Principles Thermodynamic Analysis of Ternary Chalcogenide Phase Change Materials"
Author: "Felix Adams, Ichiro Takeuchi, Carlos Ríos Ocampo, Yifei Mo"
Reference: "https://github.com/felix-adams/ternary_pcm_polymorphs"
ContentType:
  - "pdf"
Created: 2026-05-25
Processed: true
tags:
  - "source"
---

Preprint from the University of Maryland (Mo group). NSF FuSe program (DMR-2329087). Uses DFT (PBE + r2SCAN / VASP) to screen 30 ternary chalcogenide mixtures along binary-binary tie lines.

## Key Claims

- **Framework**: Ostwald's rule applied to PCMs — the metastable rocksalt (RS) phase crystallizes first as a kinetically accessible intermediate; if RS energy is < ~10 meV/atom above the stable hexagonal phase, fast switching is expected.
- **GST validation**: RS < 10 meV/atom above hex → confirmed fast crystallization. R3̅m-derived ternaries far above cutoff → correctly excluded.
- **Promising tellurides**: GeTe–Bi₂Te₃ (RS 0–10 meV/atom; fast exp.), SnTe–Sb₂Te₃ and SnTe–Bi₂Te₃ (both hex and RS < 10 meV/atom).
- **Selenides underperform**: higher energies, complex orthorhombic structures, fewer RS-like polymorphs → more phase segregation. Exception: SnSe–Bi₂Se₃ (RS ~20 meV/atom, single-phase ternaries known).
- **Structural design principle**: binary parents with octahedral coordination → more likely to yield low-energy RS ternary polymorphs. Hexagonal Bi₂Se₃ (RS-like) enables favorable SnSe–Bi₂Se₃ landscape vs. orthorhombic Sb₂Se₃.
- **Multi-anion (Se/Te)**: GeTe–GeSe shows increasing RS energy with GeSe content → slower crystallization (confirmed); Bi₂Te₃–Bi₂Se₃ forms solid solution but lacks RS → slow PCM.
- **Limitations**: 0 K DFT; amorphous structures not included; kinetics not directly computed; functional properties (optical/electrical contrast) not calculated.

## Companion
See `Raw/Files/firstprinciplesPCMthermo.pdf.md` for full study guide.
