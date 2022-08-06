# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vscode <vscode@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/06 09:31:02 by vscode            #+#    #+#              #
#    Updated: 2022/08/06 10:38:55 by vscode           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain
from distutils.log import debug
from flask import Flask, jsonify, request, render_template
import jsons as json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# al usar app.run debug true el servidor se ejecuta en modo debug y no en modo produccion y siempre se esta recagarando el servidor en cada cambio que hagamos
app.run(debug=True) # debug=True is for debugging purposes
