#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import time

class Node(object):
    def __init__(self):
        self.children = None
        # 标记匹配到了关键词
        self.flag = False


# The encode of word is UTF-8
def add_word(root, word):
    if len(word) <= 0:
        return
    node = root
    for i in range(len(word)):
        if node.children == None:
            node.children = {}
            node.children[word[i]] = Node()

        elif word[i] not in node.children:
            node.children[word[i]] = Node()

        node = node.children[word[i]]
    node.flag = True


def init(word_list):
    root = Node()
    for line in word_list:
        add_word(root, line)
    return root


# The encode of word is UTF-8
# The encode of message is UTF-8
def key_contain(message, root):
    res = set()
    for i in range(len(message)):
        p = root
        j = i
        while (j < len(message) and p.children != None and message[j] in p.children):
            if p.flag == True:
                res.add(message[i:j])
            p = p.children[message[j]]
            j = j + 1

        if p.children == None:
            res.add(message[i:j])
            # print '---word---',message[i:j]
    return res


def dfa():
    print('----------------dfa-----------')
    word_list = ['hello', '民警', '朋友', '女儿', '派出所', '派出所民警']
    root = init(word_list)

    message = '四处乱咬乱吠，吓得家中11岁的女儿躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征得主人同意后，民警和村民合力将这只发疯的狗打死'
    x = key_contain(message, root)
    for item in x:
        print(item)


if __name__ == '__main__':
    dfa()
