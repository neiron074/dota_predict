# dota_predict
predict about 3 of 4 right results in hight skill professional dota matches 

take information about every professional game after 2018 year like who's win, order to pick heroes, duration, score, experience and more

create some statistics about game and heroes for every organisations at all for example mean game duration, mean gold per minute or mean score
some statistics of all heroes like experiece per minute, health or armor
the most important features founded on players statistics especially information about players_heroes like winrate, gold per minute
and last area is statistics about five man play together like winrate versus other five man and more, it's all around 230 features (130 heroes in dota)

on test data (data from the 'future' or data that i don't use for create statistics for features) i have about 75% accuracy
right now i test model on real data, while tournament of dota 2 is going on



json_information:
all mathces after 2018 from valve_api before cleaning and ready statistics after

frames:
ready data for model and test

doin_train_frame is engineering data

input_features_for_predict is python file for create features of unseen data

modeling is model for predict, manually input
