
class Style_Sheet:
    
    css_content = """
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
    
    /*-------------------Forecast------------------*/
    
    #weatherApp_cloud_sun_Forecast{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(209, 176, 92), 
                                            stop: 1 rgb(95, 105, 123) );
        border: 3px solid black;
        border-radius: 20px;    
    }
    #weatherApp_DarkCloud_Forecast{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(135, 151, 172), 
                                            stop: 1 rgb(61, 68, 81) );
        border: 3px solid black;
        border-radius: 20px;    
    }
    #weatherApp_LightCloud_Forecast{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(210, 210, 210), 
                                            stop: 1 rgb(95, 106, 126) );
        border: 3px solid black;
        border-radius: 20px;     
    }
    #weatherApp_Rain_Forecast{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(155, 202, 213), 
                                            stop: 1 rgb(43, 98, 104) );
        border: 3px solid black;
        border-radius: 20px;     
    }
    #weatherApp_Thunder_Forecast{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(180, 180, 180), 
                                            stop: 1 rgb(49, 49, 48) );
        border: 3px solid black;
        border-radius: 20px;
    }
    #weatherApp_Sun_Forecast{
        background-color: qlineargradient(  x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 rgb(132, 239, 255), 
                                            stop: 1 rgb(250, 158, 11) );
        border: 3px solid black;
        border-radius: 20px;  
    }
    #weather_date{
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px
        
    }
    #weather_info{
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px
        
    }
    #weather_temp{
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px
    }
    
    #input_field{   
        border: 3px solid black;
        border-radius: 20px;
        padding: 10px 15px 10px 15px;
        margin: 10px 20px 10px 20px;
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px
    }
    #input_field_wrong{
        background-color: #d6746d;
        border: 3px solid black;
        border-radius: 20px;
        padding: 10px 15px 10px 15px;
        margin: 10px 20px 10px 20px;
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px
    }
    
    #button_search, #button_forecast, #button_back{
        border: 3px solid black;
        border-radius: 20px;
        padding: 10px 15px 10px 15px;
        margin: 10px 20px 20px 20px;
        font-family: Comic Sans MS;
        font-weight: bold;
        font-size: 20px;
        background-color:rgb(246, 186, 23);
    }
    
    #button_search:hover, #button_forecast:hover, #button_back:hover{
        background-color:rgba(246, 187, 23, 0);
    }
    
    #time_label{
        border-radius: 10px;
        color: white;
        font-size: 100px;
        font-weight: bold;
        background-color: rgba(224, 222, 224, 0.37);
        padding: 10px;
        margin: 20px 0px 0px 0px;
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
    #wetterbild{
         padding: 0px 100px 0px 100px;
    }
    """