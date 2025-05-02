# Death-location

**Death-location** é um script ético e educativo feito em Python, desenvolvido por #By Dark [tubas-dark](https://github.com/tubas-dark), que permite:

- Localizar números de telefone
- Ver informações detalhadas de IPs públicos
- Obter seu próprio IP local e IP público
- Interface em terminal com menu estilizado e colorido (ideal para Termux)

---

## ⚙️ Funcionalidades

- **[1] Localizar número**  
  Mostra país, operadora, tipo de linha e localização aproximada usando a API Numverify.

- **[2] Localizar IP**  
  Mostra cidade, país, região, provedor, coordenadas (lat/lon) de um IP público.

- **[3] IP Location**  
  Exibe automaticamente o IP **público** e o **IP local** do dispositivo, com geolocalização completa.

## ‼️ Install 
Requisitos
Python 3.x (recomendado 3.10+)
Termux ou terminal Linux
Pip instalado
Conexão com internet

```bash 

git clone https://github.com/tubas-dark/Death-location.git
cd Death-location
pip install -r requirements.txt
python main.py

