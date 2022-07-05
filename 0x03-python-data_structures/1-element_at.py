def element_at(my_list, idx):
    for item in range(len(my_list)):
        if idx == item and idx > 0:
            return(my_list[item])
        elif idx == item and idx < 0:
            return(None)
        elif idx > len(my_list) - 1:
            return(None)
