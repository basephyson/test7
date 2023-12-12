import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

a=st.number_input('a의 값을 입력하시오',value=2.0,step=1.0)
b=st.number_input('b의 값을 입력하시오',value=1.0,step=1.0)
c=st.number_input('c의 값을 입력하시오',value=15.0,step=1.0)
d=st.number_input('d의 값을 입력하시오',value=2000.0,step=100.0)

c1 = st.sidebar.radio('선의 색을 선택하시오',['red','green','blue','orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오.',['-','--',':','-.'])
m1 = st.sidebar.radio('점의 스타일을 선택하시오.',['o','s','h','p'])


love = []
y1 = []
y2 = []
for i in range(-29,31,3):
    love.append(i)
    y1.append(a*i*i+b*i+c)
    y2.append(i/d)




plt.plot(love, y1, color = c1, linestyle = s1, marker = m1 )
plt.plot(love, y2, color = c1, linestyle = s1, marker = m1 )
st.pyplot(fig)


# x = []
# y2 = []
# for i in range(-29,31,3):
#     x.append(i)
#     y2.append(i/d)

# plt.plot(x, y2, color = c1, linestyle = s1, marker = m1 )
# st.pyplot(fig)















import sys
sys.exit()
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("blue")
t.begin_fill()
t.circle(200)
t.end_fill()
t.forward(200)
turtle.done()

