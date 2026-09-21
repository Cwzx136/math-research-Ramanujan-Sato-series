# Coverage of the revised manuscript

This map records how the original `paper.tex` was reorganized into `paper_revised.tex`. It is an editorial guide, not an additional mathematical audit. The original source and PDF remain the separate 118-page research version. Section names and page numbers below follow the compiled 68-page revision.

The principal distinction is unchanged: existence of the tabulated CM identities and projective uniqueness are unconditional; unrestricted exhaustion of complex identities remains conditional on quadratic-period independence (QPI). The arithmetic CM criteria retain their additional prime-density or exact Frobenius hypotheses. Neither scarcity nor the appendix countertests proves unconditional CM forcing or supplies a counterexample to the original assertion.

## Main argument

| Section | Original material retained in the main text | Revised organization |
|---|---|---|
| 1. The classification problem (p. 1) | Definitions, primitive-pair convention, logical scope, conditional classification. | [introduction.tex](sections/introduction.tex): states the conditional conclusion first, with ordinary convergence and `gcd(A,B)=1` explicit. |
| 2. Elliptic period squares (p. 3) | General first-order period-square theory, four realizations, Chudnovsky/Nesterenko input, uniqueness, convergence and endpoint exclusion. | [02_periods.tex](sections/02_periods.tex): determinant comparison and the identity line replace repeated frame calculations; detailed models move to A. |
| 3. Comparison tensors and the CM implication (p. 6) | The remaining implication, modular two-jets, sufficient period conjectures, complete comparison tensors and second-cycle propagation. | [comparison.tex](sections/comparison.tex): one evaluation space and the intrinsic trace-zero endomorphism identification organize the proofs; scope obstructions move to D. |
| 4. CM arithmetic and the classification (p. 10) | Finite arithmetic after CM, rational descent, exact standard evaluations and linear Euler companions. | [classification.tex](sections/classification.tex): modular correspondences and the complementary CM eigenline explain integrality and descent; the finite certificate and all eight tables move to B. |
| 5. Arithmetic realizations of the identity line (p. 14) | Weighted Cartier criterion, algebraization and stable-complement density, arithmetic classification, exact one-prime Hodge/Frobenius criterion. | [arithmetic.tex](sections/arithmetic.tex): conjugate filtration, universal extensions and the lifting diagram organize the arguments; precision limitations and residual counting move to C. |
| 6. Arithmetic separation and counting (p. 18) | Strongest signed-level denominator-gap theorem and counting in complete degree/height windows. | [scarcity.tex](sections/scarcity.tex): product monodromy, norm descent and the two-projection counting construction supply common proofs; weaker and broader variants move to F. |

The unnumbered “remaining assertion” on p. 22 identifies the missing complex-to-CM implication. The source results are incorporated where their conclusions are used; their hypotheses are not replaced by stronger numerical independence or specialization assertions.

## Thematic appendices

Twelve appendix sections are supplied by ten input files: `extensions.tex` supplies H, I and J.

| Appendix | Retained material and destination |
|---|---|
| A. Models and ancillary period consequences (p. 23) | [period_models.tex](appendices/period_models.tex): four explicit models, common de Rham calculation, scalar-relation field consequences, gauge/pullback functoriality and general conditional finiteness. |
| B. The finite CM certificate and the identity tables (p. 24) | [cm_certificates.tex](appendices/cm_certificates.tex): exhaustive finite CM data and exact provenance; 36 standard classes and 35 linear Euler companions in [standard_tables.tex](standard_tables.tex) and [euler_tables.tex](euler_tables.tex). |
| C. Integral realizations and the limits of prime tests (p. 27) | [arithmetic_details.tex](appendices/arithmetic_details.tex): finite Clausen/reflection, Cartier differentiation, rational-prime density, Tang's analytic order, unweighted tests, higher-precision obstructions and common-tensor criteria. |
| D. Scalar comparison and its refinements (p. 32) | [comparison_obstructions.tex](appendices/comparison_obstructions.tex): restricted directions, known independence and its limits, real cycle propagation, almost-holomorphic coordinates, tensor completion, local annihilators and failed logarithm linearizations. Formal countermodels retain their limited scope. |
| E. Analytic refinements of the scalar relation (p. 36) | [analytic_refinements.tex](appendices/analytic_refinements.tex): cusp lattice separation, growing rational height, finiteness on a fixed algebraic curve, incidence derivatives and fixed-isogeny-class finiteness. |
| F. Specialization beyond a first-order weight (p. 39) | [scarcity_refinements.tex](appendices/scarcity_refinements.tex): density-zero and degree-growth refinements, all polynomial weights, fixed elliptic pullbacks and the general elliptic-family version. |
| G. Frobenius quotients and canonical normalization (p. 45) | [truncations.tex](appendices/truncations.tex): Lucas normalization, finite transport, algebraic gauges, necessary geometric hypotheses, boundary terms and finite-jet obstructions. |
| H. Functoriality and further elliptic branches (p. 50) | [extensions.tex](appendices/extensions.tex): quadratic companions, level-nine pullback and Domb identities, with their own convergence and independence hypotheses. |
| I. Modular coordinates and returning correspondences (p. 53) | [extensions.tex](appendices/extensions.tex): Moonshine/Fricke coordinates, non-CM integral-coordinate examples, returning correspondence criterion and chosen-branch derivative identity. |
| J. Arithmetic correspondences and compact Shimura curves (p. 53) | [extensions.tex](appendices/extensions.tex): finite-map bounds, class-number-four example, compact monodromy obstruction, CM residue fields, realization-dependent period targets and the precise scope of construction theorems. |
| K. Two certificate mechanisms (p. 58) | [pade_wz.tex](appendices/pade_wz.tex): explicit exclusion for rationally proportional multipliers and converses within the two specified rational-certificate families. |
| L. Finite exclusions and a modular-jet family (p. 64) | [searches.tex](appendices/searches.tex): certified finite exclusions, additional exact searches and the non-CM modular-jet test family with its exact exclusion. |

Expanded coordinate calculations used only as checks remain in the original research archive when an intrinsic argument replaces them. The revision retains the necessary models, finite certificates and counterexamples without repeating every redundant polynomial expansion.

## Consolidated labels

The nine original labels listed as omitted in [static-check.json](static-check.json) are not unresolved references. Their content has the following destinations; no placeholder labels were added solely to preserve numbering.

| Original label | Consolidation |
|---|---|
| `prop:C-divergent-gaps` | The stronger signed-level absolute-gap theorem `thm:C-absolute-gaps` in §6 includes the same-level result. |
| `cor:C-cross-level-gaps` | The same theorem includes cross-level gaps and the opposite-sign collision case. |
| `cor:all-rational-cm` | Rational CM integrality `prop:rational-cm-integrality` and the CM classification in §4 incorporate exhaustion for rational arguments. |
| `eq:finite-clausen-modp` | Reduction of the retained mod-`p²` finite Clausen identity; §5 and C.1. |
| `eq:hierarchy-fonseca` | The sufficient numerical conjectures and implication diagram in §3.3; `prop:hierarchy-implications`. |
| `eq:hierarchy-gpc` | The same hierarchy, with the exact field comparisons in its proof. |
| `eq:hierarchy-mscd` | The same hierarchy; the MSCD implication remains expressly conjectural. |
| `eq:noncm-supercongruence` | C.5 retains unweighted zeros, supersingularity and the level-four infinitude/density statement. |
| `eq:weighted-clausen` | The unified `eq:cartier-weighted-factorization` in §5, with its finite-Clausen derivation in C.1. |

Detailed editorial records are in [periods](notes/periods.md), [comparison](notes/comparison.md), [classification](notes/classification.md), [arithmetic](notes/arithmetic.md), [scarcity](notes/scarcity.md), [analytic refinements](notes/analytic_refinements.md), [truncations](notes/truncations.md) and [extensions](notes/extensions.md). These notes also identify the original source ranges and the reasons for individual consolidations.
