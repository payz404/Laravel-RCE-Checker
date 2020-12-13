from laravelrce.packages import *
from laravelrce.checker import *
from laravelrce.banner import *

os.system('clear')

console = Console()
welcome = Banners()
List = console.input("[blue][>>] Input your list.txt file: ")

app = LaravelRceCheck(List)
app.check()