# Arithmetic separation and counting: editorial and proof record

## Ownership and scope

This rewrite changes only `revision/20260919/sections/scarcity.tex` and this note. The original 118-page source, PDF, and hint files are untouched. It consolidates the strongest signed-level gap theorem and the full-height counting theorem into one section, removing the weaker density theorem and repeated proofs of same-sign and cross-level special cases from the main narrative.

## Source ranges used

- Original `paper.tex`, lines 2281–2852: original density argument, reciprocal specialization, same-level gaps, cross-level gaps, signed-level collision case, degree growth, scope qualifications.
- Original `paper.tex`, lines 3502–3739: functional affine independence, vertical arcs, precise Habegger–Pila statement, normalized and primitive tuple counting.
- Original `paper.tex`, lines 671 ff.: unconditional value independence (referenced, not re-proved).
- `hint_paper.tex`, introduction and elliptic-period exposition: restrained amsart style, numbered structural statements, a commutative diagram expressing the actual geometry.
- Primary source `problems/ramanujan-sato/attempts/sources/baldi-binyamini-urbanik-2606.08882v2.txt`, Theorem 3.13, Definitions 3.11–3.12, and Remark 3.14.
- Primary source `problems/ramanujan-sato/attempts/sources/20260918C_counting_habegger-pila-1409.0771v1.txt`, Section 7 height definition and Corollary 7.2.

## Proof organization

1. State the strongest separation theorem for all four levels and both signs.
2. Prove one product-monodromy lemma using the Gauss rank-two system, Goursat, and adjoint traces in the collision case.
3. Deduce affine functional independence from the same symmetric-square projection and finite-cover monodromy.
4. State the exact archimedean fixed-field Bombieri–André theorem used; derive reciprocal specialization.
5. Replace the expanded norm polynomial by a field norm of a quadratic relation. This makes both its rationality and degree transparent.
6. State Habegger–Pila with both projections and its actual coefficient height; use the duplicated-parameter diagram to exclude nonvertical semialgebraic paths.
7. Normalize primitive tuples and bound heights, with fibers of size at most two.

## Source hypotheses retained

### Bombieri–André via BBU Theorem 3.13

- G-functions over one fixed number field; the manuscript uses only K=Q and the archimedean place.
- The special point must lie strictly within every convergence disc; u=1/t does so eventually.
- The exponent is the transcendence degree of the field of *all derivatives*, not automatically the number of functions. It is finite because each G-function satisfies a linear differential equation. The asymptotic application does not need to calculate it.
- The graph-fiber dimension criterion for strongly nontrivial relations is stated, and algebraic independence makes it automatic.
- Both height and smallness conditions are reproduced, including the logarithm of the indicated power of h.
- No bound on coefficient heights is added. The coefficient field is handled by norm descent from Q(alpha_1²/alpha_2²).
- BBU states exact degree; the at-most-degree form follows by applying the monotone bounds to each smaller positive degree. Constants can be enlarged without effect.
- Remark 3.14 permits nonhomogeneous relations by adjoining 1.

### Habegger–Pila Corollary 7.2

- The definable set lives in a fixed o-minimal structure; here it is R_an because the standard functions are analytic on a neighborhood of the compact interval.
- Heights are polynomial coefficient d-heights, exactly as in Section 7 of the source, not logarithmic Weil heights.
- Only the first projection is semialgebraic along the produced path; the second is merely required to be nonconstant. The construction Z={((z,a,b),t):t=z} puts the *entire normalized triple* in the arithmetic projection and duplicates z in the varying projection.
- The result gives a bound on distinct parameters; unconditional value independence makes each algebraic normalized fiber a singleton.
- The source's further conclusions about the starting point and analytic cell decomposition are not needed and are omitted.

## Subtleties explicitly retained

- The joint singular sets can coincide for opposite signs and D=R. The adjoint trace is -1 at Gauss argument one and 0,1,2,3 at infinity for the four signatures. This excludes a graph subgroup even in the collision case.
- Infinity monodromy for s=1/2 can be nondiagonalizable; trace of Ad still depends only on the eigenvalues and equals 3.
- Noncentral infinity monodromy for s=1/2 is proved using the global monodromy relation, not inferred from distinct exponents.
- Taking a finite cover for algebraic functional coefficients does not change connected SL2 monodromy.
- The norm conjugates algebraic coefficients only. It makes no assertion that conjugated multipliers remain identities on the chosen period branch.
- Alpha cannot be zero by the earlier value-independence theorem.
- Ordinary convergence is preserved at z=-1 through the branch convention established earlier. The counting interval includes it. The positive endpoint is excluded by the earlier unconditional theorem.
- Primitive means gcd(A,B)=1, not gcd(A,B,C)=1.
- Divergent gaps do not imply finiteness, and full-height subpower counting does not prove pointwise CM forcing.

## Labels and assembly

Preserved: `sec:C-density`, `thm:C-absolute-gaps`, `lem:C-reciprocal-specialization`, `sec:C-semirational-counting`, `thm:C-primitive-counting`, `thm:C-normalized-counting`, `thm:C-HP-counting`, `lem:C-functional-affine-independence`, `lem:C-vertical-arcs`, `eq:C-gauss-operator`, `eq:C-normalized-surface`.

New labels are prefixed `rev:`. Cross-section references use `thm:main-conditional`, `thm:unconditional`, and `thm:B-value-independent`. Bibliography keys remain `BaldiBinyaminiUrbanik2026` and `HabeggerPilaCounting`. The section uses tikz-cd, already present in the hint style and expected in the revised preamble.

Removed weak labels (`thm:C-density-zero`, `prop:C-divergent-gaps`, `cor:C-cross-level-gaps`, `thm:C-BBU`) should be reconciled by the assembler or retained where the corresponding appendix material is moved; they are not silently attached to different theorem statements here.

## Independent source check

A delegated source audit independently verified BBU Theorem 3.13 and Habegger–Pila Corollary 7.2 against the archived primary texts. The audit emphasized the fixed coefficient field, derivative-field exponent, coefficient-height convention, and duplicated-parameter construction; all four safeguards are explicit in the rewrite.

The same independent reviewer then checked the completed draft. Two qualifications were repaired: rational substitutions must vanish at zero, not merely be regular there, and the fixed gap is explicitly an integer. The BBU constant is enlarged to c1 >= e so that the at-most-degree monotonicity is transparent. The reviewer found the norm descent, symmetric-square dominance, collision traces, normalization height, and projection diagram mathematically sound.

Final static checks: 480 source lines plus final newline; 2,314 whitespace-delimited words including formulas; no duplicate labels. The only references external to the section are the three deliberate theorem references listed above. Compilation is left to the root assembler, avoiding writes outside this agent's two owned files.
