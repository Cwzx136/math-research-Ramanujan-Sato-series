# Further elliptic families and compact extensions

Output: `revision/20260919/appendices/extensions.tex`.
Original `paper.tex` and the Hint tree were read only.

## Coverage

| Original material | Revised location and treatment |
|---|---|
| 4530–4558: quadratic companion transform | First-jet pullback lemma and `sec:quadratic-companion-extra`; one triangular jet matrix explains all derivative transports. |
| 4559–4638: convergence, divisor test, five classes, extended hypothesis | `prop:quad-extra-five`; connection asymptotics and endpoint test retained. Integrality becomes the divisor argument. Counts 62/12/6/8 and the five exact surviving parameters retained. |
| 4640–4694: independent evaluations | Incorporated into the same proof. Three evaluations by transported standard slopes; two by a compact automorphism/period table and the determinant identity. |
| 4698–4772: level-nine theorem | `sec:nine`, `thm:nine`; exact radius, uniqueness, CM integrality, two evaluations, and enlarged hypothesis retained. |
| 4774–4856: Domb classification | `sec:domb`, `prop:domb-CM`; convergence and alternating endpoint, trace integrality, six divisor candidates, two CM classes, and enlarged hypothesis retained. |
| 4858–4978: Moonshine and returning correspondences | `sec:moonshine`; Fricke norm coordinate, shifts, infinite non-CM integral-coordinate examples, returning correspondence criterion, and exact chosen-branch derivative identity retained. The first three q-coefficients were omitted as redundant checks, not proof inputs. |
| 7250–7308: arithmetic correspondence bound | `sec:extensions`, `prop:arithmetic-correspondence-packet`/`prop:extension`; field-degree proof, order-conductor bound, norm correspondence, quotient-vs-coordinate degree distinction, and coordinate-field caveats retained. Added degree-delta caveat for a rational value of a non-birational coordinate. |
| 7311–7402: level-six class-number-four example | `prop:level6-h4`; exact CCY inputs and ordinary convergence, reduced forms, norm obstruction, ramified-ideal quotient explanation retained. |
| 7405–7451: compact Yang evaluation | Moved after the target theory; `eq:yang-example`, exact table data, beta-period identification, and Chudnovsky exclusion retained. |
| 7453–7530: compact monodromy obstruction | `prop:compact-monodromy-obstruction`; boundary inertia proof, finite covers/symmetric powers/twists/gauges, standard-cusp comparison, and scope restrictions retained. |
| 7532–7621: compact degree theorem | `prop:compact-cm-degree`; individual-point class-field theorem, residue-field diagram, no factor two, fixed-curve finiteness, rational class-number-four example, and optimal-order restrictions retained. |
| 7623–7750: compact period target and weights | `prop:rank-two-torsor-cm`, `eq:compact-normalized-square`, `eq:compact-natural-target`, `prop:compact-weight-obstruction`; intrinsic first-column/determinant proof replaces expanded polynomial. Actual quaternionic realization, variable Tate coordinate, numerical genericity, and rational-cycle requirements preserved. |
| 7752–7847: exact construction-theorem hypotheses | `subsec:triangle-source-packets`; CGG domain and quadratic-parameter hypotheses, E6 nonvanishing, torsion trace, Yang branch targets, Takeuchi scope, and AG three-equation/conjectural Calabi–Yau restrictions retained. |

## External inputs and proof scope

- CCY supplies exact specified germ/modular identities and special values, not a converse CM theorem.
- CGG specializes at quadratic parameters; its E2-star algebraicity needs E6 nonzero and uses a nonreal endomorphism. The special j=1728 precursor remains separate.
- Rogers's germ identity plus the displayed singular asymptotics proves Domb convergence.
- CM reciprocity and monic integrality are imported from the main classification section; the same exhaustive class-polynomial test is applied before the standard convergence filter for quadratic companions.
- González–Rotger is used only for the canonical Q-model with square-free level, coprime reduced discriminant, and optimal embeddings. A delegated read-only checker inspected the primary source: Theorem 5.8(1) is exactly H_R=K Q(P); Proposition 5.6 supplies the free class action on each orientation branch. The discriminant -120 example has no additional orientation branches; wording was simplified accordingly.
- The GL2 genericity and tensor-torsor genericity assertions remain explicitly conditional. Computing a group is not used as a proof of numerical genericity.
- All higher-family completeness claims outside CM retain their extra parameter-range independence hypotheses. No unconditional original CM forcing is claimed.

## Dependencies to retain at assembly

Cross-references outside this file:

- `prop:rational-cm-integrality`
- `sec:enumeration`
- `eq:cm-matrix-alpha`

The unconditional period theorem and positive-endpoint theorem are named in prose to avoid obsolete label dependence. Classification owner was notified about all three referenced labels and the retained Euler ownership.

Bibliography keys:
`CGG`, `CCY`, `RogersDomb`, `CN`, `GonzalezRotger`, `Yang`, `Waldschmidt`, `Takeuchi`, `AG`.

Macros/packages: the agreed `Q`, `Qbar`, `Z`, `C`, `thetaop`, standard theorem/proof environments, and `tikz-cd`; no new macro declarations.

All important original labels requested by root are preserved. No expanded large certificate polynomials are needed here: their algebraic roles are recorded by the monic trace, quotient norm, or an exact finite-test reference. Detailed finite certificates remain in the common certificate appendix.
