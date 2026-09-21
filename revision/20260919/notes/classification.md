# Classification rewrite — 19 September 2026

Owned output: `sections/classification.tex`. Original `paper.tex` and `hint_paper.tex` were read only.

## Design

The chapter follows the two intrinsic constructions: (i) the finite modular correspondence gives the degree of a singular modulus and integrality of the chosen coordinate; (ii) the isogeny-invariant complementary CM eigenline gives existence and rational descent of the slope. The computation is then a short, exact finite certificate between structural results. The expanded monic cubics/quartics, lists of 42 discriminants, and explicit Vélu formulae are unnecessary in the main proof.

Two diagrams are used for distinct reasons: the modular quotient diagram records why a quadratic correspondence replaces a descended elliptic j-map; the projectivized de Rham square proves Galois descent. The latter is over Qbar so that a differential multiplier need not lie in Q(x).

## Core dependencies

- Existing definitions: `s_ell`, `R_ell`, `F_s`, primitive means gcd(A,B)=1.
- `sec:families`: chosen models and their Gauss period equations.
- `eq:logderivative`: theta F/F = u + v h/omega, v nonzero.
- Period normalization F = 3 omega^2/(2 pi^2); Legendre relation omega_1 h_2 - omega_2 h_1 = 2 pi i with compatible orientation.
- `eq:general-cm-determinant` from `02_periods.tex` supplies the intrinsic determinant proof. The standard endomorphism proposition here now specializes that result rather than repeating its period-matrix proof.
- `thm:unconditional`: uniqueness, zero exclusion, positive-endpoint exclusion.
- `hyp:QPI`: its exact domain is preserved. The theorem does not use an integral-parameter hypothesis at rational nonintegral C before proving CM.
- Original table labels `tab:standard1` through `tab:standard4`, `tab:euler1` through `tab:euler4` must remain in the appendix.
- `app:cm-certificate` is requested for the appendix containing the arithmetic discriminants, certificate description, and standard/Euler tables.

## References incorporated into arguments

- Cox, Chapters 7 and 11: integrality of singular moduli, irreducible ring class polynomial of degree h(D) for arbitrary orders, and ring class reciprocity. Their exact conclusion enters the degree/integrality proof.
- Watkins: complete fundamental-discriminant bound |d| <= 427 for h(d) <= 2. Together with the written conductor formula and phi(f) >= sqrt(f/2), this proves f <= 72 and makes the arithmetic enumeration exhaustive.
- CCY Tables 5–11: exact singular coordinate and differentiated modular-equation slope for each row. These are openly retained external exact evaluations.
- CCL Theorem 2.1 / CCY Theorem 2.4: specified modular forms, G = 1 - RX, quadratic nomes, and strict convergence hypotheses yield the displayed radical multiplier formula.
- Bauer: separately supplies the boundary identity because the modular theorem requires the open disk.

## Certificate material for appendix

Keep the 13 + 29 discriminant lists, exact class polynomial coefficients, elimination factorizations, and the existing `verified/cm_summary.tex` or a less repetitive equivalent. Existing exact files are `problems/ramanujan-sato/verified/enumeration.json`, `cm_verified.sage`, and `enumeration-transcript.txt`. The transcript records interval-certified Arb class polynomials compared with PARI, reduced forms/conductor classification, integer roots/factors and gcd/resultants. No new computational certificate was created here.

The four factorized modular equations stay in the main text: each genuinely explains both degree and integrality. Their fully expanded form as polynomials in C belongs only in the archive if desired.

The original explicit degree-two and degree-three isogeny formulas are not needed in the main proof. Isogeny existence follows from the eta-coordinate identification with the two elliptic j-maps on X_0(n), and constancy of the multiplier follows from Wronskians. These coordinate formulas can be retained as independent appendix checks.

## Independent focused check

Agent `descent_review` checked the complementary-line descent and the Wronskian argument. It confirmed: geometric CM suffices; the two eigenlines are Galois permuted while the Hodge line is fixed; actual isogenies must be established before using Wronskians; x = 0, 1, 1/2 are excluded when using T_x; ordinary convergence is a separate assertion. Its proposed projective square has been incorporated.

The same agent then independently reviewed the complete 474-line section and returned PASS with no substantive defect. It checked both eta j-maps by substitution, monicity, both directions of enumeration, Galois descent, source-hypothesis scope, and all convergence qualifications. Its two editorial suggestions (unambiguous wording of the conditional qualification and an explicit certificate appendix reference) were incorporated.

## Scope

The existence theorem and its endomorphism specialization are intentionally stated for -1 <= z < 1, so no continued values are counted as standard identities. CM classification is unconditional; removing the CM premise uses QPI. Numerical table validation is not used as proof of a modular singular value. The coefficient line is denoted R_x to agree with the intrinsic identity-line theorem and avoid confusing it with the Hodge line.

General fixed-family arithmetic (original proposition `prop:arithmetic-correspondence-packet`) is better placed with the higher-level extension theorem: if P(t,j) has degree m in j, then h(D) <= [k:Q] m [k(t):k], and finite j-fibers plus bounded-class-number finiteness imply finite CM parameters. The present section isolates m=(1,2,2,1) and avoids repeating that general theorem.

Integration handoff: the section is 466 lines, preserves old classification/Euler labels, and uses the new general period determinant from 02_periods.tex. It requires an appendix label app:cm-certificate. No standard/Euler table inputs were embedded, because root is placing them in the appendix. No generic higher-level arithmetic theorem was duplicated. The final source hash before assembly is B0B67BB6FD28E41F73DE7A7584FB59B557A5AB1391622F5E83F83DDD907EA175.
