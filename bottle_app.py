from bottle import static_file, route, run, default_app, debug, request

# Global variables
input_series = ['Breaking Bad','Peaky Blinders','True Detective']
ratings = [0,0,0]
rating_number = [0,0,0]
rating=[0,0,0]

def htmlify(season, title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="UTF-8" />
                      <link rel="stylesheet" href="/static/stylesheet.css" />
                      <link rel="shortcut icon" href="/static/icon.ico" />
                  </head>
                  <body class= " """+season+""" ">
                      """ + content + """
                  </body>
              </html>"""
    return page

def website_index():
    content = """
              <div class="homepagebox">
              <p><span><a class="global_link" href="/assignment1/">Click for my assignment 1.</a></span></p>
              <p><span><a class="global_link" href="/assignment2/a2_output.html">Click for my assignment 2.</a></span></p>
              <p><span><a class="global_link" href="/assignment3/">Click for my assignment 3.</a></span></p>
              </div>
              """
    return htmlify('page','Uğurcan Polat | Homepage',content)

def a3_index():
    content= """
    <h1 class="a3_hellobox">Hello, Serie Lover!</h1> <br>
    <div class="a3_inputbox">
    <form action="/series/" method='POST'>
        <p> Your Name: <input type="text" name="name" placeholder="Type your name..." /> </p>
        <p> How many series did you watch?: <input type="number" name="number" placeholder="0"/> </p>
        <input type="submit" value="Continue" />
    </form></div> """
    return htmlify('page',"Homepage",content)

def get_serie():
    name = request.POST.get('name')
    n_serie = request.POST.get('number')
    content ='<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content= content + """
    <div class="get_serie">
    <p>Hi, <strong>""" + name + """</strong>. You watched <strong>""" + n_serie + """</strong> serie(s).</p>
    <p>If you want to discover more, select a serie to discover:</p>
    <form action="/serie_page" method='POST'>
        <select name="series">
            <option value="brb" selected>Breaking Bad</option> 
            <option value="pb">Peaky Blinders</option>
            <option value="td">True Detective</option>
        </select>
        <input type="submit" value="Show me!" />
    </form><br></div><br>
    <div class="show_rating"><span><a href="/rating" class="global_link">SHOW RATING OF SERIES</a></span></div>"""
    return htmlify('page',"Series",content)

def serie_controller(): #controller
    serie = request.POST.get('series')
    if serie == 'brb' :
        return breaking_bad_page()
    elif serie == 'pb' :
        return peaky_blinders_page()
    elif serie == 'td' :
        return true_detective_page()

def breaking_bad_page(): #Breaking Bad page
    content ='<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content = content + """
    <h1 class="brb_headbox" style="color:white">Breaking Bad</h1> <br>
    <div class="brb_imagebox">
    <img class="brb_imgborder" src="/static/brb_index.jpeg" alt="Breaking Bad" style="margin-top:10px; height:350px; width:640px" />
    </div>
    <br>
    <div class="brb_checkbox">
        <form action="/brb_season" method='POST'>
            <input type="checkbox" name="seasons" value="Season1" /> Season 1<br>
            <input type="checkbox" name="seasons" value="Season2" /> Season 2<br>
            <input type="checkbox" name="seasons" value="Season3" /> Season 3<br>
            <input type="checkbox" name="seasons" value="Season4" /> Season 4<br>
            <input type="checkbox" name="seasons" value="Season5" /> Season 5<br>
            <input type="submit" value="Show!" />   
        </form> </div> <br>
        
        <div class="rate_inseries_brb">
        <img src="/static/star.png" alt="Star" style="height:10%; width:5%" /><br>
        Rate Breaking Bad
        <form action="/rating" method='POST'>
            <p><input name="series" value="Breaking Bad" readonly/></p>
            <input type="radio" name="rate" value="1" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />1 
            <input type="radio" name="rate" value="2" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />2
            <input type="radio" name="rate" value="3" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />3
            <input type="radio" name="rate" value="4" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />4
            <input type="radio" name="rate" value="5" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />5
            <input type="submit" value="Rate!" />
        </form></div><br>
        
    <div class="brb_serie_selector">
    <p>To check out another serie select from below:</p>
    <form action="/serie_page" method='POST'>
        <input type="radio" name="series" value="pb" /> Peaky Blinders <br>
        <input type="radio" name="series" value="td" /> True Detective <br>
        <input type="submit" value="Go!" />
    </form></div>
    """
    return htmlify("brb", "Breaking Bad", content)

def brb_season(): #Seasons of Breaking Bad page
    seasons = request.POST.getall('seasons')
    content = '<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content = content + '<table class="brb_table">'
    for season in seasons:
        season_name = season
        content = content + '<tr>'
        content = content + '<td class="brb_table"><p>'+ season_name + ' includes <strong>16</strong> episodes.</p></td>'
        content = content + '<td class="brb_table"><p style="text-align:center"><img class="brb_imgborder" alt="Breaking Bad" src="/static/brb_'+season_name+'.jpg" style="height:360px; width 120px" /></p></td>'
        content = content + '</tr>'
    content = content + '</table>'
    return htmlify("brb","Seasons of Breaking Bad", content)

def peaky_blinders_page(): #Peaky Blinders page
    content = '<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content =  content +"""
    <h1 class="pb_headbox" style="color:white">Peaky Blinders</h1> <br>
    <div class="pb_imagebox">
    <img class="pb_imgborder" src="/static/pb_index.jpg" alt="Peaky Blinders" style="margin-top:10px; height:350px; width:640px" />
    </div>
    <br>
    <div class="pb_checkbox">
        <form action="/pb_season" method="POST">
            <input type="checkbox" name="seasons" value="Season1" /> Season 1<br>
            <input type="checkbox" name="seasons" value="Season2" /> Season 2<br>
            <input type="submit" value="Show!" />
    </form> </div> <br>

            <div class="rate_inseries_pb">
        <img src="/static/star.png" alt="Star" style="height:10%; width:5%" /><br>
        Rate Peaky Blinders
        <form action="/rating" method='POST'>
            <p><input name="series" value="Peaky Blinders" readonly/></p>
            <input type="radio" name="rate" value="1" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />1 
            <input type="radio" name="rate" value="2" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />2
            <input type="radio" name="rate" value="3" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />3
            <input type="radio" name="rate" value="4" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />4
            <input type="radio" name="rate" value="5" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />5
            <input type="submit" value="Rate!" />
        </form></div><br>
        
    <div class="pb_serie_selector">
    <p>To check out another serie select from below:</p>
    <form action="/serie_page" method='POST'>
        <input type="radio" name="series" value="brb" /> Breaking Bad <br>
        <input type="radio" name="series" value="td" /> True Detective <br>
        <input type="submit" value="Go!" />
    </form></div>
    """
    return htmlify("pb", "Peaky Blinders", content)

def pb_season(): #Seasons of Peaky Blinders page
    seasons = request.POST.getall('seasons')
    content ='<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content = content + '<table class="pb_table">'
    for season in seasons:
        season_name = season
        content = content + '<tr>'
        content = content + '<td class="pb_table"><p>'+ season_name + ' includes <strong>6</strong> episodes.</p></td>'
        content = content + '<td class="pb_table"><p style="text-align:center"><img class="pb_imgborder" alt="Peaky Blinders" src="/static/pb_'+season_name+'.jpg" style="height:360px; width 120px" /></p></td>'
        content = content + '</tr>'
    content = content + '</table>'
    return htmlify("td","Seasons of Peaky Blinders", content)

def true_detective_page(): #True Detective page
    content = '<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content = content + """
    <h1 class="td_headbox" style="color:#f2f2f2">True Detective</h1> <br>
    <div class="td_imagebox">
    <img class="td_imgborder" src="/static/td_index.jpg" alt="True Detective" style="margin-top:10px; height:350px; width:640px" />
    </div>
    <br>
    <div class="td_checkbox">
        <form action="/td_season" method="POST">
            <input type="checkbox" name="seasons" value="Season1" /> Season 1<br>
            <input type="checkbox" name="seasons" value="Season2" /> Season 2<br>
            <input type="submit" value="Show!" />
    </form> </div> <br>
    
        <div class="rate_inseries_td">
        <img src="/static/star.png" alt="Star" style="height:10%; width:5%" /><br>
        Rate True Detective
        <form action="/rating" method='POST'>
            <p><input name="series" value="True Detective" readonly/></p>
            <input type="radio" name="rate" value="1" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />1 
            <input type="radio" name="rate" value="2" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />2
            <input type="radio" name="rate" value="3" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />3
            <input type="radio" name="rate" value="4" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />4
            <input type="radio" name="rate" value="5" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />5
            <input type="submit" value="Rate!" />
        </form></div><br>
        
    <div class="td_serie_selector">
    <p>To check out another serie select from below:</p>
    <form action="/serie_page" method='POST'>
        <input type="radio" name="series" value="brb" /> Breaking Bad <br>
        <input type="radio" name="series" value="pb" /> Peaky Blinders <br>
        <input type="submit" value="Go!" />
    </form></div>
    """
    return htmlify("td","True Detective", content)

def td_season(): #Seasons of True Detective page
    content ='<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'    
    seasons = request.POST.getall('seasons')
    content = content + '<table class="td_table">'
    for season in seasons:
        season_name = season
        content = content + '<tr>'
        content = content + '<td class="td_table"><p>'+ season_name + ' includes <strong>10</strong> episodes.</p></td>'
        content = content + '<td class="td_table"><p style="text-align:center"><img class="td_imgborder" alt="True Detective" src="/static/td_'+season_name+'.jpg" style="height:360px; width 120px" /></p></td>'
        content = content + '</tr>'
    content = content + '</table>'
    return htmlify("td","Seasons of True Detective", content)

def add_serie(): 
    content ='<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    content = content + """
        <div class="add_serie">
        <p>If the serie you want to rate is not included in the list, you can add it from below:</p>
        <form action="/rating" method='POST'>
         New serie: <input type="text" name="serie_new" placeholder="Type a serie name..." />
        <input type="submit" value="Add" /></form></div>
        """

    return htmlify ("page","Add Serie",content)

def limitdecimals(number):
    integer = int(number)
    decimal = number - int(number)
    lmt_decimal = int(decimal * 10) / 10
    new_number = integer + lmt_decimal
    return new_number

def rating_page():
    global input_series
    global ratings
    global rating_number
    global rating

    content = '<p class="homepagebutton"><span><a class="global_link" href="/">Homepage</a></span></p>'
    same_input_counter = 0

    if request.POST.getall('serie_new') == ['Breaking Bad'] or request.POST.getall('serie_new') == ['Breaking bad']:
        same_input_counter += 1
    elif request.POST.getall('serie_new') == ['True Detective'] or request.POST.getall('serie_new') == ['True detective']:
        same_input_counter += 1
    elif request.POST.getall('serie_new') == ['Peaky Blinders'] or request.POST.getall('serie_new') == ['Peaky blinders']:
        same_input_counter += 1

    if request.POST.getall('serie_new') == [''] or request.POST.getall('serie_new') == [' ']:
        same_input_counter += 2
        
    for counter in range (3,len(input_series)):
        if request.POST.getall('serie_new') == [input_series[counter]]:
            same_input_counter += 1
        elif request.POST.getall('serie_new') == ['Breaking Bad']:
            same_input_counter += 1
        elif request.POST.getall('serie_new') == ['True Detective']:
            same_input_counter += 1
        elif request.POST.getall('serie_new') == ['Peaky Blinders']:
            same_input_counter += 1
            
    if same_input_counter !=0:
        input_series = input_series

    else:
        input_series = input_series + request.POST.getall('serie_new')

    user_rate = request.POST.get('rate')
    selected_serie = request.POST.get('series')
        
    if same_input_counter == 0:
        if request.POST.getall('serie_new') != []:
            content = content + """<div class="addbox"><p><strong>""" + str(input_series[len(input_series)-1]) + """</strong> has been added to list!</p>"""
            content = content + '<p>You can rate <strong>' + str(input_series[len(input_series)-1]) + '</strong> from list:</p></div><br>'
            ratings = ratings + [0]
            rating_number = rating_number + [0]
            rating = rating + [0]
    elif same_input_counter == 1:
        content = content +'<div class="errorbox"><h2>THE SERIE YOU HAVE ENTERED IS ALREADY IN THE LIST</h2>'
        content = content +'<p>If you want to rate it, rate from below</p></div><br>'
    else:
        content = content +'<div class="spacebox"><strong>YOU SHOULD ENTER AT LEAST 1 CHARACTER</strong></div><br>'
  
    if user_rate != None and request.POST.get('series') != None:
        content = content + """<div class="votebox">Your vote for <strong>"""+str(request.POST.get('series'))+"""</strong> has been added.</div><br>"""
        
    content = content + """
            <div class="ratebox">
            <p style="text-align:center"> <strong>RATE SERIE</strong> </p>
            <form action="/rating" method='POST'>
            <select name="series">
                <option value="Breaking Bad" selected>Breaking Bad</option> 
                <option value="Peaky Blinders">Peaky Blinders</option>
                <option value="True Detective">True Detective</option>
                """

    for table_counter in range(3,len(input_series)):
        content = content + '<option value="'+str(input_series[table_counter])+'">'+str(input_series[table_counter])+'</option>'
    content = content + """</select><br>"""
    content = content + """<br>
            <input type="radio" name="rate" value="1" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />1 
            <input type="radio" name="rate" value="2" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />2
            <input type="radio" name="rate" value="3" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />3
            <input type="radio" name="rate" value="4" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />4
            <input type="radio" name="rate" value="5" /> <img src="/static/star.png" alt="Star" style="height:10%; width:5%" />5
            <input type="submit" value="Rate!" />
        </form></div><br>"""
            
    for table_counter in range(0,len(input_series)):
        if request.POST.get('series') == input_series[table_counter] and request.POST.get('rate') != None:
            ratings[table_counter] = ratings[table_counter] + int(request.POST.get('rate'))
            rating_number[table_counter] = rating_number[table_counter] + 1
        if rating_number[table_counter] == 0:
            rating[table_counter] = 0
        else:
            rating[table_counter] = ratings[table_counter]/rating_number[table_counter]
            if rating[table_counter] == int(rating[table_counter]):
                rating[table_counter] = int(rating[table_counter])
            else: 
                rating[table_counter] = limitdecimals(rating[table_counter])
            
    content = content + """
        <table class="table_rating_table">
        <tr><td colspan="3" class="rating_td" style="border:0px"><strong>RATING OF SERIES</strong></td></tr>
        <tr>
            <td class="rating_td"><strong>Serie Name</strong></td>
            <td class="rating_td"><strong>Rating</strong></td>
            <td class="rating_td"><strong>Nm.Votes</strong></td>
        <tr>
            <td class="table_rating_td">Breaking Bad</td>
            <td class="rating_td"><strong>"""+str(rating[0])+"""</strong>/5</td>
            <td class="rating_td">"""+str(rating_number[0])+"""</td>
        </tr>
        <tr>
        <td class="table_rating_td">Peaky Blinders</td>
        <td class="rating_td"><strong>"""+str(rating[1])+"""</strong>/5</td>
        <td class="rating_td">"""+str(rating_number[1])+"""</td>
        </tr>
        <tr>
        <td class="table_rating_td">True Detective</td>
        <td class="rating_td"><strong>"""+str(rating[2])+"""</strong>/5</td>
        <td class="rating_td">"""+str(rating_number[2])+"""</td>
        </tr> """

    for table_counter in range(3,len(input_series)):
        content = content + """
        <tr><td class="table_rating_td"> """ +str(input_series[table_counter])+ """ </td>"""
        content = content + """<td class="rating_td"> <strong>""" +str(rating[table_counter])+"""</strong>/5</td>"""
        content = content + """<td class="rating_td">"""+str(rating_number[table_counter])+"""</td>"""
        content = content + '</tr>'

    total_votes = 0
    for counter in range(0,len(rating_number)):
        total_votes = total_votes + rating_number[counter]
    
    content = content + """<tr><td colspan="3" class="table_rating_td" style="text-align:center">
                  TOTAL VOTES: <strong>"""+str(total_votes)+"""</strong></td></tr>"""
    
    content = content + """<tr><td colspan="3" class="table_rating_td" style="text-align:center">
                  <form action="/add_new_serie" method='POST' style="color:white">
                  ADD NEW SERIE <input type="submit" value="+" /></form></td></tr>"""
        
    content = content + '</table>'
    return htmlify ("page","Rating Chart",content)

def server_static(filename): #css file 
    return static_file(filename, root='/users/Ugurcan/Desktop/python/a3_template/static')
    
route('/assignment3/', 'GET', a3_index)
route('/', 'GET', website_index)
route('/series/' ,'POST', get_serie)
route('/serie_page' ,'POST', serie_controller)
route('/brb_season', 'POST', brb_season) 
route('/pb_season', 'POST', pb_season) 
route('/td_season', 'POST', td_season)
route('/add_new_serie', 'GET', add_serie)
route('/add_new_serie', 'POST', add_serie)
route('/rating', 'GET', rating_page) 
route('/rating', 'POST', rating_page) 
route('/static/<filename>', 'GET', server_static)

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

