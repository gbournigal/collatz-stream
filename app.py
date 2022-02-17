# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:57:31 2022

@author: georg
"""

import streamlit as st

st.header('Collatz App')
navega = st.sidebar.radio('Navegación:', options = ['About','Aplicación'])

def main():
    if navega == 'About':
        st.markdown(
            """Bienvenidos a este app para jugar un poco con el [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture#:~:text=The%20Collatz%20conjecture%20in%20mathematics%20asks%20whether%20repeating,term%20is%20one%20half%20of%20the%20previous%20term.).
            Gracias a Luis Eduardo Javier por referirme al tema."""
            )
        
        st.markdown("""De manera específica, la conjetura propone que en base a dos 
                    sencillas operaciones aritméticas cualquier número positivo 
                    será transformado a 1.""")
                    
        st.markdown("Los dos pasos a seguir son:")
        
        st.markdown("Si n es impar:")
        st.latex(r'''
                    3n + 1
                 ''')
                 
        st.markdown("Si n es par:")
        st.latex(r'''
                    n/2
                 ''')
                 
        st.markdown("""Repitiendo estos pasos de manera contínua para 
                    cualquier n positivo, siempre se alcanzará el número 1.
                    En el tab 'Aplicación' se permitirá colocar cualquier
                    número positivo y se arrojará información sobre la cadena
                    que se ejecuta.""")
    
    else:
        number = st.number_input('Ingrese un número positivo',
                        min_value = 1,
                        value = 1)
        
        if number > 999999999999999:
            st.markdown('Lo siento, de momento el número más alto permitido es 999,999,999,999,999')
        
        elif number > 0:
            
            st.markdown(f'Tu número es {number:,}')
            series = get_collatz_series(number)
            
            series_len = len(series) - 1
            
            numero_alto = max(series)
            
            st.text(f'El largo de la cadena es de {series_len} pasos.')
            st.text(f'El número más alto alcanzado es {numero_alto}.')
            
            st.text('La serie:')
            st.markdown(series)
        
        else:
            st.text('Lo siento superó el número límite del app.')


def get_collatz_series(number):
    series = []
    series.append(number)
    iteration = 0

    while min(series)!=1 and iteration < 1000:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = int(number*3 + 1)
        
        series.append(number)
        iteration = iteration + 1
    return series

if __name__ == '__main__':
    main()