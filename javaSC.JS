function calcularNivelRank(vitorias, derrotas) {//def
    let saldoVitorias = vitorias - derrotas;  //saldo
    let nivel;
    if (vitorias < 10) {
        nivel = "Ferro";
    } else if (vitorias <= 20) {
        nivel = "Bronze";
    } else if (vitorias <= 50) {
        nivel = "Prata";
    } else if (vitorias <= 80) {
        nivel = "Ouro";
    } else if (vitorias <= 90) {
        nivel = "Diamante";
    } else if (vitorias <= 100) {
        nivel = "Lendário";
    } else {
        nivel = "Imortal";
    }

    console.log(`O Herói tem de saldo de ${saldoVitorias} está no nível de ${nivel}`);
}


let vitorias = parseInt(prompt("Digite o número de vitórias: "));
let derrotas = parseInt(prompt("Digite o número de derrotas: "));


calcularNivelRank(vitorias, derrotas);
