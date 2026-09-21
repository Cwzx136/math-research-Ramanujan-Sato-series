"""Assemble supporting material without modifying either original manuscript."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[2]
base = root / 'revision/20260919'
source = (root / 'paper.tex').read_text(encoding='utf-8')
lines = source.splitlines(keepends=True)

def block(first, last):
    return ''.join(lines[first-1:last])

def write(name, text):
    path = base / 'appendices' / name
    if path.exists():
        raise RuntimeError(f'Refusing to overwrite {path}')
    path.write_text(text, encoding='utf-8')

# Bibliography remains the audited primary-source list.
bib = source[source.index('\\begin{thebibliography}'):source.index('\\end{thebibliography}')+len('\\end{thebibliography}')]
(base / 'bibliography.tex').write_text(bib.replace('\\begin{thebibliography}{99}\\small','\\begin{thebibliography}{99}'), encoding='utf-8')

write('cm_certificates.tex', r'''\section{The finite CM certificate and the identity tables}
\label{app:cm-certificate}

The arithmetic theorem reduces enumeration to orders of class number at
most two. This appendix specifies the resulting finite certificate.
For an order of discriminant $D$, let $H_D$ be its monic ring class
polynomial. At levels two and three write
\[
 P_\ell(J,C)=J^2-T_\ell(C)J+N_\ell(C).
\]
If $h(D)=2$, irreducibility gives the particularly short test
\[
 P_\ell(J,C)=H_D(J)
 \quad\Longleftrightarrow\quad
 T_\ell(C)=\operatorname{Tr}(j_D),\quad
 N_\ell(C)=\operatorname{Nm}(j_D).
\]
Thus equality of two degree-two characteristic polynomials replaces
expanded resultant calculations. For $h(D)=1$, substitution of its
integer root gives the corresponding one-variable test. Exact
factorization, rather than a bound on the size of $C$, exhausts their
integer solutions.

The class-number lists, conductor verification, and defining
correspondences are stated in Section~\ref{sec:enumeration}.
The executed certificate uses Arb complex intervals to certify the
integer class-polynomial coefficients and independently compares them
with PARI. It checks the integer roots both by exact factorization and
by resultants. These computations certify the finite algebraic step;
the period and modular arguments prove the evaluations.

''' + block(4195,4195) + r'''
\subsection{Standard classes}
The nome and its parameter $N$ use the convention in
\eqref{eq:alpha}. We choose $B>0$. Every row is ordinarily convergent;
the row $C=-64$ at level four is conditional, and all other rows are
absolutely convergent.

\input{verified/standard_tables.tex}

\subsection{Linear Euler companions}
The coefficient transport of Theorem~\ref{thm:euler} gives the following
primitive representatives and signed multipliers. Its boundary argument
is necessary: it is the reason that 36 standard classes give 35
ordinary Euler classes.

\input{verified/euler_tables.tex}
''')

write('analytic_refinements.tex', r'''\section{Analytic refinements of the scalar relation}
\label{rev:analytic-refinements}

The preceding theorems isolate the coefficient line at an algebraic
fiber. The following refinements control its behavior near the cusp,
along algebraic curves, and under differentiation. None introduces a
second comparison period.

''' + block(1987,2280) + block(3740,3956))

write('scarcity_refinements.tex', r'''\section{Specialization beyond a first-order weight}
\label{rev:scarcity-refinements}

The main separation theorem exploits cancellation of the common Tate
period at two parameters. A complementary argument works at one
parameter by taking a field norm of the period relation. Its value is
the uniformity in arbitrary polynomial weights: their derivatives
remain in one symmetric-square differential module.

''' + block(2283,2488) + block(2757,2852) + block(3206,3501))

write('truncations.tex', block(6428,7249).replace(
    '\\section{Finite Frobenius transformations for additional families}',
    '\\section{Truncation transport and canonical normalization}\n\\label{rev:truncations}'))

write('pade_wz.tex', r'''\section{Two certificate mechanisms}
\label{rev:certificate-mechanisms}

The two constructions below impose arithmetic restrictions through
explicit auxiliary identities. Pad\'e approximation separates two
rationally related values; rational telescoping classifies identities
within two fixed deformation families. Neither construction is known
to be necessary for an arbitrary standard identity.

''' + block(2853,3205) + block(8167,8493))

write('searches.tex', block(7848,8166).replace(
    '\\section{Certified exclusions and a targeted counterexample family}',
    '\\section{Finite exclusions and a modular-jet family}'))

print('Created six thematic appendices, the finite certificate, and bibliography.')
