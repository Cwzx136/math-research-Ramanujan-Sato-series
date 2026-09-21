from pathlib import Path
p=Path(__file__).parent/'appendices/scarcity_refinements.tex'
s=p.read_text(encoding='utf-8')
a=s.index('The absence of a pointwise CM-forcing theorem')
b=s.index('\\begin{theorem}[Baldi',a)
s=s[:a]+r'''We use the following fixed-field relation theorem from the preprint
\cite[Theorem~4.2(3)]{BaldiBinyaminiUrbanik2026}. Its uniformity concerns
the degree of a relation, not the heights of its coefficients.

'''+s[b:]
a=s.index('This is a rank-two $G$-operator')
b=s.index('Choose a fundamental matrix',a)
s=s[:a]+r'''It is a rank-two $G$-operator: the rational hypergeometric germ is a
$G$-function, its minimal equation has rank two by
Lemma~\ref{rev:lem:product-monodromy}, and factors of $G$-operators
remain $G$-operators \cite[Theorem~3.5]{BaldiBinyaminiUrbanik2026}.

'''+s[b:]
a=s.index('Local monodromy at zero',s.index('We first prove'))
b=s.index('For completeness, this last assertion',a)
s=s[:a]+r'''The connected monodromy is $\operatorname{SL}_2$ by
Lemma~\ref{rev:lem:product-monodromy}.

'''+s[b:]
a=s.index('Let $m(T)=')
b=s.index('has rational coefficients',a)
s=s[:a]+r'''Let $L=\Q(\alpha^2)$, with $e=[L:\Q]\le d$. Descent to the fixed
coefficient field is the norm
\begin{equation}\label{eq:C-rational-norm}
 Q_C(X)=\operatorname{Nm}_{L/\Q}\bigl(U_C(X)^2-\alpha^2V_C(X)\bigr).
\end{equation}
This polynomial
'''+s[b:]
s=s.replace('% Insert after the bounded-degree gap results, before polynomial weights.\n% Bibliography key DHK2022; exact entry is in 20260918C_pade_repair_bib.tex.\n','')
s=s.replace('The monodromy argument\nbelow also verifies that its annihilator cannot have rank one.\n','')
p.write_text(s,encoding='utf-8')
print('Consolidated the monodromy proof and replaced coefficient expansion by a field norm.')
