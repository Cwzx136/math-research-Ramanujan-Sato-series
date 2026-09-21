# Prior-work check for the added Introduction

Date: 2026-09-20. Scope: read-only review of the revision's bibliography, main period/comparison/arithmetic/scarcity sections, extensions appendix, the local CGG primary-source TeX, and the stylistic predecessor's introduction. No TeX or PDF was modified by this review.

## Supported historical outline

1. **Ramanujan's starting point.** Ramanujan's 1914 paper links rapidly convergent series for `1/pi` to modular equations. The local primary-source archive `problems/ramanujan-sato/attempts/cgg-source.tex`, Introduction, explicitly attributes 17 classical series to equations (28)–(44) of that paper. An Introduction need not retain the number 17; the qualitative statement is enough.
2. **The modular/CM construction and the known tables.** CGG describes a uniform construction from elliptic families, Picard–Fuchs equations, hypergeometric period formulas, and evaluation at imaginary quadratic parameters. Its Introduction and final section explicitly identify its 36 Clausen cases with the level 1–4 single-sum list of Chan–Cooper. It says this gives evidence for completeness because the uniform construction can only produce those 36 cases. This is the right place to explain the present converse problem: completeness among CM constructions does not prove that every algebraic scalar identity comes from CM.
3. **Further Ramanujan–Sato families.** Existing keys `CCL` (Domb-number identities), `RogersDomb` (hypergeometric transformation used in the Domb appendix), `CCY` (quadratic irrational analogues and the level-nine transformation), `AG` (Ramanujan–Sato-like series), `CGG` (noncompact arithmetic triangle groups), and `Yang` (Shimura-curve identities) support a short account of the expanded setting. Do not imply that these sources prove unconditional exhaustion for arbitrary algebraic parameters, nor that every Shimura evaluation is an algebraic multiple of `1/pi` without additional CM periods.
4. **Transcendence input.** Existing `Waldschmidt` / `WaldschmidtSurvey` give the exact Chudnovsky consequence used here: `h/omega` and `pi/omega` are algebraically independent. This establishes projective uniqueness and nonvanishing, but does not rule out `a omega^2+b omega h=alpha pi` on a non-CM fiber. `Fonseca` supports the stated Nesterenko theorem and the elliptic-period and modular-value conjectures; `EterovicMSCD` supports the modular Schanuel conjecture with derivatives. The Introduction should clearly separate these conjectural sufficient inputs from the unconditional transcendence theorem.
5. **Comparison theory.** The checked `KSV` result applies to complete algebraic de Rham–Betti tensors and endomorphisms. A single algebraic coordinate does not meet that hypothesis. The revision's exact-completion theorem makes the missing datum explicit: one further algebraic matrix entry forces completion and CM. Do not summarize this as an unconditional application of KSV to the original scalar identity.
6. **Arithmetic and scarcity tools.** `BRSTT` supplies finite hypergeometric congruences and CM supercongruences, with different hypotheses that must be retained. `Tang`, `Serre`, `Deuring`, and `Faltings` support distinct arithmetic criteria. `DHK2022` is used for the specialization route, and `HabeggerPilaCounting` for compact counting. These are ingredients for the revision's additional results; avoid claiming their published conclusions already answer the converse problem.

## Exact local bibliography candidates

The current revised bibliography has no classical Ramanujan item and no direct Chan–Cooper item. Both may be added from checked local records.

### Ramanujan

`Hint/paper_old.tex` at lines 2101–2104 reads:

```latex
\bibitem{Ram}
S. Ramanujan,
\emph{Modular equations and approximations to \(\pi\)},
Quarterly Journal of Mathematics 45 (1914), 350--372.
```

The CGG archive at line 2269 independently gives the same author, title, volume, year, and pages, abbreviating the journal as `Quart. J. Math. (Oxford)`. Using the neutral full title from the Hint archive avoids carrying over the archive's potentially anachronistic `(Oxford)` qualifier. A new key `Ramanujan` is free in the revised bibliography.

### Chan–Cooper

The CGG archive at line 2241 gives:

```latex
\bibitem{ChanCooper}
H. H. Chan and S. Cooper,
\emph{Rational analogues of Ramanujan's series for $1/\pi$},
Mathematical Proceedings of the Cambridge Philosophical Society
\textbf{153} (2012), no.~2, 361--383.
```

CGG's final section explicitly identifies its four level lists with Chan–Cooper Tables 3–6. The archived CGG source itself is enough to substantiate a conservative sentence about the known 36 evaluations, especially with a joint `ChanCooper,CGG` citation.

### Optional Chudnovsky historical item

The CGG archive at line 2247 gives:

```latex
D. V. Chudnovsky and G. V. Chudnovsky,
\emph{Approximation and complex multiplication according to Ramanujan},
in \emph{Ramanujan Revisited}, Academic Press, Boston, 1988,
pp.~375--472.
```

This is optional for a concise Introduction. Distinguish this construction reference from the transcendence input attributed to Chudnovsky and quoted precisely through Waldschmidt.

## Suggested narrative order

Open with the classical phenomenon and the scalar converse. State the precise scope: four standard branches, integer denominators, primitive coefficient pair, ordinary convergence. Present the central distinction between unconditional uniqueness/CM classification and conditional exhaustion. Explain the intrinsic mechanism (period square, first jet, selected de Rham line, CM complementary eigenline). Explain the comparison obstruction without reproducing its matrix calculation. Then describe the finite class-number step, the complementary arithmetic/scarcity results, and the organization by sections and thematic appendices.

The claims do not require any new mathematical result or new internet research. The literature paragraph can be two compact paragraphs, with detailed technical dependence left in the proofs.
