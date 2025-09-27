from bdshare import get_hist_data

# df = get_hist_data('2025-01-01','2025-01-02') # get all instrument data
# print(df.to_string())

df = get_hist_data('2025-01-01','2025-01-17','GP') # get specific instrument data
print(df.to_string())
share_values = df['value'].to_list()
print(share_values)
maximum = float('-inf')
positive_list = []

share_values = list(map(float, share_values))

flag = False
for i in range(len(share_values)-1):
    if share_values[i]<=share_values[i+1]:
        maximum = share_values[i+1]
        flag = True
    else:
        flag = False

    if flag==False:
        positive_list.append(maximum)
positive_list = set(positive_list)
print("The High Stock Values :",positive_list)
print("The number of positive count :",len(positive_list))