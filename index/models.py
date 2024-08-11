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
    scbzj = models.BooleanField(validators=[MinValueValidator(0), MaxValueValidator(2)])
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
    zswp1 = models.BooleanField()
    zswp2 = models.BooleanField()
    zswp3 = models.BooleanField()
    zswp4 = models.BooleanField()
    zswp5 = models.BooleanField()
    zswp6 = models.BooleanField()
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
    csyp1 = models.BooleanField()
    csyp2 = models.BooleanField()
    csyp3 = models.BooleanField()
    csyp4 = models.BooleanField()

    wz1 = models.BooleanField()
    wz2 = models.BooleanField()
    wz3 = models.BooleanField()
    wz4 = models.BooleanField()
    shoes1 = models.BooleanField()
    shoes2 = models.BooleanField()
    shoes3 = models.BooleanField()
    shoes4 = models.BooleanField()
    cxzw1 = models.BooleanField()
    cxzw2 = models.BooleanField()
    cxzw3 = models.BooleanField()
    cxzw4 = models.BooleanField()

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
    fzxsy = models.BooleanField()
    szb = models.BooleanField()
    mb = models.BooleanField()
    scjh = models.BigIntegerField(null=False,blank=False,validators=[MinValueValidator(0), MaxValueValidator(2)])
    scsz = models.BigIntegerField(null=False,blank=False,validators=[MinValueValidator(0), MaxValueValidator(2)])
    mjxg = models.BooleanField()
    ywls = models.BooleanField()
    mt = models.BooleanField()
    tb = models.BooleanField()
    ljt = models.BooleanField()
    ljtlj = models.BooleanField()
    wsjxsdk = models.BooleanField()
    xsdksz = models.BooleanField()
    qjby = models.BooleanField()
    wsjdmzw = models.BooleanField()
    wsjmf = models.BigIntegerField()
    wsjdmgz = models.BooleanField()
    wsjqgt = models.BooleanField()
    wsjdd = models.BooleanField()
    
    #F类扣分
    zlzw = models.BooleanField()
    ctzlcjh = models.BigIntegerField()
    ckzlcjh = models.BigIntegerField()
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
    instance.score = Decimal(9.0) - Decimal(0.2)*(instance.ctjh + instance.ctzw + instance.ckjh + instance.ccjh + instance.scbzj + instance.mjh + instance.blct + instance.blbzj + instance.mc)