# greeting_card
conda create --name swe python=3.8.17
pip install django==4.1.7
pip install crispy-bootstrap5==0.7
django-bootstrap4         23.2
pillow                    10.0.0
pip install rembg==2.0.49

File "..\anaconda3\envs\nguhoc\lib\site-packages\pymatting\preconditioner\ichol.py", line 38:
def _ichol(
    <source elided>
    b = np.zeros(
        n, np.bool8

Change "bool8" to "bool_"
