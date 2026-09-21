# Independent audit of comparison and completion theory

Date: 19 September 2026. Scope: original `paper.tex`, approximately lines 1490–1980. The original manuscript was read only. This audit concerns proof correctness and intrinsic reformulation, not a new claim of unconditional CM forcing.

## Verdict

No substantive defect was found in the second-cycle criteria, exact projector completion, coefficient-field calculation, adjoint-tensor identification, or local annihilator-lifting criterion. The careful distinction between a scalar period identity and a complete de Rham–Betti class must survive the rewrite. The matrix calculations can largely be moved to an appendix without deleting their mathematical content.

## Primary-source check

I checked the local primary text `problems/ramanujan-sato/attempts/kreutz-shen-vial-derham-betti.txt`, especially Proposition 3.6, Theorem 5.10, Corollary 5.11, Theorem 5.12, Theorem 5.13, and its proof.

For an elliptic curve over the algebraic numbers and an algebraic coefficient field L, comparison-compatible endomorphisms are exactly `End^0(E) tensor_Q L`. The source requires the complete pair of endomorphisms, not one coefficient of the Betti matrix. Theorem 5.13(ii) applies over the full algebraic coefficient field to every power of one elliptic curve: there is at most one CM field among its simple factors. It is unsafe to export this assertion unchanged to products of curves from different CM fields.

For a non-CM elliptic curve, the algebraic-coefficient de Rham–Betti group is GL2. For a CM elliptic curve it is the CM torus, split after adjoining the CM field. The source explicitly distinguishes the comparison point's Zariski closure from its smallest algebraic subtorsor. Proposition 3.6 characterizes their equality; it does not prove that equality from connectedness or Theorem 5.13.

## Exact completion

Write the comparison matrix with de Rham classes as columns, normalize its determinant as `D=2 pi i`, and suppose

`w(a w+b h)=alpha pi`, with `b alpha != 0`.

Let `nu=a Omega+b Xi`, `u=a w+b h`, and `c=2 i b/alpha`. In the new de Rham basis `(Omega,nu)`, comparison has columns

`w(1,tau)` and `u(1,tau+c)`.

The determinant identity proves this statement immediately. Hence the projector with kernel the Hodge line and image the nu-line has Betti matrix

`(1/c) [[-tau,1],[-tau(tau+c),tau+c]]`.

The upper-right entry is the scalar datum supplied by the identity. Any one of the other three entries being algebraic makes tau algebraic; for the lower-left entry, this follows from a quadratic equation with coefficients in the algebraic numbers. Schneider then gives CM. Conversely, CM makes tau algebraic and completes the matrix.

There is no hidden use of a period conjecture here: the conditional input is exactly completion of the specified matrix. KSV gives a second conceptual proof of the complete-matrix implication, since a non-CM curve has only scalar algebraic-coefficient comparison endomorphisms.

## Coefficient field and sign

At CM, the two rank-one idempotents of `K tensor_Q Qbar` are precisely the eigenspace projectors. The kernel of the specified projector is the holomorphic eigenspace. Its image must therefore be the antiholomorphic eigenspace. The ratios of Betti coordinates in these two lines are tau and its complex conjugate; this remains true even when the chosen algebraic model and differential are not real. Consequently

`tau+c=conjugate(tau)`, and `b=-alpha Im(tau)`.

The sign follows from `det P=+2 pi i`; changing the determinant or the orientation reverses it. The rewrite should state the orientation once, then retain it consistently.

The entries of the projector generate `Q(c,tau)`. In a rational Betti basis, an imaginary quadratic tau has rational trace and norm, and `c=conjugate(tau)-tau` is a nonzero purely imaginary generator of K. Thus the entry field is exactly K. This field statement depends on keeping a rational Betti basis. An arbitrary algebraic change of Betti basis can enlarge or obscure the entry field.

The projector is not a rational endomorphism: K is a field and has no nontrivial idempotents. It is a K-linear combination of algebraic endomorphisms, i.e. an element of `K tensor_Q K` after the coefficient extension that splits the two eigenspaces.

## Intrinsic adjoint identification

Put `T=Sym^2 H tensor (det H)^(-1)`. An explicit coordinate-free convention for the canonical identification `T -> End_0(H)` is

`Phi(uv tensor delta^(-1))(x) = ((u wedge x)v + (v wedge x)u)/(2 delta)`.

Here the symmetric product is the ordinary polynomial product. With `delta=u wedge v`, this sends `uv/delta` to the projector onto v along u minus half the identity. In the polynomial basis `e1^2,e1 e2,e2^2`, it sends coordinates `(x,y,z)` to

`[[-y/2,x],[-z,y/2]]`.

This verifies every sign and the factor one-half in the manuscript. The intrinsic definition is preferable in the main text. The matrix and three-coordinate formulas belong in one compact appendix lemma.

## Local lifting

The local annihilator condition is valid. For non-CM E, `T` is the irreducible adjoint representation of GL2 and has no trivial subrepresentation. In the semisimple, multiplicity-free object `T direct-sum 1`, a subobject containing a vector with nonzero components in both summands must be the whole object. A nonzero Betti functional cannot vanish on that object. At CM, the completed tensor gives the required comparison-compatible line. Thus the local lifting property is equivalent to CM under the scalar identity, not an unconditional consequence of it.

A useful commutative diagram for the rewrite is the naturality square for `Phi`, with horizontal comparison isomorphisms and vertical maps to `End_0(H)`. A second diagram may display the inclusion of a proposed subobject into `T direct-sum 1` and its Betti inclusion into the kernel of the scalar functional. Mark the existence of that subobject as the added hypothesis; a diagram must not suggest it already follows from scalar vanishing.

## Second cycles and reality

The propagation polynomial is correct:

`q(m gamma1+n gamma2)/pi = alpha (m+n tau)^2 + 2 i b n(m+n tau)`.

With `n != 0` and `alpha != 0`, algebraicity of a second value makes tau algebraic, hence CM. In the real normalization `tau=r+i y`, the imaginary part is exactly

`2 n(m+n r)(alpha y+b)`.

The mixed-cycle restriction cannot be suppressed. Real and purely imaginary cycles give real values automatically. The converse at CM is correctly deduced from the opposite CM eigenspace, Legendre, and transcendence of `pi/omega^2`.

## Suggested elegant organization

1. Define the normalized symmetric tensor and its adjoint projector intrinsically.
2. State the source theorem as a full-faithfulness theorem for complete comparison data.
3. Prove the completion criterion by eigenspaces and full faithfulness; keep the determinant argument giving the one known coefficient.
4. Derive the exact coefficient field and the second-cycle criterion as corollaries.
5. Place formal matrix countermodels, Kummer-rank limitations, and the explicit coordinate identities in the scalar-obstruction appendix.

The `b=0` nilpotent observation is also correct: a completed nonzero nilpotent would belong to either the scalar algebra or the split CM algebra, neither of which has a nonzero nilpotent. It still does not rule out algebraicity of a single scalar coordinate.

## Review of the rewritten drafts

Reviewed the full exact drafts:

- `sections/comparison.tex`, SHA256 `29191A492A864CDD7198550A569E149F545F6C202E86791061E3A1E3F7603358`;
- `appendices/comparison_obstructions.tex`, SHA256 `7C5BA218BAD93259F6CCA9FD4A8D5D6963341C3279CD94F66BAB628B666E43E5`.

Mathematical verdict: PASS. No substantive proof defect or missing claim was found in these drafts. In particular:

- The coordinate-ring diagram is correct: the kernel of evaluation is the defining prime ideal of the actual Zariski closure, so the induced map from its coordinate ring to the complex numbers is injective. The restricted three-dimensional space gives exactly QPI at a non-CM fiber.
- The new intrinsic definition of Phi has the correct signs and factor one-half, and its displayed naturality square commutes. It maps the normalized symmetric tensor to the specified projector minus half the identity.
- The projector argument preserves the exact coefficient-field condition, the determinant orientation, and the distinction between completion and scalar evaluation. The rational Betti basis needed for the entry-field assertion is fixed by the opening integral basis and stated again in the appendix.
- The modular jet dictionary has been independently recomputed from the three Ramanujan differential equations. Both coefficients of R, the signs of Q and i alpha, the inverse formulas, and the finite field extension are correct.
- The hierarchy diagram follows from the stated finite extension and exact modular-field equality; no functional theorem is upgraded to a numerical specialization.
- The appendix correctly retains rational-direction exclusion, complete-tensor and scalar distinctions, mixed-cycle reality, the almost-holomorphic criterion, nilpotent and Hodge-type obstructions, and the scope of the KSV annihilator theorem.

Three local TeX defects must be repaired before compilation. Each is a missing backslash in `left(`, and each has a matching `\\right)`:

1. `sections/comparison.tex:130`, the forbidden-jet equation: `+left(` must become `+\\left(`.
2. `appendices/comparison_obstructions.tex:178`, the almost-holomorphic linear relation: `-left(` must become `-\\left(`.
3. `appendices/comparison_obstructions.tex:206`, the formula for kappa under the scalar relation: `+left(` must become `+\\left(`.

These are presentation/build defects only; they do not affect the mathematical verdict. No expansion of the caveats or return to repetitive coordinate calculations is needed.
