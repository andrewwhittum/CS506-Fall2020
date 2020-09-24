def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    # initialize a list that will contain lists for each line
    ret = []

    # read the lines in the file
    with open(csv_file_path, "r") as f:
        lines = f.readlines()

        # go through each line and remove the commas, store each entry in a list
        for line in lines:
            list_of_strings = line.split(",")
            list_of_values = []

            # iterate through items in the list we just generated
            for item in list_of_strings:
                # try to cast items an int, add it to a new list
                try:
                    v = int(item)
                    list_of_values.append(v)
                except ValueError: 
                    # try to cast the item as a float, add to new list
                    try:
                        v = float(item)
                        list_of_values.append(v)
                    #remove leading and trailing quotes, add the variable as a string, add to new list
                    except ValueError:
                        v = item.strip('"')
                        list_of_values.append(v)
            # when each line is fully processed, add that list to overal list
            ret.append(list_of_values)

    return ret
            