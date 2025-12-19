# Markdown
https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax  
https://www.markdownguide.org/basic-syntax/  

---

[Links](http://i_dont_like_this.com)

# heading 1

## heading 2

heading 1
=========

heading 2
---------

```
Codeblock
```

```python
def format_codeblock(using = "```python"):
    print("This is Python")
```

> Blockquote
> next line
> 
> next line after paragraph


<!-- Comment --> 
comments like in HTML: "\<!-- Comment -->"

horizontal line by using "---"

---

Text  
2 trainling Spaces for line break <br>  

blank line for Paragraphs (<p></p>)

*italic*  
**bold**  
***bold italic***  

_italic_  
__bold__  
___bold italic___  

---

# LaTeX for Math equations

https://www.latex-project.org/

https://de.wikipedia.org/wiki/LaTeX

https://wiki.ubuntuusers.de/LaTeX/

https://de.overleaf.com/gallery/tagged/cheat-sheet

Jupyter Notebook uses MathJax to render LaTeX formulas

https://www.mathjax.org/

Examples:

https://jupyterbook.org/en/stable/content/math.html

https://sakurachaojun.github.io/PSYO3505/others/latex.html

https://www.datacamp.com/cheat-sheet/latex-cheat-sheet

https://medium.com/@saadsaeed85/a-primer-in-using-latex-in-jupyter-notebooks-ef23716cd103

https://www.underleaf.ai/learn/latex/vectors


## Examples of LaTeX Math equation

inline math: $ \pi $

math blocks:
$$
f(x) = a_1 x^2 + a_2 x + a_3
$$

$$
d = \sqrt[2]{x^2+y^2}
$$

$$f(x) = \sum_{i=0}^{N} \int_{a}^{b} g(t,i) \text{d}t \tag{a}$$

$$
\int \frac{1}{x} dx
$$

LaTeX-style blocks (\\begin .. \\end):
$$
\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
$$

Vectors:
$$
\vec{v} = \vec{v_1}[0] * \hat{\imath} + \vec{v_1}[1] * \hat{\jmath}
$$

Matrices:
$$
\left [
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
\right ] \tag{3-3}
$$

$$
\begin{bmatrix}
1 & 2 & \cdots & 4 \\
7 & 6 & \cdots & 5 \\
\vdots & \vdots & \ddots & \vdots \\
8 & 9 & \cdots & 10
\end{bmatrix} \tag{3-8}
$$

