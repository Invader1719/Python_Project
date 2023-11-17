import unittest
from Chiper_Coder import Chiper
from Chiper_Coder import Chiper_hack
from Visioner_Coder import Visioner
from Visioner_Coder import DEVisioner
from Vernam import Vernam_coder


class test_Calculator1(unittest.TestCase):
  '''
  Первая серия тестов проверяет корректность работы
  Шифра Цезаря на английском и Русском языках. Проверяет
  различные граничные случаи алфавита и ключа.
  А также тест обратимости что Цезарь со сдвигом
  +3 и потом для этого текста -3 даст исходный текст

  Вторая серия тестов проверяет корректность работы взлома
  шифра Цезаря на трех текстах Евангелие от Иоанна,
  текст(на английском) из википедии про Джона Леннона и
  Текст про Дарта Вейдера. На всех трех текстах программа
  выдает адекватный взлом, что подтверждает корректность
  работы алгоритма

  Третья серия тестов проверяет корректность работы Шифра
  Виженера. В начале будет тест из Википедии, потом тест
  некоторых крайних случаев, потом будет проверка обратимости
  шифра(те зная шифротекст получить исходный текст, зная ключ)
  Тесты идут с \n потому что при считывании из графического
  окна они есть

  Четвертая серия тестов проверяет работы шифра Вернама
  Учитывая мою реализацию шифра, основной критерий по
  которому можно проверять корректность моего шифра
  это сойство XOR в (a XOR b) XOR b = a
  Так, что в здесь представленны тесты проверяющие крайние
  значения работы шифра
  '''


  def test_1Caesar1(self):
    input_text = 'abcdef'
    key = '3'
    correct = 'defghi'
    ans = Chiper(input_text, key)
    self.assertEqual(ans, correct)

  def test_2Caesar2(self):
    input_text = 'abcdefghijklmnopqrstuvwxyz'
    key = '3'
    correct = 'defghijklmnopqrstuvwxyzabc'
    ans = Chiper(input_text, key)
    self.assertEqual(ans, correct)

  def test_3Caesar3(self):
    input_text = 'abcdefghijklmnopqrstuvwxyz'
    key = str(26*100500 + 3)
    correct = 'defghijklmnopqrstuvwxyzabc'
    ans = Chiper(input_text, key)
    self.assertEqual(ans, correct)

  def test_4Caesar4(self):
    input_text = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = '3'
    correct = 'ГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ'
    ans = Chiper(input_text, key)
    self.assertEqual(ans, correct)

  def test_5Caesar5(self):
    input_text = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    key = '-3'
    correct = 'ЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬ'
    ans = Chiper(input_text, key)
    self.assertEqual(ans, correct)

  def test_6Caesar6(self):
    input_text = 'Астроном приобрел телескоп диаметром объектива 280 мм с фокусным расстоянием 2 метра. Посоветуйте, окуляры с какими фокусными расстояниями ему выбрать, и для наблюдений каких объектов они подойдут.'
    key = '3'
    correct = input_text
    ans = Chiper(Chiper(input_text, key), "-" + key)
    self.assertEqual(ans, correct)

  def test_7Caesar_hack1(self):
    input_text = "john lennon was born on 9 october 1940 at liverpool maternity hospital to julia (née stanley) (1914–1958) and alfred lennon (1912–1976). alfred was a merchant seaman of irish descent who was away at the time of his son's birth.[4] his parents named him john winston lennon after his paternal grandfather, john 'jack' lennon, and prime minister winston churchill.[5] his father was often away from home but sent regular pay cheques to 9 newcastle road, liverpool, where lennon lived with his mother;[6] the cheques stopped when he went absent without leave in february 1944.[7][8] when he eventually came home six months later, he offered to look after the family, but julia, by then pregnant with another man's child, rejected the idea.[9] after her sister mimi complained to liverpool's social services twice, julia gave her custody of lennon."
    ans = Chiper_hack(Chiper(input_text, 123321))
    correct = input_text
    self.assertEqual(ans, correct)

  def test_8Caesar_hack2(self):
    input_text = "в начале было слово, и слово было у бога, и слово было бог. оно было в начале у бога. все чрез него начало быть, и без него ничто не на́чало быть, что на́чало быть. в нем была жизнь, и жизнь была свет человеков. и свет во тьме светит, и тьма не объяла его. был человек, посланный от бога; имя ему иоанн. он пришел для свидетельства, чтобы свидетельствовать о свете, дабы все уверовали чрез него."
    ans = Chiper_hack(Chiper(input_text, 7))
    correct = input_text
    self.assertEqual(ans, correct)

  def test_9Caesar_hack3(self):
    #Я сдвинул исходный текст на +5 цезарем
    input_text = """Уцтужтуо цнсжурнмс иаъетнд Жйоийхе, мерулйттао ж тйзу \
цеснс Ршпецус, мепргьейчцд ж чус, ьчу уту джрдйчцд пеп ёа \
цнсжурус ргёузу еёцургчтузу инпчечухе, пучухао цчхйснчцд п \
жрецчн, ту тй ъуьйч тйцчн ме тйк учжйчцчжйттуцчб. Чеп, жу \
жиуъй цнчъе фхуцрйлнжейчцд чепуй мтеьйтнй: ргёуо инпчечух \
цчхйснчцд уёйцфйьнчб цйёй жцк, учтнсед вчу ш ихшзнъ. Чеп н \
Иехч Жйоийх жиаъейч ж цйёд пнцрухуи, учтнсед йзу ш ихшзнъ, н \
ихшзнс иуцчекчцд сйтбэй жумишъе. Цумжшьтао цнсжурнмс йцчб н ж \
мружйюйс жаиуъй: йцрн ш инпчечухе тй фуршьейчцд учтдчб ш \
цжуёуитаъ ргийо чу, ьчу нс фхнтеирйлнч, ут цчхйснчцд нцфухчнчб \
вчу. Чеп н Жреиапе цнчъуж жаиаъейч шзрйпнцрао зем, пучухас \
тйрбмд иаэечб, ьчуёа цжуёуитас ргидс иуцчеруцб сйтбэй пнцрухуие."""

    ans = Chiper_hack(input_text)
    correct = b = """основной символизм дыхания вейдера, заложенный в него самим \
лукасом, заключается в том, что оно является как бы символом любого \
абсолютного диктатора, который стремится к власти, но не хочет нести \
за неё ответственность. так, во вдохе ситха прослеживается такое \
значение: любой диктатор стремится обеспечить себе всё, отнимая это \
у других. так и дарт вейдер вдыхает в себя кислород, отнимая его у \
других, и другим достаётся меньше воздуха. созвучный символизм есть \
и в зловещем выдохе: если у диктатора не получается отнять у свободных \
людей то, что им принадлежит, он стремится испортить это. так и владыка \
ситхов выдыхает углекислый газ, которым нельзя дышать, чтобы свободным \
людям досталось меньше кислорода."""
    self.assertEqual(ans, correct)

  def test_10Visioner1(self):
    input_text = 'ATTACKATDAWN\n'
    key = 'LEMON\n'
    correct = 'LXFOPVEFRNHR\n'
    ans = Visioner(input_text, key)
    self.assertEqual(ans, correct)

  def test_11Visioner2(self):
    input_text = 'ATTACKATDAWN\n'
    key = 'a\n'
    correct = 'ATTACKATDAWN\n'
    ans = Visioner(input_text, key)
    self.assertEqual(ans, correct)

  def test_12Visioner3(self):
    input_text = """НАСТОЯЩИЙ ВИНОВНИК КРАЖИ АЛМАЗОВ\
  И УБИЙСТВА СОЛДАТ ОХРАНЫ В НОЧЬ НА\
  ДВАДЦАТЬ ВТОРОЕ ЯНВАРЯ ТЫСЯЧА\
  ВОСЕМЬСОТ ДВАДЦАТЬ ШЕСТОГО ГОДА\
  НЕ ЖОАМ ДАКОСТА, НЕСПРАВЕДЛИВО ПРИ\
  ГОВОРЕННЫЙ К СМЕРТИ, А Я, НЕСЧАСТНЫЙ\
  СЛУЖАЩИЙ УПРАВЛЕНИЯ АЛМАЗНОГО\
  ОКРУГА; ДА, Я ОДИН, В ЧЕМ И ПОДПИСЫ\
  ВАЮСЬ СВОИМ НАСТОЯЩИМ ИМЕНЕМ,\
  ОРТЕГА"""
    key = 'ОРТЕГА'
    correct = input_text
    ans = DEVisioner(Visioner(input_text, key), key)
    self.assertEqual(ans, correct)

  def test_13Vernam1(self):
    input_text = 'abcdef\n'
    key = '111111\n'
    correct = input_text[:-1:]
    ans = Vernam_coder(Vernam_coder(input_text, key), key)
    self.assertEqual(ans, correct)

  def test_14Vernam2(self):
    input_text = 'abcdef\n'
    key = 'абвгде'
    correct = input_text[:-1:]
    ans = Vernam_coder(Vernam_coder(input_text, key), key)
    self.assertEqual(ans, correct)

  def test_15Vernam3(self):
    input_text = 'abcdef\n'
    key = 'partёй'
    correct = input_text[:-1:]
    ans = Vernam_coder(Vernam_coder(input_text, key), key)
    self.assertEqual(ans, correct)

if __name__ == "__main__":
  unittest.main()
