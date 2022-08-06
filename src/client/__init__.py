# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vscode <vscode@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/06 09:31:02 by vscode            #+#    #+#              #
#    Updated: 2022/08/06 14:24:49 by vscode           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ft_import import *

app = Flask(__name__)


def router_index():
	@app.route('/')
	def index():
		return render_template('index.html')

# al usar app.run debug true el servidor se ejecuta en modo debug y no en modo produccion y siempre se esta recagarando el servidor en cada cambio que hagamos en el codigo
app.run(debug=True) # debug=True is for debugging purposes
