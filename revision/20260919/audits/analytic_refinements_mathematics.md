# Audit of analytic refinements (19 September 2026)

Scope: `revision/20260919/appendices/analytic_refinements.tex`, read in full; dependency `sections/02_periods.tex`, especially value and nome independence.

Verdict: PASS on mathematical content. No substantive correction is required.

Checks performed:

- The cusp and polynomial-avoidance arguments use a fixed rational lattice and transcendence of pi. The first is exactly the P=0 case of the second. Northcott is used only with bounded degree and absolute height, and no unproved multiplier bound is inferred.
- The growing-height proposition uses the strict inequality 7.104 gamma + nu < 1 correctly. In the m=0 case the necessary weaker inequality gamma+nu<1 follows. In the m nonzero case the reduced approximation denominator is bounded by |m|q, and the identity bounds this by a constant times H(alpha). There is no hidden coefficient-height bound.
- Algebraic-curve finiteness holds for arbitrary real identity points as stated. Compactification gives a limit over [-1,1]. At z=1 the Gauss exponent difference is 1/2, so a finite cover removes local branching and leaves a meromorphic residual. Continuation of the identity through the slit plane reaches a branch over zero. Algebraic Laurent-Puiseux coefficients and the transcendence of pi force the homogeneous functional relation, excluded by the logarithmic singularity of the zero-balanced Gauss function. The Zariski-density example has primitive pairs and its exponential-polynomial argument is valid.
- The Riccati system is algebraically correct. Fixed-slope transversality follows from the homogeneous quadratic relation and independence of F,G. Nome/derivative independence follows from equality of the indicated rational function fields and a nonconstant rational function of r. The varying-germ contact criterion has all derivative terms, and its stated exceptional constant is correct.
- In a non-CM isogeny class, a least-degree isogeny has cyclic kernel. The injection from cyclic subgroups of a fixed order to quotient j-invariants is correct because Hom^0 has dimension one and equal degrees force the rational scalar to be plus or minus one. The Galois orbit lower bound and the consequence N <= I_E d are correct. The CM conductor bound h(f^2 D_K) >= h(D_K) phi(f)/3 is valid, including the exceptional unit groups.

Editorial recommendations, not mathematical defects:

1. Consolidate the cusp proposition into polynomial avoidance (or state it as its immediate corollary), instead of repeating the lattice argument.
2. The comment that level-four j=(C-16)^3/C is nonintegral for C>4096 can be justified in one short phrase: its remainder on division by C is -4096/C.
3. A finite-set quotient diagram can make the Galois-orbit proof more conceptual, but is optional; avoid decorative diagrams that do not encode an actual map.

No original manuscript or appendix source has been edited by this audit.

Audited source SHA256: FDC9D83023AA7F946E1E49E92B942DFD04549B272226EB7C7293F9F0DDBA15FF.
