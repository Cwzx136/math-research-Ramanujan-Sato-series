from pathlib import Path
import re, collections, hashlib, json
root=Path(__file__).resolve().parents[2]
files=[]
def expand(path):
    files.append(path)
    text=path.read_text(encoding='utf-8')
    def inc(m):
        target=root/m.group(1)
        if not target.suffix: target=target.with_suffix('.tex')
        return expand(target)
    return re.sub(r'\\input\{([^}]+)\}',inc,text)
text=expand(root/'paper_revised.tex')
labels=re.findall(r'\\label\{([^}]+)\}',text)
refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',text)
bib=re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',text)
cites=[x.strip() for s in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',text) for x in s.split(',')]
old=(root/'paper.tex').read_text(encoding='utf-8')
oldlabels=set(re.findall(r'\\label\{([^}]+)\}',old))
result={
'files':len(files),'lines':len(text.splitlines()),
'duplicate_labels':[x for x,n in collections.Counter(labels).items() if n>1],
'missing_references':sorted(set(refs)-set(labels)),
'missing_citations':sorted(set(cites)-set(bib)),
'omitted_original_labels':sorted(oldlabels-set(labels)),
'diagrams':text.count('\\begin{tikzcd}'),
'original_source_hash':hashlib.sha256((root/'paper.tex').read_bytes()).hexdigest().upper(),
'original_pdf_hash':hashlib.sha256((root/'paper.pdf').read_bytes()).hexdigest().upper(),
'file_hashes':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in files}
}
(root/'tmp/rewrite-20260919/expanded.tex').write_text(text,encoding='utf-8')
(root/'revision/20260919/static-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='file_hashes'},indent=2))
