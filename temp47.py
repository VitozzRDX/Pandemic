import pygame,sys ,os,random,math,time
from pygame.locals import *

pygame.init()

Action_Number=0
num_of_Player=0   # Nomer igroka, not chislo igrokov
number_of_Player=4   # A vot eto chislo igrokov !
num_of_Player_2=0   #schetchik till next player
if number_of_Player>2:
    num_hand_card=2
else :
    num_hand_card=4
List_of_city_w_Lab=[]
List_Of_Fishki=[]
list_of_citiez=[]
list_of_buttonz=[]
list_of_rectangz=[]
List_of_Cardz_Citiez=[]
List_of_CardzofInfection=[]
List_of_CardzofInfection_Trash=[]
List_of_CardzofInfection_Trash_Copy=[]
List_of_played_CoInf=[]
List_of_EpidCardz=[]
List_of_Deseased_Citiez=[]
List_to_see_Epid_card=[]
List_to_see_SE_card=[]
List_to_see_SE_card_only_in_game=[]
List_of_CoInf_to_infect=[]
Images_of_List_of_CoInf_to_infect=[]
clock = pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
WINDOWWIDTH = 1366#1680
WINDOWHEIGHT =768#1050
mousex, mousey=0,0
wait_time=10
stage_of_blinkin_button=1
some_strange_var=0
flag_to_show_SE_button=None
instruction=None
action=None
choosenfishka=None
ssss=None
ssss2=None
ssss3=None
ssss4=None
Check_Hand_len=False
image_of_IO_number_variable=None
number_of_virus_in_city=None
Virus_Red='Virus_Red'
Virus_Green='Virus_Green'
Virus_Violet='Virus_Violet'
Virus_Black='Virus_Black'

NumberOfVirusRed,NumberOfVirusBlack,NumberOfVirusGreen,NumberOfVirusViolet=(24,24,24,24)

LevelGame=5

List_of_CoInf_coord=[(1500,180),(1500,260),(1500,340),(1500,420),(1500,500),(1500,580),(1500,660),(1500,740),(1500,820)]

List_of_free_coord_for_Trash=[(400,140),(570,140),(740,140),(910,140),(1080,140),(1250,140),\
                                    (400,205),(570,205),(740,205),(910,205),(1080,205),(1250,205),\
                                    (400,270),(570,270),(740,270),(910,270),(1080,270),(1250,270)]

List_of_tic_coor1=[(50,969),(220,969),(390,969),(560,969),(730,969),(900,969),(1070,969),(1250,969),(1420,969)]
List_of_tic_coor2=[(50,904),(220,904),(390,904),(560,904),(730,904),(900,904),(1070,904),(1250,904),(1420,904)]
List_of_tic_coor3=[(50,839),(220,839),(390,839),(560,839),(730,839),(900,839),(1070,839),(1250,839),(1420,839)]
List_of_tic_coor4=[(50,774),(220,774),(390,774),(560,774),(730,774),(900,774),(1070,774),(1250,774),(1420,774)]

List_of_coord_for_CV_fishka=[(30,400),(30,498),(30,598),(30,700)]

List_of_all_free_coord_for_tics=[List_of_tic_coor1,List_of_tic_coor2,List_of_tic_coor3,List_of_tic_coor4]

List_of_free_coord_for_SECardz=[(1450,200),(1450,270),(1450,340),(1450,410)]

List_of_coord_for_ROI_fishka=[(971,912),(1041,912),(1113,912),(1188,912),(1262,912),(1339,912),(1416,912)]#1041 1113 1188 1262 1339 1416
List_of_ROI=[2,2,2,3,3,4,4]
ROI=0
ROI_number=List_of_ROI[ROI]
List_of_coord_for_card_to_infect=[(610,30),(780,30),(950,30),(1120,30)]

screen=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN|pygame.DOUBLEBUF,32)
#screen=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

cityboard_image=pygame.image.load(os.path.join('imag','cityboard.png'))
scientist_board_image=pygame.image.load(os.path.join('imag','boardtoscient.png'))

cardofinf=pygame.image.load(os.path.join('imag','cardofinfBei.png'))
cardofinf2=pygame.image.load(os.path.join('imag','cardofinfJak.png'))

cardofinfAlg=pygame.image.load(os.path.join('imag','cardofinfAlg.png'))

image_of_epid_card=pygame.image.load(os.path.join('imag','epid.png'))

image_of_IO_number_8=pygame.image.load(os.path.join('imag','image_of_IO_number_8.png'))
image_of_IO_number_7=pygame.image.load(os.path.join('imag','image_of_IO_number_7.png'))
image_of_IO_number_6=pygame.image.load(os.path.join('imag','image_of_IO_number_6.png'))
image_of_IO_number_5=pygame.image.load(os.path.join('imag','image_of_IO_number_5.png'))
image_of_IO_number_4=pygame.image.load(os.path.join('imag','image_of_IO_number_4.png'))
image_of_IO_number_3=pygame.image.load(os.path.join('imag','image_of_IO_number_3.png'))
image_of_IO_number_2=pygame.image.load(os.path.join('imag','image_of_IO_number_2.png'))
image_of_IO_number_1=pygame.image.load(os.path.join('imag','image_of_IO_number_1.png'))
image_of_IO_number_last=pygame.image.load(os.path.join('imag','image_of_IO_number_last.png'))

IO_NYTimes=pygame.image.load(os.path.join('imag','IO_NYTimes.png'))

image_of_CV_scale=pygame.image.load(os.path.join('imag','CV_scale.png'))
image_of_CV_fishka_red=pygame.image.load(os.path.join('imag','CV_fishka_red.png'))
image_of_CV_fishka_black=pygame.image.load(os.path.join('imag','CV_fishka_black.png'))
image_of_CV_fishka_green=pygame.image.load(os.path.join('imag','CV_fishka_green.png'))
image_of_CV_fishka_violet=pygame.image.load(os.path.join('imag','CV_fishka_violet.png'))

List_of_CV_images=[]

image_of_fishka_growing_rate_of_infection=pygame.image.load(os.path.join('imag','fishka_growing_rate_of_infection.png'))
image_of_growing_rate_of_infection=pygame.image.load(os.path.join('imag','growing_rate_of_infection.png'))

List_of_IO_numbers=[image_of_IO_number_8,image_of_IO_number_7,image_of_IO_number_6,image_of_IO_number_5,\
                    image_of_IO_number_4,image_of_IO_number_3,image_of_IO_number_2,image_of_IO_number_1,\
                    image_of_IO_number_last]
image_of_Second_wave=pygame.image.load(os.path.join('imag','Second_wave.png'))
image_of_Yournewticz=pygame.image.load(os.path.join('imag','Yournewticz.png'))
image_of_You_got=pygame.image.load(os.path.join('imag','You_got.png'))
image_of_In_city=pygame.image.load(os.path.join('imag','In_city.png'))
image_of_Warning=pygame.image.load(os.path.join('imag','Warning_Epid.png'))
image_of_Black_virus=pygame.image.load(os.path.join('imag','Black_virus.png'))
image_of_Red_virus=pygame.image.load(os.path.join('imag','Red_virus.png'))
image_of_Green_virus=pygame.image.load(os.path.join('imag','Green_virus.png'))
image_of_Violet_virus=pygame.image.load(os.path.join('imag','Violet_virus.png'))
image_of_Spreading=pygame.image.load(os.path.join('imag','Spreading_of_Infection.png'))
image_of_No_virus_in_city=pygame.image.load(os.path.join('imag','There_is_no_virus.png'))
image_of_Choose_virus=pygame.image.load(os.path.join('imag','Chose virus to cure.png'))
image_of_Choose_city_to_remove_Lab=pygame.image.load(os.path.join('imag','Choose_city_to_remove_Lab.png'))
image_of_Choose_fishka_to_move=pygame.image.load(os.path.join('imag','Choose_fishka_to_move.png'))
image_of_Choose_city_to_move=pygame.image.load(os.path.join('imag','Choose_city_to_move.png'))

image_of_RedVirus_picture=pygame.image.load(os.path.join('imag','RedVirus.png'))
image_of_BlackVirus_picture=pygame.image.load(os.path.join('imag','BlackVirus.png'))
image_of_GreenVirus_picture=pygame.image.load(os.path.join('imag','GreenVirus.png'))
image_of_VioletVirus_picture=pygame.image.load(os.path.join('imag','VioletVirus.png'))

image_of_Board_for_Virusez=pygame.image.load(os.path.join('imag','Board for Virusez.png'))
image_for_fishkaboard=pygame.image.load(os.path.join('imag','fishkaboard.png'))

dict_of_virusez={Virus_Red:(image_of_RedVirus_picture,image_of_RedVirus_picture.get_rect(topleft=(700,30)),(700,30)),\
                 Virus_Black:(image_of_BlackVirus_picture,image_of_BlackVirus_picture.get_rect(topleft=(800,30)),(800,30)),\
                 Virus_Green:(image_of_GreenVirus_picture,image_of_GreenVirus_picture.get_rect(topleft=(900,30)),(900,30)),\
                 Virus_Violet:(image_of_VioletVirus_picture,image_of_VioletVirus_picture.get_rect(topleft=(1000,30)),(1000,30))}

image_of_Lab=pygame.image.load(os.path.join('imag','Lab.png'))

image_of_virus_red_1=pygame.image.load(os.path.join('imag','path5209.png'))
image_of_virus_red_2=pygame.image.load(os.path.join('imag','path5211.png'))
image_of_virus_red_3=pygame.image.load(os.path.join('imag','path5213.png'))
image_of_virus_green_3=pygame.image.load(os.path.join('imag','path5056.png'))
image_of_virus_green_1=pygame.image.load(os.path.join('imag','path5052.png'))
image_of_virus_green_2=pygame.image.load(os.path.join('imag','path5054.png'))
image_of_virus_violet_3=pygame.image.load(os.path.join('imag','path5142.png'))
image_of_virus_violet_1=pygame.image.load(os.path.join('imag','path5138.png'))
image_of_virus_violet_2=pygame.image.load(os.path.join('imag','path5140.png'))
image_of_virus_black_3=pygame.image.load(os.path.join('imag','path4225.png'))
image_of_virus_black_1=pygame.image.load(os.path.join('imag','path4227.png'))
image_of_virus_black_2=pygame.image.load(os.path.join('imag','path4229.png'))

ticketAlg=pygame.image.load(os.path.join('imag','ticketAlg.png'))
ticketAtl=pygame.image.load(os.path.join('imag','ticketAtl.png'))
ticketBag=pygame.image.load(os.path.join('imag','ticketBag.png'))
ticketBang=pygame.image.load(os.path.join('imag','ticketBang.png'))
ticketBeij=pygame.image.load(os.path.join('imag','ticketBeij.png'))
ticketBog=pygame.image.load(os.path.join('imag','ticketBog.png'))
ticketBuen=pygame.image.load(os.path.join('imag','ticketBuen.png'))
ticketCai=pygame.image.load(os.path.join('imag','ticketCai.png'))
ticketChe=pygame.image.load(os.path.join('imag','ticketChe.png'))

ticketChic=pygame.image.load(os.path.join('imag','ticketChic.png'))
ticketDel=pygame.image.load(os.path.join('imag','ticketDel.png'))
ticketErr=pygame.image.load(os.path.join('imag','ticketErr.png'))
ticketEss=pygame.image.load(os.path.join('imag','ticketEss.png'))
ticketFris=pygame.image.load(os.path.join('imag','ticketFris.png'))
ticketHoch=pygame.image.load(os.path.join('imag','ticketHoch.png'))
ticketHong=pygame.image.load(os.path.join('imag','ticketHong.png'))
ticketJak=pygame.image.load(os.path.join('imag','ticketJak.png'))
ticketJoh=pygame.image.load(os.path.join('imag','ticketJoh.png'))

ticketKar=pygame.image.load(os.path.join('imag','ticketKar.png'))
ticketKhar=pygame.image.load(os.path.join('imag','ticketKhar.png'))
ticketKinsh=pygame.image.load(os.path.join('imag','ticketKinsh.png'))
ticketKol=pygame.image.load(os.path.join('imag','ticketKol.png'))
ticketLA=pygame.image.load(os.path.join('imag','ticketLA.png'))
ticketLag=pygame.image.load(os.path.join('imag','ticketLag.png'))
ticketLim=pygame.image.load(os.path.join('imag','ticketLim.png'))
ticketLon=pygame.image.load(os.path.join('imag','ticketLon.png'))
ticketMad=pygame.image.load(os.path.join('imag','ticketMad.png'))
ticketMan=pygame.image.load(os.path.join('imag','ticketMan.png'))
ticketMex=pygame.image.load(os.path.join('imag','ticketMex.png'))

ticketMiam=pygame.image.load(os.path.join('imag','ticketMiam.png'))
ticketMil=pygame.image.load(os.path.join('imag','ticketMil.png'))
ticketMos=pygame.image.load(os.path.join('imag','ticketMos.png'))
ticketMumb=pygame.image.load(os.path.join('imag','ticketMumb.png'))
ticketNew=pygame.image.load(os.path.join('imag','ticketNew.png'))
ticketOsa=pygame.image.load(os.path.join('imag','ticketOsa.png'))
ticketPar=pygame.image.load(os.path.join('imag','ticketPar.png'))

ticketSan=pygame.image.load(os.path.join('imag','ticketSan.png'))
ticketSanp=pygame.image.load(os.path.join('imag','ticketSanp.png'))
ticketSeol=pygame.image.load(os.path.join('imag','ticketSeol.png'))
ticketShan=pygame.image.load(os.path.join('imag','ticketShan.png'))
ticketSPb=pygame.image.load(os.path.join('imag','ticketSPb.png'))
ticketSta=pygame.image.load(os.path.join('imag','ticketSta.png'))
ticketSyd=pygame.image.load(os.path.join('imag','ticketSyd.png'))
ticketTai=pygame.image.load(os.path.join('imag','ticketTai.png'))

ticketTeh=pygame.image.load(os.path.join('imag','ticketTeh.png'))
ticketTok=pygame.image.load(os.path.join('imag','ticketTok.png'))
ticketTor=pygame.image.load(os.path.join('imag','ticketTor.png'))
ticketWash=pygame.image.load(os.path.join('imag','ticketWash.png'))

ticketSEEmergency=pygame.image.load(os.path.join('imag','SEEmergency.png'))
ticketSEGoodNight=pygame.image.load(os.path.join('imag','SEGoodNight.png'))
ticketSEGovermentGrant=pygame.image.load(os.path.join('imag','SEGovermentGrant.png'))
ticketSEImmunity=pygame.image.load(os.path.join('imag','SEImmunity.png'))

CardzofInf_image_Alg=pygame.image.load(os.path.join('imag','cardofinfAlg.png'))
CardzofInf_image_Atl=pygame.image.load(os.path.join('imag','cardofinfAtl.png'))
CardzofInf_image_Bag=pygame.image.load(os.path.join('imag','cardofinfBag.png'))
CardzofInf_image_Bang=pygame.image.load(os.path.join('imag','cardofinfBan.png'))
CardzofInf_image_Beij=pygame.image.load(os.path.join('imag','cardofinfBei.png'))
CardzofInf_image_Bog=pygame.image.load(os.path.join('imag','cardofinfBog.png'))
CardzofInf_image_Buen=pygame.image.load(os.path.join('imag','cardofinfBue.png'))
CardzofInf_image_Cai=pygame.image.load(os.path.join('imag','cardofinfCai.png'))
CardzofInf_image_Che=pygame.image.load(os.path.join('imag','cardofinfChen.png'))

CardzofInf_image_Chic=pygame.image.load(os.path.join('imag','cardofinfChic.png'))
CardzofInf_image_Del=pygame.image.load(os.path.join('imag','cardofinfDel.png'))
CardzofInf_image_Err=pygame.image.load(os.path.join('imag','cardofinfErR.png'))
CardzofInf_image_Ess=pygame.image.load(os.path.join('imag','cardofinfEss.png'))
CardzofInf_image_Fris=pygame.image.load(os.path.join('imag','cardofinfFris.png'))
CardzofInf_image_Hoch=pygame.image.load(os.path.join('imag','cardofinfHoch.png'))
CardzofInf_image_Hong=pygame.image.load(os.path.join('imag','cardofinfHon.png'))
CardzofInf_image_Jak=pygame.image.load(os.path.join('imag','cardofinfJak.png'))
CardzofInf_image_Joh=pygame.image.load(os.path.join('imag','cardofinfJoh.png'))

CardzofInf_image_Kar=pygame.image.load(os.path.join('imag','cardofinfKar.png'))
CardzofInf_image_Khar=pygame.image.load(os.path.join('imag','cardofinfKhar.png'))
CardzofInf_image_Kinsh=pygame.image.load(os.path.join('imag','cardofinfKins.png'))
CardzofInf_image_Kol=pygame.image.load(os.path.join('imag','cardofinfKol.png'))
CardzofInf_image_LA=pygame.image.load(os.path.join('imag','cardofinfLA.png'))
CardzofInf_image_Lag=pygame.image.load(os.path.join('imag','cardofinfLag.png'))
CardzofInf_image_Lim=pygame.image.load(os.path.join('imag','cardofinfLima.png'))
CardzofInf_image_Lon=pygame.image.load(os.path.join('imag','cardofinfLon.png'))
CardzofInf_image_Mad=pygame.image.load(os.path.join('imag','cardofinfMad.png'))
CardzofInf_image_Man=pygame.image.load(os.path.join('imag','cardofinfMan.png'))
CardzofInf_image_Mex=pygame.image.load(os.path.join('imag','cardofinfMex.png'))

CardzofInf_image_Miam=pygame.image.load(os.path.join('imag','cardofinfMia.png'))
CardzofInf_image_Mil=pygame.image.load(os.path.join('imag','cardofinfMil.png'))
CardzofInf_image_Mos=pygame.image.load(os.path.join('imag','cardofinfMos.png'))
CardzofInf_image_Mumb=pygame.image.load(os.path.join('imag','cardofinfMum.png'))
CardzofInf_image_New=pygame.image.load(os.path.join('imag','cardofinfNew.png'))
CardzofInf_image_Osa=pygame.image.load(os.path.join('imag','cardofinfOsa.png'))
CardzofInf_image_Par=pygame.image.load(os.path.join('imag','cardofinfPari.png'))

CardzofInf_image_San=pygame.image.load(os.path.join('imag','cardofinfSan.png'))
CardzofInf_image_Sanp=pygame.image.load(os.path.join('imag','cardofinfSaP.png'))
CardzofInf_image_Seol=pygame.image.load(os.path.join('imag','cardofinfSeol.png'))
CardzofInf_image_Shan=pygame.image.load(os.path.join('imag','cardofinfShan.png'))
CardzofInf_image_SPb=pygame.image.load(os.path.join('imag','cardofinfSPb.png'))
CardzofInf_image_Sta=pygame.image.load(os.path.join('imag','cardofinfStan.png'))
CardzofInf_image_Syd=pygame.image.load(os.path.join('imag','cardofinfSyd.png'))
CardzofInf_image_Tai=pygame.image.load(os.path.join('imag','cardofinfTai.png'))

CardzofInf_image_Teh=pygame.image.load(os.path.join('imag','cardofinfTeh.png'))
CardzofInf_image_Tok=pygame.image.load(os.path.join('imag','cardofinfTok.png'))
CardzofInf_image_Tor=pygame.image.load(os.path.join('imag','cardofinfTor.png'))
CardzofInf_image_Wash=pygame.image.load(os.path.join('imag','cardofinfWash.png'))

ticketboard=pygame.image.load(os.path.join('imag','ticketboard.png'))
World_card=pygame.image.load(os.path.join('imag','drawing-1.png'))

fish_image=pygame.image.load(os.path.join('imag','fishkawshadow.png'))
fish_image2=pygame.image.load(os.path.join('imag','fishkadispwshad.png'))
fish_image3=pygame.image.load(os.path.join('imag','fishkabuilderwshadow.png'))
fish_image4=pygame.image.load(os.path.join('imag','fishkascientistwshadow.png'))
fish_image5=pygame.image.load(os.path.join('imag','fishkadoctorwshadow.png'))
fish_image6=pygame.image.load(os.path.join('imag','fishkasearcherwshad.png'))

flag_on_exchange=pygame.image.load(os.path.join('imag','flagtoexchange3.png'))
flag_on_exchange_PRESSED=pygame.image.load(os.path.join('imag','flagtoexchange2-1.png'))

dict_of_buttonz={'button of CardChange':[pygame.image.load(os.path.join('imag','icon1-4.png')),pygame.image.load(os.path.join('imag','icon1-10.png')),pygame.image.load(os.path.join('imag','icon1-13.png')),pygame.image.load(os.path.join('imag','icon1-13(2).png')),pygame.image.load(os.path.join('imag','icon1-13(3).png'))],\
                 'button of Curing':[pygame.image.load(os.path.join('imag','g5027.png')),pygame.image.load(os.path.join('imag','g5027-1.png')),pygame.image.load(os.path.join('imag','g5027-2.png')),pygame.image.load(os.path.join('imag','g5027-3.png')),pygame.image.load(os.path.join('imag','g5027-4.png'))],\
                 'button of Moving':[pygame.image.load(os.path.join('imag','move_to.png')),pygame.image.load(os.path.join('imag','move_to-1.png')),pygame.image.load(os.path.join('imag','move_to-2.png')),pygame.image.load(os.path.join('imag','move_to-3.png')),pygame.image.load(os.path.join('imag','move_to-4.png'))],\
                 'button of Build a Lab':[pygame.image.load(os.path.join('imag','build_lab.png')),pygame.image.load(os.path.join('imag','build_lab-1.png')),pygame.image.load(os.path.join('imag','build_lab-2.png')),pygame.image.load(os.path.join('imag','build_lab-3.png')),pygame.image.load(os.path.join('imag','build_lab-4.png'))],\
                 'button of Traveling':[pygame.image.load(os.path.join('imag','travel_to.png')),pygame.image.load(os.path.join('imag','travel_to-1.png')),pygame.image.load(os.path.join('imag','travel_to-2.png')),pygame.image.load(os.path.join('imag','travel_to-3.png')),pygame.image.load(os.path.join('imag','travel_to-4.png'))],\
                 'button of Cure Inventing':[pygame.image.load(os.path.join('imag','invent_cure.png')),pygame.image.load(os.path.join('imag','invent_cure-1.png')),pygame.image.load(os.path.join('imag','invent_cure-2.png')),pygame.image.load(os.path.join('imag','invent_cure-3.png')),pygame.image.load(os.path.join('imag','invent_cure-4.png'))],\
                 'button of Next Player':[pygame.image.load(os.path.join('imag','next_player.png')),pygame.image.load(os.path.join('imag','next_player-1.png')),pygame.image.load(os.path.join('imag','next_player.png')),pygame.image.load(os.path.join('imag','next_player.png')),pygame.image.load(os.path.join('imag','next_player.png'))],\
                 'button of From Lab To Lab':[pygame.image.load(os.path.join('imag','from_lab_to_lab-1.png')),pygame.image.load(os.path.join('imag','from_lab_to_lab.png')),pygame.image.load(os.path.join('imag','from_lab_to_lab-2.png')),pygame.image.load(os.path.join('imag','from_lab_to_lab-3.png')),pygame.image.load(os.path.join('imag','from_lab_to_lab-4.png'))],\
                 'button of Charter':[pygame.image.load(os.path.join('imag','charter.png')),pygame.image.load(os.path.join('imag','charter-1.png')),pygame.image.load(os.path.join('imag','charter-2.png')),pygame.image.load(os.path.join('imag','charter-3.png')),pygame.image.load(os.path.join('imag','charter-4.png'))],\
                 'button of OK !':[pygame.image.load(os.path.join('imag','ok.png')),pygame.image.load(os.path.join('imag','ok-1.png')),pygame.image.load(os.path.join('imag','ok.png')),pygame.image.load(os.path.join('imag','ok.png')),pygame.image.load(os.path.join('imag','ok.png'))],\
                 'button of SE':[pygame.image.load(os.path.join('imag','SE _button.png')),pygame.image.load(os.path.join('imag','SE _button-1.png')),pygame.image.load(os.path.join('imag','SE _button.png')),pygame.image.load(os.path.join('imag','SE _button.png')),pygame.image.load(os.path.join('imag','SE _button.png'))]}

#dict_of_buttonz={'button of Moving':[pygame.image.load(os.path.join('imag','g5027.png')),pygame.image.load(os.path.join('imag','g5027-1.png')),pygame.image.load(os.path.join('imag','g5027-2.png')),pygame.image.load(os.path.join('imag','g5027-3.png')),pygame.image.load(os.path.join('imag','g5027-4.png'))]}
dict_of_active_bz={}

status_of_ticket_in_hand_of_changer=None

def listmerge3(lstlst):
    ll=[]
    for lst in lstlst:
      ll.extend(lst)
    return ll

def terminate():
    pygame.quit()
    sys.exit()
def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)

class Button(object):
    def __init__(self,posx,posy,image,action):
        dict_of_active_bz[self]='active'
        self.action=action
        self.posx=posx
        self.posy=posy
        self.image=image[0]
        self.image_pressed=image[1]
        self.image_blinking1=image[2]
        self.image_blinking2=image[3]
        self.image_blinking3=image[4]
        self.rectang=image[0].get_rect(topleft=(posx,posy))
        list_of_buttonz.append(self)
    def get_position(self):
        return (self.posx,self.posy)
    def set_old_rectang(self):
        self.rectang=self.image.get_rect(topleft=(self.posx,self.posy))
    def get_rec(self):
        return self.rectang
    def click(self):
        global instruction
        instruction=None
        for fishka10 in List_Of_Fishki:
            fishka10.List_of_card_to_Cure=[]
        for card in fishka.hand :
            card.flag_on_coord=0
        #fishka.List_of_tic_flag=[0,0,0,0,0,0,0]
        fishka.List_of_tic_flag=[0,0,0,0,0,0,0,0,0]
        fishka.List_of_tic_coor=[(50,969),(220,969),(390,969),(560,969),(730,969),(900,969),(1070,969),(1250,969)]
        pygame.draw.rect(screen,white,self.rectang,0)
        screen.blit(self.image_pressed,self.get_position())
        pygame.display.update(self.rectang)
        #pygame.time.wait(150)
        #pygame.draw.rect(screen,white,self.rectang,0)
        for any_button in dict_of_active_bz :
            dict_of_active_bz[any_button]='active'
        dict_of_active_bz[self]='not active'
        return self.action

button1=Button(10,10,dict_of_buttonz['button of Moving'],'moving')
button2=Button(120,10,dict_of_buttonz['button of Traveling'],'travel to')
button3=Button(230,10,dict_of_buttonz['button of Charter'],'charter to')
button4=Button(340,10,dict_of_buttonz['button of Build a Lab'],'build a lab')
button5=Button(450,10,dict_of_buttonz['button of From Lab To Lab'],'travel FLtL')
button6=Button(560,10,dict_of_buttonz['button of Curing'],'cure')
button7=Button(670,10,dict_of_buttonz['button of Cure Inventing'],'invent cure')
button8=Button(780,10,dict_of_buttonz['button of CardChange'],'exchange card')
button9=Button(890,10,dict_of_buttonz['button of Next Player'],'Next Player')
button10=Button(1450,10,dict_of_buttonz['button of OK !'],'OK !')

class SEButton(Button):
    def __init__(self,posx,posy,image,action):
        self.action=action
        self.posx=posx
        self.posy=posy
        self.image=image[0]
        self.image_pressed=image[1]
        self.image_blinking1=image[2]
        self.image_blinking2=image[3]
        self.image_blinking3=image[4]
        self.rectang=image[0].get_rect(topleft=(posx,posy))


button11=Button(1560,10,dict_of_buttonz['button of SE'],'show SE')

def Box_to_add_Virusez (Number_of_Virus_X,List_of_Virusez,List_of_Virusez_X_counterz,List_of_Virusez_X,virus,Lizt,trigger_of_Infection_Spread,city):
    # print
    # print city
    # print Number_of_Virus_X
    if Number_of_Virus_X!=3:
        city.Change_up_Number_of_Virus(virus)

        #print Number_of_Virus_X
        for  i in range(3):
            if List_of_Virusez_X_counterz[i]==0:
                List_of_Virusez.append(List_of_Virusez_X[i])
                screen.fill(white)
                screen.blit(World_card,(0,0))
                show_all_buttonz()
                show_all_citiez()
                if starting:
                    for deseased_city in List_of_Deseased_Citiez :
                        screen.blit(cityboard_image,(deseased_city.x-7,deseased_city.y-7))
                show_all_ticketz()
                show_all_virusez()
                show_all_fishkas()
                show_all_CoInf()
                #screen.fill(white,(List_of_Virusez_X[i][0]).get_rect(topleft=(List_of_Virusez_X[i][1])))
                screen.blit((List_of_Virusez_X[i][0]),(List_of_Virusez_X[i][1]))
                #pygame.display.update((List_of_Virusez_X[i][0]).get_rect(topleft=(List_of_Virusez_X[i][1])))
                screen.blit(cityboard_image,(city.x-7,city.y-7))
                pygame.display.update()
                pygame.time.wait(450)
                List_of_Virusez_X_counterz[i]=1
                break

    elif Number_of_Virus_X==3 and city.return_trigger_of_Infection_Spread()==0:

        city.trigger_of_Infection_Spread_up()
        for neybour_city in Lizt:
            neybour_city.add_virus(virus)

def Box_to_remove_Virusez(virus,List_of_Virusez_X_counterz,List_of_Virusez_X,List_of_Virusez,city):
    city.Change_down_Number_of_Virus(virus)
    for i in range(2,-1,-1):
        if List_of_Virusez_X_counterz[i]!=0:
            List_of_Virusez.remove(List_of_Virusez_X[i])
            #screen.fill(white)
            screen.blit(World_card,(0,0))
            show_all_buttonz()
            show_all_citiez()
            show_all_ticketz()
            show_all_virusez()
            show_all_fishkas()
            show_all_CoInf()
            pygame.display.update()
            List_of_Virusez_X_counterz[i]=0
            break


class Citiez (object) :
    def __init__(self,image,x,y,name):
        self.name=name
        self.Lizt=[]                    # for neeghbourz ( it shoulbe Lizt of Neebour . but no
        self.image=(pygame.image.load(os.path.join('imag','city.png')))
        self.x=x-1
        self.y=y+9
        self.Lab=0
        self.List_for_Virusez=[]
        self.List_of_Virusez_Red=[(image_of_virus_red_1,(self.x+24,self.y+25.7)),(image_of_virus_red_2,(self.x+37,self.y+25.7)),(image_of_virus_red_3,(self.x+26,self.y+37))]
        self.List_of_Virusez_Green=[(image_of_virus_green_1,(self.x+15,self.y+16)),(image_of_virus_green_2,(self.x+36,self.y+16)),(image_of_virus_green_3,(self.x+19,self.y+43))]
        self.List_of_Virusez_Violet=[(image_of_virus_violet_1,(self.x+8,self.y+8)),(image_of_virus_violet_2,(self.x+37,self.y+8)),(image_of_virus_violet_3,(self.x+12,self.y+47))]
        self.List_of_Virusez_Black=[(image_of_virus_black_1,(self.x+0,self.y+1)),(image_of_virus_black_2,(self.x+37,self.y+1)),(image_of_virus_black_3,(self.x+6,self.y+50))]
        self.List_of_Virusez_Red_counterz=[0,0,0]
        self.List_of_Virusez_Green_counterz=[0,0,0]
        self.List_of_Virusez_Violet_counterz=[0,0,0]
        self.List_of_Virusez_Black_counterz=[0,0,0]
        self.Number_of_Virus_Red=0
        self.Number_of_Virus_Green=0
        self.Number_of_Virus_Violet=0
        self.Number_of_Virus_Black=0
        self.trigger_of_Infection_Spread=0               # it mean tht there was no inf.Spread this turn in this city
        self.freecoordx1=self.x-30
        self.freecoordy1=self.y-50
        self.freecoordx2=self.x+60
        self.freecoordy2=self.y+30
        self.freecoordx3=self.x-30
        self.freecoordy3=self.y+30
        self.freecoordx4=self.x+60
        self.freecoordy4=self.y-50
        self.rectang=image.get_rect(topleft=(x,y))
        # self.Dict_of_freecoord={(self.freecoordx1,self.freecoordy1):0,(self.freecoordx2,self.freecoordy2):0,\
        #                         (self.freecoordx3,self.freecoordy3):0,(self.freecoordx4,self.freecoordy4):0}
        self.Dict_of_freecoord={0:(self.freecoordx1,self.freecoordy1),1:(self.freecoordx2,self.freecoordy2),\
                                2:(self.freecoordx3,self.freecoordy3),3:(self.freecoordx4,self.freecoordy4)}
        list_of_citiez.append(self)

    def trigger_of_Infection_Spread_up(self):
        global image_of_IO_number_variable
        self.trigger_of_Infection_Spread=1
        image_of_IO_number_variable+=1
    def return_trigger_of_Infection_Spread(self):
        return self.trigger_of_Infection_Spread
    def Change_up_Number_of_Virus(self,virus):
        if virus=='Virus_Red':
            self.Number_of_Virus_Red+=1
        elif virus=='Virus_Black':
            self.Number_of_Virus_Black+=1
        elif virus=='Virus_Violet':
            self.Number_of_Virus_Violet+=1
        elif virus=='Virus_Green':
            self.Number_of_Virus_Green+=1
        self.dict_of_numbers_of_virusez={Virus_Red:self.Number_of_Virus_Red,Virus_Black:self.Number_of_Virus_Black,\
                                         Virus_Green:self.Number_of_Virus_Green,Virus_Violet:self.Number_of_Virus_Violet}
    def Change_down_Number_of_Virus(self,virus):
        if virus=='Virus_Red':
            self.Number_of_Virus_Red-=1
        elif virus=='Virus_Black':
            self.Number_of_Virus_Black-=1
        elif virus=='Virus_Violet':
            self.Number_of_Virus_Violet-=1
        elif virus=='Virus_Green':
            self.Number_of_Virus_Green-=1
        self.dict_of_numbers_of_virusez={Virus_Red:self.Number_of_Virus_Red,Virus_Black:self.Number_of_Virus_Black,\
                                         Virus_Green:self.Number_of_Virus_Green,Virus_Violet:self.Number_of_Virus_Violet}
    def haveNearcity(self,other):
        if (other) not in self.Lizt :
            self.Lizt.append(other)
            other.Lizt.append(self)
        else :
            raise TypeError
    # def remove_fishka(self,coord):
    #     self.Dict_of_freecoord[coord]=0
    def is_neighbour(self,other):
        return other in self.Lizt
    def get_rec(self):
        return self.rectang
    def haveCard(self,card):
        self.card=card
    def add_virus(self,virus):
        global NumberOfVirusRed,NumberOfVirusBlack,NumberOfVirusGreen,NumberOfVirusViolet
        List_of_Deseased_Citiez.append(self)
        if virus=='Virus_Red':
            if NumberOfVirusRed==0:
                print str('Gameover')+str(' ')+str('NumberOfVirusRed - ')+str(NumberOfVirusRed)
                sys.exit()
            Box_to_add_Virusez(self.Number_of_Virus_Red,self.List_for_Virusez,self.List_of_Virusez_Red_counterz,self.List_of_Virusez_Red,virus,self.Lizt,self.trigger_of_Infection_Spread,self)
            NumberOfVirusRed-=1
        elif virus=='Virus_Green':
            if NumberOfVirusGreen==0:
                print str('Gameover')+str(' ')+str('NumberOfVirusGreen - ')+str(NumberOfVirusGreen)
                sys.exit()
            Box_to_add_Virusez(self.Number_of_Virus_Green,self.List_for_Virusez,self.List_of_Virusez_Green_counterz,self.List_of_Virusez_Green,virus,self.Lizt,self.trigger_of_Infection_Spread,self)
            NumberOfVirusGreen-=1
        elif virus=='Virus_Violet':
            if NumberOfVirusViolet==0:
                print str('Gameover')+str(' ')+str('NumberOfVirusViolet - ')+str(NumberOfVirusViolet)
                sys.exit()
            Box_to_add_Virusez(self.Number_of_Virus_Violet,self.List_for_Virusez,self.List_of_Virusez_Violet_counterz,self.List_of_Virusez_Violet,virus,self.Lizt,self.trigger_of_Infection_Spread,self)
            NumberOfVirusViolet-=1
        elif virus=='Virus_Black':
            if NumberOfVirusBlack==0:
                print str('Gameover')+str(' ')+str('NumberOfVirusBlack - ')+str(NumberOfVirusBlack)
                sys.exit()
            Box_to_add_Virusez(self.Number_of_Virus_Black,self.List_for_Virusez,self.List_of_Virusez_Black_counterz,self.List_of_Virusez_Black,virus,self.Lizt,self.trigger_of_Infection_Spread,self)
            NumberOfVirusBlack-=1

    def remove_virus(self,virus):
        global NumberOfVirusRed,NumberOfVirusBlack,NumberOfVirusGreen,NumberOfVirusViolet
        if self.dict_of_numbers_of_virusez[virus]==0:              # do i need this ?
            raise ValueError
        else :
            if virus=='Virus_Red':
                Box_to_remove_Virusez(virus,self.List_of_Virusez_Red_counterz,self.List_of_Virusez_Red,self.List_for_Virusez,self)
                NumberOfVirusRed+=1
            elif virus=='Virus_Green':
                Box_to_remove_Virusez(virus,self.List_of_Virusez_Green_counterz,self.List_of_Virusez_Green,self.List_for_Virusez,self)
                NumberOfVirusGreen+=1
            elif virus=='Virus_Violet':
                Box_to_remove_Virusez(virus,self.List_of_Virusez_Violet_counterz,self.List_of_Virusez_Violet,self.List_for_Virusez,self)
                NumberOfVirusViolet+=1
            elif virus=='Virus_Black':
                Box_to_remove_Virusez(virus,self.List_of_Virusez_Black_counterz,self.List_of_Virusez_Black,self.List_for_Virusez,self)
                NumberOfVirusBlack+=1
    def add_Lab(self):
        global instruction
        self.Lab=1
        List_of_city_w_Lab.append(self)
        instruction=None
    def __str__(self):
        return str(self.name)

Mos=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1152,179,'Moscow') # 1152,179
SFr=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),133,332,'Frisco')
Del=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1243,360,'Deli')
SPb=Citiez((pygame.image.load(os.path.join('imag','city.png'))),1007,156,'SPb' )#1007,156
Bag=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1032,420,'Bagdad')
Lon=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),701,160,'London')
Par=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),758,262,'Paris')

Alj=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),691,434,'Aljir')
Kair=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),878,429,'Kair')
ErR=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1022,629,'Er-Riad')
Bom=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1126,559,'Bombei')
MadR=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1180,659,'Madras')
Jak=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1263,747,'Jakarta')
Sid=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1488,812,'Sidney')
Man=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1527,652,'Manila')
Hosh=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1408,604,'Hoshimin')

Es=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),845,154,'Essen')
Mil=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),933,259,'Milan')
Sta=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1006,332,'Stambul')   #1007,332
Teg=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1176,275,'Tegeran')
Chic=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),264,269,'Chikago')
Tor=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),391,269,'Toronto')
NY=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),602,228,'NewYork')
Atl=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),330,368,'Atlanta')
WT=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),535,337,'Washington')

Mad=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),671,331,'Madrid')
Kalk=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1346,352,'Kalkutta')
Kar=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1165,420,'Karachi')
GnK=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1410,457,'Gonkong')
Shan=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1408,252,'Shanghai')
Pec=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1453,154,'Pekin')
Seul=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1561,202,'Seul')
Tok=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1546,302,'Tokio')
Osk=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1553,433,'Osaka')
Lag=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),756,544,'Lagos')
Har=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),901,538,'Hartum')
Kinsh=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),822,697,'Kinshasa')
YhB=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),917,799,'Yohannesburg')

BA=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),535,819,'Buenos-Aires')
Sant=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),428,879,'Santiago')
Lim=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),393,728,'Lima')
Bog=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),450,644,'Bogota')
May=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),535,467,'Maiamy')
Mex=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),282,578,'Mexico')
LA=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),177,500,'Los-Angeles')
Tay=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1541,543,'Taibey')
BnK=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),1272,558,'Bangkok')
SPaul=Citiez((pygame.image.load(os.path.join('imag','g4293.png'))),549,629,'San-Paulu')



Mos.haveNearcity(SPb)
Mos.haveNearcity(Teg)
Mos.haveNearcity(Sta)
SPb.haveNearcity(Sta)
SPb.haveNearcity(Es)
Sta.haveNearcity(Bag)
Sta.haveNearcity(Alj)
Sta.haveNearcity(Kair)
Sta.haveNearcity(Mil)
Mil.haveNearcity(Par)
Mil.haveNearcity(Es)
Es.haveNearcity(Par)
Es.haveNearcity(Lon)
Par.haveNearcity(Alj)
Par.haveNearcity(Mad)
Par.haveNearcity(Lon)
Lon.haveNearcity(Mad)
Lon.haveNearcity(NY)
Mad.haveNearcity(Alj)
Mad.haveNearcity(SPaul)
Mad.haveNearcity(NY)
Alj.haveNearcity(Kair)
Kair.haveNearcity(Bag)
Kair.haveNearcity(ErR)
Kair.haveNearcity(Har)
Teg.haveNearcity(Del)
Teg.haveNearcity(Kar)
Teg.haveNearcity(Bag)
Bag.haveNearcity(Kar)
Bag.haveNearcity(ErR)
Kar.haveNearcity(Del)
Kar.haveNearcity(Bom)
Kar.haveNearcity(ErR)
Del.haveNearcity(Bom)
Del.haveNearcity(MadR)
Del.haveNearcity(Kalk)
Kalk.haveNearcity(MadR)
Kalk.haveNearcity(BnK)
Kalk.haveNearcity(GnK)
Bom.haveNearcity(MadR)
MadR.haveNearcity(BnK)
MadR.haveNearcity(Jak)
BnK.haveNearcity(Jak)
BnK.haveNearcity(Hosh)
BnK.haveNearcity(GnK)
GnK.haveNearcity(Shan)
GnK.haveNearcity(Tay)
GnK.haveNearcity(Man)
GnK.haveNearcity(Hosh)
Jak.haveNearcity(Hosh)
Jak.haveNearcity(Sid)
Hosh.haveNearcity(Man)
Shan.haveNearcity(Tay)
Shan.haveNearcity(Tok)
Shan.haveNearcity(Seul)
Shan.haveNearcity(Pec)
Pec.haveNearcity(Seul)
Seul.haveNearcity(Tok)
Tok.haveNearcity(Osk)
Tok.haveNearcity(SFr)
Osk.haveNearcity(Tay)
Tay.haveNearcity(Man)
Man.haveNearcity(Sid)
Man.haveNearcity(SFr)
Sid.haveNearcity(LA)
Har.haveNearcity(YhB)
Har.haveNearcity(Lag)
Har.haveNearcity(Kinsh)
YhB.haveNearcity(Kinsh)
Kinsh.haveNearcity(Lag)
Lag.haveNearcity(SPaul)
SPaul.haveNearcity(BA)
SPaul.haveNearcity(Bog)
BA.haveNearcity(Bog)
Bog.haveNearcity(Lim)
Bog.haveNearcity(Mex)
Bog.haveNearcity(May)
Sant.haveNearcity(Lim)
Lim.haveNearcity(Mex)
Mex.haveNearcity(May)
Mex.haveNearcity(Chic)
Mex.haveNearcity(LA)
May.haveNearcity(Atl)
May.haveNearcity(WT)
LA.haveNearcity(SFr)
LA.haveNearcity(Chic)
SFr.haveNearcity(Chic)
Chic.haveNearcity(Atl)
Chic.haveNearcity(Tor)
Atl.haveNearcity(WT)
Tor.haveNearcity(NY)
Tor.haveNearcity(WT)
WT.haveNearcity(NY)

class Cardz (object):
    pass

class CardzofCity (Cardz):
    def __init__(self,city,virus,image,name):
        self.marc='ticket'
        self.image=image
        self.city=city
        self.city.haveCard(self)
        self.virus=virus            # this is color of card (for 'cure' etcetera)
        List_of_Cardz_Citiez.append(self)
        self.city.haveCard(self)
        self.rectang=image.get_rect()
        self.flag_on_coord=0
        self.name=name
        #self.List_of_tic_flag=[0,0,0,0,0,0,0]
        #self.List_of_tic_coor=[(50,769),(220,769),(390,769),(560,769),(730,769),(900,769),(1070,769),(1250,769)]
    def change_rec(self):
        self.rectang=self.image.get_rect(topleft=(self.x,self.y))
    def get_rec(self):
        return self.rectang
    def __str__(self):
        return str(self.name)

class CardzofSpecialEvents (Cardz):
    def __init__(self,image,name):
        self.marc='SECard'
        self.image=image
        self.name=name
        self.rectang=image.get_rect(topleft=(2000,0))
        self.flag_on_coord=0
        List_of_Cardz_Citiez.append(self)
        List_to_see_SE_card.append(self)
    def change_rec(self):
        self.rectang=self.image.get_rect(topleft=(self.x,self.y))
    def get_rec(self):
        return self.rectang
    def useit(self):
        if self==SEEmergency:
            return 'Move other'

        elif self==SEGoodNight:
            if not List_Of_Fishki.index(fishka)==3:
                List_Of_Fishki[List_Of_Fishki.index(fishka)+1].start_infection='off'
            else :
                List_Of_Fishki[0].start_infection='off'
        elif self==SEGoverment:
            return 'Build a Lab'
        else :
            return 'Show Infection trash'
    def __str__(self):
        return str(self.name)

SEEmergency=CardzofSpecialEvents(ticketSEEmergency,'SEEmergency')
SEGoodNight=CardzofSpecialEvents(ticketSEGoodNight,'SEGoodNight')
SEGoverment=CardzofSpecialEvents(ticketSEGovermentGrant,'SEGovermentGrant')
SEImmunity=CardzofSpecialEvents(ticketSEImmunity,'SEImmunity')

tickettoAlg=CardzofCity(Alj,Virus_Black,ticketAlg,'tickettoAlj')
tickettoAtl=CardzofCity(Atl,Virus_Violet,ticketAtl,'ticketAtl')
tickettoBag=CardzofCity(Bag,Virus_Black,ticketBag,'tickettoBag')
tickettoBang=CardzofCity(BnK,Virus_Red,ticketBang,'ticketBang')
tickettoBeij=CardzofCity(Pec,Virus_Red,ticketBeij,'ticketBeij')
tickettoBog=CardzofCity(Bog,Virus_Green,ticketBog,'ticketBog')
tickettoBuen=CardzofCity(BA,Virus_Green,ticketBuen,'ticketBuen')
tickettoCai=CardzofCity(Kair,Virus_Black,ticketCai,'tickettoKair')
tickettoChe=CardzofCity(MadR,Virus_Black,ticketChe,'ticketChe')

tickettoChic=CardzofCity(Chic,Virus_Violet,ticketChic,'ticketChic')
tickettoDel=CardzofCity(Del,Virus_Black,ticketDel,'tickettoDel')
tickettoErr=CardzofCity(ErR,Virus_Black,ticketErr,'tickettoErR')
tickettoEss=CardzofCity(Es,Virus_Violet,ticketEss,'ticketEss')
tickettoFris=CardzofCity(SFr,Virus_Violet,ticketFris,'tickettoFris')
tickettoHoch=CardzofCity(Hosh,Virus_Red,ticketHoch,'ticketHoch')
tickettoHong=CardzofCity(GnK,Virus_Red,ticketHong,'ticketHong')
tickettoJak=CardzofCity(Jak,Virus_Red,ticketJak,'tickettoJak')
tickettoJoh=CardzofCity(YhB,Virus_Green,ticketJoh,'ticketJoh')

tickettoKar=CardzofCity(Kar,Virus_Black,ticketKar,'ticketKar')
tickettoKhar=CardzofCity(Har,Virus_Green,ticketKhar,'ticketKhar')
tickettoKinsh=CardzofCity(Kinsh,Virus_Green,ticketKinsh,'ticketKinsh')
tickettoKol=CardzofCity(Kalk,Virus_Black,ticketKol,'ticketKol')
tickettoLA=CardzofCity(LA,Virus_Green,ticketLA,'ticketLA')
tickettoLag=CardzofCity(Lag,Virus_Green,ticketLag,'ticketLag')
tickettoLim=CardzofCity(Lim,Virus_Green,ticketLim,'ticketLim')
tickettoLon=CardzofCity(Lon,Virus_Violet,ticketLon,'tickettoLon')
tickettoMad=CardzofCity(Mad,Virus_Violet,ticketMad,'tickettoMad')
tickettoMan=CardzofCity(Man,Virus_Red,ticketMan,'ticketMan')
tickettoMex=CardzofCity(Mex,Virus_Green,ticketMex,'ticketMex')

tickettoMiam=CardzofCity(May,Virus_Green,ticketMiam,'ticketMiam')
tickettoMil=CardzofCity(Mil,Virus_Violet,ticketMil,'ticketMil')
tickettoMos=CardzofCity(Mos,Virus_Black,ticketMos,'tickettoMos')
tickettoMumb=CardzofCity(Bom,Virus_Black,ticketMumb,'tickettoBom')
tickettoNew=CardzofCity(NY,Virus_Violet,ticketNew,'ticketNew')
tickettoOsa=CardzofCity(Osk,Virus_Red,ticketOsa,'ticketOsa')
tickettoPar=CardzofCity(Par,Virus_Violet,ticketPar,'tickettoPar')

tickettoSan=CardzofCity(Sant,Virus_Green,ticketSan,'ticketSan')
tickettoSanp=CardzofCity(SPaul,Virus_Green,ticketSanp,'ticketSanp')
tickettoSeol=CardzofCity(Seul,Virus_Red,ticketSeol,'ticketSeol')
tickettoShan=CardzofCity(Shan,Virus_Red,ticketShan,'ticketShan')
tickettoSPb=CardzofCity(SPb,Virus_Violet,ticketSPb,'tickettoSPb')
ticketSta=CardzofCity(Sta,Virus_Black,ticketSta,'ticketSta')
tickettoSyd=CardzofCity(Sid,Virus_Red,ticketSyd,'ticketSyd')
tickettoTai=CardzofCity(Tay,Virus_Red,ticketTai,'ticketTai')

tickettoTeh=CardzofCity(Teg,Virus_Black,ticketTeh,'ticketTeh')
tickettoTok=CardzofCity(Tok,Virus_Red,ticketTok,'ticketTok')
tickettoTor=CardzofCity(Tor,Virus_Violet,ticketTor,'ticketTor')
tickettoWash=CardzofCity(WT,Virus_Violet,ticketWash,'ticketWash')

def check_to_see_SECard():
    global flag_to_show_SE_button
    flag_to_show_SE_button='off'

    for anyfishka in List_Of_Fishki:
        for SEcard in List_to_see_SE_card :
            if SEcard in anyfishka.hand :
                flag_to_show_SE_button='on'
                break

class Fishki(object):
    def __init__(self,image,city,profession):
        self.profession=profession
        if self.profession=='Scientist':
            self.nomber_of_cards_to_invent_a_cure=4
        else:
            self.nomber_of_cards_to_invent_a_cure=5
        self.city=city
        self.image=image
        self.x=0
        self.y=0

        self.hand=[]
        List_Of_Fishki.append(self)
        self.x,self.y=self.city.Dict_of_freecoord[List_Of_Fishki.index(self)]
        self.List_of_card_to_Cure=[]
        self.List_of_tic_flag=[0,0,0,0,0,0,0,0,0]
        self.List_of_tic_coor=[(50,969),(220,969),(390,969),(560,969),(730,969),(900,969),(1070,969),(1250,969)]
        self.start_infection='on'                                    # only for SEcard 'GoodNight'
        self.rectang=self.image.get_rect(topleft=(self.x,self.y))
    def get_position(self):
        return (self.x,self.y)
    def move_to(self,newcity):
        global Action_Number,instruction
        if Action_Number==4:
            return
        #self.city.remove_fishka((self.x,self.y))
        # for nom_fishka  in newcity.Dict_of_freecoord:
        #     if newcity.Dict_of_freecoord[nom_fishka]==0 :
        #         (self.x,self.y)=nom_fishka
        #         newcity.Dict_of_freecoord[nom_fishka]=1
        #         break
        self.x,self.y=newcity.Dict_of_freecoord[List_Of_Fishki.index(self)]
        self.city=newcity
        self.rectang=self.image.get_rect(topleft=(self.x,self.y))
        if not instruction=='Move other':
            Action_Number+=1
        instruction=None
    def show_yourself(self):
        screen.blit(self.image,(self.x,self.y))
    def addCardtoHand(self,card) :
        global Check_Hand_len
        self.hand.append(card)
        if card.marc=='SECard':
            List_to_see_SE_card_only_in_game.append(card)
        check_to_see_SECard()
        Check_Hand_len=True
        #print Check_Hand_len
    def removeCardFromHand(self,card):
        self.hand.remove(card)
        if card.marc=='SECard':
            List_to_see_SE_card_only_in_game.remove(card)
        check_to_see_SECard()
    def cureVirusfromCity(self,virus):
        global Action_Number
        if Action_Number==4:
            return
        if not self.profession=='Doctor':
            self.city.remove_virus(virus)
        else :
            for  i in range(self.city.dict_of_numbers_of_virusez[virus]):
                self.city.remove_virus(virus)
        Action_Number+=1
    def build_a_Lab(self):
        global Action_Number,action
        if Action_Number==4:
            return
        if not instruction=='Build a Lab':
            if not self.profession=='Builder':
                if self.city.card in self.hand and self.city not in List_of_city_w_Lab:
                    self.hand.remove(self.city.card)
                    self.city.add_Lab()
                    Action_Number+=1
            else :
                if self.city not in List_of_city_w_Lab:
                    if len(List_of_city_w_Lab)<5:
                        self.city.add_Lab()
                        Action_Number+=1
                    else :
                        action='Chose Lab to Destroy'
                        # List_of_city_w_Lab.remove(List_of_city_w_Lab[0])
                        # self.city.add_Lab()
                        # Action_Number+=1
        else :
            if self.city not in List_of_city_w_Lab:
                    if len(List_of_city_w_Lab)<5:
                        self.city.add_Lab()
                    else :
                        action='Chose Lab to Destroy'
    def __str__ (self):
        return str(self.profession)

fishkaBlue=Fishki(fish_image4,Mos,'Scientist')
fishkaRed=Fishki(fish_image3,Mos,'Builder')#'Changer') #Builder
fishkaGreen=Fishki(fish_image2,Mos,'Changer')
fishkaViolet=Fishki(fish_image6,Mos,'Doctor')

fishka=List_Of_Fishki[num_of_Player]

class CardzofInf(Cardz):
    def __init__(self,city,virus,image,name) :
        self.virus=virus
        self.city=city
        self.image=image
        self.name=name
        if self.virus==Virus_Black:
            self.text_image_for_virus=image_of_Black_virus
        elif self.virus==Virus_Green:
            self.text_image_for_virus=image_of_Green_virus
        elif self.virus==Virus_Red:
            self.text_image_for_virus=image_of_Red_virus
        elif self.virus==Virus_Violet:
            self.text_image_for_virus=image_of_Violet_virus
        List_of_CardzofInfection.append(self)
    def set_rec(self,coord):
        self.rectang=self.image.get_rect(topleft=coord)
    def get_rec(self):
        return self.rectang
    def trigga_of_desease (self):
        self.city.add_virus(self.virus)
    def __str__(self):
        return str(self.name)

CardzofInfAlg=CardzofInf(Alj,Virus_Black,CardzofInf_image_Alg,'CardzofInfAlj')
CardzofInfAtl=CardzofInf(Atl,Virus_Violet,CardzofInf_image_Atl,'CardzofInf_image_Atl')
CardzofInfBag=CardzofInf(Bag,Virus_Black,CardzofInf_image_Bag,'CardzofInfBag')
CardzofInfBang=CardzofInf(BnK,Virus_Red,CardzofInf_image_Bang,'CardzofInf_image_Bang')
CardzofInfBeij=CardzofInf(Pec,Virus_Red,CardzofInf_image_Beij,'CardzofInf_image_Beij')
CardzofInfBog=CardzofInf(Bog,Virus_Green,CardzofInf_image_Bog,'CardzofInf_image_Bog')
CardzofInfBuen=CardzofInf(BA,Virus_Green,CardzofInf_image_Buen,'CardzofInf_image_Buen')
CardzofInfCai=CardzofInf(Kair,Virus_Black,CardzofInf_image_Cai,'CardzofInfKair')
CardzofInfChe=CardzofInf(MadR,Virus_Black,CardzofInf_image_Che,'CardzofInf_image_Che')

CardzofInfChic=CardzofInf(Chic,Virus_Violet,CardzofInf_image_Chic,'CardzofInf_image_Chic')
CardzofInfDel=CardzofInf(Del,Virus_Black,CardzofInf_image_Del,'CardzofInfDel')
CardzofInfErr=CardzofInf(ErR,Virus_Black,CardzofInf_image_Err,'CardzofInfErR')
CardzofInfEss=CardzofInf(Es,Virus_Violet,CardzofInf_image_Ess,'CardzofInf_image_Ess')
CardzofInfFris=CardzofInf(SFr,Virus_Violet,CardzofInf_image_Fris,'CardzofInfFris')
CardzofInfHoch=CardzofInf(Hosh,Virus_Red,CardzofInf_image_Hoch,'CardzofInf_image_Hoch')
CardzofInfHong=CardzofInf(GnK,Virus_Red,CardzofInf_image_Hong,'CardzofInf_image_Hong')
CardzofInfJak=CardzofInf(Jak,Virus_Red,CardzofInf_image_Jak,'CardzofInfJak')
CardzofInfJoh=CardzofInf(YhB,Virus_Green,CardzofInf_image_Joh,'CardzofInf_image_Joh')

CardzofInfKar=CardzofInf(Kar,Virus_Black,CardzofInf_image_Kar,'CardzofInf_image_Kar')
CardzofInfKhar=CardzofInf(Har,Virus_Green,CardzofInf_image_Khar,'CardzofInf_image_Khar')
CardzofInfKinsh=CardzofInf(Kinsh,Virus_Green,CardzofInf_image_Kinsh,'CardzofInf_image_Kinsh')
CardzofInfKol=CardzofInf(Kalk,Virus_Black,CardzofInf_image_Kol,'CardzofInf_image_Kol')
CardzofInfLA=CardzofInf(LA,Virus_Green,CardzofInf_image_LA,'CardzofInf_image_LA')
CardzofInfLag=CardzofInf(Lag,Virus_Green,CardzofInf_image_Lag,'CardzofInf_image_Lag')
CardzofInfLim=CardzofInf(Lim,Virus_Green,CardzofInf_image_Lim,'CardzofInf_image_Lim')
CardzofInfLon=CardzofInf(Lon,Virus_Violet,CardzofInf_image_Lon,'CardzofInfLon')
CardzofInfMad=CardzofInf(Mad,Virus_Violet,CardzofInf_image_Mad,'CardzofInfMad')
CardzofInfMan=CardzofInf(Man,Virus_Red,CardzofInf_image_Man,'CardzofInf_image_Man')
CardzofInfMex=CardzofInf(Mex,Virus_Green,CardzofInf_image_Mex,'CardzofInf_image_Mex')

CardzofInfMiam=CardzofInf(May,Virus_Green,CardzofInf_image_Miam,'CardzofInf_image_Miam')
CardzofInfMil=CardzofInf(Mil,Virus_Violet,CardzofInf_image_Mil,'CardzofInf_image_Mil')
CardzofInfMos=CardzofInf(Mos,Virus_Black,CardzofInf_image_Mos,'CardzofInfMos')
CardzofInfMumb=CardzofInf(Bom,Virus_Black,CardzofInf_image_Mumb,'CardzofInfBom')
CardzofInfNew=CardzofInf(NY,Virus_Violet,CardzofInf_image_New,'CardzofInf_image_New')
CardzofInfOsa=CardzofInf(Osk,Virus_Red,CardzofInf_image_Osa,'CardzofInf_image_Osa')
CardzofInfPar=CardzofInf(Par,Virus_Violet,CardzofInf_image_Par,'CardzofInfPar')

CardzofInfSan=CardzofInf(Sant,Virus_Green,CardzofInf_image_San,'CardzofInf_image_San')
CardzofInfSanp=CardzofInf(SPaul,Virus_Green,CardzofInf_image_Sanp,'CardzofInf_image_Sanp')
CardzofInfSeol=CardzofInf(Seul,Virus_Red,CardzofInf_image_Seol,'CardzofInf_image_Seol')
CardzofInfShan=CardzofInf(Shan,Virus_Red,CardzofInf_image_Shan,'CardzofInf_image_Shan')
CardzofInfSPb=CardzofInf(SPb,Virus_Violet,CardzofInf_image_SPb,'CardzofInfSPb')
CardzofInfSta=CardzofInf(Sta,Virus_Black,CardzofInf_image_Sta,'CardzofInf_image_Sta')
CardzofInfSyd=CardzofInf(Sid,Virus_Red,CardzofInf_image_Syd,'CardzofInf_image_Syd')
CardzofInfTai=CardzofInf(Tay,Virus_Red,CardzofInf_image_Tai,'CardzofInf_image_Tai')

CardzofInfTeh=CardzofInf(Teg,Virus_Black,CardzofInf_image_Teh,'CardzofInf_image_Teh')
CardzofInfTok=CardzofInf(Tok,Virus_Red,CardzofInf_image_Tok,'CardzofInfTok')
CardzofInfTor=CardzofInf(Tor,Virus_Violet,CardzofInf_image_Tor,'CardzofInfTor')
CardzofInfWash=CardzofInf(WT,Virus_Violet,CardzofInf_image_Wash,'CardzofInf_image_Wash')

random.shuffle(List_of_CardzofInfection)

some_strange_var4=None # only to copy last card in CoInf
class Epidemic(Cardz):
    #global List_of_CardzofInfection_Trash_Copy
    def __init__(self,image):
        self.image=image
        List_of_EpidCardz.append(self)
        self.List_of_CardzofInfection_Trash_Copy=[]
    def triggerEpid (self):
        global List_of_CardzofInfection_Trash,List_of_CardzofInfection,ROI,ROI_number
        for sn3 in range(3):
            List_of_CardzofInfection[-1].trigga_of_desease()    # Last card of CoInf List add virus 3 times.what if it already had Vspishka ? We need flag that it was/
        List_of_CardzofInfection_Trash.append(List_of_CardzofInfection[-1]) # add this card to Trash
        some_strange_var4=List_of_CardzofInfection[-1]
        List_of_CardzofInfection.remove(some_strange_var4) # remove this card from List
        self.List_of_CardzofInfection_Trash_Copy=List_of_CardzofInfection_Trash[:]
        random.shuffle(List_of_CardzofInfection_Trash)        # shufflim Trash
        List_of_CardzofInfection=List_of_CardzofInfection_Trash+List_of_CardzofInfection  # second wave
        List_of_CardzofInfection_Trash=[]
        if  not ROI==6:
            print 'ok'
            ROI+=1
        ROI_number=List_of_ROI[ROI]
        return self.List_of_CardzofInfection_Trash_Copy
    def __str__(self):
        return str('Epidemic card')

for i in range(LevelGame):
    epid=Epidemic(image_of_epid_card)

some_strange_var5=0
some_strange_var6=0
some_strange_var7=0
some_strange_var8=0
some_strange_var9=0
XX=None
YY=None
ZZ=None
Second_wave=None
Infection=None
EOT=None
def show_all_buttonz():
    # print
    # print action
    global stage_of_blinkin_button,Second_wave,some_strange_var8,EOT
    global some_strange_var,XX,YY,some_strange_var6,ZZ,List_of_CardzofInfection
    global List_to_see_Epid_card,New_List_of_Cardz_Citiez,some_strange_var7,some_strange_var9,List_of_CoInf_to_infect,Images_of_List_of_CoInf_to_infect
    global Action_Number,some_strange_var5,Infection,List_of_coord_for_card_to_infect
    if not action=='Removing':
        if not action=='show SE' :
            if not action=='Chose Lab to Destroy':
                if not action=='cure':
                    if action!='Showing New card' :
                        if action!='Second wave' :
                            if action!='Infection':
                                for button in list_of_buttonz :
                                    if not dict_of_active_bz[button]=='not active':
                                        if not button==button11 :

                                            screen.blit(button.image,button.get_position())
                                        #pygame.draw.rect(screen,black,button.rectang,1)
                                    else :
                                        if stage_of_blinkin_button==1  :
                                            screen.fill(white,button.get_rec())
                                            #screen.fill(black,button.get_rec())
                                            screen.blit(button.image_blinking1,button.get_position())
                                            #pygame.time.wait(wait_time)

                                            pygame.display.update(button.get_rec())
                                            some_strange_var+=1
                                            if some_strange_var==8:
                                                some_strange_var=0
                                                stage_of_blinkin_button=2
                                        elif stage_of_blinkin_button==2 :
                                            screen.fill(white,button.get_rec())
                                            screen.blit(button.image_blinking2,button.get_position())
                                            #pygame.time.wait(wait_time)
                                            pygame.display.update(button.get_rec())
                                            some_strange_var+=1
                                            if some_strange_var==8:
                                                some_strange_var=0
                                                stage_of_blinkin_button=3
                                        elif stage_of_blinkin_button==3:
                                            screen.fill(white,button.get_rec())
                                            screen.blit(button.image_blinking3,button.get_position())
                                            #pygame.time.wait(wait_time)
                                            pygame.display.update(button.get_rec())
                                            some_strange_var+=1
                                            if some_strange_var==8:
                                                some_strange_var=0
                                                stage_of_blinkin_button=1
            if action=='Showing New card' or action=='Second wave' :
                screen.blit(image_of_Yournewticz,(10,30))

                for butt in list_of_buttonz :
                    butt.rectang=butt.image.get_rect(topleft=(2000,2000))
                if some_strange_var6<1 or some_strange_var6>19:
                    screen.blit(button10.image,(1450,10))
                    button10.rectang=button10.image.get_rect(topleft=(1450,10))
                    button11.rectang=button11.image.get_rect(topleft=(1560,10))
                if some_strange_var5==0:
                    XX=New_List_of_Cardz_Citiez[0]
                    YY=New_List_of_Cardz_Citiez[1]
                    screen.blit(New_List_of_Cardz_Citiez[0].image,(610,30))
                    screen.blit(New_List_of_Cardz_Citiez[1].image,(780,30))
                    List_to_see_Epid_card.append(New_List_of_Cardz_Citiez[0])
                    List_to_see_Epid_card.append(New_List_of_Cardz_Citiez[1])
                    for card_to_take in List_to_see_Epid_card:
                        if card_to_take != epid:
                            fishka.addCardtoHand(card_to_take)
                    List_to_see_Epid_card=[]
                    New_List_of_Cardz_Citiez=New_List_of_Cardz_Citiez[2:]
                    some_strange_var5=1

                screen.blit(XX.image,(610,30))
                screen.blit(YY.image,(780,30))

                if XX==epid or YY==epid:
                    some_strange_var6+=1

                    if some_strange_var6>20:

                        screen.fill(white)
                        screen.blit(World_card,(0,0))
                        show_all_citiez()
                        show_all_virusez()
                        show_all_fishkas()
                        screen.blit(IO_NYTimes,(30,120))
                        screen.blit(List_of_IO_numbers[image_of_IO_number_variable],(60,180))
                        if some_strange_var7==0:
                            some_strange_var7=1
                            ZZ=List_of_CardzofInfection[-1]
                        screen.blit(ZZ.text_image_for_virus,(30,30))
                        screen.blit(ZZ.image,(1100,30))
                        screen.blit(cityboard_image,(ZZ.city.x-7,ZZ.city.y-7))
                        screen.blit(button10.image,(1450,10))
                        Second_wave='begin'
                        if action=='Second wave':
                            screen.fill(white)
                            screen.blit(World_card,(0,0))
                            show_all_citiez()
                            show_all_virusez()
                            show_all_fishkas()
                            screen.blit(image_of_Second_wave,(10,20))
                            if not some_strange_var8==len(Trash):                               # why not for i in range len(Trash) ? Try it
                                for sn in [(400,10),(570,10),(740,10),(910,10),(1080,10),(1250,10),\
                                    (400,75),(570,75),(740,75),(910,75),(1080,75),(1250,75),\
                                    (400,140),(570,140),(740,140),(910,140),(1080,140),(1250,140)]:
                                    screen.blit(Trash[some_strange_var8].image,sn)
                                    some_strange_var8+=1
                                    if some_strange_var8==len(Trash):
                                        some_strange_var8=0
                                        break
                            screen.blit(button10.image,(1450,10))
                            Second_wave=None
                            Infection='begin'
                else :
                    Infection='begin'
            if action=='Infection':
                screen.fill(white)
                screen.blit(World_card,(0,0))
                show_all_citiez()
                show_all_virusez()
                show_all_fishkas()
                screen.blit(image_of_Spreading,(10,30))
                screen.blit(IO_NYTimes,(30,120))
                screen.blit(List_of_IO_numbers[image_of_IO_number_variable],(60,180))

                if not fishka.start_infection=='off':
                    if some_strange_var9==0:
                        some_strange_var9=1
                        # XX=List_of_CardzofInfection[0]
                        # YY=List_of_CardzofInfection[1]
                        # List_of_CardzofInfection_Trash.append(XX)
                        # List_of_CardzofInfection_Trash.append(YY)
                        # List_of_CardzofInfection=List_of_CardzofInfection[2:]
                        List_of_CoInf_to_infect=[List_of_CardzofInfection[i] for i in range(ROI_number)]
                        Images_of_List_of_CoInf_to_infect=[i.image for i in List_of_CoInf_to_infect ]
                        for i1 in List_of_CoInf_to_infect:
                            List_of_CardzofInfection_Trash.append(i1)
                        List_of_CardzofInfection=List_of_CardzofInfection[(ROI_number):]
                    # screen.blit(XX.image,(610,30))
                    # screen.blit(YY.image,(780,30))
                    for i3 in zip(Images_of_List_of_CoInf_to_infect,List_of_coord_for_card_to_infect):
                        XX=i3[0]
                        YY=i3[1]
                        screen.blit(XX,YY)
                screen.blit(button10.image,(1450,10))
                #screen.blit(button11.image,(button11.get_position()))
                Infection=None
                EOT='End Of Turn'
def show_all_fishkas():
    for fishka in List_Of_Fishki:
        screen.blit(fishka.image,fishka.get_position())

def show_all_citiez():
    for city in list_of_citiez:
        screen.blit(city.image,(city.x,city.y))

def show_all_ticketz():
    if not Check_Hand_len:
        for tic in fishka.hand:
            for i in range(8):
                if fishka.List_of_tic_flag[i]==0 and tic.flag_on_coord==0:
                    tic.x,tic.y=fishka.List_of_tic_coor[i]
                    tic.change_rec()
                    fishka.List_of_tic_flag[i]=1
                    tic.flag_on_coord=1
                    break

            screen.blit(tic.image,(tic.x,tic.y))



def show_all_virusez():
    for city in list_of_citiez :
        for i in city.List_for_Virusez:
            screen.blit(i[0],i[1])

flag_on_exchange_rec=None
#flag_on_exchange_PRESSED_rec=None
flagX,flagY=0,0

def show_all_ticketz_2(f):                                      # we ahould put here List_of_all_free_coord_for_tics[x] where x depends of

    index_of_fishka=List_Of_Fishki.index(f)
    global flag_on_exchange_rec
    global flagX,flagY
    if not status_of_ticket_in_hand_of_changer=='Ready to be given':
        flag_on_exchange_rec=None
        flagX,flagY=0,0
    for tic in f.hand:
        #for i in range(7): #i=0...7
        for i in range(8):
            if f.List_of_tic_flag[i]==0 and tic.flag_on_coord==0:
                tic.x,tic.y=List_of_all_free_coord_for_tics[index_of_fishka][i]
                tic.change_rec()
                #screen.blit(tic.image,List_of_tic_coor[i])
                f.List_of_tic_flag[i]=1
                tic.flag_on_coord=1
                break
        screen.blit(tic.image,(tic.x,tic.y))

    if not fishka.profession=='Changer':
        if not fishka==f and fishka.city.card  in fishka.hand:
            flagX,flagY=List_of_all_free_coord_for_tics[index_of_fishka][len(f.hand)]
            screen.blit(flag_on_exchange,(List_of_all_free_coord_for_tics[index_of_fishka][len(f.hand)]))
            flag_on_exchange_rec=flag_on_exchange.get_rect(topleft=(List_of_all_free_coord_for_tics[index_of_fishka][len(f.hand)]))
    else:
        if not fishka==f and status_of_ticket_in_hand_of_changer=='Ready to be given':
            flagX,flagY=List_of_all_free_coord_for_tics[index_of_fishka][len(f.hand)]
            screen.blit(flag_on_exchange,(List_of_all_free_coord_for_tics[index_of_fishka][len(f.hand)]))
            flag_on_exchange_rec=flag_on_exchange.get_rect(topleft=(List_of_all_free_coord_for_tics[index_of_fishka][len(f.hand)]))

def show_all_CoInf():
    global List_of_CoInf_coord
    e=0
    for i in List_of_played_CoInf:
        screen.blit(i.image,List_of_CoInf_coord[e])
        e+=1

def show_all_Labz():
    for citywLab in List_of_city_w_Lab :
        screen.blit(image_of_Lab,(citywLab.x+25,citywLab.y-30))


def clear_all_coord():
    for fishka in List_Of_Fishki:
        fishka.List_of_tic_flag=[0,0,0,0,0,0,0,0,0]
        for ticket in fishka.hand:
            ticket.flag_on_coord=0

random.shuffle(List_of_Cardz_Citiez)
for fishka in List_Of_Fishki :                                                     # move it to if starting !
    #for h in range(num_hand_card):
    for h in range(2):
        RanNum=random.randint(0,len(List_of_Cardz_Citiez)-1)                       # replace it w shuffle
        fishka.addCardtoHand(List_of_Cardz_Citiez[RanNum])
        List_of_Cardz_Citiez.remove(List_of_Cardz_Citiez[RanNum])

fishka=List_Of_Fishki[num_of_Player]

starting=True

def First_Desease(i):
    global List_of_played_CoInf
    for sn in range (3):
        #List_of_played_CoInf=[]
        RanNum=random.randint(0,len(List_of_CardzofInfection)-1)
        randomcard=List_of_CardzofInfection[RanNum]
        List_of_played_CoInf.append(randomcard)
        for sn2 in range (i):
            randomcard.trigga_of_desease()
        List_of_played_CoInf=[]
        List_of_CardzofInfection.remove(randomcard)
        List_of_CardzofInfection_Trash.append(randomcard)

def show_all_cured_virus():
    screen.blit(image_of_CV_scale,(30,400))
    if (len(List_of_CV_images))!=0:
        for i in zip(List_of_CV_images,List_of_coord_for_CV_fishka):
            screen.blit(i[0],i[1])

    # screen.blit(image_of_CV_fishka_red,List_of_coord_for_CV_fishka[0])#(30,400))
    # screen.blit(image_of_CV_fishka_green,List_of_coord_for_CV_fishka[1])#(30,498))
    # screen.blit(image_of_CV_fishka_black,List_of_coord_for_CV_fishka[2])#(30,598))
    # screen.blit(image_of_CV_fishka_violet,List_of_coord_for_CV_fishka[3])#(30,700)) #List_of_coord_for_CV_fishka=[(30,400),(30,498),(30,598),(30,700)]
some_strange_var11=0
s=None
while 1:
    if starting :
        image_of_IO_number_variable=0
        coord_for_fishka_ROI_x,coord_for_fishka_ROI_y=List_of_coord_for_ROI_fishka[ROI]
        First_Desease(3)
        First_Desease(2)
        First_Desease(1)
        v=int(len(List_of_Cardz_Citiez)/LevelGame)
        New_List_of_Cardz_Citiez=[List_of_Cardz_Citiez[m:m + v] for m in range(0, len(List_of_Cardz_Citiez), v)]
        if len(New_List_of_Cardz_Citiez)>LevelGame :
            some_strange_var10=New_List_of_Cardz_Citiez.pop(-1)
            New_List_of_Cardz_Citiez[-1].extend(some_strange_var10)
        for block_of_cardz in New_List_of_Cardz_Citiez:
            block_of_cardz.append(epid)
            random.shuffle(block_of_cardz)
        New_List_of_Cardz_Citiez=listmerge3(New_List_of_Cardz_Citiez)
        for anyfishka in List_Of_Fishki:
            for SEcard in List_to_see_SE_card :
                if SEcard in anyfishka.hand :
                    flag_to_show_SE_button='on'
                    break
        Mos.add_Lab()

        starting=False

    if Action_Number==4:
        print Action_Number
        action='Next Player'

    if  action=='Next Player' :

        #some_strange_var11=0
        some_strange_var6=0
        some_strange_var5=0
        some_strange_var7=0
        some_strange_var9=0
        for city1 in List_of_Deseased_Citiez:
            city1.trigger_of_Infection_Spread=0
        Action_Number=0
        action='Showing New card'

    if action=='OK !':
        action=None
        ssss2=None
        choosenfishka2=None
        for anybut in dict_of_active_bz :
            dict_of_active_bz[anybut]='active'
        for butt in list_of_buttonz:
            butt.set_old_rectang()
        if Second_wave=='begin':
            action='Second wave'
        if Infection=='begin':
            action='Infection'
        if EOT=='End Of Turn':
            num_of_Player_2+=1
            if num_of_Player_2==number_of_Player: #i.e if schetchik == chislu igrokov
                num_of_Player_2=0
            EOT=None

    if num_of_Player_2!=num_of_Player :
        num_of_Player=num_of_Player_2
        fishka=List_Of_Fishki[num_of_Player]
        if not List_Of_Fishki.index(fishka)==3:                                 # bad for performance? we could make another var ( if useit SEGoodNight => this var changes
            List_Of_Fishki[List_Of_Fishki.index(fishka)+1].start_infection='on'
        else :
            List_Of_Fishki[0].start_infection='on'

    clock.tick(30)
    screen.fill(white)
    screen.blit(World_card,(0,0))
    show_all_citiez()
    show_all_Labz()
    show_all_buttonz()
    show_all_virusez()
    show_all_fishkas()
    show_all_cured_virus()

    if flag_to_show_SE_button=='on':                                             # i.e if any SEcard in any player's hand
        if some_strange_var6>20 or some_strange_var6==0:
            screen.blit(button11.image,(button11.get_position()))

    if fishka!=fishkaViolet:
        screen.blit(scientist_board_image,(fishka.x-5,fishka.y+60))
    else :
        screen.blit(scientist_board_image,(fishka.x,fishka.y+60))

    if not action=='exchange card':
        show_all_ticketz()

    if some_strange_var7==1:
        Trash=epid.triggerEpid()                  #Epidemic alweys on last card !
        some_strange_var7=None
    if some_strange_var9==1:
        for i2 in range(ROI_number):
            List_of_CoInf_to_infect[i2].trigga_of_desease()
        some_strange_var9=None

    screen.blit(IO_NYTimes,(30,120))
    screen.blit(List_of_IO_numbers[image_of_IO_number_variable],(60,180))
    screen.blit(image_of_growing_rate_of_infection,(971,831))
    screen.blit(image_of_fishka_growing_rate_of_infection,List_of_coord_for_ROI_fishka[ROI])#(coord_for_fishka_ROI_x,coord_for_fishka_ROI_y)) #(971,912)1041 1113 1188 1262 1339 1416
    checkForQuit()

    for event in pygame.event.get():
        if event.type == MOUSEMOTION :
            mousepos=pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN :
            mousex, mousey = event.pos

    for  button in list_of_buttonz:             # ploho . Budet goniat po ciklu every while / Moghno poprobovat uslovie - if mouse in zone of buttonz:
        if (button.get_rec()).collidepoint(mousex, mousey) :
            action=button.click()
            clear_all_coord()
            mousex, mousey=0,0

    if dict_of_active_bz[button1]=='not active' and action=='moving':
        if not ssss2=='Choose city':
            for city in list_of_citiez:
                if (city.get_rec()).collidepoint(mousepos) and fishka.city.is_neighbour(city) :
                    screen.blit(cityboard_image,(city.x-7,city.y-7))
                if (city.get_rec()).collidepoint(mousex, mousey) and fishka.city.is_neighbour(city) :
                    mousex, mousey=0,0
                    fishka.move_to(city)
        if  fishka.profession=='Dispetcher':
            screen.blit(image_of_Choose_fishka_to_move,(800,120))
            for fishka6 in List_Of_Fishki:
                if fishka6.rectang.collidepoint(mousepos):
                    screen.blit(image_for_fishkaboard,(fishka6.x-25,fishka6.y-5))
                if fishka6.rectang.collidepoint(mousex, mousey):
                    choosenfishka2=fishka6
                    ssss2='Choose city'
                    mousex, mousey=0,0
                if ssss2=='Choose city':
                    screen.blit(image_for_fishkaboard,(choosenfishka2.x-25,choosenfishka2.y-5))
                    for city in list_of_citiez:
                        if (city.get_rec()).collidepoint(mousepos) and choosenfishka2.city.is_neighbour(city) :
                            screen.blit(cityboard_image,(city.x-7,city.y-7))
                        if (city.get_rec()).collidepoint(mousex, mousey) and choosenfishka2.city.is_neighbour(city) :
                            mousex, mousey=0,0
                            choosenfishka2.move_to(city)
                        if (city.get_rec()).collidepoint(mousex, mousey) and city in [fishka7.city for fishka7 in List_Of_Fishki] :
                            mousex, mousey=0,0
                            choosenfishka2.move_to(city)

    if  dict_of_active_bz[button8]=='not active' and action=='exchange card':
        #print 'cleaning all coordz 1'
        clear_all_coord()
        if not fishka.profession=='Changer':
            for fishka_a in List_Of_Fishki:
                #print 'Starting new cirkle in List of Fishki. Fishka_a= '+str(fishka_a)
                try:
                    if fishka.city==fishka_a.city:
                        show_all_ticketz_2(fishka_a)
                        if fishka!=fishka_a :                                               # i.e. fishka_a is notplayable
                            #print (flag_on_exchange_rec)
                            if (flag_on_exchange_rec).collidepoint(mousex, mousey) :
                                ff=flag_on_exchange_PRESSED.get_rect(topleft=(flagX,flagY))
                                pygame.draw.rect(screen,white,ff,0)
                                screen.blit(flag_on_exchange_PRESSED,(flagX,flagY))
                                pygame.display.update(ff)
                                pygame.time.wait(150)
                                fishka.removeCardFromHand(fishka_a.city.card)
                                fishka_a.addCardtoHand(fishka_a.city.card)
                                Action_Number+=1
                                mousex, mousey=0,0
                                if Action_Number==4:
                                    clear_all_coord()
                                    screen.fill(white)
                                    screen.blit(World_card,(0,0))
                                    show_all_buttonz()
                                    show_all_citiez()
                                    show_all_fishkas()
                                    for fishka_b in List_Of_Fishki:
                                        if fishka.city==fishka_b.city:
                                            show_all_ticketz_2(fishka_b)
                                    pygame.display.update()
                                    #time.sleep(1)
                                    pygame.time.wait(3500)
                                    #clear_all_coord()
                                    break
                                clear_all_coord()
                except :
                    pass                                                                # here should draw:'You could not give card that you do not have !'

                if fishka.city==fishka_a.city :
                    if fishka_a.city.card in fishka_a.hand:
                        #print 'ticket here'
                        #print 'fishka_a.city.card '+str(fishka_a.city.card) +' in fishka_a hand '+str(fishka_a)+str(fishka_a.hand)
                        screen.blit(ticketboard,(fishka_a.city.card.x-7,fishka_a.city.card.y-7))                                      # red board on card in action
                        if fishka!=fishka_a:
                            if fishka_a.city.card.rectang.collidepoint(mousex, mousey):

                                fishka_a.removeCardFromHand(fishka_a.city.card)
                                fishka.addCardtoHand(fishka_a.city.card)
                                Action_Number+=1
                                mousex, mousey=0,0
                                if Action_Number==4:
                                    # 'cleaning all coordz 4'

                                    clear_all_coord()
                                    screen.fill(white)
                                    screen.blit(World_card,(0,0))
                                    show_all_buttonz()
                                    show_all_citiez()
                                    show_all_fishkas()
                                    for fishka_b in List_Of_Fishki:
                                        if fishka.city==fishka_b.city:
                                            show_all_ticketz_2(fishka_b)
                                    pygame.display.update()
                                    #time.sleep(1)
                                    pygame.time.wait(1500)
                                    #clear_all_coord()
                                    break
                                clear_all_coord()
        elif fishka.profession=='Changer':
            some_strange_var2=0

            for fishka_c in List_Of_Fishki:
                if fishka.city==fishka_c.city:
                    show_all_ticketz_2(fishka_c)
                    some_strange_var2+=1
                    if fishka_c.city.card in fishka_c.hand :
                        screen.blit(ticketboard,(fishka_c.city.card.x-7,fishka_c.city.card.y-7))
                        if fishka!=fishka_c:
                            if fishka_c.city.card.rectang.collidepoint(mousex, mousey):
                                fishka_c.removeCardFromHand(fishka_c.city.card)
                                fishka.addCardtoHand(fishka_c.city.card)
                                Action_Number+=1
                                mousex, mousey=0,0
                                if Action_Number==4:
                                    clear_all_coord()
                                    some_strange_var2=0
                                    screen.fill(white)
                                    screen.blit(World_card,(0,0))
                                    show_all_buttonz()
                                    show_all_fishkas()
                                    for fishka_b in List_Of_Fishki:
                                        show_all_ticketz_2(fishka_b)
                                        some_strange_var2+=1
                                    pygame.display.update()
                                    #time.sleep(1)
                                    pygame.time.wait(500)
                                    clear_all_coord()

                for ticket_in_hand_of_changer in fishka.hand:
                    if ticket_in_hand_of_changer.rectang.collidepoint(mousepos):
                        screen.blit(ticketboard,(ticket_in_hand_of_changer.x-7,ticket_in_hand_of_changer.y-7))
                    if ticket_in_hand_of_changer.rectang.collidepoint(mousex, mousey):
                        status_of_ticket_in_hand_of_changer='Ready to be given'
                        ticket_that_shuold_be_given=ticket_in_hand_of_changer
                        some_strange_var3=0
                        for fishka_d in List_Of_Fishki:
                            show_all_ticketz_2(fishka_d)
                            some_strange_var3+=1
                        mousex, mousey=0,0
                    if status_of_ticket_in_hand_of_changer=='Ready to be given':
                        if fishka!=fishka_c:
                            if (flag_on_exchange_rec).collidepoint(mousex, mousey) :

                                ff=flag_on_exchange_PRESSED.get_rect(topleft=(flagX,flagY))
                                pygame.draw.rect(screen,white,ff,0)
                                screen.blit(flag_on_exchange_PRESSED,(flagX,flagY))
                                pygame.display.update(ff)
                                pygame.time.wait(150)
                                fishka.removeCardFromHand(ticket_that_shuold_be_given)
                                fishka_c.addCardtoHand(ticket_that_shuold_be_given)
                                Action_Number+=1
                                mousex, mousey=0,0
                                status_of_ticket_in_hand_of_changer=None

                                if Action_Number==4:
                                    clear_all_coord()
                                    some_strange_var3=0
                                    screen.fill(white)
                                    screen.blit(World_card,(0,0))
                                    show_all_buttonz()
                                    show_all_fishkas()
                                    for fishka_b in List_Of_Fishki:
                                        show_all_ticketz_2(fishka_b)
                                        some_strange_var3+=1
                                    pygame.display.update()
                                    #time.sleep(1)
                                    pygame.time.wait(500)
                                    clear_all_coord()

    if  dict_of_active_bz[button6]=='not active' and action=='cure':

        if fishka.city not in List_of_Deseased_Citiez :
            screen.blit(image_of_No_virus_in_city,(300,100))
            #screen.blit(button10.image,(1450,10))
        else:
            for butt in list_of_buttonz :
                butt.rectang=butt.image.get_rect(topleft=(2000,2000))
                button10.rectang=button10.image.get_rect(topleft=(1450,10))
            number_of_virus_in_city=0
            for v1 in fishka.city.dict_of_numbers_of_virusez:
                number_of_virus_in_city+=fishka.city.dict_of_numbers_of_virusez[v1]
                if fishka.city.dict_of_numbers_of_virusez[v1]!=0:
                    screen.blit(dict_of_virusez[v1][0],(dict_of_virusez[v1][2]))
                    if (dict_of_virusez[v1][1]).collidepoint(mousepos):
                        screen.blit(image_of_Board_for_Virusez,(dict_of_virusez[v1][2]))
            if not number_of_virus_in_city==0:
                number_of_virus_in_city=None
                screen.blit(image_of_Choose_virus,(10,30))
                screen.blit(button10.image,(1450,10))
                for v in dict_of_virusez:
                    if dict_of_virusez[v][1].collidepoint(mousex, mousey) and fishka.city.dict_of_numbers_of_virusez[v]!=0:
                        fishka.cureVirusfromCity(v)
                        mousex, mousey=0,0
            else :
                if fishka.city  in List_of_Deseased_Citiez :
                    List_of_Deseased_Citiez.remove(fishka.city)
                action='OK !'

    if dict_of_active_bz[button4]=='not active' and action=='build a lab':
        fishka.build_a_Lab()
        dict_of_active_bz[button4]='active'

    if action=='Chose Lab to Destroy':
        for butt in list_of_buttonz :
                butt.rectang=butt.image.get_rect(topleft=(2000,2000))
        screen.blit(image_of_Choose_city_to_remove_Lab,(10,30))
        for cwl in List_of_city_w_Lab:
            screen.blit(cityboard_image,(cwl.x-7,cwl.y-7))
            if cwl.rectang.collidepoint(mousex, mousey) :
                List_of_city_w_Lab.remove(cwl)
                fishka.build_a_Lab()
                action=None
                break

    if dict_of_active_bz[button5]=='not active' and action=='travel FLtL':
        if fishka.city in List_of_city_w_Lab:
            for cwl1 in List_of_city_w_Lab:
                if not cwl1==fishka.city:
                    screen.blit(cityboard_image,(cwl1.x-7,cwl1.y-7))
                    if cwl1.rectang.collidepoint(mousex, mousey) :
                        fishka.move_to(cwl1)
        else :
            dict_of_active_bz[button5]='active'
            action=None

    if dict_of_active_bz[button3]=='not active' and action=='charter to':
        if not fishka.profession=='Dispetcher' :
            if fishka.city.card in fishka.hand:
                screen.blit(ticketboard,(fishka.city.card.x-7,fishka.city.card.y-7))
                for anycity in list_of_citiez :
                    if anycity.rectang.collidepoint(mousex, mousey) and anycity!=fishka.city :
                        fishka.hand.remove(fishka.city.card)
                        fishka.move_to(anycity)
            else :
                dict_of_active_bz[button3]='active'            # we shuold put her .blit(theris no card of city in hand!)
                action=None
        else :
            screen.blit(image_of_Choose_fishka_to_move,(800,120))
            for fishka7 in List_Of_Fishki:
                if fishka7.rectang.collidepoint(mousepos):
                    screen.blit(image_for_fishkaboard,(fishka7.x-25,fishka7.y-5))
                if fishka7.rectang.collidepoint(mousex, mousey):
                    choosenfishka3=fishka7
                    ssss3='Choose city'
                    mousex, mousey=0,0
                if ssss3=='Choose city' and  choosenfishka3.city.card in choosenfishka3.hand:
                    for tic in choosenfishka3.hand:
                        for i in range(9):
                            if choosenfishka3.List_of_tic_flag[i]==0 and tic.flag_on_coord==0:
                                index_of_fishka=List_Of_Fishki.index(choosenfishka3)
                                #tic.x,tic.y=fishka5.List_of_tic_coor[i]
                                tic.x,tic.y=List_of_all_free_coord_for_tics[index_of_fishka][i]
                                tic.change_rec()
                                #screen.blit(tic.image,List_of_tic_coor[i])
                                choosenfishka3.List_of_tic_flag[i]=1
                                tic.flag_on_coord=1
                                break
                        screen.blit(tic.image,(tic.x,tic.y))
                    screen.blit(ticketboard,(choosenfishka3.city.card.x-7,choosenfishka3.city.card.y-7))
                    screen.blit(image_for_fishkaboard,(choosenfishka3.x-25,choosenfishka3.y-5))
                    for anycity in list_of_citiez :
                        if anycity.rectang.collidepoint(mousepos) and anycity!=choosenfishka3.city :
                            screen.blit(cityboard_image,(anycity.x-7,anycity.y-7))
                        if anycity.rectang.collidepoint(mousex, mousey) and anycity!=choosenfishka3.city :
                            choosenfishka3.hand.remove(choosenfishka3.city.card)
                            choosenfishka3.move_to(anycity)
                elif ssss3=='Choose city' and  choosenfishka3.city.card not in choosenfishka3.hand:
                    print 'no card of city in hand of' +str(choosenfishka3)          # we shuold put her .blit(theris no card of city in hand!)

    if instruction=='Build a Lab':
        fishka.build_a_Lab()


    if instruction=='Show Infection trash':
        freecoord=0
        for anyCOInfcard in List_of_CardzofInfection_Trash:
            screen.blit(anyCOInfcard.image,(List_of_free_coord_for_Trash[freecoord]))
            if not s=='Done':
                anyCOInfcard.set_rec(List_of_free_coord_for_Trash[freecoord])
            else :
                anyCOInfcard.set_rec((2000,0))
            freecoord+=1
        for anyCOInfcard1 in List_of_CardzofInfection_Trash:
            if anyCOInfcard1.get_rec().collidepoint(mousex, mousey):
                List_of_CardzofInfection_Trash.remove(anyCOInfcard1)
                s='Done'
                mousex, mousey=0,0
                for fishka3 in List_Of_Fishki:
                    if SEImmunity in fishka3.hand :
                        fishka3.removeCardFromHand(SEImmunity)
                        break
                break

    if instruction=='Move other':
        screen.blit(image_of_Choose_fishka_to_move,(800,120))
        for fishka4 in List_Of_Fishki:
            if fishka4.rectang.collidepoint(mousepos):
                screen.blit(image_for_fishkaboard,(fishka4.x-25,fishka4.y-5))
            if fishka4.rectang.collidepoint(mousex, mousey):

                choosenfishka=fishka4
                ssss='Choose city'
                mousex, mousey=0,0
            if  ssss=='Choose city':
                screen.blit(image_of_Choose_city_to_move,(800,120))
                screen.blit(image_for_fishkaboard,(choosenfishka.x-25,choosenfishka.y-5))
                for city2 in list_of_citiez:
                    if city2.rectang.collidepoint(mousepos):
                        screen.blit(cityboard_image,(city2.x-7,city2.y-7))
                    if city2.rectang.collidepoint(mousex, mousey):
                        choosenfishka.move_to(city2)
                        mousex, mousey=0,0
                        #instruction=None

    if action=='show SE':
        freecoord=0
        for anySEcard in List_to_see_SE_card_only_in_game:
            screen.blit(anySEcard.image,(List_of_free_coord_for_SECardz[freecoord]))
            anySEcard.x,anySEcard.y=List_of_free_coord_for_SECardz[freecoord]
            anySEcard.change_rec()
            freecoord+=1
        for buttonzz in list_of_buttonz:
            if not buttonzz==button10 and not buttonzz==button11:
                buttonzz.rectang=buttonzz.image.get_rect(topleft=(2000,2000))
        screen.blit(button10.image,(1450,10))
    if not action=='Removing':
        for SEcard in List_to_see_SE_card_only_in_game:
            if SEcard.rectang.collidepoint(mousepos):
                screen.blit(ticketboard,(SEcard.x-7,SEcard.y-7))
            if SEcard.rectang.collidepoint(mousex, mousey) :
                instruction=SEcard.useit()
                for fishka5 in List_Of_Fishki:
                    if  SEcard in fishka5.hand:
                        fishka5.removeCardFromHand(SEcard)
                mousex, mousey=0,0

    if dict_of_active_bz[button2]=='not active'and action=='travel to':
        for card in fishka.hand :
            if card.rectang.collidepoint(mousepos):
                screen.blit(ticketboard,(card.x-7,card.y-7))
            if card.rectang.collidepoint(mousex, mousey):
                if not card.city==fishka.city:                          # this is for not wasting card to move in city where you alr-y are
                    fishka.move_to(card.city)
                    fishka.hand.remove(card)                            # add e to discard pile!
        if fishka.profession=='Dispetcher':
            screen.blit(image_of_Choose_fishka_to_move,(800,120))
            for fishka9 in List_Of_Fishki:
                if fishka9.rectang.collidepoint(mousepos):
                    screen.blit(image_for_fishkaboard,(fishka9.x-25,fishka9.y-5))
                if fishka9.rectang.collidepoint(mousex, mousey):
                    choosenfishka4=fishka9
                    ssss4='Choose city'
                    mousex, mousey=0,0
                if  ssss4=='Choose city':
                    screen.blit(image_of_Choose_city_to_move,(800,120))
                    screen.blit(image_for_fishkaboard,(choosenfishka4.x-25,choosenfishka4.y-5))
                    for tic in choosenfishka4.hand:
                        for i in range(9):
                            if choosenfishka4.List_of_tic_flag[i]==0 and tic.flag_on_coord==0:
                                index_of_fishka=List_Of_Fishki.index(choosenfishka4)
                                #tic.x,tic.y=fishka5.List_of_tic_coor[i]
                                tic.x,tic.y=List_of_all_free_coord_for_tics[index_of_fishka][i]
                                tic.change_rec()
                                #screen.blit(tic.image,List_of_tic_coor[i])
                                choosenfishka4.List_of_tic_flag[i]=1
                                tic.flag_on_coord=1
                                break
                        screen.blit(tic.image,(tic.x,tic.y))
                    for card in choosenfishka4.hand :
                        if card.rectang.collidepoint(mousepos):
                            screen.blit(ticketboard,(card.x-7,card.y-7))
                        if card.rectang.collidepoint(mousex, mousey):
                            if not card.city==fishka.city:                          # this is for not wasting card to move in city where you alr-y are
                                choosenfishka4.move_to(card.city)
                                choosenfishka4.hand.remove(card)                            # add e to discard pile!

    for card in fishka.hand :
        if card.rectang.collidepoint(mousepos):
            screen.blit(ticketboard,(card.x-7,card.y-7))

        if dict_of_active_bz[button7]=='not active':
            print fishka.List_of_card_to_Cure
            if card.rectang.collidepoint(mousex, mousey)and action=='invent cure':      # coord of clicking mouse becomes this
                if card.y==969:                                                         # if starting point for y coord of all card is this
                    #fishka.nomber_of_cards_to_invent_a_cure-=1
                    if fishka.List_of_card_to_Cure==[] or fishka.List_of_card_to_Cure[0].virus==card.virus:
                        fishka.List_of_card_to_Cure.append(card)
                    else :
                        for card1 in fishka.List_of_card_to_Cure:
                            card1.y=969

                        fishka.List_of_card_to_Cure=[]
                        fishka.List_of_card_to_Cure.append(card)
                    card.y=965                                                          # starting point becomes this
                    a=-1                                                                # coeff becomes -1

                card.y+=5*(a)                                                           # decreasing starting point by this

                if card.y==950:                                                         # if starting point becomes this
                    card.change_rec()                                                   # changing rec to collide with
                    mousex, mousey=0,0                                                  # coord of clicking mouse becomes zero
                    card.y=951
                if card.y==951:
                    card.y=955
                    a=1
                if card.y==970:
                    fishka.nomber_of_cards_to_invent_a_cure+=1

                    card.change_rec()
                    mousex, mousey=0,0
                    card.y=969
            if fishka.profession!='Scientist':

                if len(fishka.List_of_card_to_Cure)==5:
                    for card2 in fishka.List_of_card_to_Cure:
                        fishka.removeCardFromHand(card2)
                    if card2.virus=='Virus_Red':
                        List_of_CV_images.append(image_of_CV_fishka_red)
                    elif card2.virus=='Virus_Black':
                        List_of_CV_images.append(image_of_CV_fishka_black)
                    elif card2.virus=='Virus_Green':
                        List_of_CV_images.append(image_of_CV_fishka_green)
                    elif card2.virus=='Virus_Violet':
                        List_of_CV_images.append(image_of_CV_fishka_violet)
                    dict_of_active_bz[button7]='active'
                    Action_Number+=1
                    print 'cure invented !'
            else:
                if len(fishka.List_of_card_to_Cure)==4:

                    for card2 in fishka.List_of_card_to_Cure:
                        fishka.removeCardFromHand(card2)
                    if card2.virus=='Virus_Red':
                        List_of_CV_images.append(image_of_CV_fishka_red)
                    elif card2.virus=='Virus_Black':
                        List_of_CV_images.append(image_of_CV_fishka_black)
                    elif card2.virus=='Virus_Green':
                        List_of_CV_images.append(image_of_CV_fishka_green)
                    elif card2.virus=='Virus_Violet':
                        List_of_CV_images.append(image_of_CV_fishka_violet)
                    dict_of_active_bz[button7]='active'
                    Action_Number+=1


    if not action=='Removing':
        previous_action=action

    if Check_Hand_len or action=='Removing' or action=='Showing New card':
        clear_all_coord()
        for fishka5 in List_Of_Fishki:
            if len(fishka5.hand)<8:

                Check_Hand_len=False

            else :
                action='Removing'
                #screen.blit(image_of_Choose_card_to_remove,())
                for tic in fishka5.hand:
                    for i in range(9):
                        if fishka5.List_of_tic_flag[i]==0 and tic.flag_on_coord==0:
                            index_of_fishka=List_Of_Fishki.index(fishka5)
                            #tic.x,tic.y=fishka5.List_of_tic_coor[i]
                            tic.x,tic.y=List_of_all_free_coord_for_tics[index_of_fishka][i]
                            tic.change_rec()
                            #screen.blit(tic.image,List_of_tic_coor[i])
                            fishka5.List_of_tic_flag[i]=1
                            tic.flag_on_coord=1
                            break
                    screen.blit(tic.image,(tic.x,tic.y))
                for tic in fishka5.hand:
                    if tic.rectang.collidepoint(mousex, mousey) :
                        if tic.marc!='SECard':
                            fishka5.removeCardFromHand(tic)
                        elif tic.marc=='SECard':
                            print 'using!'
                            instruction=tic.useit()
                            fishka5.removeCardFromHand(tic)
                        mousex, mousey=0,0
                        action=previous_action



    screen.blit(fishka.image,(fishka.x,fishka.y))
    pygame.display.update()


