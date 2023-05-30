import pandas as pd
import jieba

def translate(word):
    removed_n_field_named_list = load_field_named_dict("./字段命名字典.txt")
    jieba_word_suggest(removed_n_field_named_list)
    mapping_dict = load_cn_en_dict("./字段中英文对照字典.xlsx")
    
    if isinstance(word, list):
        result_list = []
        for wordItem in word:
            result_list.append(translate(wordItem))
        return result_list
    elif isinstance(word, str):
        jieba_result = jieba.lcut(word, cut_all=False)
        print("original word: " + word + ", jieba_result:" + str(jieba_result))
        return get_translate_result(jieba_result, mapping_dict)
    else:
        return "入参类型错误，允许类型仅包含[str, list]"


# 读取字段命名字典： "../字段命名字典.txt"
def load_field_named_dict(dict_path):
    # set suggest_freq, make sure words be split right
    # load dict
    with open(dict_path, encoding="utf-8") as f:
        my_dict = f.readlines()

    # remove \n
    removed_n_field_named_list = []
    for i in my_dict:
        removed_n_field_named_list.append(i.strip('\n'))
    
    return removed_n_field_named_list


# 获取中英文对照表的内容："../字段中英文对照字典.xlsx"
def load_cn_en_dict(excel_path):
    source_dict = pd.read_excel(excel_path)
    # change source mapping to dict
    return dict(zip(source_dict["ch"], source_dict["eng"]))


# 自定义结巴分词
def jieba_word_suggest(removed_n_field_named_list):
    jieba.suggest_freq(('国控', '主数据'), True)
    jieba.suggest_freq(('主数据', '编码'), True)
    jieba.suggest_freq(('折扣', '价'), True)
    jieba.suggest_freq(('打印', '发票'), True)
    jieba.suggest_freq(('成本', '价'), True)
    jieba.suggest_freq(('销售', '收入'), True)
    jieba.suggest_freq(('价格', '政策'), True)
    jieba.suggest_freq(('接口', '类型'), True)
    jieba.suggest_freq(('生产', '厂家'), True)
    jieba.suggest_freq(('经营', '方式'), True)
    jieba.suggest_freq(('证件', '号码'), True)
    jieba.suggest_freq(('医疗', '机构'), True)
    jieba.suggest_freq(('商品', '名称'), True)
    jieba.suggest_freq(('计量', '单位'), True)
    jieba.suggest_freq(('质量', '标准'), True)
    jieba.suggest_freq(('手机', '号码'), True)
    jieba.suggest_freq(('生产', '日期'), True)
    jieba.suggest_freq(('业务', '流程'), True)
    jieba.suggest_freq(('业务', '部门'), True)
    jieba.suggest_freq(('联系', '方式'), True)
    jieba.suggest_freq(('出生', '日期'), True)
    jieba.suggest_freq(('医疗', '保险'), True)
    jieba.suggest_freq('单据号', True)
    jieba.suggest_freq('大类', True)
    jieba.suggest_freq('主数据', True)
    jieba.suggest_freq(('管理', '费用'), True)
    jieba.suggest_freq(('财务', '费用'), True)
    jieba.suggest_freq(('销售', '费用'), True)
    jieba.suggest_freq(('费用', '率'), True)
    jieba.suggest_freq(('单位', '名称'), True)
    jieba.suggest_freq(('费用', '率'), True)
    jieba.suggest_freq(('总', '费用'), True)
    jieba.suggest_freq(('零售', '价格'), True)
    jieba.suggest_freq(('分销', '销退'), True)
    jieba.suggest_freq('分销', True)
    jieba.suggest_freq('销退', True)
    jieba.suggest_freq(('去年', '同期'), True)
    jieba.suggest_freq(('年度', '计划'), True)
    jieba.suggest_freq(('年度', '预算'), True)
    jieba.suggest_freq('占比', True)
    jieba.suggest_freq(('零售', '退单'), True)
    jieba.suggest_freq(('销售', '策略'), True)
    jieba.suggest_freq(('销售', '价格'), True)
    jieba.suggest_freq(('保险', '客户'), True)
    jieba.suggest_freq(('商品', '生产', '批号'), True)
    jieba.suggest_freq('退单', True)
    jieba.suggest_freq('请货单', True)
    jieba.suggest_freq('更正单', True)
    jieba.suggest_freq('出库单', True)
    jieba.suggest_freq('入库单', True)
    jieba.suggest_freq('预报单', True)
    jieba.suggest_freq('预收单', True)
    jieba.suggest_freq('申请单', True)
    jieba.suggest_freq('回款单', True)
    jieba.suggest_freq('缺货单', True)
    jieba.suggest_freq('头信息', True)
    jieba.suggest_freq(('入库单', '头信息'), True)
    jieba.suggest_freq(('银行', '账号'), True)
    jieba.suggest_freq(('英文', '名称'), True)
    jieba.suggest_freq(('注册', '资本'), True)
    jieba.suggest_freq(('最新', '更新'), True)
    jieba.suggest_freq(('法人', '代表'), True)
    jieba.suggest_freq(('商品', '生产'), True)
    jieba.suggest_freq(('申请', '单'), True)
    jieba.suggest_freq(('销售', '业务'), True)
    jieba.suggest_freq(('会计', '科目'), True)
    jieba.suggest_freq(('计算', '公式'), True)
    jieba.suggest_freq(('客户', '关系'), True)
    jieba.suggest_freq(('移动', '电话'), True)
    jieba.suggest_freq(('其他', '费用'), True)
    jieba.suggest_freq(('异常', '情况'), True)
    jieba.suggest_freq(('注册', '商标'), True)
    jieba.suggest_freq(('中文', '名称'), True)
    jieba.suggest_freq(('营业', '执照'), True)
    jieba.suggest_freq(('注册', '资金'), True)
    jieba.suggest_freq(('利润', '总额'), True)
    jieba.suggest_freq(('数据', '编码'), True)
    jieba.suggest_freq(('客户', '档案'), True)
    jieba.suggest_freq(('邮政', '编码'), True)
    jieba.suggest_freq(('银行', '账号'), True)
    jieba.suggest_freq(('医疗', '器械'), True)
    jieba.suggest_freq(('产品', '类别'), True)
    jieba.suggest_freq(('经营', '品种'), True)
    jieba.suggest_freq(('公司', '地址'), True)
    jieba.suggest_freq(('提示', '信息'), True)
    jieba.suggest_freq(('个人', '账户'), True)
    jieba.suggest_freq(('数据', '类型'), True)
    # jieba.suggest_freq(('身份证', '号'), True)

    jieba.suggest_freq(('月', '销量'), True)
    jieba.suggest_freq(('总', '重量'), True)
    jieba.suggest_freq(('责任', '人员'), True)
    jieba.suggest_freq(('负责', '人'), True)
    jieba.suggest_freq(('会员', '卡'), True)
    jieba.suggest_freq(('明细', '单'), True)
    jieba.suggest_freq(('利润', '率'), True)
    jieba.suggest_freq(('销售', '部'), True)
    jieba.suggest_freq(('净利润', '率'), True)
    jieba.suggest_freq(('滞销', '品规'), True)
    # jieba.suggest_freq(('滞销', '品规', '月', '销量'), True)
    jieba.suggest_freq('品规', True)
    jieba.suggest_freq('时长', True)
    jieba.suggest_freq('门店', True)
    jieba.suggest_freq('不动销', True)
    jieba.suggest_freq('关联单', True)
    jieba.suggest_freq('申请单', True)

    jieba.suggest_freq(tuple(removed_n_field_named_list), True)


# 根据结巴分词的结果，去中英文对照表里找到对应的英文结果
def get_translate_result(jieba_result, mapping_dict):
    # for store eng words list
    temp_eng = []
    not_match_words = []
    for words in jieba_result:
        if words != "\n" and words != "_":
            # get the eng
            got_eng = mapping_dict.get(words)
            # judge got or not ,cause dict maybe don't have
            if str(got_eng) != "None":
                # store the one column
                temp_eng.append(mapping_dict.get(words))
            else:
                temp_eng.append(words)
                not_match_words.append(words)
    
    one_column_list = []
    for words in temp_eng:
        # replace space to _
        cleaned_words = str(words).replace(" ", "_")
        one_column_list.append(cleaned_words)

    result = '_'.join(one_column_list).replace("__", "_")
    return {
        'match_result': result,
        'no_match_result': not_match_words
    }
