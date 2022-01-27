def filter_data_from_range_list(data, range_list):
    """
    从多个区间列表中筛选符合条件的数据
    :param data:
    :param range_list:
    :return:
    """
    if range_list:
        for range in range_list:
            if len(range) == 2:
                left, right = range[0], range[1]
                if left and right and left <= data and data < right:
                    return True
                if left and not right and left <= data:
                    return True
                if right and not left and data < right:
                    return True
        return False
    else:
        return True

    # range_l = [(None, 5), (20, 50)]
    # datas = [1, 2, 3, 20, 30, 50, 100, 150]
    # res = filter(lambda seq: filter_data_from_range_list(seq, range_l), datas)
    # print(list(res))
