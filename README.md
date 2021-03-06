# LS-Project / Evaluate !

## Synopsis

Evaluate ! is a tool to evaluate different alternatives, by making a ranking from the best one to the worst.
Based on two documents to be attached : the first for the desired configuration (different weightings of the criteria) and the second for the data, you can apply one of the three evaluation methods available.

The client side is developed with jQuery and Bootstrap, and the server side with Python through Flask framework.

## Motivation

This project is part of the *M2 Miage ID* training at [Paris-Dauphine][] University.  


## Deploy

Make sure that you have **Python** (2.7) and **Flask** installed on your system. If not, please download them beforehand.  

Clone ProjetLS with `git clone https://github.com/SimoRihani/ProjetLS.git`
Then run the following :

	
	cd ProjetLS
	./Evaluate.sh
  
You can access the tool by going on your browser, localhost on port 5000/index : `localhost:5000/index`

Examples of input files are in the `csv/` directory (configuration and data). `csv/lycee/` contains files for high schools in Aquitaine region for the academic year 2015. `csv/cafet/` contains files for Coffee makers.

## License

This project is licensed under the GNU LGPL, Version 3.0. See LICENSE for full license text.

## Contributors

### Students

- Hamza *BOUKRIM* - Hamza.Boukrim@dauphine.eu
- Jasmin *DIANTOUBA* - Jasmin.Diantouba@dauphine.eu
- Oussama *DIBT* - Oussama.Dibt@dauphine.eu
- Mohammed *RIHANI* - Mohammed.Rihani@dauphine.eu

### Supervisor

- Brice *MAYAG* - Brice.Mayag@dauphine.fr



[Paris-Dauphine]: http://www.dauphine.fr/fr/index.html
