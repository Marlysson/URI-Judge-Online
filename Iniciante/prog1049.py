# -*- coding:utf8 -*-

dados = {
	'vertebrado':{
		'ave':{
			'carnivoro':'aguia',
			'onivoro':'pomba'
		},
		'mamifero':{
			'onivoro':'homem',
			'herbivoro':'vaca'
		}
	},

	'invertebrado':{
		'inseto':{
			'hematofago':'pulga',
			'herbivoro':'lagarta'
		},
		'anelideo':{
			'hematofago':'sanguessuga',
			'onivoro':'minhoca'
		}
	}
}


palavra1 = input('')
palavra2 = input('')
palavra3 = input('')

print('{}'.format(dados.get(palavra1).get(palavra2).get(palavra3)))