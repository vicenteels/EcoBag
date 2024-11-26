function showLoading(){
    const div = document.createElement("div");
    div.classList.add("loading");
    div.style.position = "fixed";
    div.style.top = "0";
    div.style.left = "0";
    div.style.width = "100%";
    div.style.height = "100%";
    div.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    div.style.display = "flex";
    div.style.justifyContent = "center";
    div.style.alignItems = "center";
    div.style.fontSize = "24px";
    div.style.color = "#fff";
  
    const label = document.createElement("label");
    label.innerText = "Carregando...";
  
    div.appendChild(label);
  
    document.body.appendChild(div);
  }

  function hideLoading(){
    const loadings = document.getElementsByClassName('loading');
    if (loadings.length){
      const loading = loadings[0];
      while (loading.firstChild) {
        loading.removeChild(loading.firstChild);
      }
      loading.remove();
    }
  }

function cadastrar(){
    window.location.href = "../cadastro"
}