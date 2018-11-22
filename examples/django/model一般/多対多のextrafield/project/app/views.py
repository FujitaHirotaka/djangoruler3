from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from .models import Player, Team, Membership
d=z()
d["mode"]="index"

def index(request):
    Player.objects.all().delete()
    Team.objects.all().delete()
    Membership.objects.all().delete()
    maru=Player.objects.create(name="丸佳浩")
    kikuchi=Player.objects.create(name="菊池涼介")
    sugano=Player.objects.create(name="菅野智之")
    sakamoto=Player.objects.create(name="坂本勇人")    
    giants=Team.objects.create(name="巨人")
    carp=Team.objects.create(name="広島")
    giants_sugano= Membership.objects.create(player=sugano, team=giants, relationship="初期所属球団")
    giants_sakamoto=Membership.objects.create(player=sakamoto, team=giants, relationship="初期所属球団")
    giants_maru=Membership.objects.create(player=maru, team=giants, relationship="2019に広島から移籍して入団した球団")    
    carp_maru=Membership.objects.create(player=maru, team=carp, relationship="初期所属球団。2019に退団")    
    carp_kikuchi=Membership.objects.create(player=kikuchi, team=carp, relationship="初期所属球団")  
    print(carp.name)
    print(carp.players.all())
    #extra（中間）fieldであるmembershipがplayerの属性になっているかのようにふるまう。（検索時のみ）
    #ただし、player.membershipなどとはできない。これは複数の関係性があり、属性を一意に特定できないから。
    print(Player.objects.filter(membership__relationship="初期所属球団"))
    print(Player.objects.filter(membership__relationship="初期所属球団", membership__player__name="坂本勇人"))
    print(Player.objects.filter(membership__team__name="巨人", membership__relationship="初期所属球団"))    
    print(Player.objects.filter(membership__team__name="広島",membership__relationship="初期所属球団。2019に退団"))
    d["player_list"]=Player.objects.all()
    d["team_list"]=Team.objects.all()
    d["membership_list"]=Membership.objects.all()

    
    return render(request, "app/index.html", d)

