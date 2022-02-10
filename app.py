import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

import matplotlib.pyplot as plt
from samila import GenerativeImage
from samila import Projection
from samila import VALID_COLORS
import random
from math import sin,cos

st.title('Pythonic 🐍 Generated Art 🎨')

st.markdown('More details about Samila can be found here -> [Samila Documentation](https://pypi.org/project/samila)')

fn1 = st.sidebar.selectbox('First EQ', ['sin','cos'])
fn2 = st.sidebar.selectbox('Second EQ', ['sin','cos'])

def f1(x,y):
    if fn1 == 'sin':
        result = random.uniform(-1,1) * x**2 - sin(y**2) + abs(y-x)
    elif fn1 == 'cos':
        result = random.uniform(-1,1) * x**2 - cos(y**2) + abs(y-x)
    return result

def f2(x,y):
    if fn2 == 'cos':
        result = random.uniform(-1,1) * y**3 - cos(x**2) + 2*x
    elif fn2 == 'sin':
        result = random.uniform(-1,1) * y**3 - sin(x**2) + 2*x
    return result

projections = st.sidebar.radio('Select the art projection here:',
                                options=['RECTILINEAR','POLAR','AITOFF','HAMMER', 'LAMBERT', 'MOLLWEIDE']
                                )

st.sidebar.markdown('**Color Selection**')

color = st.sidebar.selectbox('Art Color:', VALID_COLORS, index=30)

bgcolor = st.sidebar.selectbox('Background Color:', VALID_COLORS, index=15)

with st.spinner("Wait just a moment... It's working..."):
    g = GenerativeImage(f1,f2)
    g.generate()
    st.pyplot(g.plot(color=color, bgcolor=bgcolor, projection=eval('Projection.'+ projections)))
    st.caption('Seed value to regenerate this image is: ' + str (g.seed))
