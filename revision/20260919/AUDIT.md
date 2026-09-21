# Final revision audit record

## Expanded Introduction: 70-page delivery

On 20 September 2026 the Introduction was expanded at the user's request to discuss the problem, prior research, core ideas, and organization. Only `sections/introduction.tex` and `bibliography.tex` changed among the 21 TeX inputs. The pre-existing formal statement and proof block in the Introduction is unchanged. The remaining nineteen inputs match the fully reviewed baseline byte for byte.

Three focused AI reviews passed: [prior research and citations](../20260920-introduction/prior-work-review.md), [mathematical scope](../20260920-introduction/scope-review.md), and [editorial structure](../20260920-introduction/editorial-review.md). Two precision suggestions were incorporated: quadratic-period independence is explicitly described as a sufficient condition, and its strength is distinguished from known independence results.

MiKTeX compiled the updated 70-page PDF successfully. All references and citations resolve, all labels are unique, and no overflowing boxes remain. All pages were visually inspected in six contact sheets, with pages 1-4 also inspected at higher resolution. The original 118-page source/PDF and Hint source/PDF remain unchanged. Current hashes and warnings are recorded in [final-manifest.json](final-manifest.json).

The historical record below concerns the 68-page baseline. Its immutable [input manifest](../20260920-introduction/before/revision-static-check.json), [delivery manifest](../20260920-introduction/before/revision-final-manifest.json), and [PDF](../20260920-introduction/before/paper_revised.pdf) are preserved. Its references to a final snapshot or page count should be read in that historical scope.

## Full-manuscript baseline review

The 68-page revision passed three separate AI adversarial reviews. Each report's final addendum covers the entire assembled manuscript and matches the baseline 21-input manifest; those addenda supersede any earlier limited-scope statement or page count in the reports.

| Review | Final scope and disposition |
|---|---|
| [Periods and comparison](audits/final_periods_comparison.md) | Full manuscript; period normalization, exact transcendence input, scalar versus complete tensors, CM descent, appendix arguments, and final deltas. PASS. |
| [Arithmetic](audits/final_arithmetic.md) | Full manuscript; classification, finite certificates, density, exact one-prime criterion, specialization, further families, and final deltas. PASS. |
| [Scope and architecture](audits/final_scope_architecture.md) | Full manuscript; all main and appendix proofs, thirteen diagrams, eight tables, conditional scope, preservation, and final deltas. PASS. |

The period review also has a dedicated [primary-source report](audits/final_period_sources.md). Focused source and proof checks are retained under `notes/` and `audits/`.

## Final corrections checked by all three reviewers

- The eight tables use a nonfloating environment so that they remain in the certificate appendix. Only layout differs from the verified table sources.
- The modular-jet substitution explicitly cites both equations it uses.
- The local-slope proposition explicitly assumes `p>3` and `z in Z_p`, with `z` and `1-z` units and the fiber ordinary.
- The final analytic-refinement and Frobenius-quotient appendices include the reviewed precision and typography corrections.

No mathematical correction remains requested in the final reports. No TeX input was changed after the final manifest checks. Final delivery documentation does not alter the audited mathematical text.

## Reproducibility and preservation

The SHA256 of the [baseline input manifest](../20260920-introduction/before/revision-static-check.json) is:

```text
4A7830C41BE6CCA6D58EE7A395D5C08590916DDD3DE249EBE4A1DAE7BDB257E6
```

The final master source SHA256 is:

```text
6DB61F39088A9DA00BEEBC15C9C0F99907E1897EE23F8B5E29A92AA2B4EF7508
```

The manifest records 21 inputs, 7,067 source lines, thirteen diagrams, no duplicate labels, and no missing references or citations. Its nine omitted original labels represent consolidation; see [COVERAGE.md](COVERAGE.md).

The delivery check recomputed every input hash and all four preservation hashes in [original-hashes.json](original-hashes.json). The original 118-page source/PDF and `hint_paper` source/PDF match their pre-revision records exactly. The final PDF and audit report hashes are in [final-manifest.json](final-manifest.json).

MiKTeX compilation passed with no unresolved references or overflowing material. The final delivery check also identified one nonfatal pdfTeX font-expansion warning, which the earlier case-sensitive warning scan did not report. Visual review covered all 68 rendered pages and four enlarged samples and found no associated defect. The final PDF has 22 main-text pages, with appendices beginning on page 23. The delivery manifest records this warning explicitly.

## Limits of the review

These are independent AI sessions, not independent human peer review or machine-checked formal proofs. The large archived computations were not rerun for this editorial revision; reviewers examined the retained bounds, certificate descriptions, and their logical use. The work does not prove unconditional CM forcing or provide a counterexample to the original hypotheses. Its conditional classification remains conditional.
