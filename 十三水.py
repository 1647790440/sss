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
    c_list.append("^B")   #重点

    one = []
    two = []
    three = []
    four = []

    t_list = []
    for i in range(len(c_list)-1):
        t_list.append(c_list[i])
        #print(t_list)
        #print(c_list[i])
        if(c_list[i][1:] != c_list[i+1][1:]):
            if(len(t_list) == 1):
                one.append(t_list)
            elif(len(t_list) == 2):
                two.append(t_list)
            elif(len(t_list) == 3):
                three.append(t_list)
            else:
                four.append(t_list)
            t_list = []
    return one,two,three,four

# one,two,three,four = select_pair(['&2', '*2', '$2', '#2', '*7', '*K',  '#K',  '*K', '#K', '*A','$A'])
# print(one)
# print(two)
# print(three)
# print(four)


#去掉重复的牌，用来检查顺子
def remove_same_card(card_list):
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}  #大小比对
    number_card_list = []
    digital_card_list = []
    for item in card_list:
        number_card_list.append(item[1:])
    number_card_list = sorted(set(number_card_list),key=number_card_list.index)
    for item in number_card_list:
        digital_card_list.append(card_dict[item])
    return digital_card_list

print(remove_same_card(['&2', '*2', '$2', '#2', '*7', '*K',  '#K',  '*K', '#K', '*A','$A']))



#判断是否存在特殊牌型
def if_is_special_card():
    special_card = []
    return special_card



#找出剩余手牌中最大的选项
#后敦和中敦都可以使用这个算法
#前敦不需要再一个函数了，去掉中墩和后敦之后剩下的就是前敦了
def select_best(card_list):
    best_card_list = []
    if(len(card_list) == 3):
        best_card_list = card_list
        return best_card_list                   #这个return不太行

    #前期准备
    spade_list,heart_list,diamond_list,club_list = select_suit(card_list)

    one_list,two_list,three_list,four_list = select_pair(card_list)

    #同花顺——》炸弹——》葫芦——》同花——》顺子——》三条——》两对——》对子——》散牌
    #顺子不好搞定 
    #要重新考虑
    
    return best_card_list



#逻辑问题



def main():
    #变量定义
    #好像并不是很需要变量定义
    card_list = []
    #前中后
    first_card_list = []
    second_card_list = []
    third_card_list = []
    #四花色
    # spade_list = []     #$
    # heart_list = []     #&
    # diamond_list = []   ##
    # club_list = []      #*
    #取排
    #todo
    card_string = "*2 *3 *4 *5 *6 *7 *8 *9 *10 *J *Q *K *A"   #测试
    card_list = stl(card_string)
    #理牌
    #排序
    card_list = seq(card_list)
    #spade_list,heart_list,diamond_list,club_list = select_suit(card_list)
    #后敦
    third_card_list = select_best(card_list)
    card_list = cut_card(card_list,third_card_list)   #变成集合的过程中   还能保持有序吗？这是个问题
    #中敦
    second_card_list = select_best(card_list)
    card_list = cut_card(card_list,third_card_list)
    #前敦
    first_card_list = card_list
    #出牌

#main()