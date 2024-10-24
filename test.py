from models import PlayerModel

new_model= PlayerModel()

new_model.addata([23,4,56,12,34,12,67,89],[0,0,1,0],False,False)
new_model.addata([21,4,55,12,34,10,67,89],[0,0,1,0],False,False)
new_model.addata([13,56,6,2,4,42,7,9],[0,1,0,0],False,False)
new_model.train()
new_model.addata([13,56,6,2,4,42,7,9],[0,1,0,0],False,False)
new_model.train()
print(new_model.move([[13,56,6,2,4,42,7,9]]))





