# Final adversarial audit: intrinsic periods and comparison

Date: 19 September 2026.
Auditor: `r19_final_period_audit`.

## Verdict

PASS. No correction is requested in the reviewed period/comparison core. The rewrite preserves the original mathematical status: existence and uniqueness on the CM locus are unconditional, while unrestricted exhaustion still requires the stated quadratic-period independence hypothesis. It does not infer CM from a single complex scalar identity.

This is an AI adversarial review, not human peer review or formal verification. Arithmetic density and scarcity are only checked here for consistency with their use of the period core; their independent full proofs belong to the other final audits.

A minor optional editorial improvement is to replace `This proves \eqref{eq:jet-first}` in the period--jet proof by `This proves \eqref{eq:jet-first} and \eqref{eq:jet-second}`, since that substitution proves both formulas. The proof already contains all required algebra, so this is not a correctness defect or a condition of PASS.

## Exact reviewed files

All paths below are relative to the research root.

| File | SHA256 |
|---|---|
| `paper_revised.tex` | `0B2705403764955DE86ADEBD4B2016DDAE38D63D11736E21C897B4467234D479` |
| `revision/20260919/sections/introduction.tex` | `B6A0EDB12F9BEF92159CE45E67F31F4244C6652BF2163596DBC2C0C262362A5B` |
| `revision/20260919/sections/02_periods.tex` | `A13A6E4819A5E38DFD31752BE0C0A537301C6827A876E2003638C3E5AE4B4642` |
| `revision/20260919/sections/comparison.tex` | `9E9B1EFF25F34DAFA05175AAF3498B635E6C2929839C23BA19A8E74839179070` |
| `revision/20260919/appendices/period_models.tex` | `5508AAE3A3EF0B040ECB5DFCD2C8479648BCADB6781D22CFCCB91221951A0921` |
| `revision/20260919/appendices/comparison_obstructions.tex` | `35138237756E6E5D7B86E9D9EE5378171F52718F5F95933D7A1C2A62EE724B3F` |

I also checked the CM coefficient construction and rational-descent proof in the classification section for compatibility of the intrinsic maps, and checked the arithmetic/scarcity statements at their period-theory interfaces.

## Checks performed

1. **Normalization and intrinsic construction.** The determinant comparison square gives the same Legendre orientation used throughout. The coefficient map has determinant proportional to the nonzero Kodaira--Spencer coefficient; changing the holomorphic frame scales its output as claimed. The resulting first-jet pairing and the standard normalization `k=-6` agree.

2. **Exact transcendence input.** Chudnovsky gives algebraic independence of `h/omega` and `pi/omega`, not the stronger quadratic-period statement. I checked the archived Waldschmidt survey, Corollaries 31 and 32. The half-period derivation and the sign `h=-eta` are correct. The theorem transfers to an arbitrary algebraic complementary de Rham class and to an integral multiple of a primitive cycle.

3. **Unique identity line.** Evaluation on one nonzero cycle is injective on the algebraic de Rham space because `h/omega` is transcendental. Its inverse image of the one-dimensional Tate-period line therefore has dimension at most one. The CM determinant proof produces precisely the complementary eigenline; the rational-slope criterion and uniqueness up to simultaneous sign follow. No existence claim outside CM is hidden in this argument.

4. **CM period independence.** The formula `h=c omega+d pi/omega`, with `d` nonzero algebraic, makes `K(omega,pi)=K(h/omega,pi/omega)`. Thus the claimed algebraic independence follows exactly from Chudnovsky. This is used correctly at the positive endpoint, where the first-order parameter map itself is not admissible.

5. **Standard realizations and endpoints.** The de Rham connection, common nodal residue and Gauss equation produce the stated period normalization. The logarithmic discriminant formula gives the same first-derivative coefficients as the original. Ordinary convergence at the two endpoints is handled separately. The endpoint CM isogeny calculations produce `j=8000` and `j=54000` with the correct quotients.

6. **Value and nome independence.** The field identity `K(F,G)=K(R,S^2)` is correct. Nesterenko's full statement gives the nome enhancement through the exact modular formulas, including cases where `g2` or `g3` vanishes. Algebraic independence of these normalized ratios is never confused with independence of `pi,omega^2,omega h`.

7. **Modular two-jet.** I recomputed `j'=-9 i j(g3/g2)P` and `j''/j'=R(j)j'-iQ` from the Ramanujan equations. Their inverse, the forbidden-jet equation, and the claimed field equality have the correct factors and signs. The nonzero hypotheses remove the elliptic fixed points before division.

8. **Numerical conjectures.** The finite extension of period fields and the exact modular-field equality justify the implication diagram. The bounds from Fonseca and the one-point modular Schanuel conjecture are quoted as numerical conjectures. Eterovic's functional theorem is explicitly kept separate, with the correct reason it is vacuous over the j-closure at algebraic j-values.

9. **Complete tensors.** The adjoint isomorphism has the correct one-half normalization and sends the indicated symmetric tensor to the projector minus half the identity. Its diagram is natural. Kreutz--Shen--Vial applies to complete comparison data, with its coefficient-field restriction stated; a power of one elliptic curve satisfies that restriction. The coordinate ring diagram concerns evaluation on the actual numerical closure and does not identify it with the torsor without an added assertion.

10. **Projector and propagation criteria.** The projector has exactly one algebraic entry supplied by the scalar identity. Each other algebraic entry forces algebraicity of the period ratio, hence CM. The CM entry field is exactly the quadratic field in the fixed rational Betti basis. The second-cycle and mixed-cycle-reality formulas, including their nondegeneracy conditions, are correct. The case `b=0` remains an uncompleted nilpotent obstruction.

11. **Appendix restrictions.** The rational coefficient directions, local annihilator criterion, almost-holomorphic coordinate, and formal matrix countermodels retain their exact scope. The logarithm, 1-motive, and biextension arguments identify missing hypotheses; none is presented as a counterexample to the original identity problem. The pullback transport keeps its ramification and ordinary-convergence conditions. General bounded-degree finiteness includes the necessary nonisotriviality and finite-map assumptions.

12. **CM descent interface.** The companion eigenline descends even if individual CM endomorphisms do not. The Gauss Wronskian argument makes the isogeny's differential multiplier constant, and functoriality then identifies the projective coefficient maps. Galois descent at the quadratic parameter consequently gives the rational line required for the finite classification.

## Primary-source verification

The delegated independent checker `r19_final_period_audit/source_check` checked the rewritten claims directly against archived Waldschmidt, Fonseca, Eterovic and Kreutz--Shen--Vial texts and returned PASS. Its exact-hash report is `revision/20260919/audits/final_period_sources.md`.

I independently opened the Waldschmidt Corollaries 31--32, Fonseca Proposition 4.7 and Conjectures 4.5/4.8, Eterovic Conjecture 2.3 and Lemma 4.6/Proposition 4.7, and Kreutz--Shen--Vial Theorem 5.10, Corollary 5.11 and Theorem 5.13. These source statements support the hypotheses and conclusions attributed to them in the revision.

## Preservation and presentation

The original `paper.tex` and `paper.pdf` hashes still equal the frozen 118-page checkpoint:

- source: `4E84A62F276EB35F911CAFDE599869BB3BC5863F16F61E17302D8D5E4E7D8698`;
- PDF: `CC21FC55AF09AF7F8D07D7ED84B2505446E514DD491282B223BDC8D9F002BED6`.

The conditional theorem remains first. The main period proof now develops one construction through the Hodge line, Gauss--Manin connection and determinant rather than repeated coordinate elimination. The commutative diagrams express genuine naturality and field-comparison statements. Computations are concentrated in the supporting appendix. The requested author attribution and explicit AI disclosure are present.



## Full-revision extension and final delta — 20 September 2026

Final verdict: **PASS on the full assembled revision.** This extension supersedes the earlier limited-scope qualification. I have now read the complete actual input tree: the master, all six main sections, all ten thematic appendices, the bibliography, the CM certificate summary, and both complete table files. No further mathematical correction is requested.

The review concerns mathematical text, proof dependencies, source scope, and consistency of the assembled result. Existing exact finite computations were not rerun; I read their hypotheses, bounds, certificate descriptions, and implications. The separate final arithmetic and analytic audits supplement this review. No manuscript was edited by this auditor.

### Full coverage and conclusions

- **Leading statement and intrinsic periods:** conditional CM forcing remains explicitly conditional; gcd(A,B)=1, ordinary convergence, nonzero multiplier and unique projective slope are retained. The period and comparison checks recorded above apply unchanged except for the correctly completed two-equation reference.
- **Classification and identity tables:** the correspondence has degree (1,2,2,1) in the elliptic invariant; monicity gives integrality before enumeration. CM eigenline descent and the constant isogeny multiplier prove rationality of the slope. The class-number and conductor bounds justify the finite scan. All 36 standard and 35 Euler rows are present with the same coefficients and multipliers as the verified originals. Euler's boundary exclusion remains part of the proof.
- **Arithmetic main text and details:** the finite Clausen polynomial statement, Cartier normalization, Frobenius twists, and supersingular alternative are distinguished. The density argument retains all places above each rational prime, Tang's weighted bad-place upper density, and the order-two growth bound. The exact one-prime criterion uses phi^f and the graph-divisor lifting argument, not a finite-precision substitute. The common-tensor statement does not infer a common Galois eigenline from separate local eigenvalues.
- **Scarcity and its refinements:** product monodromy handles the one coincident-singularity configuration through unequal adjoint traces. Arithmetic norms descend only coefficients, without asserting Galois propagation of analytic values. Bombieri--Andre and BBU are used with their fixed coefficient fields and precise nontriviality conditions. Height-window counting duplicates the parameter so that the semialgebraic path must move in that parameter. Density zero, divergent gaps and finite height windows are not promoted to unrestricted finiteness.
- **Analytic refinements:** the cusp lattice argument retains the finite multiplier set or its quantitative rational substitute; the algebraic-curve theorem uses algebraicity over Qbar of the whole curve, not merely a real semialgebraic path. Contact differentiation is applied to the analytic branch, including at the negative endpoint. The fixed-isogeny argument uses the least-degree cyclic kernel and equivariant orbit injection.
- **Truncations and algebraic gauges:** the Frobenius-quotient diagram is the exact covariance identity. Its polynomial degree condition is imposed before identifying it with a raw truncation. The algebraic-gauge classification retains regularity of the function field, degree-preserving reduction, the Kummer divisibility d|(p-1), and the sharp strict half-density condition. The root-multiplicity and divisor arguments correctly replace long coefficient calculations. The finite-jet examples change the family or normalization and are not labeled original-hypothesis counterexamples.
- **Further families and compact systems:** each pullback states its branch, nondegeneracy and ordinary-convergence domain. Quadratic, Domb and level-nine lists remain unconditional within CM, with precisely enlarged period hypotheses for unrestricted exhaustion. The compact-monodromy obstruction excludes an elliptic-family realization, not isolated identities. The compact degree bound is tied to the stated canonical model and optimal-embedding hypotheses. Its rank-two genericity and weight statements preserve the distinction between pi/Omega_0^2 and 1/pi.
- **Pade and WZ:** the seven-value independence is over Q. The explicit exclusion concerns two rationally proportional multipliers, not one isolated identity. The determinant, norm and remainder estimates retain their nonvanishing hypotheses. Both rational-certificate classifications are complete within the displayed deformations; neither is claimed necessary for a bare scalar identity. Ordinary evaluation of the affine survivor uses integer-parameter telescoping and dominated convergence.
- **Finite exclusions and modular jets:** coefficient, degree and denominator bounds remain explicit. Exact certificate claims and numerical evidence are distinguished. The jet family has a potential original-hypothesis counterexample only if an additional algebraic constant gives an integral denominator; no such example is claimed. Its bounded-denominator exclusion and denominator-growth bound do not exclude every algebraic constant.
- **Diagrams:** the determinant square, intrinsic adjoint naturality, coefficient covariance, Cartier triangle, universal-extension tangent sequence, correspondence specialization, counting square, Frobenius-quotient covariance, and compact field inclusions are compatible with the definitions. The two modular-coordinate pictures are expressly correspondences and assert no missing descent arrow.
- **Bibliography and disclosure:** cited construction results do not supply converse assertions. The author line and explicit AI-assistance disclosure match the approved presentation. No human review or formal verification is implied.

### Exact final delta verification

1. The master now defines the nonfloating `identitytable` minipage environment. Its change concerns layout and table placement only.
2. Both revised table files were compared against `verified/standard_tables.tex` and `verified/euler_tables.tex` after removing only the table/identitytable environment wrappers, `clearpage`, and whitespace. The complete remaining mathematical and textual contents are identical in each comparison. No row, sign, number, radical, caption, or label changed.
3. The CM certificate appendix inputs the two revised table copies; the unchanged finite certificate summary remains `verified/cm_summary.tex`.
4. The comparison proof now explicitly says that substitution proves both `eq:jet-first` and `eq:jet-second`, resolving the optional editorial point in the first audit.
5. The local-slope proposition explicitly assumes `p>3` and `z in Z_p`, with z and 1-z units. This states exactly the base-ring and etaleness conditions used by its proof.
6. All 21 files in the final static-check source manifest have been hashed independently and each actual SHA256 equals its recorded value. The original 118-page source and PDF still match their preserved hashes above.

### Final source manifest

The complete set of reviewed sources is recorded below. All hash comparisons passed. Static-check reports 7,067 expanded source lines, 13 diagrams, no duplicate labels, no missing references, and no missing citations.

Manifest: `revision/20260919/static-check.json`; SHA256 `4A7830C41BE6CCA6D58EE7A395D5C08590916DDD3DE249EBE4A1DAE7BDB257E6`.

| Reviewed source | SHA256 |
|---|---|
| `paper_revised.tex` | `6DB61F39088A9DA00BEEBC15C9C0F99907E1897EE23F8B5E29A92AA2B4EF7508` |
| `revision\20260919\sections\introduction.tex` | `B6A0EDB12F9BEF92159CE45E67F31F4244C6652BF2163596DBC2C0C262362A5B` |
| `revision\20260919\sections\02_periods.tex` | `A13A6E4819A5E38DFD31752BE0C0A537301C6827A876E2003638C3E5AE4B4642` |
| `revision\20260919\sections\comparison.tex` | `40CD6A4FD8BF43D70D9239E0C587450BBBC6EC1F31372922926C3D268F4EF4CF` |
| `revision\20260919\sections\classification.tex` | `B0B67BB6FD28E41F73DE7A7584FB59B557A5AB1391622F5E83F83DDD907EA175` |
| `revision\20260919\sections\arithmetic.tex` | `0E8C2AFDBF35E1EEB399EF6B3D756AB57FF7620B8032291CD262D0949A76E015` |
| `revision\20260919\sections\scarcity.tex` | `0D2751E517F20FBCD28BAAF213F6B9550F7424B50AF156C1B67D7EB7C072B26D` |
| `revision\20260919\appendices\period_models.tex` | `5508AAE3A3EF0B040ECB5DFCD2C8479648BCADB6781D22CFCCB91221951A0921` |
| `revision\20260919\appendices\cm_certificates.tex` | `514126D42E9C8172DB07B6BB77249AE0C14DA528F83EC144601C5D879D6CADAD` |
| `verified\cm_summary.tex` | `E949E3ED5113A911A7E0359F908FE1DCC7B2DBC1B170F34EC44940ADC8802259` |
| `revision\20260919\standard_tables.tex` | `365E0E9710B0ABD80A6763954A50AA4D2FAFA72F33008F938E9A07DDCFD78CCD` |
| `revision\20260919\euler_tables.tex` | `F6FDDE37A103D94DE321B89D8AD813365CCE9357BA1CDD229A319E266D3E6B34` |
| `revision\20260919\appendices\arithmetic_details.tex` | `80E33ABBBB47D5CCC8A9DD6FEBDF7D7C7C18C0AA634C77EFA8FB15332DA64F6A` |
| `revision\20260919\appendices\comparison_obstructions.tex` | `35138237756E6E5D7B86E9D9EE5378171F52718F5F95933D7A1C2A62EE724B3F` |
| `revision\20260919\appendices\analytic_refinements.tex` | `3795DBC020C591B8E9082C0DBCEB3F4578837A36A24299713AC348AD96167F4D` |
| `revision\20260919\appendices\scarcity_refinements.tex` | `9FAB305E53B0A8C4C56B811E6C53B800C16A5573F7292716DEAC3AD3DA09C3F1` |
| `revision\20260919\appendices\truncations.tex` | `561F5C861EA82F058F88470D795A5121F973EA0B7FB956A87414D1D6D707656F` |
| `revision\20260919\appendices\extensions.tex` | `DD72185CE183B6DB49D2D0832C7464D8A4B32B66F65341AFCC9BB395CBD3033E` |
| `revision\20260919\appendices\pade_wz.tex` | `5A785A59950D68CF4AEA35C166EB1295B52348538C27727C27A142E9BDD7F613` |
| `revision\20260919\appendices\searches.tex` | `C33A705273BB83245AA52163E9F5F4639D581439984DDA0ADC21B901D8816EDC` |
| `revision\20260919\bibliography.tex` | `209FAD15D078EAA55AF5F4E8DC1EABDC296FE064D92AE1D739F18194BB73EE1C` |

