import requests
import base64
import time
import re
from urllib.parse import urlparse
import os


# в цикл надо поставить, чтобы перебор был
def take_url_img_in_wp(list_test):
    url_img = re.search("(?P<url>https?://[^\s]+)", list_test[0][2]).group("url")  # выделить из кортежа ссылки на одну картинку
    a = urlparse(url_img)  # выделили название картинки из ссылки
    name_img = os.path.basename(a.path)
    name_img = name_img.rstrip(name_img[-1])  # убрали последний элемент

    img_data = requests.get(url_img).content  # скачиваем миниатюру с сайта и добавляем к себе в медиабиблиотеку WP
    with open(f'pictures/{name_img}', 'wb') as f:  # сохранили у себя на компьютере
        f.write(img_data)

    url = "https://zvukoviku.ru/wp-json/wp/v2/"
    user = "zvukz"
    password = "mrQI GGvU JXEJ 5WM5 LhJP hJz1"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    # date = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())

    media = {'file': open(f'pictures/{name_img}', 'rb'),  # открыли миниатюру на компьютере
             'caption': 'pic'}
    responce_media = requests.post(url + 'media', headers=header, files=media)
    img_url_in_wp = responce_media.json()['guid']['rendered']  # ссылка в ВП на картинку

    return img_url_in_wp


# print(take_url_img_in_wp([(None, 'Полукустарник малина обыкновенная (Rubus idaeus) является представителем рода рубус семейства розовые. Этот род объединяет около 600 видов. Большинство данных видов были известны уже в Древнем мире, так, первое упоминание о существовании дикой малины имеются в рукописях 3 в. до нашей эры. Впервые культивировать малину стали в Западной Европе в 16 в. В природных условиях такой полукустарник предпочитает расти по речным берегам и в лесах. На протяжении многих веков данное растение входит в число наиболее популярных ягодных культур, выращиваемых в садах. На сегодняшний день это растение можно повстречать практически на каждом садовом участке. Душистые и очень вкусные плоды малины ценят еще и за их полезность, так в них содержатся минеральные вещества, нужные человеческому организму кислоты и витамины. Эта культура отличается своей неприхотливостью. Такое растение способно отлично расти и давать хорошие урожаи даже в запустении. Если за малиной правильно ухаживать, то она будет защищена от заражения различными заболеваниями и вредителями, а также будет давать богатые урожаи. Содержание ', '<img alt="" class="attachment-large size-large wp-post-image" decoding="async" height="564" sizes="(max-width: 700px) 100vw, 700px" src="https://rastenievod.com/wp-content/uploads/2018/01/2-13-700x564.jpg" srcset="https://rastenievod.com/wp-content/uploads/2018/01/2-13-700x564.jpg 700w, https://rastenievod.com/wp-content/uploads/2018/01/2-13-300x242.jpg 300w, https://rastenievod.com/wp-content/uploads/2018/01/2-13.jpg 800w" width="700"/> '), ('Особенности малины', ' На сегодняшний малина пользуется большой популярностью среди садоводов различных стран, как, например, смородина, земляника, крыжовник, клубника, голубика и другие очень полезные и просто вкусные садовые культуры. Очень часто садоводы выращивают малину не только для себя, но и на продажу. В связи с этим садовод старается получить богатый урожай ягод хорошего качества. Малина обыкновенная представляет собой листопадный полукустарник, высота которого может варьироваться от 150 до 250 сантиметров. У такого растения имеется деревянистый корень, вокруг которого вырастает большое количество придаточных корней. Это приводит к образованию крепкой разветвленной системы корней. Стебли являются прямостоячими. Травянистые молоденькие побеги очень сочные зеленого окраса, на их поверхности находится сизый налет и множество меленьких шипов. Уже на второй год стебли одревесневают и окрашиваются в коричневый цвет. Когда заканчивается плодоношение, наблюдается засыхание таких стеблей, однако в следующем сезоне их сменяют новые молодые побеги. Очереднорасположенные овальной формы листовые пластины имеют черешки, они являются сложными, насчитывается 3–7 яйцевидных листочков. Лицевая поверхность листьев темно-зеленая, а изнаночная ― белесого окраса, потому что на ней находится опушение. Пазушные верхушечные кистевидные соцветия состоят из цветков белого окраса, которые в диаметре достигают около 10 мм. Как правило, ягоды вырастают на второй год жизни стеблей. Ягоды представляют собой маленькие волосистые костянки, которые срослись в сложный плод, они могут быть окрашены в самые разные оттенки малинового цвета, а еще встречаются бордово-черные (у сортов, являющихся ежевикообразными) либо желтые плоды. Благодаря проводимым селекционным работам на свет появилась ремонтантная малина, ее плодоношение начинается в первый год роста, а за сезон с нее снимают 2 урожая. Куманика и ежевика являются видами малины, образующими длинные стебли, ими они цепляются за опору благодаря колючкам, размещающимся на их поверхности. Костяника и княженика являются травянистыми видами малины. Вырастить малину достаточно просто, но для того чтобы получить обильный урожай необходимо придерживаться правил агротехники данной культуры, а также правильно за ней ухаживать. ', '<img alt="13.Малина.Как посадить малину без ошибок." height="460" src="https://rastenievod.com/wp-content/plugins/wp-youtube-lyte/lyteCache.php?origThumbUrl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FZzc8YWE8Ilw%2F0.jpg" width="853"/> '), ('Посадка малины в открытый грунт', ' Высадкой малины в открытую почву можно заниматься и в весеннее, и в осеннее время (с сентября по октябрь). Подходящий для посадки участок должен быть солнечным. В том случае, если данную культуру выращивать в затененном месте, то из-за нехватки света молоденькие побеги иногда вытягиваются настолько, что затеняют плодоносящие стебли. У различных сортов малины свои предпочтения относительно грунта. Однако их большая часть хорошо растет на легких питательных почвах, также данному растению подходит суглинок и чернозем. Необходимый для малины рН почвы должен быть от 5,7 до 6,5. В низинах и в местах с неровным рельефом данный полукустарник выращивать нельзя, потому что в них наблюдается застой воды. Также для посадки не подходят крутые склоны, а еще возвышенные участки, в этом случае малина будет страдать от нехватки влаги. Для посадки такой культуры рекомендуется выбирать равнинный либо имеющий небольшой уклон участок. На одном и том же месте без пересадки такой полукустарник можно выращивать 7–10 лет, после чего ему понадобится пересадка, потому что грунт будет сильно истощенным. А на данном участке вновь высадить малину можно будет лишь спустя не меньше 5–7 лет. Там, где выращивались пасленовые (картофель, томаты, перец), высаживать данную ягодную культуру ни в коем случае нельзя. Зато участок после зерновых либо бобовых культур для высадки малины подходит очень хорошо.  Весенняя и осенняя посадка различаются лишь способом подготовки к данной процедуре, а в остальном они абсолютно одинаковы. В начале весеннего периода нужно подготовить яму, величина которой должна быть 0,5х0,4х0,4 м, при этом верхний питательный слой грунта следует откинуть отдельно. Дистанция меж экземплярами в саду должна быть около 0,5 м, при этом ширина междурядий должна быть не меньше 1,5 м. Верхний питательный слой грунта необходимо соединить с 50 граммами сернокислого калия, со 100 граммами гранулированного суперфосфата, с 10 килограммами перегноя либо компоста и с 0,4 килограммами древесной золы. Часть получившейся почвосмеси нужно высыпать в ямку, а остатки надо насыпать горкой возле нее. Если до того как вы приступите к посадке, почвосмесь в ямке слежится, ее нужно будет взрыхлить. Затем в ямку следует поместить саженец таким образом, чтобы почка замещения располагалась чуть ниже уровня грунта. После того как корешки будут осторожно расправлены, ямку следует заполнить почвой. Ее утрамбовывают, а затем вокруг растения делают не очень глубокую луночку, которую следует наполнить водой. После того как жидкость полностью впитается, поверхность лунки надо замульчировать опилками, перегноем либо сухой соломой. Саженец укорачивают до 0,3 м над уровнем почвы. Если в течение нескольких суток после высадки малины будет стоять сухая погода, то растеньицам понадобится повторный полив. Весной высаживать малину хуже, чем осенью, потому что велика вероятность опоздать по срокам из-за неблагоприятной погоды, в результате чего саженцы будут приживаться намного хуже. Весной высаживают приобретенный в специальном магазине либо питомнике посадочный материл либо тот, что был заготовлен в осеннее время (его на зимовку помещают в холодильник).  В осеннее время подготовкой посадочной ямы следует знаться за 6 недель до дня высадки. Участок подвергают перекопке на глубину штыка лопаты, при этом выбирают все корни сорняков и вносят 0,2–0,4 кг суперфосфата, от 2 до 3 ведер перепревшего навоза и 100–200 грамм сернокислого калия из расчета на 1 м2 участка. Если до посадки вы удобрите почву, то малина не будет нуждаться в фосфорных и калийных удобрениях примерно 5 лет. Если грунт торфяной, то на каждый 1 м2 участка нужно внести по четыре ведра песка. Лучше всего высадкой малины заниматься в последние дни сентября либо первые ― октября. Осенью высаживать данную культуру рекомендуют и специалисты, и опытные садоводы, ведь в этом случае можно будет никуда не спеша подготовить участок под посадку, а сами растения до зимы хорошо укореняются, а в весеннее время начинают активно расти. ', '<img alt="Правильная посадка малины осенью. Сорт Таруса." height="460" src="https://rastenievod.com/wp-content/plugins/wp-youtube-lyte/lyteCache.php?origThumbUrl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FcXOrVvWcfIM%2F0.jpg" width="853"/> '), ('Уход за малиной', ' Сразу же после того как растает весь снег на участке, его надо будет освободить от опавших в прошлом году листьев, потому что в них могут находиться болезнетворные микроорганизмы либо вредители, прятавшиеся там от зимних морозов. Данному полукустарнику необходима опора, поэтому в весеннее время следует произвести подвязку малины к шпалере. Если растение будет подвязано к шпалере, то в результате этого оно будет равномерно освещаться солнечными лучами, произойдет ускорение созревания и роста молоденьких прикорневых побегов, а также за такими кустами сравнительно легче ухаживать. Если вы решили сделать шпалеры, то вам понадобится в конце и в начале каждого ряда врыть по обеим сторонам мощные столбики в высоту достигающие 150 сантиметров. Меж этими столбами необходимо протянуть проволоку в 2 ряда: нижний ряд должен располагаться на высоте 0,6–0,7 м от поверхности участка, а верхний ― на высоте 1,2 м. Чтобы избежать провисания проволоки, необходимо через каждые 5 м в землю воткнуть деревянный кол. Разместите стебли кустов по проволоке веерообразно, а затем зафиксируйте их, подвязав шпагатом. Спустя пару лет меж столбами необходимо протянуть дополнительные ряды проволоки: первый ― на высоте 0,3 м от поверхности участка, а другой ― на высоте 1,5 м. В остальное время ухаживать за данной культурой будет очень просто. Так, ее нужно систематически полоть, подкармливать, поливать, рыхлить почву около кустиков на небольшую глубину, после чего ее поверхность засыпается слоем мульчи. Что используют для подкормки данной культуры в весеннее время? В том случае, если перед посадкой в почву были внесены все необходимые удобрения, то в калии и фосфоре малина не будет нуждаться на протяжении 5 лет. Однако подкармливать растения азотсодержащими удобрениями необходимо каждый год. Подготовьте следующий питательный раствор для подкормки: 10 л воды соедините с 1 лопатой помета коровы и с 5 граммами мочевины либо селитры. Данную смесь вливают под каждое растение в последние дни марта либо первые ― апреля. Если вы решите использовать иное азотсодержащее удобрение, то на каждый 1 м2 участка надо будет взять от 20 до 25 грамм вещества. Затем поверхность грунта надо будет разрыхлить.  Когда в осеннее время все плоды с кустов будут собраны, нужно заняться подготовкой малины к предстоящей зимовке. К данной процедуре нужно подходить со всей ответственностью, так как именно от этого зависит, насколько обильным урожай будет в следующем сезоне. Поверхность участка необходимо освободить от старого мульчирующего слоя, который следует уничтожить, так как в нем могут находиться различные вредители либо болезнетворные микроорганизмы. Затем грунт аккуратно перекапывается на глубину не превышающую 8–10 сантиметров. 1 раз в пару лет под перекопку рекомендуется в почву внести древесную золу и компост. Азотсодержащие удобрения для подкормки малины в осеннее время не используются, потому что из-за них может начаться активный рост молоденьких побегов, у них поздно облетят листья, в результате чего увеличивается вероятность повреждения их морозом. В том случае, если полукустарник нуждается в фосфорных и калийных удобрениях, то их следует вносить в не очень глубокие (от 15 до 20 сантиметров) бороздки, которые должны располагаться от растений на расстоянии не менее 0,3 м. На 1 кустик берется не больше 40 грамм калийной соли и 60 грамм суперфосфата. У подкормленных таким образом растений улучшится закладка цветочных почек, что положительно отразиться на будущем урожае.  Поливать малину в весеннее и летнее время нужно только в том случае, если наблюдается продолжительная засуха. Если же систематически идут дожди, то в поливе она нуждаться не будет. В жаркий и засушливый период растению понадобится обильный полив, при этом вода должна промочить верхний слой грунта на 0,3–0,4 м. Помимо этого у данного полукустарника возникает необходимость в обязательном поливе в мае, перед тем как он зацветет, а также во время активного роста и созревания плодов. Подзимний полив для такой культуры имеет большое значение, так как в осеннее время у нее происходит закладка почек роста в корневой системе. При этом постарайтесь, чтобы почва пропиталась на максимально возможную глубину, тогда зимовка малины будет более чем успешной. Более всего для полива данного растения подходит капельный способ, потому что он обладает рядом преимуществ: Если вы желаете значительно сократить число поливов в летнее время, то поверхность участка следует засыпать слоем мульчи.  При пересадке такого растения нужно придерживаться тех же принципов, что и при его первичной посадке. Данный полукустарник склонен к сильному разрастанию. Его корни размещаются достаточно близко к поверхности почвы, и за летнее время вырастает большое количество побегов-отпрысков. При желании с помощью лопаты их можно отделить от материнского кустика и, выкопав вместе с корнями, высадить на новое постоянное место. Если экземпляр изросшийся и старый, то используя лопату от него можно отрезать наиболее молодую часть вместе с системой корней и комом земли, при этом следует учесть, что диаметр ее побегов не должен быть меньше 10 мм. У такой «деленки» нужно укоротить побеги до 0,25 м, а затем ее высаживают на другое место. Пересадить малину можно когда угодно, кроме зимнего периода. Однако опытные садоводы рекомендуют проводить данную процедуру в весеннее время. Чтобы предотвратить бесконтрольное разрастание такого растения, участок, где оно растет необходимо оградить, для этого по периметру в грунт вкапываются листы железа либо шифера.  Размножить малину очень просто, легко и быстро. О том, как ее размножить отпрысками, было подробно описано выше. Также для размножения этого растения используют черенкование. Нарезку черенков производят в июне в облачный день, для этого выбирают двухлетние либо трехлетние корневые отпрыски. Длина черенков должна быть от 10 до 12 сантиметров, а на них должно иметься 2 либо 3 листовые пластины. Черенки на 12 ч погружают в средство, стимулирующее рост корней, после этого производят их высадку в емкости объемом 0,5 л, которые нужно заполнить песком, смешанным с торфом. Емкости убирают под пленку, при этом следует учесть, что необходимая для укоренения черенков влажность воздуха должна быть примерно 90 процентов, а температура ― от 22 до 25 градусов. Спустя 4 недели черенки должны тронуться в рост. Когда это произойдет, их аккуратно вместе с комом земли переваливают в более просторную емкость: ее высота должна быть не меньше 14 сантиметров, а объем ― 1,5 л. После того как черенки приживутся, их надо начать закалять, для этого вынося на некоторое время на свежий воздух. Закаленные черенки высаживают на учебную грядку, им понадобится притенение от палящих солнечных лучей, которое убирают только тогда, когда растения приживутся и тронутся в рост. В осеннее время их пересаживают на постоянное место. Заготовленные в осеннее время черенки нужно подвергнуть обработке фунгицидом, что защитит их от грибковых заболеваний. Затем черенки нужно засыпать торфом и убрать на хранение в погреб, подвал либо иное прохладное место. Таким образом, до наступления весеннего периода черенки пройдут стратификацию, важно не забывать систематически увлажнять торф. В весеннее время черенки сразу же высаживаются на грядку, при этом ее поверхность надо засыпать слоем мульчи. Существует виды малины, для размножения которых используют укоренение верхушек (как у ежевики). Так, в их число входит пурпуровая и черноплодная малина. В первые осенние недели подросший побег начинает наклоняться к почве, при этом листочки, располагающиеся на его верхушке, становятся мельче, а сама она приобретает петлеобразную форму ― в данное время и производят ее укоренение. Данный побег следует отделить вместе с «ручкой», при этом его нужно укоренять точно так же, как это описано выше. ', '<img alt="Размножение малины" class="alignnone size-large wp-image-11397" decoding="async" height="421" loading="lazy" sizes="(max-width: 700px) 100vw, 700px" src="https://rastenievod.com/wp-content/uploads/2018/01/10-13-700x421.jpg" srcset="https://rastenievod.com/wp-content/uploads/2018/01/10-13-700x421.jpg 700w, https://rastenievod.com/wp-content/uploads/2018/01/10-13-300x180.jpg 300w, https://rastenievod.com/wp-content/uploads/2018/01/10-13.jpg 912w" width="700"/> '), ('Обрезка малины', ' В весеннее время у малины следует обрезать до здоровой почки все пострадавшие от морозов стебли, а еще надо вырезать травмированные, пораженные болезнью и слаборазвитые ветви. Если следовать правилам агротехники данной культуры, то на 1 погонный метр участка должно приходиться 10–15 побегов. В связи с этим на кусте следует вырезать все побеги, оставив лишь те, которые тронулись в рост первыми, их необходимо укоротить на 15–20 сантиметров. В результате такой прореживающей обрезки улучшится качество плодов, а также они будут крупнее. Подобную обрезку можно провести при желании в осеннее время, но все равно с наступлением весны у кустов нужно будет вырезать все травмированные и поврежденные морозом стебли. А по утверждению И. В. Казакова, кустики обрезанные весной дадут более богатый урожай.  В осеннее время после сбора урожая нужно удалить все двухлетние стебли, так как в следующем сезоне они не будут цвести и давать плоды. Конечно, их можно вырезать и в весеннее время, но в этом случае они будут отнимать у растения питательные вещества, так необходимые ему зимой. Вырезать следует все стебли, которые давали плоды в текущем сезоне. Если выращиваемая вами малина не ремонтантная, то ее обрезку можно произвести и пораньше, и совсем не обязательно ждать глубокой осени. Специалисты рекомендуют провести подобную процедуру сразу же после того, как весь урожай с кустов будет собран, в этом случае все силы малины будут направленны на рост и развитие молоденьких побегов, а именно они будут плодоносить в следующем сезоне. Если выращиваются ремонтантные сорта, то их следует обрезать по окончанию второго плодоношения. Все срезанные стебли рекомендуется уничтожить, так как на них могут поселиться патогенные микроорганизмы и различные вредители. ', '<img alt="Обрезка малины на зиму. Правила ухода за малиной. Сайт &amp;quot;Садовый мир&amp;quot;" height="460" src="https://rastenievod.com/wp-content/plugins/wp-youtube-lyte/lyteCache.php?origThumbUrl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FdQbl5MMPKsI%2F0.jpg" width="853"/> '), ('Зимовка малины', ' Очень важно правильно подготовить малину к зимовке. Очень распространенно мнение среди садоводов, что малину на зиму необходимо связать и оставить в стоячем положении. Однако этого делать ни в коем случае нельзя, потому что цветочные почки не укрытые снегом могут вымерзнуть. Кустики пригибают максимально близко к поверхности почвы и фиксируют в таком положении, подвязывая к самой нижней проволоке шпалеры. Со стеблей нужно убрать всю листву, для этого наденьте рукавицы и проведите по побегу по направлению снизу вверх. Будьте внимательны, потому что если вы будете обрывать листву, проводя рукой сверху вниз, то это может привести к удалению и цветочных почек. Постарайтесь, чтобы во время зимы данный полукустарник был полностью покрыт снегом. Поэтому при необходимости малинник нужно будет закидывать снегом. Также очень важно помнить, что зимующим растениям необходим воздух, в связи с этим появляющуюся на снежном покрове наледь следует обязательно прокалывать. Если зима будет малоснежной, в этом случае малинник нужно будет накрыть укрывным материалом. В весеннее время укрытие с участка надо убрать. Просмотрите все стебли и удалите те из них, что пострадали от мороза. Оставшиеся побеги можно поднять и подвязать к шпалере. ', '<img alt="Зимовка малины" class="alignnone size-large wp-image-11400" decoding="async" height="525" loading="lazy" sizes="(max-width: 700px) 100vw, 700px" src="https://rastenievod.com/wp-content/uploads/2018/01/13-13-700x525.jpg" srcset="https://rastenievod.com/wp-content/uploads/2018/01/13-13-700x525.jpg 700w, https://rastenievod.com/wp-content/uploads/2018/01/13-13-300x225.jpg 300w, https://rastenievod.com/wp-content/uploads/2018/01/13-13.jpg 900w" width="700"/> '), ('Болезни малины и их лечение', ' Многих садоводов интересует, из-за чего листва малины становится желтой и облетает? В том случае, если листва на кустике сменила свой цвет на желтый, то это значит что данный экземпляр заражен корневым раком, ржавчиной либо хлорозом. Узнать, что растение больно таким неизлечимым заболеванием как корневой рак, можно по появившимся вздутиям на поверхности корней, стебли вырастают чересчур короткими, плоды не имеют вкуса, а листовые пластины становятся желтыми и облетают. Зараженные растения следует извлечь из земли и уничтожить, при этом тот участок, на котором они росли, не должен использоваться под посадку не меньше 8 лет. Если же растение заражено ржавчиной, то она начнет проявляться в мае. Начнется подсыхание, пожелтение и облетание листвы, на поверхности стеблей появятся язвы темного окраса. Вылечить такое заболевание можно лишь на начальной стадии развития, для этого кустики опрыскивают раствором бордоской смеси (1%). Если же болезнь уже запущена и кусты поражены очень сильно, то их нужно обязательно выкопать и уничтожить. Главным переносчиком такого вирусного заболевания как хлороз является тля. В связи с этим, чтобы защитить малину от хлороза, необходимо предпринять все необходимые меры для борьбы с тлей. У зараженных экземпляров мельчают и деформируются листовые пластины, стебли перестают развиваться, плоды высыхают и утрачивают свои вкусовые качества. В некоторых случаях причиной развития хлороза может стать использование холодной воды для полива, сильная щелочная реакция грунта, недостаточное количество микроэлементов в земле либо застой воды в почве. Постарайтесь узнать, что именно стало причиной развития данного заболевания, и устраните ее в кратчайшие сроки.  Данная культура относится к числу влаголюбивых, поэтому если растениям не будет доставать влаги, то тогда листва начнет засыхать. Однако если кустики всегда поливаются вовремя и в достаточном объеме, то нужно хорошенько рассмотреть засохшие листики. Если на их поверхности вы увидите утолщения, то это значит, что малина поражена галлицей. Данный вредитель откладывает свои личинки на поверхности листовых пластин малины, в результате появляются подобные утолщения, именуемые галлами. Все зараженные побеги необходимо вырезать до корня, при этом пеньков остаться не должно, затем их сжигают. Если этот полукустарник будет поражен пурпуровой пятнистостью, которая является грибковой болезнью, то вначале на его листовых пластинах появятся пятнышки буро-красного окраса, а со временем они засыхают. После того как будут собраны с пораженных кустиков все плоды, их нужно опрыскать препаратом Циркон. Вырежьте до корня все засохшие стебли сразу же после того, как станет ясно, что растение больное, при этом ждать, пока наступит осень, не нужно.  Грибковое заболевание антракноз активно развивается в сырую дождливую погоду в летнее время. У пораженного кустика на поверхности листовых пластин появляются пятнышки серого цвета с красным окаймлением, плоды засыхают, а также наблюдается отмирание концов побегов. В целях профилактики для посадки следует выбирать сорта, обладающие устойчивостью к данному заболеванию, а также нужно вырезать и сжигать все зараженные части малины. Также пораженный экземпляр надо обработать раствором Нитрафена. ', '<img alt="Болезни и лечение малины. Антракноз. Септориоз. Дидимелла. Серая гниль(Ботритис)" height="460" src="https://rastenievod.com/wp-content/plugins/wp-youtube-lyte/lyteCache.php?origThumbUrl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FWsr4Jg09Sl4%2F0.jpg" width="853"/> '), ('Вредители малины и борьба с ними', ' На кустах малины могут поселиться следующие вредители: тля, паутинный клещ, побеговая и стеблевая малинные галлицы, долгоносик, малинная орехотворка, малинный жук и малинная стеблевая муха. В период цветения на данном полукустарнике может поселиться буро-желтый малинный жук. Данный вредитель питается бутонами, цветками и листвой растения, при этом самки в цветках устраивают свои яйцекладки. Вылупившиеся из яиц личинки поедают плоды. После того как сойдет снег, пораженные кустики необходимо опрыскать Нитрафеном, а во врем цветения вишни их обрабатывают Фитовермом. Малинная стеблевая муха делает свои яйцекладки в пазухах верхушечных листовых пластин, появившиеся на свет личинки выедают стебли изнутри. Малинная орехотворка и стеблевые, а также побеговые галлицы делают свои яйцекладки в молоденьких побегах, когда личинки вылупятся, то они будут их поедать. Если на кусте поселилась тля, то на поверхности стеблей и листовых пластин можно будет обнаружить медвяную росу, также происходит деформация побегов и скручивание листвы. Помимо этого данный вредитель является главным переносчиком различных опасных заболеваний. Паутинные клещи, селясь на малине, высасывают ее сок, при этом они являются переносчиками вирусных болезней и серой гнили. В бутонах цветков самка долгоносика делает свои яйцекладки, подгрызая при этом цветоножки. Одна особь может нанести вред большому количеству цветков (до 50). Чтобы избавиться от всех описанных вредителей, нужно ранней весной и после того, как будут собраны все плоды, обработать кустики Карбофосом либо Актелликом. А главное, помните, что если вы будете придерживаться правил агротехники, то проблем с вредителями у вас не возникнет. ', '<img alt="ВРЕДИТЕЛИ на МАЛИНЕ. Способы борьбы БЕЗ ХИМИИ (Малиновые МУХА, ЖУК, ДОЛГОНОСИК и ГАЛЛИЦА)" height="460" src="https://rastenievod.com/wp-content/plugins/wp-youtube-lyte/lyteCache.php?origThumbUrl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FwmO71ky-fgI%2F0.jpg" width="853"/> '), ('Сорта малины с фото и описанием', 'Множество сортов малины разделяют на крупноплодные, традиционные и ремонтантные. Традиционные сорта отличаются своей надежностью, они быстро приспосабливаются к климатическим условиям и нетребовательны к грунту, однако собрать с них богатый урожай не удастся. Стебли у крупноплодных сортов ветвятся сравнительно сильно, благодаря чему они отличаются высокой урожайностью, их плоды большие и душистые. Ремонтантные сорта дают 2 урожая за сезон, при этом плодоносить они прекращают лишь с наступлением очень сильных заморозков. Также данные сорта отличаются друг от друга цветом и качеством вкуса плодов, сроком созревания, а еще по степени устойчивости к болезням и вредным насекомым.     ', '<img alt="80.Малина. Высокоурожайные сорта малины." height="460" src="https://rastenievod.com/wp-content/plugins/wp-youtube-lyte/lyteCache.php?origThumbUrl=https%3A%2F%2Fi.ytimg.com%2Fvi%2F3i6DYRPS-6g%2F0.jpg" width="853"/> '), ('Свойства малины', 'Ягоды малины включают в свой состав фруктозу, органические кислоты – лимонную, яблочную, винную, аскорбиновую, муравьиную, капроновую, а еще витамины и микроэлементы – магний, железо, калий, кальций и фосфор. С давних пор малину используют в качестве противопростудного средства, так, с высушенными ягодами готовят чай, делают варенье либо перетирают свежие плоды с сахарным песком. Малина отличается от иных ягод тем, что после термической обработки все ее полезные свойства сохраняются. Из листвы растения готовят отвары и настои, используемые при ангине и кашле. А настой, приготовленный из листвы и цветков, применяют для лечения геморроя и гинекологических заболеваний. Препараты, изготовленные из ягод, цветков и листвы, отличаются жаропонижающим, антиоксидантным, антисклеротическим и противовоспалительным эффектом, их использует во время терапии простудных заболеваний, атеросклероза, гипертонии, сахарного диабета, малокровия, нарушений сердечного ритма, болезней почек. В восточной медицине подобными препаратами лечится половое бессилие и бесплодие. Настой, приготовленный из листвы, используется при угрях, рожистых воспалениях кожи, экземе и сыпях, при этом им протирают поверхность эпидермиса. Из него делают примочки при конъюнктивите и блефарите. Из корешков готовится отвар, используемый для лечения гнойного отита и остановки геморроидального и носового кровотечения. Не так давно в университете Клемсона были проведены исследования, касающиеся малины. Подопытным животным, имеющим раковую опухоль, давалась вытяжка малины, это привело к гибели 90 процентов раковых клеток. Данный результат не может повторить не один известный науке антиоксидант. При этом данным эффектом обладают все сорта малины. У малины имеется ряд противопоказаний. Ее не рекомендуется употреблять в период обострения гастрита, язвы желудка и двенадцатиперстной кишки. А еще она противопоказана людям, страдающим нефритом, подагрой и амилоидозом. Ваш адрес email не будет опубликован. Обязательные поля помечены * Комментарий * Имя *  Email *  Сайт      Δ ', '<img alt="Крыжовник" class="attachment-yarpp-thumbnail size-yarpp-thumbnail wp-post-image" data-pin-nopin="true" decoding="async" height="110" loading="lazy" src="https://rastenievod.com/wp-content/uploads/2018/01/1-13-205x110.jpg" width="205"/> '), ('Рубрики', '', '<img alt="Удобрения и стимуляторы" class="category_icon" src="https://rastenievod.com/wp-content/uploads/icons/13.png"/> '), ('Популярные растения', '', '<img alt="Бальзамин комнатный" class="wpp-thumbnail wpp_featured wpp_cached_thumb" height="160" loading="lazy" src="https://rastenievod.com/wp-content/uploads/wordpress-popular-posts/1773-featured-320x160.jpg" width="320"/> ')]))