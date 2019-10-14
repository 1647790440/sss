#十三水理牌算法
#初版
import collections

# def get_str():
#     card_string = ""
#     return card_string


#把字符串转变成为卡牌
def stl(card_string):
    card_list = []
    card_list = card_string.split(' ')
    return card_list

#print(stl("*2 *4 *3 *5 *6 $A *7 *8 *9 *10 *J *Q *K *A"))    单元测试


def cut_card(card_list,select_best):
    t_list = card_list
    t_list = sorted(set(card_list) - set(select_best),key=t_list.index)    #保证顺序
    return t_list

#print(cut_card(['*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9', '*10', '*J', '*Q', '*K', '*A'],['*2', '*4', '*5', '*6', '*7', '*8',  '*10',  '*Q', '*K', '*A'])) 


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
    c_list = card_list.copy()
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
    #print(card_list)
    #print(c_list)
    return one,two,three,four

# one,two,three,four = select_pair(['&2', '*2', '$2', '#2', '*7', '*K',  '#K',  '*K', '#K', '*A','$A'])
# print(one)
# print(two)
# print(three)
# print(four)


#去掉重复的牌，用来检查顺子
def remove_same_card(card_list):
    #print(card_list)
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}  #大小比对
    number_card_list = []
    digital_card_list = []
    for item in card_list:
        number_card_list.append(item[1:])
    number_card_list = sorted(set(number_card_list),key=number_card_list.index)
    for item in number_card_list:
        digital_card_list.append(card_dict[item])

    #print(digital_card_list)

    return digital_card_list

#print(remove_same_card(['&2', '*2', '$2', '#2', '*7', '*K',  '#K',  '*K', '#K', '*A','$A']))

#挑出顺子
def select_digital(digital_card_list):
    for i in range(len(digital_card_list)-4):
        if(digital_card_list[i] == digital_card_list[i+4]+4):
            #证明是顺子
            return digital_card_list[i]
            #只能证明存在顺子，但是得不到牌
    return False


#挑出顺子
def select_straight(card_list):
    digital_card_list = remove_same_card(card_list)
    digital = select_digital(digital_card_list)
    if(digital == False):
        return []
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}  #大小比对
    straight_card_list = []
    for i in range(len(card_list)):
        if(card_dict[card_list[i][1:]] == digital):
            straight_card_list.append(card_list[i])
            digital = digital - 1
        if(len(straight_card_list) == 5):
            break
    return straight_card_list

#print(select_straight(['&A', '*K', '$Q', '#J', '*10', '*9',  '#8',  '*7', '#6', '*5','$4']))


#判断是否存在特殊牌型
#放弃不写
# def if_is_special_card():
#     special_card = []
#     return special_card



#找出剩余手牌中最大的选项
#后敦和中敦都可以使用这个算法
#前敦不需要再一个函数了，去掉中墩和后敦之后剩下的就是前敦了
#主函数
def select_best(card_list):
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}  #大小比对     
    # first_card_list = []
    # second_card_list = []
    # third_card_list = []
    best_card_list = []    #要换成空列表
    if(len(card_list) == 3):
        best_card_list = card_list
        print("乌龙")
        return best_card_list                   #这个return不太行
    #前期准备
    spade_list,heart_list,diamond_list,club_list = select_suit(card_list)
    one_list,two_list,three_list,four_list = select_pair(card_list)

    #同花顺——》炸弹——》葫芦——》同花——》顺子——》三条——》两对——》对子——》散牌
    #顺子不好搞定 解决了
    #要重新考虑

    #同花顺
    if(len(spade_list) >= 5):
        best_card_list = select_straight(spade_list)
    elif(len(heart_list) >= 5):
        best_card_list = select_straight(heart_list)
    elif(len(diamond_list) >= 5):
        best_card_list = select_straight(diamond_list)
    else:
        best_card_list = select_straight(club_list)

    if(len(best_card_list) != 0):    #这个不是很好
        print("同花顺")
        return best_card_list

    #炸弹
    if(len(four_list) != 0):
        best_card_list = four_list[0]
        if(len(one_list) != 0):
            best_card_list.append(one_list[-1][0])
            print("炸弹")
            return best_card_list
        elif(len(two_list) != 0):
            best_card_list.append(two_list[-1][0])
            print("炸弹")
            return best_card_list
        else:
            best_card_list.append(three_list[-1][0])
            print("炸弹")
            return best_card_list

    #葫芦
    if(len(two_list) != 0 and len(three_list) != 0):
        best_card_list = three_list[0] + two_list[-1]
        print("葫芦")
        return best_card_list
    elif(len(two_list) == 0 and len(three_list) >= 2):
        best_card_list = three_list[0] + three_list[1][:1]
        print("葫芦")
        return best_card_list

    #同花
    if(len(spade_list) >= 5):
        best_card_list = spade_list[:5]
    if(len(heart_list) >= 5):
        if(len(best_card_list) != 0):
            # print(1)
            # print(best_card_list)
            if(card_dict[best_card_list[0][1:]] < card_dict[heart_list[0][1:]]):
                best_card_list = heart_list[:5]
        else:
            best_card_list = heart_list[:5]
    if(len(diamond_list) >= 5):
        if(len(best_card_list) != 0):
            # print(2)
            # print(best_card_list)
            if(card_dict[best_card_list[0][1:]] < card_dict[diamond_list[0][1:]]):
                best_card_list = diamond_list[:5]
        else:
            best_card_list = diamond_list[:5]
    if(len(club_list) >= 5):
        if(len(best_card_list) != 0):
            # print(3)
            # print(best_card_list)
            if(card_dict[best_card_list[0][1:]] < card_dict[club_list[0][1:]]):
                best_card_list = club_list[:5]
        else:
            best_card_list = club_list[:5]
    if(len(best_card_list) != 0):
        print("同花")
        return best_card_list

    #顺子
    best_card_list = select_straight(card_list)
    if(len(best_card_list) != 0):
        print("顺子")
        return best_card_list

    #三条
    if(len(three_list) != 0):
        best_card_list = three_list[0] + one_list[0] + one_list[1]
        print("三条")
        return best_card_list
        
    #两对
    if(len(two_list) >= 2):
        best_card_list = two_list[0] + two_list[1] + one_list[0]
        print("两对")
        return best_card_list

    #对子
    if(len(two_list) == 1):
        best_card_list = two_list[0] + one_list[0] + one_list[1] + one_list[2]
        print("对子")
        return best_card_list

    #散牌
    for item in one_list:
        best_card_list = best_card_list + item
        if(len(best_card_list) == 5):
            break
    print("乌龙")
    return best_card_list

def main_function(card_string):
    #变量定义
    #好像并不是很需要变量定义
    card_list = []
    card_string_list = []
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
    #card_string = "#A $2 #3 $4 #5 $6 #7 $8 #9 $10 #J $Q #K"   #测试
    card_list = stl(card_string)
    #理牌
    #排序
    card_list = seq(card_list)
    #spade_list,heart_list,diamond_list,club_list = select_suit(card_list)
    # #后敦
    print("后敦")
    third_card_list = select_best(card_list)
    card_list = cut_card(card_list,third_card_list)   #变成集合的过程中   还能保持有序吗？这是个问题  已经解决
    third_card_list.reverse()
    third_card_string = " ".join(third_card_list)
    print(third_card_string)
    #中敦
    print("中敦")
    second_card_list = select_best(card_list)
    card_list = cut_card(card_list,second_card_list)
    second_card_list.reverse()
    second_card_string = " ".join(second_card_list)
    print(second_card_string)
    #前敦
    print("前敦")
    first_card_list = select_best(card_list)
    first_card_list.reverse()
    first_card_string = " ".join(first_card_list)
    print(first_card_string)
    #first_card_string,second_card_string,third_card_string
    card_string_list.append(first_card_string)
    card_string_list.append(second_card_string)
    card_string_list.append(third_card_string)
    print(card_string_list)
    return card_string_list

#main_function()

