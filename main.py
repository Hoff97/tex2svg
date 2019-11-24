import base64
import io
import os
import uuid
import xml.etree.ElementTree as ET

from flask import Flask, Response, abort, escape, request

app = Flask(__name__)

template_file = open("template.texfile", "r")
template = template_file.read()
template_file.close()

@app.route('/')
def get_svg():
    latex = request.args.get('latex')
    if latex == None:
        latex = request.args.get('latexB64')
        latex = base64.b64decode(latex).decode("utf-8")
    if latex == None:
        return abort(400)

    req_id = uuid.uuid4()
    svg = gen_svg(latex, req_id)

    scale = request.args.get('scale')
    if scale != None:
        scale = float(scale)

        svg_f = io.StringIO(svg)
        root = ET.parse(svg_f).getroot()

        width = float(root.get('width').replace('pt', ''))
        height = float(root.get('height').replace('pt', ''))

        root.set('width', str(width*scale) + 'pt')
        root.set('height', str(height*scale) + 'pt')

        svg = ET.tostring(root, encoding='utf8', method='xml')

    return Response(svg, mimetype='image/svg+xml')

def gen_svg(latex, req_id):
    print(req_id)
    os.system('mkdir -p res')

    texcontent = template.replace('{{{cmd}}}', latex)

    f = open(f"res/{req_id}.tex", "w+")
    f.write(texcontent)
    f.close()

    os.system(f'cd res && latexmk {req_id}.tex -pdfps')
    os.system(f'rm res/{req_id}.tex')
    cleanup_tex('res', req_id)
    os.system(f'pdfcrop res/{req_id}.pdf')
    os.system(f'rm res/{req_id}.pdf')
    os.system(f'pdf2svg res/{req_id}-crop.pdf res/{req_id}.svg')
    os.system(f'rm res/{req_id}-crop.pdf')

    svg_file = open(f"res/{req_id}.svg", "r")
    svg = svg_file.read()
    svg_file.close()

    os.system(f'rm res/{req_id}.svg')

    return svg

def cleanup_tex(folder, name):
    os.system(f'rm {folder}/{name}.aux')
    os.system(f'rm {folder}/{name}.dvi')
    os.system(f'rm {folder}/{name}.fdb_latexmk')
    os.system(f'rm {folder}/{name}.fls')
    os.system(f'rm {folder}/{name}.log')
    os.system(f'rm {folder}/{name}.ps')
