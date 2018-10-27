import sys
import os

CODE = 'ansi'

def latex_encoding(s):
    out = s.replace('à', '\\`a')
    out = out.replace('é', "\\'e")
    out = out.replace('è', '\\`e')
    out = out.replace('ê', '\\^e')
    out = out.replace('ë', '\\"e')
    out = out.replace('ï', '\\"i')
    out = out.replace('î', '\\^i')
    out = out.replace('ô', '\\^o')
    out = out.replace('û', '\\^u')
    out = out.replace('ù', '\\`u')
    out = out.replace('ü', '\\"u')
    out = out.replace('ç', '\\c{c}')
    return out
    
	
class LatexGenerator(object):

    def __init__(self, text_file, author='Alexis Roche'):
	
        self.name = os.path.splitext(text_file)[0] + '.tex'
        
        f = open(text_file)
        self._text = [l.encode(CODE).decode() for l in f.readlines()]		
        text = [latex_encoding(l) for l in self._text]
        f.close()
        title = text[0].replace('\n','')
        self.preamble = [
            '\\documentclass{article}\n', 
	    '\\usepackage{fullpage}\n', 
            '\\usepackage{amsmath,amssymb}\n',
            '\\title{%s}\n' % title,
            '\\author{%s}\n' % author,
            '\\begin{document}\n',
            '\\maketitle\n']
        self.end = ['\n', '\\end{document}\n']
        self.text = text[1:]
        self.find_sections()
		
    def find_sections(self):
        out = []
        sec, sub = False, False		
        for l in self.text:
            if '***' in l:
                print('section')
                sec = True 
            elif '---' in l:
                print('subsection')
                sub = True
            else:
                ls = l.strip()
                if ls != '':
                    if sec:
                        out.append('\\section{%s}\n' % ls)
                        sec = False
                    elif sub:
                        out.append('\\subsection{%s}\n' % ls)
                        sub = False
                    else:
                        out.append(l.replace('\n', ' '))
                else:
                    out.append('\n\n')
        self.text = out

    def save(self):
        f = open(self.name, 'w')
        f.writelines(self.preamble + self.text + self.end)
        f.close()
	    

g = LatexGenerator(sys.argv[1])
g.save()

