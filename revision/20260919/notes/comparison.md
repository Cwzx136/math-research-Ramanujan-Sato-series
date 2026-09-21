# Comparison-theory revision and coverage

Source: original `paper.tex`, lines 843–1986. The original, all Hint files, and all other delegates' files were left unchanged.

## Main text

`sections/comparison.tex` organizes the material around four mathematical constructions:

1. The exact three-dimensional evaluation subspace on the comparison torsor. A restriction/evaluation diagram states the precise genericity premise; this is equivalent to QPI on the selected fibers.
2. The invertible period–two-jet dictionary. The full Ramanujan-identity calculation is retained in a single proof, with the forbidden affine quadratic jet relation and its unconditional one-dimensional relation bound as a corollary.
3. The hierarchy of sufficient numerical conjectures. The exact field equalities prove all arrows in a concise implication diagram. Fonseca 4.5, 4.8 and the one-point form of Eterović 2.3 are stated where used, without upgrading functional theorems to pointwise independence.
4. Intrinsic tensor completion. The natural isomorphism Sym²(H) ⊗ det(H)⁻¹ ≅ End₀(H) is defined by polarization and a genuine comparison square. KSV full faithfulness, coefficient restrictions and the algebraicity theorem are incorporated before the exact projector-completion proof. Second-cycle propagation completes the geometric interpretation.

The conditional CM proposition, exact completion equivalences, exact CM coefficient field, multiplier square condition, nilpotent constant-weight case and second-cycle iff criterion remain proved in the main text. The original projector is retained as one revealing coordinate formula, rather than repeated in several proofs.

## Appendix coverage

`appendices/comparison_obstructions.tex` retains and consolidates:

- The weak rational-direction restriction tQ − e_l and its exact equivalence to rational-slope exclusion.
- All exact field comparisons and their transcendence-degree deficits (main-text equalities are referenced, not repeated as independent results).
- Chudnovsky's compatibility with a hypothetical identity and its consequence that ω,h would be algebraically independent.
- Nesterenko's exact three-generator consequence, with the missing independent π made explicit.
- The j-closure diagnosis explaining why established Ax–Schanuel does not give numerical MSCD at these points.
- Mixed-cycle reality, including its converse, automatic real/pure-imaginary directions, the real-structure linearization, and exact modular cycle-transport formulas.
- The almost-holomorphic coordinate criterion, direct CM eigenvector proof and Masser scope.
- Both symmetric-bilinear and polynomial tensor coordinate conventions, the determinant identity, exact coefficient-field distinction and the nilpotent warning (latter is already in the main text).
- The local annihilator-lift iff criterion with irreducibility proof, exact KSV 3.6/5.8/5.13 scope, and the rank-19 versus rank-20 Kummer distinction.
- Projector affine-line and reality countermodels; torsor connectedness and scalar numerical evaluation countermodels.
- Tangent hyperplane nonalgebraicity, symmetric central-cocycle splitting, the discrete-central-period obstruction, 1-motive Hodge-type obstruction, and biextension/Hodge-class obstruction.

No failed approach is represented as a proof of CM forcing. No formal countermodel is represented as an algebraic elliptic or original-series counterexample. The repetitions diagnosing the same missing coordinate were consolidated.

## Labels and normalization

Normalizations were coordinated with `r19_period_theory`: h = −η, determinant +2πi, F = 3ω²/(2π²), and the original u_s,v_s are unchanged. Original section/proposition/equation labels were retained where meaningful; `eq:jet-second` now aliases the combined dictionary equation, and `prop:hierarchy-fields` aliases the hierarchy proposition whose proof contains the exact field comparison. Unreferenced original named-conjecture display labels are not carried forward as standalone numbered displays; the conjectures are stated in numbered prose.

No new bibliography entries or custom macros are needed. `tikz-cd` is used for three substantive diagrams. KSV's entry-field statement assumes the specified rational Betti basis.

Independent focused audit: `notes/comparison_independent_check.md`, which checked the original KSV and completion conclusions against the archived primary text and confirmed the intrinsic sign convention. The same independent checker reviewed both rewritten files and passed their mathematical arguments. Three missing backslashes before `left` were identified and corrected before integration.

Post-correction SHA256:

- `sections/comparison.tex`: `24D2C2879074C175093A04E4C3BFFCC2B4306995A728CD0A4F6CF6A2DA388669`
- `appendices/comparison_obstructions.tex`: `35138237756E6E5D7B86E9D9EE5378171F52718F5F95933D7A1C2A62EE724B3F`
