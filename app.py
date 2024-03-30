from flask import Flask, render_template
import psutil
import flaskwebgui
app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return render_template('index.html')

@app.route('/api/cpu')
def api()  -> str:
    return str(psutil.cpu_percent(interval=0.1))

# created child class of flaskwebgui primary class in order to modify browser flags
# without the --inPrivate flag, edge creates popup informing user about profile sync status
class myFlaskUI(flaskwebgui.FlaskUI):
    def get_browser_command(self):
        flags = [
            self.browser_path,
            f"--user-data-dir={self.profile_dir}",
            "--new-window",
            "--no-first-run",
            # added this flag
            "--inPrivate"
        ]

        if self.width and self.height:
            flags.extend([f"--window-size={self.width},{self.height}"])
        elif self.fullscreen:
            flags.extend(["--start-maximized"])

        flags.extend([f"--app={self.url}"])

        return flags
if __name__ == '__main__':
    # To run in browser on port 5000:
    # app.run(debug=True)
    gui = myFlaskUI(app=app, server="flask", width=600, height=600)
    # print(gui.profile_dir)
    gui.run()
    