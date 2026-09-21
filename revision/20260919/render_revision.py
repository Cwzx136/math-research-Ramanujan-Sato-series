from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess, json, re
from PIL import Image, ImageOps, ImageDraw
import pdfplumber
root=Path(__file__).resolve().parents[2]
out=root/'tmp/rewrite-20260919'
pdf=root/'paper_revised.pdf'
poppler=Path(r'C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
reader=pdfplumber.open(pdf)
n=len(reader.pages)
def render(p):
    prefix=out/f'review-{p:03d}'
    subprocess.run([str(poppler),'-f',str(p),'-l',str(p),'-r','65','-singlefile','-png',str(pdf),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=4) as pool:
    list(pool.map(render,range(1,n+1)))
sheet_paths=[]
for start in range(1,n+1,12):
    canvas=Image.new('RGB',(1360,1940),'#d9d9d9')
    draw=ImageDraw.Draw(canvas)
    for j,p in enumerate(range(start,min(start+12,n+1))):
        im=Image.open(out/f'review-{p:03d}.png').convert('RGB')
        im.thumbnail((430,605))
        x=(j%3)*450+(450-im.width)//2
        y=(j//3)*480+23
        # Use the whole page at a common 420px height to fit four rows.
        im=ImageOps.contain(im,(435,445))
        x=(j%3)*450+(450-im.width)//2
        canvas.paste(im,(x,y))
        draw.text(((j%3)*450+12,(j//3)*480+7),str(p),fill='black')
    target=out/f'contact-{start:03d}.png'
    canvas.save(target)
    sheet_paths.append(str(target))
texts=[p.extract_text() or '' for p in reader.pages]
appendix_page=next((i+1 for i,t in enumerate(texts) if 'Models and ancillary period consequences' in t and i>2),None)
log=(root/'paper_revised.log').read_text(encoding='utf-8',errors='replace')
result={'pages':n,'appendix_starts':appendix_page,'contact_sheets':sheet_paths,'warnings':re.findall(r'^.*(?:Warning|Overfull|Underfull).*$' ,log,re.M)}
(out/'pdf-qa.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
(out/'pdf-text.txt').write_text('\n\n'.join(f'PAGE {i+1}\n{t}' for i,t in enumerate(texts)),encoding='utf-8')
print(json.dumps(result,indent=2))
