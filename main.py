import json
import random
from flask import Flask,render_template

app=Flask(__name__,template_folder='./templates')

with open('list-李志.json','r')as f:
	data=json.loads(f.read())

ar='李志'

##解析数据
al=[]
for a in data:
	al.append(a['al'])
al=list(set(al))
al_dic=[]
for n in data:
	al_dic.append({'name':n['al'],'cover':n['cover']})
temp=[]
for a in al_dic:
	if a not in temp:
		temp.append(a)
al_dic=temp

def get_al(name):
	global ar
	ls=[]
	for n in data:
		if name==n['al']:
			ls.append({'name':n['name'],'artist':ar,'url':n['url'],'cover':n['cover']})
		else:
			pass
	return ls

##下面是视图函数
@app.route('/')
def index():
	try:
		return render_template('index.html',data=al_dic,ar=ar)
	except:
		global al
		name=random.choice(al)
		return render_template('404.html',name=name),404

@app.route('/al/<string:name>')
def return_al(name):
	try:
		data=get_al(name)
		return render_template('res.html',name=name,data=data,ar=ar)
	except:
		global al
		name=random.choice(al)
		return render_template('404.html',name=name),404

@app.errorhandler(404)
def f2f(e):
	global al
	name=random.choice(al)
	return render_template('404.html',name=name),404