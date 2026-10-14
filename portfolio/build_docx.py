import re
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn

doc=Document()
st=doc.styles['Normal']; st.font.name='Arial'; st.font.size=Pt(12)
st.element.rPr.rFonts.set(qn('w:eastAsia'),'Arial')
st.paragraph_format.line_spacing=1.5
for n in ['Heading 1','Heading 2','Title']:
    s=doc.styles[n]; s.font.name='Arial'; s.font.size=Pt(12 if n!='Heading 1' else 14); s.font.bold=True
    s.font.color.rgb=None; s.element.rPr.rFonts.set(qn('w:asciiTheme'),'') if False else None
    s.paragraph_format.line_spacing=1.5


from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
def add_link(p,url):
    rid=p.part.relate_to(url,RT.HYPERLINK,is_external=True)
    h=OxmlElement('w:hyperlink'); h.set(qn('r:id'),rid)
    r=OxmlElement('w:r'); rpr=OxmlElement('w:rPr')
    f=OxmlElement('w:rFonts'); f.set(qn('w:ascii'),'Arial'); f.set(qn('w:hAnsi'),'Arial'); rpr.append(f)
    c=OxmlElement('w:color'); c.set(qn('w:val'),'0563C1'); rpr.append(c)
    u=OxmlElement('w:u'); u.set(qn('w:val'),'single'); rpr.append(u)
    sz=OxmlElement('w:sz'); sz.set(qn('w:val'),'24'); rpr.append(sz)
    r.append(rpr); tx=OxmlElement('w:t'); tx.text=url; r.append(tx); h.append(r); p._p.append(h)
def runs(p,text):
    for part in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*|https?://[^\s)]+[^\s).,;])',text):
        if not part: continue
        if part.startswith('http'): add_link(p,part); continue
        if part.startswith('**'): r=p.add_run(part[2:-2]); r.bold=True
        elif part.startswith('*'): r=p.add_run(part[1:-1]); r.italic=True
        else: r=p.add_run(part)
        r.font.name='Arial'; r.font.size=Pt(12)

doc.add_paragraph('Professional Portfolio',style='Title')
for l in ['Name: Apsara Sunuwar','Role: [YOU SUPPLY: programme / role]','Date: [YOU SUPPLY: submission date]','Title: Building the conditions for independent judgement: identity, an AI-supported placement case, and a career plan']:
    runs(doc.add_paragraph(),l)

def add_md(path):
    lines=open(path).read().split('\n'); i=0
    while i<len(lines):
        l=lines[i]
        if l.startswith('# '): doc.add_heading(l[2:],1)
        elif l.startswith('## '): doc.add_heading(l[3:],2)
        elif l.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                if not re.match(r'\|[-| ]+\|$',lines[i]): rows.append([c.strip() for c in lines[i].strip('|').split('|')])
                i+=1
            t=doc.add_table(rows=len(rows),cols=len(rows[0])); t.style='Table Grid'
            for r,row in enumerate(rows):
                for c,cell in enumerate(row):
                    p=t.cell(r,c).paragraphs[0]; runs(p,('**%s**'%cell) if r==0 and not cell.startswith('**') else cell)
            continue
        elif l.strip(): runs(doc.add_paragraph(),l)
        i+=1
for f in ['section1.md','section2.md','section3.md']: add_md(f)
doc.add_heading('References',1)
for l in open('references.md').read().split('\n')[1:]:
    if l.strip():
        p=doc.add_paragraph(); runs(p,l)
doc.save('Professional Portfolio.docx')
