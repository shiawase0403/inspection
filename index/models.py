from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

import django.utils.timezone as timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20,null=True,blank=True)
    grade = models.BigIntegerField(null=True,blank=True)
    #hireDate = models.DateField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '人员信息'
        verbose_name_plural = '人员信息'


class Dorminspect(models.Model):
    #A类扣分
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(PersonInfo,on_delete=models.CASCADE)
    room = models.CharField(max_length=10)
    ctjh = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    ctzw = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    ckjh = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    ccjh = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    scbzj = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    mjh = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    blct = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])
    blbzj = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    mc = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    cl = models.BooleanField()

    #B类扣分
    zszw1 = models.BooleanField()
    zszw2 = models.BooleanField()
    zszw3 = models.BooleanField()
    zszw4 = models.BooleanField()
    zszw5 = models.BooleanField()
    zszw6 = models.BooleanField()
    zswp = models.BooleanField()
    sjzw1 = models.BooleanField()
    sjzw2 = models.BooleanField()
    sjzw3 = models.BooleanField()
    sjzw4 = models.BooleanField()
    sjzw5 = models.BooleanField()
    sjzw6 = models.BooleanField()
    cmwgj1 = models.BooleanField()
    cmwgj2 = models.BooleanField()
    cmwgj3 = models.BooleanField()
    cmwgj4 = models.BooleanField()
    cmwgj5 = models.BooleanField()
    cmwgj6 = models.BooleanField()
    yz1 = models.BooleanField()
    yz2 = models.BooleanField()
    yz3 = models.BooleanField()
    yz4 = models.BooleanField()
    yz5 = models.BooleanField()
    yz6 = models.BooleanField()
    ct1 = models.BooleanField()
    ct2 = models.BooleanField()
    ct3 = models.BooleanField()
    ct4 = models.BooleanField()
    ct5 = models.BooleanField()
    ct6 = models.BooleanField()
    yzzw1 = models.BooleanField()
    yzzw2 = models.BooleanField()
    yzzw3 = models.BooleanField()
    yzzw4 = models.BooleanField()
    yzzw5 = models.BooleanField()
    yzzw6 = models.BooleanField()
    cmbzj1 = models.BooleanField()
    cmbzj2 = models.BooleanField()
    cmbzj3 = models.BooleanField()
    cmbzj4 = models.BooleanField()
    cmbzj5 = models.BooleanField()
    cmbzj6 = models.BooleanField()
    cmgt1 = models.BooleanField()
    cmgt2 = models.BooleanField()
    cmgt3 = models.BooleanField()
    cmgt4 = models.BooleanField()
    cmgt5 = models.BooleanField()
    cmgt6 = models.BooleanField()


    #C类扣分
    cszw1 = models.BooleanField()
    cszw2 = models.BooleanField()
    cszw3 = models.BooleanField()
    cszw4 = models.BooleanField()
    cszw5 = models.BooleanField(null=True,blank=True)
    cszw6 = models.BooleanField(null=True,blank=True)
    csyp1 = models.BooleanField()
    csyp2 = models.BooleanField()
    csyp3 = models.BooleanField()
    csyp4 = models.BooleanField()
    csyp5 = models.BooleanField(null=True,blank=True)
    csyp6 = models.BooleanField(null=True,blank=True)

    wz1 = models.BooleanField()
    wz2 = models.BooleanField()
    wz3 = models.BooleanField()
    wz4 = models.BooleanField()
    wz5 = models.BooleanField(null=True,blank=True)
    wz6 = models.BooleanField(null=True,blank=True)
    shoes1 = models.BooleanField()
    shoes2 = models.BooleanField()
    shoes3 = models.BooleanField()
    #shoes4 = models.BooleanField()
    cxzw1 = models.BooleanField()
    cxzw2 = models.BooleanField()
    cxzw3 = models.BooleanField()
    #cxzw4 = models.BooleanField()

    #D类扣分
    dmbzj = models.BooleanField()
    wjdq = models.BigIntegerField()
    szbj = models.BooleanField()
    bjlj = models.BooleanField()
    szjh = models.BooleanField()
    dqwg = models.BooleanField()
    lpbzq = models.BooleanField()
    lpzw = models.BooleanField()
    lpjzw = models.BooleanField()
    qj = models.BooleanField()
    kgczjh = models.BooleanField()
    gyss = models.BooleanField()
    xlx = models.BooleanField()
    qsgt = models.BigIntegerField()
    wsmf = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    #E类扣分
    stbgj = models.BooleanField()
    styzw = models.BooleanField()
    szb = models.BooleanField()
    scjh = models.BigIntegerField(null=False,blank=False,validators=[MinValueValidator(0), MaxValueValidator(2)])
    scsz = models.BigIntegerField(null=False,blank=False,validators=[MinValueValidator(0), MaxValueValidator(2)])
    mjxg = models.BooleanField()
    ywls = models.BooleanField()
    mt = models.BooleanField()
    tb = models.BooleanField()
    ljt = models.BooleanField()
    ljtlj = models.BooleanField()
    wsjxsdk = models.BigIntegerField(null=False,blank=False,validators=[MinValueValidator(0), MaxValueValidator(2)])
    qjby = models.BooleanField()
    wsjdmzw = models.BooleanField()
    wsjmf = models.BigIntegerField()
    wsjdmgz = models.BooleanField()
    ysqbbgj = models.BooleanField()
    ysdbbgj = models.BooleanField()
    wsjqgt = models.BooleanField()
    wsjdd = models.BooleanField()

    #F类扣分
    zlzw = models.BooleanField()
    zldd = models.BooleanField()
    zlmf = models.BooleanField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    #计算字段
    score = models.DecimalField(editable=False,blank=True,null=True,default=9.00,max_digits=10,decimal_places=3)
    add_date = models.DateTimeField('保存日期',default = timezone.now)

    #@property
    #def score(self):
    #    return self.score - self.ctjh





    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '纪检信息'
        verbose_name_plural = '纪检信息'

@receiver(pre_save,sender=Dorminspect)
def calculate_score(sender,instance,**kwargs):
    instance.score = Decimal(9.0) - Decimal(0.1)*(instance.ctjh + instance.ctzw + instance.ckjh + instance.ccjh + instance.scbzj + instance.mjh + instance.blct + instance.blbzj + instance.mc + instance.wsmf + instance.scjh + instance.scsz + instance.wsjxsdk + instance.wjdq + instance.qsgt + instance.wsjmf + instance.zlmf) - Decimal(0.1)*(int(instance.zszw1) + int(instance.zszw2) + int(instance.zszw3) + int(instance.zszw4) + int(instance.zszw5) + int(instance.zszw6) + int(instance.sjzw1) + int(instance.sjzw2) + int(instance.sjzw3) + int(instance.sjzw4) + int(instance.sjzw5) + int(instance.sjzw6) + int(instance.cmwgj1) + int(instance.cmwgj2) + int(instance.cmwgj3) + int(instance.cmwgj4) + int(instance.cmwgj5) + int(instance.cmwgj6) + int(instance.yz1) + int(instance.yz2) + int(instance.yz3) + int(instance.yz4) + int(instance.yz5) + int(instance.yz6) + int(instance.ct1) + int(instance.ct2) + int(instance.ct3) + int(instance.ct4) + int(instance.ct5) + int(instance.ct6) + int(instance.yzzw1) + int(instance.yzzw2) + int(instance.yzzw3) + int(instance.yzzw4) + int(instance.yzzw5) + int(instance.yzzw6) + int(instance.cmbzj1) + int(instance.cmbzj2) + int(instance.cmbzj3) + int(instance.cmbzj4) + int(instance.cmbzj5) + int(instance.cmbzj6) + int(instance.cmgt1) + int(instance.cmgt2) + int(instance.cmgt3) + int(instance.cmgt4) + int(instance.cmgt5) + int(instance.cmgt6) + int(instance.cszw1) + int(instance.cszw2) + int(instance.cszw3) + int(instance.cszw4) + int(instance.cszw5) + int(instance.cszw6) + int(instance.csyp1) + int(instance.csyp2) + int(instance.csyp3) + int(instance.csyp4) + int(instance.csyp5) + int(instance.csyp6) + int(instance.wz1) + int(instance.wz2) + int(instance.wz3) + int(instance.wz4) + int(instance.wz5) + int(instance.wz6) + int(instance.shoes1) + int(instance.shoes2) + int(instance.shoes3) + int(instance.cxzw1) + int(instance.cxzw2) + int(instance.cxzw3)) - Decimal(0.2)*(int(instance.cl) + int(instance.zswp) + int(instance.dmbzj) + int(instance.szbj) + int(instance.bjlj) + int(instance.szjh) + int(instance.dqwg) + int(instance.lpbzq) + int(instance.lpzw) + int(instance.lpjzw) + int(instance.qj) + int(instance.kgczjh) + int(instance.gyss) + int(instance.xlx) + int(instance.stbgj) + int(instance.styzw) + int(instance.szb) + int(instance.mjxg) + int(instance.ywls) + int(instance.mt) + int(instance.tb) + int(instance.ljt) + int(instance.ljtlj) + int(instance.wsjdmzw) + int(instance.wsjdmgz) + int(instance.ysqbbgj) + int(instance.ysdbbgj) + int(instance.qjby) + int(instance.wsjqgt) + int(instance.wsjdd) + int(instance.zlzw) + int(instance.zldd))