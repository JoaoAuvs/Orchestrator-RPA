let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();//calling the function(optional)
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
    } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");//replacing the iocns class
    }
}

/* FORMATA A COLUNA DE ACORDO COM O RESULTADO DO STATUS DA API */
function condicional() {
    var tds = document.getElementsByTagName("td");
    var tr = document.getElementsByTagName("tr");
    var submitButton = document.getElementById("submitButton");
    for (i = 0; i < tds.length; i++) {
        if (tds[i].innerHTML == "OPERANTE") {
            tds[i].style.background = "#19d16a";
        }
        else if (tds[i].innerHTML == "FALHOU") {
            tds[i].style.background = "#f00";
        }
        else if (tds[i].innerHTML == "EM MANUTENÇÃO") {
            tds[i].style.background = "#f9ca3f";
        }
        else if (tds[i].innerHTML == "EXECUTANDO") {
            tds[i].style.background = "#f9ca3f";
        }
    }
}

$(document).ready(function () {
    $('#table-lista').DataTable({
        responsive: true, /* FORMATAR TABELA RESPONSIVA */
        update: true, /* ATUALIZAR TABELA */
        /* searching: false,  DESATIVA BUTTON DE PESQUISA */
        "iDisplayLength": 25, /* QUANTIDADE DE REGISTROS POR PÁGINA */
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json"
        }
    });
});