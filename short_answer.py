import random

q5 = ['网络信息高速发展，新媒体广泛应用，受众接受信息碎片化的现象越来越显著，对高校的教学活动和学生管理都产生了影响，除了课堂学习，学生可以借助微博、论坛等平台，更方便地接收和发布信息。',
      '微课、慕课等线上教学形式的推广，学生信息接收更快、耗时更短，互联网和媒介新技术的发展，信息传播方式更加碎片化，对学生产生的影响较大，也引起了高校的关注。',
      '网络信息化发展，碎片化的信息传播接受更容易，同时人们的碎片化时间较多，更进一步促进了信息碎片化的发展，而碎片化的信息更好地充实了人们的碎片时间。',
      '高校学生受网络发展时代的影响较大，对新媒体的认识程度较深，使用媒体的频率也较高，成为很多网站和软件开发的重点研究对象。',
      '在互联网的应用中，学生多是处于好奇、钻研的心理，利用互联网平台查阅资料，进行自学，了解行业发展和专业知识等，同时也拓展了学生的视野;',
      '在新媒体发展阶段，信息海量化的发展，学生接受信息的方式更加便捷，通过移动终端设备，可以进行随时随地的学习和阅读，也可以加深与教师和其他学生的交流与沟通。',
      '网络信息泛滥。互联网的快速发展，也容易分散人们的注意力，学生在学习中，不愿花费过多的时间去阅读、思考.',
      '人们更愿意直接接受简单的文字和图片、视频这类的碎片化信息，更快捷地认识世界，但是互联网上的信息内容虽多，但内容良莠不齐',
      '学生面临信息无法做出正确的选择和判断。碎片化的信息，专业权威信息相对较少，高校学生难以获取完整的信息，知识系统不够完善，影响到学生的学习效率和逻辑思维的发展',
      '信息泛娱乐化带来的身心健康影响。当前网络信息发展中，尤其是自媒体的快速发展，娱乐性信息更是充斥着网络。',
      '网络信息娱乐化的发展，影响到学生深度阅读和研究的注意力，浪费掉学生很多时间',
      '一些学生沉迷于网络，在一些低质量的信息中消耗了过多时间，缺乏系统性的知识，且长时间地观看图文和视频，会产生视觉疲劳。',
      '一些负面信息等充斥网络，学生容易受到其影响，影响到价值观的形成等，对学习和未来发展出现消极抵抗的情绪，网络中不乏有一些对社会不满的声音，学生难以分辨事实，常常会去转发评论。',
      '面对新的网络和媒体发展环境，要重视借助先进的技术和有用的信息为学生发展服务，对碎片化的信息加以整合，构建完善的知识体系',
      '实现平台内容的收藏，信息汇总处理，从而更好地满足学生对信息的需求，对碎片化的信息加以整合，实现学生最终从浅层阅读到深层阅读。',
      '当前高校云盘的建设中，多是以教学资源共享为主，信息融合发展的发背景下，高校也要重视做好信息的处理和加工',
      '借助高校云盘开放权限的资源，了解高校资源分享和下载的数量，对于阅读和下载频率较高的信息进行完善和加工，避免信息的重复，并重视提升此类信息的质量，确保学生能对信息有系统化的认识。',
      '引导学生有效使用笔记类、阅读类网站和软件',
      '加强高校云盘建设，实现信息资源共享',
      '引导学生学会自我学习，学会深度思考',
      '利用网络优势，加深学生深度阅读',
      '增强网络学习的趣味性',
      '没有认识',
      '没有理解',
      '不知道']

q10 = ['在学校官方公众号可及时接受到关键信息的推送',
       '辅导员在年级群里发布信息',
       '班委、学生会等学生在群里发布信息',
       '学校通知的方式较为分散',
       '接受学校信息的途径比较多',
       '乐学，微信，qq都有重要的信息',
       '学校发布信息应该采取统一的途径',
       '学校发布信息比较科学',
       '几乎所有同学都能及时看到重要信息',
       '很好',
       '很不错',
       '不知道',
       '无']

q16 = ['统一传递信息的平台',
       '目前平台太分散了，可以统一一下',
       '重要消息短信通知，与联网的消息区分开',
       '打电话通知消息',
       '尽量在一个平台上发布消息，一会看qq，一会看微信很麻烦',
       '传电报',
       '二进制01序列传输信息',
       '不知道',
       '无'
]

q18 = ['整合是个不断思考、相互关联、系统化的的过程，笔记和总结是种方法，但要注意整体的过程。',
       '阅读时就系统化地阅读，内容才利于整合。不同类型的信息要多想想他们之间的关系。',
       '笔记尽量直接就系统、结构化，如这种树形笔记，一个主题有结构、有顺序地整合在一起',
       '总结不是一下就完成的，不断地总结，就能不断提高自己的能力。',
       '多观看下别人的笔记整理。就是在一些学习网站上面观看讲师讲课时，换一个角度去考虑这些问题',
       '少看短视频和营销文，真是互联网公司为了流量脸都不要了',
       '多看书，小说（网络小说除外），剧本，看完以后自己总结一下人物关系',
       '信息應用能力可能是企業在獲得與服務於顧客與股東的過程中贏取利潤的最重要因素。',
       '信息整合能力的提高能以三種途徑影響競爭：改變運作結構，從而改變競爭規則；支持低成本以及差異化戰略',
       '醞釀全新的業務。經理人員需要的是有利於其作出正確決策的信息，包括基礎信息等',
       '多看信息，多想想信息间的内在联系与矛盾。',
       '有时间看看矛盾论之类的哲学书籍。',
       '没有想法',
       '不懂',
       '没看懂问题',
       '不知道',
       '无']


def random_answer(answer_list: list):
    length = len(answer_list)
    index = random.randint(0, length-1)
    return answer_list[index]


def get_short_answer(no: int):
    res = ''
    if no == 5:
        res = random_answer(q5)
    elif no == 10:
        res = random_answer(q10)
    elif no == 16:
        res = random_answer(q16)
    else:
        res = random_answer(q18)

    return res