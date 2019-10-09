#十三水理牌算法
#初版
import collections

def get_str():
    card_string = ""
    return card_string


#把字符串转变成为卡牌
def stl(card_string):
    card_list = []
    card_list = card_string.split(' ')
    return card_list

#print(stl("*2 *4 *3 *5 *6 $A *7 *8 *9 *10 *J *Q *K *A"))    单元测试


def cut_card(card_list,select_best):
    return list(set(card_list) - set(select_best))

#print(cut_card(['*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9', '*10', '*J', '*Q', '*K', '*A'],['*2', '*4', '*5', '*6', '*7', '*8',  '*10',  '*Q', '*K', '*A']))  单元测试


#对卡牌进行排序
def seq(card_list):
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}  #大小比对
    card_dict_ordered = collections.OrderedDict()
    #card_list = []
    card_list_ordered = []
    seq_card_list = []
    #card_list = stl(card_string)
    #card_list = ['*2', '*4', '*5',  '*7','*6', '*8',  '*10',  '*Q', '*K', '*A','$A']   #测试
    #card_list.reverse()                                                           #测试                  
    #print(card_list)                                                             #测试
    #a = '2'                                                                      #测试
    #print(card_dict[a])
    for item in card_list:
        str = item[1:]
        value = card_dict[str]
        card_dict_ordered[item] = value
    card_dict_ordered=collections.Counter(card_dict_ordered).most_common()
    for item in card_dict_ordered:
        card_list_ordered.append(item[0])
    #print(card_list_ordered)           #测试
    #print(card_dict_ordered)           #测试
    #print(type(card_dict_ordered))     #测试
    seq_card_list = card_list_ordered
    return seq_card_list

#print(seq(['*2', '*4', '*5',  '*7','*6', '*8',  '*10',  '*Q', '*K', '*A','$A']))

#对卡牌花色进行挑选
def select_suit(card_list):
    spade_list = []     #$
    heart_list = []     #&
    diamond_list = []   ##
    club_list = []      #*
    for item in card_list:
        if(item[0] == '$'):
            spade_list.append(item)
        elif(item[0] == '&'):
            heart_list.append(item)
        elif(item[0] == '#'):
            diamond_list.append(item)
        else:
            club_list.append(item)
    return spade_list,heart_list,diamond_list,club_list
    
#这边要给一个测试样例
# spade_list,heart_list,diamond_list,club_list = select_suit(['&2', '*4', '$5', '#6', '*7', '*8',  '#10',  '*Q', '#K', '*A','$A'])
# print(spade_list)
# print(heart_list)
# print(diamond_list)
# print(club_list)


#分出炸弹、三条、对子、散牌
def select_pair(card_list):
    c_list = card_list
    one = []
    two = []
    three = []
    four = []
    for i in range(len(c_list)-1):
        
    return one,two,three,four

#select_pair(['&2', '*4', '$5', '#6', '*7', '*8',  '#10',  '*Q', '#K', '*A','$A'])


#判断是否存在特殊牌型
def if_is_special_card():
    special_card = []
    return special_card



#找出剩余手牌中最大的选项
#后敦和中敦都可以使用这个算法
#前敦不需要再一个函数了，去掉中墩和后敦之后剩下的就是前敦了
def select_best(seq_card_list):
    best_card_list = []
    return best_card_list

def main():
    #变量定义
    card_list = []
    #前中后
    first_caed_list = []
    second_card_list = []
    third_card_list = []
    #四花色
    spade_list = []     #$
    heart_list = []     #&
    diamond_list = []   ##
    club_list = []      #*
    #取排
    #todo
    card_string = "*2 *3 *4 *5 *6 *7 *8 *9 *10 *J *Q *K *A"   #测试
    card_list = stl(card_string)
    #理牌
    #排序
    card_list = seq(card_list)
    spade_list,heart_list,diamond_list,club_list = select_suit(card_list)
    #后敦
    third_card_list = select_best(card_list)
    card_list = cut_card(card_list,third_card_list)
    #中敦
    second_card_list = select_best(card_list)
    card_list = cut_card(card_list,third_card_list)
    #前敦
    first_caed_list = card_list
    #出牌

#main()