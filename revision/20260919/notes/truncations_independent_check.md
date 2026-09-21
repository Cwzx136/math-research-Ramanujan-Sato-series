# Independent audit: Frobenius quotients and canonical normalization

Audited the rewritten `revision/20260919/appendices/truncations.tex` (the approximately 21.6 KB version dated 19 September), against its preceding approximately 33.4 KB version and relevant arithmetic and extension statements. This is a mathematical audit, not formal verification.

## Mathematical verdict

PASS, subject to the two notation clarifications below. I found no mathematical error in the rewritten arguments. The shortened proofs preserve the needed hypotheses and conclusions.

- Frobenius quotient transport is correct for normalized series over F_p, because r(t^p)=r(t)^p and g(t^p)=g(t)^p. The degree criterion converts the quotient to the raw truncation.
- The three polynomial transformations have nonnegative exponents at all primes p>3. Their degrees are less than p. The half-power gauge in the level-nine case is handled correctly.
- The arithmetic classification uses the raw-truncation transport, the nonzero jet determinant, the weighted-density CM criterion, and the CM slope dichotomy. The exceptional convergent endpoints C=K and C=16 have only B=0 and transform to the smooth CM point x=1/2. Their raw zero sets have density 1/2.
- The algebraic Lucas-gauge classification is sound. Regularity over Q gives absolute irreducibility and eventual degree preservation; Kummer theory gives d|(p-1); prime density greater than 1/2 forces d<=2. In degree two, zero trace at infinitely many primes yields g^2 rational. The Picard-Fuchs operator bounds zero multiplicities by two away from 1 and one at 1; polynomiality eliminates zeros of g^2, and the degree at infinity forces an inverse linear polynomial. The cubic gauge proves sharpness.
- The critical non-CM pullback, vanishing gauge, irrational-slope gauge and singular-source examples preserve the important scope caveats. None supplies a counterexample to the original four branches.
- The raw Euler boundary calculation and its density 1/2 conclusion are correct.
- The finite-jet density-zero construction is correct with N>=1. Its finite boundary coefficient is 2^(M+1-2N)3^(N-1), nonzero at p>3; the auxiliary Legendre curve has j=35152/9 and is non-CM. The claimed convergence and integral rescaling are preserved.
- The algebraic progression-gauge construction is valid, including nonrationality by the divisor at infinity and the degree budget for Lucas primes.

## Notation clarifications recommended before final integration

1. The standard Frobenius proposition currently calls u_l(n) "the coefficients in (eq:series)", but the revised introduction does not name u_l(n), and the summands there also contain A+Bn. Define explicitly `u_\ell(n)=R_\ell^n c_{s_\ell}(n)` at first use.
2. The finite-transformations proposition writes H_Domb and H_9, whereas the extension appendix calls both local generating functions H. Add a sentence that H_Domb and H_9 denote those two specified functions, and that T_{p,s} is the truncation of F_s. This avoids an unnecessary dependence on context.

These are notation repairs, not changes to the mathematics. No further computation or new assumption is needed.
