# Introduction: prior-work and attribution delta review

Date: 2026-09-20.

Reviewed the new `revision/20260919/sections/introduction.tex` in full and the two additions to `revision/20260919/bibliography.tex`. Read-only review; no TeX was edited. Scope is the Introduction's sources, historical attributions, and summaries of existing results, not a new audit of the entire paper.

## Result

The literature claims and the new bibliography entries are supported. Two small precision corrections are recommended below; there is no substantive attribution error or new mathematical overclaim in the reported results.

1. Replace “The quadratic relation needed for the CM converse is stronger than the particular consequences of these theorems used here” with “The quadratic-period independence sufficient for the CM converse is stronger than the particular consequences of these theorems used here.” The logical input is exclusion of a relation, not the relation itself.
2. Replace “Quadratic-period independence expresses precisely the numerical exclusion needed for the original families” with “Quadratic-period independence gives an explicit numerical exclusion sufficient for the original families.” The main text explicitly distinguishes exclusion of all algebraic coefficient directions (QPI) from exclusion of rational coefficient directions (sufficient for the original classification problem). The Introduction should preserve that distinction and not suggest that QPI is the weakest possible input.

Subject to these wording corrections: **PASS**.

## Source correspondence

- `Ramanujan1914`: author, title, journal, volume, year, and pages agree with `Hint/paper_old.tex:2101–2104`; the CGG archive independently confirms the same bibliographical data. The neutral journal title avoids the archive's unnecessary `(Oxford)` qualifier.
- `ChanCooper`: agrees with the entry in `problems/ramanujan-sato/attempts/cgg-source.tex:2241`. The statement about the level 1–4 rational analogues is conservative.
- `CGG`: the local primary-source Introduction and its final “Ramanujan type series and relation...” section explicitly identify the 36 Clausen cases with Chan–Cooper Tables 3–6 and describe the rational-CM-uniformizer enumeration. The revised Introduction properly distinguishes this construction from exclusion of arbitrary non-CM special values.
- `CCL`: the general modular summation theorem is cited precisely as Theorem 2.1 in the classification proof. The local Campbell–Cooper–Ye text quotes it as Theorem 2.4; `attempts/20260918B_identity_sources.md` records the checked convergence qualification. The Introduction does not use it to claim a converse.
- `RogersDomb`, `AG`, `CCY`, and `Yang`: the descriptions match their stated subject and the transformations and normalizations actually used in the appendices. The wording about additional CM periods on compact Shimura curves is appropriately qualified.
- `Waldschmidt`, `WaldschmidtSurvey`, `Fonseca`, `EterovicMSCD`: the narrative retains the difference between proved transcendence/uniqueness and conjectural quadratic-period exclusion. It does not attribute the missing CM converse to Chudnovsky or Nesterenko.
- `KSV`: the paragraph accurately retains complete comparison data as a premise.
- `CoxCM`, `Watkins`: the Introduction's finite-order step agrees with the class-number and conductor argument in the classification section.
- `BRSTT`, `Tang`: the stated lower natural density threshold greater than 3/4 agrees with the arithmetic classification theorem, and the relation from polynomial identities to filtration is described as part of the present argument, not as BRSTT's standalone conclusion.
- `MaulikPoonen`: the one-prime summary retains good ordinary reduction, exact preservation, and the residue-field power of crystalline Frobenius. These are the crucial qualifications of the existing theorem.
- `BaldiBinyaminiUrbanik2026`, `HabeggerPilaCounting`: the bounded degree of the squared multiplier and complete height-window qualifications are preserved. The paragraph explicitly leaves isolated non-CM identities unresolved.

The organizational paragraph accurately describes the main sections and thematic appendices. No new internet research is required by these additions.

## Final delta verification

The current Introduction has been reread after both recommended precision edits. Both corrections are present. Final result: **PASS**, with no outstanding correction from this source/attribution review.

SHA-256 of the reviewed files:

- `revision/20260919/sections/introduction.tex`: `619A1F0D47BDE2A1111FFC27F6C59CA35CF156DBA2A4B4FE13E689F4CC5E6B39`
- `revision/20260919/bibliography.tex`: `1CDBAEA1D24338A24448692BE67BF38B902F3F50FCC9552C452BB750CD6DF2FF`
