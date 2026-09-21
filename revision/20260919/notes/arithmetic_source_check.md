# Arithmetic primary-source check for the elegant rewrite

Read-only scope: original `paper.tex`, approximately lines 5390–6427; Tang, arXiv:1510.01357v3, §§5.1.1–5.1.4, Theorem 5.1.5, proof of Proposition 2.3.4 and footnote 20, proof of Theorem 2.3.5; Maulik–Poonen, arXiv:0907.4781v3, Setup 1.6, Theorems 4.21 and 4.24, and formal GAGA discussion. The two source texts are archived under `problems/ramanujan-sato/attempts/sources/`.

## Verdict

The original arithmetic arguments preserve the hypotheses of these sources. No substantive defect was found in this assigned scope. Neither theorem supplies the unproved complex-period-to-prime-condition transfer.

## Tang: hypotheses that must survive compression

1. The variety is geometrically irreducible and quasi-projective over a number field; the distribution is an involutive subbundle; its formal leaf through a rational point is smooth and Zariski dense.
2. At every complex embedding the leaf germ is uniformized biholomorphically by a holomorphic map from the full space `C^d`; its finite Nevanlinna order is bounded by the common maximum rho.
3. Bad places are precisely those where the reduced distribution is not closed under the restricted **p-th** power of derivations. Their density is a **limsup**, weighted by `[K_v:Q_p] log(p)/(p-1)` and cut off by the rational residue characteristic p, not by Norm(v).
4. The conclusion is `N=d` or `1 <= N rho alpha_bad/(N-d)`. Thus `N=2g`, `d=g`, `rho<=2` yields lower stable-place density at most 3/4. No stronger threshold follows merely by citing this theorem.
5. The commutative-group exponential-map growth bound of order at most two comes from the proof of Proposition 2.3.4, footnote 20. Do not cite the abelian-product Lemma 5.2.8 as if it directly covered universal vector extensions.
6. The universal-vector-extension Lie algebra and restricted-power/crystalline-Frobenius identification is explicitly used in the proof of Theorem 2.3.5 and Lemma 5.2.6. Here one uses p-semilinear Frobenius modulo p, not its residue-degree iterate.
7. To transport natural rational-prime density, include **every** place above each admitted rational prime. The local-degree identity and partial summation then give the required lower weighted density. Finitely many denominators, bad reduction places, and ramified places may be removed.

The Hodge-complement leaf is Zariski dense for any abelian variety, with no simplicity assumption. If its closure is H and U=H intersect V, the complementary tangent projection makes H/U -> A^vee an isomorphism. A subgroup of a characteristic-zero vector group is connected, so there is no hidden finite kernel. It follows that the quotient extension G/U splits. Its class is the restriction of the universal isomorphism `V^* -> H^1(A^vee,O)` to `(V/U)^*`; hence U=V. This is already the clean intrinsic proof. It is enough to display the universal extension once and explain the restriction of its class; no coordinates are needed.

## Maulik–Poonen: exact one-prime criterion

Setup 1.6 allows any complete discretely valued characteristic-zero field with perfect characteristic-p residue field. In particular the local field may be ramified. Theorem 4.24 says exactly that a special-fiber line bundle has a tensor p-power lifting to the formal scheme if and only if its crystalline first Chern class, transported to de Rham cohomology, lies in Fil^1. Theorem 4.21 supplies the functorial comparison and its Chern-class compatibility. Formal GAGA algebraizes the formal lift on the projective abelian scheme.

For residue field `F_q`, `q=p^f`, use `Phi=varphi^f`. This is linear over `Frac W(F_q)` and therefore extends canonically to the possibly ramified local field. No chosen Frobenius lift on that field is required. The use of a linear iterate here is different from the p-semilinear operator required in the density theorem.

The original graph proof is sound. The graph is Cartier even for inseparable Frobenius because `(x,y) -> pi_q(x)-y` is smooth. Its mixed Kunneth class lies in Fil^1 precisely when the corresponding operator preserves the Hodge line; its two pure components already lie in Fil^1. Lifting a p-power of the line bundle lifts a nonzero p-power multiple of the endomorphism through the Picard functor. Ordinary Frobenius is nonscalar, since its slopes are 0 and 1. A lifted nonscalar endomorphism forces geometric CM.

In the converse, after finite extension the characteristic-zero CM endomorphism field specializes into the ordinary special-fiber endomorphism field. Both are imaginary quadratic, so specialization identifies them. A rational multiple of Frobenius therefore lifts and preserves the Hodge line. Vanishing of the induced map from the Hodge line to its quotient descends to the original local field.

## Recommended elegant formulation

Introduce the following lifting lemma, then make the one-prime theorem its immediate application:

> Let E over O_L be an elliptic scheme. A special-fiber rational endomorphism lifts to a rational generic-fiber endomorphism if its crystalline action preserves the generic-fiber Hodge line. The converse follows from functoriality.

Proof: use the Poincare bundle to associate a divisor class on `E_k x E_k` to the endomorphism. Polarization identifies its mixed Kunneth component with the endomorphism. The filtration condition is equivalent to preservation of the isotropic Hodge line. Apply the p-adic Lefschetz theorem, algebraize, and recover the endomorphism from the mixed component of the relative Picard homomorphism. This avoids displaying the graph's 2-by-2 block matrix without concealing why a lifted divisor yields a lifted endomorphism.

The key intrinsic identification is

`Fil^1(H tensor H) = F tensor H + H tensor F`,

so the obstruction is the projection to `(H/F) tensor (H/F)`. Under polarization this projection corresponds to `F -> H -> H/F`. A small commutative diagram with this projection and the Chern-class comparison diagram expresses all the needed linear algebra. Conventions can replace the endomorphism by its polarization adjoint; in dimension two the Hodge line is isotropic and either preserves it exactly when the other does.

If preferred, retain the graph argument but replace the explicit matrix by one sentence: the mixed component of the homomorphism associated to the lifted line bundle, under the product principal polarization, specializes to plus or minus the required p-power multiple of Frobenius. This is the most concise safe edit.

## Boundaries worth retaining explicitly

- At ordinary reduction, a Frobenius-stable complement is the conjugate-filtration image. The criterion in the one-prime theorem instead concerns the characteristic-zero **Hodge line** and exact vanishing.
- Supersingular weighted zeros must not be counted as stable complements.
- A congruence modulo p, however dense in primes, is not an exact p-adic projector condition.
- The original complex scalar identity has not been proved to imply either the weighted-prime condition or exact Hodge-line stability.
