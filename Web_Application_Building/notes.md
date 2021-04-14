#### Single Page Application

> - HTML, CSS si JS sunt trimise o singura data la încărcarea paginii
> - Cu ajutorul JavaScript se poate remodifica structura paginii web (DOM-ul)
>

#### MVC - Model View Controller

> 3 components:
> - Model(Objective JavaScript)
> - View(HTML-CSS)
> - Controller (JavaScript)

### Static Content

> - Conținutul static al unui website este conținut distribuit
    > la client în aceeași formă în care există pe server
> - Conținut static sunt: pagini HTML/CSS, imagini, fișiere
    > textuale etc.
> - Pentru distribuția conținutului serverul trebuie să aibă
    > posibilitatea de a citi cererile HTTP și lucrul cu sistemul
    > de fișiere
> - Elementele modulului http.server au implicit această
    > posibilitate

## BaseHTTPRequestHandler

> - Proprietăți
    >
- path (calea cererii)
>    - headers (antetul cererii)
>    - wfile (flux de ieșire)
>    - rfile (flux de intrare)
> - Metode
    >
- do_GET (cererea get)
>    - do_POST (cererea post)