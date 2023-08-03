from my_app import app


@app.route('/')
@app.route('/module-1')
def module_one():
    return 'Module 1'
