#!/usr/bin/python3
# starts a webflask app

@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
