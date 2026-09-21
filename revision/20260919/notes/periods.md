# Period-theory rewrite

## Files and status

- Main contribution: `sections/02_periods.tex`.
- Supporting appendix: `appendices/period_models.tex`.
- The original `paper.tex`, original PDF, `hint_paper.tex`, and all verified tables were read only.
- This is an expository reorganization of original lines 181–842. It makes no new CM-forcing claim.

## Conceptual organization

The main argument now follows a single construction. The Hodge line in rank-two de Rham cohomology and the Gauss–Manin connection define an invertible coefficient map. Its complex evaluation gives the original first-order identity. A determinant-comparison diagram identifies the Tate normalization. Chudnovsky makes evaluation injective; a CM endomorphism identifies the unique complementary eigenline and its Tate-valued pairing. The same argument yields the CM independence needed for the endpoint. The standard models then enter only through the Gauss equation, the common nodal residue, and the nonzero Kodaira–Spencer coefficient.

The stronger value theorem incorporates the exact Chudnovsky and Nesterenko conclusions, including the nome, into one field comparison. The main text retains the distinction between the known ratio independence and the unproved quadratic-period independence.

## Source-result integration

- Waldschmidt, Corollary 4 / survey Corollary 31: algebraic independence of eta/omega and pi/omega, transferred explicitly to arbitrary algebraic de Rham frames. The half-period specialization and Legendre sign are supplied.
- Waldschmidt, Corollary 6 / survey Corollary 32: recovered within the CM eigenline proof, rather than quoted as a black box.
- Fonseca, Theorem 1.1 and Proposition 4.7: Nesterenko's full three-variable transcendence-degree conclusion and the period expressions for E2, E4, E6 imply independence of the nome and the two standard values.
- Cox: the ring class field degree is used explicitly in the general conditional finiteness appendix. The sharp small-degree enumeration remains the classification section's task.

## Disposition of original results

| Original item | Revised destination |
|---|---|
| General identity-line theorem | Main, same label `thm:general-identity-line`; proof through the coefficient map and CM determinant. |
| General frame-change calculation | Subsumed by intrinsic coefficient-class covariance; no need to list three transformed scalar coefficients. |
| Algebraic gauge/pullback transport | Appendix, same label `eq:general-pullback-transport`; both ramification and convergence cautions preserved. |
| General bounded-degree finiteness | Appendix, same label `thm:general-finiteness`; proof retained. |
| Convergence analysis | Main, joined to the endpoint proof; same label `eq:asymptotic`. |
| Explicit four Weierstrass models | Appendix; same mathematical models and discriminants. |
| Normalization and differentiation lemma | Main, same label `lem:period`; connection matrix and polynomial reduction moved to appendix. |
| Four-entry u,v table | Replaced by the logarithmic discriminant formula and epsilon=(1,1,1,2); same `eq:logderivative`. |
| Exact Chudnovsky theorem | Main, same label `thm:B-chudnovsky`; arbitrary-frame formulation already used in the original general theorem. |
| CM period independence | Main corollary, same label `prop:B-CM-independent`; subsumes the second copy of the CM determinant calculation. |
| Standard value and nome independence | Main, same label `thm:B-value-independent`; field equality replaces inverse-coordinate bookkeeping. |
| Complete scalar relation space | Main corollary, same label `prop:B-relation-space`; injective projection proof. |
| Exact ideal/value-field consequence | Appendix, same label `prop:B-value-field`. |
| Period-field consequence | Appendix, same label `prop:B-period-field`. |
| Schneider discussion | Its only point needed here is retained as the distinction between ratio and quadratic-period independence; formal Schneider/conjecture comparisons belong to the comparison section. |
| Positive endpoint exclusion | Main, same section label `sec:endpoint`; explicit two-isogeny calculations moved to appendix. |

All old labels within the assigned range are preserved. No label from outside the assigned range is required by these two files. The appendix's new label is `rev:period-models`.

## Independent audit

Subagent `period_audit` independently read the original assigned range and checked the primary Waldschmidt statement. It confirmed the Chudnovsky normalization, the CM eigenline determinant, the integral nonprimitive-cycle case, the nodal normalization, and the endpoint argument. It explicitly confirmed that the endpoint cannot be treated as an admissible specialization because the parameter derivation is singular there. A second pass on the rewritten files found no substantive proof gap or syntax defect. Its two precision edits were applied: the comparison diagram is stated at an algebraic fiber, and the general degree theorem explicitly requires a compactification and parameter map over K0.

## Assembly requirements

Use `tikz-cd`, standard theorem environments, and the existing macros `Q`, `Qbar`, `C`, `Z`, `thetaop`. Citations: `Waldschmidt`, `WaldschmidtSurvey`, `Fonseca`, `CoxCM`. The material should occupy roughly six to eight main-text pages plus three to four appendix pages in the hint style. Final layout and labels must be checked in the assembled MiKTeX build.
