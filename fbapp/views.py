from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_content, OpenGraphImage 

@app.route('/')
@app.route('/index/')
def index():
	if 'img' in request.args:
		img = request.args['img']
		og_image = url_for('static', filename=img, _external=True)
		og_url = url_for('index', img=img, _external=True)

	else:
		og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
		og_url = url_for('index', _external=True)
	
	description = """Tu es un gagnant ..."""
	page_title = "Le test ultime"
	og_description = "Découvre qui tu es vraiment en faisant le test ultime !"

	return render_template('index.html',
							user_name='Julio',
							user_image=url_for('static', filename='img/profile.png'),
							description=description,
							blur=True,
							page_title=page_title,
							og_url=og_url,
							og_image=og_image,
							og_description=og_description)

@app.route('/result/')
def result():
	gender = request.args.get('gender')
	user_name = request.args.get('first_name')
	uid = request.args.get('id')
	profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
	description = find_content(gender).description
	img = OpenGraphImage(uid, user_name, description).location
	og_url = url_for('index', img=img, _external=True)

	return render_template('result.html',
                            user_name=user_name,
                            user_image=profile_pic,
                            description=description,
                            og_url=og_url)

if __name__ == "__main__":
    app.run()