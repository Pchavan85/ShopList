#Shop List
shop_list = ["Banana", "clothes", "soap", "food", "Ice-cream"]
print("Initial shop_list:", shop_list)          #print(type(shop_list)) to check data type
#new variable
item_tocheck = str(input('Enter the item: '))
print("item_tocheck:", item_tocheck)
# item does Not Exists
if item_tocheck not in shop_list:
      print("Item does not exists","\n","Then add This item to shop list")
      shop_list.append(item_tocheck)
# item Exists                
else:
      print("Item exists in list","\n","Then Delete this item")
      if item_tocheck in shop_list:
            #print(shop_list)
            #print(shop_list.index('Banana'))
            shop_list.remove(item_tocheck)
            shop_list.append(str(input('Enter new item: ')))       
print("updated list: ", shop_list)
