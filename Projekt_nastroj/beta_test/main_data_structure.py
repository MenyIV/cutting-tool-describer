tool_program_data = {"N1 vrtak":{
                            "picture_name":"Drill",
                            "picture_suffix":".png",
                            "picture_category":"pic_mill_tool",

},
                   "N2 freza-valcova":{
                            "picture_name":"Flat_End_Mill",
                            "picture_suffix":".png",
                            "picture_category":"pic_mill_tool",

},
                    "N3 Srazec":{
                            "picture_name":"Counter_sink",
                            "picture_suffix":".png",
                            "picture_category":"pic_mill_tool",

},
                     "N4 turn test":{
                            "picture_name":"CV",
                            "picture_suffix":".png",
                            "picture_category":"pic_turn_insert",

},
}

tooldata_nesteddict = {        "N1":({
                                            "Name":"",
                                            "Výrobce":"",
                                            "D1":"",
                                            "L1":"",
                                            "L2":"",
                                            "A":"",
                                            "":"",
                                            "Poznámka":"",
                                            },
                                        {   "picture_name":"CV",
                                            "picture_suffix":".png",
                                            "picture_category":"pic_turn_insert",
                                            }),
                      
                       
                    "N2 freza-valcova":{
                            "Name":"",
                            "Výrobce":"",
                            "D1":"",
                            "L1":"",
                            "L2":"",
                            "Zubů":"",
                            "":"",
                            "Poznámka":"",
},
                    "N3 Srazec":{
                            "Name2":"",
                            "Výrobce":"",
                            "D2":"",
                            "":"",
                            "Poznámka":"",
                            
},             
                    "N4 turn test":{
                            "Name2":"",
                            "Výrobce":"",
                            "D2":"",
                            "D5":"",
                            "D7":"",
                            "":"",
                            "Poznámka":"",
},   
                    
}

print (tooldata_nesteddict("N1"))