from django.db import models
from datetime import datetime
# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    verification_text = models.CharField(max_length=20)
    addtime = models.DateTimeField(default=datetime.now)
    mailbox = models.CharField(max_length=30)

    class Meta:
        db_table = "login"

class wuhugneral(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    count = models.CharField(max_length=30)
    xingjiabistar = models.CharField(max_length=30)
    jingsestar =models.CharField(max_length=30)
    quweistar = models.CharField(max_length=30)
    comment = models.CharField(max_length=1500)
    shijian = models.DateField()
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "Generalcomment"

class commentnums(models.Model):
    name = models.CharField(max_length=20)
    score = models.CharField(max_length=10)
    shuliang = models.CharField(max_length=50)

    class Meta:
        db_table = "Commentnum"

class menghuan(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    count = models.CharField(max_length=30)
    xingjiabistar = models.CharField(max_length=30)
    jingsestar = models.CharField(max_length=30)
    quweistar = models.CharField(max_length=30)
    comment = models.CharField(max_length=1500)
    shijian = models.DateField()
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "menghuan"

class marenqi(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    count = models.CharField(max_length=30)
    xingjiabistar = models.CharField(max_length=30)
    jingsestar = models.CharField(max_length=30)
    quweistar = models.CharField(max_length=30)
    comment = models.CharField(max_length=1500)
    shijian = models.DateField()
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "Marenqi"

class jiuzi(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    count = models.CharField(max_length=30)
    xingjiabistar = models.CharField(max_length=30)
    jingsestar = models.CharField(max_length=30)
    quweistar = models.CharField(max_length=30)
    comment = models.CharField(max_length=1500)
    shijian = models.DateField()
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "jiuzi"

class dongfang(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    count = models.CharField(max_length=30)
    xingjiabistar = models.CharField(max_length=30)
    jingsestar = models.CharField(max_length=30)
    quweistar = models.CharField(max_length=30)
    comment = models.CharField(max_length=1500)
    shijian = models.DateField()
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "Dongfang"


class seapark(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    count = models.CharField(max_length=30)
    xingjiabistar = models.CharField(max_length=30)
    jingsestar = models.CharField(max_length=30)
    quweistar = models.CharField(max_length=30)
    comment = models.CharField(max_length=1500)
    shijian = models.DateField()
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "Seapark"

class wdcloud(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "Wdclouds"

class posneg(models.Model):
    nums= models.CharField(max_length=30)
    class Meta:
        db_table = "Posneg"

class imagehrefs(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'imagehrefs'
class imagelabels(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'imagelabels'
class menghuanhrefs(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'menghuanhrefs'
class menghuanlabels(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'menghuanlabels'
class dongfanghrefs(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'dongfanghrefs'
class dongfanglabels(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'dongfanglabels'
class seaparkhrefs(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'seaparkhrefs'
class seaparklabels(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'seaparklabels'
class marenhrefs(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'marenhrefs'
class marenlabels(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'marenlabels'
class jiuzihrefs(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'jiuzihrefs'
class jiuzilabels(models.Model):
    hrefs=models.CharField(max_length=200)

    class Meta:
        db_table = 'jiuzilabels'

class menghuannums(models.Model):
    nums=models.CharField(max_length=50)

    class Meta:
        db_table = 'menghuannums'


class dongfangnums(models.Model):
    nums = models.CharField(max_length=50)

    class Meta:
        db_table = 'dongfangnums'


class seaparknums(models.Model):
    nums = models.CharField(max_length=50)

    class Meta:
        db_table = 'seaparknums'


class marenqinums(models.Model):
    nums = models.CharField(max_length=50)

    class Meta:
        db_table = 'marenqinums'
class jiuzinums(models.Model):
    nums = models.CharField(max_length=50)

    class Meta:
        db_table = 'jiuzinums'

class keywordnums(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()


    class Meta:
        db_table = 'keywordums'
class dongfangtimes(models.Model):
    count = models.CharField(max_length=50)
    class Meta:
        db_table = 'dongfangtimes'
class menghuantimes(models.Model):
    count = models.CharField(max_length=50)
    class Meta:
        db_table = 'menghuantimes'
class jiuzitimes(models.Model):
    count = models.CharField(max_length=50)
    class Meta:
        db_table = 'jiuzitimes'
class seaparktimes(models.Model):
    count = models.CharField(max_length=50)
    class Meta:
        db_table = 'seaparktimes'
class marenqitimes(models.Model):
    count = models.CharField(max_length=50)
    class Meta:
        db_table = 'marenqitimes'


class posneg_shijian(models.Model):
    nums= models.CharField(max_length=30)
    shijian=models.DateField()
    class Meta:
        db_table = "Posneg_shijian"

class pingfen(models.Model):
    nums = models.CharField(max_length=30)
    class Meta:
        db_table = 'pingfen'

class imageposition(models.Model):
    nums = models.CharField(max_length=30)
    class Meta:
        db_table = 'imageposition'

class dongfangdegrees(models.Model):
    degrees = models.CharField(max_length=30)
    class Mtea:
        db_table = 'dongfangdegrees'
class menghuandegrees(models.Model):
    degrees = models.CharField(max_length=30)
    class Mtea:
        db_table = 'menghuandegrees'
class jiuzidegrees(models.Model):
    degrees = models.CharField(max_length=30)
    class Mtea:
        db_table = 'jiuzidegrees'
class marenqidegrees(models.Model):
    degrees = models.CharField(max_length=30)
    class Mtea:
        db_table = 'marenqidegrees'
class seaparkdegrees(models.Model):
    degrees = models.CharField(max_length=30)
    class Mtea:
        db_table = 'seaparkdegrees'

class sexs(models.Model):
    sexs = models.CharField(max_length=30)
    class Mtea:
        db_table = 'sexs'
class dongfangsexs(models.Model):
    sexs = models.CharField(max_length=30)
    class Mtea:
        db_table = 'dongfangsexs'
class menghuansexs(models.Model):
    sexs = models.CharField(max_length=30)
    class Mtea:
        db_table = 'menghuansexs'
class marenqisexs(models.Model):
    sexs = models.CharField(max_length=30)
    class Mtea:
        db_table = 'marenqisexs'
class seaparksexs(models.Model):
    sexs = models.CharField(max_length=30)
    class Mtea:
        db_table = 'seaparksexs'
class jiuzisexs(models.Model):
    sexs = models.CharField(max_length=30)
    class Mtea:
        db_table = 'jiuzisexs'

class allimagecaption(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "allimagecaption"
class dongfangimagecaption(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "dongfangimagecaption"

class menghuanimagecaption(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "menghuanimagecaption"

class jiuziimagecaption(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "jiuziimagecaption"

class marenqiimagecaption(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "marenqiimagecaption"
class seaparkimagecaption(models.Model):
    words = models.CharField(max_length=30)
    count = models.IntegerField()

    class Meta:
        db_table = "seaparkimagecaption"

class meituangeneral(models.Model):
    username = models.CharField(max_length=30)
    userimage = models.CharField(max_length=200)
    comment = models.CharField(max_length=1500)
    xiaofei = models.CharField(max_length=30)
    liulan = models.CharField(max_length=30)
    shijian = models.DateField()
    zan = models.CharField(max_length=30)
    labels = models.CharField(max_length=30)

    class Meta:
        db_table = "meituangeneral"

class oneseason(models.Model):
    count = models.CharField(max_length=30)

    class Meta:
        db_table = "oneseason"


class twoseason(models.Model):
    count = models.CharField(max_length=30)

    class Meta:
        db_table = "twoseason"


class threeseason(models.Model):
    count = models.CharField(max_length=30)

    class Meta:
        db_table = "threeseason"


class fourseason(models.Model):
    count = models.CharField(max_length=30)

    class Meta:
        db_table = "fourseason"

class huanlescore(models.Model):
    count = models.CharField(max_length=30)

    class Meta:
        db_table = "huanlescore"

class ldanums(models.Model):
    count = models.CharField(max_length=30)
    words = models.CharField(max_length=30)

    class Meta:
        db_table = "ldanums"

class imagess(models.Model):
    hrefs = models.CharField(max_length=300)
    titles = models.CharField(max_length=300)

    class Meta:
        db_table = "imagess"

class caption2(models.Model):
    words1 = models.CharField(max_length=30)

    class Meta:
        db_table = "caption2"







