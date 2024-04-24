// URL para compilar
//http://remix.ethereum.org/#appVersion=0.7.7&optimize=false&version=soljson-v0.4.11+commit.68ef5810.js

//ico rostcoins

//versão
pragma solidity ^0.4.11;
 
contract rostcoin_ico {
 
    //número máximo de rostcoins disponíveis no ICO		 
    uint public max_rostcoins = 1000000;
    //Taxa cotacao do rostcoin por dolar	
    uint public usd_to_rostcoins = 1000;
    //total de rostcoins compradas por investidores	
    uint public total_rostcoins_bought = 0;
    
    //funcoes de equivalencia
    mapping(address => uint) equity_rostcoins;
    mapping(address => uint) equity_usd;
 
    //verificando se o investidor por comprar rostcoins
    modifier can_buy_rostcoins(uint usd_invested) {
        require (usd_invested * usd_to_rostcoins + total_rostcoins_bought <= max_rostcoins);
        _;
    }
 
    //retorna o valor do investimento em rostcoins 	
    function equity_in_rostcoins(address investor) external constant returns (uint){
        return equity_rostcoins[investor];
    }
 
    //retorna o valor do investimento em dolares
    function equity_in_usd(address investor) external constant returns (uint){
        return equity_usd[investor];
    }
 
    //compra de rostcoins 
    function buy_rostcoins(address investor, uint usd_invested) external 
    can_buy_rostcoins(usd_invested) {
        uint rostcoins_bought = usd_invested * usd_to_rostcoins;
        equity_rostcoins[investor] += rostcoins_bought;
        equity_usd[investor] = equity_rostcoins[investor] / usd_to_rostcoins;
        total_rostcoins_bought += rostcoins_bought;
    }
 
    //venda de rostcoins
    function sell_rostcoins(address investor, uint rostcoins_sold) external {
        equity_rostcoins[investor] -= rostcoins_sold;
        equity_usd[investor] = equity_rostcoins[investor] / usd_to_rostcoins;
        total_rostcoins_bought -= rostcoins_sold;
    }
}
