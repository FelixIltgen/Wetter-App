
class Style_Sheet:
    
    css_content = """
    /*Test*/
    #weatherApp{
        background-color: #d1be99;
    }
    #weatherApp_cloud_sun{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(209, 176, 92), 
                                            stop: 1 rgb(95, 105, 123) );     
    }
    #weatherApp_DarkCloud{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(135, 151, 172), 
                                            stop: 1 rgb(61, 68, 81) );     
    }
    #weatherApp_LightCloud{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(210, 210, 210), 
                                            stop: 1 rgb(95, 106, 126) );     
    }
    #weatherApp_Rain{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(155, 202, 213), 
                                            stop: 1 rgb(43, 98, 104) );     
    }
    #weatherApp_Thunder{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(180, 180, 180), 
                                            stop: 1 rgb(49, 49, 48) );
    }
    #weatherApp_Sun{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(132, 239, 255), 
                                            stop: 1 rgb(250, 158, 11) );
        
    }
    #input_field, button_search{   
        border: 3px solid black;
        border-radius: 20px;
        padding: 10px 15px 10px 15px;
        margin: 10px 50px 10px 50px;
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px
    }
    #button_search{
        border: 3px solid black;
        border-radius: 20px;
        padding: 10px 15px 10px 15px;
        margin: 10px 50px 20px 50px;
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px;
        background-color:rgb(246, 186, 23);
    }
    
    #button_search:hover {
        background-color:rgba(246, 187, 23, 0);
    }
    
    #output_label{
        border-radius: 10px;
        color: white;
        font-family: Comic Sans MS;
        font-size: 25px;
        background-color: rgba(224, 222, 224, 0.37);
        padding: 10px;
        margin: 20px 0px 0px 0px;
    }
    
    
    """