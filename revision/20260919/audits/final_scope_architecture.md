# Final adversarial audit: scope, architecture, and claims

Date: 19 September 2026.
Auditor: `r19_final_scope_audit`.

## Verdict

PASS for scope, manuscript architecture, and the preservation requirements. No required correction was found. This review is an AI adversarial audit; it is neither human peer review nor formal proof verification.

I read the full main text, all statements and scope qualifications in the supporting appendices, and the detailed arguments at the main/appendix interfaces. I did not independently replay the archived numerical certificates or every coefficient identity in the Padé/WZ appendices. Those claims retain their explicit certificate-family or finite-computation scope, and their separate mathematical audits remain necessary.

## User requirements

1. The first main theorem is the conditional classification, preceded by precise definitions and its explicit quadratic-period independence hypothesis.
2. The main text follows the approved structure: the classification problem; intrinsic period squares; comparison tensors; CM classification; arithmetic CM criteria; unconditional scarcity.
3. The conceptual proofs use the coefficient map into de Rham cohomology, the complementary CM eigenline, the determinant, equivariance and Galois descent, a norm of the multiplier relation, monodromy and geometric specialization. Coordinate models, exact tables, expanded auxiliary certificates, transformed families and failed converse mechanisms are in thematic appendices.
4. The diagrams express actual naturality, fiber-functor comparison, conjugate/Hodge exact sequences, maps of coefficient lines, and field inclusions. The two incomplete modular-correspondence diagrams are explicitly described as correspondences, with no nonexistent descending j-map asserted.
5. The document uses the amsart typography, title format, sectionwise equations, restraint, and formal tone of hint_paper.tex. It retains ZiXian Chang-Wang as the author, as requested.
6. The disclosure describes mathematical exploration, drafting, computation and AI review accurately. It explicitly distinguishes these reviews from independent human review and formal verification, and does not claim subsequent human validation.
7. The original paper.tex, paper.pdf, hint_paper.tex and hint_paper.pdf are unchanged; their independently recomputed SHA256 hashes equal original-hashes.json.

## Mathematical scope checks

- **Main conclusion.** The abstract, leading theorem, closing main-text paragraph, comparison section, and appendix conclusions agree: the 36 standard and 35 linear Euler classes are proved on the CM locus; exhaustion of unrestricted scalar identities remains conditional. No passage claims unconditional CM forcing.
- **Primitivity.** The revision consistently uses gcd(A,B)=1. It explicitly explains why triple-primitivity would change the problem and permit infinite multiples.
- **Convergence.** The standard branch always uses ordinary convergence. The positive endpoint is excluded separately, the Bauer negative endpoint is retained conditionally, and all linear Euler endpoint pairs diverge. Transformed families state and prove their own convergence domains.
- **Zero values.** The first-order standard theory excludes a nonzero pair giving zero. Higher polynomial weights exclude alpha=0 explicitly and exhibit Picard–Fuchs annihilators as the reason. Critical and vanishing-gauge examples are identified as transformed-family countermodels.
- **Comparison input.** Chudnovsky's known independence is kept separate from QPI. The numerical conjectures are named and stated with their exact hypotheses. Kreutz–Shen–Vial concerns complete comparison tensors; one scalar entry is never promoted to completeness. The two-cycle and projector criteria specify exactly the additional datum.
- **Arithmetic input.** The weighted-density theorem assumes a lower natural prime density strictly greater than 3/4; it does not derive this from a complex identity. The one-prime criterion requires exact Hodge preservation by crystalline Frobenius at good ordinary reduction; modulo-p complement stability and finite precision are expressly distinguished.
- **CM arithmetic.** The class-number bound is one at levels one/four and two at levels two/three. The conductor bound makes the finite scan rigorous. Rationality of the CM slope is proved before numerical identification through equivariance and descent. The scalar hypothesis is not silently extended to arbitrary rational C or to additional transformed fibers.
- **Scarcity.** Absolute-denominator separation bounds the degree of alpha squared, without a coefficient-height bound. It does not imply finiteness. The height-counting theorem controls full tuples, and the proof accounts for the at-most-two primitive representatives after normalization. The norm conjugates algebraic coefficients only, without claiming Galois conjugates of an analytic identity.
- **Further families.** Quadratic companions, Domb and level-nine identities are complete within the CM locus, with larger QPI domains expressly required for unconditional-looking exhaustion statements. Higher-level quotient degree is accounted for by the correspondence. The compact Shimura discussion requires the specified realization, target, optimal-embedding hypotheses and extra comparison assumption.
- **Finite searches.** Exact finite exclusions, heuristic higher-degree searches and the modular-jet candidate mechanism are clearly separated. No finite null result is treated as a proof for arbitrary coefficients or multipliers. No original-hypothesis counterexample is claimed.
- **Auxiliary certificate theorems.** The Padé result concerns two rationally proportional multipliers, and its independence is over Q. The WZ converses classify only the specified rational-certificate deformation families; no necessity of such a certificate for an arbitrary identity is inferred.
- **Lucas gauges.** The half-density theorem is explicitly about algebraic scalar gauges preserving canonical Lucas congruences. Its sharpness and finite-jet examples do not assert a new complex-to-Frobenius bridge.

## Citations and presentation

The key main proofs incorporate the hypotheses and conclusions actually used from Chudnovsky, Nesterenko, Kreutz–Shen–Vial, CM reciprocity, Watkins, the modular summation theorems, Tang, Maulik–Poonen, Bombieri–André in the cited form, and Habegger–Pila. Established results, named conjectures, recent preprints, and computational certificates are differentiated in the text. I checked consistency of those packets with their use in the rewrite; independent primary-source checks are recorded in the period/arithmetic/scarcity audits.

The residual expanded polynomial calculations are supporting certificate calculations in the appendices, rather than the organizing method of the main theory. This is consistent with the user's requested elegance while retaining checkable proof content.

The current MiKTeX log reports a 70-page revision. The build and visual checks are the responsibility of the assembling agent; this audit does not certify an unviewed PDF.

## Exact reviewed source manifest

The following hashes identify the reviewed snapshot. The analytic-refinement and truncation appendices include the latest minor edits observed during this audit.

| File | SHA256 |
|---|---|
| paper_revised.tex | 0B2705403764955DE86ADEBD4B2016DDAE38D63D11736E21C897B4467234D479 |
| sections/introduction.tex | B6A0EDB12F9BEF92159CE45E67F31F4244C6652BF2163596DBC2C0C262362A5B |
| sections/02_periods.tex | A13A6E4819A5E38DFD31752BE0C0A537301C6827A876E2003638C3E5AE4B4642 |
| sections/comparison.tex | 9E9B1EFF25F34DAFA05175AAF3498B635E6C2929839C23BA19A8E74839179070 |
| sections/classification.tex | B0B67BB6FD28E41F73DE7A7584FB59B557A5AB1391622F5E83F83DDD907EA175 |
| sections/arithmetic.tex | 0E8C2AFDBF35E1EEB399EF6B3D756AB57FF7620B8032291CD262D0949A76E015 |
| sections/scarcity.tex | 0D2751E517F20FBCD28BAAF213F6B9550F7424B50AF156C1B67D7EB7C072B26D |
| appendices/period_models.tex | 5508AAE3A3EF0B040ECB5DFCD2C8479648BCADB6781D22CFCCB91221951A0921 |
| appendices/cm_certificates.tex | EFA37B0ECF343B2DE35E8398638F89561C95DE7D70746A5294E517E8D5D67953 |
| appendices/arithmetic_details.tex | 03A72124D8D3D2E4E7807785BE478E554DAF49C24127A07A072FAB238E11399E |
| appendices/comparison_obstructions.tex | 35138237756E6E5D7B86E9D9EE5378171F52718F5F95933D7A1C2A62EE724B3F |
| appendices/analytic_refinements.tex | 3795DBC020C591B8E9082C0DBCEB3F4578837A36A24299713AC348AD96167F4D |
| appendices/scarcity_refinements.tex | 9FAB305E53B0A8C4C56B811E6C53B800C16A5573F7292716DEAC3AD3DA09C3F1 |
| appendices/truncations.tex | 561F5C861EA82F058F88470D795A5121F973EA0B7FB956A87414D1D6D707656F |
| appendices/extensions.tex | DD72185CE183B6DB49D2D0832C7464D8A4B32B66F65341AFCC9BB395CBD3033E |
| appendices/pade_wz.tex | 5A785A59950D68CF4AEA35C166EB1295B52348538C27727C27A142E9BDD7F613 |
| appendices/searches.tex | C33A705273BB83245AA52163E9F5F4639D581439984DDA0ADC21B901D8816EDC |
| bibliography.tex | 209FAD15D078EAA55AF5F4E8DC1EABDC296FE064D92AE1D739F18194BB73EE1C |
| verified/cm_summary.tex | E949E3ED5113A911A7E0359F908FE1DCC7B2DBC1B170F34EC44940ADC8802259 |
| verified/standard_tables.tex | 92E16B712E430C506B0880E3EC58FB58CA6C6558545D4B90BA347FF298B62C6E |
| verified/euler_tables.tex | 20C5D5E01174E1331679567060567DCFF8FE9F626781C70AB5F921DAB21C72AD |

Section and appendix paths are relative to revision/20260919; paper_revised.tex and verified paths are relative to the research root.

Original source: 4E84A62F276EB35F911CAFDE599869BB3BC5863F16F61E17302D8D5E4E7D8698.
Original PDF: CC21FC55AF09AF7F8D07D7ED84B2505446E514DD491282B223BDC8D9F002BED6.
Hint source: 2049594A9F9787757D5B39CA881C70A4FF11BA8A018B73FEAC36F142BA680894.
Hint PDF: 6E2EEEBB8E514C2243E74C343BBCA7E52B6A958C166E04DF551A1722244707F3.

## Final full-coverage and delta confirmation — 20 September 2026

**PASS on the final 68-page revision. No correction requested.** This addendum supersedes the earlier limited appendix-coverage qualification: I have now read all ten appendices in full, including the complete Padé determinant and growth proof, both unrestricted-degree rational WZ certificate proofs, the full Cartier extraction and projective Frobenius arguments, the complete one-point norm and polynomial-weight specialization arguments, the extension/convergence proofs, and every row of all eight identity tables. I also reread all thirteen diagrams in their surrounding arguments. I did not rerun the large archived computations; the distinction between their finite certificate conclusions and the structural theorems is maintained.

The full reading found no loss of a hypothesis, necessary proof step, or convergence qualification caused by moving material to appendices. In particular, the Padé determinant remains supported by the coalescence and beta-log integral proof, rather than a bare assertion; the WZ degree classifications retain their pole-endpoint arguments before coefficient comparison; the finite CM enumeration retains a proved stopping range and exact class-polynomial tests. The appendix references used by the central classification resolve to their intended material.

The final changes were checked directly:

- The master defines a nonfloating `identitytable` environment. The CM appendix now includes the two table copies under `revision/20260919`. Normalizing only `table[p]` to `identitytable`, the closing environment, whitespace and `clearpage` makes each new table file identical to its original verified counterpart. No row, caption, label, sign or multiplier changed.
- The period–jet proof explicitly cites both `eq:jet-first` and `eq:jet-second`; this accurately describes the same substitution already in the proof.
- The local-slope proposition explicitly assumes `p>3` and `z in Z_p`. These assumptions state the integral base and prime exclusions needed by its finite étale argument; they do not enlarge its conclusion.
- The original source, PDF and Hint source/PDF were rehashed and still match `original-hashes.json`.

All 21 source-file hashes were independently recomputed and match the final `revision/20260919/static-check.json`. That manifest has SHA256 **4A7830C41BE6CCA6D58EE7A395D5C08590916DDD3DE249EBE4A1DAE7BDB257E6**. It records 7,067 lines, no duplicate labels, no missing references or citations, and thirteen diagrams. The final master source hash is **6DB61F39088A9DA00BEEBC15C9C0F99907E1897EE23F8B5E29A92AA2B4EF7508**. These hashes supersede the earlier snapshot table for the changed files.

The final MiKTeX log reports 68 pages. This confirmation approves mathematical scope, complete-source coverage, preservation, and the final deltas; it does not substitute for the assembling agent's visual PDF inspection or for human peer review.
