import random, json

JSONs_PATH = './src/libraries/JsonFiles/'

lorem_ipsum = """Lorem ipsum dolor sit amet, fugit habemus vel id. Te vix sonet regione, quo cu tollit pertinacia, efficiendi deterruisset ne cum. Alii appetere eum ut, id simul laudem maiestatis eum, ius habeo recteque definitionem an. Legere fuisset delicata id usu, eu aperiam alterum cum, cu mel eros falli.
    Vivendum concludaturque vix ut. Legimus luptatum mei ex, oblique nominavi noluisse vix ei. Ei option eleifend posidonium per, facer latine ponderum in vis. Eu mei verear perfecto, qui id delectus percipitur interpretaris. Nostro luptatum recusabo ea sea, in mel erat audire. Vel impedit denique te.
    Eu verear oblique vituperata mei, est ei vidisse dolores, eam alienum postulant splendide at. Vim ne tritani praesent, ceteros oporteat ut vis. Ad putant verterem expetendis nam, ad vel viris appareat. Nec ne audire vulputate, id has erat clita, sea nulla erroribus id. Ea vix mundi scriptorem, timeam deserunt volutpat ne eos. Eu tritani dolores sed, munere nemore utroque no vix, veri instructior eos no. No legimus sadipscing nam.
    Has duis ullum munere in. In sint oblique consequat has, ponderum salutandi mei ne, eu pro dicit officiis placerat. Ea purto case has. Mentitum prodesset philosophia mea id. Admodum accumsan ex vis.
    Mea et elit suscipit dissentias, et debet choro iudicabit vis. Debet maiorum vituperata mel ne, mel omnes mucius labitur te. Utinam homero et nam. Duo albucius adipisci cotidieque an, nam libris reprehendunt ne. Quis equidem mel no.
    Vim eu quot suavitate complectitur. Ut nam harum aliquid, quo ea dolorem hendrerit, forensibus adversarium mea in. Per quando nemore no, mea ex efficiendi suscipiantur. Cum ea discere reformidans, te sit enim prodesset. Usu ut modus delenit, purto deserunt prodesset eum ne, unum luptatum vim et. Mel invenire periculis comprehensam ad, eos id omnesque percipitur, cu qui probo detracto deleniti.
    Movet solet quaerendum his ex. Ei libris adipisci nam. Ex mollis ancillae recteque vix. Vix detracto delectus intellegam cu, eius fuisset interesset duo ei. At bonorum suavitate qui. Eam dictas percipitur dissentias id, dissentiunt intellegebat ut per.
    Cum et quem alia dicam, at duo ferri nullam dolorem, pri cibo torquatos ne. Sit at intellegat consectetuer, mel decore ceteros et. Sit an laudem omnium volumus. Consul saperet pro ne. Dicit everti interpretaris no mea. His no vocent timeam eleifend, te vim accusam appareat, elit inani ridens te sit.
    Id pri libris similique. Enim omnis errem cum an, id scripta reformidans eum. Cum duis labores eu, duo falli iusto accusata te, audire appareat corrumpit ad vis. Eum cetero nusquam cu, probo ubique te nam. Tritani prompta vim ex.
    At vel nostro cetero oporteat. Discere democritum eum cu. Stet denique scaevola in has, laoreet deterruisset consequuntur no usu, in putent nostro delectus per. Platonem suavitate definiebas cum no, cum at atqui dicta periculis. An eros accusam noluisse sed, te sea harum tincidunt moderatius, ut viris tritani pri. Ne eum albucius mnesarchum, sonet sensibus perpetua te quo.
    Ex latine laoreet vim, eum odio mucius nusquam no. Dicam erroribus tincidunt per ei. An vim integre postulant intellegam, erat reque fuisset at nam. Iriure scaevola luptatum qui ad, molestiae consequuntur nam at. Fastidii laboramus nam ei, te has dolore ancillae, ut ubique gloriatur forensibus vim. Vidisse argumentum necessitatibus ei sed, te sed laudem debitis fuisset, eu noster laboramus pri.
    Diam menandri forensibus nam ea. Cum consetetur intellegam cu, ea populo reformidans per. Eum cu vocibus habemus deleniti, ei nam natum qualisque conceptam, eu mel ponderum repudiare. Eu usu omnes facilisis, mutat etiam ei vim. Mel placerat phaedrum petentium id, diam invenire voluptatibus ei eum, ea iusto delectus appellantur vix. Et duis impedit quaestio vim, commune officiis repudiandae at eam, nam et fugit habemus petentium. Et sed sumo movet virtute.
    Deseruisse sadipscing in cum, pri id postea fuisset. Sed et debet viris definitionem, mucius mediocrem cum et, te mel essent scripserit intellegebat. An per quaestio vulputate, ne vis oporteat pericula prodesset. Has malorum erroribus id, an nec harum perpetua accommodare.
    Ut aeque debitis est, ne sit iudico scripserit. Esse numquam ut vim, has sint mundi splendide at. Ne mel cetero consetetur, an qui discere ancillae. Cu nemore volumus repudiandae quo. No regione quaerendum est, vis et integre placerat repudiandae.
    Ei vel posse legere indoctum, nam wisi ocurreret conceptam et. Melius commune assentior est eu, cu dico atqui pro. Minimum complectitur no qui. Nonumes accumsan cum at, qui idque persecuti definitionem an, pro in libris quaeque eloquentiam. Ei dolores sensibus vim, admodum invidunt his ex."""\
    .replace(".", "").replace(",", "").split(" ")

months = ["January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
]

domains = ["gmail", "hotmail", "yahoo"]

countries = [(country['code'], country['name']) for country in
                json.load(open(JSONs_PATH+'countries.json'))]


upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = "0123456789"

def random_choice(string_sequence, length):
    x = ""
    for _ in range(length):
        x += random.choice(string_sequence)
    return x

def random_email():
    return  random_choice(numbers, random.randint(3, 5)) + random_choice(lower_letters+upper_letters, random.randint(3, 5)) + "@" + random.choice(domains) + ".com"

def random_date():
    year = random.randint(1970, 2008)
    month = random.choice(months)

    if(month == "February"):
        day = random.randint(1, 28)
    elif(month in ["February", "April", "June", "Sepember", "November"]):
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    return "{}/{}/{}".format(day, month, year)

