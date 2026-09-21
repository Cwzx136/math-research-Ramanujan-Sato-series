# Final arithmetic and classification audit, 19 September 2026

Verdict: PASS. This is an AI-assisted mathematical review, not formal verification or independent human peer review.

## Read scope

Read the assembled `paper_revised.tex`, all six main-text sections, all ten thematic appendix files, the bibliography, and all three external table/certificate inputs. The closest line-by-line review covered classification, arithmetic realizations, integral arithmetic details, finite transformations, Lucas normalization, further CM branches, and compact CM degree bounds. The existing finite numerical certificates were reviewed through their mathematical certificate statements; this audit did not rerun the 1,918 lattice computations or the class-polynomial enumeration.

No source file was edited. The original source and PDF hashes still agree with the preserved 118-page manuscript.

## Main arithmetic conclusions

- The coefficient pair is primitive by gcd(A,B)=1. Ordinary convergence and the positive and negative boundary conventions remain intact.
- The four modular equations are monic in C and have degrees (1,2,2,1) in j. CM reciprocity therefore proves both integrality of rational CM parameters and the correct class-number bounds. The conductor bound and the finite enumeration are not presented as numerical evidence for an unrestricted cutoff.
- The de Rham complementary eigenline descends without requiring all CM endomorphisms to be defined over the ground field. The actual modular isogeny is established before the Wronskian argument proves the constancy of its differential multiplier. Its equivariance gives rational coefficient descent.
- The 36 standard and 35 linear Euler counts survive the rewrite. The Euler coefficient matrix, primitive normalization, and exclusion of both endpoints are correct. The external modular evaluations retain their strict-convergence premise, with Bauer treated separately.
- Finite Clausen is used as an unconditional polynomial congruence; its CM supercongruence consequence is kept separate. The Cartier statement includes the differential normalization, semilinearity, and all perfect residue fields. Supersingular zeros are not misidentified as stable Hodge complements.
- Tang's theorem is stated with its actual weighted limsup bad-place density, holomorphic uniformizations at every archimedean embedding, and maximum Nevanlinna order. The universal-extension leaf is dense for any abelian variety; the extension-class argument correctly proves this without a simplicity assumption. The order-two estimate yields the threshold 3/4 and no stronger one.
- Rational-prime transport includes every place above each admitted prime. The projective Q-curve argument proves density zero for non-CM supersingular rational primes, including inert/higher-residue-degree primes; the finite-image count and order of limits are valid.
- The one-prime theorem uses the linear iterate phi^f, allows ramification, and requires exact preservation of the characteristic-zero Hodge line. The graph-divisor, Lefschetz lifting, formal GAGA, and off-diagonal correspondence recover a nonscalar lifted endomorphism. The ordinary CM converse correctly uses the equality of the two imaginary-quadratic endomorphism fields after specialization.

## Primary sources rechecked

Read the archived primary text at Tang §§5.1.1–5.1.4, Theorem 5.1.5 and the proof of Proposition 2.3.4 (including footnote 20); Maulik–Poonen Theorems 4.21 and 4.24; and Gonzalez–Rotger Theorem 5.8 and Lemma 5.9. The rewritten statements preserve their operative hypotheses and conclusions. No source is used to infer the missing complex-scalar-to-Frobenius implication.

## Appendix arithmetic and scope

- The inverse-linear-square-root classification follows from the Frobenius quotient, geometric degree preservation, Kummer divisibility d|(p-1), the strict half-density threshold, and a divisor/degree budget. The multiplicity argument at z=1 retains the exceptional characteristic-p residue bound. The cubic gauge shows the claimed sharpness.
- The finite pullback transformations have the required nonnegative exponents and degrees less than p. For quadratic companions with transported z<-1, the arithmetic theorem applies at rational z outside {0,1}, while analytic values are evaluated by the explicitly identified continuation; only the original companion series is counted under ordinary convergence. This is correctly distinguished from a convergent standard series.
- The quadratic-companion divisor test, level-nine C|27 argument, Domb C|64 argument, and their additional independence hypotheses are correctly stated. No hypothesis restricted to the original integer standard denominators is silently enlarged.
- The higher-level correspondence bound includes the coordinate-map degree and finite-fiber hypotheses. The compact CM bound uses the field of the actual coarse point, optimal embeddings, and square-free level. No extra factor two or universal class-number-two claim is introduced.
- Local Frobenius eigenvalues, finite precision, transformed-gauge counterexamples, and formal comparison objects remain explicitly distinct from counterexamples to the original problem.
- The Padé independence is over Q, its conclusion excludes pairs only, and both WZ converses are limited to their precisely stated deformation/certificate families.

## Frozen hashes of the closest-reviewed inputs

| File | SHA256 |
|---|---|
| sections/arithmetic.tex | 0E8C2AFDBF35E1EEB399EF6B3D756AB57FF7620B8032291CD262D0949A76E015 |
| sections/classification.tex | B0B67BB6FD28E41F73DE7A7584FB59B557A5AB1391622F5E83F83DDD907EA175 |
| appendices/arithmetic_details.tex | 03A72124D8D3D2E4E7807785BE478E554DAF49C24127A07A072FAB238E11399E |
| appendices/truncations.tex | 561F5C861EA82F058F88470D795A5121F973EA0B7FB956A87414D1D6D707656F |
| appendices/extensions.tex | DD72185CE183B6DB49D2D0832C7464D8A4B32B66F65341AFCC9BB395CBD3033E |
| appendices/cm_certificates.tex | EFA37B0ECF343B2DE35E8398638F89561C95DE7D70746A5294E517E8D5D67953 |
| verified/standard_tables.tex | 92E16B712E430C506B0880E3EC58FB58CA6C6558545D4B90BA347FF298B62C6E |
| verified/euler_tables.tex | 20C5D5E01174E1331679567060567DCFF8FE9F626781C70AB5F921DAB21C72AD |
| verified/cm_summary.tex | E949E3ED5113A911A7E0359F908FE1DCC7B2DBC1B170F34EC44940ADC8802259 |

There are no outstanding mathematical corrections in this audit's scope. Unconditional CM forcing remains explicitly unresolved in the abstract, leading theorem, main conclusion, and relevant appendices.

Assembled root paper_revised.tex hash at completion: 0B2705403764955DE86ADEBD4B2016DDAE38D63D11736E21C897B4467234D479.

## Final delta confirmation, 20 September 2026

Verdict: PASS on the final manifest below. No required correction remains.

All 21 on-disk TeX inputs match `static-check.json`. Its SHA256 at this check is `4A7830C41BE6CCA6D58EE7A395D5C08590916DDD3DE249EBE4A1DAE7BDB257E6`.

The following changes were examined directly:

1. The master adds the nonfloating `identitytable` environment. Removing that block reconstructs the previously audited master hash exactly: `0B2705403764955DE86ADEBD4B2016DDAE38D63D11736E21C897B4467234D479`.
2. The CM appendix now inputs the revision-local table copies. Read the entire current appendix. For both tables, the mathematical body is identical to the verified original after replacing the environments and removing the standard-table clearpage; the sole remaining standard-table difference is whitespace. No coefficient, multiplier, label, or convergence description changed.
3. The period–jet proof now explicitly references both equations it proves. This corrects the citation wording and changes no formula or premise.
4. The local-slope proposition explicitly assumes `p>3` and `z in Z_p`. This makes its rational reduction-ring conclusion precise. Reversing exactly that sentence reconstructs the previously audited arithmetic-details hash `03A72124D8D3D2E4E7807785BE478E554DAF49C24127A07A072FAB238E11399E`.

The original `paper.tex`, `paper.pdf`, `hint_paper.tex`, and `hint_paper.pdf` still have their recorded preservation hashes. I did not compile or make a new layout-verification claim in this delta audit. The current revised PDF has SHA256 `1FC2092F8840E3960ACF146C43CD3D6F10648C14BA40DECEF01D883FD0148D92`.

Final complete input manifest (SHA256):
- paper_revised.tex: 6DB61F39088A9DA00BEEBC15C9C0F99907E1897EE23F8B5E29A92AA2B4EF7508
- revision\20260919\sections\introduction.tex: B6A0EDB12F9BEF92159CE45E67F31F4244C6652BF2163596DBC2C0C262362A5B
- revision\20260919\sections\02_periods.tex: A13A6E4819A5E38DFD31752BE0C0A537301C6827A876E2003638C3E5AE4B4642
- revision\20260919\sections\comparison.tex: 40CD6A4FD8BF43D70D9239E0C587450BBBC6EC1F31372922926C3D268F4EF4CF
- revision\20260919\sections\classification.tex: B0B67BB6FD28E41F73DE7A7584FB59B557A5AB1391622F5E83F83DDD907EA175
- revision\20260919\sections\arithmetic.tex: 0E8C2AFDBF35E1EEB399EF6B3D756AB57FF7620B8032291CD262D0949A76E015
- revision\20260919\sections\scarcity.tex: 0D2751E517F20FBCD28BAAF213F6B9550F7424B50AF156C1B67D7EB7C072B26D
- revision\20260919\appendices\period_models.tex: 5508AAE3A3EF0B040ECB5DFCD2C8479648BCADB6781D22CFCCB91221951A0921
- revision\20260919\appendices\cm_certificates.tex: 514126D42E9C8172DB07B6BB77249AE0C14DA528F83EC144601C5D879D6CADAD
- verified\cm_summary.tex: E949E3ED5113A911A7E0359F908FE1DCC7B2DBC1B170F34EC44940ADC8802259
- revision\20260919\standard_tables.tex: 365E0E9710B0ABD80A6763954A50AA4D2FAFA72F33008F938E9A07DDCFD78CCD
- revision\20260919\euler_tables.tex: F6FDDE37A103D94DE321B89D8AD813365CCE9357BA1CDD229A319E266D3E6B34
- revision\20260919\appendices\arithmetic_details.tex: 80E33ABBBB47D5CCC8A9DD6FEBDF7D7C7C18C0AA634C77EFA8FB15332DA64F6A
- revision\20260919\appendices\comparison_obstructions.tex: 35138237756E6E5D7B86E9D9EE5378171F52718F5F95933D7A1C2A62EE724B3F
- revision\20260919\appendices\analytic_refinements.tex: 3795DBC020C591B8E9082C0DBCEB3F4578837A36A24299713AC348AD96167F4D
- revision\20260919\appendices\scarcity_refinements.tex: 9FAB305E53B0A8C4C56B811E6C53B800C16A5573F7292716DEAC3AD3DA09C3F1
- revision\20260919\appendices\truncations.tex: 561F5C861EA82F058F88470D795A5121F973EA0B7FB956A87414D1D6D707656F
- revision\20260919\appendices\extensions.tex: DD72185CE183B6DB49D2D0832C7464D8A4B32B66F65341AFCC9BB395CBD3033E
- revision\20260919\appendices\pade_wz.tex: 5A785A59950D68CF4AEA35C166EB1295B52348538C27727C27A142E9BDD7F613
- revision\20260919\appendices\searches.tex: C33A705273BB83245AA52163E9F5F4639D581439984DDA0ADC21B901D8816EDC
- revision\20260919\bibliography.tex: 209FAD15D078EAA55AF5F4E8DC1EABDC296FE064D92AE1D739F18194BB73EE1C

