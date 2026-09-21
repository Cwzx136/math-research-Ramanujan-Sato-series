# Final source audit: periods and comparison

Date: 19 September 2026.

Verdict: PASS. I independently compared the primary-source statements used by the revised period and comparison proofs against the locally archived primary texts. No substantive source misquotation, normalization error, or unsupported strengthening was found.

## Files reviewed

- `sections/02_periods.tex`, SHA256 `A13A6E4819A5E38DFD31752BE0C0A537301C6827A876E2003638C3E5AE4B4642`.
- `sections/comparison.tex`, SHA256 `9E9B1EFF25F34DAFA05175AAF3498B635E6C2929839C23BA19A8E74839179070`.
- `appendices/comparison_obstructions.tex`, SHA256 `35138237756E6E5D7B86E9D9EE5378171F52718F5F95933D7A1C2A62EE724B3F`.
- `bibliography.tex`, SHA256 `209FAD15D078EAA55AF5F4E8DC1EABDC296FE064D92AE1D739F18194BB73EE1C`.

These paths are relative to `revision/20260919/`. The originals were read only.

## Primary-source findings

1. Waldschmidt's lecture notes, Theorem 6 and Corollary 4, and his 2008 survey, Theorem 30 and Corollary 31, state algebraic independence of eta/omega and pi/omega for an algebraic elliptic curve. The manuscript correctly uses h=-eta, transports the claim under an algebraic de Rham basis change, and handles nonprimitive cycles by algebraic rescaling. The two-torsion explanation exactly matches the source deduction and Legendre sign.

2. The CM independence consequence agrees with lecture Corollary 6 (which includes an algebraic discriminant factor) and survey Corollary 32. The manuscript's direct deduction via the opposite CM eigenline is valid and removes no hypothesis.

3. Waldschmidt Section 5 gives dimension six for the algebraic span of 1, the four period/quasi-period entries, and 2 pi i in the non-CM case. It therefore supports precisely the four-entry linear independence used by the almost-holomorphic argument. It does not support quadratic independence, and the revision never claims it does.

4. Fonseca Theorem 1.1 and Proposition 4.7 give the Nesterenko and lattice-formula inputs in the manuscript. Changing from the conventional quasi-period to h=-eta gives E2=-3 omega h/pi^2, with the displayed E4 and E6 coefficients. Independent substitution in the Ramanujan differential equations confirms the first and second modular-jet formulas, including both coefficients of R and the signs of iQ and i alpha.

5. Fonseca Conjectures 4.5 and 4.8 have exactly the stated non-CM bounds four and five. The manuscript's finite extension and exact modular-field equality justify the implications to quadratic-period independence. It does not claim the named conjectures are equivalent.

6. Eterovic Conjecture 2.3 gives the numerical derivative bound three per nonquadratic modular orbit. Lemma 4.6 and Proposition 4.7 separately support the explanation why functional Ax--Schanuel over the j-closed field contributes no positive bound at these algebraic j-values. The numerical/functional distinction remains explicit.

7. Kreutz--Shen--Vial Theorem 5.10 and Corollary 5.11 give full faithfulness and algebraicity of complete endomorphism tensors with algebraic coefficients. Theorem 5.13(ii) allows the full algebraic coefficient field for powers of one elliptic curve because there is at most one CM field. The complete-tensor theorem is not being misapplied to a single coordinate.

8. KSV Corollary 6.17 gives only torsor equality at Picard corank one and actual numerical Zariski-closure equality at corank zero. The manuscript states these distinctions correctly for Kummer surfaces of non-CM and CM elliptic squares.

## Proof compatibility

The intrinsic adjoint map carries the normalized symmetric tensor to the chosen projector minus half the identity. The determinant argument gives exactly one algebraic projector entry from the scalar identity. Any further entry gives algebraic tau, hence CM by Schneider; none is silently supplied. The source theorem gives an alternative complete-matrix argument, not a scalar-to-completion theorem.

No corrections requested. This is an AI-assisted source and proof check, not formal verification or independent human peer review.
