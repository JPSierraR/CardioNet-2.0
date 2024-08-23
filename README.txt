 _______   ________   ______   _______   __       __  ________ 
|       \ |        \ /      \ |       \ |  \     /  \|        \
| $$$$$$$\| $$$$$$$$|  $$$$$$\| $$$$$$$\| $$\   /  $$| $$$$$$$$
| $$__| $$| $$__    | $$__| $$| $$  | $$| $$$\ /  $$$| $$__    
| $$    $$| $$  \   | $$    $$| $$  | $$| $$$$\  $$$$| $$  \   
| $$$$$$$\| $$$$$   | $$$$$$$$| $$  | $$| $$\$$ $$ $$| $$$$$   
| $$  | $$| $$_____ | $$  | $$| $$__/ $$| $$ \$$$| $$| $$_____ 
| $$  | $$| $$     \| $$  | $$| $$    $$| $$  \$ | $$| $$     \
 \$$   \$$ \$$$$$$$$ \$$   \$$ \$$$$$$$  \$$      \$$ \$$$$$$$$
                                                               
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                          
                 Juan Sierra - Jesus Gamboa - Jorge Castro
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Descripción

	Este proyecto es básicamente un ejemplo de las distintas formas de desplegar un modelo de aprendizaje automático.
	Para este caso, usando Python y el microframework Flask para aplicaciones web y enlace entre página y base de datos logramos:

		- Desplegar un modelo de aprendizaje automático.
		- Interactuar con una base de datos para la gestión de datos de pacientes.
		- Crear una interfaz de usuario web amigable utilizando HTML y CSS.
		- Generar y mostrar códigos QR para la identificación de pacientes.
		- Implementar funcionalidades de registro, búsqueda y predicción para pacientes.

Requisitos:

	- numpy==1.26.4
	- scikit-learn==1.2.2 
	- Flask
	- pickle 
	- pandas 
	- Xampp ==> (Programa, debe descargarse por aparte en internet) << https://www.apachefriends.org/download.html >> *Obligatorio tener servicio apache y mysql


Para instalar todo ingresar a una ventana de comandos y dirigirse a la ruta
donde se aloja requirements.txt e ingresar en la consola:

			<< pip install -r requirements.txt >> 


Para lanzar servicio solo se necesita ejecutar << app.py >> y se montara en << localhost:5000 >>

    _   _____   _____ ___ _____ ___ _  _  ___ ___   _   _    _    _    _ 
   /_\ |   \ \ / / __| _ \_   _| __| \| |/ __|_ _| /_\ | |  | |  | |  | |
  / _ \| |) \ V /| _||   / | | | _|| .` | (__ | | / _ \|_|  |_|  |_|  |_|
 /_/ \_\___/ \_/ |___|_|_\ |_| |___|_|\_|\___|___/_/ \_(_)  (_)  (_)  (_)

                                                                                        
  *Nota_1_: Es posible que al descargar el scikit-learn 1.2.2 y demás, se produzcan unos problemas
	    Relacionados con Microsoft C++ Build tools. Es por lo anterior que recomiendo el siguiente video
	    Que puede arreglar ese problema.

		- https://youtu.be/gzRBH726vUs?si=O3oI80HMPCgm3_JL


*Nota_2_: La razón por la cual se usa una version especifica de Scikit-learn es por ser la que misma
	  que tiene google colab, entorno donde se entrenó el modelo.


*Nota_3_: Scikit-learn 1.2.2 presenta problemas de compatibilidad con numpy 2.0 por lo que se recomienda 
	  usar versiones por debajo de esta.
	  
	  - Puede verificar la compatibilidad en: https://scikit-learn.org/stable/whats_new/v1.2.html#

	  - Aqui puede verificar versiones minimas compatibles con Scikit-learn: https://scikit-learn.org/1.2/install.html


*Nota_4_: Es recomendable guardar el proyecto dentro de la carpeta httdocs de xampp.      


*Nota_5_: La llave maestra que se pide en el formulario de registro de usuario es <<  CardioNet  >>, copie y pegue si es necesario.     


**Nota__6__: Se debe crear una base de datos en mysql llamada "db2", 2 tablas llamadas "users" y "pacientes", adicional a esto
	     un usuario con privilegios para bases de datos en mysql. mas informacion en el documento.
	     



                                                   
                                                                                                                                                                                             
                                                                                                    
       .^^~:                                                                           ^~.          
        .!Y5Y?7:                                                                    ::~J?           
          ~7YG?                                                                     7Y!7:           
         .^J7?Y.                                                                   .!?Y^            
         :JY5G57:                                                                 .~!J5.            
          .7Y5GG?:                                                                !JYPYJ            
           .~J5P5Y7!^::                                                          ^?JYPJ~            
             .7YYPY?Y!:                                                         ^Y555J.             
               .?5PJY7^                                                        .?PBGJ.              
                .~Y5JJY7                                                      .!5GG7                
                  :?JPYJ?:                                                    ~JGBJ                 
                    ^Y?5P5^                              ....                !YGB5.                 
                     . .~Y5?^                         :77!7??!             .!JYPY:                  
                         .?55YJ?~                    .!J?7??7P~           .7?57.                    
                           ~?JPP5:                   .!!!!!J?J7         :~?!7P7.                    
                            !Y5YGP?~                 .!!!~77?7:        .J5J5GGGYJJ?????JJ??7!!^^.   
                             ^JJYPPP?^.               ^~^!??:          :JYYY7~:^^^::::::^~~~!7?J:   
                              :55PPY:^^^~^~.           !7?Y?.         ^J?7J!                        
                              .?5Y5P!   .:!7!:...:::::~?!!7?7~~!~~^   75?:7:                        
                              .^?75PP7:     :~7!!?!~~~~~!!!!??77~!!. .Y5?:~                         
                            .:^!!5PYYPP?     .^7??!~~~~!!!!!7Y5!:^^^.!YY7^!~:                       
                           :~~~^!?~..~YP!   .^7Y!!77~^^!!!!!7JY. .^:~Y57:^~7~                       
                           ^~^^!??     ?PY!^!757~^^!7!~~~^~!7JJ.   ::7GG!:^~~                       
                            .:^!77^    ^5BBP7.^~^^JYJ?7!~^^!7?7     ::!?^^~~.                       
                               .:~7!::.7GGJ.  ^~~5PY?7!!77!!7?^      .^~^~~.                        
                                  .:^!7JYY.  .~?YG5J?!!7JJ????.      :!!~~.                         
                                      .^~. .~7?GGGPJ77?J?5?7JJ.      .:::.                          
                                         :^~?5?7J5Y!7?YJ?J77!!7.                                    
                                       .:::^~~77!!7!?Y77?!7!^:~?^                                   
                                   ..:::::^^:^~!7?7!!JJ?~~^^:::!7^:.                                
                                ..::^^:..     :^^^!!~^7!..   ..:7~:::.                              
                             ..::^^:.                           ^?!.:::.                            
                          .::::^:..                                 ::::^.                          
                       .:^^::^:.                                      :::^^.                        
                     :^!!~^~^.                                          .::^^:.                     
                     :~!!!!^                                             .::^~!~:                   
                      ~!~!!                                               :~^^~~!^                  
                      .::!?!:.                                             .:~!!!^.                 
                          .~777.                                             .^!~^.                 
                         .^~!7?!:                                            .~7^                   
                     .^~!!!^..                                               ^!7~.                  
                    .::::..                                                 :~!!!~^:                
                                                                             .. .^~~^^:.            
                                                                                                 		
	                  _                      _____ _                     
		         | |                    / ____(_)                    
		         | |_   _  __ _ _ __   | (___  _  ___ _ __ _ __ __ _ 
		     _   | | | | |/ _` | '_ \   \___ \| |/ _ \ '__| '__/ _` |
		    | |__| | |_| | (_| | | | |  ____) | |  __/ |  | | | (_| |
		     \____/ \__,_|\__,_|_| |_| |_____/|_|\___|_|  |_|  \__,_|

				       j.sierrarios9930@gmail.com
                                                                                                    
