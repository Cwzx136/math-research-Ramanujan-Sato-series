# Revised presentation

Completed on 20 September 2026. The manuscript date records the start of the revision, 19 September 2026.

The revised master is [paper_revised.tex](../../paper_revised.tex), and the compiled manuscript is [paper_revised.pdf](../../paper_revised.pdf). The author is ZiXian Chang-Wang. The original 118-page `paper.tex` and `paper.pdf`, and the source and PDF of `hint_paper`, are unchanged; their SHA256 hashes are recorded in [original-hashes.json](original-hashes.json).

## Architecture and mathematical status

The revision has 68 pages. Its six main sections and closing statement occupy pages 1-22; supporting material starts on page 23. The conditional classification is the first principal theorem. The main argument then develops intrinsic elliptic period lines, comparison tensors, CM arithmetic, arithmetic CM criteria, and unconditional separation and counting results. Twelve appendix sections, supplied by ten input files, retain coordinate certificates, supplementary results, further families, and unsuccessful approaches.

The principal conceptual changes are:

- The Hodge line, Gauss-Manin connection, and determinant comparison organize the period identity and the CM complementary eigenline.
- Naturality of the adjoint construction separates one scalar period relation from a complete comparison tensor.
- CM descent and the degree of a modular correspondence precede the finite classification; all eight identity tables are collected with the certificate.
- Field norms replace expanded elimination polynomials in the main specialization argument, and Frobenius quotients organize finite transport in the appendix.
- Thirteen diagrams express the comparison, transport, and implication maps used in the proofs. The AMS presentation follows `hint_paper.tex`.

The key proofs state and use the relevant hypotheses and conclusions from their references. Named conjectures, cited theorems, deductions, and finite computational certificates remain distinct. The 36 standard and 35 linear Euler classes, their ordinary-convergence qualifications, and the normalization `gcd(A,B)=1` are retained.

**Unconditional CM forcing remains unresolved.** Existence of the listed identities and projective uniqueness are unconditional. Unrestricted exhaustion remains conditional on the explicitly stated quadratic-period independence hypothesis. The arithmetic criteria and scarcity theorems do not close that remaining implication.

The [coverage map](COVERAGE.md) records the relocation and consolidation of the original material. Individual rewrite and source-check records are in [notes](notes/).

## Review and build

Three separate AI adversarial reviews passed the complete final input tree, including the final corrections. Their scope and limitations are recorded in [AUDIT.md](AUDIT.md). These are AI-assisted checks, not human peer review or formal verification. The manuscript contains an explicit AI disclosure.

The final PDF was built with MiKTeX 25.12. From the research directory, run:

```powershell
.\build_paper_revised.ps1
```

The build runs three passes and checks for unresolved references and overflowing boxes. The delivered build has no unresolved references or citations, duplicate labels, or overflowing boxes. The log contains one nonfatal pdfTeX font-expansion warning; visual inspection found no associated defect. All 68 pages were rendered and inspected in six contact sheets; enlarged pages 3, 8, 26, and 45 were also inspected. The identity tables remain within their appendix.

[static-check.json](static-check.json) fixes the 21 audited TeX inputs. [final-manifest.json](final-manifest.json) records the delivered PDF, source and audit hashes, build and visual checks, and original-file preservation. Rebuilding can change the PDF hash through its metadata without changing the mathematical source.
